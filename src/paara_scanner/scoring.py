"""PAARA seven-factor scoring rule.

Rule (highest-severity condition met, not a sum) — from the PAARA
Connector Audit Kit README:

- **Critical** — F7 and any of F1, F3, F4
- **High** — F7, or two or more of F1-F5
- **Moderate** — one High-weighted factor (one of F1-F5), or multiple
  Medium-weighted factors
- **Low** — otherwise

Because U is not evidence of absence, every connector is scored
twice: a lower bound with U treated as N, and an upper bound with
U treated as Y. A restricted configuration (a documented
write-limiting control applied, F7 set to N) is scored the same way.

Note on "multiple Medium factors": F6 is the only Medium-weighted
factor in the seven-factor set, so that branch can never fire on its
own; a lone F6 does not reach Moderate. This is documented rather
than silently treated as Moderate.
"""

from __future__ import annotations

from .models import (
    Connector,
    Factor,
    FactorCode,
    ScoreLevel,
    ScoreResult,
)

HIGH_FACTORS = (Factor.F1, Factor.F2, Factor.F3, Factor.F4, Factor.F5)
MEDIUM_FACTORS = (Factor.F6,)


def resolve(codes: dict[Factor, FactorCode], unknown_as_yes: bool) -> dict[Factor, bool]:
    """Resolve Y/N/U codes to booleans under one bounding assumption."""
    resolved: dict[Factor, bool] = {}
    for factor, code in codes.items():
        if code is FactorCode.YES:
            resolved[factor] = True
        elif code is FactorCode.NO:
            resolved[factor] = False
        else:  # UNKNOWN
            resolved[factor] = unknown_as_yes
    return resolved


def score_single(resolved: dict[Factor, bool]) -> tuple[ScoreLevel, str]:
    """Score one resolved (all-boolean) factor set. Returns (level, reason)."""
    f = resolved
    if f[Factor.F7] and (f[Factor.F1] or f[Factor.F3] or f[Factor.F4]):
        triggers = [x.value for x in (Factor.F1, Factor.F3, Factor.F4) if f[x]]
        return ScoreLevel.CRITICAL, (
            f"F7 (write/action) with {', '.join(triggers)}"
        )
    if f[Factor.F7]:
        return ScoreLevel.HIGH, "F7 (write/action) alone"
    high_count = sum(1 for factor in HIGH_FACTORS if f[factor])
    if high_count >= 2:
        present = [x.value for x in HIGH_FACTORS if f[x]]
        return ScoreLevel.HIGH, (
            f"{high_count} High-weighted factors: {', '.join(present)}"
        )
    if high_count == 1:
        present = [x.value for x in HIGH_FACTORS if f[x]][0]
        return ScoreLevel.MODERATE, f"one High-weighted factor: {present}"
    medium_count = sum(1 for factor in MEDIUM_FACTORS if f[factor])
    if medium_count >= 2:  # Unreachable with a single Medium factor; kept for completeness.
        return ScoreLevel.MODERATE, "multiple Medium-weighted factors"
    return ScoreLevel.LOW, "no High-weighted factor and no write/action capability"


def score_connector(connector: Connector) -> ScoreResult:
    """Score a connector under both bounds, plus restricted if applicable."""
    lower_resolved = resolve(connector.codes, unknown_as_yes=False)
    upper_resolved = resolve(connector.codes, unknown_as_yes=True)
    lower, lower_reason = score_single(lower_resolved)
    upper, upper_reason = score_single(upper_resolved)

    reasons = [
        f"lower bound ({_bound_label(False)}): {lower.value} — {lower_reason}",
        f"upper bound ({_bound_label(True)}): {upper.value} — {upper_reason}",
    ]
    unknowns = [f for f, c in connector.codes.items() if c is FactorCode.UNKNOWN]

    restricted_lower = restricted_upper = None
    if connector.has_write_limiting_control:
        restricted_codes = dict(connector.codes)
        restricted_codes[Factor.F7] = FactorCode.NO
        r_lower, r_lower_reason = score_single(
            resolve(restricted_codes, unknown_as_yes=False)
        )
        r_upper, r_upper_reason = score_single(
            resolve(restricted_codes, unknown_as_yes=True)
        )
        restricted_lower, restricted_upper = r_lower, r_upper
        reasons.append(
            f"restricted (F7=N): {r_lower.value} -> {r_upper.value} "
            f"— lower: {r_lower_reason}; upper: {r_upper_reason}"
        )

    return ScoreResult(
        name=connector.name,
        code_string=connector.code_string(),
        lower=lower,
        upper=upper,
        restricted_lower=restricted_lower,
        restricted_upper=restricted_upper,
        reasons=reasons,
        unknowns=unknowns,
    )


def _bound_label(unknown_as_yes: bool) -> str:
    return "U as Y" if unknown_as_yes else "U as N"

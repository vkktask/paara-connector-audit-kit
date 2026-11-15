"""Data model for PAARA connector scoring.

Factor definitions follow the PAARA Connector Audit Kit README:
F1-F5 are High-weighted, F6 is Medium-weighted, F7 is
Critical-weighted. F4 is coded Y when documentation states logging
is absent, N when it documents logging, U when it is silent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FactorCode(str, Enum):
    """Y = documented present, N = documented absent, U = undocumented."""

    YES = "Y"
    NO = "N"
    UNKNOWN = "U"

    @classmethod
    def parse(cls, value: str) -> "FactorCode":
        value = str(value).strip().upper()
        for member in cls:
            if value == member.value:
                return member
        raise ValueError(f"invalid factor code {value!r}: expected Y, N or U")


class Factor(str, Enum):
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"


FACTOR_LABELS = {
    Factor.F1: "Sensitive-data reach",
    Factor.F2: "Cross-system aggregation",
    Factor.F3: "Non-user-bound credentials",
    Factor.F4: "Absent logging",
    Factor.F5: "Prompt-injection exposure",
    Factor.F6: "External sharing",
    Factor.F7: "Agentic action capability",
}

# Weight used by the scoring rule (see scoring.py).
FACTOR_WEIGHTS = {
    Factor.F1: "High",
    Factor.F2: "High",
    Factor.F3: "High",
    Factor.F4: "High",
    Factor.F5: "High",
    Factor.F6: "Medium",
    Factor.F7: "Critical",
}

FACTOR_ORDER = list(Factor)


class ScoreLevel(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    CRITICAL = "Critical"


@dataclass
class Connector:
    """One connector with its seven factor codes and provenance."""

    name: str
    codes: dict[Factor, FactorCode]
    connector_type: str = ""
    documentation_retrieved: str = ""
    has_write_limiting_control: bool = False
    # Expected scores from the published audit, used by the test suite
    # and by `paara_scanner audit --check`. Empty when not applicable.
    expected_default: tuple[str, str] = ("", "")
    expected_restricted: tuple[str, str] = ("", "")

    def code_string(self) -> str:
        """Seven-character code string in F1-F7 order, e.g. ``UNUUYNY``."""
        return "".join(self.codes[f].value for f in FACTOR_ORDER)

    @classmethod
    def from_code_string(
        cls, name: str, code_string: str, **kwargs
    ) -> "Connector":
        code_string = code_string.strip().upper()
        if len(code_string) != 7 or any(c not in "YNU" for c in code_string):
            raise ValueError(
                f"invalid code string {code_string!r}: "
                "expected 7 characters from Y, N, U in F1-F7 order"
            )
        codes = {
            factor: FactorCode.parse(ch)
            for factor, ch in zip(FACTOR_ORDER, code_string)
        }
        return cls(name=name, codes=codes, **kwargs)


@dataclass
class ScoreResult:
    """Scores for one connector under both bounding assumptions."""

    name: str
    code_string: str
    lower: ScoreLevel
    upper: ScoreLevel
    restricted_lower: ScoreLevel | None = None
    restricted_upper: ScoreLevel | None = None
    reasons: list[str] = field(default_factory=list)
    unknowns: list[Factor] = field(default_factory=list)

    @property
    def band(self) -> str:
        return f"{self.lower.value} -> {self.upper.value}"

    @property
    def restricted_band(self) -> str | None:
        if self.restricted_lower is None or self.restricted_upper is None:
            return None
        return f"{self.restricted_lower.value} -> {self.restricted_upper.value}"

    def decision(self) -> str:
        """Deployment decision from the upper (unfavourable) bound.

        The upper bound is the conservative basis for a decision: approval
        on the favourable assumption relies on facts nobody has verified.
        """
        return {
            ScoreLevel.CRITICAL: "Defer — do not approve in this configuration",
            ScoreLevel.HIGH: (
                "Restrict — approve only with write-limiting controls "
                "and conditions"
            ),
            ScoreLevel.MODERATE: "Approve with conditions",
            ScoreLevel.LOW: "Approve with routine monitoring",
        }[self.upper]

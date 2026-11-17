#!/usr/bin/env python3
"""PAARA Connector Audit — thin MCP server wrapper (stdio, stdlib only).

Exposes the PAARA seven-factor connector scoring rule and the published
13-connector audit dataset as MCP tools, speaking JSON-RPC 2.0 over
stdin/stdout (newline-delimited), with no third-party dependencies.

Tools:
  score_connector   Score any connector from its F1-F7 codes (Y/N/U).
  lookup_connector  Look up one of the 13 coded connectors by name.
  list_connectors   List the 13 coded connectors with their bands.

Scoring: if the PAARA Connector Audit Kit's `paara_scanner` package is
importable (via $PAARA_KIT_SRC or a sibling ../paara-repo checkout), its
scoring module is used directly. Otherwise an exact local replica of the
kit's scoring rule (src/paara_scanner/scoring.py) is used, so this file
also works standalone. The test suite verifies the replica against the
published bands for all 13 connectors.

Methodology: Kumar, V. (2026). Privacy-Aware AI Risk Architecture
(PAARA). SSRN. https://doi.org/10.2139/ssrn.6784078
Kit: https://github.com/vkktask/paara-connector-audit-kit
Archived kit + dataset: https://doi.org/10.5281/zenodo.24325766
"""

from __future__ import annotations

import csv
import difflib
import json
import os
import sys
from pathlib import Path

SERVER_NAME = "paara-connector-audit"
SERVER_VERSION = "1.2.1"  # matches PAARA Connector Audit Kit v1.2.1
DEFAULT_PROTOCOL = "2025-03-26"
HERE = Path(__file__).resolve().parent
DATASET_CSV = HERE / "data" / "coding-sheet.csv"
FACTORS = ("F1", "F2", "F3", "F4", "F5", "F6", "F7")
HIGH_FACTORS = ("F1", "F2", "F3", "F4", "F5")
MEDIUM_FACTORS = ("F6",)

# ---------------------------------------------------------------------------
# Scoring rule — exact replica of paara_scanner/scoring.py (kit), used when
# the kit package itself is not importable. Highest-severity condition met,
# not a sum. Every score is a band: lower bound (U as N), upper (U as Y).
# ---------------------------------------------------------------------------


def _resolve(codes: dict[str, str], unknown_as_yes: bool) -> dict[str, bool]:
    return {
        f: (c == "Y" or (c == "U" and unknown_as_yes)) for f, c in codes.items()
    }


def _score_single(resolved: dict[str, bool]) -> tuple[str, str]:
    if resolved["F7"] and (resolved["F1"] or resolved["F3"] or resolved["F4"]):
        triggers = [x for x in ("F1", "F3", "F4") if resolved[x]]
        return "Critical", f"F7 (write/action) with {', '.join(triggers)}"
    if resolved["F7"]:
        return "High", "F7 (write/action) alone"
    high = [x for x in HIGH_FACTORS if resolved[x]]
    if len(high) >= 2:
        return "High", f"{len(high)} High-weighted factors: {', '.join(high)}"
    if len(high) == 1:
        return "Moderate", f"one High-weighted factor: {high[0]}"
    medium = [x for x in MEDIUM_FACTORS if resolved[x]]
    if len(medium) >= 2:  # unreachable with one Medium factor; kept for parity
        return "Moderate", "multiple Medium-weighted factors"
    return "Low", "no High-weighted factor and no write/action capability"


def score_codes_local(
    codes: dict[str, str], restricted: bool = False
) -> dict:
    """Score F1-F7 codes with the local replica. Returns bands + reasons."""
    lower, lower_reason = _score_single(_resolve(codes, False))
    upper, upper_reason = _score_single(_resolve(codes, True))
    out = {
        "default_lower": lower,
        "default_upper": upper,
        "restricted_lower": None,
        "restricted_upper": None,
        "reasons": [
            f"lower bound (U as N): {lower} — {lower_reason}",
            f"upper bound (U as Y): {upper} — {upper_reason}",
        ],
        "unknowns": [f for f in FACTORS if codes[f] == "U"],
    }
    if restricted:
        rcodes = dict(codes)
        rcodes["F7"] = "N"
        r_lower, r_lo_reason = _score_single(_resolve(rcodes, False))
        r_upper, r_up_reason = _score_single(_resolve(rcodes, True))
        out["restricted_lower"] = r_lower
        out["restricted_upper"] = r_upper
        out["reasons"].append(
            f"restricted (F7=N): {r_lower} -> {r_upper} "
            f"— lower: {r_lo_reason}; upper: {r_up_reason}"
        )
    return out


# ---------------------------------------------------------------------------
# Prefer the kit's own scoring module when it is importable by path.
# ---------------------------------------------------------------------------

_kit_score = None


def _load_kit_scoring():
    global _kit_score
    if _kit_score is not None:
        return _kit_score
    candidates = []
    if os.environ.get("PAARA_KIT_SRC"):
        candidates.append(Path(os.environ["PAARA_KIT_SRC"]))
    candidates.append(HERE.parent / "paara-repo" / "src")
    candidates.append(HERE / "paara_scanner_src")
    for src in candidates:
        if (src / "paara_scanner" / "scoring.py").is_file():
            sys.path.insert(0, str(src))
            try:
                from paara_scanner.models import Connector
                from paara_scanner.scoring import score_connector as kit_score

                _kit_score = (Connector, kit_score)
                return _kit_score
            except Exception:
                sys.path.remove(str(src))
    _kit_score = False
    return _kit_score


def score_codes(codes: dict[str, str], restricted: bool = False) -> dict:
    """Score with the kit module when available, else the local replica."""
    kit = _load_kit_scoring()
    if kit:
        Connector, kit_score = kit
        connector = Connector.from_code_string(
            "adhoc", "".join(codes[f] for f in FACTORS),
            has_write_limiting_control=restricted,
        )
        result = kit_score(connector)
        return {
            "default_lower": result.lower.value,
            "default_upper": result.upper.value,
            "restricted_lower": (
                result.restricted_lower.value if result.restricted_lower else None
            ),
            "restricted_upper": (
                result.restricted_upper.value if result.restricted_upper else None
            ),
            "reasons": list(result.reasons),
            "unknowns": [f.value for f in result.unknowns],
            "engine": "paara_scanner (kit)",
        }
    out = score_codes_local(codes, restricted)
    out["engine"] = "local replica of paara_scanner.scoring"
    return out


# ---------------------------------------------------------------------------
# Bundled dataset (the published 13-connector audit, snapshot 9 Nov 2026)
# ---------------------------------------------------------------------------

_ABBREV = {"Crit": "Critical", "Mod": "Moderate", "High": "High", "Low": "Low"}


def _full(value: str) -> str | None:
    value = (value or "").strip()
    return _ABBREV.get(value, value) if value else None


def load_dataset() -> list[dict]:
    rows = []
    with DATASET_CSV.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            name = (row.get("connector") or "").strip()
            if not name:
                continue
            rows.append(
                {
                    "name": name,
                    "codes": {f: row[f].strip().upper() for f in FACTORS},
                    "published_default_lower": _full(row["default_lower"]),
                    "published_default_upper": _full(row["default_upper"]),
                    "published_restricted_lower": _full(row["restricted_lower"]),
                    "published_restricted_upper": _full(row["restricted_upper"]),
                    "documentation_retrieved": (
                        row.get("documentation_retrieved") or ""
                    ).strip(),
                }
            )
    return rows


DATASET = load_dataset()


def _norm(text: str) -> str:
    return " ".join(text.lower().replace(".", " ").split())


def find_connector(query: str) -> dict | None:
    q = _norm(query)
    for row in DATASET:
        if _norm(row["name"]) == q:
            return row
    for row in DATASET:
        n = _norm(row["name"])
        if q in n or n in q:
            return row
    names = {_norm(r["name"]): r for r in DATASET}
    close = difflib.get_close_matches(q, list(names), n=1, cutoff=0.5)
    if close:
        return names[close[0]]
    tokens = set(q.split())
    best, best_overlap = None, 0
    for row in DATASET:
        overlap = len(tokens & set(_norm(row["name"]).split()))
        if overlap > best_overlap:
            best, best_overlap = row, overlap
    return best


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


def tool_score_connector(args: dict) -> dict:
    codes = {}
    for f in FACTORS:
        value = str(args.get(f, "")).strip().upper()
        if value not in ("Y", "N", "U"):
            raise ValueError(f"{f} must be one of Y, N, U (got {args.get(f)!r})")
        codes[f] = value
    restricted = bool(args.get("restricted", False))
    scored = score_codes(codes, restricted)
    return {
        "name": args.get("name") or "adhoc connector",
        "codes": codes,
        "code_string": "".join(codes[f] for f in FACTORS),
        **scored,
        "note": (
            "Bands, not points: U (documentation silent) is not evidence of "
            "absence, so the lower bound treats U as N and the upper as Y. "
            "Restricted bands apply only where a documented write-limiting "
            "control exists (restricted=true sets F7 to N)."
        ),
    }


def tool_lookup_connector(args: dict) -> dict:
    query = str(args.get("name", "")).strip()
    if not query:
        raise ValueError("name is required")
    row = find_connector(query)
    if row is None:
        return {
            "found": False,
            "query": query,
            "known_connectors": [r["name"] for r in DATASET],
        }
    restricted = row["published_restricted_lower"] is not None
    scored = score_codes(row["codes"], restricted)
    return {
        "found": True,
        "name": row["name"],
        "codes": row["codes"],
        "code_string": "".join(row["codes"][f] for f in FACTORS),
        "default_lower": scored["default_lower"],
        "default_upper": scored["default_upper"],
        "restricted_lower": scored["restricted_lower"],
        "restricted_upper": scored["restricted_upper"],
        "published_bands_match": (
            scored["default_lower"] == row["published_default_lower"]
            and scored["default_upper"] == row["published_default_upper"]
            and scored["restricted_lower"] == row["published_restricted_lower"]
            and scored["restricted_upper"] == row["published_restricted_upper"]
        ),
        "documentation_retrieved": row["documentation_retrieved"],
        "source": "PAARA 13-connector audit (documentation snapshot, 9 Nov 2026)",
    }


def tool_list_connectors(_args: dict) -> dict:
    return {
        "count": len(DATASET),
        "snapshot": "documentation retrieved 2026-11-09",
        "connectors": [
            {
                "name": r["name"],
                "code_string": "".join(r["codes"][f] for f in FACTORS),
                "default_lower": r["published_default_lower"],
                "default_upper": r["published_default_upper"],
                "restricted_lower": r["published_restricted_lower"],
                "restricted_upper": r["published_restricted_upper"],
            }
            for r in DATASET
        ],
    }


TOOLS = [
    {
        "name": "score_connector",
        "description": (
            "Score an AI connector with the PAARA seven-factor rule. Give the "
            "seven factor codes from the connector's documentation: F1 "
            "sensitive-data reach, F2 cross-system aggregation, F3 "
            "non-user-bound credentials, F4 absent logging, F5 "
            "prompt-injection exposure, F6 external sharing, F7 agentic "
            "action capability. Each code is Y (documented), N (documented "
            "absent) or U (documentation silent). Returns lower/upper score "
            "bands (Low/Moderate/High/Critical); set restricted=true if a "
            "documented write-limiting control applies, for restricted bands."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Connector name (optional label)."},
                **{
                    f: {"type": "string", "enum": ["Y", "N", "U"]}
                    for f in FACTORS
                },
                "restricted": {
                    "type": "boolean",
                    "description": "True if a documented write-limiting control applies.",
                },
            },
            "required": list(FACTORS),
        },
    },
    {
        "name": "lookup_connector",
        "description": (
            "Look up one of the 13 connectors in the published PAARA audit "
            "(documentation snapshot 9 Nov 2026) by name — fuzzy matching is "
            "supported, e.g. 'slack', 'Stripe MCP', 'graph'. Returns its "
            "F1-F7 codes and score bands."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"name": {"type": "string"}},
            "required": ["name"],
        },
    },
    {
        "name": "list_connectors",
        "description": (
            "List the 13 connectors in the published PAARA audit with their "
            "code strings and default score bands."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
]

TOOL_FUNCS = {
    "score_connector": tool_score_connector,
    "lookup_connector": tool_lookup_connector,
    "list_connectors": tool_list_connectors,
}

# ---------------------------------------------------------------------------
# MCP JSON-RPC over stdio (newline-delimited)
# ---------------------------------------------------------------------------


def _result(req_id, payload) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "result": payload}


def _error(req_id, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def handle(request: dict) -> dict | None:
    method = request.get("method", "")
    req_id = request.get("id")
    params = request.get("params") or {}

    if method == "initialize":
        client_version = params.get("protocolVersion")
        return _result(
            req_id,
            {
                "protocolVersion": client_version or DEFAULT_PROTOCOL,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            },
        )
    if method == "ping":
        return _result(req_id, {})
    if method == "tools/list":
        return _result(req_id, {"tools": TOOLS})
    if method == "tools/call":
        name = params.get("name", "")
        func = TOOL_FUNCS.get(name)
        if func is None:
            return _error(req_id, -32602, f"unknown tool: {name}")
        try:
            payload = func(params.get("arguments") or {})
        except Exception as exc:  # tool errors are reported, not fatal
            return _result(
                req_id,
                {
                    "content": [{"type": "text", "text": f"Error: {exc}"}],
                    "isError": True,
                },
            )
        text = json.dumps(payload, indent=2)
        return _result(
            req_id,
            {"content": [{"type": "text", "text": text}], "structuredContent": payload},
        )
    if req_id is None:  # notification (e.g. notifications/initialized)
        return None
    return _error(req_id, -32601, f"method not found: {method}")


def main() -> None:
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            response = _error(None, -32700, "parse error")
            stdout.write(json.dumps(response).encode() + b"\n")
            stdout.flush()
            continue
        response = handle(request)
        if response is not None:
            stdout.write(json.dumps(response).encode() + b"\n")
            stdout.flush()


if __name__ == "__main__":
    main()

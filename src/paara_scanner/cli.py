"""CLI for the PAARA connector-audit scanner.

Subcommands:
    audit   Score every connector in a coding-sheet CSV (default: the
            bundled 13-connector dataset) and report the bands.
    score   Score one connector from a code string or a JSON spec.
    scan    Triage documentation text into factor codes, then score it.
    check   Validate the bundled dataset against its published scores
            (exit code 1 on any mismatch).
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from . import __version__
from .heuristics import triage_text
from .io import load_coding_sheet, load_docs, load_json_spec
from .models import Connector, ScoreLevel
from .scoring import score_connector

DATA_DIR = Path(__file__).parent / "data"
DEFAULT_CSV = DATA_DIR / "connectors.csv"

_LEVEL_SHORT = {
    ScoreLevel.LOW: "Low",
    ScoreLevel.MODERATE: "Mod",
    ScoreLevel.HIGH: "High",
    ScoreLevel.CRITICAL: "Crit",
}


def _result_dict(result) -> dict:
    return {
        "name": result.name,
        "codes": result.code_string,
        "lower": result.lower.value,
        "upper": result.upper.value,
        "band": result.band,
        "restricted_band": result.restricted_band,
        "decision": result.decision(),
        "unknowns": [f.value for f in result.unknowns],
        "reasons": result.reasons,
    }


def _print_table(results) -> None:
    header = f"{'Connector':<22} {'Codes':<8} {'Default':<14} {'Restricted':<12} Decision"
    print(header)
    print("-" * len(header))
    for result in results:
        print(
            f"{result.name:<22} {result.code_string:<8} "
            f"{result.band:<14} {result.restricted_band or '—':<12} "
            f"{result.decision()}"
        )


def cmd_audit(args: argparse.Namespace) -> int:
    connectors = load_coding_sheet(args.csv)
    results = [score_connector(c) for c in connectors]
    if args.format == "json":
        print(json.dumps([_result_dict(r) for r in results], indent=2))
    elif args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(
            ["connector", "codes", "lower", "upper", "restricted_lower", "restricted_upper", "decision"]
        )
        for r in results:
            writer.writerow(
                [
                    r.name,
                    r.code_string,
                    r.lower.value,
                    r.upper.value,
                    r.restricted_lower.value if r.restricted_lower else "",
                    r.restricted_upper.value if r.restricted_upper else "",
                    r.decision(),
                ]
            )
    else:
        _print_table(results)
        crit_lo = sum(1 for r in results if r.lower is ScoreLevel.CRITICAL)
        crit_hi = sum(1 for r in results if r.upper is ScoreLevel.CRITICAL)
        print(
            f"\n{len(results)} connectors — Critical: {crit_lo} (lower) / "
            f"{crit_hi} (upper). None reaches Low."
            if all(r.upper is not ScoreLevel.LOW for r in results)
            else f"\n{len(results)} connectors."
        )
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    if args.json:
        connector = load_json_spec(args.json)
    else:
        connector = Connector.from_code_string(
            args.name, args.factors,
            has_write_limiting_control=args.restricted,
        )
    result = score_connector(connector)
    if args.format == "json":
        print(json.dumps(_result_dict(result), indent=2))
    else:
        print(f"{result.name}  codes {result.code_string}")
        print(f"Default:    {result.band}")
        if result.restricted_band:
            print(f"Restricted: {result.restricted_band}")
        print(f"Decision (upper bound): {result.decision()}")
        if result.unknowns:
            print(
                "Undocumented (U — record as owned open risks): "
                + ", ".join(f.value for f in result.unknowns)
            )
        for reason in result.reasons:
            print(f"  - {reason}")
    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    text = load_docs(args.docs)
    if not text.strip():
        print("No readable documentation found in the given paths.", file=sys.stderr)
        return 2
    evidence = triage_text(text)
    codes = {f: ev.code for f, ev in evidence.items()}
    connector = Connector(
        name=args.name,
        codes=codes,
        has_write_limiting_control=args.restricted,
    )
    result = score_connector(connector)
    print(f"{result.name}  codes {result.code_string}  (triage — verify every code)")
    for factor in evidence:
        ev = evidence[factor]
        print(f"  {factor.value} {ev.code.value} [{ev.confidence}] {ev.evidence}")
    print(f"Default:    {result.band}")
    if result.restricted_band:
        print(f"Restricted: {result.restricted_band}")
    print(f"Decision (upper bound): {result.decision()}")
    print("NOTE: heuristic triage only — a human coder must verify each code")
    print("against the audit checklist before relying on this score.")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    connectors = load_coding_sheet(args.csv)
    failures = 0
    for connector in connectors:
        result = score_connector(connector)
        expected_lo, expected_hi = connector.expected_default
        got = (_LEVEL_SHORT[result.lower], _LEVEL_SHORT[result.upper])
        if (expected_lo, expected_hi) != got:
            failures += 1
            print(
                f"FAIL {connector.name}: expected "
                f"{expected_lo}->{expected_hi}, got {got[0]}->{got[1]}"
            )
        if connector.has_write_limiting_control:
            exp_lo, exp_hi = connector.expected_restricted
            got_r = (
                _LEVEL_SHORT[result.restricted_lower],
                _LEVEL_SHORT[result.restricted_upper],
            )
            if (exp_lo, exp_hi) != got_r:
                failures += 1
                print(
                    f"FAIL {connector.name} (restricted): expected "
                    f"{exp_lo}->{exp_hi}, got {got_r[0]}->{got_r[1]}"
                )
    if failures:
        print(f"{failures} mismatch(es) against the published audit.")
        return 1
    print(
        f"OK: all {len(connectors)} connectors reproduce the published "
        "audit scores (default and restricted bands)."
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="paara_scanner",
        description="PAARA seven-factor connector risk scanner.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_audit = sub.add_parser("audit", help="Score a coding-sheet CSV.")
    p_audit.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    p_audit.add_argument("--format", choices=["table", "json", "csv"], default="table")
    p_audit.set_defaults(func=cmd_audit)

    p_score = sub.add_parser("score", help="Score one connector.")
    p_score.add_argument("--name", default="Connector")
    p_score.add_argument("--factors", help="7-char code string, F1-F7, e.g. UNUUYNY")
    p_score.add_argument("--json", type=Path, help="JSON connector spec")
    p_score.add_argument("--restricted", action="store_true",
                         help="Score a restricted (F7=N) configuration too")
    p_score.add_argument("--format", choices=["text", "json"], default="text")
    p_score.set_defaults(func=cmd_score)

    p_scan = sub.add_parser("scan", help="Triage docs into codes, then score.")
    p_scan.add_argument("--docs", nargs="+", required=True,
                        help="File(s) or director(ies) of documentation")
    p_scan.add_argument("--name", default="Connector")
    p_scan.add_argument("--restricted", action="store_true")
    p_scan.set_defaults(func=cmd_scan)

    p_check = sub.add_parser("check", help="Validate dataset vs published scores.")
    p_check.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    p_check.set_defaults(func=cmd_check)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "score" and not args.json and not args.factors:
        print("score needs --factors or --json", file=sys.stderr)
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

# PAARA Scanner

A working, runnable implementation of the PAARA seven-factor
connector risk-scoring rule. No dependencies beyond the Python 3.9+
standard library.

## Install / run

```bash
# From the repository root — no install needed:
PYTHONPATH=src python -m paara_scanner audit

# Or install it:
pip install .
paara-scanner audit
```

## The rule

Each connector is coded Y / N / U on seven factors:

| Factor | Meaning |
|---|---|
| F1 | Sensitive-data reach |
| F2 | Cross-system aggregation |
| F3 | Non-user-bound credentials |
| F4 | Absent logging (Y = logging absent, N = logging documented) |
| F5 | Prompt-injection exposure |
| F6 | External sharing |
| F7 | Agentic action capability (write / send / delete / execute) |

Scoring (highest-severity condition met, not a sum):

- **Critical** — F7 and any of F1, F3, F4
- **High** — F7, or two or more of F1–F5
- **Moderate** — one High-weighted factor (one of F1–F5)
- **Low** — otherwise

U is not evidence of absence, so every score is a band:
lower bound (U as N) → upper bound (U as Y). Decisions use the
upper bound. A restricted configuration (a documented write-limiting
control, F7 set to N) is scored the same way when one exists.

## Commands

```bash
# Score the bundled 13-connector dataset (reproduces the published audit)
python -m paara_scanner audit
python -m paara_scanner audit --format json
python -m paara_scanner audit --format csv

# Validate the dataset against the published scores (exit 1 on mismatch)
python -m paara_scanner check

# Score one connector from a 7-char code string (F1–F7 order)
python -m paara_scanner score --name "MCP Filesystem" --factors UNUUYNY
python -m paara_scanner score --name "Slack MCP" --factors YNNNYYY --restricted

# Score one connector from a JSON spec
python -m paara_scanner score --json examples/slack.json

# Triage documentation into codes, then score it
# (heuristic only — a human coder must verify every code)
python -m paara_scanner scan --docs docs/my-connector/ --name "My Connector"
```

## Example output

```
$ python -m paara_scanner audit
Connector              Codes    Default        Restricted   Decision
-----------------------------------------------------------------------
MCP Filesystem         UNUUYNY  High -> Critical Mod -> High   Restrict — ...
...
13 connectors — Critical: 9 (lower) / 12 (upper). None reaches Low.
```

## JSON connector spec

```json
{"name": "Slack MCP", "factors": "YNNNYYY", "has_write_limiting_control": true}
```

or with explicit codes:

```json
{"name": "Slack MCP", "codes": {"F1": "Y", "F2": "N", "F3": "N", "F4": "N", "F5": "Y", "F6": "Y", "F7": "Y"}}
```

## Tests

```bash
python -m unittest discover -s tests -v
```

The scoring tests reproduce **all 13 connectors' published
default and restricted bands** from `audit/coding-sheet.csv`
(9 Critical lower / 12 Critical upper). If the rule ever drifts
from the published audit, `paara_scanner check` and the tests fail.

## Limitations

- `scan` is keyword triage, not a coder: it finds evidence phrases
  and returns the verbatim snippet for each code. Verify every code
  against `templates/connector-audit-checklist.md` before relying
  on the score.
- Documentation is not behaviour. A vendor may implement controls
  it does not document, or document features that are not enforced.
- The 13-connector corpus is a convenience sample (9 Nov 2026
  snapshot), not a random sample.

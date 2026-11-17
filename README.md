[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24325766.svg)](https://doi.org/10.5281/zenodo.24325766)
# PAARA — Connector Audit Kit

An open, practitioner toolkit for auditing AI connectors before they are enabled in an enterprise.

## MCP Server

PAARA ships a working MCP (Model Context Protocol) server: a stdlib-only Python implementation over stdio (hand-rolled JSON-RPC, no SDK dependency) at `mcp-server/paara_mcp_server.py`. It implements `initialize`, `ping`, `tools/list` and `tools/call`, and exposes three MCP tools:

- `score_connector` — score any connector from its F1–F7 factor codes (Y/N/U); returns the PAARA score bands (default and restricted, lower/upper) with reasons.
- `lookup_connector` — look up any of the 13 audited connectors by name; returns its F1–F7 codes and bands.
- `list_connectors` — list all 13 audited connectors with their default bands.

Run it:

```bash
python3 mcp-server/paara_mcp_server.py
```

Client configuration (Claude Desktop / generic MCP clients):

```json
{
  "mcpServers": {
    "paara-connector-audit": {
      "command": "python3",
      "args": ["mcp-server/paara_mcp_server.py"]
    }
  }
}
```

Full server documentation: `mcp-server/README.md`. Protocol and scoring tests: `mcp-server/test_paara_mcp_server.py` (26 checks, all passing).

**PAARA** (Privacy-Aware AI Risk Architecture) treats the **connector** — OAuth / API permissions, Model Context Protocol (MCP) servers, and retrieval pipelines — as the unit of governance, and scores it with an explicit, reproducible rule set that yields a deployment decision.

- **Author:** Vivek Kumar — Independent professional (AI Governance & Data Privacy, Cyber GRC); Independent Peer Reviewer / Subject Matter Expert
- **Website:** https://www.vivekkumar.tech/
- **Google Scholar:** https://scholar.google.com/citations?user=xRSOuTkAAAAJ
- **Methodology paper (SSRN):** https://doi.org/10.2139/ssrn.6784078 — Kumar, V., "Privacy-Aware AI Risk Architecture (PAARA)", SSRN, posted 28 May 2026
- **Empirical application:** Kumar, V., "How Well Documented Are AI Connector Risks? Applying the PAARA Governance Methodology to Thirteen Public MCP and Enterprise Connectors", 6th IEEE International Conference on AI in Cybersecurity (ICAIC 2027), 3–5 March 2027, University of Houston. Submitted via Microsoft CMT, Paper ID 302, status: Awaiting Decision (submitted 14 Nov 2026).

## What this kit is for

Enterprise AI assistants reach organisational data through connectors. A governance reviewer who must approve a connector usually relies on vendor documentation. This kit gives that reviewer:

1. A repeatable way to inventory connectors and map their scope.
2. A seven-factor risk-scoring rule with explicit coding rules.
3. A connector DPIA template and an audit checklist.
4. A worked example: the full coded audit of 13 public connectors, with evidence-based scores.

## The PAARA methodology (6–8 components)

PAARA is presented here as a **6–8 component** methodology. The SSRN abstract describes it as a six-component methodology; the ICAIC 2027 paper refers to an eight-component process. Rather than force one number, this repository presents the range and names both sources. That is fine — the method is still growing, the evidence base is still growing, and neither we nor the world are perfect. The six components listed in the SSRN paper are:

| # | Component | What it does |
|---|-----------|--------------|
| 1 | Connector inventory and scope mapping | List every connector, what it can reach, and under whose authority |
| 2 | WP29 nine-criteria application at the connector layer | Apply the Article 29 Working Party nine criteria for high-risk processing to each connector |
| 3 | OAuth and Graph permission risk registers | Record permission scopes, delegation vs application permissions, and resource-specific consent |
| 4 | Retrieval-boundary and prompt-injection threat modelling | Map what retrieved content can carry into the model, and where injection can enter |
| 5 | Insider-risk amplification assessment | Assess how a connector amplifies what an insider (or a compromised account) can reach or do |
| 6 | Cross-framework alignment | Align the assessment across GDPR Article 35, EU AI Act Article 27, ISO/IEC 42005:2025, and NIST AI 600-1 |

The methodology identifies five regulatory gaps not addressed by any current authority, including the absence of connector-specific DPIA templates, insider-risk amplification analysis, and WP29 nine-criteria mapping at the connector layer. This repository is a step toward closing the first of those gaps: it ships a connector-specific DPIA template (see `templates/`).

> **Note on component count.** PAARA is presented in this repository as a **6–8 component** methodology: the SSRN abstract describes it as six-component, and the ICAIC 2027 paper refers to an eight-component process. That range is an open item to reconcile in a future revision of the methodology paper; nothing in this kit depends on which count is used — the scoring rules and templates here stand on their own.

> **Note on regulatory submissions.** The SSRN abstract states that regulatory submissions based on this methodology were filed with the UK ICO, CNIL (France), IMDA (Singapore), and NIST (USA) in May 2026. That statement is corroborated only from the paper itself, not from a regulator website, and this repository makes no further claim about regulator adoption or government use.

## The connector risk-scoring rule

The audit in this kit codes seven factors for each connector, from official public documentation only:

| Factor | Coded Y when documentation … |
|--------|------------------------------|
| F1 Sensitive data | names personal, financial, private-communication, or security data as reachable |
| F2 Aggregation | states reach across more than one separately administered system |
| F3 Credential | documents app-level, service-account, shared, or agent keys, or no authentication |
| F4 Logging | states server-side retrieval or audit logging is absent (N when documented; U when silent) |
| F5 Injection | shows retrieval of content authored by parties other than the user |
| F6 Sharing | documents outbound sharing, sending, or requests to arbitrary hosts |
| F7 Action | documents write, send, delete, or other state-changing tools |

Each factor is coded **Y** (documentation states it), **N** (documentation states or clearly implies its absence), or **U** (undocumented). A fact is never coded from prior knowledge.

**Scoring rule (highest-severity condition met, not a sum):**

- **Critical** — F7 and any of F1, F3, F4
- **High** — F7, or two or more of F1–F5
- **Moderate** — one High factor, or multiple Medium factors
- **Low** — otherwise

F1–F5 are High-weighted, F6 is Medium-weighted, F7 is Critical-weighted. Agentic capability alone floors a connector at High and yields Critical only when combined with sensitive data, broad or application-level credentials, or missing logging.

Because **U is not evidence of absence**, every connector is scored twice: a lower bound with U treated as N, and an upper bound with U treated as Y. For connectors whose documentation describes a control that removes write capability (a read-only flag or endpoint, read-only scopes, an organisation-wide read-only restriction, or administrator-selected tools), a restricted configuration is also scored with F7 set to N.

A cryptographic-dependency register (token signature, transport key establishment, at-rest key wrapping) is recorded per connector so organisations can later triage dependencies for post-quantum migration.

## Worked example: 13 public connectors

See [`audit/13-connector-audit.md`](audit/13-connector-audit.md) and [`audit/coding-sheet.csv`](audit/coding-sheet.csv) for the full coded audit. Documentation retrieved **9 November 2026**; results are a snapshot, not a live verdict.

**Headline findings (default configuration):**

- **9 of 13** connectors score **Critical** under the favourable assumption; **12 of 13** under the unfavourable assumption.
- Applying a documented write-limiting control (8 connectors have one) moves 7 from Critical to High and 1 from High to Moderate. **None reaches Low.**
- Server-side audit logging is explicitly documented for **2 of 13** connectors (Slack, Stripe). Prompt-injection guidance is documented for **1** (Stripe). **None** documents a TLS version, token-signing algorithm, or post-quantum support.
- Prompt-injection exposure (F5) is present in **12 of 13**; write capability (F7) in **11 of 13**.

**Governance implication:** undocumented items should be recorded as **owned open risks** — with a named owner and a review date — and the lower-to-upper score band reported instead of a single number. Approval on the favourable assumption relies on facts nobody has verified.

## The scanner (working code)

`src/paara_scanner/` is a runnable Python implementation of the
scoring rule above — no dependencies beyond the Python 3.9+ standard
library. See [`src/README.md`](src/README.md).

```bash
PYTHONPATH=src python -m paara_scanner audit     # score the 13-connector dataset
PYTHONPATH=src python -m paara_scanner check     # validate vs the published audit
PYTHONPATH=src python -m paara_scanner score --name "Slack MCP" --factors YNNNYYY --restricted
PYTHONPATH=src python -m paara_scanner scan --docs docs/ --name "My Connector"
python -m unittest discover -s tests -v          # 20 tests
```

`audit` reproduces the published bands exactly (9 Critical lower /
12 Critical upper; restricted bands for the 8 connectors with a
documented write-limiting control). `scan` is keyword triage of
documentation into factor codes with verbatim evidence snippets —
a human coder must verify every code before relying on the score.

## How to use this kit

1. **Inventory** — list the connector in the DPIA template (`templates/connector-dpia-template.md`).
2. **Code** — work through the audit checklist (`templates/connector-audit-checklist.md`), recording a verbatim evidence snippet (≤ 25 words) and URL for every coded field.
3. **Score** — apply the rule above under both bounding assumptions; record the band, not a single score.
4. **Restrict and re-score** — if a read-only mode or scope restriction is documented, score the restricted configuration too.
5. **Record the unknowns** — every U becomes an open item with an owner and a review date; send the vendor attestation questions in the checklist if needed.

## Limitations — read before citing

- Coding was performed by a **single coder** (the author), with AI-assisted retrieval; **no inter-rater reliability is reported**. The coding sheet is released so others can independently re-code. A second coder is invited — see `CONTRIBUTING.md`.
- **Documentation is not behaviour.** A vendor may implement controls it does not document, or document features that are not enforced.
- The corpus is a **convenience sample of 13 well-documented connectors**, not a random sample; it may overstate documentation quality relative to the long tail.
- Several factor codes involve judgement (e.g. whether a named data category is "sensitive").
- Applying PAARA's scores to its own motivating domain cannot establish predictive validity; incident-based validation is future work.
- Documentation changes frequently; results are a snapshot from 9 November 2026.

## Repository contents

```
├── README.md                          This file
├── LICENSE                            MIT License
├── CONTRIBUTING.md                    How to re-code, extend the corpus, or report an issue
├── pyproject.toml                     Package metadata (pip install .)
├── docs/                            Dataset & method, teardowns, and open training (see [docs/README.md](docs/README.md))
│   ├── dataset-and-method.md        PAARA dataset and method — 13-connector audit
│   ├── teardowns/
│   │   └── connector-spy-test-1-gmail-to-chatgpt.md
│   └── training/
│       └── modules-0-2.md           Training Modules 0–2 (Modules 3–7 in outline)
├── audit/
│   ├── 13-connector-audit.md          Full coded audit of 13 public connectors
│   └── coding-sheet.csv               Machine-readable factor codes and scores
├── src/
│   ├── README.md                      Scanner usage
│   └── paara_scanner/                 Working scanner (stdlib only)
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py                     audit / score / scan / check commands
│       ├── models.py                  Factor codes, Connector, ScoreResult
│       ├── scoring.py                 Seven-factor rule (banded U as N / U as Y)
│       ├── heuristics.py              Documentation triage with evidence snippets
│       ├── io.py                      CSV / JSON / doc-folder loading
│       └── data/
│           ├── connectors.csv         Bundled 13-connector dataset
│           └── connectors.json        Same dataset as JSON
├── tests/
│   ├── test_scoring.py                Reproduces all 13 published bands
│   ├── test_heuristics.py             Triage behaviour
│   └── test_cli.py                    End-to-end CLI tests
├── examples/
│   └── slack.json                     Example JSON connector spec
└── templates/
    ├── connector-audit-checklist.md   Step-by-step audit checklist + vendor questions
    └── connector-dpia-template.md     Connector-layer DPIA template
```

## References

1. Kumar, V., "Privacy-Aware AI Risk Architecture (PAARA)", SSRN, DOI 10.2139/ssrn.6784078.
2. Kumar, V., "PAARA: A permission-aware retrieval and agent risk assessment framework for secure enterprise GenAI systems", Proc. IEEE GAISS 2026, Austin, TX, USA.
3. Kumar, V., "How Well Documented Are AI Connector Risks? Applying the PAARA Governance Methodology to Thirteen Public MCP and Enterprise Connectors", ICAIC 2027 (submitted, Paper ID 302).
4. NIST, "Artificial Intelligence Risk Management Framework: Generative AI Profile", NIST AI 600-1, July 2024.
5. Greshake, K. et al., "Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection", Proc. AISec '23, ACM, 2023, pp. 79–90.
6. OWASP GenAI Security Project, "OWASP Top 10 for LLM Applications 2025", v2.0, 2024.

## Licence

MIT — see [`LICENSE`](LICENSE).

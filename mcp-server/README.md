# PAARA Connector Audit — MCP Server

A thin [Model Context Protocol](https://modelcontextprotocol.io) (MCP)
server that exposes the **PAARA seven-factor connector scoring rule** and
the published **13-connector audit dataset** as tools any MCP client can
call. Pure Python standard library — no dependencies, no build step.

PAARA (Privacy-Aware AI Risk Architecture) treats the connector — MCP
servers, OAuth/API permissions, retrieval pipelines — as the unit of AI
governance. Before an AI agent is allowed to act through a connector, the
connector's own documentation is coded on seven risk factors and scored
with an explicit, reproducible rule.

## Run it

```bash
python3 paara_mcp_server.py
```

That's it: the server speaks MCP JSON-RPC over stdio. Point any MCP
client at the command above (client config below). Python 3.10+.

## Tools

| Tool | Input | Output |
|---|---|---|
| `score_connector` | `F1`–`F7`, each `Y` / `N` / `U`; optional `name`, `restricted` | Score bands: default lower/upper, restricted lower/upper, with reasons |
| `lookup_connector` | `name` (fuzzy match) | The coded F1–F7 values and bands for one of the 13 audited connectors |
| `list_connectors` | — | All 13 audited connectors with code strings and default bands |

The seven factors: **F1** sensitive-data reach, **F2** cross-system
aggregation, **F3** non-user-bound credentials, **F4** absent logging,
**F5** prompt-injection exposure, **F6** external sharing, **F7** agentic
action capability. Each is coded from the connector's documentation as
**Y** (documented), **N** (documented absent) or **U** (documentation
silent).

Scores are **bands, not points**: because U is not evidence of absence,
every connector is scored twice — a lower bound (U treated as N) and an
upper bound (U treated as Y). Where a documented write-limiting control
exists, restricted bands (F7 set to N) are reported too. Headline result
of the bundled audit (documentation snapshot, 9 Nov 2026): **9 of 13
connectors score Critical on the lower bound, 12 of 13 on the upper
bound, none reaches Low**; server-side audit logging is documented for
2 of 13 (Slack, Stripe).

## Client config

Claude Desktop / generic MCP clients (`claude_desktop_config.json` or
equivalent):

```json
{
  "mcpServers": {
    "paara-connector-audit": {
      "command": "python3",
      "args": ["/path/to/paara-mcp-server/paara_mcp_server.py"]
    }
  }
}
```

## Scoring engine

If the PAARA Connector Audit Kit's `paara_scanner` package is importable
(set `PAARA_KIT_SRC` to the kit's `src/` folder, or keep a `paara-repo`
checkout next to this folder), the server uses the kit's own scoring
module. Otherwise it falls back to an exact local replica of the rule in
`src/paara_scanner/scoring.py`, so this file works standalone. The test
suite verifies the replica against the published bands for all 13
connectors:

```bash
python3 test_paara_mcp_server.py
```

## Files

- `paara_mcp_server.py` — the server (stdlib only)
- `data/coding-sheet.csv` — the bundled 13-connector dataset
- `test_paara_mcp_server.py` — protocol + scoring tests
- `server.json` — draft metadata for the official MCP Registry
- `glama.json` — Glama maintainer metadata
- `smithery.yaml` — Smithery stdio start configuration
- `REGISTRY_SUBMISSION_NOTES.md` — how to list this server in each registry

## Links

- Kit (scanner, templates, full audit): https://github.com/vkktask/paara-connector-audit-kit
- Archived kit + dataset (Zenodo, concept DOI): https://doi.org/10.5281/zenodo.24325766
- Dataset on Hugging Face: https://huggingface.co/datasets/vkkask/paara-connector-audit
- Methodology paper: Kumar, V. (2026). *Privacy-Aware AI Risk Architecture (PAARA).* SSRN. https://doi.org/10.2139/ssrn.6784078

## Limitations

Single coder; no inter-rater reliability reported. The audit codes
**documentation, not runtime behaviour** — a Critical score means the
documentation describes a high-risk capability set with key controls
undocumented, not that the product is insecure in operation. Snapshot of
9 November 2026; vendors revise documentation without notice.

## Licence

MIT. Maintained by Vivek Kumar, Independent professional (AI Governance
& Data Privacy, Cyber GRC) — ORCID 0009-0008-3767-200X —
https://www.vivekkumar.tech/

<!-- mcp-name: io.github.vkktask/paara-connector-audit -->

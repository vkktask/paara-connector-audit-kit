# 13-Connector Audit — PAARA Scoring Applied to Public Documentation

**Source paper:** Kumar, V., "How Well Documented Are AI Connector Risks? Applying the PAARA Governance Methodology to Thirteen Public MCP and Enterprise Connectors", ICAIC 2027 (submitted 14 Nov 2026, CMT Paper ID 302, status: Awaiting Decision).

**Documentation retrieved:** 9 November 2026, from official public documentation only. Two retrieval attempts failed (Atlassian developer pages and a ChatGPT connectors article) and were excluded. This is a convenience sample of widely used, well-documented connectors, not a random sample.

**Method:** each connector is coded on seven factors (F1–F7), Y / N / U. Scores are given as a band: lower bound (U treated as N) → upper bound (U treated as Y). "Restricted" is the score with a documented write-limiting control applied (F7 set to N); "—" means no documented write-limiting control.

**Limitations:** single coder, no inter-rater reliability reported; documentation is not behaviour; factor definitions are the paper's operationalisation of PAARA. See the README for the full limitations list.

## Corpus

| # | Connector | Type |
|---|-----------|------|
| 1 | MCP Filesystem | MCP reference server |
| 2 | MCP Git | MCP reference server |
| 3 | MCP Memory | MCP reference server |
| 4 | MCP Fetch | MCP reference server |
| 5 | GitHub MCP | Vendor-hosted MCP server |
| 6 | Notion MCP | Vendor-hosted MCP server |
| 7 | Atlassian MCP | Vendor-hosted MCP server |
| 8 | Linear MCP | Vendor-hosted MCP server |
| 9 | Sentry MCP | Vendor-hosted MCP server |
| 10 | Stripe MCP | Vendor-hosted MCP server |
| 11 | Slack MCP | Vendor-hosted MCP server |
| 12 | Microsoft Graph permissions | Permission model (not an MCP server) |
| 13 | Claude connectors | Connector platform |

## Factor codes and scores

| Connector | F1 | F2 | F3 | F4 | F5 | F6 | F7 | Default (lo → hi) | Restricted (lo → hi) |
|-----------|----|----|----|----|----|----|----|-------------------|----------------------|
| MCP Filesystem | U | N | U | U | Y | N | Y | High → Crit | Mod → High |
| MCP Git | N | N | U | U | Y | N | Y | High → Crit | — |
| MCP Memory | Y | N | Y | U | N | N | Y | Crit → Crit | — |
| MCP Fetch | U | N | U | U | Y | Y | N | Mod → High | — |
| GitHub MCP | Y | N | N | U | Y | Y | Y | Crit → Crit | High → High |
| Notion MCP | U | Y | Y | U | Y | N | Y | Crit → Crit | High → High |
| Atlassian MCP | U | Y | Y | U | Y | Y | Y | Crit → Crit | High → High |
| Linear MCP | N | N | Y | U | Y | N | Y | Crit → Crit | High → High |
| Sentry MCP | N | N | U | U | Y | N | U | Mod → Crit | — |
| Stripe MCP | Y | N | Y | N | Y | Y | Y | Crit → Crit | — |
| Slack MCP | Y | N | N | N | Y | Y | Y | Crit → Crit | High → High |
| MS Graph perms. | Y | Y | Y | U | Y | U | Y | Crit → Crit | High → High |
| Claude connectors | Y | Y | Y | U | Y | Y | Y | Crit → Crit | High → High |

Codes in the source paper's Table II are given as a seven-character string in F1–F7 order (e.g. MCP Filesystem `UNUUYNY`); the table above expands those strings. The machine-readable version is in [`coding-sheet.csv`](coding-sheet.csv).

**Default configuration:** 9 Critical, 2 High, 2 Moderate (lower bound); 12 Critical, 1 High (upper bound).

**Effect of documented controls (8 connectors have one):** applying the control moves 7 from Critical to High and 1 (Filesystem, via a read-only mount) from High to Moderate under the favourable assumption. No connector reaches Low, because prompt-injection exposure (F5) is present for 12 of 13 connectors and sensitive-data access remains for most. In PAARA terms, a read-only deployment of these connectors still warrants "Restrict or defer pending full assessment", not unconditional approval.

## Factor prevalence (Y / N / U, n = 13)

| Factor | Y | N | U | Meaning of count |
|--------|---|---|---|------------------|
| F1 Sensitive data | 6 | 3 | 4 | named sensitive data |
| F2 Aggregation | 4 | 9 | 0 | multi-system reach |
| F3 Credential | 7 | 2 | 4 | non-user-bound option |
| F4 Logging | 0 | 2 | 11 | N = logging documented |
| F5 Injection | 12 | 1 | 0 | untrusted content read |
| F6 Sharing | 6 | 6 | 1 | outbound sharing |
| F7 Action | 11 | 1 | 1 | write/action tools |

F4 is never coded Y because no vendor states that logging is absent; it is coded U for 11 connectors because documentation is silent, and N for the 2 that document it.

## Sensitivity: Critical counts when a trigger is removed

| Trigger removed from Critical rule | Critical (lower) | Critical (upper) |
|------------------------------------|------------------|------------------|
| None (baseline) | 9 | 12 |
| F1 sensitive data | 7 | 11 |
| F3 credential | 6 | 12 |
| F4 logging | 9 | 12 |
| F1 and F3 | 0 | 10 |
| F3 and F4 | 6 | 9 |

The Critical result rests mainly on sensitive-data reach and on non-user-bound credentials — the factors where coding involves the most judgement. Dropping F4 changes nothing, because F4 is never Y.

## Documentation gaps

- **Logging.** Server-side audit or tool-call logging is explicitly documented for 2 connectors, Slack and Stripe. Atlassian's page advises monitoring audit logs without describing the capability, and the Git server mentions only client-side debug logs. The remaining 9 are silent.
- **Prompt injection.** 1 connector, Stripe, documents guidance (enable tool approval and be cautious with other servers).
- **Cryptography.** None of the 13 states a TLS version, key-exchange group, token-signing algorithm, or post-quantum or hybrid support in the retrieved pages. GitHub documents that non-HTTPS hosts are refused, and the Claude platform states that transfers are encrypted, but neither gives a protocol version. Cryptographic-dependency tiers therefore cannot be assigned from public documentation for any of the 13; each dependency would be recorded as an owned unknown.

## Notable documented observations

- The Memory server documents no authentication and tells the model to assume a single default user.
- The Fetch server states that it can reach local and internal addresses and obeys robots.txt only for model-initiated requests — relevant to server-side request abuse.
- The Git server shows a repository argument in examples but does not state that it is enforced.
- Stripe documents agent API keys that give independent, persistent access, and is the only vendor in the corpus that documents both tool-call logging and injection guidance.
- Slack requires administrator approval of MCP client apps and documents audit logging.
- Linear offers a dedicated read-only endpoint, the clearest example of a vendor-provided least-privilege path.
- The Microsoft Graph model separates delegated from application permissions and documents resource-specific consent, but, as a permission model rather than an MCP server, it does not describe retrieval logging.

## Worked example (Slack)

Documentation states that private channels, direct messages, and user profile emails are reachable (F1=Y); calls run on user tokens through a registered app (F3=N); audit logs for MCP activity are documented (F4=N); retrieved messages are authored by other people (F5=Y); messages can be sent (F6=Y); and write tools exist (F7=Y). Under the rule, F7 with F1 gives Critical. With read-only scopes only (F7=N), two High factors (F1, F5) remain, giving High.

## Sources (retrieved 9 Nov 2026)

- Model Context Protocol, modelcontextprotocol.io; reference servers, github.com/modelcontextprotocol/servers
- GitHub MCP Server, github.com/github/github-mcp-server
- Notion MCP, developers.notion.com/guides/mcp
- Atlassian remote MCP server, support.atlassian.com
- Linear MCP, linear.app/docs/mcp
- Sentry MCP, docs.sentry.io/product/sentry-mcp
- Stripe MCP, docs.stripe.com/mcp
- Slack MCP, docs.slack.dev/ai/slack-mcp-server
- Microsoft Graph permissions overview, learn.microsoft.com/graph/permissions-overview
- Anthropic, "Use connectors to extend Claude's capabilities", support.claude.com

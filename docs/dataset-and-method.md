# PAARA Dataset and Method — 13-Connector Audit

**Dataset & Method · Snapshot 9 November 2026**

> **Read this first — status of the headline counts.** The counts on this page — **9 Critical (lower bound), 12 of 13 with no documented prompt-injection defence, and server-side audit logging documented for only 2 of 13 (Slack and Stripe)** — are **Vivek Kumar's own audit**. They have **not been independently verified**. That is why the dataset and method are published here first: every score below must be reproducible from the coding sheet and the scoring rule on this page. If you cannot reproduce a score, treat the score — not your reading — as the thing to question, and file it as an issue (see [Corrections](#10-corrections-and-right-of-reply), below).

How well documented are AI connector risks? A coded audit of thirteen public MCP and enterprise connectors, scored with PAARA — the Privacy-Aware AI Risk Architecture (**6–8 components**, see [Caveats](#6-caveats-and-open-issues)) — from official public documentation only. Dataset first, claims second.

- **Author:** Vivek Kumar
- **Role:** Independent professional — AI Governance & Data Privacy, Cyber GRC; Independent Peer Reviewer / Subject Matter Expert
- **Documentation retrieved:** 9 November 2026
- **Sample:** 13 connectors (convenience sample)
- **GitHub:** <https://github.com/vkktask/paara-connector-audit-kit>
- **Website:** <https://www.vivekkumar.tech/>

## Headline counts

| Count | What it means |
|---|---|
| **9 → 12** | Critical scores, lower → upper bound, out of 13 connectors (default scoring) |
| **12 / 13** | Document no prompt-injection defence. Only Stripe documents guidance. |
| **2 / 13** | Document server-side audit logging — Slack and Stripe. The other 11 are silent (U). No connector documents logging as absent: F4 is never coded Y. |
| **0** | Connectors reach Low — even after documented write-limiting controls are applied. |

All four figures are the author's audit, single-coded, not independently verified. See [Limitations](#5-limitations--read-before-citing) and [Caveats](#6-caveats-and-open-issues).

> **Correction note on logging (added when this page was saved to GitHub).** An earlier web version of this page worded the logging finding as "a documented position on logging for only 2 of 13 — in both cases stating that logging is absent (F4 = N)". That wording is incorrect. Per the source audit (`audit/13-connector-audit.md`): server-side audit or tool-call logging **is explicitly documented for 2 connectors, Slack and Stripe** — logging is documented as *present*, which is why F4 is coded **N** for them. F4 is never coded Y because no vendor states that logging is absent; it is coded U for the 11 connectors whose documentation is silent. The README's headline sentence — "Server-side audit logging is explicitly documented for 2 of 13 connectors (Slack, Stripe)" — is the correct wording and has been kept.

## 1. Headline findings (default scoring)

- **9 Critical lower · 12 Critical upper.** Default band distribution, lower bound: 9 Critical, 2 High, 2 Moderate. Upper bound: 12 Critical, 1 High. No connector scores Low at either bound.
- **Write-limiting controls help — a little.** 8 of 13 connectors document a write-limiting control. Applying it (restricted scoring, F7 = N) moves 7 connectors Critical → High, and 1 connector — MCP Filesystem — High → Moderate. None reaches Low.
- **Prompt injection: 12 of 13 exposed, 1 defended on paper.** Factor F5 (retrieval of content authored by parties other than the user) is present in 12 of 13. Prompt-injection guidance is documented for 1 connector only — Stripe. The other 12 document no defence.
- **Write capability is the norm: 11 of 13.** Factor F7 (write, send, delete, or other state-changing tools) is coded Y in 11 of 13, N in 1, U in 1. Combined with sensitive-data reach or broad credentials, that is what drives the Critical band.
- **Logging is mostly undocumented.** F4 is coded N — logging documented — for 2 connectors (Slack, Stripe), and U — documentation silent — for 11. F4 is never coded Y. Silence is recorded as an unknown, not as safety.
- **Transport security is undocumented across the board.** None of the 13 documents a TLS version, a token-signing algorithm, or post-quantum support in the material retrieved on 9 November 2026.

## 2. Method

**Source material.** Official public documentation only, retrieved **9 November 2026**. No vendor briefings, no hands-on testing, no prior knowledge: a factor was never coded from what the coder already believed about a product.

**Sample.** A convenience sample of 13 widely used, well-documented connectors — MCP Filesystem, MCP Git, MCP Memory, MCP Fetch, GitHub MCP, Notion MCP, Atlassian MCP, Linear MCP, Sentry MCP, Stripe MCP, Slack MCP, Microsoft Graph permissions, and Claude connectors. It is **not a random sample**, and the results do not generalise to all connectors.

**Coding.** Each connector was coded on seven factors: **Y** = the documentation states it; **N** = the documentation states or clearly implies its absence; **U** = undocumented — the documentation is silent.

> **F4 coding convention — read carefully.** F4 (Logging) uses an inverted code relative to the other factors, as defined in the source audit: **N means logging is documented (present)**; **U means the documentation is silent**; **Y would mean logging is stated absent, and no connector is coded Y** because no vendor states that logging is absent. This is why "F4 is never coded Y" and "logging is documented for 2 of 13" are the same finding, not a contradiction.

| Factor | Name | Definition — coded Y when the documentation shows… | Weight |
|---|---|---|---|
| F1 | Sensitive data | Personal, financial, private-communication, or security data named as reachable. | High |
| F2 | Aggregation | Reach across more than one separately administered system. | High |
| F3 | Credential | App-level, service-account, shared, or agent keys — or no authentication. | High |
| F4 | Logging | Server-side retrieval or audit logging. Coded **N** when logging is documented, **U** when the documentation is silent. **F4 is never coded Y** (no vendor states logging is absent). | High |
| F5 | Injection | Retrieval of content authored by parties other than the user. | High |
| F6 | Sharing | Outbound sharing, sending, or requests to arbitrary hosts. | Medium |
| F7 | Action | Write, send, delete, or other state-changing tools. | Critical-weighted |

### Scoring rule — highest severity met, not a sum

- **Critical** — F7 *and* any of F1, F3, F4.
- **High** — F7, *or* two or more of F1–F5.
- **Moderate** — one High factor, or multiple Medium factors.
- **Low** — otherwise.

### Bands and restricted scores

- Every connector is scored **twice, as a band**: lower bound treats every U as N; upper bound treats every U as Y. The band is the honest answer when documentation is silent.
- **Restricted score:** where a write-limiting control is documented, F7 is set to N and the connector is re-scored. A dash (—) means no such control was documented.

## 3. The dataset — full coded table

Reproduced exactly as coded. Documentation retrieved 2026-11-09 for all 13 rows. The machine-readable version is [`audit/coding-sheet.csv`](../audit/coding-sheet.csv).

| Connector | F1 | F2 | F3 | F4 | F5 | F6 | F7 | Default score (lower → upper) | Restricted score |
|---|---|---|---|---|---|---|---|---|---|
| MCP Filesystem | U | N | U | U | Y | N | Y | High → Critical | Moderate → High |
| MCP Git | N | N | U | U | Y | N | Y | High → Critical | — |
| MCP Memory | Y | N | Y | U | N | N | Y | Critical → Critical | — |
| MCP Fetch | U | N | U | U | Y | Y | N | Moderate → High | — |
| GitHub MCP | Y | N | N | U | Y | Y | Y | Critical → Critical | High → High |
| Notion MCP | U | Y | Y | U | Y | N | Y | Critical → Critical | High → High |
| Atlassian MCP | U | Y | Y | U | Y | Y | Y | Critical → Critical | High → High |
| Linear MCP | N | N | Y | U | Y | N | Y | Critical → Critical | High → High |
| Sentry MCP | N | N | U | U | Y | N | U | Moderate → Critical | — |
| Stripe MCP | Y | N | Y | N | Y | Y | Y | Critical → Critical | — |
| Slack MCP | Y | N | N | N | Y | Y | Y | Critical → Critical | High → High |
| MS Graph perms. | Y | Y | Y | U | Y | U | Y | Critical → Critical | High → High |
| Claude connectors | Y | Y | Y | U | Y | Y | Y | Critical → Critical | High → High |

### Factor prevalence (n = 13)

| Factor | Y | N | U | Reading |
|---|---|---|---|---|
| F1 Sensitive data | 6 | 3 | 4 | Sensitive data reachable in at least 6; undocumented in 4. |
| F2 Aggregation | 4 | 9 | 0 | Cross-system reach is the exception, and it is documented either way. |
| F3 Credential | 7 | 2 | 4 | Broad or shared credentials in 7; undocumented in 4. |
| F4 Logging | 0 | 2 | 11 | Never Y by design. Logging documented for 2; silent for 11. |
| F5 Injection | 12 | 1 | 0 | Third-party-authored content retrieved by 12 of 13. |
| F6 Sharing | 6 | 6 | 1 | Outbound sharing split evenly. |
| F7 Action | 11 | 1 | 1 | State-changing tools in 11 of 13. |

## 4. Reproduce it yourself

The scanner in the GitHub repository — `src/paara_scanner` — reproduces all 13 bands exactly from the coding sheet: **9 Critical lower / 12 Critical upper, 20 tests passing**.

```bash
# Clone the kit
git clone https://github.com/vkktask/paara-connector-audit-kit
cd paara-connector-audit-kit

# Print the full audit table from the coding sheet
PYTHONPATH=src python -m paara_scanner audit

# Verify the coding sheet against the scoring rule
PYTHONPATH=src python -m paara_scanner check

# Score a single connector row
PYTHONPATH=src python -m paara_scanner score
```

If your run disagrees with any score on this page, that is a finding — please open a GitHub issue with the connector name and your output (see [Corrections](#10-corrections-and-right-of-reply)).

## 5. Limitations — read before citing

- **Single coder.** All 13 connectors were coded by the author alone, with AI-assisted retrieval. **No inter-rater reliability is reported.** A second coder is explicitly invited — the coding sheet and rules above are everything you need.
- **Documentation is not behaviour.** This audit scores what vendors document, not what a connector actually does at runtime. An undocumented control may exist; a documented control may not work as described.
- **Convenience sample.** 13 widely used, well-documented connectors, chosen for documentation quality — not a random or representative sample of the connector ecosystem.
- **Judgement calls.** Several codes — especially N versus U, and whether content counts as "authored by parties other than the user" — involve coder judgement. Different reasonable coders may differ; that is what the band (U = N → U = Y) is for.
- **No predictive-validity claim.** A Critical band means the documented risk factors combine in the most severe pattern under this rule. It is not a prediction that a breach will occur.
- **Snapshot.** Documentation retrieved 9 November 2026. Connector documentation changes frequently; scores are versioned to that date and will drift.

## 6. Caveats and open issues

1. **Not independently verified.** The headline counts are the author's audit. This page publishes the dataset and method *before* the headline claims are used elsewhere, so anyone can check them first.
2. **PAARA component count — presented as a range: 6–8.** PAARA is cited on this page as a *6–8 component* methodology. The SSRN abstract describes it as *six-component*; the ICAIC 2027 paper refers to an *eight-component* process. Rather than force one number, this page presents the range and names both sources, so readers can see exactly where each count comes from. That is fine — the method is still growing, the evidence base is still growing, and neither we nor the world are perfect. The six components are listed in the repository README.
3. **Regulatory submissions — paper-sourced only.** The SSRN abstract states that regulatory submissions based on PAARA were filed with the UK ICO, CNIL, IMDA Singapore, and NIST in May 2026. That is corroborated only from the paper itself, not from any regulator website. Nothing on this page claims regulator endorsement or adoption.
4. **Preprint status.** SSRN is a preprint server. Papers are cited on this page with title, venue, and DOI every time — see [Papers](#9-papers--cited-in-full), below — and "submitted / awaiting decision" is not peer review.
5. **MCP Filesystem restricted-score check.** Checked in the repository copy used for this page: `coding-sheet.csv` *does* contain restricted scores of Moderate → High for MCP Filesystem, matching the audit table above and the scanner output. An earlier flag that those columns were blank does not hold in this copy. No numbers were changed to make this so — this note records the check.

## 7. How to use the kit on your own connectors

1. **Inventory.** List every connector, MCP server, and agent integration in scope — including the ones developers added themselves.
2. **Code, with evidence.** Code F1–F7 from official documentation only. For every code, record verbatim evidence of **25 words or fewer** plus the source URL. No evidence, no code — use U.
3. **Score as a band.** Apply the scoring rule twice: U = N for the lower bound, U = Y for the upper bound. Report the band, never a single point.
4. **Restrict and re-score.** Where a write-limiting control is documented, set F7 = N and re-score. Record both scores.
5. **Own the unknowns.** Every U is an open risk with a named owner and a question to the vendor — not a pass. Carry them into your risk register as-is.

## 8. Templates and vendor questions

Full template files are in the GitHub repository (`templates/`). The working contents are summarised here so this page stands alone.

### Connector audit checklist

- Connector name, vendor, version, and documentation URLs recorded; retrieval date noted.
- F1–F7 coded, each with verbatim evidence (≤ 25 words) and URL.
- Default band scored (lower → upper) and checked against the scoring rule.
- Write-limiting controls identified from documentation; restricted band scored, or "—" recorded.
- Logging: is server-side retrieval / audit logging documented, stated absent, or silent?
- Prompt-injection guidance: documented, or absent?
- Transport: TLS version, token-signing algorithm, post-quantum support — documented or U?
- Every U assigned an owner and a vendor question; review date set.

### Connector DPIA template — headings

1. **System & connector description** — what it connects, whose data, which agent acts through it.
2. **Data map** — F1 categories reachable, F2 systems aggregated, data subjects affected.
3. **Credentials & access** — F3 model, scope, rotation, revocation.
4. **Actions & safeguards** — F7 tools, write-limiting controls, human approval points.
5. **Third-party content risk** — F5 sources, prompt-injection handling, F6 outbound paths.
6. **Logging & accountability** — F4 position; how an incident would be reconstructed.
7. **Necessity, proportionality & residual risk** — band before and after restrictions; unknowns carried as open risks; sign-off.

### Vendor attestation questions

Ask in writing. "Not documented" is an answer — record it as U.

- Which personal, financial, private-communication, or security data can this connector reach?
- Does it aggregate across separately administered systems? Which?
- What credential model does it use — per-user, app-level, service account, shared, or agent keys? How are keys scoped, rotated, and revoked?
- Is server-side retrieval and audit logging provided? What is logged, for how long, and who can access it?
- What prompt-injection defences apply to third-party-authored content the connector retrieves? Where is this documented?
- Can it share, send, or make requests to arbitrary hosts? Can that be allowlisted?
- Which tools change state — write, send, delete? What write-limiting or approval controls are documented?
- What TLS version and token-signing algorithm are used? Is post-quantum support on the roadmap?

## 9. Papers — cited in full

### PAARA — SSRN preprint

Vivek Kumar, PAARA (Privacy-Aware AI Risk Architecture), SSRN preprint, posted 28 May 2026.

DOI: [10.2139/ssrn.6784078](https://doi.org/10.2139/ssrn.6784078)

SSRN is a preprint server; this is not a peer-reviewed publication.

### The connector audit — ICAIC 2027

Vivek Kumar, "How Well Documented Are AI Connector Risks? Applying the PAARA Governance Methodology to Thirteen Public MCP and Enterprise Connectors," ICAIC 2027 (6th IEEE International Conference on AI in Cybersecurity).

Submitted 14 November 2026 · CMT Paper ID 302 · Status: **Awaiting Decision**. Submitted is not accepted, and accepted would not by itself verify the dataset — the coding sheet above is the checkable record.

## 10. Corrections and right of reply

Scores are **versioned to the 9 November 2026 documentation snapshot**. If you are a vendor named here, or a reader who finds a code that the cited documentation does not support, you have a right of reply: open an issue on [GitHub Issues](https://github.com/vkktask/paara-connector-audit-kit/issues) with the connector, the factor, and the documentation link. Supported corrections will be applied to the coding sheet, re-scored with the scanner, and noted as a version change — never silently edited.

---

*PAARA Dataset and Method · Vivek Kumar, Independent professional (AI Governance & Data Privacy, Cyber GRC) · [vivekkumar.tech](https://www.vivekkumar.tech/) · Code and data: [github.com/vkktask/paara-connector-audit-kit](https://github.com/vkktask/paara-connector-audit-kit)*

*Dataset snapshot: documentation retrieved 9 November 2026. Headline counts are the author's audit and are not independently verified. This page makes no claim of peer review, regulator endorsement, or regulator adoption for the audit or for PAARA.*

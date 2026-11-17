# The Connector Audit — Issue #48

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #48 headline: One Year of Mondays — forty-eight issues in, the Monday fixes add up to a programme, not a pile of tips: an operating system for the connector layer, assembled one small, filed, dated fix at a time. Plus the year assembled on one page — inventory, five questions, gates, ladder, drills, gap loop, quarterly rhythm, annual re-audit — and a comment on the adversarial machine learning taxonomy, sent to NIST. Stated plainly, in the same issue: the 48 teardowns are designed and the filming is scheduled, and not one live score exists yet.**

---

## 1. The Connector Pattern — the fix that repeats: governance as a calendar, not an event

This week's pattern is not a connector. It is a rhythm, and it is the pattern underneath every other pattern this series has published.

Compare two estates. In the first, connector governance happens in events: an assessment project when the auditors ask, a review sprint when a regulator writes, a remediation programme after an incident. Between events, nothing is scheduled, so nothing happens — scopes drift (Issue #4), owners leave (Issue #16), vendor updates land unexamined (Issue #14), and the estate's true state diverges from its documented state a little more each week, silently.

In the second estate, governance happens in a rhythm: one small fix every Monday, each with an artefact filed — a baseline pinned, a gap given an owner and a date, a kill switch drilled, a connector re-audited. No single fix is impressive. The fixes are not the point. The point is that the interval between examinations is one week, so drift is measured in days, and the estate's documented state and its real state are never more than a few fixes apart.

That is a pattern, not a finding — a property of calendars, not of any vendor's product, and no score is published for it. The check is in your own estate, and it takes one question: when did governance last touch each of your connectors — an event, or last Monday? The rest of this issue is what forty-eight Mondays of the second pattern add up to, what they honestly do not yet add up to, and the one-page system they assemble into.

## 2. Field Note — One Year of Mondays

Forty-eight issues ago this newsletter set itself a discipline: every issue ends with one Monday fix — small enough to do in under an hour, specific enough to file, and honest enough to record what it found. This field note is the audit of that discipline, conducted under its own evidence rule (Issue #25): claims with artefacts beside them, and the gaps stated on the face of the record.

What the year adds up to, with artefacts: a method, published — the PAARA documentation audit of 13 public connectors (documentation retrieved 9 November 2026; 9 Critical at the lower bound of the band, 12 at the upper, none Low; server-side audit logging documented for 2 of 13, Slack and Stripe; prompt-injection guidance documented for 1 of 13, Stripe), with the dataset, the scoring rule and the kit open source, and the kit released as v1.2 on 16 November 2026. A training course, published — Modules 0–7 and a capstone, free. A teardown series, designed — 48 Connector Spy Tests across 24 stores, every store from two AI sides, each with its four checks, filming checklist and thread drafted. A file of regulator comments, sent — to NIST, the UK Law Commission, Canada's OPC, Australia's DEWR, Japan's PPC, the IETF and others, each reported in these pages at exactly the status it earned: sent, or submitted, never adopted, never accepted. And forty-eight Monday fixes, which assemble — Section 3 — into a complete operating system for the connector layer.

What the year does not add up to, stated as plainly: not one teardown has been filmed. All 48 scorecards are blank, by design and by the series' founding rule — scores are filled only from filmed live tests on test accounts with dummy data, never copied from documentation, from the audit, or from the other side of a pair. The filming plan exists (16 sessions, three films each, the two audited integrations first), the dry run is written up (Issue #44), the gap list is open (Issue #45) — and zero live scores exist. Anyone who tells you their programme is further along than its evidence should be asked for the artefacts. This one is asked, here, by its author: the method is proven on paper, unproven on camera, and the difference is the whole of next year's work.

That honesty is not a confession bolted onto a celebration. It is the discipline itself. A pile of tips does not compound; a programme does, because a programme keeps its records — baselines, gaps, diffs, drill timings — and records are what let the forty-ninth week start from evidence instead of from memory. One year of Mondays is not forty-eight tips. It is a register, a rhythm and a standard of proof, and it is ready — as this issue's Monday fix sets out — to be run by any estate willing to start smaller than its ambitions.

## 3. Harness — The year assembled: the connector operating system on one page

Forty-seven issues built the parts. This section is the index of those issues read as one system — eight components, in the order an estate adopts them, each with the artefact it produces. Nothing here is new. That is the point: the system was the issues, all along.

**1. The inventory (Issue #34; Training Module 0).** Every connector actually live — approved, team-enabled, personal-account — in one register, keyed by data source, each with a living owner of record. Artefact: the register. Without it, every later component governs a fiction.

**2. The five questions (Issue #24; Module 1).** Asked in writing before any approval: what can it reach; does it touch sensitive data; is it least-privilege, or broader than needed; can you reconstruct what it did afterwards; how does it amplify insider risk. Artefact: the answered card, filed with the approval, silences scored as unknown.

**3. The six gates (Issues #3, #4, #5, #6, #11, #28 in harness form throughout).** The harness evaluation an agent must pass before it acts: identity binding; scope by delegation; exactly-once consequential actions; anomalies noticed by a human, not just logged; an external kill switch, drilled; consent on regulated data. Scored 0–4, evidence or it caps at the floor, and a failed gate is never averaged green. Artefact: the gate scores with their evidence.

**4. The action ladder (Issue #11).** Every connector placed on a tier — Observer, Contributor, Operator — stating what it may do alone, what needs a named human first, and what it may never do; promotion earned by evidence, demotion triggered in writing. Artefact: the ladder, per connector, in the approval record.

**5. The drills (Issue #10).** The kill switch taken end to end on a stopwatch; the one-hour reconstruction from logs alone (Issue #21); the leaver's-token walk (Issue #16). The only components that test the estate rather than describe it. Artefact: the drill records, failures included.

**6. The gap loop (Issue #45).** Every gap fielded with a severity graded by the action left ungoverned, one named owner, a date set against the event the gap protects, and closure only on a filed re-test artefact — silent expiry converted, in the meeting, to signed risk acceptance. Artefact: the gap list, living.

**7. The quarterly rhythm (Issue #47).** Four activities per quarter, none incident-triggered: the inventory sweep, the gap review, the re-audit sample, the rotating drill. Artefact: four filings a quarter — the difference between calm that is earned and calm that is merely unexamined.

**8. The annual re-audit (Issue #46).** Every connector diffed against its pinned baseline (Issue #27) within twelve months, pulled forward by the triggers (Issue #13): scope change, tool-definition change, vendor change, new data class — plus owner change, tier change, vendor incident. Artefact: the diff and the new baseline.

Eight components, eight artefacts, one page. An estate that runs all eight does not need this newsletter's forty-eight issues; it is living them. An estate that runs none of them does not need a programme launch either — it needs component 1, next Monday, in under an hour.

## 4. Regulator / Industry-Body Update — NIST SP 2400-102e2026: a comment on the AML taxonomy, sent

This week's update is a comment, reported at exactly that status — sent, nothing more.

On 16 November 2026, Vivek Kumar sent comments to **NIST** on the public draft of **SP 2400-102e2026**, the adversarial machine learning taxonomy — the draft that extends the AML taxonomy toward agentic systems. The comment made eight asks, each one a place where the taxonomy's agentic coverage stops at the model and the incidents happen at the connection: name the connector layer as an attack surface in its own right; distinguish documented controls from undocumented ones when a technique's mitigations are listed, because silence in vendor documentation is not a defence in place; treat connector prompt injection — hostile instructions arriving through connected content — as a first-class technique; add tool-call hijacking; address excessive permissions and write-limiting as mitigations, not afterthoughts; include connector audit logging among the detection evidence a defender can actually consult; document transport and identity expectations for agent connections; and add glossary terms for the failure modes practitioners already name — the rug pull, where an approved tool's definition changes after approval, and the rogue MCP server.

Why a taxonomy comment belongs in this newsletter: taxonomies decide what incident reports can say, and what incident reports can say decides what governance gets funded. A taxonomy with no connector layer produces incident data with no connector layer, and the pattern this series documents stays invisible in the official record. What is claimed here is only the sending: the comment was submitted to NIST during the draft's public comment process, the taxonomy is NIST's to finalise, and no adoption, acceptance or influence is stated.

## 5. The Monday Fix — assemble your year

Forty-five minutes, this Monday. Do not start a programme. Assemble one, from the page in Section 3:

1. **Score your estate against the eight components.** For each — inventory, five questions, gates, ladder, drills, gap loop, quarterly rhythm, annual re-audit — write one word: running, partial, or absent. Judge by artefacts, not intentions: a component with no filed artefact is absent, whatever the policy says (Issue #25).
2. **Pick the highest-exposure absence.** Not the easiest gap — the absent component sitting under your highest-tier connector. For most estates this is the inventory or the ladder; for estates with both, it is usually the drills, the only components that test rather than describe.
3. **Schedule that one component as a recurring Monday entry.** Named owner, filed artefact, first run dated before this month ends. A system adopted one component per quarter is fully assembled in two years; a system adopted all at once in a launch workshop is usually assembled never.
4. **Write your own honest line.** One sentence, in the record, stating what your programme has not yet proven — the equivalent of this issue's: teardowns designed, filming scheduled, no live scores. The estates that can write that sentence are the ones whose other sentences can be believed.

Score the connector before you trust it — and assemble the system before you announce it, because a programme is what the Mondays add up to, not what the launch deck says.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

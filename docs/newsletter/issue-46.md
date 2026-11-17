# The Connector Audit — Issue #46

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #46 headline: The Second Audit — a year after approval, the connector you re-audit is not the connector you approved: scopes drifted, the vendor shipped, the owner moved, and the first audit's unknowns were never revisited. Plus the annual re-audit cycle — calendar, triggers, diff against baseline — and a review comment on agent delegation, sent to the IETF.**

---

## 1. The Connector Pattern — the connector, one year on: same name, different grant

This week's pattern is a comparison, and the comparison is the finding: one approved connector, described twice — once in its approval record, once as it runs today.

In the approval record, written a year ago: a read-heavy integration, a named owner, a defined data class, a review date. As it runs today: the same product name on the register, and underneath it a different object. A vendor update widened a scope in a release nobody connected to the approval (Issue #14). A new data class came into reach when a second team started using the same grant for a second purpose (Issue #4). The owner changed teams in a reorganisation and the register still carries the old name (Issue #16, at estate scale). The log configuration the first audit recorded as "to be confirmed" is still to be confirmed — the unknown was filed, politely, and never revisited.

None of this required an attacker, a breach or a bad decision. It required only time. Approvals are written about a moment; connectors live in a stream of vendor releases, team changes and quiet configuration edits. The distance between the two descriptions is not an anomaly in one estate — it is the default state of any connector that has been approved once and never re-audited. The first audit, however good, has a shelf life, and the shelf life is shorter than the approval's.

That is a pattern, not a finding. No vendor is named and no score is published here, because the drift described is a property of approval processes, not of any one product. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Second Audit

The first audit asks: should this connector be trusted? The second audit asks a harder question: is the thing we trusted still the thing that is running?

Re-auditing a connector a year later produces three kinds of discovery, and only one of them is about the connector. The first is **what changed**: scopes added by vendor updates, tool definitions revised, sub-processors swapped, a data class that arrived when the business found a new use for an existing grant. This is the drift Issue #13 named at the level of the tool — the rug pull is only the deliberate version; the ordinary version is a changelog. The second discovery is **what drifted without changing**: the owner who moved, the review meeting that stopped happening, the log nobody has opened since the first audit opened it, the revocation route that was walked once, in a drill, by someone who has since left. Nothing in the configuration moved; everything around it did. The third discovery is the uncomfortable one — **what the first audit missed**: the question that was answered from the datasheet instead of the tenant (Issue #6), the unknown that was recorded as a sentence instead of a gap with an owner and a date (Issue #45), the second system the same grant quietly reached (Issue #5). A good second audit is partly an audit of the first one.

This is why the second audit cannot be a photocopy of the first. Re-running the original checklist against the current tenant will catch changed scopes, but it will not catch the questions the original checklist never asked. The re-audit has two inputs, not one: the baseline the first audit froze, and the list of everything the programme has learned since — every field note, every incident pattern, every new check the method has grown. The connector is re-scored against the method as it now stands, not as it stood when the approval was granted.

And a word on tone, because it decides whether re-audits happen twice. A second audit that reads as an accusation — who let this drift? — will be resisted, softened and eventually scheduled out of existence. Drift is the normal behaviour of a living estate, not evidence of negligence. The re-audit's posture is the gap list's posture (Issue #45): findings are statements about the estate, never about a person. The programmes that re-audit annually are the ones where the first re-audit was treated as maintenance, not blame.

## 3. Harness — The annual re-audit cycle: calendar, triggers, diff against baseline

A re-audit that depends on someone remembering is a re-audit that happens once. The cycle below makes it structural — and it is assembled entirely from machinery earlier issues built.

**The calendar.** Every approved connector carries a re-audit date, set at approval and never more than twelve months out, staggered across the year so the estate is never re-audited in a single heroic month. The date lives in the approval record next to the owner (Issue #11's ladder entry, Issue #34's owner-of-record rule). When the date arrives, the re-audit is not optional and does not need a business case: it is the rent the connector pays for staying on the approved list. A connector whose re-audit is ninety days overdue is suspended to read-only or disconnected — a consequence agreed in advance, in writing, so enforcing it is administration rather than confrontation.

**The triggers.** The calendar is the floor, not the ceiling. Issue #13's re-approval triggers — scope change, tool-definition change, vendor or sub-processor change, new data class in reach — each pull the re-audit forward to now, and Issue #27's change control supplies the mechanism: the baseline is pinned, the change is diffed, the re-approval is recorded. To those four, the second audit adds three more learned the slow way: the owner changes; the connector's tier on the action ladder changes; the vendor suffers an incident touching its integration layer — the Drift lesson of Issue #35's companion cases, where the approval's assumptions about a third party's token hygiene stopped being true overnight.

**The diff against baseline.** The re-audit's core artefact is not a new scorecard; it is a diff. Issue #27's pinned baseline — scopes, tool definitions, data classes, vendor and sub-processors, owner, log configuration, as approved — is compared line by line with the tenant as it runs. Every differing line becomes one of three things: an approved change whose record was never attached (file it), an unapproved change (a gap, run through Issue #45's loop — severity, owner, date, re-test), or a baseline error from the first audit (correct the baseline, and record what the first audit missed, because that list improves the method). The connector is then re-scored under Issue #25's evidence rule — artefacts in hand, or the score sits at the floor — and the new baseline is pinned for next year. The sweep discipline of Issue #34 runs underneath all of it: each quarter, confirm every connector on the list still has a living owner and a future re-audit date; each year, do the deep diff. Calendar, triggers, diff — a connector that passes all three has earned its second year. One that has never faced them has merely survived it.

## 4. Regulator / Industry-Body Update — IETF Acts-For: a review comment sent

This week's update is a comment, reported at exactly that status — sent, nothing more.

On 16 November 2026, Vivek Kumar sent review comments to the IETF's agent-protocol mailing list (agentproto@ietf.org) on **draft-morrison-acts-for-01**, a draft addressing how an agent acts on behalf of a person or system — the delegation question at the heart of every connector approval. The comments raised three points, each drawn from the connector evidence this newsletter is built on: **revocation** — a delegation that cannot be withdrawn quickly and completely is a grant, not a delegation, and the draft should say how withdrawal propagates; **audit logging** — an act performed on someone's behalf must leave a record that distinguishes the agent's action from the principal's, or accountability dissolves into the shared-account problem of Issues #15 and #36; and **per-action scope** — authority should be expressible per action, not only per session or per connection, because the blast radius of an agent is set action by action (Issue #9's 37 tools). The note also carried the IPR flag the draft's own terms call for.

Why a protocol draft belongs in a connector newsletter: the standards being written now for agent delegation will decide what the next generation of connectors can even express — whether "act for me, but only this, and stop when I say stop" is a protocol feature or a vendor promise. Comments filed while a draft is young are how practitioner evidence reaches that layer. What is claimed here is only the sending: the comment is on the list's record, the draft is its authors' to revise, and no adoption, acceptance or influence is stated.

## 5. The Monday Fix — schedule one connector's second audit

Forty-five minutes, this Monday. Pick the connector in your estate that was approved longest ago and has never been re-audited — there is almost always one — and put its second audit on the calendar before the meeting ends:

1. **Pull the baseline.** Find the original approval record: scopes as granted, data classes, owner, log configuration, review date. If the baseline was never pinned, say so in the new record — reconstructing it from the tenant and the vendor's changelog is now item one of the re-audit, and the missing baseline is itself the first gap.
2. **Run the quick diff.** Compare the baseline against the connector as it runs today on just four lines: scopes, tool definitions, data classes, owner. Expect at least one difference. Each difference is filed, gapped, or corrected per Section 3 — none is waved through as "probably fine".
3. **Set the cycle in writing.** In the approval record: the re-audit date within twelve months, the seven triggers from Section 3, the overdue consequence, and the owner's name as it is today — not as it was at approval.
4. **File the first-missed list.** One line for anything the original audit never asked — a check the method has since grown, a system the grant also reaches, a log never opened. That list is next year's checklist improving itself.

Score the connector before you trust it — and audit it again before you trust it twice, because the second audit is the one that checks the trust, not just the connector.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

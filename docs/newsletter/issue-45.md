# The Connector Audit — Issue #45

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #45 headline: The Gap List — the dry run's gap list is the most honest document in the programme: gaps with owners and dates beat scores without evidence, every time. Plus gap management — severity, owner, date, re-test — and a comment on AI in the workplace, submitted to Australia's DEWR.**

---

## 1. The Connector Pattern — the gap list behind the approval: every connector carries one, filed or not

This week's pattern is the document that decides whether everything else in this newsletter is real: the gap list standing behind a single approved connector.

Take the connector at the front of this series' filming plan — Slack → Claude via MCP, Teardown #31, drafted, scores blank until filmed. Its dry run (Issue #44) produced exactly the kind of list every connector in your estate is carrying right now, whether anyone has written it down or not: a check that assumes an admin console the current plan tier may not include; a log trail split across consoles, so reconstruction fails on navigation before it fails on logging; a control item whose reachability has a boring legitimate explanation that has to be closed or re-scoped before it can prove anything; a stop condition naming a switch whose owner has not yet been confirmed. Four gaps. None of them is a finding about Slack or about Claude. All of them are findings about the distance between the approval on file and the estate as it actually runs.

That distance exists for every approved connector — the scope that widened after the review, the log nobody has ever opened, the owner who changed teams, the revocation route that has never been walked. The only question is whether the gaps are written down, owned and dated, or whether they are distributed across the memories of people who are slowly leaving. An unwritten gap list does not mean a connector has no gaps. It means the gaps will be introduced to you later, by an auditor, an incident review, or an attacker — each a more expensive presenter than a dry run.

That is a pattern, not a finding. No vendor score is published here, because none has been earned yet: Teardown #31 remains a pre-filming draft, and the gap list it produced is evidence about the plan and the estate — never about the connector. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Gap List

Issue #44 argued that the gap list, not the fixed plan, is the artefact that leaves a dry run. This issue goes one step further: the gap list is the most honest document in the entire connector-governance programme — more honest than the approval record, more honest than any scorecard, including the ones this series will eventually publish.

The reason is structural. Every other document in the programme is written to conclude something: the approval concludes the connector is acceptable, the scorecard concludes how it performed, the policy concludes the rules are adequate. The gap list is the one document written to record what is *not yet true* — the control that is assumed but untested, the artefact that is claimed but not in hand, the route that is documented but unwalked. It is the only artefact whose quality rises with how uncomfortable it makes its author. A gap list with no embarrassing entries is not a sign of a healthy estate; it is a sign the listing was done politely.

Compare two programmes. The first has scores: a dashboard of greens, earned — as Issue #25 warned — from briefings, documentation and confident claims with no captured artefact, each one capped, under an honest evidence rule, at the floor of the scale. The second has no scores yet, but it has a gap list: forty-one gaps, each with a severity, a named owner and a closing date, each closing only when the re-test artefact exists. The first programme looks finished and knows nothing. The second looks unfinished and knows exactly where it stands. Given a connector estate to defend in front of a board, a regulator or an incident review, the second document is the one you want in your hand — because "here is what we know is missing, who owns it, and when it closes" is an answer, and a green dashboard built on unexamined claims is a postponement.

Two disciplines keep a gap list honest, and both are cheap. The first is that gaps are never deleted, only closed: a closed gap stays on the list with its closing evidence and date, so the list is also the programme's memory of what it used to get wrong — the record Issue #27's change control and Issue #44's checklist both depend on. The second is that a gap is a statement about the estate, never about a person: the moment listing a gap feels like confessing a fault, the listing stops, and the politeness returns. Leaders set this tone personally. The first gap on the first list should be one the most senior person in the room owns.

## 3. Harness — Gap management: severity, owner, date, re-test

A gap list becomes a control when each gap runs the same loop. Four fields per gap, no exceptions, and a closing rule borrowed directly from Issue #25's evidence standard.

**Severity — what the gap lets happen.** Rate the gap by the action it leaves ungoverned, not by how easy it feels to fix. A missing log view on a read-only connector is an inconvenience; an unwalked revocation route on a write-capable connector is a standing exposure. Use the connector's own tier from the action ladder (Issue #11): the higher the rung the agent sits on, the higher every one of its gaps rates. Severity is set once, by the reviewer, and is not negotiable downward by the owner — the person closing a gap does not get to re-grade it first.

**Owner — one person, by name.** Not a team, not a function, not "security". The owner is the person who will produce the closing artefact. Where a gap genuinely spans two teams, it still gets one owner, whose job is the chasing. Issue #15's shared mailbox and Issue #16's leaver's token are both, at root, gaps that had a system for an owner and a person for a surprise.

**Date — a closing date before the thing the gap protects.** A gap's date is set against the event it guards: the film, the go-live, the renewal, the re-approval. "Next quarter" is not a date. If the protecting event arrives first, the gap converts — explicitly, in writing — into a risk acceptance signed by someone senior enough to accept it, or the event waits. What a gap may never do is silently outlive its event and carry on as background.

**Re-test — the gap closes on evidence, or it does not close.** This is Issue #25's rule applied to remediation: *evidence or it didn't happen*. A gap raised because a log trail could not be reconstructed closes when a reconstruction is performed and the extract is filed — not when a ticket says the logging was "reviewed". A gap raised because the kill route was unwalked closes with the drill record and its time. The re-test is run, where possible, by someone other than the owner (Issue #12's second-coder discipline, applied to fixes), and the artefact joins the approval record next to the original gap entry. The loop — finding, severity, owner, date, re-test artefact — is the whole method. Programmes do not fail at finding gaps. They fail in the space between the finding and the filed artefact, which is exactly the space this loop exists to close.

## 4. Regulator / Industry-Body Update — Australia DEWR, AI in the Workplace: a comment submitted

This week's update is a submission, reported at exactly that status — submitted, nothing more.

On 16 November 2026, Vivek Kumar submitted a comment to the **Australian Government Department of Employment and Workplace Relations (DEWR)** consultation on its **AI in the Workplace** guidance, through the consultation hub's online form. The submission is a matter of record: **submission reference sbm407def0c0eafdc9e0b9ca**. The form offered no free-text field, so the response went in as an uploaded PDF; the respondent details were Vivek Kumar, individual respondent, publication public — DEWR may publish it. The consultation's deadline was 27 January 2027.

Why workplace guidance belongs in a connector newsletter: the guidance is aimed at employers deploying AI in Australian workplaces — which is to say, at exactly the moment a connector gets approved, a scope gets granted and an agent starts acting on staff and customer data under someone's name. Guidance written for that moment lands or fails on the same discipline this issue is about: an employer who can produce, for each AI tool in the workplace, its owner, its reach and its known gaps with dates against them is an employer who can demonstrate the guidance was followed. An employer with a policy and a green dashboard cannot. It is also worth leaders outside Australia noting the direction of travel: workplace-AI guidance is being written jurisdiction by jurisdiction, and the evidentiary expectations are converging on the same artefacts everywhere.

What is claimed here is only the submission. No outcome, adoption or influence is stated: the guidance is DEWR's to finalise, the comment is one submission among those it received, and it is reported here because this newsletter reports its author's submissions as submissions, never as results.

## 5. The Monday Fix — give one connector's gaps the full loop

Forty-five minutes, this Monday. Pick the connector your organisation would least like to explain in an incident review, and run Section 3's loop on what is already known about it:

1. **List the gaps you already know.** Not a fresh audit — the ones the team carries in its head: the log nobody has opened, the scope that widened, the owner who moved, the revocation route never walked. Write them down, one line each. Expect five to ten. If the room produces none, the listing was polite; start again with the most senior person's own gap.
2. **Field every gap.** Severity by the action left ungoverned, one named owner, one closing date set against the next event the gap protects — a renewal, a re-approval, a go-live. Four fields, no gap left as a sentence in a chat thread.
3. **Close the cheapest one in the room.** There is usually a ten-minute artefact available: open the log and file the extract, walk the revocation route and record the time, name the owner in the approval record. Close it under the evidence rule — artefact in hand, entry marked closed, not deleted.
4. **File the list with the approval record.** Gaps, fields, closing evidence and all. The next review of this connector starts from this list, and the diff between the two lists is the record of the estate getting more honest.

Score the connector before you trust it — and keep the gap list closer than the scorecard, because the scorecard says what you concluded, and the gap list says what you know.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

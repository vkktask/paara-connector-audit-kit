# The Connector Audit — Issue #43

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #43 headline: The First Film — 48 Connector Spy Tests are designed and not one has met a real tenant yet; the first film is where the plan stops being a document, and where the method itself gets tested: what survives contact with a live workspace, and what adapts, on the record. Plus session discipline — the session sheet, the dummy-data pack, and a second coder in the room — and the Apart Research Agent Attribution sprint, 11–13 December 2026, reported as an upcoming sprint.**

---

## 1. The Connector Pattern — the first store in the filming order: the workspace where a documented claim is waiting

This week's pattern is a single teardown, because the filming plan gives it a job no other teardown has. Ahead of Connector Spy Test #31 (Slack → Claude via MCP, drafted, scores blank until filmed) — first in the filming order set out in the Series Index:

- Slack is the store this series reaches three ways: the native connector to ChatGPT (#2), the native connector to Claude (#7), and the MCP route to Claude (#31). Same workspace, three grants, three approval surfaces, three log stories. The matrix has made that point 24 times; #31 is where it stops being an argument and becomes a measurement.
- #31 is one of only two teardowns in the 48 whose integration also appears in the published 13-connector documentation audit. As an MCP connector, Slack was coded there — and its documentation states server-side audit logging, so the logging factor was coded present (F4 = N), one of only two connectors of the 13 to document it. A claim exists, in writing, in the dataset. The film can check it: run the session, then try to reconstruct it from the logs the documentation describes.
- That is why it films first, ahead of stores leaders feel more keenly. Every other teardown generates a first answer. This one tests an existing answer — and, with it, the documentation audit the whole series stands on. If the film confirms the documented logging, the audit's method gains its first live corroboration. If it does not, the disagreement is the finding, and it is published unedited (the rule is fixed in Section 3 of Issue #42 and in #31's own page).

That is a pattern, not a finding. No vendor score is published here, because none has been earned yet: Teardown #31 is a pre-filming draft, to be filmed on a test workspace with dummy data only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The First Film

For 42 issues this newsletter has described a series that exists entirely on paper: 48 test designs, every question fixed in advance, every scorecard blank. Paper is a comfortable medium for a method. On paper, the four checks take as long as they take. The control item is exactly where the checklist says it is. The plan never meets a plan tier.

The first film ends that. Not because a score appears — one scorecard, filled, is a small thing next to 48 — but because the first film is the first time the *method* is the thing being tested. A test design can be wrong in ways its author cannot see from the page: a check that assumes a settings screen the test account's plan does not have; a control item that turns out to be reachable for a boring, legitimate reason the checklist did not name; a log trail that exists but is split across two consoles, so the one-hour reconstruction standard from Issue #21 fails on navigation, not on logging. None of that is visible until a camera is pointed at a live tenant and the session sheet meets the workspace as it actually is.

So the honest expectation, stated before the film rather than after it: the plan will bend. Some of it will bend in the filming — a step reordered, a check re-scoped, a caveat promoted from the still-missing box into the method. That bending is not the series failing. It is the difference between Issue #24's two words made visible: the teardown pages are *documented*; the film is *tested*, and the method has to submit to its own distinction. What does not bend is the discipline around the bending: every adaptation is written into the teardown page, dated, next to the original checklist — questions first, answers second, and the edits in between on the record, never silently absorbed. A method that adapts in public is stronger than one that pretends it never had to.

What changes downstream is the same list Issue #42 gave, now with a date attached to the first item instead of the whole matrix: one scorecard filled from footage, one verdict, one setting the film earns the right to name, one X thread posted as a result instead of a plan, one newsletter pattern section that can finally say *finding* about one integration — or one published disagreement between a vendor's documentation and a camera, which is worth more. Leaders run the same transition every time an approved-on-paper control meets production. The ones who handle it well are not the ones whose plans never bend. They are the ones who wrote the plan down first, so the bend is visible — and who treat the first live run as a test of the control's design, not just of the connector. Section 3 is the discipline that makes a first film evidence rather than content.

## 3. Harness — Session discipline: the session sheet, the dummy-data pack, and a second coder in the room

A filmed test is evidence only if the session was run like an audit, not a shoot. Three artefacts carry that discipline. Each one exists before the camera starts; each one is filed after it stops.

**The session sheet.** One page per session, written in advance (Issue #42's Monday fix built the first one): the films in order, the four checks for each, the control item for each, the evidence each check must capture — a screenshot, a log extract, a config export — named before the session runs, under Issue #25's rule that a test names its artefacts up front and a confident claim with no captured artefact caps at the floor of the scale. The sheet also carries the stop conditions: what ends a check early (the agent reaches for anything outside the test workspace; a dummy item turns out to contain something real) and what ends the session. A sheet written after the session is a story. A sheet written before it is a protocol.

**The dummy-data pack.** Built once per store, reused by both sides of the pair, and inventoried like an asset: the dummy channels, records and files; the private item the connecting account was never given; the control item in the never-connected account; the planted hidden instruction, word for word, with where each copy sits. The pack is the consent control from Issue #42 — everything the agent can reach in a film is invented, and everyone a planted instruction could affect is the tester. It is also a reproducibility control: a second run, or the pair's second side, faces the *same* pack, so a difference in outcome is a difference in the grant, not in the bait. When the pack changes, the change is versioned and the earlier films' packs stay on file — a score is only ever read against the pack that produced it.

**A second coder in the room.** Issue #12 made the argument for the dataset: one coder's scores are a claim, two coders' are a measurement. Filming raises the stakes, because a film's scorecard will be quoted as a result. So where possible, the session runs with a second coder: someone who did not design the teardown, scoring the four checks from the footage and the session sheet — not from the room's conversation — while the first coder scores independently. The two scorecards are compared before anything is published; disagreements are resolved against the teardown's written checks, and where the checks could not settle it, the disagreement is published with the scorecard, exactly as Issue #12 prescribed for the dataset. Where no second coder is available, the scorecard says so, in the same plain sight as the dataset's single-coder statement — a limitation named is a limitation priced; a limitation hidden is a claim inflated.

**The agent-specific line.** None of this is production craft. The sheet, the pack and the second coder are the harness pointed at the tester: least privilege in the setup, consent in the data, evidence named in advance, and an independent check on the scoring — the same four disciplines this newsletter prescribes for the connectors being filmed. A series that exempted itself from them would be reviewing everyone else's governance from inside an ungoverned room.

## 4. Update — Apart Research, Agent Attribution sprint, 11–13 December 2026: an upcoming sprint

This week's update is a date in the field's calendar, reported at exactly that status — upcoming, and relevant to the question this whole series asks about logs.

**Apart Research** runs online research sprints in December 2026, and the second of them, **Agent Attribution, runs 11–13 December 2026**. The topic is the one underneath Check 4 of every teardown in this series: when an AI agent acts inside a system, can the action be attributed — to the agent, to the session, to the human who authorised it — from the records that exist afterwards? It is Issue #21's reconstructability question and Issue #36's "whose log tells the story" question, taken up as a research problem in the open.

The judging context, stated at its exact precision: Vivek Kumar is **confirmed on the judging panel for the companion sprint, Threat Intelligence, running 4–6 December 2026**. For Agent Attribution itself, **no judging role is claimed here** — this issue reports the sprint because its question is this newsletter's question, not because of a role in it. Nothing about outcomes, entries or results is stated, because the sprint has not run yet.

Why does an unrun sprint belong in this slot? Because attribution is where connector governance is heading, and leaders should hear the direction early. Today's approval records mostly answer *who connected this*. The question regulators, incident reviewers and insurers will ask after the first serious agent incident is the attribution question: *which actions in this log were the agent's, under whose authority, and can you prove it from the record alone?* Estates that cannot answer it will discover the gap the way this series keeps describing — after the fact, in a room they did not choose. A research sprint will not settle it. It is a sign of where the field's attention is going, and it is reported here as exactly that: a sign, upcoming, nothing more.

## 5. The Monday Fix — dry-run the first film

Forty-five minutes, this Monday — still no publishing, and the camera is optional. This fix rehearses Session 1 end to end, so the first real film is the second time the session has run:

1. **Run the session sheet against the workspace.** Open the Slack test workspace built for Session 1 (Issue #42's fix) and walk Teardown #31's four checks in order, at reading pace, without scoring: can each step actually be performed on this account, on this plan tier, in this console? Every step that cannot is a plan-versus-tenant gap — write it on the sheet, dated, next to the original step. Do not quietly fix the teardown page yet; the gap list is the artefact.
2. **Audit the dummy-data pack against its inventory.** Check every item the pack claims to contain: the public and private channels, the control item in the never-connected account, the planted instruction in each of its copies, word for word. If a real name, customer or project has crept into any dummy item, replace it now and note the replacement. A pack that has drifted from its inventory invalidates the comparison before it starts.
3. **Name the second coder — or write down that there isn't one.** Ask one person who did not design the teardown to score from the footage when the film runs (Section 3). If nobody is available, write that sentence into the teardown page now, before filming, where a reader will see it next to the scores — not in a footnote after they appear.
4. **Set the publication rule in writing, one line, in the session sheet:** *the scorecard records what the camera saw; where it disagrees with the documentation, the disagreement is published unedited.* Sign and date it. Rules agreed in a corridor bend under the first awkward result; rules filed with the session sheet hold.

Score the connector before you trust it — and before you film the test, dry-run the session, so the plan's first meeting with a real tenant happens off the record and every adaptation after it is on it.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

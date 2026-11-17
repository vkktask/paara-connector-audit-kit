# The Connector Audit — Issue #44

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #44 headline: The Dry Run — the first film has not happened yet, and the rehearsal for it is not a formality: a dry run is where the plan's gaps surface while surfacing them is still free. Plus the pre-flight checklist — accounts, data pack, session sheet, stop conditions, second coder, on one page — and a comment on product liability and the connector layer, submitted to the UK Law Commission.**

---

## 1. The Connector Pattern — the rehearsal tenant: a workspace that exists only to be practised in

This week's pattern is not a connector. It is the room the next several issues will be filmed in — and the room itself is the pattern to check in your own estate.

Ahead of Connector Spy Test #31 (Slack → Claude via MCP, drafted, scores blank until filmed), Session 1 of the filming plan runs in a purpose-built Slack test workspace: dummy channels, a private channel the connecting account was never given, a control item in a second account that is never connected at all, and a planted instruction sitting in the data, word for word as the session sheet records it. Nothing in that workspace is real except the grant. That is the design: the connector under test holds full-strength permissions, and everything those permissions can reach is invented.

Most estates have the opposite room. Changes to agent configuration are rehearsed — if they are rehearsed anywhere — in the production tenant, at low strength, with the tester quietly avoiding the actions that would prove anything, because the data is real and the blast radius is real. The result is a rehearsal that cannot fail, which is to say no rehearsal at all: the first full-strength run of the control is the incident, the migration, or the film. The pattern to check is simple. For every agent and connector you govern, is there a tenant whose only job is to be practised in — same plan tier, same settings surface, dummy data, a control item the account was never given? If the answer is no, every test you run this year will be run at demo strength, and its results will deserve exactly that much confidence.

That is a pattern, not a finding. No vendor score is published here, because none has been earned yet: Teardown #31 is a pre-filming draft, to be filmed on a test workspace with dummy data only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Dry Run

Issue #43's Monday fix was a dry run, and this issue's field note is what a dry run is actually for — because the word gets used for two very different activities, and only one of them is worth the hour.

The useless version is a walkthrough: the team reads the session sheet aloud, nods at each step, confirms the test workspace exists, and adjourns with the plan pronounced sound. Nothing was attempted, so nothing could fail, so nothing was learned. The useful version is a rehearsal in the stage sense: every step is physically performed, at reading pace, against the real test tenant — open the settings screen the check names, find the log the check plans to read, locate the control item, walk the revocation route — and every place the plan and the tenant disagree is written down, dated, on the sheet, next to the step that assumed otherwise.

Those disagreements are the product. A dry run of Session 1 can be expected to find them in predictable places, because they are the places paper cannot see: a check that assumes an admin console the test account's plan tier does not include; a log trail that exists but is split across two consoles, so the one-hour reconstruction standard from Issue #21 fails on navigation rather than on logging; a control item that turns out to be reachable for a boring, legitimate reason the checklist never named — a default channel membership, an inherited permission — which has to be closed or re-scoped before the film, because a control that fails for the wrong reason proves nothing about the grant; a stop condition that names a switch nobody in the room can actually reach. Each one found in rehearsal is a gap closed for free. Each one found on camera would have cost the session — or worse, been quietly worked around and absorbed into the footage, invisible to every reader of the scorecard afterwards.

Two disciplines keep a dry run honest. The first is that the gap list, not the fixed plan, is the artefact that leaves the room: the teardown page is not edited during the rehearsal, the adaptations are recorded against the original checklist, and the page is updated afterwards, in the open, exactly as Issue #43 prescribed for the film itself. The second is that a dry run produces no scores — not provisional ones, not "indicative" ones. The moment a rehearsal number exists, it will be quoted, and it was earned against a plan that was still bending. The scorecard stays blank until the film. That restraint is the same one this series applies to documentation, to the other side of a pair, and to vendor claims: an answer is published when the evidence for it exists, and a rehearsal is evidence about the plan — never about the connector.

Leaders already fund this discipline everywhere except software change. Fire drills rehearse the evacuation before the fire. Tabletop exercises rehearse the incident before the incident. Pilots rehearse the failure in a simulator because the first full-strength run cannot be the real one. The agent estate deserves the same courtesy, and it is cheaper there than anywhere: the tenant is already built, the data is already dummy, and the only cost is an hour in which the plan is allowed to be wrong in private — so that it does not have to be wrong in public.

## 3. Harness — The pre-flight checklist: one page, five blocks, nothing from memory

Issue #42 set the filming plan as a governance act and Issue #43 set the session discipline. This section assembles both into the artefact that runs before any session — and, with the names changed, before any agent go-live or connector change in a governed estate. One page. Five blocks. An item counts as done only when the named artefact exists, under Issue #25's rule: a confident claim with no captured artefact caps at the floor.

**Block 1 — Accounts.** ☐ Test workspace / tenant created for this session, on the plan tier the checks assume — tier verified on screen, not from the order email. ☐ Connecting account holds only the grant under test. ☐ Control account exists, is never connected, and holds the control item. ☐ A second dummy account holds the shared-in items. ☐ Revocation route for the connecting account identified: console, owner, expected minutes.

**Block 2 — Data pack.** ☐ Pack inventoried: every dummy channel, record and file listed, with its owner and purpose. ☐ Private item present that the connecting account was never given. ☐ Control item present in the never-connected account. ☐ Planted hidden instruction recorded word for word, with every copy's location. ☐ No real name, customer, project or credential anywhere in the pack — checked item by item, not assumed. ☐ Pack versioned; changes since the last session noted on the sheet.

**Block 3 — Session sheet.** ☐ Films listed in order, four checks per film, written before the session. ☐ Evidence named up front for every check: screenshot, log extract, config export. ☐ The pair rule stated: the legitimate action goes through AND the violating action is blocked — half a pair is not a control. ☐ Scoring method stated: the teardown's written checks are the rubric; the sheet is a protocol, not a story to be reconstructed afterwards.

**Block 4 — Stop conditions.** ☐ What ends a check early, written down: the agent reaches for anything outside the test workspace; a dummy item turns out to contain something real. ☐ What ends the session, written down. ☐ The kill route walked once in the dry run — identity, tokens, connector app — with the time recorded. ☐ The person who can call the stop is named and is in the room or on call.

**Block 5 — Second coder.** ☐ A second coder named — someone who did not design the teardown — scoring from the footage and the sheet, independently. ☐ Comparison step scheduled before anything is published; disagreements resolved against the written checks, and published with the scorecard where the checks cannot settle them (Issue #12). ☐ Or: the single-coder limitation written into the teardown page now, in plain sight, before the scores exist.

Five blocks, twenty-one items, one page. Print it. A pre-flight checklist that lives in someone's memory is not a checklist — it is a hope with good posture. Run it for a filming session and it protects the evidence; run the same five blocks before an agent goes live in production — accounts, data, session plan, stop conditions, independent eyes — and it protects the estate.

## 4. Regulator / Industry-Body Update — UK Law Commission, Product Liability (CP 279): a comment submitted

This week's update is a submission, reported at exactly that status — submitted, nothing more.

On 16 November 2026, Vivek Kumar submitted a comment on the **UK Law Commission's Product Liability consultation (Consultation Paper 279)**, through the Commission's online Citizen Space form. The submission is a matter of record: **Response ID ANON-5Z8J-4M5F-D**. The consultation's deadline is 14 January 2027.

Why a product-liability consultation belongs in a connector newsletter: the Commission's review asks how liability for defective products should work as products become software-driven, updated after sale, and composed of components from many hands. That is a precise description of the connector layer. An agent's harmful action is rarely one company's act: the model, the harness, the connector, the connected system and the organisation that granted the scopes each hold a piece of the causal chain — and, as Issue #21 and Issue #36 keep asking, the record that would apportion responsibility is exactly the log trail most connectors document worst. A liability regime written for that world will ask the attribution question — *which component acted, under whose configuration, and can you prove it from the record?* — of every party in the chain. Estates building their connector evidence now are building the answer to that question before it is asked of them in a worse room.

What is claimed here is only the submission. No outcome, adoption or influence is stated: the consultation is the Commission's, the response is one response among those it receives, and any reform is Parliament's to make and the Commission's to recommend. It is reported because leaders tracking where connector accountability is heading should know the question is being asked in liability law as well as in security guidance — and because this newsletter reports its author's submissions as submissions, never as results.

## 5. The Monday Fix — run the pre-flight checklist against one real session

Forty-five minutes, this Monday. Take Section 3's checklist off the page and run it against Session 1 — or, if no film is planned, against the next agent go-live or connector change on your own calendar:

1. **Score the five blocks honestly.** For each of the twenty-one items, mark *artefact in hand* or *gap*. No partial credit, no "basically done": Issue #25's rule applies — an item counts only when you hold the thing it names. Expect Block 1 and Block 4 to carry the gaps; they usually do.
2. **Give every gap a name and a date.** Each gap gets one owner — a person, not a team — and a closing date before the session or go-live it protects. A gap with no owner is a decision to run without the item, taken by nobody; write it as a risk acceptance or close it, but do not leave it as a shrug.
3. **Close the cheapest gap in the room.** There is almost always one that takes ten minutes: verify the plan tier on screen, write the session-ending stop condition, name the second coder or write the limitation into the page. Close it now, while the checklist is open — momentum is a control too.
4. **File the checklist with the session sheet.** Signed, dated, gaps and owners included. The next dry run starts from this artefact, not from memory — and the diff between the two checklists is the record of the plan getting stronger.

Score the connector before you trust it — and before the camera rolls or the agent ships, run the pre-flight, so the plan's gaps are found by a checklist on a Monday and not by an incident on a Friday.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

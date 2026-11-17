# The Connector Audit — Issue #25

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #25 headline: The Test Mode Illusion — the controls held in test mode, against dummy data, under test keys, and go-live quietly changed all three: live data behaves differently, live keys carry different reach, and the approval and logging you proved in the sandbox are not automatically the ones running in production. Plus evidence standards — what actually counts as evidence for a control — and a talk on connector auditing submitted to the FIRST Annual Conference 2027: submitted, not accepted.**

---

## 1. The Connector Pattern — the payments layer, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #15 tested Stripe → ChatGPT. Teardown #32 tests **Stripe → Claude**: the same payments account, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same list of who paid you, how much, and how.

- The read reach is the revenue record. Customers, payments, invoices, subscriptions, refund records — tested in Teardown #32 in **Stripe test mode with dummy data only**: the records named in the request, a record nobody pointed the assistant at, and a **control customer** held in a separate test-mode account, or behind a restricted scope, that was never connected. The filmed question is whether the reach is the use case, or the whole account made searchable.
- The write reach moves money. Refund a charge, create a charge or payment link, cancel or pause a subscription, edit a customer's details — each filmed in Teardown #32 with the approval step, or its absence, on camera. A refund is the sharpest write in this series: it is not a record edit, it is money going back out of the door, and whether a human confirms it before it lands is a filmed fact, not a documentation claim.
- The dataset context is unusually good for this store — and it is still only context. In the published 13-connector documentation audit, Stripe is the **one** connector of the 13 that documents prompt-injection guidance, and one of only two that document server-side audit logging (Slack and Stripe, F4 = N). Teardown #32 states that on its face, labelled as documentation context, and its scorecard is blank anyway: the live session, through this AI side, is what gets scored — and it gets scored in test mode, which is exactly the limit this issue's field note is about.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #32 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Test Mode Illusion

Issue #20 was about the demo org: a vendor's clean room, where the controls really do behave — on a system that does not exist in your organisation. This note is about the mirror image, and it is in some ways harder to catch, because this clean room is **yours**. The test mode illusion: your own test environment, your own sandbox, your own dummy data — and a set of results that are true there and quietly stop being true at go-live.

Test mode is not a smaller copy of production. In payment systems it is a deliberately different world, and the differences are the point: test keys instead of live keys, test card numbers that always behave, amounts that never trigger a real review, customers invented last Tuesday. Three substitutions happen at go-live, and each one can change what a control does.

**The data changes.** Dummy data is polite. It has no legacy metadata written by three previous integrations, no customer notes accumulated over six years of support calls, no free-text fields carrying instructions, complaints and other people's personal data in the same breath. A hijack test that passes against a tidy dummy note has tested the note you wrote for the test. Production notes were written by everyone, for years, for other purposes — and an AI connector reads them all as context. The control was proven against the clean version of the thing it will actually meet.

**The keys change.** Test-mode keys and restricted test scopes are how careful teams run evaluations — rightly. But the grant that goes live is often not the grant that was tested: a restricted key widened "temporarily" for launch, a live key with the reach the integration asked for rather than the reach the test proved sufficient, a different acting identity entirely. The approval step filmed in test mode belongs to the test configuration. If the live configuration differs in scope, identity or confirmation behaviour, the filmed result describes a system you are not running.

**The behaviour changes.** Systems treat live traffic differently by design. Real amounts trip thresholds dummy amounts never reach. Real customers have real subscription states, real failed payments, real refund histories — edge cases the dummy set never contained, each one a path the agent can walk that nobody rehearsed. And the log: a dashboard activity view confirmed in test mode proves that view records test-mode events; the production question — are live reads of customer and payment data recorded, under the acting identity, reconstructably — is a separate fact that has to be checked separately, in the live tenant, read-only, after go-live.

None of this makes test mode a mistake. Test mode is the only ethical place to run Teardown #32: no real customers, no real charges, no full card numbers, ever — that rule does not move. The illusion is not testing in test mode. The illusion is **filing the test-mode result as the production assurance** — letting "it passed" travel from the sandbox to the approval record without its address on it. Issue #24's rule applies with the volume up: every piece of connector evidence should carry which kind it is and where it was taken. A test-mode pass is evidence about test mode. It becomes production evidence only when the three substitutions — data, keys, behaviour — have each been checked and the differences written down.

Teardown #32 is built to that standard. It runs in test mode, says so in every take, and its filming checklist includes the step most teardowns skip: the live-configuration differences are named as an open item on the page, not smoothed over. The scorecard will be filled from the film. What the film proves will be stated at test-mode precision — and the approval that cites it will still owe the go-live checks in Section 5.

The lesson for leaders: when a control is presented as proven, ask **where it was proven** — which environment, which keys, which data. "In the sandbox" is a good answer to a different question. The production question is what changed on the way to live, and who checked each change. If nobody can list the differences, the proof did not survive the journey — only the confidence did.

## 3. Harness — Evidence standards: what counts as evidence for a control

This week's harness section is the rule the whole evaluation method stands on, from the AI Agent Harness Evaluation Playbook: **evidence or it didn't happen.** Every test names its artifact up front — a log excerpt, a trace, a blocked-action record, a screenshot. A confident claim with no captured artifact caps at the floor of the scale. Briefings and documentation never score; observation does. Here is what that means, artifact by artifact, when someone tells you a connector control works.

**A screenshot — of the right screen, dated.** The authorisation screen showing the scopes actually granted. The admin console showing the setting as configured, not as intended. The approval prompt as the user actually sees it. A screenshot earns its place when it shows the state, the identity and the date — and it is the weakest artifact on this list, because it proves a moment. It answers "was it configured this way, then?" It cannot answer "does it behave this way every time?"

**A log extract — the behaviour, recorded by the system.** The retrieval log showing which records were actually fetched against what was asked for. The audit entry showing the write, the acting identity and the timestamp. The blocked-action record showing a violating action stopped, not merely disallowed on paper. A log extract is the strongest ordinary evidence a control can produce, because it was written by the system while the behaviour happened, not by a person describing it afterwards. Its standard is completeness: an extract that shows the writes but not the reads is evidence about writes, and the gap is part of the finding.

**A config export — the grant, in machine-readable form.** The tool list the connector actually presents, exported, not screenshotted. The scope set, the key restrictions, the retention setting — as data that can be diffed against the approval and against last month's export. The export is what makes change visible: Issue #13's rug pull — a connector's tools or scopes changing under an existing approval — is only detectable if a dated export exists to diff against. A screenshot can be retaken; an export can be compared.

**What does not count.** A vendor's slide. A documentation page describing what the control is meant to do. A verbal assurance in a review meeting, however senior the voice. A passed questionnaire — in the playbook's method the evidence-mandatory questionnaire sets the hypothesis; live testing produces the score. And a result from the wrong environment: as this issue's field note argues, a test-mode artifact is evidence about test mode, labelled as such, or it is a claim wearing evidence's clothes.

**The pair rule.** A control counts only when it is proven both ways: the legitimate action goes through **and** the violating action is blocked. A connector that blocks everything has not demonstrated discrimination; a connector that allows everything has not demonstrated a control. Half the pair is an outage or a hole. So every evidence pack for a control should contain both artifacts — the allowed action's log entry and the blocked action's record — captured in the same session, under the same configuration.

Set the standard before the test, not after it: name the artifact each check must produce, the environment it must be produced in, and the pair it must complete. A folder of dated artifacts behind a signed scorecard is an answer that survives an auditor, a board member, or your own engineers asking "why do we believe this?" A confident claim with no artifact is a floor score — however confident it sounds.

## 4. Regulator / Industry-Body Update — FIRST Annual Conference 2027: a talk submitted, not accepted

This week's update is a submission, reported at exactly that status.

**On 16 November 2026, Vivek Kumar submitted a talk to the FIRST Annual Conference 2027 — Submission 4436 on EasyChair — titled "Score the Connector Before You Trust It: Auditing the AI Agent Layer as an Incident Response Problem."** It is a 45-minute, Technical Advanced talk, marked TLP:CLEAR, across three topics: Attack Surface Management, Incident Response Methodologies, and Securing AI Systems. The framing is this programme's method turned toward the incident-response community: the connector layer as attack surface, the audit as an IR discipline — inventory the grants, reconstruct from the logs, drill the revocation before you need it.

The status, stated at its actual precision: **submitted, and nothing more.** Notifications run from 15 February to 5 March 2027. No acceptance is claimed, implied, or expected in print before it exists — this newsletter has made the same distinction for marketplace listings, channel memberships and open pull requests, and a conference submission gets the same treatment. If it is accepted, that will be reported here when the notification arrives, as a new fact with a date on it.

One further fact is recorded now because it conditions any future acceptance: the FIRST Annual Conference is **in person, in Bangkok**. Vivek Kumar is based in the USA, and in-person attendance abroad requires an attorney/DSO travel check **before accepting** — the standing rule for every in-person event outside the USA in this programme. Submitting needed no clearance; accepting would. That check is noted against the notification window, not improvised after it.

Why submit to FIRST at all? Because the connector layer's failures will be handled, when they surface, by incident responders — the people FIRST convenes. A governance method that never reaches the IR room stays a paper exercise; the talk takes the teardown evidence standard — film it, log it, reconstruct it — to the audience whose first question after any incident is the one this series asks in Check 4: *can anyone prove what it did?*

## 5. The Monday Fix — list what changed between test mode and live

Forty-five minutes, this Monday — one connector, three substitutions, written down:

1. Pick **one connector your organisation tested in a sandbox, test mode, or pilot** and has since taken live — a payments connector is the sharpest case, but any connector with a test-to-live journey qualifies. Pull two documents: the test evidence (the scores, screenshots, or sign-off from the evaluation) and the approval record that cited it.
2. Write down the **data substitution**: what data did the test use, and what data classes does the live connector actually reach now? Name at least one class the dummy data never contained — legacy notes, real personal data, records written by other integrations. If the hijack and read checks were only ever run against tidy test data, mark those checks **due for a re-run** against production-shaped dummy data in a staging environment.
3. Write down the **keys substitution**: compare the scopes, key restrictions and acting identity from the test configuration against the live grant, side by side — a config export from each, diffed. Any widening, however small and however temporary it was meant to be, gets written into the approval record as a change that was never re-tested, with a named owner.
4. Write down the **behaviour substitution**: in the live tenant, read-only, check the one thing test mode cannot prove — pick one real (already completed) connector action and reconstruct it from the live logs alone: who asked, what was read, what was written, under whose identity, with timestamps. If the reconstruction fails, that is the finding, and the connector goes to the re-review queue with a date.

Score the connector before you trust it — and after go-live, check that the score was earned in the world the connector actually lives in. This Monday, the difference list is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

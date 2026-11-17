# The Connector Audit — Issue #26

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #26 headline: The Pipeline Confession — a CRM read whole tells the real pipeline story: the deals that are actually alive, the customers who are actually unhappy, and the notes reps write when they think nobody senior will ever read them. Plus vendor questions that work — the kit's questions to ask in writing before you approve — and a hands-on connector-audit workshop submitted to CyCon 2027: submitted, not accepted.**

---

## 1. The Connector Pattern — the CRM, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #12 tested HubSpot → ChatGPT. Teardown #33 tests **HubSpot → Claude**: the same CRM, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same system of record for your revenue.

- The read reach is the pipeline itself. Contacts with their notes and custom properties, companies, deals with amounts and stages, support tickets — tested in Teardown #33 on a **test portal with dummy data only**: the records named in the request, a record nobody pointed the assistant at, and a **control record** held in a separate test portal, or behind record-level permissions, that was never connected. The filmed question is whether the reach is the use case, or the whole portal made searchable.
- The write reach edits the system of record — and can speak in your name. Add a note, create a task, update a property such as a deal stage — each filmed in Teardown #33 with the approval step, or its absence, on camera. The sharpest write is the email: whether the connector **drafts** a customer email for a human to send, or **sends** it, is the difference between an assistant and a delegate, and it is a filmed fact, not a documentation claim.
- There is no dataset shortcut for this one. HubSpot → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on — and nothing carries over from Teardown #12 either, because the grant, the approval surface and the log story belong to this route, not to the CRM. Teardown #33's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #33 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Pipeline Confession

Issue #18 was about the calendar: connect an AI to it, and the pattern of who meets whom, when, and about what confesses the strategy. The CRM confesses something more concrete, and for most companies more sensitive: **the money.** Read whole, a CRM does not describe the pipeline your board pack describes. It tells the pipeline as it actually is — and the distance between those two pipelines is the confession.

Start with what the records contain, because CRM data is written the way calendar entries are written: in a hurry, for a small audience, in shorthand that assumes context. A rep's call notes are not written for the board. They are written for the rep — "champion left in March, replacement is sceptical," "budget is really half what they told procurement," "legal has seen the contract twice and gone quiet," "do not put the discount in writing." Deal stages carry the same honesty in compressed form: the opportunity that has sat at "proposal" for ninety days, the one whose close date has been moved four times, the enterprise deal whose amount was typed in during a confident week in Q1 and never revised down. Support tickets complete the picture from the other side: which customers are one more outage away from churning, in their own words, timestamped.

No single record confesses anything. A note is a note; a stage is a stage. The confession is in the whole — the same property this series found in the calendar. Which deals are real (the ones with recent activity, a named next step, and a customer who answers), which are theatre (the ones carried at full value on the strength of one good call), which accounts are quietly at risk (ticket volume rising while the deal record still says "healthy"), which rep's book is sound and whose is optimism with a CRM login. Assembled, that is not sales data. That is the company's forward revenue position, its customer-satisfaction truth, and several people's candid judgements about named customers — in one store, in plain language.

Then the assistant arrives, and the confession becomes queryable. Nobody connects an AI to a CRM so it can be asked "which of our top ten deals are actually dead," "what did the rep really write after the call with our largest customer," or "which accounts complained this month and haven't been called back" — yet those are exactly the questions a full read reach can answer, in seconds, in fluent summary, from data that was never written for that purpose. The rep wrote the note for themselves. The support agent wrote the ticket summary for the next agent. Nobody wrote any of it for a system that reads everything, forgets nothing it is shown, and answers whoever holds the grant. Add the write reach tested in Teardown #33 and the confession becomes editable: notes added, stages moved, properties changed — the system of record altered by the same session that read it, and, if the email test lands the wrong way, a message sent to a customer under a person's name.

Teardown #33 tests this pattern on HubSpot → Claude: read reach across contacts, companies, deals and tickets with a control record it was never given, write actions including the drafted-vs-sent email question, a hidden instruction planted in a dummy contact record, and the audit trail behind it all. It is not filmed yet, and this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates — usually twice, once per AI assistant, which is why this series tests the same CRM from both sides.

The lesson for leaders: treat the CRM as what it is — the most candid document your company keeps about its own future — and govern the AI grant to it accordingly. Someone senior should be able to answer, for your estate: which AI tools can read the CRM, whether that reach is the whole portal or the records the job needs, whether the tool can write — notes, tasks, stages — and whether it can send email or only draft it, and what log would prove what it did, under whose identity. If those answers do not exist, the confession is being read. You just do not know by what — or what it has already repeated.

## 3. Harness — Vendor questions that work: ask in writing, before you approve

This week's harness section is the cheapest control in the whole method, taken from the PAARA connector-audit kit's checklist and DPIA template and turned into the form a leader actually uses: **a short list of questions, sent to the vendor in writing, before the connector is approved — with the answers filed as part of the approval record.** The kit's discipline is that a fact is coded from evidence, never from prior knowledge; the vendor-question version is the same discipline pointed at a sales process. A verbal assurance in a demo is not evidence. A written answer, dated, from a named vendor contact, is the start of evidence — and a question the vendor will not answer in writing has also been answered.

Ask these, in writing, for every AI connector — and notice that each one maps to a check you would otherwise have to film to discover:

**On reach.** 1. List every data class this connector can read in our tenant — not the classes the use case needs, the classes the grant reaches. 2. Is the read reach limited to records a user opens in the session, or can the assistant search and retrieve across the whole connected store? 3. Can the grant be restricted — read-only, selected objects or record types, specific scopes — and if so, which restrictions are supported today, in configuration, not on the roadmap?

**On action.** 4. List every write action the connector can take, one by one. For each: does it execute directly, or does it produce a draft for a human to complete? 5. Where the connector can send — email, messages, external posts — is sending behind a human approval step that shows the exact content and recipient before anything leaves? Can that step be configured so it cannot be bypassed? 6. Under whose identity do writes appear in the connected system — the user's, a named service identity, or the vendor's application?

**On hostile content.** 7. What prompt-injection guidance or defence do you publish for this connector? (In the published 13-connector documentation audit, exactly one connector of the 13 documented any — the question is worth asking precisely because the documented answer is usually silence.) 8. Can content retrieved through the connector — a record, a note, a document written by someone else — trigger a tool call or a write without user confirmation? What stops it?

**On the record.** 9. What server-side log records this connector's activity — reads as well as writes — with the acting identity and timestamps? Where does an admin see it, and how long is it retained? 10. From that log alone, after an incident, could we reconstruct who asked, what was read, and what was written? If reads are not logged, say so in the answer, not in the incident review.

**On change and exit.** 11. How are customers notified when the connector's scopes, tool definitions or data classes change after approval — and does a material change require re-consent? 12. How is the grant revoked — per user, per group, per tenant — and what happens to data the connector already retrieved or created when it is?

Three rules make the questions work. **First, in writing or it didn't happen** — the answers go in the approval file next to the scorecard, with the date and the name of who answered; "covered in the demo" is not an answer. **Second, score the silences** — an unanswered question is recorded as *unknown*, and unknown is a finding, not a neutral: in the PAARA method, "not documented" has never meant "probably fine." **Third, the answers set the test plan** — every written claim a vendor makes here is a claim a filmed teardown can check, and the pair rule from Issue #25 applies: the legitimate action goes through *and* the violating action is blocked, on camera, before the claim is filed as proven.

None of this requires a tool, a budget, or a consultant. It requires sending twelve questions before the approval meeting instead of discovering the answers after the incident. Vendors with good answers answer quickly and precisely — the questions are, for them, a chance to differentiate. Vendors who stall, deflect to a roadmap, or insist the answers are in the demo have told you the thing you most needed to know, in writing, while it was still free to walk away.

## 4. Regulator / Industry-Body Update — CyCon 2027: a workshop submitted, not accepted

This week's update is a submission, reported at exactly that status.

**On 16 November 2026, Vivek Kumar submitted a workshop proposal to CyCon 2027 via the conference's official form: "Score the Connector Before You Approve It: A Hands-On PAARA Audit of AI Connectors."** The proposal is a **90-minute, hands-on workshop for up to 60 participants, bring-your-own-device**, submitted under the form's Legal track — the form allows one track only, and a note was added that the session spans Legal and Technology. The format is this programme's method run live by the participants: take a real AI connector, work the four checks — what it can read, what it can write, whether planted content can steer it, whether a log can prove what it did — and leave with a score and the one setting to change.

The status, stated at its actual precision: **submitted, and nothing more.** The form issued **no reference number** — the confirmation was the form's "Thank you for your application!" message — and applicants are contacted **after 31 January 2027**. No acceptance is claimed, implied, or expected in print before it exists. This newsletter has made the same distinction for conference talks, marketplace listings and open pull requests, and a workshop proposal gets the same treatment: if an answer arrives after 31 January 2027, it will be reported here as a new fact with a date on it.

Why CyCon? Because it convenes the legal and technical communities around cyber conflict and security policy in the same rooms — the two audiences a connector audit has to convince at once. The governance case for scoring a connector before approval is a legal argument about accountability and evidence; the audit itself is a technical act. A hands-on session puts both in the same ninety minutes: lawyers working the checks themselves, engineers arguing the verdicts. That is the room where "score the connector before you trust it" either survives contact with practitioners or gets improved by them — and either outcome is worth the submission.

## 5. The Monday Fix — send the vendor questions for one connector, in writing

Forty-five minutes, this Monday — one connector, twelve questions, on the record:

1. Pick **one AI connector your organisation is about to approve, renew, or expand** — a CRM connector is the sharpest case after this issue, but any connector still short of a signed approval qualifies. If everything is already approved, pick the one whose approval file is thinnest.
2. Send the vendor the **twelve questions from Section 3, in writing** — email is fine — addressed to a named contact, with a reply date before the approval decision, and a line saying the answers will be filed as part of the approval record. That sentence changes the answers you get: people write differently for the file.
3. File what comes back against the approval, question by question. Mark each answer **answered / partial / unanswered**. Every unanswered question is recorded as *unknown* in the approval record — with the consequence written next to it: if the logging question is unanswered, the approval states that reconstructability is unproven, and a filmed log check goes on the post-approval test plan with a date.
4. Take the vendor's strongest written claim — the one the approval most depends on — and schedule the live check that would prove it: the legitimate action goes through **and** the violating action is blocked, in one session, before the connector's next renewal or scope expansion. Put the date in the approval record, next to the claim it tests.

Score the connector before you trust it — and make the vendor score themselves first, in writing, while walking away is still free. This Monday, the sent email is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

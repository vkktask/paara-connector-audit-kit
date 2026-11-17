# The Connector Audit — Issue #29

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #29 headline: The Booking That Never Was — an agent that can book and cancel meetings acts on other people's calendars, not just yours: it books time a second person never agreed to, cancels meetings a second person was still planning around, and leaves no human who can say why. Plus consent and notice for the other party — the bystander rule applied to scheduling — and a workshop paper on what a DPIA must prove about AI connectors, submitted to PALS 2027 at ICISSP: submitted, not accepted.**

---

## 1. The Connector Pattern — the scheduling layer, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #14 tested Calendly → ChatGPT. Teardown #36 tests **Calendly → Claude**: the same scheduling layer, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same diary — and, uniquely in this store, on other people's diaries too.

- The read reach is a live list of who is meeting you. Event types with their upcoming, past and cancelled bookings, each booking carrying the invitee's name, email and the answers they typed into the booking form — tested in Teardown #36 on a **test account with dummy bookings only**: the bookings named in the request, a booking nobody pointed the assistant at, and a **control booking** held under a second user or team that was never connected. The filmed question is whether the reach is the one booking in the conversation, or the whole book made searchable — every visitor, every note they wrote when they booked.
- The write reach acts on two calendars at once. Create a booking, cancel one, reschedule one, change the account's availability — each filmed in Teardown #36 with the approval step, or its absence, on camera. Two of those writes reach past the account holder: a **cancellation** is a message to a real person that their meeting is gone, and a **reschedule** moves time in someone else's week. The availability change is quieter and wider still: it rewrites when the whole world can book, without touching any single booking at all.
- There is no dataset shortcut for this one. Calendly → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #14 either, because the grant, the approval surface and the log story belong to this route, not to the scheduling layer. Teardown #36's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #36 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Booking That Never Was

Every other write in this series lands on the account holder's own estate: their files, their tickets, their records. A scheduling write is different. A booking is a two-party object. It exists in your calendar and in someone else's — the invitee who set time aside, rearranged their day around it, and told their own team they would be in it. When an agent books, reschedules or cancels, it is not editing a record. It is making and unmaking commitments in another person's week, under your name.

Start with the phantom booking. An agent asked to "set up time with the vendor" creates the meeting — at a time the invitee never chose, sometimes with a title or description the invitee reads as a decision already made. No bad intent is required; the agent filled the slot the calendar offered. But the invitee experiences it as you deciding, unilaterally, when they will attend and what has already been settled. The booking exists. The agreement it implies never did.

The cancellation is sharper. A cancellation notice is one of the most socially loaded messages in business: it says the meeting does not matter enough to keep. Sent by a human, it usually arrives with a reason and an apology, because the human knows what it costs. Sent by an agent clearing a calendar — resolving a clash, tidying a week, acting on a stale instruction — it arrives bare: a system email, no reason, no human who can be asked why. The invitee learns their meeting is gone from a notification, and learns in the same moment that nobody they can call made the call. And the mirror case is worse: the meeting cancelled in the system that the invitee never hears about at all, because the notice went to a spam folder, an old address, or nowhere — and they arrive, prepared, at a room or a link where nobody is waiting.

Consent is the hole underneath both. The invitee consented to a booking process: they picked a slot, answered the questions, accepted the invite. They did not consent to an agent holding write access over that booking afterwards — able to move it, cancel it, or read the answers they typed into the form alongside every other booking in the book. The approval conversation, if there was one, happened with the account holder, about the account holder's convenience. The other party to every booking was never in it. Section 3 takes that up as a harness rule; this note stays with the human fact: scheduling is the one store where every record has a second owner, and the second owner is the one who finds out last.

Teardown #36 tests this pattern on Calendly → Claude: read reach across event types and bookings with invitee detail and a control booking it was never given, write actions — create, cancel, reschedule, change availability — with the approval step filmed, a hidden instruction planted in a dummy event description and a dummy invitee answer, and the log trail behind it all. It is not filmed yet, and this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates — usually twice, once per AI assistant, which is why this series tests the same scheduling layer from both sides.

The lesson for leaders: a scheduling connector is not a diary feature. It is delegated authority over other people's time, exercised under your name, in messages those people receive as yours. Someone senior should be able to answer, for your estate: which AI tools can create, move or cancel bookings, whether a human sees a cancellation before the invitee does, and what the invitee is told — and by whom — when an agent changes their meeting. If those answers do not exist, your calendar is making promises and breaking them, and the people it breaks them to cannot tell the difference between the agent and you.

## 3. Harness — Consent and notice for the other party: the bystander rule, applied to scheduling

Issue #19 set out the bystander rule for messaging: consent collected from the account holder covers the account holder, and the people inside the data — the group members, the customers, the former colleagues — never agreed to the connection. Scheduling is where that rule bites hardest, because the bystander here is not a passive name in a history. The invitee is an active party with a live commitment, and the agent's writes change that commitment. This section applies Issue #19's three tests to the calendar.

**Test 1 — Reach test: who else is inside this grant?** Before approval, enumerate the other parties by class, not by name: every invitee in the booking history, every future booker, every attendee on events the agent can create. A booking page is a rolling register of everyone who wants your time — prospects, candidates, customers, patients, students — and their self-written answers sit inside the same reach as the diary itself. If the approval record cannot say whose bookings and whose answers the connection reads, it was written for a smaller system than the one being connected.

**Test 2 — Notice test: how does the other party know an agent is acting?** There must be an answer that does not depend on the invitee asking. Practical forms, in increasing strength: a line on the booking page itself that AI assistance manages this calendar; a sentence in the confirmation and cancellation emails that an automated assistant may move or cancel the booking; a human-sent follow-up whenever an agent — not a person — makes or breaks a commitment. A cancellation with no reason and no human name fails this test on its face: the invitee cannot tell whether a person decided or a process fired. If the platform offers no way to mark agent-made changes, that absence goes in the approval record as a known gap, accepted by a named owner — not silently inherited by every invitee.

**Test 3 — Refusal and remedy test: what happens when the other party objects, or is harmed?** A booking moved without notice costs the invitee real things: travel booked, preparation done, a slot given up elsewhere. The harness needs a working answer decided before go-live: agent-made changes to other people's bookings require a human approval step, or they do not happen; an invitee who objects gets a human, not a thread with the agent; and a wrongly cancelled meeting has a named owner whose job is to restore it and apologise — in person, because the apology is part of the control. The remedy route is set by the owner in advance, not improvised by whoever notices the invitee's angry reply first.

**Where this sits in the gates.** This is the consent gate — G6 in the harness playbook, consent on regulated data — widened the way Issue #19 widened it: from the person connecting to every bystander in the store, and in scheduling, from read to write. The scoring discipline is the same: it is a gate, not a score. Fail one gate, no score can rescue it. An assistant that can cancel a hundred people's meetings on one person's say-so has not passed a weaker version of the consent test. It has not taken it — and neither, yet, have the invitees.

## 4. Regulator / Industry-Body Update — PALS 2027 at ICISSP: a workshop paper submitted, not accepted

This week's update is a submission, reported at exactly that status.

**On 16 November 2026, Vivek Kumar submitted a paper to the PALS 2027 workshop at ICISSP, via PRIMORIS — paper code ICISSP_2027_211: "What a DPIA Must Prove About AI Connectors: A Documentation-Evidence Method for Agentic Systems under the GDPR and the EU AI Act."** The paper takes the question this issue's harness section asks in scheduling form — what must be shown, in evidence, before a connection is allowed to act — and puts it in its legal form: a data protection impact assessment for an AI connector cannot rest on what the vendor's documentation says; it has to prove, from evidence, what the connector can reach, what it can write, what happens when the content it reads turns hostile, and what record survives afterwards. It is the connector-audit method written for the room where DPIAs are argued about.

The status, stated at its actual precision: **submitted, and nothing more.** Paper code ICISSP_2027_211 is an identifier on a submitted paper, not a result. Notification is scheduled for **21 December 2026**; no acceptance is claimed, implied, or expected in print before that date exists. This newsletter has made the same distinction for conference talks, symposium papers, short papers and marketplace listings, and a workshop paper gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because the DPIA is where connector governance stops being a newsletter argument and becomes a legal artefact — the document a regulator can ask for, a customer can audit against, and a court can read after an incident. A method that says "assess the connector, with evidence, not the system, from brochures" has to survive the practitioners who write those assessments for a living. That is the PALS room, and it is why the paper went there rather than to a general AI audience.

## 5. The Monday Fix — put a human in front of one connector's cancellations

Forty-five minutes, this Monday — one scheduling connector, one other-party rule, one named owner:

1. Pick **one AI connector with write access to scheduling** — the Calendly connector from this issue is the sharpest case, because its writes land in other people's weeks. If several qualify, pick the one whose bookings involve people outside your organisation.
2. Write its **other-party rule** into the approval record, in three lines: what the agent may do to a booking that involves another person (create / reschedule / cancel), what requires a human approval step first, and what the invitee is told — and by whom — when an agent-made change happens. If the honest current answer to the last line is "a system email, from nobody", write that down and date it; it is the finding this fix exists to close.
3. Turn on the **human step for cancellations** — or record why you cannot: cancellations and reschedules of bookings with external invitees go through a named human before the notice goes out, starting this week. Where the tool cannot enforce it, the rule goes in the team's working agreement, with the connector's owner named as the person who checks.
4. **Walk one change end to end, today**: on a test booking with a dummy invitee, have the agent reschedule it, and read what the invitee receives with the invitee's eyes — who it appears to come from, whether a reason travels with it, and whether a human is reachable in it. File the screenshots and the gaps in the approval record. The first agent-made change an invitee sees should be one you staged, not one you apologise for.

Score the connector before you trust it — and before it writes to someone else's calendar, make sure a person is standing in front of it. This Monday, the other-party rule is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

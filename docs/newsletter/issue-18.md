# The Connector Audit — Issue #18

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #18 headline: The Calendar Is a Confession — connect an AI to a calendar and it can read who meets whom, when, and about what, including the private events and the calendars other people only shared as a courtesy. Plus least-privilege scoping worked through on calendar scopes, and a rolling feedback route into the NIST AI RMF Playbook.**

---

## 1. The Connector Pattern — the calendar joins the estate

This week's pattern to check in your own estate:

The calendar is the store nobody assesses, because it arrives as a side effect. The AI assistant is approved for mail, or for documents, and the calendar comes with the same connection — the pattern tested in Teardown #25 (Google Calendar → ChatGPT), alongside the other two Google stores in this series: mail in Teardown #1 (Gmail → ChatGPT) and files in Teardown #5 (Google Drive → Claude). What the pattern actually grants, once an AI can read and write the calendar layer:

- The calendar is a record of intent, written in advance. Mail records what was said; files record what was produced; the calendar records what is *about to happen* — the negotiation before it is announced, the interview loop, the meeting with the lawyer, the board observer nobody listed. Titles and descriptions carry the subject; attendee lists carry the network; recurrence carries the rhythm.
- Shared calendars widen the reach silently. Calendars are shared as a courtesy — with assistants, with teams, with counterparties — at levels from free/busy to full detail. An AI connected to one person's account inherits every calendar that person can open, including other people's calendars shared with them, under whatever detail level those shares allow.
- "Private" is a display setting until it is tested. Events marked private are hidden from other calendar viewers. Whether a connected AI treats a private event's description differently from a public one is an empirical question — which is why Teardown #25 plants a dummy figure inside a private event's description and asks for it, and why the teardown also plants a control calendar the connecting user was never given, to test whether the reach stops where the sharing stops.

That is a pattern, not a finding about a named product. No vendor score is published here. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Calendar Is a Confession

Ask a leader what their calendar says about them and they will laugh — then stop. Because the calendar, read whole, is the strategy in outline. It shows which deal is real (the one with the recurring meetings), which executive is leaving (the one whose 1:1s quietly stopped), which problem is serious (the one that got a meeting with the lawyer in it), and which project is dying (the one whose reviews keep slipping). No single event confesses anything. The pattern confesses everything — and a calendar is nothing but pattern: who, whom, when, how often, about what.

People write calendars the way they speak in meetings, not the way they write email. Email is drafted knowing it persists and can be forwarded. Calendar entries are typed in a hurry, for an audience of the attendees, in shorthand that assumes context: a first name, a project codename, a figure in the description, the personal appointment — the doctor, the school, the interview — sitting in the same store as the board pre-read, often marked private in the belief that the marking is a wall. It is, at best, a curtain. It hides the event from colleagues browsing the calendar. It was never designed as a control against a connected application reading the account's data with the account holder's own grant.

Then the assistant arrives, and the confession becomes queryable. The questions a calendar answers are not the questions anyone approved it for. Nobody connects an AI to a calendar so it can be asked "who has met the regulator this quarter," "which customers has the departing rep seen in the last month," or "what is on the CEO's calendar the day before the announcement" — yet those are exactly the questions a full read reach can answer, in seconds, in plain language, from data that was never written for that purpose. Add write access and the confession becomes editable: events created, moved and deleted, attendees added — invitations issued under a person's name, booking their time and notifying others, by a system acting on a grant nobody scoped to that power.

Teardown #25 tests this pattern on Google Calendar → ChatGPT: read reach across shared calendars and private events, a control calendar it was never given, write actions including adding attendees, a hidden instruction planted in a dummy event description, and the audit trail behind it all. It is not filmed yet, and this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates.

The lesson for leaders: treat the calendar as a data store with a sensitivity of its own, not as plumbing that comes free with the mail approval. Someone senior should be able to answer, for your estate: which AI tools can read which calendars, whether shared and private events are inside that reach, whether the tool can write — create, move, delete, invite — and what log would prove what it did. If those answers do not exist, the confession is being read. You just do not know by what.

## 3. Harness — Least-privilege scoping, worked through on calendar scopes

From Training Module 2 of *Governing AI Connectors* (Scopes & Least Privilege): PAARA scores every connector twice — once with permissions as shipped (the default), and once after applying the restrictions the platform actually documents (the restricted score). The worked example in the training is Slack MCP: documented reach into private channels, direct messages and profile emails, and the ability to send messages — a broad default grant, where the restrictions an admin applies are what move the score at all. The lesson generalises: **the scope is the control.** Here is the same worked example run on calendar scopes instead of chat scopes.

**Step 1 — name the job before the grant.** The stated job for most calendar assistants is narrow: check availability, summarise the user's own upcoming meetings, draft scheduling suggestions. Write the job down in one sentence before touching the configuration. Every scope decision below is tested against that sentence, and anything the sentence does not need is not granted.

**Step 2 — read the default grant against the job.** A default calendar connection typically asks for the whole store: read all events on all calendars the account can open, and write — create, edit, delete. Set that against the Slack MCP pattern from the training: the documented reach (every channel the user belongs to, DMs, profile emails) was far wider than the use case (summarise my team's channels) — believed reach vs actual reach. The calendar version is identical in shape: believed reach is "my meetings"; actual reach is every calendar the account can open, every shared calendar at its shared detail level, every private event's full description, as far back and as far forward as the store holds.

**Step 3 — apply the restrictions that exist, in order.** The Module 2 discipline is to restrict in configuration, not in the prompt, and to re-score after each restriction: (a) **read-only** — remove write scopes entirely if the job is summarise-and-answer; a connector that cannot create or delete cannot be hijacked into doing so. (b) **Calendar selection** — limit the grant to the calendars the job names (the user's primary work calendar), and exclude shared calendars and personal calendars from the grant rather than trusting the assistant not to look. (c) **Free/busy where detail is not needed** — availability questions need times, not titles, descriptions or attendee lists; where the platform supports a free/busy-only level, that is the scope for scheduling use cases. (d) **Write behind approval** — if write is genuinely part of the job, it sits behind a human confirmation that names the calendar, the attendees and the exact event before anything lands or any invitation is sent.

**Step 4 — re-score, and record the delta.** The training's point is not that restrictions make a broad connector safe; it is that the delta between the default and restricted scores is the evidence the approval was real. If restricting the scopes does not change what the assistant can reach — because the platform offers one all-or-nothing grant — that is itself the finding, and it goes in the approval record: the choice is then connect-it-all or do-not-connect, made knowingly, by a named owner.

## 4. Regulator / Industry-Body Update — NIST AI RMF Playbook: a rolling feedback route that stays open

This week's update is an open route, reported at its exact status.

The industry-bodies scan published with this newsletter's work on 16 November 2026 ranked the **NIST AI Risk Management Framework (AI RMF) Playbook** seventh of eleven routes for a governance practitioner: the Playbook — NIST's companion guidance for putting the AI RMF into practice — accepts **rolling feedback, submitted by email**, with no fixed deadline and no conference, membership or submission portal involved. It is a **virtual** route, open on a continuing basis.

That is the complete, current status: **a feedback channel identified as open, on a rolling basis.** No submission is claimed here — nothing has been sent to the Playbook feedback route under this newsletter's work, and any feedback sent will be reported only when it exists, at the same precision as the other entries in this series.

Why flag a standing feedback mailbox in a newsletter about connectors? Because the Playbook is where the AI RMF becomes operational practice — the suggested actions, examples and references practitioners actually copy into their governance files. The connector layer this series tests is precisely where framework language meets configuration: scoping a grant, logging an agent's actions, naming an owner. Feedback from practitioners who have run those controls against real connectors is the kind of input a playbook can absorb at any time — and a rolling route rewards the reader who sends one concrete, evidenced observation over the reader who waits for a formal call that may never come.

## 5. The Monday Fix — scope one calendar grant

Thirty minutes, this Monday:

1. Pick the one AI assistant most widely connected to calendars in your estate, and pull up its actual grant — the scopes it holds, not the scopes the approval email described. If the grant cannot be displayed, that is the finding, and it goes to the top of the list.
2. Run the four restrictions from Section 3 against it, in writing: can write be removed or put behind approval? Can the grant be limited to named calendars, excluding shared and personal ones? Is a free/busy level available for the scheduling use cases? Each "no" is recorded as a platform fact, not argued with.
3. Apply what can be applied, and re-check what the assistant can still reach afterwards — including one private event and one shared calendar, tested, not assumed.
4. Record the delta and the residue: what the restricted grant still allows, the named owner who accepts it, and the date the grant is reviewed again. A scope nobody re-checks creeps — grants widen by update and by exception, and the calendar, of all stores, will not announce that it has started confessing to a wider audience.

You cannot govern a grant you have never read. Read one on Monday, restrict what the job does not need, and the calendar goes back to being a diary instead of a broadcast.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

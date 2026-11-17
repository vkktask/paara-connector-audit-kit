# The Connector Audit — Issue #17

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #17 headline: The Meeting That Became a Record — the AI meeting assistant joins, transcribes, summarises and files the meeting, and a conversation people treated as spoken and temporary becomes searchable, retrievable data that outlives everyone in the room. Plus the data classes an agent may never touch alone, and an open call in Dallas.**

---

## 1. The Connector Pattern — the meeting layer joins the estate

This week's pattern to check in your own estate:

A meeting used to be the least recorded thing an organisation did. People spoke, someone took rough notes, and the rest lived in memory. The AI meeting assistant changes the default in one move — it joins the call, transcribes everything, summarises it, and files the result where other systems can reach it:

- The transcript is a connector output. Once a meeting is transcribed and summarised by an AI assistant — the pattern tested in Teardown #4 (Zoom → ChatGPT) and, on the conversation side, in Teardown #24 (Microsoft Teams → Microsoft 365 Copilot) — the words leave the meeting platform and land in chat, files, and AI context, under whatever retention and access rules those places have, not the rules anyone set for the meeting.
- Speech becomes searchable text. A figure mentioned once, a name raised and dropped, a complaint aired and resolved — spoken, all of it becomes retrievable by anyone, or any agent, with reach into the store where the transcript sits. The audience for the meeting was the people in the room. The audience for the record is whoever can search it.
- The assistant attends meetings people forget it is in. Recurring meetings carry the assistant forward by default; guests, candidates and counterparties join calls where a transcription they never arranged is running, announced — if at all — by a line in a participant list.

That is a pattern, not a finding about a named product. No vendor score is published here. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Meeting That Became a Record

Every organisation runs two kinds of conversation. The written kind — email, documents, tickets — people handle carefully, because they know it persists. The spoken kind — the meeting, the call, the corridor version before the corridor became a video tile — people handle loosely, precisely because it does not. Candour lives in the spoken kind: the pre-decision doubts, the personnel problem named out loud, the number that is not ready to be a number yet, the complaint about a client that everyone in the room understands will never be written down.

The AI meeting assistant quietly moves the spoken kind into the written kind, without anyone re-deciding the candour rules. It joins — sometimes invited by one participant, sometimes riding a recurring series set up months ago — and it produces three artefacts the meeting never used to produce: a full transcript, a summary, and a set of extracted actions. Those artefacts are then filed, shared and indexed by exactly the connector machinery this newsletter exists to audit. The transcript lands in the meeting chat. The summary lands in a document store. An agent connected to either can read both, months later, in answer to a question nobody in the original meeting imagined being asked.

Teardown #4 in this series tests the pattern on Zoom → ChatGPT: what the assistant can read back out of meetings, and what leaves the platform. Teardown #24 tests the same layer from inside Microsoft Teams → Microsoft 365 Copilot, where the meeting transcript sits in the same store as the chats and channels — so a question asked about "what the team discussed" can be answered from words that were only ever spoken. Neither teardown is filmed yet, and this note claims no result from either. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already in most estates.

The record also changes the meeting's legal shape. A transcript is discoverable in a way a memory is not. It can be searched in eDiscovery, produced in a dispute, and read by people with no context for the tone in the room — the joke reads as a statement, the hypothesis reads as a decision, the figure floated to be argued down reads as the figure. And retention cuts both ways: a transcript kept forever is a liability that compounds; a transcript deleted on a short cycle may be exactly the record a regulator or an auditor later asks for. Neither default was chosen. Both were inherited from a tool setting.

The lesson for leaders: treat the meeting assistant as a recording decision, not a productivity feature. Someone senior should be able to answer, for your estate: which meetings get transcribed, who is told, where the transcript and summary land, who and what can search them, and how long they are kept. If those five answers do not exist, the meeting has already become a record — you just have not read your own record yet.

## 3. Harness — Data-class rules: what an agent may never touch alone

From the AI Agent Harness Evaluation Playbook: gates decide whether an agent goes live; data-class rules decide what it may touch once it is live. The rule is simple to state and routinely skipped in configuration: **an agent's permissions should be set per data class, not per tool** — because the same connector, with the same scopes, can reach a routine project update and a payroll file in one search, and only the data class tells you which of those needed a human.

**The four classes and the rule for each:**

1. **Never alone — human in the loop, every time.** Regulated and irreversible-harm data: personal data about identifiable people beyond the requester's own, health and financial records, credentials and secrets, legal and HR matters, and anything whose disclosure triggers a notification duty. An agent may *find* that such data exists; it may not read it into an answer, copy it, summarise it or act on it without a named human approving that specific access. If the platform cannot enforce the pause, the class is out of scope for the agent — not "use with care."
2. **Read alone, never write alone.** Business-sensitive working data: pipeline and pricing, internal financials, unreleased plans, other teams' project detail. The agent may retrieve and summarise for an entitled requester; any write — a change, a share, a send — needs the approval step, because a read stays in the room and a write leaves it.
3. **Act alone, inside the ladder.** Routine operational data the agent was deployed for: its own team's project status, public-facing content, its own prior outputs. This is the Observer / Contributor / Operator ladder from the Go-Live Runbook applied to data: the agent acts alone only at the rung it was approved for, on the classes it was approved for.
4. **No class, no access.** Data that has never been classified is not treated as class 3 by default. It is treated as class 1 until someone classifies it — because in every estate this newsletter has examined, the unclassified store is where the forgotten sensitive material lives: the export nobody deleted, the shared-in file nobody opened, the transcript nobody knew was kept.

Two enforcement notes, because a rule that lives only in a policy document is a hope. First, the classes must be wired to the connector configuration — scopes, store boundaries, approval steps — not written into the agent's prompt, where the next planted instruction (the hijack test in every teardown in this series) can argue with them. Second, the classes are a re-approval trigger: when a connector gains reach into a new store — a new channel type, a transcript store, a shared mailbox — the data-class review runs again before the reach does, not at the next quarterly review.

## 4. Regulator / Industry-Body Update — ISACA + IIA GRC 2027: an open call, closing 27 November

This week's update is an open call, reported at its exact status.

The industry-bodies scan published with this newsletter's work on 16 November 2026 ranked the **ISACA and Institute of Internal Auditors (IIA) GRC Conference 2027, in Dallas** third of eleven routes for a governance practitioner: an **in-person conference in the USA** whose **call for presentations closes 27 November 2026**.

That is the complete, current status: **a call identified as open, with a deadline of 27 November 2026.** No submission is claimed here — nothing has been submitted to GRC 2027 under this newsletter's work, and any submission will be reported only when a confirmation exists, at the same precision as the other entries in this series.

Why flag a conference call in a newsletter about connectors? Because GRC is the room where the audit side of this work gets decided. The connector questions this series tests — what can it read, what is logged, who owns the grant — become durable when auditors start asking them as standard fieldwork, and GRC is where governance, risk and audit practitioners set what standard fieldwork is. A CFP with a near deadline is also the honest kind of opportunity: it is open to anyone with a practitioner session worth hearing, it is in-person in the USA, and it closes on a date close enough that a reader with a session ready still has time to file it properly rather than in a rush.

## 5. The Monday Fix — answer the five meeting-record questions

Thirty minutes, this Monday:

1. List every AI meeting assistant and transcription feature switched on in your estate — the standalone assistants, and the ones built into your meeting platforms. Include the ones riding recurring meeting series set up months ago. If the list cannot be produced, that is the finding, and it goes to the top of the list.
2. For each one, answer in writing: **which meetings** get transcribed, **who is told** (and how — a participant-list line is a fact, not a practice), **where the transcript and summary land**, **who and what can search them** — including which agents and connectors have reach into that store — and **how long they are kept**.
3. Apply the data-class rules from Section 3 to the transcript store specifically: meeting transcripts are class 1 by default wherever personnel, client or regulated matters are discussed, which in practice means the store an agent may never read into an answer without a human approving that specific access.
4. Set the trigger going forward: no new meeting assistant, and no platform transcription feature, goes live until the five answers exist for it — named owner, dated. A meeting becomes a record by configuration. Make someone sign the configuration.

You cannot govern a record you do not know you are keeping. Answer the five questions, and the next meeting's candour rules are a decision again — yours, not the tool's default.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

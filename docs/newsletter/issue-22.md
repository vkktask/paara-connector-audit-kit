# The Connector Audit — Issue #22

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #22 headline: The Transcript Is Forever — a meeting ends in an hour, but its transcript outlives the meeting, the project, and sometimes the employment of everyone who spoke in it, kept on a retention setting nobody remembers choosing. Plus retention and deletion for agent data — what the agent read, what it created, where the copies live, and deletion that actually deletes — and a watchlist entry: IAPP's co-located 2027 conferences in Vancouver, whose call for proposals was not yet open at last check.**

---

## 1. The Connector Pattern — the meeting layer, read and run by the same grant

This week's pattern to check in your own estate:

Most connector reviews treat the meeting platform as a scheduling problem: can the AI book a room and send an invite? The pattern tested in Teardown #29 (Zoom → Claude) is the deeper half of the same grant — the record of everything that was said:

- The read reach is the spoken organisation, made searchable. A meeting connector that follows one user's grant can reach scheduled meetings, cloud recordings, transcripts and in-meeting chat — not just the call in the prompt. The filmed checks in Teardown #29 include the boundary that decides whether that reach is scoped or total: a control meeting, with its own recording and transcript, held in an account that was never connected at all.
- The write reach runs other people's time. Scheduling a meeting is the visible case; deleting one and changing a setting are the serious ones. A deleted meeting lands in every invitee's calendar, and a changed recording or transcription setting governs every meeting after it — made by the same grant that was approved for summarising calls.
- The meeting is also an input channel written live. Anyone who can speak or type into a call — attendees, guests, dial-ins — writes text the AI later reads as part of the record. A hidden instruction planted in a dummy meeting's chat, and a second copy spoken so it lands in the transcript, are filmed checks in Teardown #29 precisely because nobody reviews a transcript as a prompt.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #29 is not filmed yet — its scores are blank until the film. It pairs with Teardown #4 (Zoom → ChatGPT): the same meeting platform, the other AI side, tested fresh. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Transcript Is Forever

A meeting used to be the one record an organisation did not keep. People spoke, disagreed, floated numbers they would never put in an email, said the candid thing about the client, the candidate, the negotiation — and then the meeting ended, and the speaking evaporated. What survived was what someone chose to write down: minutes, a decision, an action list. The forgetting was not a bug. It was how candour survived inside companies.

Transcription ended the forgetting, and almost nobody re-decided the rules when it happened. Issue #17 of this newsletter covered the moment speech became a record — the meeting that became searchable text. This note is about what happens next: the record does not age the way the meeting did. A meeting lasts an hour. A project lasts a quarter. Employment lasts a few years. A transcript, kept on whatever retention setting the platform shipped with or an admin once clicked, can outlive all three — the meeting, the project, and sometimes the employment of everyone who spoke in it.

Three consequences follow, and none of them needs a breach to happen.

First, **the words outlive the context that made them safe.** The number floated in a call was a negotiating position, not a commitment. The remark about a candidate was a first impression, corrected by the interview that followed. Read two years later — by a new manager, a litigator, an auditor, or an AI summarising "everything we have on this topic" — the transcript speaks without its moment. It does not say "this was said before the facts arrived." It just says what was said, with names attached.

Second, **retention nobody set is still a decision — made by default.** Ask, in most organisations, who chose how long meeting transcripts are kept, and the honest answer is: nobody. The vendor's default chose. The admin who enabled transcription to fix note-taking chose, without knowing they were choosing. A retention period that no one picked, for a record no one re-reads, is governance by inertia — and it is discoverable, searchable and retrievable for exactly as long as it exists.

Third, **the leaver's words stay when the leaver goes.** When someone leaves, their account is disabled, their files transfer, their access ends — the offboarding runbook in Issue #16 covers the tokens. But the transcripts of every meeting they ever spoke in remain, under other people's meeting records, in the platform's retention, saying what they said, for as long as the default says. The organisation keeps the voice of people it no longer employs, in a record it may not even know it holds.

Teardown #29 tests Zoom → Claude in a test account with dummy meetings only, and the page says so on its face: read reach across meetings, recordings, transcripts and chat including a control meeting, write actions including scheduling and deleting meetings and changing settings with the approval step filmed, a hidden instruction planted in a dummy meeting's chat and spoken into its transcript, and the log trail through audit and usage records. It is not filmed yet; this note claims no result from it.

The lesson for leaders: a transcript is not meeting notes. It is a record with a lifespan, and the lifespan is a decision — yours, or the default's. Decide it the way you decide any retention: by data class, on purpose, in writing. The meeting ends. What you owe the people who spoke in it does not end until the record does.

## 3. Harness — Retention and Deletion for Agent Data: what it read, what it made, where the copies live

This week's harness section is the discipline that sits underneath both the field note and Issue #3's hidden copy: **retention and deletion for agent data.** A connector approval usually answers three questions — what may the agent reach, what may it do, who can stop it. It almost never answers the fourth: **for how long does what the agent touched continue to exist, and where?** Agent data comes in three kinds, and each needs its own retention answer.

**What the agent read.** Reads feel harmless because nothing changes. But a read by an agent is rarely just a read: the retrieved content is copied into the session, quoted in the output, sometimes indexed to make the next answer faster. Issue #3 named the pattern — "connected" quietly means "copied": a synced connector builds an indexed copy of your data inside the vendor's cloud, with its own retention clock, and disconnecting the connector does not delete the copy. So the retention question for reads is not "how long do we keep the source?" It is: **what copies did the read create — in the session, in the index, in the output — and what clock governs each one?**

**What the agent created.** Drafts, summaries, transcripts it generated, pages it edited, records it wrote. Created data inherits the retention of wherever it lands, not the retention you intended for the agent: a summary saved into the wiki lives on the wiki's clock; a transcript saved into the meeting platform lives on the platform's clock — the clock from the field note above, the one nobody set. The test is simple to state and rarely done: **for each place an agent's output can land, name the retention that applies there, and check it is the retention you would have chosen for that data class.**

**Deletion that actually deletes.** Deletion is a claim, and like every claim in this newsletter, it should be tested rather than believed. A deletion that actually deletes has four properties: it covers **the source and every copy** — the record, the index, the cached retrieval, the backups on their stated cycle; it is **confirmed in a record** — a log line or a vendor attestation you can file, not a spinner that stopped spinning; it **propagates on a stated clock** — you know the number of days, in writing, from the vendor's terms; and it is **someone's named job** — deletion on departure, on project close, on retention expiry happens because an owner runs it, not because everyone assumed the default would. Run the test on one artefact: pick one transcript or one agent-created summary, ask for its deletion, and then try to retrieve it — from the platform, from the AI that read it, from search. What you can still find is your real retention policy. The written one is just the intention.

This is the harness's long memory problem. The gates decide what an agent may do today; retention decides how long today lasts. Set it per data class, set it before go-live, and re-check it whenever a connector's terms change — the vendor update nobody read, from Issue #14, can move a retention clock as quietly as it moves a scope.

## 4. Regulator / Industry-Body Update — IAPP P.S.R. + AI Governance Global 2027, Vancouver: a watchlist entry, not yet open

This week's update is a watchlist entry, reported as exactly that — an opportunity identified in the industry-bodies scan of 16 November 2026, flagged for watching rather than action. Nothing has been submitted to it, and no submission window is claimed to exist.

The scan's eleventh item was **IAPP's co-located P.S.R. and AI Governance Global conferences for 2027, in Vancouver** — in-person, abroad. Two facts from the scan, carried at the same precision: as of 16 November 2026, the **call for proposals was not yet open**, and the item sat on the list as a **watchlist** entry — a venue to monitor for the CFP announcement, not a deadline to meet. The scan also recorded nothing open at that date across IAPP's other checked calls, so this is not a case of a missed window: there was, at last check, no window to miss.

Why carry a not-yet-open call in this section at all? Because the connector layer's audience gathers at exactly these two conferences — privacy, security and risk practitioners at P.S.R., and the AI-governance profession at AI Governance Global — and CFP windows at major conferences open and close on the organiser's schedule, not the author's. The discipline this newsletter preaches for connectors applies to venues too: an inventory you check beats a deadline you discover late. The practical move is the small one: note the watchlist entry, check the IAPP calls page on a cadence, and have the session abstract — the connector audit, the dataset, the filmed teardown format — drafted before the window opens, so the decision is about fit, not about time. And one standing rule from this programme applies if a proposal is ever accepted: in-person abroad means attorney/DSO travel clearance before accepting — not before submitting, and not assumed.

## 5. The Monday Fix — set one transcript retention, in writing

Thirty minutes, this Monday — one record class, decided on purpose:

1. Pick the meeting platform your teams use most. Find the retention setting for **meeting transcripts and cloud recordings** — the actual number of days, in the actual admin console or the vendor's terms. If you cannot find it in ten minutes, that is the finding: the retention was set by default, by nobody.
2. Write down what the default currently keeps, and for how long, next to the record classes it covers: transcripts, recordings, chat logs, AI summaries generated from them. One line each.
3. Decide the number you would defend — by data class, the way you would for email: how long does a transcript of a routine status call need to exist? A hiring panel? A client negotiation? Set the retention to the decided number, or file the exception with a named owner and a review date.
4. Close the loop with the agent question: name one AI tool connected to that platform and ask, in writing, what its reads and summaries inherit — where the copies live (Issue #3) and what clock deletes them. File the answer with the connector's approval.

The meeting ends in an hour. The transcript keeps whatever clock you give it — so give it one, on purpose, this Monday.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

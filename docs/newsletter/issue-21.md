# The Connector Audit — Issue #21

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #21 headline: The Wiki That Writes Itself — the AI connected to your internal wiki does not just read the record, it edits it, and quietly becomes the author of record: its words sit under a person's name, get quoted as policy, and get read by the next agent as fact. Plus reconstructability — can you rebuild what the agent did, from logs alone, in one hour — and an open call at IEEE ETHICS-2027 with a January deadline.**

---

## 1. The Connector Pattern — the wiki, read and written by the same grant

This week's pattern to check in your own estate:

Most connector reviews treat the knowledge store as a read problem: what can the AI see? The pattern tested in Teardown #28 (Notion → ChatGPT) is the other half of the same grant — the write side, on the store your organisation treats as its memory:

- The read reach is the whole memory, not the page you named. A wiki connector that follows one user's grant can reach team pages, project databases, meeting notes and sub-pages — and the filmed checks in Teardown #28 include the two boundaries that decide whether page permissions are a control or a decoration: a private page the connecting user was never given access to, and a control page in a workspace that was never connected at all.
- The write reach lands on the record itself. Creating a page is the visible case; editing an existing page is the serious one. The page colleagues treat as the current truth — the runbook, the policy summary, the decision log — can be changed by the same grant that was approved for summarising it, and the change appears under a person's name.
- The store is also an input channel. Wiki pages are written by everyone: colleagues, templates, imports, pasted documents. A hidden instruction planted in a dummy meeting-notes page is a filmed check in Teardown #28 precisely because nobody reviews wiki text as prompts — yet every page an agent reads is one.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #28 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Wiki That Writes Itself

Every organisation has a page that functions as the truth. Nobody voted on it. It is simply the page people link to, the page new joiners are sent to, the page quoted in the meeting when someone asks "what did we decide?" The internal wiki earns that role slowly, by being written by people, argued over by people, and corrected by people who remember what actually happened.

Now connect an AI to it — with write access, because write access is what makes the demos sing: draft the page, update the tracker, tidy the notes. Something quiet changes. The AI does not just read the record. It becomes one of the record's authors. And unlike every human author before it, it writes fluently, confidently, at volume, and under someone else's name — because a connector's edit appears in the page history as the connecting user's edit, with nothing marking it as machine-made unless the filmed test shows otherwise.

Three consequences follow, and none of them needs a breach to happen.

First, **provenance dissolves.** A human-written page carries its author's judgement; you can ask them what they meant. An AI-edited paragraph carries a plausible summary of whatever the agent could reach that day — including, possibly, a page it should never have read. Once it is saved, the next reader cannot tell which sentences came from a person who was there and which came from a model that was merely connected. The page still looks like the record. It has quietly become a blend.

Second, **the blend compounds.** The next agent that reads the wiki — next quarter's assistant, the search index, the onboarding bot — reads the AI's words as organisational fact and builds on them. An error a human would have caught in review becomes a premise. This is how a wiki that writes itself drifts: not in one dramatic falsification, but in a hundred fluent, unreviewed, perfectly formatted edits, each one citing the last.

Third, **accountability points at the wrong person.** When the page is wrong — when the runbook step is out of date, when the decision log misstates the decision — the name on the edit is a colleague's. They did not write it. They may never have seen it. The organisation will ask them anyway, because the record says they did it.

Teardown #28 tests Notion → ChatGPT in a test workspace with dummy data only, and the page says so on its face: read reach including a private page and a control workspace, write actions including creating and editing pages with the approval step filmed, a hidden instruction planted in a dummy page, and the log trail through page history and activity surfaces. It pairs with Teardown #3 (Notion → Claude) — the same wiki, the other AI side. It is not filmed yet; this note claims no result from it.

The lesson for leaders: read access to the wiki is a confidentiality question. Write access is an authorship question. Approve them as two different decisions, because they are. The record of your organisation should have authors you can name — and if one of them is a machine, the page should say so, every time, in the history, where the next reader will look.

## 3. Harness — Reconstructability: rebuild it from the logs, in one hour

This week's harness section comes from Training Module 4 of the open course (Governing AI Connectors): logging and reconstructability. The module's argument is that "logging" is not a checkbox. A vendor saying "we log activity" tells you almost nothing. The test that means something is a reconstruction: take one thing the agent did, and rebuild the full story of it — from the logs alone, against the clock.

**The six questions.** After an AI assistant acts — sends a message, edits a page, changes a record — someone will ask: **who** acted, **which agent identity**, **which tools** ran, **what data** was touched, **which decision** was made, and **can the record be tampered with**? If the logs cannot answer all six, you cannot reconstruct the output. You cannot do incident response, you cannot answer a regulator, and you cannot tell a data subject what happened to their data.

**The one-hour standard.** Set a timer. Pick one real output from your own stack — a drafted reply, a summary, a filed ticket, an edited wiki page. Working only from the logs and records the systems offer, try to answer the six questions completely, with timestamps, in one hour. Where the trail breaks is not a complaint — it is your requirements list, written in the vendor's own evidence. The module's worksheet turns each break into a line item a vendor can answer: acting identity logged, every tool call logged in order, data touched logged, approvals logged, retention stated, tamper-evidence stated.

**What the audit found — stated precisely.** In the PAARA documentation audit of 13 connectors, server-side audit logging is explicitly documented for **2 of 13**: Slack and Stripe — which is why F4 is coded N for them, the risk condition shown not to apply because logging is documented. The other 11 are **silent (U)** on logging. Silent is not the same as absent: no vendor in the corpus states that logging is absent, so F4 is never coded Y in this dataset. The honest sentence is: 11 of 13 do not document logging, so what their agents did cannot be reconstructed from the record. That is a finding about evidence — and exactly the kind a vendor can fix by documenting what they log.

**Where this sits in the gates.** Reconstructability is the harness's memory. The gates decide what an agent may do; the log is how you prove, afterwards, what it actually did — and reads are where the trail usually breaks first, because most audit surfaces were built to record changes, not reading. An agent whose reads leave no trace has a blast radius you can only guess at. Run the one-hour test before the incident, while the only thing at stake is an afternoon.

## 4. Regulator / Industry-Body Update — IEEE ETHICS-2027: an open call, in person, in the USA

This week's update is an open call for papers, reported as exactly that — an opportunity identified in the industry-bodies scan of 16 November 2026, not a submission. Nothing has been submitted to it under this newsletter's work, and no acceptance is claimed or implied.

**IEEE ETHICS-2027** is scheduled at **Duke University, in person, in the USA**, and its **call for papers closes 11 January 2027**. It sits in the scan's ranked list because the fit is direct: an ethics-of-engineering venue where the connector layer — the gap between what an AI system is approved to do and what its connectors let it reach — is a governance question, not a product claim. One hedge from the scan is carried here at the same precision: the registration fee was unverified in the scan, so check the current call before budgeting anything around it.

Why carry an open call in this section at all? Because the connector layer will be governed in rooms like this one — standards bodies, professional societies, ethics venues — or it will be governed by incident reports. A CFP deadline of 11 January 2027 is close enough that a paper decision is a December decision: the abstract either gets written over the break, on evidence already published — the 13-connector dataset, the method, the filmed-teardown format — or the date passes and the room fills without the connector question in it. This newsletter's position is the one it takes on its own estate advice: a deadline you can name is a control you can plan around.

## 5. The Monday Fix — run the one-hour reconstruction test

Sixty minutes, this Monday — the Module 4 exercise, done once, on one output:

1. Pick one thing an AI assistant actually did in your estate last week — a sent message, an edited page, a changed record. One output, real, small. Note the time it happened.
2. Set a timer for one hour. Working only from the logs and records your systems offer — no asking the vendor, no asking the user what they remember — try to answer the six questions: who acted, which agent identity, which tools ran in what order, what data was read and changed, which decision was made and who approved it, and whether the record could have been altered since.
3. Write down where the trail breaks, in the vendor's own terms: "reads not logged," "entries name the user, not the agent," "no record of the approval." Each break becomes one line on a log-requirements list, in the Module 4 worksheet format — item, documented Y/N/U, evidence, the question for the vendor.
4. Send the list to the vendor and file it with the connector's approval. A break the vendor answers in writing is a control improving. A break the vendor cannot answer is now a known, owned gap on the approval — not a surprise waiting for the incident.

You cannot govern what you cannot rebuild. One hour on Monday, and you know — precisely, in writing — whether your agent's story can be told from the record, or only from memory.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

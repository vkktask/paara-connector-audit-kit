# The Connector Audit — Issue #30

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #30 headline: The Invoice That Sent Itself — an agent that can send invoices acts on the company's money and the company's name at the same time: the wrong amount, to the wrong customer, sent before a human ever saw it, and discovered when the customer complains. Plus money actions need a second pair of eyes — approval design for financial writes — and a talk on auditing the AI agent layer as an incident response problem, submitted to FIRST CTI 2027: submitted, not accepted.**

---

## 1. The Connector Pattern — the books, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #16 tested QuickBooks → ChatGPT. Teardown #37 tests **QuickBooks → Claude**: the same books, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same company file.

- The read reach is the whole business in numbers. Customers, invoices open and paid, payments, expenses, the profit-and-loss story the file can tell when it is read whole — tested in Teardown #37 in a **QuickBooks sandbox company with dummy data only**: the records named in the request, records nobody pointed the assistant at, company-wide questions (biggest debtor, quarterly spend, the P&L), and a **control customer** held in a second sandbox company that was never connected. The filmed question is whether the reach is the one invoice in the conversation, or the entire financial position made searchable.
- The write reach moves money and speaks in the company's name. Create an invoice, **send** it, record a payment, edit an entry — each filmed in Teardown #37 with the approval step, or its absence, on camera. Two of those writes leave the building: a sent invoice is a demand for money carrying the company's name, letterhead and reputation, and a recorded payment rewrites what the books say a customer owes — the record every later conversation, dunning run and audit starts from.
- There is no dataset shortcut for this one. QuickBooks → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #16 either, because the grant, the approval surface and the log story belong to this route, not to the books. Teardown #37's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #37 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Invoice That Sent Itself

Every write in this series so far has landed on a record. An invoice send lands on a relationship — and on a bank balance. When an agent sends an invoice, it is doing two things at once that no other connector write does together: it commits the company's money position (this is what you owe us, by this date, on these terms) and it speaks in the company's name to a customer who will read it as the company speaking. There is no unsend. There is only the correction, the apology, and the customer's revised opinion of your competence.

Consider how ordinary the failure is. The agent is asked to "bill the Henderson account for last month's work." It finds a customer with a similar name — or the right customer and the wrong month's rate card, or a draft invoice that was deliberately never sent because the work was disputed. It creates the invoice from the data it can reach, which is all the data there is, and sends it, because sending was inside the grant and nothing in the workflow required a human to see it first. The amount is wrong, or the customer is wrong, or the timing is wrong in a way that breaks a promise a human made on a call. Nobody in the company knows. The first person to discover the error is the customer — the one party whose trust the invoice was supposed to build.

The mirror writes are quieter and, in the long run, worse. Recording a payment that never arrived makes the books say a debtor has paid: the dunning stops, the cash position flatters itself, and the truth surfaces at reconciliation, weeks later, with no clean story of how it got there. Editing an entry — a line-item amount, a date, a tax code — rewrites history in the one system where history is supposed to be the point. Accounting's whole discipline exists because financial records are legal artefacts: auditors, lenders and tax authorities read them as the company's sworn account of itself. An agent with write access is not using a productivity tool. It is keeping the books.

And underneath all of it sits the question this series asks of every connector: whose name is on the act? The sent invoice carries the company's name, not the agent's. The recorded payment sits in the audit log under whatever identity the connection used — often the human who connected it, who may never have seen the transaction. When the customer calls, angry, about an invoice nobody remembers approving, the company will go looking for a person. What it will find is a grant.

Teardown #37 tests this pattern on QuickBooks → Claude: financial read reach across the company file with a control customer in a company it was never given, write actions — create and send invoices, record payments, edit entries — with the approval step filmed, a hidden instruction planted in a dummy invoice note, and the audit log trail behind it all. It is filmed in a sandbox company with dummy data only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates — usually twice, once per AI assistant, which is why this series tests the same books from both sides.

The lesson for leaders: finance is where "the agent did it" stops being an explanation. Money actions are irreversible in the ways that matter — a sent invoice cannot be unsent, a recorded payment corrupts every report built on it, and the customer always finds out first. Someone senior should be able to answer, for your estate: which AI tools can create, send, record or edit anything financial, what a human sees before money moves, and whose name the audit log puts on an agent's entries. Section 3 turns that into a design rule.

## 3. Harness — Money actions need a second pair of eyes: approval design for financial writes

Most connector approvals are designed as a single gate at connection time: someone senior clicked approve once, and every write after that inherits the click. Issue #28 showed where that logic ends in the ticket queue — the agent certifying its own work, closing the loop on itself. In finance the same collapse is more expensive, because the loop the agent closes is the money loop: it creates the invoice, sends it, and records the payment, and at no point does a second mind enter the circuit. This section sets out the approval design that keeps a human inside it.

**Rule 1 — Separate making from sending, and both from recording.** The three financial writes are different acts and need different rungs on the action ladder. Creating a draft invoice is Contributor work: reversible, internal, safe to automate. **Sending** is the act that leaves the building — it should sit at the top rung, behind a named human's approval, every time, because it is the moment the company's name and a demand for money reach a customer. Recording a payment is different again: it certifies that money arrived, and a false certification poisons the ledger — it needs approval by someone who can see the bank side, not just the books side. One grant that covers all three is not an approval design; it is an absence of one.

**Rule 2 — Thresholds, written down in advance.** Approval design for money runs on numbers, not vibes. The approval record for a finance connector should state, in figures: the largest invoice the agent may draft without review, the largest it may send with one named approver, and the amount above which two approvers or a finance officer are required — with **no threshold at all** above which the agent acts alone on a send. Thresholds also run the other way: credit notes, refunds and write-offs are money leaving, and they belong in the same table, not in a gap nobody priced. If the record cannot state the numbers, the honest entry is "unlimited" — written down, dated, and owned by whoever signed it.

**Rule 3 — A named approver, and never self-approval.** An approval step that routes to "the team" routes to nobody. The approver is a named person (with a named deputy), who sees the actual artefact — the invoice as the customer will see it, the payment against the bank evidence — not a summary the agent wrote about it. And the rule Issue #28 established for tickets applies here with interest: the agent must never be able to approve, confirm or certify its own financial writes. The maker-checker split is the oldest control in accounting precisely because self-certification fails silently; an agent that drafts, sends and records is a maker-checker collapse with a chat interface. Where the tool cannot enforce the split, that goes in the approval record as a known gap with a named owner — the same discipline as any other control that exists on paper only.

**The evidence discipline.** Approvals are only as real as their records. Each approved send should leave the pair Issue #25's evidence standard requires: the artefact approved (the invoice itself, dated) and the approval (who, when, under which threshold). Sampled monthly: pick agent-touched invoices at random and re-perform the approval from the record. If the record cannot show who saw what before money moved, the control is a story the company tells itself — and the first audience for that story, as Section 2 said, will be a customer or an auditor, not this newsletter.

## 4. Regulator / Industry-Body Update — FIRST CTI 2027: a talk submitted, not accepted

This week's update is a submission, reported at exactly that status.

**On 16 November 2026, Vivek Kumar submitted a talk to FIRST CTI 2027 — Submission 6230.** The talk takes the incident responder's view of the connector layer: when an AI agent connected to your estate is the thing that read the data, sent the message or moved the money, the investigation that follows is only as good as the connector's logs, its identity story, and the approval record that was written before anything went wrong — which is to say, it is exactly the discipline this issue's harness section applies to finance, generalised to the incident timeline.

The status, stated at its actual precision: **submitted, and nothing more.** Submission 6230 is an identifier on a submitted talk, not a result. No acceptance is claimed, implied, or expected in print before a decision exists. This newsletter has made the same distinction for workshop papers, symposium papers, short papers and conference talks throughout this series, and a CTI talk gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because incident responders are the people who discover, at 3 a.m., what a connector's governance actually consisted of. A method that says "score the connector before you trust it" has to survive the practitioners who will inherit the connector after it fails — the ones who will ask who approved it, what it could reach, and why the log cannot say what it did. That is the FIRST CTI room, and it is why the talk went there.

## 5. The Monday Fix — put a second pair of eyes on one finance connector's sends

Forty-five minutes, this Monday — one finance connector, one approval table, one named approver:

1. Pick **one AI connector with write access to your books** — the QuickBooks connector from this issue is the sharpest case, because its writes move money and speak in the company's name. If several qualify, pick the one connected to the live company file, not the sandbox.
2. Write its **money-approval table** into the approval record, in figures: what the agent may draft alone, the largest amount it may send with one named approver, the amount above which two approvers or a finance officer are required, and the same three lines for the money-out direction — credit notes, refunds, write-offs. If the honest current entry for any line is "unlimited", write that down and date it; it is the finding this fix exists to close.
3. **Split the ladder**: sending and payment-recording come off the agent's unattended grant and go behind the named approver, starting this week — the approver sees the invoice as the customer will see it, and the payment against the bank evidence, not the agent's summary of either. Where the tool cannot enforce the split, the rule goes in the team's working agreement, with the connector's owner named as the person who checks.
4. **Re-perform one approval, today**: take the most recent agent-touched invoice in the live file and rebuild its story from the record alone — who saw it before it was sent, under which threshold, and what the audit log says acted. File the gaps in the approval record. The first invoice a customer questions should not be the first one whose approval nobody can reconstruct.

Score the connector before you trust it — and before it sends anything with your name on it, make sure a second pair of eyes has seen it first. This Monday, the money table is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

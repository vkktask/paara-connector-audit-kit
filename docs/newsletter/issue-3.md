# The Connector Audit — Issue #3

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #3 headline: The Hidden Copy — disconnecting is not deleting.**

---

## 1. The Connector Pattern — the Copilot that reads whatever the permissions allow

This week's pattern to check in your own estate, ahead of Connector Spy Test #10 (Microsoft 365 Copilot → SharePoint, drafted, scores blank until filmed):

An enterprise AI assistant grounded on your document estate is usually approved for one narrow job — "summarise this project site before the steering meeting." The reach behind it is rarely that narrow. The pattern to look for:

- The assistant answers from across the sites, libraries and files the signed-in user can open — not just the one site in the prompt.
- Old, broad sharing decisions become AI reach overnight: a site that was "temporarily" open to everyone in the company is now one question away from anyone's summary.
- Nobody wrote down which sites were in scope, so nobody can say afterwards whether a retrieval was in scope or out of it.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Microsoft 365 Copilot → SharePoint teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test tenant with dummy data fills it in. Check the pattern in your own tenant first — the fix is in Section 5.

## 2. Field Note — The Hidden Copy

From the field, anonymised:

"Connected" quietly means "copied." A synced connector builds an indexed copy of your data inside the vendor's cloud, so answers come back fast. That copy has its own retention clock — often around 30 days after you disconnect — and retention or zero-retention terms sometimes treat connector data differently from API data.

Disconnecting the connector does not delete the copy. The connector goes away; the index stays, on the vendor's clock, in the vendor's cloud, until the vendor's deletion timer runs out — assuming the terms you signed even start that timer.

The lesson is not "never sync." It is: you did not connect your data, you copied it — so govern the copy. A copy you have never inventoried, with a retention clock you have never read, is a second estate you did not know you were running.

## 3. Harness Gate — G3: exactly once

One gate from the AI Agent Harness Evaluation Playbook, in plain English:

**A consequential action executes exactly once — even when things go wrong.**

Payments, filings, deletions, sends: when an agent retries after a timeout, fans out to sub-agents, or recovers from a failure, the action must not happen twice — and must not silently happen zero times either. The agent verifies state before it retries. Prove it with a forced-retry test: interrupt the action mid-flight, let the agent recover, and count the outcomes. Two executions is a fail. A silent zero is a fail. Exactly one, verified, is the only pass. Fail this gate and no score elsewhere rescues the deployment — that is the whole point of a gate.

## 4. Regulator / Industry-Body Update — UK Law Commission, product liability in an agent world

On 16 November 2026, Vivek Kumar submitted a comment on the UK Law Commission's Product Liability consultation (CP 279) through its online form — Response ID ANON-5Z8J-4M5F-D, ahead of the 14 January 2027 deadline.

Why it belongs in a connector newsletter: product liability law was written for products that sit still. An AI agent acting through connectors does not sit still — it reads, decides and acts across other companies' systems, and when something causes harm, the first question is where in that chain responsibility sits. Consultations like this one are where that chain gets defined, and practitioner comments are how the connector layer gets into the record at all.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — inventory the copies, in writing

Thirty minutes, this Monday:

1. List every synced or indexed connector in your AI tools — the ones that copy data to answer faster, not just the ones that fetch live.
2. For each one, ask the vendor three questions in writing: what exactly is copied, where does the copy live, and what is the deletion timer after we disconnect?
3. Any connector whose vendor cannot state the retention terms in writing goes in the risk register as a permanent copy until proven otherwise.
4. Add "delete the vendor copy" as a named step in your offboarding checklist for every AI tool — disconnecting alone does not do it.

You didn't connect your data. You copied it. Govern the copy.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

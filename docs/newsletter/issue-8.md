# The Connector Audit — Issue #8

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #8 headline: The Monday Question — the five-minute inventory habit that makes every other control real. Plus the Go-Live Canvas: five questions to answer before any agent goes live.**

---

## 1. The Connector Pattern — the payments account that hands an AI your revenue, your customers and the refund button

This week's pattern to check in your own estate, ahead of Connector Spy Test #15 (Stripe → ChatGPT, drafted, scores blank until filmed):

A payments connector is usually approved for one narrow job — "answer questions about this month's revenue." The grant behind it reaches a very different asset. The pattern to look for:

- A payments account is a live list of people and money: every record carries a customer's name and email, what they paid, how they paid, and what they bought — and customer notes and metadata fields accumulate free text written by staff, systems and customers themselves.
- The same connection that reads payments can often write them: issue a refund, create a charge or a payment link, cancel or pause a subscription. A refund is not a database edit — it moves money back out of the business to a real person.
- Notes and metadata are free text. Anything an agent reads there, it may also obey — which makes a customer record an input channel, not just a record.

One piece of verified context, stated precisely: in the published PAARA 13-connector audit (documentation retrieved 9 Nov 2026), Stripe is the one connector of the 13 that documents prompt-injection guidance, and one of only two that document server-side audit logging. That is documentation context — the strongest paperwork in the set — and it is exactly why this integration earns a live test rather than a pass on paper.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Stripe → ChatGPT teardown is a pre-filming draft, to be filmed on a test account in test mode with dummy data only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Monday Question

From the field, anonymised:

Every control in this newsletter quietly assumes one thing: that somebody can name what is connected. In practice, that is the control that fails first. A connector approved in March is still live in November. A token issued for a pilot outlives the pilot. An agent nobody remembers granting is still holding scopes nobody would approve today — not because anyone decided that, but because nobody asked.

The habit that fixes it is embarrassingly small, and it has a name in this newsletter: **the Monday question.** Every Monday, one named person asks, out loud, in a room or a channel where the answer is recorded: *which AI connectors and tokens are live right now — and who owns each one?*

Five minutes. Three things make it work where annual reviews do not. It is weekly, so drift is measured in days, not audit cycles. It demands names, not departments — an unnamed connector is an unowned risk. And it is asked before anything else that week, so the inventory every other control depends on is never more than seven days old.

The lesson: governance does not fail at the policy. It fails at the list. If you can't name the owner, you don't have a control — you have a hope. Section 5 turns the Monday question into this week's fix.

## 3. Harness — the Go-Live Canvas: five questions before any agent acts

From the Go-Live Canvas & Resilience Runbook: before an agent goes live, answer five questions in writing. Not in a workshop, not in a slide — in the deployment record, with evidence attached.

1. **Whose identity does it act under?** A dedicated, verifiable agent identity — not a borrowed human login, not a generic service account. If you cannot name whose keys it holds, you cannot audit anything it does.
2. **What can it reach?** The actual scopes and connected data, listed — not the use case it was bought for. Believed reach is the demo. Actual reach is the grant.
3. **What may it do alone?** Place the agent on the action ladder — read, draft, write, execute, irreversible — and set the highest rung it may reach without a human. Three tiers frame the answer: **Observer** (reads and reports), **Contributor** (drafts and prepares, a human sends), **Operator** (acts, inside a ceiling set in configuration).
4. **Who approves the rest?** Every action above the solo rung names a human approver — a person, not a team alias — and the approval fires before execution, not in a log reviewed afterwards.
5. **Who can stop it — and have they practised?** A named owner who can revoke the identity, the tokens and the connector from outside the platform, in minutes — proven by a failure drill, not asserted in a document. The runbook's drills are simple: kill the agent mid-task, revoke a connector and watch what breaks, and replay a bad action from the log. If taking the keys back takes a meeting, you don't have a kill switch — you have a committee.

Five questions, one page, per agent. A deployment that cannot answer all five in writing is not ready to act — whatever its demo looked like.

## 4. Regulator / Industry-Body Update — Canada's OPC consults on third-party risk, and the connector question goes in

On 16 November 2026, Vivek Kumar sent a comment to Canada's Office of the Privacy Commissioner (OPC) on its third-party guidance consultation, from vkktaskusa@gmail.com to cpvp-opcconsultation1@priv.gc.ca (Gmail message id 1a1e6271fe3441bc). The consultation deadline is 4 December 2026.

Third-party guidance is where connector governance quietly lives or dies. The classic third-party question — "have you assessed your processor?" — was written for vendors a company contracts with, on a cycle, with a questionnaire. An AI connector does not behave like that vendor. It is granted in minutes, by an individual user, often outside procurement entirely; it holds standing scopes rather than processing instructions per task; and it can act — read, write, send — under a person's identity, at machine speed, between one annual assessment and the next.

The comment's argument, in one line: guidance on third parties has to reach the connections employees actually grant — the connectors, tokens and agent integrations that move personal information today — and not stop at the vendors on the procurement list. A third party you cannot name is a third party you have not assessed, which is the Monday question of Section 2 wearing a regulator's clothes.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — ask the Monday question, and write down the answers

Thirty minutes, this Monday:

1. Book the habit before you do the work: a recurring five-minute slot, same time every Monday, one named person asking the question — *which AI connectors and tokens are live right now, and who owns each one?*
2. This first time, spend the thirty minutes building the list the question will check: connected apps in your AI assistants, third-party access in your Google / Microsoft accounts, apps installed in Slack, and the AI subscriptions on expense reports. Most organisations find at least one connector nobody approved.
3. Give every line a named owner — a person, not a department. Any connector with no owner gets a date: justified and owned within two weeks, or disconnected.
4. Record the list where next Monday's question will be asked, and ask it again in seven days. The control is not the list. The control is the asking.

An inventory you can't name is not a control. Start the week by naming it.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

# The Connector Audit — Issue #2

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #2 headline: The Immortal Grant — the connector nobody ever revoked.**

---

## 1. The Connector Pattern — the CRM connector that can see the whole pipeline

This week's pattern to check in your own estate, ahead of Connector Spy Test #9 (Salesforce → ChatGPT, drafted, scores blank until filmed):

A CRM connector is usually approved for one narrow job — "summarise this account before my call." The grant behind it is rarely that narrow. The pattern to look for:

- The connected app can search across accounts, contacts, opportunities and cases — not just the one record in the prompt.
- The access runs under one user's permissions, so whatever that user can see, the agent can reach.
- Nobody wrote down which objects were in scope, so nobody can say afterwards whether a retrieval was in scope or out of it.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Salesforce → ChatGPT teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test org with dummy data fills it in. Check the pattern in your own tenant first — the fix is in Section 5.

## 2. Field Note — The Immortal Grant

From the field, anonymised:

An OAuth grant is approved in a hurry, for a pilot, by someone who then changes role. The pilot ends. The project closes. The grant does not. It sits there — valid token, original scopes, original reach — because revoking it was never anyone's job, and no expiry was ever set.

Months later the connector is still connected. It still holds the scopes it was given on day one. If it is queried, it will still answer with the access it was granted, because nothing in the grant knows the pilot is over.

The lesson is not "don't grant access." It is: a grant without an owner and an expiry date is not a pilot control. It is a permanent one that nobody chose.

## 3. Harness Gate — the external kill switch

One gate from the AI Agent Harness Evaluation Playbook, in plain English:

**Can you stop the agent from outside the agent?**

Before go-live, prove — by doing it, timed — that someone can disable the agent's identity, revoke the connector's tokens, and disable the connector app, without asking the agent's permission and without the agent being able to restart itself. If stopping it takes a meeting, you do not have a kill switch; you have a committee. Fail this gate and no score elsewhere rescues the deployment — that is the whole point of a gate.

## 4. Regulator / Industry-Body Update — the EU FRIA template, and the connector gap

On 16 November 2026, Vivek Kumar submitted a comment on the EU AI Act's Fundamental Rights Impact Assessment (FRIA) template (Contribution ID 57ab2929-b348-472e-b068-709f588b89e0).

The point made in that submission, and the one worth repeating here: an impact assessment that assesses the AI system but never its connectors misses where the data actually moves. The template's gap is the connector layer — what each connector can reach, what scopes it holds, and what is logged when an agent acts through it. A FRIA for an agentic system should have to name those things, connector by connector, or it has assessed the model and skipped the plumbing.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — give every grant an owner and an expiry

Thirty minutes, this Monday:

1. Pull the list of connected apps and OAuth grants in your main AI tools and CRM.
2. For each grant, write down two things: a named owner, and a review date no more than 90 days out.
3. Any grant with no owner, or tied to a pilot that has ended, gets revoked on the spot — it can be re-granted in minutes if it turns out to be needed.
4. Put the review dates in the calendar now, not in a document nobody opens.

A grant that cannot name its owner is the Immortal Grant. Kill it before it outlives another reorganisation.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

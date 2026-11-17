# The Connector Audit — Issue #5

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #5 headline: Two Doors, One Vault — each platform passed its review. Nobody reviewed the pair.**

---

## 1. The Connector Pattern — the same CRM, connected twice, reviewed never as a pair

This week's pattern to check in your own estate, ahead of Connector Spy Test #12 (HubSpot → ChatGPT, drafted, scores blank until filmed):

A CRM is usually approved for one narrow job on one platform — "summarise this account before my call." Then a second team connects the same CRM to a second AI platform, for a second reasonable job. The pattern to look for:

- Each connection was reviewed on its own, against its own use case — and each review was, on its own terms, correct.
- The connected app on each platform can search across contacts, companies, deals and tickets — not just the one record in the prompt.
- Nobody ever reviewed the combined reach: what the two doors, opened together, let an agent see when data from the same source is joined in one context.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the HubSpot → ChatGPT teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test portal with dummy data fills it in. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — Two Doors, One Vault

From the field, anonymised:

The same data source gets connected to two AI platforms because two teams asked separately. Each connection passed review on its own. Nobody reviewed the combined reach — and data joined across sources in one context can become more sensitive than either source alone. Restricted plus Restricted can become Sensitive.

Neither team did anything wrong. Each asked for a door to the vault, each door was assessed, each door was approved. The failure sits between the reviews: the registry — if there is one — is kept per platform, so the second door never shows up as a second door. It shows up as a first door, somewhere else.

The lesson is not "allow only one platform." It is: a data source does not care which platform reaches it. Review the source's total exposure, not each platform's slice of it — or the pair will keep passing reviews the vault never got.

## 3. Harness Gate — G5: external kill switch

One gate from the AI Agent Harness Evaluation Playbook, in plain English:

**You can stop the agent from outside the platform — and prove that it stopped.**

Revoke the agent's identity, its connector tokens, and the connector app itself, in minutes, without asking the agent's permission and without the agent being able to restart itself. Then prove the negative: run the stopwatch drill, and afterwards show the dead sessions — no live token, no active connection, no action completing after the stop. A kill switch you have only read about in a vendor document is not a kill switch. Fail this gate and no score elsewhere rescues the deployment — that is the whole point of a gate.

## 4. Regulator / Industry-Body Update — IETF Acts-For draft, review comment sent

On 16 November 2026, Vivek Kumar sent a review comment on the IETF draft draft-morrison-acts-for-01 to the IETF's agentproto mailing list (agentproto@ietf.org) — subject: "Review comments on draft-morrison-acts-for-01 — revocation, audit logging, and per-action scope" (Gmail message id 1a1e7c79ce6cb487).

The comment pressed on three points where delegation drafts tend to go quiet, and where connector governance lives in practice: how a delegation gets revoked when the person or the job ends; what audit logging must exist so an agent's actions can be reconstructed afterwards; and whether scope is set per action, rather than granted once, broadly, at connection time. Those are the same three questions the PAARA checks ask of a live connector — which is why a standards draft is worth a practitioner's hour: what the draft requires is what vendors will eventually have to document.

No endorsement or adoption is claimed — a review comment sent to a public list is a review comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — one registry, keyed by data source

Thirty minutes, this Monday:

1. Start one registry of every AI connector in the estate — a single page is enough — and key it by data source, not by platform: CRM, mailbox, file store, code repos, each listed once, with every platform that can reach it named underneath.
2. Flag every source with two or more doors. For each flag, write down the combined reach: what an agent could see if both connections were used together, and whether joined data raises the sensitivity of either source alone.
3. Give each data source one named owner — one person who sees every door to that vault, whichever team asked for it.
4. Set one rule from today: a second connection to a source already in the registry triggers a combined-reach review before it goes live. First doors get a review; second doors get a bigger one.

Each platform passed its review. Give the vault a review of its own.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

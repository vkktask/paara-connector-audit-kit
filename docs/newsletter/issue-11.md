# The Connector Audit — Issue #11

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #11 headline: The Approval That Never Happens — an approval step that is always clicked "yes" is not a control, it is a delay. Plus the action ladder: what an agent may do alone, rung by rung, and Canada's OPC Children's Privacy Code consultation.**

---

## 1. The Connector Pattern — the design library that hands an AI your unreleased assets, and the publish button that decides when they stop being unreleased

This week's pattern to check in your own estate, ahead of Connector Spy Test #18 (Canva → ChatGPT, drafted, scores blank until filmed):

A design-tool connector is usually approved for one narrow job — "let the assistant draft and tidy designs." The grant behind it reaches a very different asset. The pattern to look for:

- A design library is where an organisation keeps what has not been announced yet: unreleased campaigns, pricing decks, product screenshots, the new brand kit. Approving the connector approves reach into all of it, not just the design somebody asked about — and team folders other people shared in come along with your own.
- The same connection that reads designs can often write: create, edit, export. And one write matters more than the rest — publishing or sharing. Moving an unreleased asset outside the design tool is not a formatting step. It is a disclosure decision, made by software, under a person's identity.
- Designs are an input channel, not just pictures. Text elements, comments and briefs inside designs are written by staff, agencies and freelancers — anything an agent reads in them, it may also obey.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Canva → ChatGPT teardown is a pre-filming draft, to be filmed on a test account with dummy designs only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Approval That Never Happens

From the Go-Live Canvas & Resilience Runbook — the approval step that exists in the design document and nowhere else:

On paper, the workflow is reassuring. The agent drafts. A human approves. The action lands. The approval step is in the architecture diagram, in the DPIA, in the vendor's slide deck. Everyone who reviewed the design saw it, and everyone felt better because of it.

In production, watch what the approval actually looks like. The request arrives mid-task, in a queue, formatted identically to the last forty. The approver has no context the agent did not supply — the summary they are approving from was written by the thing asking for approval. The button is one click, the rejection path is three screens and a justification field, and the queue is measured on clearance time. Within a month the approval is a reflex: click, click, click. Within a quarter it is effectively auto-approved — the only difference from no approval step at all is a log line saying a human was present.

That log line is the dangerous part. After an incident, the approval record will be produced as evidence of human oversight — and it will be technically true and substantively false. The human was there. The judgment was not. A control that has never once said "no" is not evidence of a well-behaved agent; it is evidence the control cannot say no — because the approver lacks the time, the context, or the mandate to refuse.

The runbook's test is simple: an approval step is real only if three things are true. The approver sees something the agent did not write — the underlying record, not the agent's summary of it. Refusal is as cheap as approval — one click, no penalty, no queue metric punishing it. And refusals actually happen, and are recorded, and nobody treats a refusal as a process failure. If any of the three is missing, write the workflow down honestly as unapproved automation with a witness — and then decide, at that honesty level, whether the action belongs on the agent's ladder at all.

## 3. Harness — the action ladder (Go-Live Canvas)

From the Go-Live Canvas & Resilience Runbook: before go-live, every action an agent can take is placed on one rung of the ladder, in writing. The rung decides what the agent may do alone, what needs a human, and what it may never do. Promotion up the ladder is earned by evidence from the rung below — never granted by enthusiasm at launch.

**Rung 1 — Observer.** The agent may look, and report what it saw. Nothing else.

- [ ] Read and retrieve within its granted scopes
- [ ] Summarise, draft and prepare — drafts stay drafts, visible to a human
- [ ] No writes, no sends, no changes to any system of record
- [ ] Every read logged, so observation itself is auditable

**Rung 2 — Contributor.** The agent may prepare work inside the system, but a human completes it.

- [ ] Create drafts, tickets, documents and designs that a named human reviews and submits
- [ ] Propose changes — values, text, recipients — shown to the approver from the underlying record, not the agent's summary
- [ ] Approval and refusal are equally cheap: one click each, refusals recorded without penalty
- [ ] Nothing the agent prepares leaves the organisation on its own

**Rung 3 — Operator.** The agent may act alone, inside a written ceiling.

- [ ] Act without per-action approval only on the actions named for this rung, in writing
- [ ] Ceiling set in configuration, not in the prompt: value limits, named systems, named action types
- [ ] Irreversible actions stay human-only by default — the rollback drill (Issue #10) defines what counts as irreversible
- [ ] Every action logged with the agent's identity, and the kill switch (Issue #10) drilled for this rung before it is granted

The ladder's discipline is the demotion rule: an agent that misbehaves, or whose connector's permissions change underneath it, drops a rung first and argues about it second. And an action that cannot be placed on a rung has not been approved — it has been overlooked.

## 4. Regulator / Industry-Body Update — Canada's OPC and the Children's Privacy Code

On 16 November 2026, Vivek Kumar sent a comment to Canada's Office of the Privacy Commissioner (OPC) on its Children's Privacy Code consultation, by email to the OPC's consultation address, **cpvp-opcconsultation1@priv.gc.ca** (Gmail message id **1a1e67496b9b35ed**).

Why a children's privacy code belongs in a connector newsletter: children do not connect AI tools to school and family accounts — adults do it on their behalf, and platforms do it by default. A children's privacy regime has to answer the same question this series asks of every connector, sharpened: when an AI assistant is connected to an account holding a child's data, what can it reach, what may it do with what it reaches, and who approved that grant — a parent making an informed choice, or a terms-of-service click nobody read? Consent that is rubber-stamped is this issue's field note wearing a regulator's clothes: an approval that never happens, recorded as though it did.

The comment is on the record as sent, with its message id, so it can be checked and held to account — the same standard this newsletter applies to its own claims, including the blank scores in every teardown until the film exists.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — audit one approval step until it says no, or admit it can't

Thirty minutes, this Monday:

1. Pick one AI workflow in your estate that has a human approval step — the one everyone cites when asked about oversight.
2. Pull its last month of approval records. Count three numbers: how many requests, how many approvals, how many refusals. If refusals are zero, you do not yet know whether the step works — you only know it has never been exercised.
3. Check the three conditions: does the approver see the underlying record, or only the agent's summary? Is refusal exactly as cheap as approval — same clicks, no justification form, no queue penalty? Is there a named person whose job includes saying no?
4. Write the result where the go-live decision lives: the counts, the missing conditions, and an owner and date for each gap. If a condition cannot be fixed, reclassify the workflow honestly on the action ladder — unapproved automation with a witness sits on the Operator rung's terms, not the Contributor rung's comfort.

An approval that never happens is not oversight. Count the refusals, and find out whether yours is a control or a ceremony.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

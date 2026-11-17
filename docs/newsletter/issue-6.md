# The Connector Audit — Issue #6

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #6 headline: Paper vs Production — the review approved the datasheet. Nobody tested the tenant.**

---

## 1. The Connector Pattern — the project tool that can read the roadmap, and rewrite it

This week's pattern to check in your own estate, ahead of Connector Spy Test #13 (Asana → ChatGPT, drafted, scores blank until filmed):

A project-management connector is usually approved for one narrow job — "summarise this project before my standup." The grant behind it is rarely that narrow. The pattern to look for:

- The connected app can search across projects and tasks in the workspace — not just the one project in the prompt — and project tools hold roadmaps, deadlines and candid internal discussion in the comments.
- Private projects exist in the same workspace as public ones, and whether the connector's reach respects that boundary is a production question, not a datasheet question.
- The same connection that reads can often write: create a task, mark one complete, comment, reassign. A summary tool that can quietly re-plan the work is a different risk from a summary tool that cannot.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Asana → ChatGPT teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test workspace with dummy data fills it in. Check the pattern in your own workspace first — the fix is in Section 5.

## 2. Field Note — Paper vs Production

From the field, anonymised:

Every connector arrives with two versions of itself. The paper version lives in the vendor documentation, the security whitepaper and the approval form: the scopes listed, the logging described, the controls named. The production version lives in your tenant: the scopes actually granted on the day, the settings a pilot changed and never changed back, the log that turns out to be on a different plan tier.

Reviews assess the paper version, because the paper version is what fits in a meeting. Incidents happen in the production version. The gap between them is rarely a lie — it is drift: a scope widened for a demo, an admin setting inherited from a template, a documentation page describing the current release while the tenant runs the connector approved two versions ago.

The lesson is not "don't trust documentation." It is: documentation is a claim, and a claim about your own tenant can be tested in an afternoon. Approve the paper if you must — but govern the production version, because that is the one connected to your data.

## 3. Harness Gate — G6: consent on regulated data

One gate from the AI Agent Harness Evaluation Playbook, in plain English:

**The agent does not touch regulated data without a recorded consent basis for that data, that purpose, and that action.**

Before go-live, prove — with the actual data classes the agent will reach — that personal, health, financial or otherwise regulated data is only processed where a consent or lawful-basis record exists, that the record names the connector doing the processing, and that withdrawing consent actually stops the agent, not just the form it arrived on. An agent that reads first and checks the basis later has the order backwards, and "the user connected it" is not a consent record. Fail this gate and no score elsewhere rescues the deployment — that is the whole point of a gate.

## 4. Regulator / Industry-Body Update — the FRIA template gap, checked page by page

Issue #2 reported the submission: on 16 November 2026, Vivek Kumar submitted a comment on the EU AI Act's Fundamental Rights Impact Assessment (FRIA) template (Contribution ID 57ab2929-b348-472e-b068-709f588b89e0), arguing that an impact assessment which assesses the AI system but never its connectors misses where the data actually moves.

This issue adds the follow-up check behind that argument. The official draft template was read in full — all 13 pages — looking for the connector layer: a question about what each connector can reach, what scopes it holds, how an agent's actions through it are logged, or who owns it. There is no connector question anywhere in the draft. Not a weak one, not a partial one — none. The template asks about the system, its deployer and its affected groups, and stops at the boundary where, in an agentic deployment, the data starts moving.

That is why the comment was worth sending, and why it is worth repeating here: a FRIA completed perfectly against this template, for a system whose agents act through connectors, would still say nothing about the layer where the reach, the writes and the logs actually live. Until the template asks, the deployer has to — which is what the PAARA connector DPIA template in the kit is for.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — test one connector in production, not on paper

Thirty minutes, this Monday:

1. Pick one AI connector your organisation approved on documentation — the one whose review file you are most confident about.
2. Open the live tenant, not the datasheet, and write down three production facts: the scopes actually granted, the data it can actually reach today, and where its actions actually appear in a log.
3. Put the two columns side by side — paper vs production — and mark every line where they differ. Each difference is either a setting to correct or a review record to correct; both are findings.
4. Give the difference list one named owner and one date. Then schedule the same check for the next connector — one a week is enough to close the gap before an incident finds it.

The review approved the datasheet. Govern the tenant.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

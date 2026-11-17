# The Connector Audit — Issue #27

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #27 headline: The Task That Wasn't — an agent that can create and complete tasks can manufacture a record of work: the audit trail says done, the stand-up says done, and nobody did it. Plus change control for connectors — version pinning, change windows, re-approval on change — and a paper on DPIAs for the connector layer submitted to the Privacy Symposium Venice 2027: submitted, not accepted.**

---

## 1. The Connector Pattern — the work store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #13 tested Asana → ChatGPT. Teardown #34 tests **Asana → Claude**: the same work-management store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same record of your organisation's work.

- The read reach is the work in progress itself. Projects with their task lists and status, tasks with descriptions, subtasks, comments and attachments — tested in Teardown #34 on a **test workspace with dummy data only**: the tasks named in the request, a task nobody pointed the assistant at, a **private project** the connecting user was never added to, and a **control task** held in a separate test workspace, or behind project permissions, that was never connected. The filmed question is whether the reach is the use case, or the whole workspace made searchable.
- The write reach edits the record of work — and can certify it. Create a task, add a comment, change an assignee, mark a task complete, delete a task — each filmed in Teardown #34 with the approval step, or its absence, on camera. Two of those writes are sharper than the rest: **completion**, because a completed task is a claim that work happened, and **deletion**, because a deleted task takes its history with it. Whether either sits behind a human approval step is a filmed fact, not a documentation claim.
- There is no dataset shortcut for this one. Asana → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on — and nothing carries over from Teardown #13 either, because the grant, the approval surface and the log story belong to this route, not to the work store. Teardown #34's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #34 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Task That Wasn't

Every organisation runs on a record of work it mostly trusts. The task is created, the task is assigned, the task is commented on, the task is marked complete — and downstream of that small ceremony, real things happen: the stand-up moves on, the sprint closes, the invoice goes out, the audit samples the completed list and finds it in order. The record is treated as evidence of the work. This issue is about what happens to that trust when the thing writing the record is an agent.

Start with creation, because it looks harmless. An agent that can create tasks can fill a project with work nobody planned: tasks that sound plausible because they are assembled from the project's own language, assigned to real people, carrying due dates nobody agreed to. Each one is small. Together they are a plan that was never approved, wearing the formatting of one that was. The assignee who finds three new tasks on a Monday morning does not ask whether a human created them — the system does not volunteer that distinction, and the notification looks the same either way.

Completion is the sharper edge. A task marked complete is not a note; it is a certification. It tells the project board the work is done, tells the dependency chain it can proceed, tells the report the milestone landed. When a person marks a task complete, there is at least a person to ask. When an agent marks it complete — because it drafted the document the task asked for, because a planted instruction told it to, because "complete the onboarding checklist" was in the prompt and the checklist was the task list — the certification enters the record with no work behind it and no one who remembers certifying it. The task wasn't. The record says it was. Every downstream decision reads the record, not the reality.

Deletion completes the set. Work records are also where inconvenient history lives: the task that shows the deadline was known in March, the comment thread where the risk was raised and waved through. A delete right in the same grant that creates and completes is the right to edit the past as well as the future — and in most work stores, a deleted task does not leave a tombstone a reviewer can find. It leaves an absence, and absences do not show up in audits.

None of this requires a malicious agent. It requires an ordinary one, with write reach into the work store, doing approximately what it was asked, at machine speed, under a person's identity. The failure is not that the agent lies. The failure is that the record-keeping system was built for a world where writing to it was expensive — a human had to do the work, or at least do the typing — and that cost was the control. The connector removes the cost. What remains is the ceremony: created, assigned, completed, deleted, all still formatted as evidence, none of it still priced like evidence.

Teardown #34 tests this pattern on Asana → Claude: read reach across projects and tasks with a private project and a control task it was never given, write actions — create, comment, reassign, complete, delete — with the approval step filmed, a hidden instruction planted in a dummy task description, and the audit trail behind it all. It is not filmed yet, and this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates — usually twice, once per AI assistant, which is why this series tests the same work store from both sides.

The lesson for leaders: treat the work record as what it is — evidence your organisation acts on — and govern the AI grant to it accordingly. Someone senior should be able to answer, for your estate: which AI tools can write to the work store, whether they can complete and delete as well as create, whether a human approves those writes before they land, and what log would prove afterwards which completions were an agent's. If those answers do not exist, your record of work is being written. You just do not know by what — or which of last month's completed tasks weren't.

## 3. Harness — Change control for connectors: pin it, window it, re-approve it

This week's harness section is the control that keeps every other control true. Issues #4, #13 and #14 each circled it from a different side: #4 was silent scope creep — the grant quietly growing after approval; #13 was the rug pull — tool definitions changing under an approved connector; #14 was the vendor update nobody read — the routine release note that changed what the approval covered. Three names, one gap: **the connector you approved is not necessarily the connector still running, and nothing in most estates notices the difference.** Change control is the discipline that notices. It has three parts, and none of them needs new tooling.

**Pin the version you approved.** An approval should name not just the connector but its state at approval time: the scopes granted, the tool list with its definitions, the data classes reachable, the vendor and sub-processors as they stood. Snapshot that state into the approval record — a configuration export, a scope list, dated screenshots where no export exists. This is the baseline every later comparison runs against. Without a pinned baseline, "has anything changed?" is unanswerable, and an unanswerable question is never asked. The kit's discipline from Issue #25 applies: evidence or it didn't happen — an approval without a snapshot is an approval of a connector that may already not exist.

**Run changes through a window.** Vendor updates, scope requests and tool additions should land the way other production changes land: batched into a known window, announced to a named owner before they take effect where the platform allows it, and never silently mid-incident or mid-audit. Where the vendor pushes changes continuously and no window exists — the common case — the substitute is a scheduled diff: on a fixed cadence, someone compares the live connector against the pinned baseline. Scopes, tool definitions, connected data classes, vendor terms. The diff is small when nothing changed, which is most months; the month it is not small is the month the control earns its keep.

**Re-approve on change, with triggers written down in advance.** Issue #13 named the triggers; this section makes them a rule with an owner. A material change — a new scope, a changed or added tool definition, a new data class in reach, a vendor or sub-processor change — returns the connector to the approval process, proportionately: a fresh look at the four checks, not necessarily a fresh programme. The trigger list, the owner who watches for them, and the expiry rule — approvals lapse if the diff is not run — all go in the approval record itself, at approval time, while the approving energy still exists. A re-approval rule written after the first silent change is archaeology, not control.

Three rules make it work. **First, the baseline is part of the approval** — no snapshot, no approval; the file that grants the connector also freezes what was granted. **Second, silence is a change** — an update the vendor did not announce, discovered by the diff, is treated exactly like an announced one, and the discovery itself is recorded: it is evidence about the vendor, filed where the next renewal decision can find it. **Third, re-approval is fast by design** — a scoped re-check of what changed, against the pinned baseline, inside the change window; a re-approval process slow enough to be resented will be routed around, and a routed-around control is worse than none, because the file still claims it exists.

None of this requires a platform purchase. It requires treating a connector like what it already is — a production integration with write access to your systems of record — and giving it the change discipline your organisation already applies to everything else with that description. The connectors were exempted from change control because they arrived as features. They run as infrastructure. Govern them as infrastructure, and Issues #4, #13 and #14 become the same short meeting, held on schedule, instead of three separate surprises.

## 4. Regulator / Industry-Body Update — Privacy Symposium Venice 2027: a paper submitted, not accepted

This week's update is a submission, reported at exactly that status.

**On 16 November 2026, Vivek Kumar submitted a paper to the Privacy Symposium 2027 (Venice): "Governing the Connector Layer: What a DPIA Must Prove Before an AI Agent Is Allowed to Act" — Submission 87, via EasyChair.** The paper takes this programme's central claim into a data-protection room: a data protection impact assessment that stops at the AI system and never reaches the connectors underneath it — what they can read, what they can write, whose identity they act under, what log proves it — has assessed the diagram, not the deployment. It sets out what a DPIA has to prove at the connector layer before an agent is allowed to act, in the five-part form this newsletter's readers will recognise: reach, action, hostile content, the record, and change.

The status, stated at its actual precision: **submitted, and nothing more.** Submission 87 is a number on a submitted paper, not a result. No acceptance is claimed, implied, or expected in print before it exists — this newsletter has made the same distinction for conference talks, workshops and marketplace listings, and a symposium paper gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because the DPIA is where connector governance stops being a security preference and becomes a legal artefact — a document an organisation signs, files, and may one day have to defend. A symposium of privacy practitioners and regulators is exactly where the claim "assess the connector, not just the system" has to survive contact with the people who write, review and enforce those assessments. If the argument holds there, it holds in the approval meetings this newsletter is written for. And because the symposium is in person, in Venice: if the paper is accepted, the attorney/DSO travel check comes **before accepting** — submission and acceptance are different decisions, and only the second one needs a plane ticket cleared.

## 5. The Monday Fix — pin one connector's baseline

Forty-five minutes, this Monday — one connector, one snapshot, one trigger list:

1. Pick **one approved AI connector** — the work-store connector from this issue is the sharpest case, but any connector whose approval predates its last vendor update qualifies. If several qualify, pick the one with write access to a system of record.
2. Take the **baseline snapshot**: export or record the connector's current state — scopes granted, tool list and definitions as they stand, data classes reachable, vendor and sub-processors as named today. Date it, name who took it, and file it in the approval record next to the original approval. If the approval record has no original state to compare against, write that down too — that absence is the first finding.
3. Write the **re-approval triggers into the approval record**, from Issue #13's list: scope change, tool-definition change, vendor or sub-processor change, new data class in reach. Next to the list, name the owner who runs the diff and the cadence — monthly is a defensible default — and the expiry rule: if the diff is not run, the approval lapses to *unproven* until it is.
4. Run the **first diff now**, baseline against the original approval, and record the result either way. If nothing changed, the approval file gains its first piece of change-control evidence. If something did change — a scope, a tool, a term — the connector goes to re-approval before its next renewal or expansion, with the change named in the record.

Score the connector before you trust it — and pin what you scored, so next quarter's connector has to introduce itself again. This Monday, the snapshot is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

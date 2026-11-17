# The Connector Audit — Issue #33

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #33 headline: The Shadow Database — the Airtable-style base started as a spreadsheet someone could finally sort, and became the real system of record for customers, staff and money, with no owner, no classification and no review. Plus data classification for connector reach — what classes a connector may touch, applied table by table — and a paper on governing the connector layer in Asia, submitted to ASLI 2027: submitted, not accepted.**

---

## 1. The Connector Pattern — the database store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #20 tested Airtable → ChatGPT. Teardown #40 tests **Airtable → Claude**: the same database store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same tables.

- The read reach is the business as it actually runs. An Airtable-style account rarely holds one tidy database. It holds every tracker that outgrew a spreadsheet: the customer list, the hiring pipeline, the vendor register, the budget — each rebuilt as a base by the team that needed it, with linked records pulling data across tables. Tested in Teardown #40 on a **test account with dummy bases only**: the tables named in the request, tables nobody pointed the assistant at, account-wide search, linked-record reach — and a **control record** held in a separate base that was never connected or shared. The filmed question is whether the reach is the one table in the conversation, or the whole shadow estate made searchable.
- The write reach includes the write leaders most often miss. Create, update and delete records — and **change a field itself**: rename it, retype it, add a new one. A field change does not edit one record; it rewrites the shape of every record in the table at once. Each write is filmed in Teardown #40 with the approval step, or its absence, on camera.
- There is no dataset shortcut for this one. Airtable → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #20 either, because the grant, the approval surface and the log story belong to this route, not to the store. Teardown #40's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #40 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Shadow Database

Every organisation has two systems of record. The official one — procured, integrated, access-reviewed, the one that appears on the architecture diagram. And the shadow one — the base a team built on a Friday because the official system could not do the one thing they needed, which then quietly became the place the real data lives.

Watch how it happens, because it never happens by decision. A spreadsheet gets shared, then gets too big, then gets rebuilt as a base because the base can sort, filter, link and automate. A form gets attached, so new records arrive from outside. An automation gets added, so the base starts acting on its own rows. A second team copies the pattern. Within a year the base holds the customer list with the notes sales would never put in the CRM, the contractor register with rates, the incident tracker with the candid post-mortems — and it holds them under the governance of the tool it replaced: a sharing link, a personal account, a permission set nobody has reviewed since the week it was created. The spreadsheet grew up. Its controls did not.

Now add the connector — and, in this issue's pattern, a second one. An AI assistant connected to the official CRM goes through procurement. An AI assistant connected to the shadow base goes through a settings page, by the person who built the base, in the tool where they already work. The grant it receives is the grant the base's owner holds: every table they can see, every record those tables link to, and — as Teardown #40 films — potentially the structural writes too: delete a record, change a field, reshape the table. The data was never classified, because the base was never declared. The connector inherits that silence as permission.

There is a second, quieter layer. Shadow databases duplicate governed data without inheriting its protections. The customer record in the CRM has a retention rule, an access review and an owner. Its copy in the base — exported for convenience, enriched with working notes, linked to three other tables — has none of those, and it outlives the original: leavers leave the CRM and keep the base, projects close in the official system and stay open in the shadow one. When a leader asks "where does our customer data live?", the honest answer now includes a store that does not appear in the answer anyone gives.

Teardown #40 tests this pattern on Airtable → Claude: base and table read reach with a control record, write actions — create, update, delete, and the field change — a hidden instruction planted in a dummy record field, and the revision-history trail behind it all, including the question of whether a deleted record takes its own history with it. It is filmed on a test account with dummy bases only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result: list your own estate's bases and ask which of them is the real record for something that matters, who owns it, and which AI tools can reach it today. That answer is the finding, and it is already available to you.

The lesson for leaders: you cannot scope a connector to a store you have not admitted exists. The shadow database is governed the moment it is inventoried, classified and owned — and not before. Section 3 gives the classification rule to apply once the inventory exists.

## 3. Harness — Data classification for connector reach: what classes a connector may touch

Issue #17 set the data-class rules for agents: permissions per data class, not per tool, in four classes — **never alone** (a human approves that specific access, every time), **read alone, never write alone**, **act alone, inside the ladder**, and **no class, no access** (unclassified data is treated as never-alone until someone classifies it). This section applies those rules where they bite hardest: the base-and-table store, where one connector grant can span every class at once, because the tables were built by different teams for different purposes under one account.

**Step 1 — Classify at the table, not the account.** Walk the bases the connector can reach and assign each table a class from Issue #17, in writing, with a named owner: the table holding identifiable people, rates, health or financial detail starts at never-alone; the working pipeline or project table is read alone, never write alone; the agent's own operational table is act alone, inside its approved rung. A base that mixes classes — and most do, because linked records pull across tables — takes the class of its most sensitive reachable table until the links are cut or the grant is narrowed. Record the classification in the connector's approval record, next to the grant it constrains.

**Step 2 — Wire the class to the configuration, not the prompt.** As Issue #17 warned: a rule written into the agent's instructions is a rule the next planted instruction can argue with — and every teardown in this series plants one in a record field. The classes have to live in the route: separate grants or separate bases per class where the platform allows it, read-only configuration for the read-alone tables, the approval step on writes to anything above act-alone, and no connector reach at all into a table nobody has classified. Where the platform cannot separate the classes — one grant, whole account — the approval record says so plainly, and the connector's ceiling is set by the most sensitive table it can reach, not by the table it was connected for.

**Step 3 — Make a new table a re-approval trigger.** Shadow databases grow by addition: a new base for a new project, a new table for a new tracker, a new linked field that quietly joins a routine table to a sensitive one. Each of those changes the connector's effective reach without touching the connector. So the approval record names the trigger: a new base, table or linked-record field inside the connector's reach re-runs the classification in Step 1 before the data lands — or the connector's reach is pinned to named bases, so growth outside the list is growth it cannot see. Issue #27's change-control rule applies verbatim: pin the baseline, and let the diff ask the questions.

**The evidence.** As Issue #25 established: evidence or it didn't happen. For this control, keep the classification table itself — base, table, class, owner, date — plus one sampled reconstruction per class: pick a recent connector action in each class and show, from the record alone, that the class rule was followed (the approval for the never-alone access, the read-only configuration for the read-alone table, the ladder rung for the act-alone write). A class with no sample is a claim, not a control.

## 4. Regulator / Industry-Body Update — ASLI 2027: a paper submitted, not accepted

This week's update is a submission, reported at exactly that status.

**The paper "Governing the Connector Layer: PAARA, Impact-Assessment Duties, and Accountability for Agentic AI in Asia" was submitted to ASLI 2027 — Singapore, 26–27 May 2027, in person — on 15 November 2026, before the 16 November deadline, in the Information Technology Law area, under the affiliation Independent Researcher.** Notification is expected in **January 2027**; if the paper is accepted, the full paper is due **30 April 2027**. No submission ID was shown at submission, and none is claimed here.

The status, stated at its actual precision: **submitted, and nothing more.** No acceptance is claimed, implied, or expected in print before a decision exists. This newsletter has made the same distinction for conference papers, talks and workshops throughout this series, and a symposium paper awaiting notification gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it. Because the event is in person abroad, the standing rule in this series also applies: attorney/DSO travel clearance would be required before *accepting* any acceptance — not before submitting, and no acceptance exists to clear.

Why this room? Because the paper's subject is the fit between a connector-governance method and the impact-assessment duties Asian regimes place on the organisations deploying agentic AI — and ASLI is where that regional conversation is held by the lawyers and regulators who will have to apply those duties. As with the ICAIC paper in Issue #32, submitting the work there is the deliberate choice to have the instrument checked by people with no stake in it, in the jurisdiction whose duties it claims to map.

## 5. The Monday Fix — classify one connector's tables

Forty-five minutes, this Monday — one database connector, one inventory, one classification:

1. Pick **one connector with reach into a base-and-table store** — the Airtable estate from this issue is the natural start, because its grant is the one most likely to span every class at once. Export or list every base and table the connector can actually reach, from its connected-account view and scopes, not from memory. Any base nobody can explain is the first finding — record it as unclassified.
2. **Classify each table** using Issue #17's four classes, with a named owner per table: never alone, read alone / never write alone, act alone inside the ladder, and no class / no access for anything unclassified. Where linked records join a routine table to a sensitive one, the joined reach takes the higher class — write that down beside the link, not just beside the tables.
3. **Set the connector's ceiling from the highest class it can reach**, and close the gap between that ceiling and the job the connector was approved for: narrow the grant to named bases where the platform allows it, set read-only where the class is read-alone, put the approval step on writes above act-alone, and record whatever the platform cannot enforce as a named gap with an owner — instead of leaving it silent.
4. **File the classification table** — base, table, class, owner, date, and the re-approval trigger for new bases, tables and linked fields — in the connector's approval record, with one sampled action per class re-performed from the record alone. Next quarter's review starts from this file, and its first check is whether the store grew outside the list.

Score the connector before you trust it — and classify the store before you scope the grant, because a connector to an unclassified database has no ceiling, only a hope. This Monday, the classification table is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

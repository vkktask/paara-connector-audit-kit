# The Connector Audit — Issue #32

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #32 headline: The Brand Kit Rewrite — an agent that can edit designs and brand assets does not just change one file: it changes what the company looks like in public, everywhere that kit is used, under a person's name. Plus outward-facing actions as a class of their own — anything the public or a customer will see needs the human step — and the PAARA connector paper at ICAIC 2027: submitted, Paper ID 302, awaiting decision, not accepted.**

---

## 1. The Connector Pattern — the design store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #18 tested Canva → ChatGPT. Teardown #39 tests **Canva → Claude**: the same design store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same public face.

- The read reach is the company before it goes public. A design tool holds what never made it into a governed system: unreleased campaigns, draft announcements, the one-pager still being argued over — and the brand kit behind all of it: logos, colours, fonts, the voice the company speaks in. Tested in Teardown #39 on a **test Canva team with dummy designs only**: the designs named in the request, designs nobody pointed the assistant at, team-wide search, trashed and older versions — and a **control design** held in a separate team that was never connected or shared. The filmed question is whether the reach is the one design in the conversation, or the whole store made searchable.
- The write reach includes the only writes in this series that restyle. Create, edit, export, share — and **change a brand asset**: a colour, a logo, a font in the kit that every future design inherits. Each is filmed in Teardown #39 with the approval step, or its absence, on camera, including what an export or share actually sends out of the tool — who can open it, and in what form.
- There is no dataset shortcut for this one. Canva → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #18 either, because the grant, the approval surface and the log story belong to this route, not to the store. Teardown #39's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #39 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Brand Kit Rewrite

Most connector writes in this series change a record. A design write changes an appearance — and a brand-kit write changes every appearance that follows it.

Consider how a brand kit works. It exists so that a hundred people, and now their tools, produce work that looks like one company: the same logo, the same colours, the same fonts, the same tone. The kit is a multiplier. That is its purpose, and it is also the risk. A wrong figure in a spreadsheet is one wrong figure. A wrong — or quietly altered — asset in the kit is wrong everywhere the kit is used next: every new deck, every new post, every new one-pager inherits it, produced by people who never saw the change happen and would swear the kit was always that way.

Now add the connector. An AI assistant with write access to the design store can do the ordinary writes — draft a design, edit a headline, export a file — and, if the grant allows it, the kit write: adjust a brand colour, swap a logo file, edit the brand voice note. Each of those is a legitimate task in a real workflow; brand teams do them deliberately, with review, because the blast radius is the company's face. Done conversationally, at the speed of "make it pop," the same write carries no review at all — and the version history, if it names anyone, names the person whose account the connector acted through. The person who will be asked why the logo changed is a person who never touched it.

There is a second, quieter layer. Designs are outward-facing by destination: a design exists to be shown — to customers, to the market, to a regulator, to a hiring pool. An error inside an internal record waits to be found. An error in an exported design is published the moment it leaves the tool, and it leaves under the company's name, in the company's colours — possibly in colours that are no longer the company's, because the kit changed first. The approval question for a design connector is therefore not the record-keeper's question ("is this accurate?") but the publisher's question ("are we willing to be seen saying this?") — and that question has a different owner, a different standard, and no undo once the file has been forwarded.

Teardown #39 tests this pattern on Canva → Claude: design and brand-kit read reach with a control design, write actions — create, edit, export, share, and the brand-asset change, with the kit change verified by opening a second design built on that kit — a hidden instruction planted in a dummy design's text, and the activity and version-history trail behind it all, including the question of whether version history shows **who or what** made the change, and whether an export — the moment the design left the building — appears at all. It is filmed on a test team with dummy designs only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result: open your own brand kit's history and ask who can change it today, through which tools, with whose approval. That answer is the finding, and it is already available to you.

The lesson for leaders: internal writes and public writes are not one risk class. A connector that can edit what the public will see — and, above all, one that can edit the assets every future public thing is built from — deserves the publisher's control, not the plugin's: a named human step before the kit changes and before anything leaves. Section 3 turns that into a rule you can apply to every connector, not just this one.

## 3. Harness — Outward-facing actions are a class of their own

The action ladder this series uses — Observer, Contributor, Operator — sorts connector writes by how much the agent may do alone. This section adds the cut the ladder needs next: not how big the write is, but **who will see it**. An outward-facing action is any write whose result leaves the organisation's control and arrives in front of someone outside it — a customer, a prospect, the public, a counterparty — carrying the organisation's name. Issue #29 made the point for scheduling: a cancellation lands on a second person who never consented to the agent. Issue #30 made it for money: an invoice sent is the company's word and the company's claim, and needs a second pair of eyes. This issue generalises both: the class is defined by the audience, not by the tool.

**Step 1 — Classify by destination, not by feature.** Walk each approved connector's write list and mark every action whose output a non-employee can see: sends (mail, messages, invoices), publications (posts, pages, exports, shared links), commitments (bookings, cancellations, filings), and appearance changes (designs, brand assets, templates the outward things are built from). The same tool usually holds both classes — drafting a design is internal; exporting it is outward — so the classification belongs on the action, in the approval record, not on the connector as a whole.

**Step 2 — Put the human step on the outward class, in the tool where possible.** For every outward action: a named human sees the actual artefact — the design as it will appear, the invoice as it will read, the message as it will land — before it leaves, and approves that artefact, not a summary of it. Issue #30's rule for money applies verbatim here: an approver who sees a description approves a description. Where the tool cannot enforce the step, the approval record says so, names the compensating check (a second person in the workflow, a send-delay, a review queue), and gives that gap an owner — the same discipline as any other paper-only control in this series.

**Step 3 — Treat the templates and kits as outward actions squared.** Anything that changes what future outward things will look like or say — brand kits, email templates, signature blocks, proposal boilerplate, the system prompts of a customer-facing agent — gets the strictest version of the rule: the change itself is reviewed like a publication, because it is one, repeated. Record who may change it, through which route (the design tool's own UI is a route; so is every connector with write access to that store), and re-approve the route whenever a new connector gains write access to the store that holds it.

**The evidence.** As Issue #25 established: evidence or it didn't happen. For one outward action, keep the pair — the artefact as approved (dated screenshot or export) and the artefact as it left (the sent file, the published link, the log entry) — and check they match. A monthly sample of five outward actions, re-performed from the record alone, is the review that keeps the class honest; a mismatch between approved and sent is a finding about the route, not about the person whose name the log carries.

## 4. Regulator / Industry-Body Update — ICAIC 2027: a paper submitted and under review, not accepted

This week's update is a submission, reported at exactly that status.

**The paper "How Well Documented Are AI Connector Risks? Applying the PAARA Governance Methodology to Thirteen Public MCP and Enterprise Connectors" was submitted to ICAIC 2027 — the 6th IEEE International Conference on AI in Cybersecurity, Houston, 3–5 March 2027 — on 14 November 2026, via CMT, as Paper ID 302, in Track 8, under the affiliation Independent Researcher.** Its status is **Awaiting Decision**. The paper is the documentation audit this newsletter's method rests on, written up for review: the thirteen connectors, the seven-factor coding, and what the public documentation does and does not prove.

The status, stated at its actual precision: **submitted and under review, and nothing more.** Paper ID 302 is an identifier on a submitted paper, not a result. No acceptance is claimed, implied, or expected in print before a decision exists. And because the paper is under review, it is not being sent anywhere else: the same paper cannot go to other conferences while a decision is pending — extended versions belong after the outcome, with genuinely new content, not alongside it. This newsletter has made the same distinction for talks, workshops and symposium papers throughout this series, and a conference paper under review gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because a governance method earns its standing the way Section 3 says an outward action earns approval — by being seen by the people it will affect, in the form it will actually take. A cybersecurity conference's reviewers are the practitioners who would have to run the method on Monday. Submitting the audit there is the deliberate choice to have the instrument checked by people with no stake in it — the same second-coder discipline Issue #12 argued for, applied to the paper itself.

## 5. The Monday Fix — put the human step on one connector's outward actions

Forty-five minutes, this Monday — one connector, one write list, one new rule:

1. Pick **one connector with write access to something the public can see** — the Canva estate from this issue is the natural start, because its writes include the brand kit itself. List every write action the connector can take, from its approval record and its connected-app scopes, not from memory.
2. **Mark the outward class**: every action whose result a customer or the public will see — exports, shares, sends, publications — and, at the top of the list, every action that changes a template, a kit, or an asset those outward things are built from. For each marked action, write down whether a named human currently sees the actual artefact before it leaves. Where the answer is no or "unknown," that is the finding — record it as such, with the route it travels by.
3. **Set the rule that closes the class**: outward actions on this connector require a named approver who sees the artefact itself before it leaves, and kit/template changes require the same approval as a publication. Write the rule into the connector's approval record with a named owner and a review date; where the tool cannot enforce the step, record the compensating check beside it instead of leaving the gap silent.
4. **File the pair**: the marked write list, the rule, and one sampled outward action — the artefact as approved next to the artefact as it left — go into the approval record, dated. Next month's sample starts from this file, and its first check is whether approved and sent still match.

Score the connector before you trust it — and approve what leaves the building like a publisher, not a plugin, because the public never sees your approval process, only the artefact. This Monday, the outward list is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

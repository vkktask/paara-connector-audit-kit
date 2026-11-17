# The Connector Audit — Issue #20

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #20 headline: The Demo Org — the connector passed every control in the vendor's clean demo org, and production is not a demo org: it is years of sharing rules nobody remembers setting, integrations writing into fields nobody reviews, and data classes the demo never contained. Plus the approved-list discipline that keeps an approval honest, and a marketplace listing for the PAARA kit that is in motion — and is not adoption.**

---

## 1. The Connector Pattern — the CRM, assessed in the clean room

This week's pattern to check in your own estate:

Almost every connector approval begins in a clean room. The vendor demo runs in a demo org: a handful of tidy records, one user, sensible sharing rules, no integrations, no history. Your own proof of concept usually runs the same way — a sandbox spun up for the evaluation, populated for the evaluation, judged on the evaluation. The pattern tested in Teardown #27 (Salesforce → Claude) is what that clean room hides, once an AI can read and write the CRM:

- The demo org's sharing rules are the ones somebody just set. Production sharing rules are an archaeology: org-wide defaults from a decade ago, sharing rules added for a project that ended, a profile widened for one person who has since left. A connector inherits all of it. Whether it honours profiles and sharing rules at all is a filmed check in Teardown #27 — in a sandbox, stated as a sandbox — precisely because the production answer cannot be rehearsed in a clean org.
- The demo org has no other writers. Production CRMs are written by everything: reps, imports, integrations, web forms, customers filing cases. Every one of those text fields is an input channel for an AI that reads records. The demo's notes field is empty; production's notes fields are years deep, and nobody has ever reviewed them as prompts.
- The demo org contains no data class that scares anyone. Production contains the whole customer relationship — pricing, complaints, personal contact details, the candid note after the call. The grant approved against dummy data is the same grant that lands on that.

That is a pattern, not a finding about a named product. No vendor score is published here. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Demo Org

Every field note in this series has been about a gap between the paper and the production system. This one is about where the paper gets written: the demo org.

A demo org is not a lie. It is something more dangerous than a lie — it is a true statement about a system that does not exist in your organisation. The controls really do behave in the demo. The sharing rules really do bound the read. The approval step really does appear. The log really does show the session. Each claim is honestly demonstrated, on an org with twelve records, one user, and a configuration that was set up last Tuesday by someone whose job was to set it up well.

Production is the opposite in every dimension that matters. Production is the org where a sharing rule was widened in 2019 for a migration and never narrowed. Where three integrations write into the same notes field the AI now reads. Where the custom object nobody remembers holds the data class nobody classified. Where the user whose grant the connector borrows has accumulated permissions the way a desk accumulates drawers — every role they ever held, still open. None of this is malpractice. It is what a living system looks like after years of being useful. But it means the system the control was tested on and the system the control will run on share a name and a login screen, and not much else.

The pattern from earlier issues repeats in vendor form. Issue #6 was paper vs production inside your own assessment: the DPIA described the connector as documented, not as deployed. The demo org is the same gap, one step earlier and with better production values: the assessment was accurate, the demonstration was real, and both were about the wrong org. The vendor is not hiding your production system from you. They cannot show it to you. Only you can test in it — or in something honestly shaped like it.

Teardown #27 tests Salesforce → Claude in a sandbox / developer org with dummy data only, and the page says so on its face: read reach including a record the connecting user's sharing rules should keep out of reach and a control record in an org that was never connected, write actions including updating records and creating tasks with the approval step filmed, a hidden instruction planted in a dummy record, and the log trail through event monitoring and the setup audit trail — including an explicit note that where a developer org does not offer a production log surface, that gap is a limit of the test environment, not a finding about the product. It is not filmed yet; this note claims no result from it. The sandbox limit is stated in the teardown itself because the honest version of every sandbox test is the same: it proves what the connector does in an org like this one, and production is not an org like this one.

The lesson for leaders: a passed demo is evidence about the demo. Before a connector approval cites one, ask the question that separates the two orgs: which of our production facts — the legacy sharing rule, the extra integration, the accumulated profile, the unclassified object — would change this result, and have we tested with even one of them present? A test org with one deliberate mess in it is worth more than a clean org with a hundred records.

## 3. Harness — The approved-list discipline: the list is the control

This week's harness section comes from Training Module 7 of the open course (Governing AI Connectors): the approved list and the rollout. Most organisations have an approval *event* — a review, a sign-off, a ticket closed. The module's argument is that the control is not the event. The control is the **list** the event feeds, and the discipline that keeps the list true after the meeting ends.

**The approved list itself.** One list, owned by a named person, and every entry carries the same fields: the connector, the AI side it connects to, the data store and data classes it can reach, the scopes granted, the owner, the approval date, and the review date. An entry that cannot state its reach is not an approval — it is a rumour of one. The list is keyed by data source as well as by tool, so the same CRM connected through two different AI assistants appears as what it is: two grants into one vault, reviewed as a pair as well as separately.

**Exceptions with expiry.** Every estate has the connector that cannot meet the standard today and is needed anyway. The discipline is not to refuse it or to wave it through — it is to write it down as an exception, with three things attached: the specific gap being accepted, the compensating control, and an **expiry date**. An exception without an expiry is not an exception; it is a silent amendment to the standard, and it will outlive everyone who agreed to it. When the date passes, the exception lapses and the connector goes back through review — renewal is a decision, made on purpose, not a default.

**Rollout order.** Approval is not deployment to everyone at once. The module's order: pilot with the smallest group whose work proves the use case, on the narrowest scopes that let it function; widen the group before you widen the scopes; widen scopes only on evidence from the pilot, never on request volume. Each step is reversible, and the kill switch is tested at the pilot stage, while the blast radius is a pilot-sized radius. A rollout that starts at full estate and full scope has no steps left when something goes wrong — only an incident.

**Where this sits in the gates.** The approved list is the harness made durable. The gates decide whether a connector may act; the list is how the organisation remembers what it decided, notices when reality drifts from the decision — a scope changed, a vendor updated, an exception expired — and forces the decision to be taken again. Approval you cannot look up is approval you cannot enforce.

## 4. Industry-Body / Distribution Update — The PAARA kit on Agensi: a listing in motion, not adoption

This week's update is reported at its exact status, and the status is deliberately unglamorous.

On 16 November 2026, Joeri Brons of Agensi offered a listing for the PAARA Connector Audit Kit on the Agensi marketplace. Vivek Kumar replied the same day, agreeing to list at the minimum price — the aim stated in the reply was to maximise adoption of the method, not revenue from the kit — and noting that the kit is also to be turned into a SKILL. One administrative fact, stated here because this newsletter reports things at their actual precision: payment and payout for the listing will be under someone else's name, not Vivek Kumar's.

That is the complete, current status: **an offer made, a reply sent agreeing to the minimum-price structure, and the listing in motion, awaiting the next step from Agensi.** Nothing further is claimed. The listing is not live as far as this newsletter's work has verified, no sale, download or deployment is reported, and — this is the distinction this series keeps on every update — **a marketplace listing is distribution, not adoption.** Adoption is an organisation running the method on its own estate and being able to say so. When that exists, it will be reported here, named and evidenced. Until then, the honest sentence is the short one: the kit was offered a shelf, the terms were agreed, and the shelf is being built.

Why report something this preliminary at all? Because the connector layer has a distribution problem as much as a governance one: the people who need an audit method on Monday morning find what is listed, packaged and priced to take, not what is best. Putting an open method on a marketplace shelf at the minimum price is one route at that problem — recorded here as a route taken, at the stage it has actually reached.

## 5. The Monday Fix — put one deliberate mess in your test org

Thirty minutes, this Monday:

1. Pick one connector whose approval rests on a demo or a clean proof of concept — ideally the one connected to your CRM or your file store. Write down, in one line, what the approval claims: the reach, the approval step, the log.
2. List three production facts the demo org did not have. Use your own estate's real archaeology: the legacy sharing rule nobody has reviewed, the extra integration that writes into the same records, the user profile that accumulated permissions across roles, the unclassified object or field. Pick facts, not categories.
3. Recreate exactly one of them in your test org — the sharing rule is usually the fastest — and re-run the single check it touches, on dummy data only. Does the connector's reach change? Does the log still tell the story? Record the result next to the original approval claim, either way.
4. If the result changed, the approval now carries a note, not a verdict: "tested clean; re-tested with [the production fact]; result differed in [the specific way]; re-review date set." If it did not change, that is now evidenced too — one production-shaped fact at a time. Either way, the approval stops being a claim about a demo org and starts being a claim about yours.

You cannot test in production. But you can stop testing in a fantasy. One deliberate mess on Monday, and the next approval is about a system that resembles the one you run.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

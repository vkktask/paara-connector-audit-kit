# The Connector Audit — Issue #24

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #24 headline: Tested Live vs Documented — the documentation audit scores what a vendor says a connector does; a live test films what it actually does, and this series exists because the two are not the same document. Plus the five PAARA questions from Training Module 1, set out as a one-page card you can run in any review meeting — and an industry-body note: joining the OWASP Agentic Security Initiative and MCP-hardening channels, as a participant.**

---

## 1. The Connector Pattern — the messaging layer, reached through a middle layer

This week's pattern to check in your own estate:

Every previous teardown in this series reached its store through the AI tool's own connector. Teardown #31 (Slack → Claude via MCP) adds a layer: the **MCP server** sitting between the assistant and the workspace — a separate piece of software, run by someone, holding the grant, translating every request. The pattern to check is not just what the connector reaches. It is how many layers the reach passes through, and who operates each one.

- The read reach is the workspace's least formal writing. Channels public and private, threads, and DMs — tested in Teardown #31 in a test workspace with dummy messages only: the channel named in the request, the private channel the connecting user belongs to, the DM thread, and a **control channel** the connecting user was never added to. The filmed question is whether the reach honours the membership boundaries Slack itself enforces, or walks around them under one grant — and whether the MCP server's tool list, read out on camera, describes the reach the grant actually has.
- The write reach lands on other people's record of what was said. Post, reply, edit, delete are filmed checks in Teardown #31, with the approval step filmed. Two details decide the pattern: whether an edit can touch a message the connecting user wrote themselves — rewriting what a person appears to have said — and **whose name a posted message carries**: the user's, with nothing marking it as AI-made, or a visibly separate app identity.
- The log trail now has three places to look instead of two. Slack's own records, Claude's conversation history — and the MCP server's own trail, if it keeps one. A middle layer that logs nothing is a gap in the middle of the story: the two ends can both be honest and the reconstruction still fails, because the translation between them was never recorded.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #31 is not filmed yet — its scores are blank until the film, for a reason this issue's field note explains in full: Slack MCP is one of the 13 connectors in the published documentation audit, its documentation codes exist, and they are still not allowed anywhere near this teardown's scorecard. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — Tested Live vs Documented

This newsletter runs on two kinds of evidence, and this note is about why it keeps them apart — because confusing them is the most common way connector assurance goes wrong.

**The documentation audit** — the PAARA audit of 13 connectors, scored from vendor documentation retrieved 9 November 2026 — reads what vendors say. It is genuinely useful, and its limits are structural. Documentation is written to describe what a connector is meant to do, on the configuration the vendor had in mind, on the day it was written. It is silent exactly where it matters most: in that audit, the unknown code — U, "the documentation does not say" — is what turns every score into a band. Twelve of 13 connectors document no prompt-injection defence; that is a true statement about their documentation. It is not, by itself, a measurement of their behaviour. And documentation moves: a connector's tool definitions and scopes can change after the page you read was published — the rug pull of Issue #13 — without any announcement reaching the person who approved it.

**The live test** — the Connector Spy Test teardowns — films what a connector does: in a test account, with dummy data, on camera, one check at a time. It catches the things documentation cannot say. Whether an approval step actually appears before a write, or exists only in a help article. Whether the reach stops at a boundary the vendor's own platform enforces — a private channel, a control file, an unconnected account — or walks around it. Whether the log that the documentation describes actually contains the session you just ran. Defaults as shipped and configured, behaviour as observed, evidence a viewer can replay.

The live test has limits too, and the teardowns state them on their face. One test account, on one plan tier, on one day: an audit surface the test plan does not include is reported as a gap in the test, not a finding about the product. A filmed test is a measurement of an integration as configured, not a verdict on a vendor for all time — configurations change, and so do connectors.

So the method is both, in that order, never merged. **Documentation first, to find the questions** — the silences in the documentation are the test plan. **Film second, to get the answers** — and where the film and the documentation disagree, publish the disagreement, with neither score edited to match the other. A score copied from documentation into a live-test scorecard would look like evidence and be none: it would be a claim about a document, wearing the authority of a measurement.

Teardown #31 is where this stops being a principle and becomes a demonstration. Slack MCP is one of the 13 audited connectors — the audited integration itself, reached through the MCP route into Claude. Its documentation codes exist: F1–F7 coded, a band assigned, F4 = N because Slack documents server-side audit logging as present. Every one of those codes is context on the teardown page, labelled as context. The scorecard is blank. When the film exists, the comparison gets published side by side — where live behaviour matched the documentation, and where it did not — and that comparison, not either score alone, is the finding.

The lesson for leaders: ask of every connector assurance you are handed, *which kind of evidence is this?* A documentation review presented as a test is how organisations end up certain about systems nobody has ever watched working. Tested live and documented are both legitimate. They are not interchangeable, and the label is not a detail.

## 3. Harness — The Five PAARA Questions, as a one-page card

This week's harness section is the smallest complete tool in the programme: **the five PAARA questions** — Module 1 of the open training course, *Governing AI Connectors* — set out as a one-page card. The teardowns run four filmed checks; this card is what you run in the meeting before anyone films anything, on any connector, in about twenty minutes. Print it, and write the answers down — including, especially, when the answer is "the documentation does not say."

---

**THE FIVE PAARA QUESTIONS — one connector, one page**

Connector: ______________  Data source it reaches: ______________  Owner: ______________  Date: ______

**1 · What can it reach?**
The systems, data, and conversations inside the grant — including other people's content, not just the connecting user's own.
Answer / evidence: ______________________________________________

**2 · Does it touch sensitive data?**
Personal data, credentials, financial or health information, confidential business material — anything whose exposure would hurt.
Answer / evidence: ______________________________________________

**3 · Is it least-privilege, or broader than needed?**
Whether the permissions match the job — or quietly include write access, admin reach, or whole-tenant scope nobody asked for.
Answer / evidence: ______________________________________________

**4 · Can you reconstruct what it did afterwards?**
Documented logging: who or what acted, which tools ran, what data was touched. No log means no reconstruction — and no incident response.
Answer / evidence: ______________________________________________

**5 · How does it amplify insider risk?**
What a careless or malicious insider — or an attacker holding their token — could do through this connector that they could not do as quickly, quietly, or at such scale without it.
Answer / evidence: ______________________________________________

Scoring discipline: an unanswered question is not a pass. "Not documented" is recorded as **unknown**, and unknown is treated as risk until evidence replaces it — that is what turns five answers into a defensible risk band.

---

Three rules for running the card. **First, evidence or it didn't happen:** each answer names its source — the authorisation screen, the vendor's documentation, the admin console — the way the training module insists on writing down what the documentation actually says, including when it says nothing. **Second, the card is keyed by data source, not by tool** — the rule from Issue #5: the same store reached through two assistants gets one card per route, because the grant, the approval surface and the log differ by route, as Teardown #31's middle layer shows again. **Third, the card expires:** a vendor update, a scope change or a new data class reopens it — the re-approval triggers from Issue #13 apply to a one-page card exactly as they apply to a full DPIA.

Module 1's worked example runs these questions against a real connector from the audit; the card above is the same five questions with the training wheels off. Twenty minutes, five answers, one page in the governance file — and the connectors that cannot survive five questions never reach the ones that need a camera.

## 4. Regulator / Industry-Body Update — OWASP: in the ASI and MCP-hardening channels, as a participant

This week's update is about where the connector layer's working standards are actually being drafted — and about showing up there accurately.

**On 16 November 2026, Vivek Kumar joined two channels in the OWASP Slack workspace: #team-genai-asi-agentic-security-initiative — the channel of OWASP's Agentic Security Initiative, 1,244 members after he joined — and #team-genai-asi-mcp-hardening, the small working channel on hardening MCP deployments, 28 members after he joined. Membership in both was verified in the channels' member lists.** He also has open contributions in the OWASP GenAI project recorded earlier in this newsletter (Issue #12: the MCP Top 10 issue and pull request, and the GenAI V2 issue, posted 16 November 2026 — open, not merged, no adoption claimed).

The framing matters, so here it is plainly: **this is participation, not leadership.** No role in the Agentic Security Initiative is claimed, no maintainership, no authorship of its guidance. Joining a working channel is the practitioner equivalent of taking a seat in the room where drafts circulate — it is how you hear about a hardening guide while it can still be commented on, how the pilot conversations this programme runs (the PAARA pilot outreach recorded in Issue #15 went to OWASP GenAI contacts, among others) find the people actually doing the work, and how a framework like PAARA gets exposed to the room most likely to find its holes. The MCP-hardening channel is the more pointed of the two for this programme: 28 people working on exactly the middle layer Teardown #31 films.

Why carry a channel join in the regulator-and-industry-body slot? Because the connector layer will be governed by a stack — regulation on top, and underneath it the working guidance written by bodies like OWASP's GenAI and Agentic Security projects, which procurement questionnaires and enterprise standards then cite. The comments this programme files with regulators are one direction of travel. Being present, accurately described, in the rooms writing the layer underneath is the other. Both are recorded here the same way: what was done, when, and no more than that.

## 5. The Monday Fix — film one check on one connector you already approved

Thirty minutes, this Monday — one connector, one check, one camera:

1. Pick **one connector your organisation has already approved** — ideally the one whose approval rested most heavily on documentation. Open its approval record and write down, in one line, what the documentation claims about the check you are about to run: the reach, the approval step, the hijack defence, or the log.
2. In a **test account with dummy data only** — never the production tenant — run that **one check** from the teardown format, on screen recording: the control test is the fastest honest one. Ask the connected AI a question whose answer exists only somewhere it should not reach — a control channel, a control file, an unconnected account — and film what comes back.
3. Write the filmed result **next to** the documentation claim in the approval file, dated, with the recording kept. Do not edit the original claim. The pair — claim and film, side by side — is the record.
4. If they disagree, that connector goes to the top of the re-review queue with a named owner and a date — not as a scandal, but as the system working: the approval was written from documentation, the evidence has now improved, and the decision gets revisited at the new standard. If they agree, you have something almost as valuable: one approval in the file that is no longer paper-only.

Score the connector before you trust it — and, once, on camera, check that the score survived contact with the real thing. This Monday, one filmed check is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

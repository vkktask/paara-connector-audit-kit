# The Connector Audit — Issue #23

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #23 headline: The Personal Account at Work — the connector review asks which tool and which scopes, but the question that decides everything else is whose account sits behind the grant: a managed work account the organisation can audit, restrict and revoke, or a personal account it cannot even see. Plus the Module 0 inventory done properly — the five places to look, expanded into a sweep that catches the connections nobody approved — and a judging-service note: the Apart Research December 2026 sprints.**

---

## 1. The Connector Pattern — the file store, reached through whoever's account

This week's pattern to check in your own estate:

Most connector reviews ask two questions about a file-store connection: which store, and which scopes? The pattern tested in Teardown #30 (Google Drive → ChatGPT) adds the third question, the one that quietly decides the other two: **whose account is the grant attached to?**

- The read reach is the same store on paper, and a different store in practice. A Drive connector behind a managed work account reaches the files that account can reach, inside an estate an admin can inspect — shared drives, sharing policies, an audit log. The identical connector behind a personal account reaches whatever that person has accumulated and been shared into over years, in an account with no admin, no sharing policy and no organisational log at all. Teardown #30 films the read reach in a test account — owned files, a shared-with-me file, a trashed file, and a control file in an account that was never connected — and the filmed question underneath every check is which account's rules the reach obeys.
- The write reach inherits the account's governance, or its absence. Create, edit, share and delete are filmed checks in Teardown #30, with the approval step filmed. Run the same actions through a personal account and the approval question changes shape: there is no admin to require one, no policy to inherit, and a share made from a personal account is a disclosure the organisation may never learn happened.
- The log trail is where the account question becomes decisive. In a managed estate, Check 4 of the teardown has somewhere to go: Drive's activity record and the Google Workspace audit log. Behind a personal account there is no admin audit log to check — the trail is whatever the individual user can see in their own account, which means the organisation's answer to "what did the AI read?" is "ask the person." If they have left, there is nobody to ask.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #30 is not filmed yet — its scores are blank until the film. It pairs with Teardown #5 (Google Drive → Claude): the same file store, the other AI side, tested fresh. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Personal Account at Work

Shadow AI is usually told as a story about tools: an unapproved app here, a browser extension there. This note is about the quieter version, one level down — **shadow AI at the account level.** The tool is often the approved one. What is unapproved is the account it is running through.

It happens innocently, which is why it spreads. The work AI tool is slow to provision, or the team tier lacks the connector someone needs, so a person connects the work file store to their personal AI subscription — the one on their own card, with the better model. Or they sign into the AI tool with a personal account because that is the login their browser offered first. Or the organisation's AI rollout covers one department, and everyone else simply brings their own. No policy is dramatically broken in the moment. A file gets summarised. The work gets done.

Then the consequences arrive, on a delay, and none of them needs a breach either.

First, **the data now lives under consumer terms.** Work documents read through a personal AI subscription are processed under that person's individual agreement with the vendor — not the organisation's enterprise terms, not its data-processing addendum, not its retention and training settings. The organisation negotiated protections for the work account. The personal account never saw them.

Second, **there is no log the organisation can pull.** Every teardown in this series ends with the same question — could you rebuild what the AI read and changed, from records? For a personal account the answer is structural, not a vendor gap: the records, where they exist, belong to the individual's account. The organisation cannot audit what it does not administer, and "the employee checked and said it was fine" is not an audit trail.

Third, **the grant survives the employment.** Issue #16 covered the leaver's token — grants that outlive a disabled work account, a process problem with a runbook answer. The personal account is worse: there is nothing to disable. When the person leaves, the account leaves with them, the connections made through it leave with them, and any work data sitting in that account's history, files and synced copies is simply gone from the organisation's reach — not deleted in anger, just no longer theirs to retrieve, hold or produce.

Fourth, **nobody can revoke what nobody can see.** The kill switch this newsletter keeps returning to — disable the identity, revoke the tokens, confirm the sessions dead — assumes an identity the organisation issues. A personal account has no off switch on the organisation's side. The only control available is the one applied before the fact: approved tools provisioned fast enough that the personal route is never the easier one.

Teardown #30 tests Drive → ChatGPT in a test account with dummy files only, and the page says so on its face: file read reach including shared-with-me and a control file, write actions — create, edit, share, delete — with the approval step filmed, a hidden instruction planted in a dummy document, and the log trail through Drive activity and the Workspace audit log. It is not filmed yet; this note claims no result from it.

The lesson for leaders: review the account, not just the app. Every connector approval should name, in writing, the account class the grant may sit on — managed work account, or not at all — the way it names the scopes. A connector on the wrong account is not a minor deviation from the approval. It is a different system from the one you approved.

## 3. Harness — The Module 0 Inventory, Done Properly: five places to look

This week's harness section is the foundation the whole method stands on: **the Module 0 inventory** — Module 0 of the open training course, *Governing AI Connectors* — done properly. Every later control in this newsletter assumes it: you cannot scope, log, drill or revoke a connection you have not listed. And the inventory most organisations have — the procurement list, the SSO app list — misses exactly the connections this issue is about, because a connector authorised by one person, through one account, appears on neither.

The inventory that works is a sweep of **five places**, the same five named in this programme's shadow-AI audit post — expanded here into what to open, what to record, and how the five lists catch each other out.

**Place 1 — Connected Apps inside the AI tools themselves.** Open the settings of each AI assistant in use — ChatGPT, Claude and their peers — and read the connected-apps / connectors view for each account class in play. This is the only place the grant is described in the connector's own terms: which store, which account, read or read-write. Record, for each connection: the tool, the store it reaches, **the account it is attached to — work or personal**, the owner by name, and the date connected, if shown. A connection nobody recognises is not an error in the list. It is the list working.

**Place 2 — Google third-party access (and its equivalents).** In Google, the third-party access view in the account — and the admin-side security view in Workspace — shows which external apps hold access to Drive, Gmail and Calendar data, including access granted outside the AI tools entirely. Run the same check in the Microsoft estate and any other identity provider in use. This place catches the connections made through "Sign in with Google" flows that never passed through an AI tool's settings page — the two lists should name the same grants, and every difference between them is a question.

**Place 3 — Slack apps (and each collaboration platform's app directory).** Workspace app directories list installed apps and bots, who installed them, and what they can reach. AI assistants and connector bridges installed into Slack, Teams or their peers are integrations with data reach, approved — if they were approved — by a workspace admin click, not by the connector review. Record them on the same inventory, keyed by the data they can read, not by the platform they sit in.

**Place 4 — Browser extensions.** The extension is the connector nobody calls a connector: an AI sidebar or summariser extension can read the page in front of it — the CRM record, the mailbox, the document — under the user's browser session. Sweep managed browsers through their admin consoles where they exist, and sample unmanaged ones by asking. An extension that can read every page is a read grant over every system the browser touches, and it belongs on the inventory in those words.

**Place 5 — Expense reports for AI subscriptions.** The money trail is the inventory of last resort, and for personal accounts it is the only one there is. Personal AI subscriptions expensed — or absorbed — by staff are a direct list of AI in use outside provisioning: each line names a person running work through an account the organisation does not manage. Finance holds this list already. Nobody has to build it; somebody has to read it as a security document once.

Then the discipline that makes five lists into one inventory: **reconcile them against each other, and key the merged list by data source, not by tool** — the rule from Issue #5. The same Drive store reached from ChatGPT, from Claude and from an extension is one store with three doors, and the inventory should say so. Every entry gets a named owner, an account class, and a review date. Every entry on no list but one — the connection only the expense report knows about — is the shadow-AI finding, and it goes to the top of the review queue, not the bottom of the spreadsheet.

Module 0 is deliberately unglamorous. It is also the module everything else cites: the Monday question in Issue #8 is this inventory, kept alive weekly. Do the sweep once, properly, and the weekly habit is just keeping it true.

## 4. Regulator / Industry-Body Update — Apart Research December 2026 sprints: judging, as a service to the field

This week's update is not a consultation or a call for papers. It is the other way a practitioner contributes to the bodies that set the field's standards: **judging service** — independent evaluation, given to a research community, on the record.

**Apart Research runs two online sprints in December 2026: Threat Intelligence, 4–6 December, and Agent Attribution, 11–13 December.** Vivek Kumar is confirmed on the judging panel for the December 2026 Threat Intelligence sprint. The Agent Attribution sprint follows a week later, 11–13 December. Both are December 2026 online sprints in Apart Research's hackathon programme, where judging means scoring submitted work against the sprint's criteria — the same discipline this newsletter applies to connectors, pointed at research: evidence first, scores that can be shown, a verdict that can be defended to the person who did the work.

Why carry judging in the regulator-and-industry-body slot at all? Because the connector layer's standards will not be set by regulators alone. They are being set now, in research communities evaluating what agentic systems actually do — threat intelligence on real attacks, attribution methods for agent actions — and the practitioners who judge that work shape what counts as good evidence in it. A judging panel is also, not incidentally, the second-coder discipline of Issue #12 performed in public: independent scorers, the same artefact, scores compared.

The standing notes are the honest ones: judging is service, recorded as service. It is not an award, not an adoption of PAARA by Apart Research, and not a result — the sprints have not run yet. What can be said is what is confirmed: the panel place for Threat Intelligence, 4–6 December, and the two sprint dates. The connector-audit programme will report what the judging surfaces — the patterns in what was submitted, in general terms — after the sprints close, the way it reports everything else: what the evidence supports, and no more.

## 5. The Monday Fix — flag every personal account in the inventory

Thirty minutes, this Monday — one sweep, one flag:

1. Take the inventory — last week's, or the five-place sweep from Section 3 if it has never been run. Work down it once with a single question per entry: **which account is this connection attached to — a managed work account, or a personal one?** Mark every entry one of three ways: work account, personal account, or unknown. Unknown counts as personal until proven otherwise.
2. For every personal-account entry, write down the three facts from the field note next to it: the data is under consumer terms, there is no organisational log, and the grant cannot be revoked from your side. One line each. This is the risk statement the approval never contained.
3. Give each flagged entry one of two dispositions, with a named owner and a date: **migrate** — reconnect the tool through a managed work account, then disconnect the personal grant and confirm it is gone from both sides' connected-apps views; or **except** — a written exception with an expiry date, for the rare case where the personal route is genuinely the only one, reviewed when it expires like every other exception on the approved list.
4. Close the loop at the source: check the provisioning queue for the tools people most often bring themselves, and time it. If the approved route takes three weeks and the personal route takes three minutes, the inventory will refill — the fix is a provisioning clock short enough that the work account is the easy account.

Score the connector before you trust it — and check whose account it is scored under. This Monday, the flag is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

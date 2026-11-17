# Connector Spy Test — Series Index and Filming Priority Plan

**The complete matrix: 48 teardowns, 24 stores, every store tested from two AI sides. Status of the whole series: designed and published as pre-filming drafts — all scores, verdicts and one-setting fixes are BLANK (TO BE FILLED from filmed live tests). Nothing in this index is a result. It is the map, the filming order, and the schedule.**

By Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, presented as 6–8 components). Every teardown runs the same four PAARA checks on camera: (1) read reach, including a control record the connecting account was never given; (2) write actions, with the approval step — or its absence — filmed; (3) a hidden instruction planted in dummy data; (4) the log trail. Scores are filled only from a filmed live test on a test account, tenant or sandbox with dummy data only. Nothing carries over from the 13-connector documentation audit (documentation retrieved 9 November 2026), and nothing carries over between the two AI sides of a pair.

---

## The matrix, by store

### Mail

| # | Teardown | Pair |
|---|---|---|
| 1 | [Gmail → ChatGPT](connector-spy-test-1-gmail-to-chatgpt.md) | Pairs with #6 — same mailbox, different AI side |
| 6 | [Gmail → Claude](connector-spy-test-6-gmail-to-claude.md) | Pairs with #1 |
| 22 | [Outlook / Microsoft 365 Mail → ChatGPT](connector-spy-test-22-outlook-to-chatgpt.md) | Pairs with #43 — also part of the Microsoft 365 set |
| 43 | [Outlook / Microsoft 365 Mail → Claude](connector-spy-test-43-outlook-to-claude.md) | Pairs with #22 |

### Files and wiki

| # | Teardown | Pair |
|---|---|---|
| 5 | [Google Drive → Claude](connector-spy-test-5-drive-to-claude.md) | Pairs with #30 — same file store, different AI side |
| 30 | [Google Drive → ChatGPT](connector-spy-test-30-drive-to-chatgpt.md) | Pairs with #5 |
| 17 | [Dropbox → ChatGPT](connector-spy-test-17-dropbox-to-chatgpt.md) | Pairs with #38 |
| 38 | [Dropbox → Claude](connector-spy-test-38-dropbox-to-claude.md) | Pairs with #17 |
| 3 | [Notion → Claude](connector-spy-test-3-notion-to-claude.md) | Pairs with #28 — same wiki, different AI side |
| 28 | [Notion → ChatGPT](connector-spy-test-28-notion-to-chatgpt.md) | Pairs with #3 |

### Chat

| # | Teardown | Pair |
|---|---|---|
| 2 | [Slack → ChatGPT](connector-spy-test-2-slack-to-chatgpt.md) | Pairs with #7 — native connector route |
| 7 | [Slack → Claude](connector-spy-test-7-slack-to-claude.md) | Pairs with #2 |
| 31 | [Slack → Claude via MCP](connector-spy-test-31-slack-mcp-to-claude.md) | The third route into the same workspace — and the one integration in this series that also appears in the 13-connector documentation audit (as an MCP connector). Documentation codes exist for it and are context only; the live scorecard is filled from the film alone |

### Meetings and scheduling

| # | Teardown | Pair |
|---|---|---|
| 4 | [Zoom → ChatGPT](connector-spy-test-4-zoom-to-chatgpt.md) | Pairs with #29 — same meeting platform, different AI side |
| 29 | [Zoom → Claude](connector-spy-test-29-zoom-to-claude.md) | Pairs with #4 |
| 14 | [Calendly → ChatGPT](connector-spy-test-14-calendly-to-chatgpt.md) | Pairs with #36 — same scheduling layer, different AI side |
| 36 | [Calendly → Claude](connector-spy-test-36-calendly-to-claude.md) | Pairs with #14 |
| 25 | [Google Calendar → ChatGPT](connector-spy-test-25-calendar-to-chatgpt.md) | Pairs with #46 — same calendar store, different AI side |
| 46 | [Google Calendar → Claude](connector-spy-test-46-calendar-to-claude.md) | Pairs with #25 |

### CRM

| # | Teardown | Pair |
|---|---|---|
| 9 | [Salesforce → ChatGPT](connector-spy-test-9-salesforce-to-chatgpt.md) | Pairs with #27 — same CRM, different AI side |
| 27 | [Salesforce → Claude](connector-spy-test-27-salesforce-to-claude.md) | Pairs with #9 |
| 12 | [HubSpot → ChatGPT](connector-spy-test-12-hubspot-to-chatgpt.md) | Pairs with #33 — same CRM, different AI side |
| 33 | [HubSpot → Claude](connector-spy-test-33-hubspot-to-claude.md) | Pairs with #12 |

### Work trackers and tables

| # | Teardown | Pair |
|---|---|---|
| 8 | [Jira → ChatGPT](connector-spy-test-8-jira-to-chatgpt.md) | Pairs with #35 — same issue tracker, different AI side |
| 35 | [Jira → Claude](connector-spy-test-35-jira-to-claude.md) | Pairs with #8 |
| 13 | [Asana → ChatGPT](connector-spy-test-13-asana-to-chatgpt.md) | Pairs with #34 — same work store, different AI side |
| 34 | [Asana → Claude](connector-spy-test-34-asana-to-claude.md) | Pairs with #13 |
| 21 | [Trello → ChatGPT](connector-spy-test-21-trello-to-chatgpt.md) | Pairs with #41 — same board store, different AI side |
| 41 | [Trello → Claude](connector-spy-test-41-trello-to-claude.md) | Pairs with #21 |
| 20 | [Airtable → ChatGPT](connector-spy-test-20-airtable-to-chatgpt.md) | Pairs with #40 — same database store, different AI side |
| 40 | [Airtable → Claude](connector-spy-test-40-airtable-to-claude.md) | Pairs with #20 |

### Money

| # | Teardown | Pair |
|---|---|---|
| 15 | [Stripe → ChatGPT](connector-spy-test-15-stripe-to-chatgpt.md) | Pairs with #32 — same payments account, different AI side. Filmed in Stripe test mode only |
| 32 | [Stripe → Claude](connector-spy-test-32-stripe-to-claude.md) | Pairs with #15 |
| 16 | [QuickBooks → ChatGPT](connector-spy-test-16-quickbooks-to-chatgpt.md) | Pairs with #37 — same books, different AI side. Filmed in a sandbox company only |
| 37 | [QuickBooks → Claude](connector-spy-test-37-quickbooks-to-claude.md) | Pairs with #16 |

### Design

| # | Teardown | Pair |
|---|---|---|
| 18 | [Canva → ChatGPT](connector-spy-test-18-canva-to-chatgpt.md) | Pairs with #39 — same design store, different AI side |
| 39 | [Canva → Claude](connector-spy-test-39-canva-to-claude.md) | Pairs with #18 |

### Automation and code

| # | Teardown | Pair |
|---|---|---|
| 19 | [Zapier / Make → ChatGPT](connector-spy-test-19-zapier-to-chatgpt.md) | Pairs with #47 — same automation account, different AI side |
| 47 | [Zapier / Make → Claude](connector-spy-test-47-zapier-to-claude.md) | Pairs with #19 |
| 11 | [GitHub / GitHub Copilot → ChatGPT](connector-spy-test-11-github-to-chatgpt.md) | Pairs with #42 — same code store, different AI side |
| 42 | [GitHub → Claude](connector-spy-test-42-github-to-claude.md) | Pairs with #11. GitHub MCP is also one of the 13 audited connectors — documentation codes are context only, live scores from the film alone |

### Messaging

| # | Teardown | Pair |
|---|---|---|
| 26 | [WhatsApp → ChatGPT-style AI assistant](connector-spy-test-26-whatsapp-to-chatgpt.md) | Pairs with #48 — same messaging store, different AI side. Test numbers/accounts the tester owns only |
| 48 | [WhatsApp → Claude-style AI assistant](connector-spy-test-48-whatsapp-to-claude.md) | Pairs with #26 |

### Microsoft 365

| # | Teardown | Pair |
|---|---|---|
| 10 | [Microsoft 365 Copilot → SharePoint](connector-spy-test-10-copilot-to-sharepoint.md) | The team-file anchor of the Microsoft 365 set. EchoLeak (CVE-2025-32711) is context only — demonstrated exploit, patched, no customer exploitation reported |
| 23 | [OneDrive → Microsoft 365 Copilot](connector-spy-test-23-onedrive-to-copilot.md) | Pairs with #44 — same file store, different AI side. The personal-file companion to #10 |
| 44 | [OneDrive → ChatGPT](connector-spy-test-44-onedrive-to-chatgpt.md) | Pairs with #23 |
| 24 | [Microsoft Teams → Microsoft 365 Copilot](connector-spy-test-24-teams-to-copilot.md) | Pairs with #45 — same conversation layer, different AI side |
| 45 | [Microsoft Teams → ChatGPT](connector-spy-test-45-teams-to-chatgpt.md) | Pairs with #24 |
| — | Outlook / Microsoft 365 Mail pair (#22, #43) | Listed under Mail above; completes the Microsoft 365 set with #10, #23/#44 and #24/#45 |

---

## Filming priority — the first 10, and why

The order is deliberate: film first where a comparison already exists, then where leaders feel the risk most, and always finish a pair before opening a new store — a pair filmed is a comparison published; a single side filmed is an anecdote.

1. **#31 Slack → Claude via MCP.** The only teardown whose integration also sits in the 13-connector documentation audit. Slack documents server-side audit logging (F4 = N in the audit), so this film is the series' first documentation-vs-live comparison: does the live test confirm what the documentation claims?
2. **#42 GitHub → Claude.** GitHub MCP is the second audited integration in the series, and its documentation was silent on audit logging (F4 = U). The film is the first evidence either way — the highest information value per minute of footage in the matrix.
3. **#1 Gmail → ChatGPT.** The series opener. Mail is the store every leader already worries about, and this is the test the whole format was designed around.
4. **#6 Gmail → Claude.** Completes the first pair on the same test mailbox and dummy-data pack as #1 — the cheapest second film in the series, and it turns #1 into a comparison.
5. **#9 Salesforce → ChatGPT.** CRM is the second store leaders ask about: the system of record for customers and pipeline, read whole.
6. **#27 Salesforce → Claude.** Completes the CRM pair in the same sandbox / developer org as #9.
7. **#15 Stripe → ChatGPT.** Money. Stripe is also the one connector of the 13 that documents prompt-injection guidance, and one of two that document server-side audit logging — context only; the live scores come from the film, in test mode.
8. **#32 Stripe → Claude.** Completes the money pair on the same test-mode account.
9. **#2 Slack → ChatGPT.** Reuses the Slack test workspace built for #31; opens the native-connector comparison against the MCP route.
10. **#5 Google Drive → Claude.** Reuses the Google test account built for #1/#6; opens the files store, the third leg of the mail–files–chat triangle leaders start with.

## The filming schedule — 16 sessions, 3 films each

Three films per session is the honest pace: each film runs four checks on camera, and the session's real work is the setup — a test account, tenant, workspace or sandbox per store, seeded with a dummy-data pack (dummy records, a private/control item the connecting account was never given, and the planted hidden instruction). Setup is built once per store and reused by both sides of the pair. At two sessions a week, the full matrix films in about eight weeks.

| Session | Films | Setup built or reused |
|---|---|---|
| 1 | #31, #2, #7 | Slack test workspace + dummy channels/DMs |
| 2 | #42, #1, #6 | GitHub test organisation; Google test account + dummy mailbox |
| 3 | #5, #30, #25 | Google test account reused — Drive dummy files, Calendar dummy events |
| 4 | #46, #3, #28 | Google account reused; Notion test workspace |
| 5 | #9, #27, #12 | Salesforce sandbox / developer org; HubSpot test portal |
| 6 | #33, #13, #34 | HubSpot portal reused; Asana test workspace |
| 7 | #15, #32, #16 | Stripe test-mode account; QuickBooks sandbox company |
| 8 | #37, #18, #39 | QuickBooks sandbox reused; Canva test account/team |
| 9 | #8, #35, #21 | Jira test project; Trello test workspace |
| 10 | #41, #20, #40 | Trello workspace reused; Airtable test bases |
| 11 | #10, #23, #24 | Microsoft 365 test tenant — SharePoint, OneDrive, Teams dummy data |
| 12 | #44, #45, #22 | Test tenant reused |
| 13 | #43, #4, #29 | Test tenant reused (Outlook); Zoom test account |
| 14 | #14, #36, #47 | Calendly test account; Zapier/Make test account |
| 15 | #19, #26, #48 | Automation account reused; WhatsApp test numbers the tester owns |
| 16 | #17, #38, #11 | Dropbox test account; GitHub test organisation reused — matrix complete |

## What each film unlocks

A teardown page today is a test design with a blank scorecard. One filmed session per teardown converts it into evidence:

- **The scorecard, filled** — the four PAARA checks scored from the film, nothing else.
- **The verdict** — CRITICAL / HIGH / MEDIUM under the series rule, stated once the scores exist.
- **The one setting to change** — the single fix the film earns the right to name.
- **The X thread goes live** — every teardown already carries its 9-post leader thread draft; filming is the only thing standing between the draft and the post.
- **The Reel and carousel publish** — the ~60-second Reel script and 7-slide carousel are written in every teardown; the film is the footage they were written for, posted natively on X and Instagram.
- **The pair comparison** — when both sides of a store are filmed, the comparison post follows: same store, two AI sides, two grants, two log stories.
- **The newsletter can cite a result** — until a teardown is filmed, The Connector Audit treats its pattern as a pattern. A filmed teardown is the first thing in the series that can be cited as a finding.

## The rules that do not change

- Test accounts, tenants, workspaces and sandboxes only; dummy data only; test numbers the tester owns only for messaging.
- No score, verdict or setting is ever filled from documentation, from the 13-connector audit, from the other side of a pair, or from memory.
- Where the film disagrees with the documentation, the disagreement is published unedited — that is the point of filming.
- This index is a plan. It will be updated as films land, and each filmed teardown's page — not this index — is where its scores live.

---

*PAARA — Privacy-Aware AI Risk Architecture · Vivek Kumar · [vivekkumar.tech](https://www.vivekkumar.tech/) · [github.com/vkktask/paara-connector-audit-kit](https://github.com/vkktask/paara-connector-audit-kit)*

# The Connector Audit — Issue #15

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #15 headline: The Shared Mailbox — connect an AI assistant to one person's account and it quietly inherits every shared and team mailbox that account can open: a whole function's correspondence, granted in one click, assessed by nobody. Plus the three identity patterns every agent runs under, and the PAARA pilot invites now out with three reviewers.**

---

## 1. The Connector Pattern — one account, every mailbox it can open

This week's pattern to check in your own estate, ahead of Connector Spy Test #22 (Outlook / Microsoft 365 Mail → ChatGPT, drafted, scores blank until filmed):

A mail connector approval reads like a personal productivity feature — "let the assistant use my email." The grant behind it typically follows the connecting account's reach, and a work account's reach is rarely one mailbox:

- Shared mailboxes ride along. Support, finance, HR, info@ — team mailboxes the connecting user was granted access to months or years ago, often for a project that ended. If the account can open the mailbox, the connector's read reach has to be assumed to include it until a filmed test proves otherwise.
- Write access hides inside a summarising story. The use case is searching and summarising mail. The grant can also cover sending as the user, replying, forwarding out of the original thread, and deleting — and, where the user holds send-as rights, sending under the shared mailbox's name, as the team.
- Every inbound email is an input channel. Mail is written by everyone — staff, customers, strangers, anyone who has the address. Any message an agent reads is text it may obey. Nobody reviewed inbound mail as an instruction channel, because nobody thought of it as one.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Outlook / Microsoft 365 Mail → ChatGPT teardown is a pre-filming draft, to be filmed on a test tenant with dummy mailboxes only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Shared Mailbox

The shared mailbox is the most honest artefact in any mail system. It exists because the work was never one person's: the support queue, the finance inbox, the HR mailbox, the team alias that outlives every reorganisation. Access to it is granted person by person, over years, usually by whoever administered the tenant at the time, and it is almost never taken back — because nobody's job is "review who can still open the team mailboxes," and because removing access feels riskier than leaving it.

Now connect an AI assistant to one of those people's accounts.

Nothing about the shared mailbox changed. No new grant was made, no new person was added, no admin approved anything. But the reach of that mailbox changed completely: everything in it — every thread, every attachment, every conversation a whole function has had with customers, employees and suppliers — is now inside the retrieval reach of an AI session, searchable and summarisable at machine speed, under a consent screen that said "email." The people whose correspondence fills that mailbox never consented to it. Most of them do not know the mailbox is connected to anything. The person who connected it probably does not know either: the consent screen names an account, not the mailboxes that account can open.

This is the general shape of connector risk, in its purest form. The approval was assessed — if it was assessed at all — against one person's mailbox: their mail, their risk, their choice. The grant executes against the account's full reach: their mail, plus every shared mailbox, plus every delegated folder, accumulated over a career. Believed reach is the use case. Actual reach is the permission graph. The gap between the two is not a vendor defect and not a user error — it is what happens when an approval process reviews the story of a connection instead of its reach.

The lesson for leaders: before any mail connector is approved, the question is not "whose account is this?" It is "what can this account open?" List the shared and delegated mailboxes first, decide — mailbox by mailbox — whether the AI grant should include them, and write the answer into the approval. If the platform cannot scope the grant below the account's full reach, that is not a detail. That is the decision.

## 3. Harness — Agent identity: the three patterns

From Training Module 5 of *Governing AI Connectors*, the open PAARA training course: every agent action runs under some identity, and in practice there are only three patterns. Most estates are running the second and third without ever having chosen them.

1. **The agent's own identity.** A dedicated, named identity per agent or agent role — never a person's name, never "the AI." Scoped to the narrowest permissions the job needs, credentials short-lived and re-issued, every action logged under the agent's own identity, and revocable in one action: a kill-switch that has been tested, not assumed. When something goes wrong, there is a single identity to switch off and a log that says what it did. This is the only pattern where "the agent did it" is a traceable statement.
2. **A borrowed user identity.** The agent runs on a person's token or login and inherits everything that person can reach — which, per Section 2, includes every shared mailbox and delegated folder that person can open. The log, if there is one, shows the person's name. When the person changes role or leaves, the token may keep working. When the agent misbehaves, there is no agent to switch off — only a person whose access you would have to revoke to stop it. This is the most common pattern, and it is chosen by default every time a connector is approved under a user's account.
3. **A shared service account.** One standing account, used by several agents, automations and often several teams, with long-lived credentials nobody wants to rotate because nobody knows everything that depends on them. Actions under it are attributable to no one agent and no one person. It cannot be killed without breaking everything else that shares it — so it never is. The shared service account is the borrowed identity with the accountability removed and the blast radius widened.

The module's test is a demonstration, not a document: give a test agent its own identity, scope it, run one small reversible task on dummy data, then revoke the identity and ask the agent to repeat the task. Record the failure — the exact error, the time it took revocation to bite, and the log entry under the agent's own name. If revocation takes hours to propagate, or the agent can still act afterwards, that delay is the finding. A one-page policy per agent role — name, identity, owner, scopes with expiry, credential lifetime, which irreversible actions (send, delete, pay, deploy) need a human, kill-switch owner and last-tested date, log location, review date — is the worksheet in Module 5. One page, because if it does not fit on one page, it will not be read.

## 4. Regulator / Industry-Body Update — PAARA pilot invites: sent, replies awaited

This week's update is from this newsletter's own workbench, reported at its exact status — because the difference between "invited" and "adopted" is the whole point of this section.

On 16 November 2026, PAARA pilot invitation emails were sent to three practitioners, inviting each to pilot the PAARA Connector Audit Kit — to run the method against connectors in their own world and report what holds up and what does not:

- **Anas Mohiuddin Syed** — author of the IETF MCP security draft to which a review note was also sent the same day.
- **Vineeth Sai Narajala** — OWASP GenAI, at vineeth.sai@owasp.org.
- **Ken Huang** — CSA AI Controls Matrix (AICM) co-chair.

That is the complete, current status: **invites sent on 16 November 2026; replies awaited.** No pilot has been confirmed, no results are in, and no adoption — by these reviewers, their organisations, or anyone else — is claimed here or anywhere else in this newsletter. A pilot invite is an email. It becomes evidence only when someone runs the kit and says, in their own words, what happened — and if that happens, this newsletter will report it with the same precision, including if the verdict is that the method does not hold up.

Why report an unanswered email at all? Because frameworks do not spread by announcement; they spread when independent people test them and talk about the test. The invitations are the start of that, and the honest status of a start is "started." Leaders reading vendor claims of "adoption" and "endorsement" should ask for exactly this level of detail — who, when, in what form, and what came back — and treat anything vaguer as marketing.

## 5. The Monday Fix — list what the account can open, before you connect it

Thirty minutes, this Monday:

1. Pick the mailboxes and accounts your AI connectors are already connected to — the Monday inventory from Issue #8. For each connecting account, answer one question: what else can this account open? Every shared mailbox, every delegated folder, every send-as right. If nobody can list them, that is the finding.
2. Decide mailbox by mailbox. For each shared or team mailbox on the list, write down — in the approval record — whether the AI grant is intended to include it, and who decided. A shared mailbox holds other people's correspondence; "it came with the account" is not a decision.
3. Where the platform lets you scope below the account's full reach, scope it: the connector gets the mailboxes the use case names, not the mailboxes the account happens to hold. Where it does not, record that as the residual risk with a named owner — the DPIA move from Issue #14.
4. Set the review trigger: shared-mailbox access changes — a grant added, a person joining a team mailbox — re-open the connector approval, the same as the vendor-update trigger from Issue #14. Access to shared mailboxes changes quietly and often; the approval has to hear about it.

You cannot scope a grant you have not mapped. List what the account can open, decide mailbox by mailbox, and the shared mailbox stops being the inheritance nobody approved.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

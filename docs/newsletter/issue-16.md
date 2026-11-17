# The Connector Audit — Issue #16

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #16 headline: The Leaver's Token — the account gets disabled on the last day, but the connector grants, the refresh tokens and the live sessions that person created can outlive the account: access nobody owns, held by nobody, still working. Plus the offboarding list for an agent, and an open door at the Cloud Security Alliance.**

---

## 1. The Connector Pattern — the grant that survives the account

This week's pattern to check in your own estate:

When someone leaves, the standard leaver process disables the account. What it usually does not touch is everything the account *created* while it was alive:

- Connector grants ride on. An OAuth grant the leaver approved — "let this AI tool read my mail / files / CRM" — is a standing permission, not a session. Disabling the login does not automatically revoke every grant, token and connected app registered under that identity, and in many estates nobody has a list of them to check.
- Sessions outlive passwords. A password reset does not kill existing sessions, and a disabled account does not necessarily end every refresh token already issued. The door is locked; copies of the key are still in circulation.
- Agent identities inherit the problem. An agent or automation the leaver set up under their account — or under a shared account they administered — keeps running on schedule after they have gone: reading, summarising, sometimes writing, owned by a person who no longer works there, reviewed by nobody.

That is a pattern, not a finding about a named product. No vendor score is published here. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Leaver's Token

Issue #2 of this newsletter was about the immortal grant: a connector approval that never expires, quietly keeping its reach for as long as nobody revokes it. The leaver's token is its close relative, and it is worth separating, because the immortal grant is a *design* problem — the grant was built without an expiry — while the leaver's token is a *process* problem: the grant may be perfectly reasonable, but the process that should have ended it never fires.

Every organisation has an offboarding checklist, and it is usually good at the visible things: laptop back, badge back, account disabled, group memberships removed. The checklist was written for a world where access meant logging in. A person who cannot log in cannot reach anything — that was the assumption, and for a long time it was true.

Connector access breaks the assumption in a specific way. The grant is not the person's login; it is a token the person *caused to be issued*, held by a third-party app or an agent, refreshed silently in the background, and exercised by software — not by the leaver typing a password. Disabling the account stops the human. It does not, by itself, walk the estate asking "what did this identity authorise, and is that authorisation still live?" In many tenants, some grants die with the account and some do not, and the difference depends on the platform, the grant type and how the app was registered — which is precisely why it has to be checked, grant by grant, rather than assumed either way.

The sharpest version is the agent the leaver built. A connector automation set up under a departing engineer's account — a scheduled summariser, a sync, an agent with its own workflow — does not know its owner has left. It keeps its timetable. Its outputs keep arriving in channels whose members assume a current employee is behind them. When it breaks, nobody owns the fix; when it leaks, nobody owns the incident. The leaver is gone, the manager has changed, and the token is still working.

The lesson for leaders: offboarding is no longer an account event, it is a *grant* event. The leaver checklist needs a connector line: every grant, token, connected app, live session and agent this identity created or owns — revoked, transferred to a named current owner, or explicitly kept with a reason and a review date. If your process cannot produce that list for the last person who left, run the test in Section 5 on the next one.

## 3. Harness — Offboarding an agent: the revoke list

From the Go-Live Canvas & Resilience Runbook: an agent that was governed going live needs the same discipline coming off. Onboarding gave the agent an identity, scopes, an owner and a kill switch; offboarding is where each of those is closed out, in an order that stops access first and tidies up second.

**The revoke list — run it in this order:**

1. **Disable the agent's identity.** The agent's own named identity is switched off first, so nothing new can authenticate as the agent while the rest of the list runs. (This is why the identity pattern from Issue #15 matters: an agent running on a borrowed user identity has no identity of its own to disable — offboarding it means revoking a person's access, which is why borrowed identities linger.)
2. **Revoke the connector tokens.** Every OAuth grant and refresh token the agent holds, per connector, revoked at the provider — not just deleted from your own registry. Then confirm: ask the agent, or the app, to act, and record the failure. A revocation that has not been tested is a hope.
3. **Disable the connector apps.** The app registrations and connected-app entries themselves are disabled or removed, so a stray token or a re-issued credential has nothing to connect to.
4. **Confirm the sessions are dead.** Check active sessions for the agent's identity and the owning user's identity, and end the ones tied to the agent. A password reset alone does not do this.
5. **Transfer or close what it owned.** Scheduled jobs, automations, shared resources and outputs the agent produced: each gets a named current owner, or is switched off. Nothing stays owned by the departed identity.
6. **Keep the log, close the file.** The agent's action log is retained per your retention rules — offboarding ends access, not evidence — and the agent's one-page record (identity, owner, scopes, kill-switch test date, from Training Module 5) is marked closed with the date and the name of the person who ran this list.

Time it, the way the kill-switch drill from Issue #10 is timed. If offboarding an agent takes a meeting to organise, the agent is effectively un-offboardable at incident speed — and an agent you cannot switch off on a Friday afternoon is an agent you do not fully control on any other day either.

## 4. Regulator / Industry-Body Update — CSA working groups: an open, rolling route in

This week's update is a route, not a result — reported at its exact status.

The industry-bodies scan published with this newsletter's work on 16 November 2026 checked where a practitioner can contribute to AI governance work in the open, and ranked the **Cloud Security Alliance's AI Controls Matrix (AICM) and AI Agent Risk Management (AARM) working groups** second of eleven: **virtual, rolling intake, free to join** — working groups you apply to and contribute to, rather than conferences you wait a year to speak at.

That is the complete, current status: **an open route, identified and verified as open on 16 November 2026.** No membership is claimed here — joining, attending and contributing are steps still to be taken, and this newsletter will report them only when they have happened, at the same precision as the PAARA pilot invites in Issue #15 (sent 16 November 2026, replies awaited, no adoption claimed).

Why flag an un-joined working group at all? Because this is where connector governance stops being one author's framework. The AICM is a controls matrix — the place where a check like "does the connector document prompt-injection defence" either becomes a control other people use, or stays a blog post. Leaders evaluating any framework, this one included, should ask where its ideas are being tested in rooms the author does not control. A working group with rolling, free, virtual intake is the lowest-friction such room there is — for PAARA, and for any practitioner reading this with a method of their own to stress-test.

## 5. The Monday Fix — add the connector line to the leaver checklist

Thirty minutes, this Monday:

1. Take the last person who left your team. Produce — from your identity provider, your connected-apps list and your AI tools' admin views — every connector grant, connected app, live session and agent or automation registered under or owned by their identity. If the list cannot be produced, that is the finding, and it goes to the top of the list.
2. For each item on the list, one of three decisions, in writing: **revoked** (and tested — try to use it, record the failure), **transferred** to a named current owner with a review date, or **kept** with a reason and an expiry. "Still running, owner unknown" is not a fourth option.
3. Add the connector line to the leaver checklist itself, next to "disable account": *grants revoked, sessions ended, agents offboarded or transferred — name and date.* Use the revoke list in Section 3 as the template; it is the same list whether the identity belonged to a person or an agent.
4. Set the trigger going forward: no leaver process closes until the connector line is signed. Account disabled is step one of offboarding now, not the whole of it.

You cannot revoke a grant you have not listed. Add the connector line, and the next leaver's token dies on the last day — with the account, the way everyone already assumes it does.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

# The Connector Audit — Issue #10

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #10 headline: The Kill-Switch Drill — if taking the keys back takes a meeting, you don't have a kill switch, you have a committee. Plus the three failure drills from the Go-Live Runbook, and a timed drill you can run before your next go-live.**

---

## 1. The Connector Pattern — the file store that hands an AI your documents, and the share links that decide who else can read them

This week's pattern to check in your own estate, ahead of Connector Spy Test #17 (Dropbox → ChatGPT, drafted, scores blank until filmed):

A file-store connector is usually approved for one narrow job — "let the assistant find and summarise documents." The grant behind it reaches a very different asset. The pattern to look for:

- A file store is where an organisation keeps what never made it into a system of record: contracts, board papers, HR letters, the spreadsheet with the salary bands in it. Approving the connector approves reach into all of it, not just the document somebody asked about — and folders other people shared in come along with your own.
- The same connection that reads files can often write: upload, edit, move, delete. And one write matters more than the rest — changing who a share link reaches. Widening a link is not a file operation. It is a disclosure decision, made by software, under a person's identity.
- Documents are an input channel, not just records. Contracts, packs and notes are written by staff, counterparties and other systems — anything an agent reads in them, it may also obey.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Dropbox → ChatGPT teardown is a pre-filming draft, to be filmed on a test account with dummy files only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Kill-Switch Drill

From the Go-Live Canvas & Resilience Runbook — the drill every connected workflow runs, timed, before go-live:

Something has gone wrong. Not hypothetically — the scenario on the table is a poisoned document steering the agent's outputs, mid-incident, while the connector's permissions shift underneath it. The question is not whether your team knows, in principle, how to take the agent's access away. The question is how long it takes, with a stopwatch running, outside business hours, when the person who set the connector up is not in the room.

The sequence is four moves, in order:

1. **Disable the agent's identity.** The dedicated non-human identity the agent authenticates as — disabled, not just disconnected.
2. **Revoke the connector's tokens and sessions.** Every token and live session the grant issued — revoked, so a cached credential cannot quietly re-open the door.
3. **Disable the connector app.** The app / integration registration itself — disabled, so nothing can mint a fresh token while you work.
4. **Confirm the sessions are dead.** No live sessions, no new actions appearing in the logs. Verification, not assumption — then notify the business owner and affected teams.

In the runbook's worked example — Bellhaven Mutual, a hypothetical composite — the drill ran **11 minutes end-to-end**, and was documented as a go-live condition with a named owner. Eleven minutes is what "we have a kill switch" actually means. Anything that requires convening the people who approved the connector is not a kill switch; it is an incident process with extra steps, and the agent keeps its keys for the whole meeting.

The drill also exposes the gaps nothing else finds. If step 1 has no answer because the agent borrows a human's login, that is a finding. If step 2 cannot be done because nobody knows where the tokens live, that is a finding. If step 4 cannot be confirmed because the reads were never logged, that is the finding this whole series keeps returning to. Run it before go-live, when the findings are cheap.

## 3. Harness — the failure drills (Go-Live Runbook, B6)

From the Go-Live Canvas & Resilience Runbook: three drills, run before go-live. The kill-switch drill is the first; the other two answer the questions an incident will ask anyway — what happens when the connector disappears, and what happens when the agent has already acted.

**Drill 1 — Take the keys back (compromise).** Run the sequence with a stopwatch, outside business hours, before go-live. Target: minutes, not meetings.

- [ ] 1 · Disable the agent's identity
- [ ] 2 · Revoke the connector's tokens and sessions
- [ ] 3 · Disable the connector app / integration registration
- [ ] 4 · Verify: no live sessions, no new actions in the logs
- [ ] 5 · Notify the business owner and affected teams

**Drill 2 — The connector is gone for 72 hours (outage).** The vendor is down, or you pulled the keys yourself. Answer in writing:

- [ ] How does the business process run manually?
- [ ] Who staffs it?
- [ ] Who is notified, and by whom, within the first hour?
- [ ] What data or actions queue up, and how are they reconciled when service returns?
- [ ] At what point does degraded operation become a business incident, and who declares it?

**Drill 3 — Roll it back.** Pick one real action the agent performed (or will perform in pilot). Reverse it. Record what it took:

- [ ] The action reversed
- [ ] The steps and time required
- [ ] What could NOT be reversed — this list defines your "irreversible" rung on the action ladder, and irreversible actions are human-only by default

A drill that has never been run is a hope with a heading. Each drill ends in an artifact — a time, a written answer, a reversal record — or it did not happen.

## 4. Regulator / Industry-Body Update — Japan's PPC, the APPI, and a comment filed through e-Gov

On 16 November 2026, Vivek Kumar submitted a comment to Japan's Personal Information Protection Commission (PPC) on its APPI guidance, through Japan's e-Gov public-comment portal. The submission is on the record: **case 240000133, receipt 240000133169060227**.

Why this one belongs in a connector newsletter: the APPI governs how personal information is handled and shared with third parties — and an AI connector is, in practice, a standing third-party sharing arrangement that most inventories never record. When an employee connects an AI assistant to a file store, a mailbox or a CRM, personal information starts flowing to a provider under a grant nobody assessed, in a direction no transfer register describes. The compliance question is the same one this series asks in every issue, wearing a Japanese regulator's clothes: can you name the connections actually granted, what each one can reach, and what is logged — or only the systems on the architecture diagram?

Filing through e-Gov, with a case number and a receipt, matters for a second reason. A comment on the record can be checked, cited and held to account — by the regulator, and by readers. That is the standard this newsletter applies to its own claims, including the blank scores in every teardown until the film exists.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — run the kill-switch drill, timed

Thirty minutes, this Monday — plus the drill itself, scheduled before your next go-live:

1. Pick the one AI connector whose compromise would hurt most — the widest reach, the most sensitive data, the write access nobody talks about.
2. Write down the four moves for that connector, by name, for your stack: which identity gets disabled, where its tokens and sessions are revoked, where the app registration is disabled, and where you verify no live sessions and no new log entries remain. If any move has no named console, screen or owner, you have found this week's gap.
3. Put the drill in the calendar — outside business hours, stopwatch running, the connector's installer not required to be present. Record the time, end to end.
4. File the result where the go-live decision lives: the time, the gaps, and an owner and date for each gap. A drill time with no record is a story; a recorded time is a control.

If taking the keys back takes a meeting, you don't have a kill switch — you have a committee. Time it, and find out which one you have.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

# The Connector Audit — Issue #34

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #34 headline: The Board Nobody Owns — the project ended, the team moved on, the owner left, and the board is still there: still shared, still holding the record, and now reachable by every connector its last members ever approved. Plus workspace and tenant hygiene for agents — the owner-of-record rule, orphan cleanup and the quarterly sweep — and a chapter abstract on AI governance, submitted to a Springer edited volume: submitted, not accepted.**

---

## 1. The Connector Pattern — the board store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #21 tested Trello → ChatGPT. Teardown #41 tests **Trello → Claude**: the same board store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same boards.

- The read reach is the work as the team actually recorded it. A Trello-style account rarely holds one tidy project board. It holds every board ever spun up — delivery boards, hiring boards, incident boards, personal boards — including boards for projects that closed years ago, still holding their full card history: descriptions, comments, checklists, attachments. Tested in Teardown #41 on a **test workspace with dummy boards only**: the boards named in the request, boards nobody pointed the assistant at, account-wide search, a **private board** the connecting user could see but was never directed to — and a **control card** held on a board in a separate workspace that was never connected or shared. The filmed question is whether the reach is the one board in the conversation, or every board the account has accumulated.
- The write reach includes the writes that change what the record says. Create and move cards — a move to Done certifies work as finished — comment, change members, and **delete a card**, which takes the card and its activity trail out of the record. Each write is filmed in Teardown #41 with the approval step, or its absence, on camera.
- There is no dataset shortcut for this one. Trello → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #21 either, because the grant, the approval surface and the log story belong to this route, not to the store. Teardown #41's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #41 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Board Nobody Owns

Every workspace accumulates boards the way a house accumulates drawers. A project starts, a board is created in an afternoon, the work moves onto it because it is faster than the official system. Then the project ends. The team disperses. The person who created the board changes roles, or leaves. And the board stays — because closing it was nobody's job, deleting it felt risky, and it costs nothing to leave it exactly where it was.

Watch what an orphaned board actually holds, because it is never nothing. It holds the project's real history — not the sanitised version in the closure report, but the cards as they were written at the time: the customer problem described candidly, the contractor's rate on a card comment, the restructure discussed a month before it was announced, the incident timeline nobody edited afterwards. It holds its sharing list, too: the members added along the way, the external guests invited for one meeting and never removed, the link settings chosen in a hurry. And it holds its automations and connections — the integrations approved when the board was alive, still authorised, still able to act, attached to a store nobody has opened in a year.

Issue #16 told the individual version of this story: the leaver's token, the grants and sessions that outlive the account that created them. The orphaned board is the collective version. The leaver's token is one person's leftover access; the orphaned board is a whole project's leftover store, with everyone's leftover access still attached to it. Nobody owns it, so nobody reviews it. Nobody reviews it, so nobody notices when its sharing widens, its data ages past its retention date, or its membership quietly stops matching any team that exists.

Now add the connector — and, in this issue's pattern, a second one. An AI assistant connected to the live project board goes through whatever approval the project had. The same assistant, granted account-wide reach, reaches the orphaned boards on the same grant — the closed project's candid history, summarisable on request, by whoever holds the connection. The grant does not distinguish between the board the team works on today and the board nobody has owned since 2024. The approval did not either, because the inventory it was approved against listed the live boards and stopped there.

Teardown #41 tests this pattern on Trello → Claude: board and card read reach with a private board and a control card, write actions — create, move, comment, member changes, delete — a hidden instruction planted in a dummy card description, and the card-activity trail behind it all. It is filmed on a test workspace with dummy boards only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result: list your own estate's boards and ask which of them have no living owner, what they still hold, and which AI tools can reach them today. That answer is the finding, and it is already available to you.

The lesson for leaders: a workspace is not cleaned by the projects ending. It is cleaned by an owner-of-record rule and a sweep — and until both exist, every connector grant you approve is a grant over the orphans too. Section 3 gives the hygiene rule.

## 3. Harness — Workspace and tenant hygiene for agents: the owner-of-record rule, orphan cleanup, and the quarterly sweep

Connectors inherit the tenant they are connected to — every board, base, channel and folder in it, live and orphaned alike. Hygiene is therefore not housekeeping that sits beside connector governance; it is the thing that decides what a grant actually covers. Three rules, applied to the workspace or tenant the agent can reach:

**Rule 1 — Every store has an owner of record, and the record is checked, not assumed.** Each board, workspace and shared store in the connector's reach carries a named owner — a person, in post today — recorded in the store itself or in the connector's approval record. Ownership means three duties: know what the store holds, review who can reach it, and close it when its purpose ends. When the owner changes roles or leaves, ownership transfers by name at offboarding — Issue #16's revoke list gains a line: the stores this person owned, and who owns them now. A store whose owner of record has left and not been replaced is an orphan by definition, whatever its activity feed says.

**Rule 2 — Orphans are closed on a clock, not on a hunch.** A store with no owner of record, no activity in the agreed window, or a purpose that has ended gets a disposition, in writing: transfer to a named owner who accepts it, archive it read-only under a retention date, or delete it with its sharing list recorded first. What it does not get is another quarter of silence. Until disposition, an orphan is treated at the highest caution: connector reach into it is suspended or scoped out where the platform allows, because there is no owner who can say what the data is, who should see it, or whether an agent should be reading it at all. Where the platform cannot scope it out, the approval record names that gap — the same discipline as Issue #33's classification ceiling: the connector's effective reach includes the orphans, and the record says so.

**Rule 3 — The sweep is quarterly, and it re-runs the inventory, not the memory.** Once a quarter, export the workspace's stores and sharing lists fresh — boards, members, external guests, link settings, connected apps — and diff against last quarter's file, the same baseline-and-diff discipline as Issue #27's change control. The sweep asks four questions: which stores are new, which lost their owner, which gained members or guests nobody can explain, and which connectors' reach grew because the tenant grew. Each answer gets an owner and a date. As Issue #25 established: evidence or it didn't happen — the sweep's export and diff are the evidence, filed with the approval records they amend.

**The agent-specific line.** Run the sweep before approving a new connector, not after: the grant is priced against the tenant as it stands that day, orphans included. A hygiene pass that removes or archives the dead stores first is the cheapest scope reduction available — it narrows what every future grant can reach, on every AI side, without touching a single connector setting.

## 4. Regulator / Industry-Body Update — Springer edited volume: a chapter abstract submitted, not accepted

This week's update is a submission, reported at exactly that status.

**A chapter abstract was submitted on 16 November 2026 to the Springer edited volume "AI, Governance, and Sustainable Development".** A decision is expected on **15 December 2026**; if the chapter is accepted, the full chapter would be due **15 February 2027**. The submission asked the editors to confirm the contract, series and ISBN, the peer-review process and any fees in writing before any full chapter is written.

The status, stated at its actual precision: **submitted, and nothing more.** No acceptance is claimed, implied, or expected in print before a decision exists. This newsletter has made the same distinction for conference papers, talks and workshops throughout this series, and an edited-volume chapter awaiting an editor's decision gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because an edited academic volume is where practitioner method gets checked by editors and reviewers with no stake in it, and placed on the record beside the scholarly literature the field cites. Submitting the abstract — with the contract, peer-review and fee questions asked in writing up front — is the deliberate choice to have both the work and the terms examined before anything further is committed.

## 5. The Monday Fix — give one orphaned board an owner, or a closing date

Forty-five minutes, this Monday — one workspace, one orphan list, one disposition round:

1. Pick **one workspace a connector can already reach** — the board store from this issue is the natural start, because it is the one most likely to hold closed projects. Export or list every board in it, with its owner of record, its last activity, and its sharing list, from the workspace's own admin views, not from memory. Any board whose owner has left, changed roles, or cannot be named is an orphan — record it as one.
2. **Give each orphan a disposition, in writing, with a date:** a named owner who accepts it, archive read-only under a retention date, or delete with the sharing list recorded first. No fourth option of leaving it for another quarter. Where an orphan holds data nobody can classify, it takes the cautious route — archived or deleted, not transferred on a guess.
3. **Scope the connectors against the cleaned tenant:** for each connector with reach into the workspace, record whether the orphans sit inside its grant, scope them out where the platform allows, and where it does not, write the gap into the approval record with an owner — instead of leaving the grant's real coverage unstated.
4. **File the sweep** — the board list, owners, dispositions and dates — in the workspace's approval records, and set the quarterly date for the next one now. Next quarter's sweep starts from this file, and its first check is whether any store lost its owner since.

Score the connector before you trust it — and own the tenant before you scope the grant, because a connector approved against the live boards alone is also approved, silently, over every board nobody owns. This Monday, the orphan list is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

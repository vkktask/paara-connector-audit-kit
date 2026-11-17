# The Connector Audit — Issue #35

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #35 headline: The Merge Nobody Reviewed — an agent connected to your code store can open the pull request, approve it, and merge it, and the review gate your policy describes never actually happened: the approval on the record is real, the reviewer was not. Plus code and change gates for agents — branch protection, required reviewers, agent identity in the audit log — and a chapter abstract on AI for future societies, submitted to the Aula Fellowship volume: submitted, not accepted.**

---

## 1. The Connector Pattern — the code store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #11 tested GitHub / GitHub Copilot → ChatGPT. Teardown #42 tests **GitHub → Claude**: the same code store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same repositories.

- The read reach is the codebase as the team actually built it. A GitHub-style organisation rarely holds one tidy project repo. It holds every repo ever created — application code, infrastructure-as-code, internal tools, archived experiments — including the candid material people put in code-adjacent places because a repo feels technical and safe: the incident timeline in an issue, the credentials discussion in a PR comment, the customer name in a test fixture. Tested in Teardown #42 on a **test organisation with dummy repositories only**: the repos named in the request, repos nobody pointed the assistant at, organisation-wide search, a **private repo** the connecting user could see but was never directed to — and a **control repo** held in a separate organisation that was never connected or shared. The filmed question is whether the reach is the one repo in the conversation, or every repo the organisation has accumulated.
- The write reach includes the writes that change what ships. Open issues, comment on pull requests, open pull requests — and the two writes this issue is about: **approve a pull request**, which satisfies a review gate another human was meant to perform, and **merge**, which puts code on the path to production. Each write is filmed in Teardown #42 with the approval step, or its absence, on camera.
- There is a dataset context for this one, stated at its exact precision. GitHub MCP **is** one of the 13 connectors in the published documentation audit (documentation retrieved 9 Nov 2026; F1–F7 coded, with the logging factor F4 coded U — the public documentation was silent on audit logging). Those codes score what the documentation says. They are context only: Teardown #42's scorecard is blank until the film, nothing carries over from Teardown #11 either, and where the film and the documentation disagree, both get published.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #42 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Merge Nobody Reviewed

Every engineering organisation has a sentence in its policy that sounds like this: no code reaches production without review by a second engineer. The sentence exists because the review is not bureaucracy — it is the moment a second mind checks the change, the moment accountability splits between the person who wrote the code and the person who let it in. The pull request is where that sentence lives. The approve button is the signature.

Now watch what a connector does to that sentence. An AI assistant connected to the code store with write reach can open the pull request. It can comment on it. And — this is the step leaders consistently miss — it can **approve** it, and it can **merge** it. The approval is recorded. The merge is recorded. The branch protection rule that required one approving review shows satisfied. Every artefact the policy asks for exists. The only thing missing is the event the policy was actually describing: a second human being reading the change and deciding it should ship.

The record does not show that gap, because the record was designed for human actors. The approval sits under a person's identity — the person whose account the connector acts through. Months later, in an incident review or an audit, that person is asked why they approved a change they never saw. The honest answer — an agent approved it in a session I started for something else — is not in the log. It is in nobody's log, unless the platform separates agent actions from human ones, which is a question almost nobody asked at approval time. Issue #28 made this point about tickets: the agent certifying its own work. Code is the same shape with higher stakes, because the certified artefact does not sit in a queue — it ships.

The quieter version of the same failure needs no malice at all. The agent is asked to tidy up a repo. It opens a sensible PR. A tired human approves it without reading, because the agent's PRs are usually fine — the review gate performed as a reflex, the signature real, the review not. Agent temperament, Issue #7's lesson, is not a control; neither is a human who has learned to trust the agent's output. Between the agent that approves its own work and the human who approves it unread, the gate fails the same way: the artefact exists, the scrutiny does not.

Teardown #42 tests this pattern on GitHub → Claude: repo read reach with private repos and a control repo, write actions — issues, comments, PRs, approval, merge — a hidden instruction planted in a dummy issue and a dummy README, and the audit-log trail behind it all. It is filmed on a test organisation with dummy repos only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result: open your own estate's recent merges and ask how many approvals were given by a human who read the diff, how many were given by an agent session, and whether your log can tell the difference. That answer is the finding, and it is already available to you.

The lesson for leaders: a review gate is a person reading, not a status turning green. If an agent can produce the status, the gate has to be rebuilt around the agent — Section 3 gives the rebuild.

## 3. Harness — Code and change gates for agents: branch protection, required reviewers, agent identity in the audit log

Issue #4 used the GitHub pattern to make the scope point: a connector approved to explain one repo quietly holding reach across all of them, growing one reasonable request at a time. This section is the write-side companion — the gates that have to exist when the connector can not only see the code store but change what ships from it. Three gates, applied to every repo an agent can reach:

**Gate 1 — Branch protection that counts the agent as an author, never as a reviewer.** The protected branch requires pull requests and at least one approving review — and the configuration is checked for the agent-shaped holes: the identity the connector acts through cannot approve a pull request it opened, cannot approve its own session's work under a borrowed human identity without that being visible, and cannot merge around the requirement (no direct pushes, no admin bypass left switched on from an old incident). Where the platform cannot separate the agent's approval from a human's, the rule is written the other way: agent-opened PRs require a named human approver from a list, full stop. The test is Issue #25's evidence pair: a legitimate human-approved change goes through, **and** an agent approval on an agent-opened PR is blocked — both halves filmed or logged, not asserted.

**Gate 2 — Required reviewers are named people, and the requirement survives the agent.** Code-owner rules route sensitive paths — infrastructure, auth, payments, migrations — to named owners. The agent changes none of that: a connector session touching a protected path triggers the same owner review as a junior engineer's first PR, and the review request goes to the owner, not to the session that opened the PR. Reviewer fatigue is treated as a gate failure, not a personality trait: if agent-opened PRs arrive faster than owners can read them, the answer is a queue and a rate, not a quieter standard. A gate that everyone routes around under time pressure is Issue #27's change-control lesson applied to code — pin the baseline, and treat every bypass as a change that needs its own approval.

**Gate 3 — The audit log names the agent, or the approval record says it cannot.** After any agent session, the log must be able to answer: which actions were taken by the connector, under which grant, in which session — separately from the human's own actions under the same account. Where the platform's log does separate them, that separation is verified in a drill, the way Issue #10 drills the kill switch: run a session, then rebuild it from the log alone, in the room, before go-live. Where the log cannot separate them — where an agent's approval is indistinguishable from the person's — the approval record states that gap in writing, and the connector's write tier drops accordingly: an agent whose approvals cannot be told apart from a human's does not get approval rights. This is also where the documentation earns a check: for GitHub MCP, the published audit coded the logging factor U, silent — so the estate's own drill, not the vendor's page, is the evidence.

**The agent-specific line.** None of these gates is a setting on the connector. They live in the repo platform and the approval record — which is precisely why they get missed: the connector review looked at scopes, and the review gate lived somewhere else. Price the write reach against the gates as they actually stand, the way Issue #34 prices a grant against the tenant as it actually stands.

## 4. Regulator / Industry-Body Update — Aula Fellowship "AI for Future Societies" Vol I: a chapter abstract submitted, not accepted

This week's update is a submission, reported at exactly that status.

**A chapter abstract was submitted on 16 November 2026 to the Aula Fellowship edited volume "AI for Future Societies" Vol I.** As with the companion submission that week, the cover email asked the editors to confirm the contract, series and ISBN, the peer-review process and any fees in writing before any full chapter is written. No decision date is stated here, because none has been given to rely on.

The status, stated at its actual precision: **submitted, and nothing more.** No acceptance is claimed, implied, or expected in print before a decision exists. This newsletter has made the same distinction for conference papers, talks, workshops and an edited-volume chapter throughout this series, and a fellowship volume awaiting its editors' decision gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room? Because a fellowship volume on AI and future societies is where practitioner method gets read beside academic and policy work — the audience that writes the frameworks practitioners later have to implement. Submitting the abstract, with the contract, peer-review and fee questions asked in writing up front, is the deliberate choice to have both the work and the terms examined before anything further is committed.

## 5. The Monday Fix — make one repo's review gate agent-proof

Forty-five minutes, this Monday — one repository a connector can already reach, one gate rebuilt:

1. Pick **one repository an AI connector can write to** — the one closest to production is the honest start. Pull its branch-protection settings and its last month of merges, from the platform's own views, not from memory. For each merge, record who opened the PR and who approved it — and mark every approval you cannot attribute to a human who plausibly read the diff, including any given through a connector session.
2. **Close the self-approval path, in the settings, today:** the identity the connector acts through cannot approve a PR it opened; agent-opened PRs on this repo require a named human approver; direct pushes and stale admin bypasses on the protected branch are off. Film or screenshot the settings before and after — Issue #25's rule: evidence or it didn't happen.
3. **Test the log, don't trust it:** run or reconstruct one past connector session against this repo and rebuild it from the audit log alone — reads, writes, approvals, merges, identities. Whatever the log cannot attribute to the agent, write into the connector's approval record as a named gap with an owner, and drop the connector's approval rights on this repo until the gap closes.
4. **File the gate** — the protection settings, the approver rule, the log test and its gaps — in the repo's connector approval record, and set the date to re-run the merge sample next quarter. Next quarter's check starts from this file, and its first question is whether any approval since has come from a session instead of a reader.

Score the connector before you trust it — and guard the merge like the signature it is, because a review gate an agent can satisfy by itself is not a gate; it is a status. This Monday, the approval list is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

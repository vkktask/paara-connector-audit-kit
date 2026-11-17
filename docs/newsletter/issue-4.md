# The Connector Audit — Issue #4

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #4 headline: Silent Scope Creep — the connector that quietly grew.**

---

## 1. The Connector Pattern — the code assistant that can see more repos than the job needs

This week's pattern to check in your own estate, ahead of Connector Spy Test #11 (GitHub / GitHub Copilot → ChatGPT, drafted, scores blank until filmed):

A code or repository connector is usually approved for one narrow job — "explain this repo before the review." The reach behind it is rarely that narrow. The pattern to look for:

- The connected app can read across the repositories the signed-in user can open — including private repos — not just the one repo in the prompt.
- The write side is broader than the read side suggests: opening issues, commenting on pull requests, and proposing changes are actions taken as the user, under the user's name.
- Nobody wrote down which repos were in scope, so nobody can say afterwards whether a retrieval or a comment was in scope or out of it.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the GitHub → ChatGPT teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test account with dummy repos fills it in. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — Silent Scope Creep

From the field, anonymised:

Nobody expands a connector's access in one big decision. It grows one reasonable request at a time. A second repo for the new project. Read access to the shared library. One more scope because a feature would not work without it. Each step is small, each step is approved by someone acting in good faith — and no step ever triggers a fresh review, because no single step looks like a change.

A year later the connector holds reach nobody ever chose as a whole. The original approval still says the narrow job. The scopes say something else. If you compare the two documents — the approval and the current grant — they no longer describe the same connector.

The lesson is not "never widen access." It is: scope changes are access decisions, and an access decision that never gets reviewed was never really made. It just accumulated.

## 3. Harness Gate — G4: anomalies noticed

One gate from the AI Agent Harness Evaluation Playbook, in plain English:

**Someone — or something — notices when the agent behaves strangely, and a human hears about it.**

An agent that reads ten times its usual volume at 3 a.m., touches a repo it has never touched, or starts failing in a new way should not be a discovery made weeks later in a log review. Prove it before go-live: run a deliberate anomaly — an unusual access pattern, an out-of-hours burst, a first-time reach into a sensitive area — and time how long it takes for a named human to be alerted and to act. No alert is a fail. An alert nobody owns is a fail. A timely alert to a named owner who can stop the agent is the only pass. Fail this gate and no score elsewhere rescues the deployment — that is the whole point of a gate.

## 4. Regulator / Industry-Body Update — Australia DEWR, AI in the workplace

On 16 November 2026, Vivek Kumar submitted a comment on the Australian Department of Employment and Workplace Relations (DEWR) draft best practice guide on the adoption of AI in the workplace, through the consultation hub's online form — submission reference sbm407def0c0eafdc9e0b9ca, ahead of the consultation's closing date of 27 January 2027.

Why it belongs in a connector newsletter: workplace AI guidance is where duties about surveillance, work intensification and discrimination get written — and the connector layer is where those duties bite in practice. What an agent can reach, what scopes it holds, and what is logged when it acts are the facts a workplace guide has to be able to ask for, or its principles have no way to be checked. Practitioner comments are how that layer gets into the record at all.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — diff the grant against the approval

Thirty minutes, this Monday:

1. Pick your three broadest AI connectors. For each one, pull up two documents side by side: the original approval (what job, what data, what scopes) and the current grant (what scopes it actually holds today).
2. List every scope, repo, workspace or data source the connector can reach now that the approval never named. That list is your scope creep, in writing.
3. Anything on that list with no current business need gets removed on the spot — it can be re-granted in minutes if it turns out to be needed.
4. Set one rule from today: any scope change to a live connector goes through the same review as a new connector. No silent widening.

The connector you approved is not always the connector you are running. Diff them.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

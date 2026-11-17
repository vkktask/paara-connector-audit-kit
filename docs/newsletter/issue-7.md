# The Connector Audit — Issue #7

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #7 headline: Agent Temperament — your agent's personality is not a control. Plus the year-end gate check: all six gates, one page.**

---

## 1. The Connector Pattern — the booking page that hands an AI your visitors' names, emails and notes

This week's pattern to check in your own estate, ahead of Connector Spy Test #14 (Calendly → ChatGPT, drafted, scores blank until filmed):

A scheduling connector is usually approved for one narrow job — "tell me who's on my calendar tomorrow." The grant behind it reaches a very different asset. The pattern to look for:

- A booking page is a live list of people: every booking carries an invitee's name, their email address, and whatever they typed into the booking form — and invitees write real things in that box, including phone numbers, internal project names and the reason for the meeting.
- The same connection that reads bookings can often write them: create a booking, cancel one, move one. A cancellation is not a database edit — it sends a notice to a real person outside your organisation.
- The notes field is free text written by strangers. Anything an agent reads there, it may also obey — which makes a booking form an input channel, not just a record.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Calendly → ChatGPT teardown is a pre-filming draft, and every score in it stays blank until a filmed live test on a test account with dummy bookings fills it in. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — Agent Temperament

From the field, anonymised:

One agent asks permission constantly. Another runs fifty steps without checking in once. Same policy document, same approved workflow — completely different risk. Agents differ in how often they pause for approval, how far they will chain actions together before surfacing anything, and how literally they take an instruction they find in the data they were asked to read.

The uncomfortable part is not that temperament varies between products. It is that it varies within one product, across model updates, with no change notice that reaches the risk register. The deployment you approved in October was, behaviourally, a specific agent. The one running in December may ask less, chain more, and improvise further — under the same name, the same connector and the same scopes.

The lesson: if your control is "the agent will ask first," your control is a personality trait. Controls have to bind by design — a ceiling set in configuration, a gate that fires before execution — because temperament is a default, and defaults change. Section 3 is the year-end version of that point, for all six gates at once.

## 3. Harness Gates — the year-end checklist: all six gates, G1–G6

One gate per issue for six issues. This week, the full set from the AI Agent Harness Evaluation Playbook, as a single year-end checklist. A gate is pass/fail, proven with evidence — fail one, and no score elsewhere rescues the deployment.

- **G1 — Agentic identity.** Every agent action runs under a real, dedicated, verifiable identity, and that identity survives every hop of a multi-step task. No generic service-account soup. *Proof: one trace, the same identity at every step.*
- **G2 — Acts as the user, not above them.** On a user's behalf, the agent carries that user's entitlements — it can never surface what the requesting user could not open themselves, even through a summary. *Proof: a low-privilege probe is refused, with no indirect leak.*
- **G3 — Exactly once.** A consequential action — payment-like, filing-like, delete-like — executes exactly once under retries, failures and multi-agent fan-out. The agent verifies state before it retries. *Proof: a forced-retry test — no double execution, no silent zero.*
- **G4 — Anomalies get noticed.** Behavioural-anomaly detection exists on agent activity — bulk pulls, odd hours, scope-boundary probing — and it alerts a human, not just a log file. *Proof: a simulated bulk pull raises an alert to a named owner.*
- **G5 — External kill switch.** You can stop the agent from outside the platform — revoke its identity, its connector tokens and the connector app, in minutes — and prove all activity stopped. *Proof: a stopwatch drill, plus dead-session evidence afterwards.*
- **G6 — Consent gate on regulated data.** Disclosure of regulated data — tax, health, financial records — is blocked unless a current, disclosure-specific consent is validated before execution. *Proof: a blocked disclosure, plus the consent-check record.*

Run the list against every agent deployment you own before the year turns. Any gate you cannot prove with an artifact is, for audit purposes, a gate you do not have — whatever the policy document says.

## 4. Regulator / Industry-Body Update — NIST's adversarial ML taxonomy, and the connector layer it doesn't name yet

On 16 November 2026, Vivek Kumar sent comments on Draft NIST SP 2400-102e2026, the Adversarial Machine Learning Taxonomy, from vkktaskusa@gmail.com to SP-2400-102@nist.gov (Gmail message id 1a1e5efa114f7a44). The comment made eight asks, all aimed at one gap: the taxonomy treats adversarial ML largely as something done to models, while in agentic deployments the attacks arrive through the connector layer — the integrations that carry the model's reach into real systems.

The eight asks: (1) name the connector layer as an attack surface in its own right; (2) distinguish documented from undocumented controls when a technique depends on vendor behaviour; (3) cover connector prompt injection — instructions arriving through connected content; (4) cover tool-call hijacking; (5) cover excessive permissions and the need for write-limiting on connectors; (6) require connector audit logging as the evidence base for detecting these techniques; (7) cover transport and identity documentation for connectors; and (8) add glossary terms for the "rug pull" — a connector or MCP server changing its behaviour after approval — and the rogue MCP server.

A taxonomy is not a footnote exercise. Incident responders, auditors and insurers classify real events with these documents; a technique with no name in the taxonomy is a technique that gets recorded as something else, or not recorded at all. The connector layer is where agentic incidents will actually happen, and it needs names before it needs anything else.

No endorsement or adoption is claimed — a submitted comment is a submitted comment. It is recorded here so readers can hold the argument, not the author, to account.

## 5. The Monday Fix — set the action ceiling in configuration, not in the prompt

Thirty minutes, this Monday:

1. Pick one AI agent or connector your organisation runs, and write down its action ladder: read, draft, write, execute, irreversible. Mark the highest rung it is allowed to reach on its own.
2. Check where that ceiling actually lives. If it is a sentence in a prompt or a line in a policy document, it is temperament-dependent — move it into configuration: scopes, approval settings, tool permissions.
3. Test it: attempt the action one rung above the ceiling, in a test context, and confirm the human gate fires before execution — not after, not in a log you read next week.
4. Record the ceiling, the gate and the test result in the connector's inventory entry, with one named owner. Repeat for the next connector — one a week, and by the new year every agent you run has a ceiling you set, instead of a temperament you inherited.

Your agent's personality is not a control. Set the ceiling yourself.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

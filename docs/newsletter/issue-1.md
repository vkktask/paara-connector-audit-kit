# The Connector Audit — Issue #1

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness gate, one regulator or industry-body update, and one Monday fix — every week.

**Issue #1 headline: The Blind Path: Your Agents Are Already Connected. Can You Name Where?**

*Issue #1 · Monday 16 November 2026*

---

Most leadership teams can list their AI tools. Very few can list what those tools are connected to, with whose permissions, and where the data goes next. That gap — not the model — is where your next incident is already sitting.

Welcome to the first issue. Let me start with the question I now ask at the beginning of every review, because the answer tells me more than any policy document:

"Show me every system your AI agents can touch — and who approved each connection."

I have asked some version of that question across more than seventy reviews of AI systems and their connectors. The pattern is so consistent it stopped surprising me a long time ago. The AI tool itself was procured properly. There was a business case, a security review, sometimes a very good one. But the connectors — the plugs that let the agent read your mailbox, search your files, post into chat, query the CRM — were switched on later, one at a time, by well-meaning people solving a problem in front of them. Each one looked small. Nobody added them up.

So the agent ends up with a reach nobody chose. Not the CIO, not the CISO, not the data protection officer. It just accumulated. I call it the blind path: the route data actually travels once an agent is connected, which is rarely the route on the architecture diagram.

This newsletter exists to close that gap, one week at a time. Here is issue one.

## 1. The Connector Score — the first connector to score is the one you cannot see

Every week I will score a connector pattern against five checks. This week, the pattern is the most common one I find: **an AI assistant connected to email and files under a broad, standing grant**. Scored honestly, a typical first review looks like this:

| Check | Finding in a typical first review | Rating |
|---|---|---|
| Permission breadth | Read and write granted where the use case only ever needed read. | Fail |
| Token lifetime | Grant has no expiry and no owner who remembers creating it. | Fail |
| Data path | Nobody can say whether retrieved content is stored, indexed, or used for training by the vendor. | Watch |
| Logging | Agent actions are logged somewhere — but not in the system your security team actually monitors. | Watch |
| Revocation | It can be switched off, but only by breaking the tool for everyone, so nobody ever does. | Watch |

Two fails and three watches is not a failing organisation. It is a normal one. That is precisely the point: the risk is not negligence, it is invisibility. You cannot fix a score you have never taken. Next week we take the second check — token lifetime — apart on its own, because it deserves it.

## 2. Field Note — the connector nobody owned

A field note, generalised so no organisation is identifiable. A team had done a genuinely careful review of an AI assistant before rollout. Permissions were scoped, the vendor paperwork was in order, the launch was clean. Months later, during a routine access review for something unrelated, someone asked a simple question: why does this integration still have access to a shared drive the project stopped using?

Nobody could answer. The connector had been enabled during a pilot, by a person who had since changed roles. The pilot ended. The connector did not. It sat there, quietly valid, with standing access to material nobody was using anymore — not malicious, not exploited, just forgotten. The fix took an afternoon. Finding it took months, and it was found by accident.

I tell this story because it is the most common story I have. The dangerous connector is rarely the one you argued about in the design review. It is the one left over from the pilot.

## 3. Harness Gate — Gate 1 of 6: prove the identity before you prove the intelligence

Before any agent goes live, it should pass six harness gates. We will work through one a week in this newsletter, in order. Gate 1 is identity and least privilege, and it comes first for a reason: every later test is meaningless if you do not know who — or what — is acting.

The gate is simple to state and awkward to pass. The agent must act under its own identifiable identity, not a shared human account. Its permissions must match the job it was approved to do, and nothing else. And you must be able to show, from logs, which actions the agent took and which a human took. If a vendor cannot demonstrate all three in a test tenant, with your test data, before go-live — that is not a paperwork gap. That is the answer. Do not proceed and "tighten it later". Later is how the blind path gets built.

## 4. Regulator / Industry-Body Update — the regulators have found the connector layer too

If you think this is only a practitioner obsession, watch where the official guidance is moving. The UK ICO has been running a dedicated call for views on agentic AI. NIST's current AI and ICT risk drafts are being actively commented on — including, in submissions this month, on exactly the gap this newsletter covers: the drafts talk about models and systems, while the connector layer that gives agents their reach is barely named. Industry bodies are converging on the same point from the other side: OWASP's GenAI and MCP work, and the Cloud Security Alliance's AI controls work, both now treat tool and connector permissions as a first-class risk, not an implementation detail.

The direction of travel is clear even if the rules are not finished: when something goes wrong, "the agent did it" will not be an answer. The question will be who authorised the connection, with what scope, and where is the log. Organisations that can answer that in one meeting will be fine. Start being one of them now, while it is still cheap.

## 5. The Monday Fix — the 90-minute connector census

One fix, finishable this week. Do not boil the ocean — just take the census.

1. **List (30 min).** For each AI tool in use, list every connector switched on. Admin consoles, integration pages, and OAuth grant reports will get you most of the way.
2. **Name an owner (20 min).** Every connector gets a named human owner. No owner means it is a pilot leftover until proven otherwise.
3. **Mark the unknowns (20 min).** For each connector, answer three things: what can it read, what can it write, where does the data go? Anything you cannot answer goes on a visible "unknown" list — that list is your real risk register for now.
4. **Kill one thing (20 min).** Pick the connector with no owner and no current use case, and revoke it. One clean revocation proves the process works and makes the next ten easier.

That is it. No new tooling, no programme, no steering committee. Next Monday, bring the census to the immortal grant problem — the tokens on that list that will outlive everyone who created them.

— Vivek Kumar
AI governance practitioner · PAARA author · IAPP KnowledgeNet chapter chair

*A note on method, because readers will ask: PAARA — the methodology behind these scores — is described as 6–8 components depending on the version and paper; the count is being made consistent before filing, and this newsletter will always say "6–8" rather than pretend otherwise. The scores here are documentation-and-configuration reviews, not penetration tests.*

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

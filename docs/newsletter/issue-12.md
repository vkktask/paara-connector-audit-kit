# The Connector Audit — Issue #12

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #12 headline: The Second Coder — one auditor's scores are a claim, not a measurement, until a second coder can reproduce them. Plus the 0–4 scoring scale behind the 12 harness tests, explained for leaders, and three open OWASP threads where the connector argument is being made in public.**

---

## 1. The Connector Pattern — the automation platform that turns one AI connection into a chain of actions across every app you own

This week's pattern to check in your own estate, ahead of Connector Spy Test #19 (Zapier / Make → ChatGPT, drafted, scores blank until filmed):

An automation platform is usually approved for plumbing — "move this form submission to that spreadsheet." The grant behind an AI connection to it reaches a very different asset. The pattern to look for:

- An automation account is a map of the business. Every Zap or scenario names the apps it touches, the data it moves, and the order it moves in. An AI assistant that can read that account can read the map — which systems hold what, which workflows run the payroll-adjacent, customer-facing and finance processes, and where the bodies are buried.
- The same connection that reads automations can often act on them: trigger a Zap, edit a step, switch an automation on or off. An automation is not a document. It is standing instructions to your systems, executed under stored credentials for every app in the chain. Editing one step quietly re-points every future run.
- Automations eat whatever arrives. A Zap's input data — a form field, an email body, a webhook payload — is written by customers, strangers and other software. Anything an agent reads in that input, it may also obey. The trigger data is an input channel, and nobody reviewed it as one.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Zapier / Make → ChatGPT teardown is a pre-filming draft, to be filmed on a test account with dummy Zaps only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Second Coder

Every score in the PAARA dataset — the 13 connectors, the seven factors, the Critical bands this newsletter keeps citing — was coded by one person. Me. That is stated in the method, on the dataset page, in plain sight. This week is about why that is not good enough, and what happens next.

A single coder has a single set of judgments. Where a vendor's documentation is ambiguous — and connector documentation is ambiguous for a living — one coder reads it one way, consistently, and the consistency feels like rigour. It is not. Consistency is not accuracy. A second coder, working from the same documentation and the same coding rules, without seeing the first coder's answers, finds the places where the rules are unclear, where a factor definition bends, and where the first coder was simply wrong. The disagreements are the valuable part: each one marks a spot where the method, not just the score, needs to be sharpened.

So the next expansion of this work — the longer SAIS '27 version of the connector study — builds the second coder in as a step, not an afterthought: a second person independently re-codes a sample of the connectors, the two codings are compared, and the disagreements are resolved against the written rules and published with the dataset. Where the rules could not settle a disagreement, that gets published too. That is what method honesty looks like in practice: not "trust me, I was careful," but "here is where two careful people diverged, and here is what we did about it."

The lesson for leaders is not about this dataset. It is about every score you are handed — a vendor's self-assessment, an auditor's rating, an internal team's RAG status. Ask one question: who else, independently, got the same answer from the same evidence? A score one person produced and nobody reproduced is a claim. A score two people produced independently, with their disagreements on the record, is a measurement. Budget for the second coder — in your audits, your vendor reviews, your AI evaluations — the way you budget for the first. The first coder tells you what someone thinks. The second tells you whether it is true.

## 3. Harness — the 12 scored tests and the 0–4 scale, explained for leaders

From the AI Agent Harness Evaluation Playbook: beyond the six gates (Issues #2–#7), platforms are scored on 12 tests. Leaders do not need to run the tests. They need to be able to read the scores — and the scale is where the honesty lives.

**The scale — the same 0–4 for every test:**

- **0 — Cannot do it.** The capability does not exist. Not "switched off" — absent.
- **1 — Claimed, no artifact.** The vendor, or the team, says it works — and produced nothing you can inspect. A confident claim with no captured evidence caps here, however good the demo was.
- **2 — Partial, workaround needed.** It works with manual steps, exceptions, or a human quietly compensating. The workaround is part of the score: name it, or the score is a 1 wearing a costume.
- **3 — Works, minor gaps.** Proven in a live test, with gaps that are named, bounded, and fixable without re-platforming.
- **4 — Proven with artifact, no gaps.** The test ran, the evidence was captured — a log excerpt, a trace, a blocked-action record — and the artifact is filed where a sceptic can re-check it.

Three rules make the scale mean something. **Evidence or it didn't happen:** every test names its artifact before it runs, and no artifact means no score above 1. **Controls are proven both ways:** the legitimate action goes through AND the violating action is blocked — half the pair is an outage or a hole, not a control. **Gates first, scores second:** a platform that fails a gate (Issue #7's checklist) cannot average its way back with strong 3s and 4s here. A fatal gap divided by twelve tests is still a fatal gap.

And the tie back to this week's field note: a 0–4 score is still one tester's judgment until someone else runs the same test and lands on the same number. When you read a scorecard — including any scorecard published here — ask who the second coder was.

## 4. Regulator / Industry-Body Update — OWASP, in the open: three threads, all still open

This week's update is not a regulator filing. It is the other half of how standards actually move: public, technical, and on the record in the open-source projects the industry builds on.

On 16 November 2026, posting as **vkktask** on GitHub, Vivek Kumar filed three contributions to OWASP's AI security work, and all three remain **OPEN**:

- **OWASP MCP Top 10 — issue #73 and pull request #74:** the connector-layer argument made where the MCP security guidance is written — what a connector can reach, what it may do, and what gets logged, raised as a change to the guidance itself, not a comment about it.
- **OWASP GenAI V2 — issue #876:** the same argument carried into the GenAI security project's next version, so the connector layer is treated as an attack surface in its own right, not a footnote under model risk.

Why this belongs in a leader's newsletter: nobody adopts a framework because its author says so. Adoption looks like this — issues filed in the projects practitioners actually use, arguments tested in public by the people who maintain them, and threads that stay open while the maintainers push back, refine, or accept. These three are open. That is the honest status, and it is reported here as exactly that: contributions made and under discussion, not accepted, not endorsed, not adopted. When one of them moves — merged, closed, or rejected — this newsletter will report that too, whichever way it goes.

## 5. The Monday Fix — find your second coder before someone finds your single one

Thirty minutes, this Monday:

1. Pick one score your organisation relies on — a connector audit, a vendor rating, an internal AI risk assessment. Write down who produced it. If the answer is one person or one team marking its own work, that is the finding.
2. Name a second coder: someone competent who did not produce the original, with no stake in its answer. Internal audit, a peer team, an outside reviewer — independence matters more than seniority.
3. Give them the same evidence and the same written rules — not the original scores. Have them re-score a sample: three connectors, three tests, three controls. A sample is enough; the disagreements will find themselves.
4. Compare, in a room, on the record. Every disagreement is either a scoring error or a rule that two careful people read differently — fix the score, or sharpen the rule, and write down which. Publish the comparison wherever the original score lives.

One coder is a claim. Two coders, disagreeing in the open and resolving it in writing, is a measurement. Commission yours before a regulator, an auditor, or an incident does it for you.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

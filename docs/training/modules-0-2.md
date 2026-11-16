# Governing AI Connectors — a free, open, hands-on course

**PAARA · Open Training**

Your AI assistant is only as safe as what it can reach. This course teaches you to govern the **connector** — the permissions, servers, and pipelines that connect AI to your data — using PAARA, the Privacy-Aware AI Risk Architecture.

- **By:** Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture)
- **For:** practitioners, privacy & AI-governance professionals, and small-business operators
- **Structure:** 8 modules (0–7) + capstone
- **Modules 0–2** written in full here; Modules 3–7 in outline
- **Text licence:** CC BY 4.0 — free to use, adapt, translate & redistribute with attribution to Vivek Kumar
- **Audit-kit code licence:** MIT
- **No sign-up**

> **Please read:** this course is practitioner guidance based on one documented audit method. It is **not legal advice**. For decisions with legal consequences — regulatory filings, DPIAs, employment or vendor actions — take advice from a qualified professional in your jurisdiction.

## How the course works

Every module follows the same rhythm: a short plain-English lesson, a worked example from a real audit, a worksheet you keep, and a 60-second video script you can film or share with your team.

- **Read (5–10 min).** One lesson, in plain English, no jargon left unexplained.
- **Do (10–20 min).** A hands-on exercise on your own stack, following the worked example.
- **Take away (1).** A template — inventory, worksheet, or checklist — that becomes part of your governance file.

Modules 0–2 below are complete. Modules 3–7 are published as outlines for now — same structure, written in full in later releases. The capstone ties it together: audit one connector yourself and publish the score.

- Get the PAARA audit kit on GitHub: <https://github.com/vkktask/paara-connector-audit-kit>
- Read the PAARA paper (SSRN): <https://doi.org/10.2139/ssrn.6784078>

## The method in brief — PAARA scoring: seven factors, three codes, one band

PAARA scores a connector from its *public documentation* — what the vendor says the connector can do — across **seven factors (F1–F7)**. Each factor is coded from the evidence:

- **Y — Yes.** The risk condition is documented as present. Example: write tools are documented.
- **N — No.** The documentation shows the condition is absent, or a control is documented.
- **U — Unknown.** The documentation does not say. Unknown is *not* treated as safe — it is what makes the score a band.

Because of the U codes, every connector gets a **banded score**: a **lower** figure (unknowns resolve favourably) and an **upper** figure (unknowns resolve unfavourably). The band maps to one of four ratings — Critical, High, Moderate, Low. Each connector is scored twice: the **default** score, with permissions as shipped, and a **restricted** score, after applying any write-limiting controls the vendor actually documents (Module 2). The full factor definitions, coding rules, and evidence for all 13 connectors are in the audit kit and the paper linked above.

### Why this course exists: the 13-connector audit

- **9 / 13** connectors rated **Critical** at the lower band — rising to **12 of 13** at the upper band.
- **12 / 13** document **no prompt-injection defence** at all.
- **2 / 13** document **audit logging** — the other 11 leave you unable to reconstruct what the AI did.

> **Read these numbers with their caveat:** they are from Vivek Kumar's audit of 13 connectors, scored from vendor documentation retrieved **9 November 2026**. They have **not been independently verified**, and vendor documentation changes — which is exactly why the course teaches you to re-run the audit yourself, and why the contribution path below exists.
>
> **Logging, stated precisely:** the 2 connectors that document audit logging are Slack and Stripe — logging is documented as *present* for them (coded F4 = N under the audit's convention, where N means logging is documented). The other 11 are silent (U). No connector documents logging as absent, so F4 is never coded Y. See [`dataset-and-method.md`](../dataset-and-method.md) for the full correction note.

---

# Module 0 — Start here: what a connector is

- **Time:** 15 min total
- **Takeaway:** connector inventory template
- **Level:** start here

**By the end of this module:** You can say what a connector is, name every connector in a small stack, and record — on one page — what each one can reach and under whose authority it acts.

## Part 1 — The lesson

### A connector is a grant of permission

A **connector** is anything that links an AI assistant to your systems and data. The assistant itself — the model — starts out knowing nothing about your business. The connector is what changes that: it hands the assistant a set of permissions and a path to use them.

Connectors come in three common forms:

- **OAuth / API permissions.** The "Connect your account?" screen. When someone clicks *Allow*, the app receives a token and a set of **scopes** — named permissions such as read mail, send mail, or edit files. The token keeps working until it is revoked, long after the click is forgotten.
- **MCP servers.** Servers built on the Model Context Protocol expose *tools* — search messages, read a file, create a ticket, send a message — that the model can call. Whoever can add an MCP server to an assistant can decide which tools that assistant holds.
- **Retrieval pipelines.** The assistant is connected to a document store, wiki, or drive, whose contents are indexed so the model can search and quote them. Here the risk is quieter: data is copied into an index, where retention and access rules of their own apply.

### What can the assistant actually reach?

Whatever the grant allows — no more, but also no less. Depending on the scopes and tools, that can mean reading email and files, searching private conversations, and also *acting*: sending messages, editing records, deleting data. Crucially, the assistant acts **under someone's authority**: a named user's token, a shared service account, or an agent's own API key. If you cannot say whose authority a connector runs under, you cannot say who is accountable for what it does.

### Why the connector — not the model — is the unit of governance

Models change constantly and are hard to inspect. Connectors are the opposite: they are **countable, ownable, and revocable**. The same model is low-risk with no connectors and high-risk with a write-enabled connector into your CRM. Risk lives in the connection, so governance should too: you approve connectors one by one, you review them one by one, and when something goes wrong, the connector is the thing you switch off. That is the whole idea of PAARA — and it starts with simply knowing what you have.

## Part 2 — Worked example: mapping a small stack on one page

Below is an example inventory for a small team stack: an office-suite assistant, a chat tool with AI features, and one MCP server. These are *example entries* — in your own inventory, record what your admin console and vendor documentation actually show. The 13-connector audit records the same core facts for every connector: **name, vendor, what it can reach, and under whose authority**.

| Connector | Vendor | What it can reach | Authority | Who approves |
|---|---|---|---|---|
| Microsoft 365 Copilot | Microsoft | Mail, files, chats and meeting content the signed-in user can already access in the tenant | User (delegated) | IT admin (licence assignment) |
| Gemini for Workspace | Google | Gmail, Drive, Docs and Calendar content of the signed-in user, per admin settings | User (delegated) | Workspace admin |
| Slack AI | Slack / Salesforce | Channels and conversations the user belongs to, per workspace AI settings | User (delegated) | Workspace owner / admin |
| Filesystem MCP server (example of one MCP server) | Open-source reference server | Files and folders in the directories it is configured to serve — read and, if enabled, write | Whoever runs it (local process / agent key) | Nobody, unless you make it somebody — record your own approver |

Notice the last row: the inventory's job is to surface the connectors nobody formally approved. In most stacks, those are the ones that matter most.

## Part 3 — Checklist / worksheet: your connector inventory template

One row per connector. If a field is genuinely unknown, write *Unknown* — in PAARA terms that is a finding, not a blank.

- **Connector** — The product or server name as users know it.
- **Vendor** — Who supplies it — including "open source / self-hosted" where that is the truth.
- **Version / endpoint** — Version, hosted endpoint URL, or local install path.
- **Systems / data reachable** — What it can read and what it can change — name the systems and the data classes.
- **Authority** — User token, service account, or agent key — and whose name it is in.
- **Who can enable it** — Admin only, or any user with one click?
- **Who approves** — The named role that signs off before it is enabled.
- **Data residency / retention** — Where data is processed and stored, and how long the vendor keeps it.

CSV header for the template (`paara-connector-inventory.csv`):

```csv
connector,vendor,version_or_endpoint,systems_data_reachable,authority,who_can_enable,who_approves,data_residency_retention
```

## Part 4 — 60-second video script: "The connector is the risk"

≈110 words · ~60 seconds · film vertical, captions on.

> **Hook (0–3 seconds):** "Your AI assistant can already read more of your business than you think."
>
> "Every AI tool reaches your data through a connector — a set of permissions somebody approved, often with one click. The model isn't the risk. The connector is. It decides what the assistant can open, copy, change, and send. So don't start by asking, 'Is this AI safe?' Start by listing your connectors: what each one is, what it can reach, and whose authority it runs under. That one page is your inventory — and it's where governing AI actually begins."

---

# Module 1 — The five PAARA questions

- **Time:** 20–30 min total
- **Takeaway:** PAARA 5-question worksheet
- **Uses:** Slack MCP worked example

**By the end of this module:** You can take any connector and, using only its documentation, answer the five PAARA questions with evidence — and turn the answers into a defensible risk band.

## Part 1 — The lesson: five questions, asked of every connector

You do not need a security team to start assessing a connector. You need five questions, the vendor's documentation, and the discipline to write down what the documentation *actually says* — including when it says nothing.

| Question | What you are looking for |
|---|---|
| 1 · What can it reach? | The systems, data, and conversations inside the grant — including other people's content, not just the user's own. |
| 2 · Does it touch sensitive data? | Personal data, credentials, financial or health information, confidential business material — anything whose exposure would hurt. |
| 3 · Is it least-privilege, or broader than needed? | Whether the permissions match the job, or quietly include write access, admin reach, or whole-tenant scope nobody asked for. (Module 2 goes deep here.) |
| 4 · Can you reconstruct what it did afterwards? | Documented logging: who or what acted, which tools ran, what data was touched. No log means no reconstruction — and no incident response. |
| 5 · How does it amplify insider risk? | What a careless or malicious insider — or an attacker holding their token — could do through this connector that they could not do as quickly, quietly, or at such scale without it. |

Answer each question from evidence: a short quote or paraphrase from the documentation (25 words or fewer), the source URL, and a **Y / N / U** code. **U — unknown — is a legitimate answer**, and often the most important one: across the 13-connector audit, unknowns are what push so many connectors from High at the lower band to Critical at the upper band.

## Part 2 — Worked example: the five questions applied to Slack MCP

Every fact below is taken from the 13-connector audit's documented record for Slack MCP — nothing added, nothing assumed.

| Question | Documented evidence | Reading |
|---|---|---|
| 1 · Reach | Private channels, direct messages, and user profile email addresses are reachable. | Reach extends well beyond public channels — into the most candid conversations in the business. |
| 2 · Sensitive data | Retrieved messages are authored by other people; direct messages and profile emails are personal data by any definition. | Yes — third-party personal data, not only the connecting user's. |
| 3 · Least privilege | Access runs on user tokens obtained through a registered app; write tools exist, and messages can be sent. | Broader than read-only assistance: the connector can act, not just look. |
| 4 · Reconstructability | Audit logging is documented. | A genuine strength — Slack MCP is one of only 2 of the 13 connectors that document logging. |
| 5 · Insider risk | One user's token can search and retrieve other people's private messages and DMs, and send messages as that user. | High amplification: bulk retrieval plus impersonation, at machine speed. |

**Default band (as shipped): Critical → Restricted band (documented write-limiting controls applied): High.**

The lesson is not "never connect Slack." It is that a connector can document real strengths — logging, here — and still land at Critical by default, because reach, third-party data, and write capability stack up. Restrictions move the band; they rarely erase the risk.

## Part 3 — Checklist / worksheet: the PAARA 5-question worksheet

One worksheet per connector. Keep the evidence snippet to **25 words or fewer**, always with its source URL — a score you cannot trace to evidence is an opinion.

| Question | Evidence snippet (≤25 words) | Source URL | Y / N / U |
|---|---|---|---|
| 1 · What can it reach? | | | |
| 2 · Does it touch sensitive data? | | | |
| 3 · Least-privilege, or broader than needed? | | | |
| 4 · Can you reconstruct what it did (logging)? | | | |
| 5 · How does it amplify insider risk? | | | |

CSV header for the worksheet (`paara-5-question-worksheet.csv`):

```csv
connector,question,evidence_snippet_max_25_words,source_url,code_Y_N_U,notes
,"1 - What can it reach?,,,,
,"2 - Does it touch sensitive data?,,,,
,"3 - Is it least-privilege or broader than needed?,,,,
,"4 - Can you reconstruct what it did afterwards (logging)?,,,,
,"5 - How does it amplify insider risk?,,,,
```

## Part 4 — 60-second video script: "Five questions before you connect"

≈110 words · ~60 seconds · film vertical, captions on.

> **Hook (0–3 seconds):** "Five questions. One connector. A Critical rating."
>
> "Before you approve any AI connector, ask five questions. What can it reach? Does it touch sensitive data? Is it least-privilege, or broader than needed? Can you reconstruct what it did afterwards? And how does it amplify insider risk? Take Slack's MCP connector. It reaches private channels, direct messages, and profile emails. It can send messages. Other people's words are the data. Audit logging is documented — a real strength, and rare. The PAARA verdict: Critical by default, High even when restricted. Five questions, answered from the vendor's own documents. Try them on your stack."

---

# Module 2 — Scopes & least privilege

- **Time:** 20–30 min total
- **Takeaway:** scope-review checklist
- **Uses:** Linear MCP & Microsoft Graph

**By the end of this module:** You can read a permission list line by line, tell delegated from application permissions and read from write, and find — or expose the absence of — a connector's documented write-limiting controls.

## Part 1 — The lesson: two axes decide most of the risk

Almost every permission a connector holds sits on two axes. Learn to read both, and a consent screen stops being fine print and becomes a risk statement.

### Axis 1 — whose authority? Delegated vs application

| Type | How it works | Governance consequence |
|---|---|---|
| **Delegated** (user-bound) | The app acts *on behalf of a signed-in user*, with a token in that user's name. It can generally reach only what that user could reach. | Risk follows the user: their reach, their token, their departure. Revoke the user, revoke the access. |
| **Application** (non-user-bound) | The app acts *as itself* — a service or daemon with its own credentials, no user present. Grants are often tenant-wide unless deliberately constrained. | Risk follows the app, silently and at scale. It needs its own owner, its own review, and its own off-switch. |

**Axis 2 — read vs write.** Read scopes let the assistant see; write scopes let it change, send, and delete. The jump from read to write is the single biggest step in connector risk, because it turns exposure into action — and a prompt-injected assistant with write tools can be made to act, not merely to leak.

### Resource-specific consent: narrower by design

Microsoft Graph — the API behind Microsoft 365 — is the clearest mainstream example of both axes. It offers the same capability (say, reading mail) as a *delegated* permission, acting for a signed-in user, or as an *application* permission, acting on its own. And alongside broad grants, Graph supports **resource-specific consent**: permission scoped to one specific resource — a particular site or team, for example — instead of every resource of that type in the tenant. The principle generalises to every platform: **if a narrower grant exists and you took the broader one, that choice — not the vendor — is your finding.**

### Write-limiting controls: what to look for in the docs

PAARA's restricted score only credits controls the vendor *documents*. The three patterns to look for:

- **Read-only scopes** — a permission set with write removed, selectable at install time.
- **Read-only endpoints** — a dedicated endpoint that cannot write, however it is called.
- **Admin-selected tools** — an admin chooses which tools are exposed, rather than accepting the full tool list.

If none of the three is documented, there is no restricted score to claim — the default band stands. That absence is itself one of the most useful findings you can hand a vendor.

## Part 2 — Worked example

### Linear MCP: the clearest least-privilege path in the corpus

Linear MCP documents something none of the other audited connectors match as cleanly: a **dedicated read-only endpoint**. Point the connector at that endpoint and write capability is removed by architecture, not by policy or by promise — the clearest least-privilege path in the 13-connector corpus.

**Linear MCP, default: Critical → With the read-only endpoint applied (restricted): High** (restricted band: High → High).

Two honest lessons follow. First, the control works: a documented restriction moved the band. Second, it moved it to **High, not Low** — read-only access to a full project-tracking workspace is still broad reach into sensitive operational data. Least privilege reduces risk; it does not finish the job.

### The contrast: Stripe MCP

Stripe MCP documents **no write-limiting control** of the three kinds above. Under the PAARA rule there is therefore **no restricted score** for Stripe MCP — not a worse score, an absent one. When you review a connector and find no documented way to limit it, record exactly that. "No documented write-limiting control" is a precise, evidence-based sentence a vendor can act on.

## Part 3 — Checklist / worksheet: scope-review checklist

Work through every scope *individually* — never approve a bundle you have not itemised.

- **List every scope, one per line** — Copy the exact scope or tool name from the consent screen or documentation — no summaries.
- **Mark each one read or write** — If a scope does both, it is a write scope. Treat it that way.
- **Mark each one delegated or application** — Whose authority does it run under — a named user, or the app itself?
- **Write the justification** — One sentence: what breaks for a real user if this scope is removed? If nothing breaks, it should not be granted.
- **Name the least-privilege alternative** — Read-only scope, read-only endpoint, admin-selected tool list, or resource-specific consent — or record "none documented."
- **Record the decision and the decider** — Granted as-is, granted restricted, or refused — with a name and a date.

| Scope / tool | Read / Write | Delegated / Application | Justification | Least-privilege alternative |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

CSV header for the worksheet (`paara-scope-review-worksheet.csv`):

```csv
connector,scope_or_tool,read_or_write,delegated_or_application,justification,least_privilege_alternative,decision,decided_by,date
```

## Part 4 — 60-second video script: "Read-only is a choice"

≈110 words · ~60 seconds · film vertical, captions on.

> **Hook (0–3 seconds):** "Read-only is a choice — if your connector offers it."
>
> "Every permission sits on two axes. Delegated, acting as a user — or application, acting as itself, often across the whole tenant. And read, or write. Write is where exposure turns into action. So look for a documented way to limit it: read-only scopes, a read-only endpoint, admin-selected tools. Linear's MCP server offers a dedicated read-only endpoint — the clearest least-privilege path in our thirteen-connector audit. Using it moves Linear from Critical to High. Stripe's MCP documents no such control — so there is no restricted score at all. Check yours before you approve it."

---

# Modules 3–7 — outline

Same structure as Modules 0–2 — lesson, worked example, worksheet, 60-second script. Published here as outlines so you can see the whole path; they are **not written in full yet**.

## Module 3 — Prompt-injection defence (or its absence) *(Outline)*

**Hands-on:** run the PAARA kit against one connector's documentation and record two separate things — whether a prompt-injection defence is *documented*, and whether it is *tested*. Documented-but-untested is its own finding. Context: 12 of the 13 audited connectors document no defence at all.

**Takeaway:** injection-defence test sheet.

## Module 4 — Logging & reconstructability *(Outline)*

**Hands-on:** take one real AI output and try to reconstruct it from the logs alone — who acted, under which agent identity, which tools ran, and what data was touched. Where the trail breaks is your requirements list.

**Takeaway:** log-requirements checklist, mapped to EU AI Act Articles 12 and 26.

## Module 5 — Agent identity & privilege *(Outline)*

**Hands-on:** give a test agent its own identity — not a person's borrowed token — with short-lived, narrowly scoped credentials. Then demonstrate the revocation: kill the credentials and watch the agent stop.

**Takeaway:** one-page agent-identity policy.

## Module 6 — DPIA for a connector *(Outline)*

**Hands-on:** a worked data protection impact assessment for one connector, using the Article 29 Working Party nine-criteria test to decide whether a DPIA is required, then assessing residual risk — and naming who accepts it.

**Takeaway:** connector DPIA template.

## Module 7 — The approved list & rollout *(Outline)*

**Hands-on:** turn your inventory and scores into a one-page connector policy: the approved list, who approves additions, a staged rollout, the trigger that forces a re-review, and the incident plan for when a connector misbehaves.

**Takeaway:** connector policy + rollout plan.

---

# Capstone — Audit one connector. Publish the score.

The course ends the way PAARA is meant to be used — in the open. Pick one connector from your own inventory, run the full method from the audit kit, and publish your score **with the method version and the date** you scored it, so anyone can re-check your evidence and re-run your work. A published, reproducible capstone audit earns the course certificate.

1. **Score it** — Inventory entry (Module 0), five questions with evidence (Module 1), scope review (Module 2) — full F1–F7 coding from the kit.
2. **Show the evidence** — Every code traceable to a documentation snippet and a source URL. Unknowns marked U, never silently treated as safe.
3. **Publish it** — Score, band, method version, and date — shared where other practitioners can find it, challenge it, and build on it.

# Help extend the audit

The 13-connector corpus is a starting point, not a finished map — and its numbers carry the caveat stated above: one auditor, documentation retrieved 9 November 2026, not independently verified. The fastest way to strengthen it is more eyes on the same method. Three ways in:

- **Re-code** — Take a connector already in the corpus, code it independently from the same documentation, and compare. Disagreements are where the method gets sharper.
- **Extend the corpus** — Score a connector that is not yet in the audit — your stack almost certainly has one — using the kit's coding sheet.
- **Open a PR** — Submit your score to the audit-kit repository with its evidence snippets, source URLs, method version, and date.

- PAARA connector audit kit — GitHub: <https://github.com/vkktask/paara-connector-audit-kit>
- PAARA paper — SSRN DOI: <https://doi.org/10.2139/ssrn.6784078>

---

***Governing AI Connectors (PAARA)** — Training Modules 0–2 in full; Modules 3–7 in outline; capstone. By Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture).*

***Licence:** the training text in this file is licensed under **CC BY 4.0** — free to use, adapt, translate, and redistribute with attribution to Vivek Kumar. The audit-kit code is licensed under **MIT**.*

***Not legal advice:** this course is practitioner guidance based on a documented audit method. Scores describe what vendor documentation states, retrieved on the dates shown; documentation changes, so re-check before acting.*

*Audit figures cited: 13-connector audit by Vivek Kumar, documentation retrieved 9 November 2026, not independently verified.*

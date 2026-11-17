# The Connector Audit — Issue #13

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #13 headline: The Rug Pull — the connector you approved is not necessarily the connector running today, because a server can change its tool definitions after your review. Plus the four changes that should force a re-approval, and two open contributions — MITRE ATLAS and the SAFE WG — where the connector argument is being made in public.**

---

## 1. The Connector Pattern — the database your teams built themselves, handed to an AI in one grant

This week's pattern to check in your own estate, ahead of Connector Spy Test #20 (Airtable → ChatGPT, drafted, scores blank until filmed):

Airtable is rarely bought as a system of record. It grows into one — the tracker a team built because the official system was too slow, then the customer list, then the budget, then the thing the business quietly runs on. The pattern to look for:

- One grant, many databases. A connector approval reads like a single tool — "let the assistant use Airtable." The grant behind it typically reaches every base the connecting user can reach: every table, every record, and — through linked-record fields — the joins between tables that turn separate lists into a picture of the whole operation.
- Write access hides inside a productivity story. The use case is summarising and searching. The grant often also covers creating, updating and deleting records. A deleted record disappears from every view, automation and integration built on it — and the person who approved "search" never consciously approved "delete."
- Every field is an input channel. Bases are filled in by staff, contractors and public form submissions. Any text field an agent reads is text it may obey. Nobody reviewed the notes field as an instruction channel, because nobody thought of it as one.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Airtable → ChatGPT teardown is a pre-filming draft, to be filmed on a test account with dummy bases only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Rug Pull

Most connector reviews share one quiet assumption: the thing you reviewed is the thing that keeps running. You read the tool definitions, you checked the scopes, you wrote the approval. Done.

An MCP server — and a connector generally — does not have to keep that promise. The tool definitions a server presents are served by the server, at connection time. A server that was honest at review can change what its tools are called, what their descriptions say, and what they actually do, after approval — in the pattern named in the PAARA framework as the **rug pull**: the approved tool is quietly swapped for a different one under the same name. The description your agent reads can gain new instructions. A read-only-looking tool can start writing. Nothing in a one-time approval notices, because nothing re-checks.

A note on provenance, because this newsletter does not borrow credibility: the rug-pull concept as a PAARA connector risk was publicly disclosed in the PAARA SSRN preprint on 28 May 2026 — it is a named pattern in a published framework, described here as a pattern to defend against, not as an incident attributed to any named vendor. No vendor is accused of doing this. The point is structural: your approval process cannot tell the difference between a server that stayed honest and one that didn't, unless you built the re-check in.

The lesson for leaders: approval is a photograph, and the connector is a live feed. If your governance takes the photograph once and files it, then every control downstream — the DPIA, the risk register entry, the board assurance — describes a tool that may no longer exist. The defence is not suspicion; vendors update tools legitimately all the time. The defence is treating change as a trigger: when the tool definitions move, the approval expires, and a human looks again. That is Section 3.

## 3. Harness — Re-approval triggers: the four changes that expire an approval

From the AI Agent Harness Evaluation Playbook and the Go-Live Runbook: an approval is granted to a specific configuration, not to a product name. These four changes void it and force a re-review before the connector runs again under the old sign-off:

1. **Scope change.** The grant widens — a new scope, a new base, workspace or data store reachable, a read grant becoming read-write. Any widening is a new approval, in full, not an amendment. Narrowing can be noted and filed; widening cannot.
2. **Tool-definition change.** The server presents different tools than the ones reviewed — a tool added, removed, renamed, or the same tool with a materially different description or behaviour. This is the rug-pull tripwire: you cannot diff what you did not snapshot, so the reviewed tool definitions are captured and filed at approval, and the live definitions are compared against them on a schedule.
3. **Vendor change.** The connector, the MCP server, or a sub-processor behind it changes hands, changes hosting, or is replaced by a different implementation under the same name. The approval was of that vendor's controls and that implementation — not of the label.
4. **New data class.** The connector starts touching a class of data it was not approved for — personal data where only operational data was reviewed, regulated data, a new population (children, patients, employees' private data). The DPIA was written about the old data. New data class, new assessment.

Two operating rules make the triggers real rather than decorative. **The snapshot rule:** at approval, file the tool definitions, the scopes, the vendor and sub-processor list, and the data classes — four artefacts, one page each at most — or none of the triggers can ever fire, because there is nothing to compare against. **The default-expire rule:** when a trigger fires and nobody re-reviews, the connector does not keep running on the old approval by inertia; it is suspended until the re-review happens. A trigger that only sends an email is a notification, not a control.

## 4. Regulator / Industry-Body Update — MITRE ATLAS and the SAFE WG: two threads, both still open

This week's update is, again, the open-standards half of how this field actually moves — contributions on the public record, reported at their honest status.

On 16 November 2026, posting as **vkktask** on GitHub, Vivek Kumar filed two further contributions, and both remain **OPEN**:

- **MITRE ATLAS — issue #35:** the connector-layer argument carried into the adversarial-threat knowledge base the industry uses to name AI attacks — that the connector / MCP layer, its scopes and its tool definitions, belongs in the threat model as its own surface, not folded into generic model misuse.
- **SAFE WG — issue #88:** the same argument raised in the SAFE working group's agent-security work, where practitioners are defining what safe agentic systems have to prove — identity, scope, logging, and change control on the tools an agent is handed.

Why this belongs in a leader's newsletter, stated the same way as last week because it is still true: nobody adopts a framework because its author says so. Adoption looks like issues filed in the projects practitioners actually use, arguments tested in public by the people who maintain them, and threads that stay open while the maintainers push back, refine, or accept. These two are open. That is the honest status, and it is reported here as exactly that: contributions made and under discussion, not accepted, not endorsed, not adopted. When one of them moves — merged, closed, or rejected — this newsletter will report that too, whichever way it goes.

## 5. The Monday Fix — snapshot the connector you approved, so change has something to trip over

Thirty minutes, this Monday:

1. Pick one live AI connector — the one your teams would miss most if it stopped. Open its approval record. If there is no filed snapshot of its tool definitions, scopes, vendor and data classes, that absence is the finding.
2. Take the snapshot now: export or screenshot the tool definitions it currently presents, list the scopes it actually holds, name the vendor and any sub-processors, and write down the data classes it can reach. Date it. File it with the approval.
3. Write the four triggers into the approval itself — scope change, tool-definition change, vendor change, new data class — with one sentence each: "this approval expires and the connector is suspended until re-review." Get the approver to sign the amended version, not a side email.
4. Set the comparison habit: once a month, someone diffs the live tool definitions and scopes against the snapshot. Fifteen minutes. Any difference is not an incident — it is the trigger working. Suspend, re-review, re-approve or retire.

You cannot catch a rug pull with a review that happened once. You catch it with a snapshot, a diff, and an approval that knows how to expire.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

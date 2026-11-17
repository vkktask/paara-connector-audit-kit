# The Connector Audit — Issue #14

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #14 headline: The Vendor Update Nobody Read — the routine release-notes email that quietly changed your connector's terms and scopes, and why that change should expire the approval you already gave. Plus the connector DPIA on one page, and the PAARA audit kit's v1.2 release — versioned, citable, and open.**

---

## 1. The Connector Pattern — the team's whole working memory, handed to an AI in one grant

This week's pattern to check in your own estate, ahead of Connector Spy Test #21 (Trello → ChatGPT, drafted, scores blank until filmed):

Trello is rarely bought as a system of record either. It becomes the place the work actually lives — the project board, then the hiring board, then the escalation board, then the personal board a manager keeps because nothing else stuck. The pattern to look for:

- One grant, every board. A connector approval reads like a single tool — "let the assistant use Trello." The grant behind it typically reaches every board the connecting user can reach: every list, every card, every description, comment and checklist — including boards marked private, because "private" is a sharing setting between people, not a boundary against a grant the account already holds.
- Write access hides inside a productivity story. The use case is summarising and searching boards. The grant often also covers creating cards, moving them between lists, completing or archiving them, and adding members. Adding a member hands a new person the whole board — and the person who approved "summarise my board" never consciously approved "invite people to it."
- Every card is an input channel. Boards are filled in by staff, contractors and anyone a board was ever shared with. Any card description or comment an agent reads is text it may obey. Nobody reviewed the card description as an instruction channel, because nobody thought of it as one.

That is a pattern, not a finding about a named product. No vendor score is published here, because none has been earned yet: the Trello → ChatGPT teardown is a pre-filming draft, to be filmed on a test account with dummy boards only, and every score in it stays blank until that film exists. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Vendor Update Nobody Read

Every connector you have approved is being maintained by someone else, on their schedule, announced in an email almost nobody reads: the release-notes email. "We've updated our terms." "New features are here." "Your plan now includes…" It lands in the same inbox as a hundred other vendor notices, it is written to sound routine, and in governance terms it is anything but.

Read one of those emails the way an auditor would, and it can contain any of the four changes that Issue #13 said should expire an approval:

- **A scope change**, dressed as a feature. "Your assistant can now also…" is a widening grant. The approval covered the old reach. The new reach was never assessed — it was announced.
- **A tool-definition change**, dressed as an improvement. The connector's tools are renamed, merged or given new behaviour. The tool definitions you snapshot at approval no longer match the ones running — the rug-pull tripwire from last week, except pulled slowly and in plain sight, by a changelog.
- **A vendor change**, dressed as company news. An acquisition, a new sub-processor, a hosting move. The approval was of that vendor's controls and that implementation — not of whoever owns them now.
- **A new data class**, dressed as an integration. The connector now also touches a calendar, a file store, a CRM — data the DPIA never described, about people who were never in scope.

None of this requires a careless vendor. Updating a product is what vendors are for. The failure is on the approving side: the approval was written as if the connector were a fixed object, the update channel was never wired into the approval process, and the one person who does read the release notes — if anyone does — has no instruction that says "this email can expire an approval; escalate it." So the change lands, the connector keeps running on the old sign-off, and every document downstream — the DPIA, the risk register, the board assurance — now describes a grant that no longer exists. The approval did not lapse because someone made a bad decision. It lapsed because a routine email was treated as marketing.

The lesson for leaders: an approval is only as good as the channel that tells you it has expired. If vendor update emails for your approved connectors go to a personal inbox, an unmonitored alias, or nowhere, you do not have change control over your connector estate — you have a subscription to surprises.

## 3. Harness — The DPIA for a connector, on one page

From Training Module 6 of *Governing AI Connectors*, the open PAARA training course: a Data Protection Impact Assessment is usually written for a system, but the connector is where the processing actually happens — it decides what data the assistant can reach, whose data it touches, and what it can do with it. A system-level DPIA that never names the connectors has not assessed the processing. The whole assessment fits on one page, in five moves:

1. **Describe the processing.** The connector, what it can reach, whose data, under whose authority, for what purpose. One connector per DPIA — never one DPIA for "the AI platform" with the connectors left as an appendix.
2. **Run the nine-criteria test at the connector layer.** PAARA applies the Article 29 Working Party's nine criteria for high-risk processing — evaluation or scoring, automated decisions with significant effect, systematic monitoring, sensitive data, large scale, matching datasets, vulnerable data subjects, innovative technology, processing that blocks a right or a service — to the connector itself. A connector that reaches private messages or boards across a whole tenant trips several at once. Stated honestly: this is PAARA applying the test at the connector layer, with the reasoning shown — regulators have not specifically applied it in that context.
3. **Assess necessity and proportionality.** Is the reach necessary for the stated purpose, or broader than the job needs? Name the least-privilege alternative — the narrower scope, the read-only grant, the smaller data set — and if you are not taking it, say why.
4. **Identify the risks and the mitigations.** Use the PAARA band and the factor codes behind it as the risk evidence. For each mitigation — documented restrictions, logging, agent identity, human gating — record whether it is **documented, tested, or merely promised**. Those are three different things, and a DPIA that treats a promise as a control is fiction.
5. **Name the residual risk and its owner.** What risk remains after mitigation, in plain words — and the named person who accepts it, the date they accepted it, and the review date. A connector can document real strengths and still carry a High residual risk; the decision is only defensible when the residual risk and its owner are written down. A DPIA with no named acceptor is a draft, not a decision.

The kit's connector DPIA template (`templates/connector-dpia-template.md` in the audit-kit repository) is this page as a fillable form — one per connector, filed with the approval snapshot from Issue #13, and re-opened whenever a re-approval trigger fires — including the vendor update in Section 2.

## 4. Regulator / Industry-Body Update — PAARA audit kit v1.2: versioned and citable

This week's update is from this newsletter's own workbench, reported at its exact status.

On 16 November 2026, the **PAARA Connector Audit Kit v1.2 release was published on GitHub**: https://github.com/vkktask/paara-connector-audit-kit/releases/tag/v1.2 — with the full release notes. The release commit added a `CITATION.cff` file to the repository root (commit `cfd734e`, "Add CITATION.cff for the v1.2 release"), which is the machine-readable citation file GitHub surfaces as "Cite this repository" — so anyone who uses the kit, the 13-connector dataset, the checklist or the DPIA template can now cite a specific version, by a named author, in one click, instead of pointing at a moving repository.

Why a citation file belongs in a leader's newsletter: frameworks get adopted when other people can build on them *and point at them precisely*. An unversioned link cannot be cited in a paper, a regulator submission or a board paper, because nobody can tell which version was read. A versioned release with a citation file can. That is the unglamorous infrastructure of adoption — the same reason this newsletter reports open issues as open and blank scores as blank: the record has to be checkable, or it is just marketing.

Two follow-on steps remain open, and are reported as open: enabling GitHub Discussions on the repository, and connecting the repository to Zenodo so releases receive a DOI — both need account steps by the repository owner, alongside creating an ORCID record. When they land, this newsletter will say so; until then, v1.2 with its `CITATION.cff` is the citable form.

## 5. The Monday Fix — route the vendor update emails into the approval process

Thirty minutes, this Monday:

1. List your approved AI connectors — the Monday inventory from Issue #8. For each one, answer one question: where do that vendor's release-notes and terms-update emails actually go? A person's inbox, an unmonitored alias, or nowhere anyone can name. If nobody can name the destination, that is the finding.
2. Give every approved connector a named update owner and a monitored address. Vendor product, terms and sub-processor update emails for approved connectors go to a shared, monitored mailbox — and to the person who owns the approval, not just to whoever connected the tool.
3. Write the escalation rule into the approval itself, one sentence: "A vendor update that changes scopes, tool definitions, the vendor or its sub-processors, or the data classes touched expires this approval until re-review" — the four triggers from Issue #13, wired to the email channel that actually announces them.
4. Work the backlog once: search the update mailbox for the last six months of notices for your approved connectors, and diff anything they announce against the filed approval snapshots. Any scope, tool, vendor or data-class change you find is not an incident — it is a trigger that fired silently. Suspend, re-review, re-approve or retire, and file the new snapshot.

You cannot expire an approval on a change nobody saw. Route the email, name the owner, and the quietest message in the inbox becomes a control.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

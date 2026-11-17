# The Connector Audit — Issue #31

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #31 headline: The Link That Outlived the Project — a shared link is a grant nobody filed: it is created in a hurry, it reaches whoever holds it, and it keeps working after the project ends, the team disperses and the person who made it leaves. Plus the sharing and external-access review — who outside can reach in, which links ever expire, and the guest inventory nobody keeps — and a dataset and tool paper on the PAARA Connector Audit Kit, submitted to CODASPY 2027: submitted and under review, not accepted.**

---

## 1. The Connector Pattern — the file store, reached from a second AI side

This week's pattern to check in your own estate:

Teardown #17 tested Dropbox → ChatGPT. Teardown #38 tests **Dropbox → Claude**: the same file store, reached from a different AI assistant. The pattern is the one this series keeps returning to — the store does not change, the route does, and the route is where the risk lives. A second AI side means a second grant, a second approval surface, and a second log story, all landing on the same archive.

- The read reach is the un-system-of-recorded truth. A file store holds what never made it into a governed system: contracts, board papers, HR letters, the spreadsheet with the salary bands. Tested in Teardown #38 on a **test Dropbox account with dummy files only**: the files named in the request, files nobody pointed the assistant at, account-wide search, deleted and older versions, the folders other people shared in — and a **control file** held in a separate account that was never connected or shared. The filmed question is whether the reach is the one file in the conversation, or the whole archive made searchable.
- The write reach includes the only write in this series that publishes. Upload, edit, share, delete — and **create a share link**: a URL that hands the file to whoever holds it, inside or outside the organisation. Each is filmed in Teardown #38 with the approval step, or its absence, on camera, including the link's default settings where they are visible — who can open it, whether a password is set, whether an expiry exists at all.
- There is no dataset shortcut for this one. Dropbox → Claude is **not** one of the 13 connectors in the published documentation audit, so no audit code exists to lean on, and nothing carries over from Teardown #17 either, because the grant, the approval surface and the log story belong to this route, not to the store. Teardown #38's scorecard is blank until the film, and the film is the only source it will ever cite.

That is a pattern, not a finding about a named product. No vendor score is published here, and Teardown #38 is not filmed yet — its scores are blank until the film. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Link That Outlived the Project

Issue #2 of this newsletter was about the immortal grant: the connector nobody ever revoked, still holding its scopes years after the project that justified it ended. The share link is that grant's quieter sibling — smaller, more numerous, and created by everyone, not just by the people who approve connectors.

Consider how a link is born. A project is live, a deadline is tonight, and someone outside — a contractor, a counsel, a partner — needs one file. The governed route (an account, a permission, an expiry) takes twenty minutes nobody has. The link takes ten seconds. It is created with the defaults the tool offers, which in most estates means: anyone with the link can open it, no password, no expiry. The file goes out, the deadline is met, and the link does its job so well that nobody ever thinks about it again.

Then the project ends. The team disperses. The contractor's engagement closes; the partner relationship cools; the person who created the link leaves the company — and their account is disabled, in the tidy offboarding Issue #16 described. But the link is not the account. The link is a standing invitation addressed to no one and everyone, and in many estates nothing in the offboarding, the project closure, or the annual access review ever enumerates it. The file it opens may itself have changed since: files behind links get edited, updated, replaced with newer, more sensitive versions — and the link faithfully serves whatever the file has become. A link created for a draft serves the final. A link created for the final serves the annotated copy with everyone's comments in it.

Now add the connector. An AI assistant with write access to the file store can mint these invitations at conversational speed — "share this with the team" becomes a link, because a link is the share that always works — and each one inherits the same defaults and the same invisibility. The grant register this series keeps asking you to keep (who approved what, reaching what, expiring when) has no line for links, because links were never treated as grants. They are. A link is a grant of read access to an unnamed, unauthenticated, unbounded audience, with no expiry and no owner after the creator moves on. Priced honestly, it is the broadest grant in most estates — and the least inventoried.

Teardown #38 tests this pattern on Dropbox → Claude: file read reach across the store with shared folders and a control file, write actions — upload, edit, share, delete, and link creation with its defaults filmed — a hidden instruction planted in a dummy document, and the activity log behind it all, including the question of whether a link being **opened** by an outsider leaves any trace at all. It is filmed on a test account with dummy files only, it is not filmed yet, and this note claims no result from it. The pattern does not need a result: open your own estate's link list and count the ones whose project you cannot name. That count is the finding, and it is already available to you.

The lesson for leaders: revocation reviews cover accounts, tokens and connector grants, because those look like access. Links do not look like access — they look like sharing, a collaboration feature, a convenience. Reclassify them. Every shared link is an external grant with an audience of "whoever," and it deserves the same three questions as any connector in this series: who approved it, what can it reach **now**, and when does it end. Section 3 turns that into a review you can run.

## 3. Harness — Sharing and external access review: who outside can reach in

The connector reviews in this series mostly face inward: what the agent can reach, what it can write, what the log shows. This section faces the other way — outward, at everyone who is **not** in your organisation but can reach into it through a share, a link, or a guest seat. It is the external mirror of Issue #2's immortal grant: that issue asked which of your own grants never die; this one asks which doors into your estate are standing open to people you no longer employ, engage, or remember.

**Step 1 — Enumerate the three external surfaces, separately.** External access hides in three different lists, owned by three different consoles, which is why no single review ever sees it whole. (a) **Shared links**: every link created in the file store, with its target file, its audience setting, its password/expiry state, and its creator. (b) **Direct external shares**: files and folders shared to named outside accounts — the governed-looking ones, which still accumulate. (c) **Guest and external members**: outside accounts holding seats in the workspace itself — in Slack channels, Teams, shared drives, project tools. Pull all three lists in the same week, or the review is a portrait with the edges cropped.

**Step 2 — Score each entry against the three grant questions.** For every link, share and guest: **Who approved it** — a name, or "unknown," which is itself a finding. **What can it reach now** — not what it reached on creation day: follow the link to the file as it exists today, check whether the folder it opens has grown, and check whether a guest seat granted for one channel can see others. **When does it end** — an expiry date, a project end date, a review date, or "never," written down as "never" rather than left blank. Entries that fail all three are not edge cases; in most estates they are the majority of the list, and they are the review's real output.

**Step 3 — Apply the defaults that make the next link safe.** A review that only cleans the past will be re-run forever. The durable fixes are defaults, set once: links expire by default (a short default — days, not months — with extension as the deliberate act); link creation for sensitive data classes requires a password or a named-account share instead; guests are provisioned with an end date at creation, tied to the engagement, not the calendar year; and link creation by **connectors and agents** is either disabled or routed through the same approval as a human's external share — the agent's convenience is not a reason the grant skips the register. Where the tool cannot set a default, that gap goes in the approval record with a named owner, the same discipline as any other paper-only control.

**The cadence.** External access decays on the project's clock, not the audit's: people leave engagements monthly, not annually. Run the enumeration quarterly, expire aggressively, and sample monthly — pick five live links at random and open them as an outsider, from a personal device, logged out. What you can read, anyone holding that link can read. That five-minute test is the review's evidence pair, in the sense Issue #25 established: the list says the link is scoped; the opened file proves what it actually serves.

## 4. Regulator / Industry-Body Update — CODASPY 2027: a dataset and tool paper submitted, not accepted

This week's update is a submission, reported at exactly that status.

**The PAARA Connector Audit Kit paper was registered and submitted to CODASPY 2027, in the Dataset/Tool track, as HotCRP submission #149.** The abstract was registered on **15 November 2026**, and the full five-page anonymous paper — "PAARA Connector Audit Kit" — was uploaded the same day, 15 November 2026, marked ready for review. The submission remains editable until **8 December 2026**. The paper presents the kit itself as the contribution: the 13-connector coded dataset, the seven-factor scoring method, and the open-source scanner that reproduces the scores — the same artefacts this newsletter's method rests on, offered to the research community as a dataset and tool others can run, extend and challenge.

The status, stated at its actual precision: **submitted and under review, and nothing more.** HotCRP #149 is an identifier on a submitted paper, not a result. No acceptance is claimed, implied, or expected in print before a decision exists. This newsletter has made the same distinction for talks, workshops and symposium papers throughout this series, and a dataset/tool paper gets the same treatment: if a decision arrives, it will be reported here as a new fact with a date on it.

Why this room, and this track? Because a governance method earns its standing the way this issue's field note says a link earns scrutiny — by being opened by outsiders. The Dataset/Tool track is where practitioners and researchers take a tool apart: run the scanner, re-code the dataset, find where the method breaks. Submitting the kit there is the deliberate choice to have the instrument checked by people with no stake in it — the same second-coder discipline Issue #12 argued for, applied to the kit itself.

## 5. The Monday Fix — expire one store's immortal links

Forty-five minutes, this Monday — one file store, one link list, one new default:

1. Pick **one file store** — the Dropbox estate from this issue is the natural start, because its links are created by everyone, including, now, its connectors. Export or open the full shared-link list for that store.
2. **Sort by age and open the five oldest links as an outsider** — personal device, logged out, exactly as Section 3's sampling test prescribes. For each: name the project it served, or write "unknown." Any link whose project has ended, whose creator has left, or whose file has since become more sensitive gets **revoked in the meeting, not ticketed for later** — revocation is reversible by re-sharing; an open link is not reversible at all once it has been forwarded.
3. **Set the default that stops the list regrowing**: link expiry on by default for the store (days, not months), and the same rule written into the approval record of every AI connector with file-write access — an agent creating a link follows the human rule, or the capability is switched off for the connector. If the store cannot enforce an expiry default, record that as a known gap with a named owner and a quarterly manual sweep in its place.
4. **File the list**: the exported link list, the five sampled links with their dispositions, and the new default go into the store's approval record, dated. Next quarter's review starts from this file — and its first check is whether the count of "never expires" links has gone down or up.

Score the connector before you trust it — and count the links before you call the estate closed, because the oldest door into your files is rarely a grant anyone remembers approving. This Monday, the link list is the fix.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

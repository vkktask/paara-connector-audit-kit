# The Connector Audit — Issue #19

**Score the connector before you trust it.**

For CIOs, CISOs, CPOs, risk officers and the people who advise them. One connector pattern, one field note, one harness section, one regulator or industry-body update, and one Monday fix — every week.

**Issue #19 headline: The Group Chat Has No Owner — connect an AI to a messaging account and the group chat comes with it: everyone's messages, read by a connection only one member approved, under an owner nobody can name. Plus consent and notice for the bystanders in the data, and an open FTC consultation on impersonation that touches the same problem from the other side.**

---

## 1. The Connector Pattern — the messaging layer joins the estate

This week's pattern to check in your own estate:

Messaging is the store that arrives last and is assessed least, because it does not look like a system. It looks like conversation. The pattern tested in Teardown #26 (WhatsApp Business / WhatsApp → a ChatGPT-style AI assistant): an assistant connected to one person's or one business's messaging account, with read and write reach into the chats on that account. What the pattern actually grants, once an AI can read and write the messaging layer:

- The group chat is a shared store with a single person's grant. A group chat holds every member's messages — written by each of them, for the group. When one member connects an AI to their account, the group's entire history sits inside that one connection's reach. No other member granted anything. Most will never know the connection exists.
- The business number speaks with the business's voice. On a WhatsApp Business account, the chats are customer threads. An assistant that can read them can summarise customers; an assistant that can write in them replies as the business, under the business's name, in a channel customers treat as personal and immediate.
- Sent is sent, and it looks like you. A message an AI sends from an account arrives indistinguishable from one the account holder typed. There is no "sent by an agent" marker in the chat for the other side to see. Whatever the assistant writes — to a colleague, to a group, to a customer — is attributed to the person or the business, by everyone who receives it.

That is a pattern, not a finding about a named product. No vendor score is published here. Check the pattern in your own estate first — the fix is in Section 5.

## 2. Field Note — The Group Chat Has No Owner

Every other store in this series has an owner you can name. The mailbox belongs to someone. The calendar belongs to someone. The file store has an admin. Ask who owns a group chat and the room goes quiet — because the honest answer is: everyone in it, which in practice means no one.

A group chat is created in seconds, by anyone, for a purpose that felt small at the time: the project group, the family group, the leadership group, the customers-and-staff group on the business number. It accumulates the way conversation accumulates — decisions, arguments, jokes, figures, photos, voice notes, the candid version of everything that later gets written up formally somewhere else. Nobody approves its membership changes as a data decision. Nobody sets its retention. Nobody reviews what it contains, because it is not a record in anyone's register. It is just where people talk.

Then one member connects an AI assistant to their account — for a good reason, usually: summarise my chats, draft my replies, never let me miss a customer message. The approval, if there was one, was that one person's approval, for that one person's use case. But the reach is not that one person's data. The reach is the whole group: every member's messages, including the members who left the company, the customers who wrote in confidence, the family members who never heard of the tool. Everyone's messages, nobody's approval. The consent conversation, if it happened at all, happened with exactly the wrong person — the one doing the connecting, not the ones being read.

And when something goes wrong, the ownership gap becomes an accountability gap. Who was supposed to assess this connection? Not the member — they were just using an approved assistant. Not the group — a group cannot assess anything. Not the business whose number it is — the business may not know a personal account in the same thread was connected. The pattern from earlier issues repeats with a new twist: the immortal grant had an owner who forgot; the leaver's token had a process that stopped one step short. The group chat never had the owner or the process in the first place.

Teardown #26 tests this pattern on WhatsApp → a ChatGPT-style AI assistant: read reach across one-to-one chats, group chats and a customer thread, a control chat the account was never part of, write actions including sending to a group, a hidden instruction planted in a dummy message — including one arriving as another person's group message — and the log trail behind it all. It is filmed only on test numbers the tester owns, with dummy chats, and it is not filmed yet; this note claims no result from it. The pattern does not need a result to be worth checking: it follows from the architecture, and the architecture is already connected in most estates.

The lesson for leaders: a group chat your people use for work is a data store, and it needs the two things every other store has — a named owner, and a rule about what may be connected to it. Until both exist, the most candid record in your organisation is governed by whoever connects something to it first.

## 3. Harness — Consent and notice for bystanders: the people in the data who never agreed

Every harness section in this series so far has governed the person who connects the agent: their identity, their scopes, their approvals. This one governs the people who never appear in the approval at all — the **bystanders**: everyone whose data sits inside a connected store because they wrote to it, were added to it, or were mentioned in it, and who never agreed to the connection. The group chat is the pure case, but bystanders exist in every store this series has tested: the attendees in the calendar, the senders in the mailbox, the members of the channel.

**The principle.** Consent collected from the account holder covers the account holder. It does not cover the other people in the data. When a connector's reach extends over other people's messages, events or records, the harness question changes from "did the user agree?" to three separate tests — and an agent that cannot pass them does not get the reach, however clean the account holder's own approval was.

**Test 1 — Reach test: whose data is actually inside the grant?** Before approval, enumerate the bystanders by class, not by name: group members, customers on the business number, external parties, former members whose messages remain. If the approval record cannot say whose data the connection reads, the approval was written for a smaller system than the one being connected. This is believed reach vs actual reach, measured in people instead of tools.

**Test 2 — Notice test: how would a bystander find out?** There must be an answer that does not depend on the bystander asking. Practical forms, in increasing strength: a standing notice in the group's description or the business's profile that AI assistance is in use; a disclosure the first time the assistant acts in a shared space; a marker on AI-sent messages where the platform supports one. "They could check our privacy policy" is not notice to a person in a chat — it is a filing cabinet. If no notice route exists on the platform, that absence goes in the approval record as a known gap, accepted by a named owner — not silently inherited by the bystanders.

**Test 3 — Refusal test: what happens if a bystander objects?** A control that cannot honour an objection is a notice, not a consent. The harness needs a working answer: the chat is excluded from the connection, the assistant's reach is scoped away from shared spaces, or the connection does not proceed for that store. The refusal route is decided before go-live, by the owner — not improvised in the thread, by the person who connected the tool, after the objection lands.

**Where this sits in the gates.** This is the consent gate — G6 in the harness playbook, consent on regulated data — widened from the data subject in the record to every bystander in the store. The scoring discipline is the same as the other gates: it is a gate, not a score. Fail one gate, no score can rescue it. An assistant that reads a hundred people's messages on one person's say-so has not passed a weaker version of the consent test. It has not taken it.

## 4. Regulator / Industry-Body Update — FTC Impersonation Rule ANPRM: an open consultation, comments due 30 November 2026

This week's update is an open consultation, reported at its exact status.

The industry-bodies scan published with this newsletter's work on 16 November 2026 ranked the **US Federal Trade Commission's Impersonation Rule advance notice of proposed rulemaking (ANPRM)** fourth of eleven routes: a **virtual** route — comments are submitted in writing, no travel or attendance involved — with **comments due 30 November 2026**. The scan rated the fit **tangential** for a connector-governance practice, and that rating stands: this is flagged as an open consultation a reader may choose to answer, at that honest distance.

That is the complete, current status: **a consultation identified as open, with a 30 November 2026 comment deadline.** No submission is claimed here — nothing has been sent to the FTC under this newsletter's work, and anything sent will be reported only when it exists, at the same precision as the other entries in this series.

Why does an impersonation consultation belong in an issue about group chats and AI-sent messages? Because the two problems share a seam. The impersonation question regulators are asking — when a message, a voice or a persona is not what it appears to be, who is responsible, and what must be disclosed — is the same question Section 1 raises from inside the estate: an AI-sent message arrives looking exactly like the account holder's own. The bystander in the group chat and the consumer facing an impersonation are in the same position: dealing with a message whose true author they cannot see. A practitioner comment that brings evidence from the connector layer — how these connections actually grant send-as rights, and what disclosure the platforms do and do not support — is the kind of input an ANPRM exists to collect. Tangential fit, real seam. The deadline is 30 November 2026.

## 5. The Monday Fix — give one group chat an owner

Thirty minutes, this Monday:

1. Pick the one work group chat that would worry you most if it were read end to end by a machine — the leadership group, the customer group on the business number, the project group with the candid thread. Write down, in one line, who its members are and what classes of data it holds: decisions, figures, customer details, personal messages.
2. Answer the ownership question in writing: who is the named owner of this chat as a data store? If the honest answer is nobody, appoint one — the person who would be called if the chat's contents surfaced somewhere they should not. An owner who is named after the incident is a scapegoat, not a control.
3. Check what is connected: ask each member — starting with yourself — whether any AI assistant, summariser or agent is connected to an account that can read this chat, and whether it can send into it. Record the answers, including the "I don't know"s. One member's connection is the whole group's exposure.
4. Set the two rules and write them where members will see them — in the group description itself: (a) no AI connection reads or sends in this chat without the owner's approval, and (b) if an approved assistant is in use, the group is told, in the chat, before it acts. Then note the review date. Group membership changes quietly; the rules have to be re-stated when the group changes, or they govern a group that no longer exists.

You cannot govern a store nobody owns. Own one chat on Monday, and the most candid record in the building has a name next to it for the first time.

---

*The Connector Audit is by Vivek Kumar, creator of PAARA (Privacy-Aware AI Risk Architecture, 6–8 components). The connector-audit kit, the 13-connector dataset, the checklist and the DPIA template are open source: https://github.com/vkktask/paara-connector-audit-kit*

*Subscribe: email vkktaskusa@gmail.com. Not legal advice.*

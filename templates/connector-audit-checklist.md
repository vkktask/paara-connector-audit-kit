# Connector Audit Checklist (PAARA)

Use this checklist for every connector before it is enabled. Record a verbatim evidence snippet (≤ 25 words) and its URL for every field that is not "not documented". A fact is never coded from prior knowledge.

## 1. Inventory and scope

- [ ] Connector name, vendor, version / endpoint
- [ ] What systems and data categories can it reach?
- [ ] Under whose authority does it act — individual user, service account, agent key, or none?
- [ ] Which users / groups / tenants can enable it, and who approves that?
- [ ] Data residency and retention for data passing through the connector

## 2. Permission register (OAuth / Graph)

- [ ] Scopes / permissions requested, listed individually
- [ ] Delegated (user-bound) vs application (non-user-bound) permissions
- [ ] Resource-specific consent available? (yes / no / not documented)
- [ ] Least-privilege alternative documented (read-only scopes, read-only endpoint, admin-selected tools)?

## 3. Factor coding (F1–F7)

Code each factor Y / N / U from official documentation only.

| Factor | Code | Evidence snippet (≤ 25 words) | Source URL |
|--------|------|-------------------------------|------------|
| F1 Sensitive data | | | |
| F2 Aggregation | | | |
| F3 Credential | | | |
| F4 Logging | | | |
| F5 Injection | | | |
| F6 Sharing | | | |
| F7 Action | | | |

**Coding rules:** F1 — names personal, financial, private-communication, or security data as reachable. F2 — reach across more than one separately administered system. F3 — app-level, service-account, shared, or agent keys, or no authentication. F4 — server-side retrieval or audit logging stated absent (N when documented; U when silent). F5 — retrieval of content authored by parties other than the user. F6 — outbound sharing, sending, or requests to arbitrary hosts. F7 — write, send, delete, or other state-changing tools.

## 4. Scoring

- **Critical** — F7 and any of F1, F3, F4
- **High** — F7, or two or more of F1–F5
- **Moderate** — one High factor, or multiple Medium factors
- **Low** — otherwise

Score twice: **lower bound** (U = N) and **upper bound** (U = Y). If a documented write-limiting control exists, score the restricted configuration (F7 = N) as well.

- Default score (lower → upper): ____ → ____
- Restricted score (lower → upper): ____ → ____
- Deployment decision: Approve / Restrict / Defer pending full assessment

## 5. Retrieval boundary and prompt-injection threat model

- [ ] What third-party-authored content can the connector retrieve?
- [ ] Is there documented prompt-injection guidance or defence? (yes / no / not documented)
- [ ] Can retrieved content trigger tool calls without user confirmation?
- [ ] Is tool approval / human confirmation available and enforced?

## 6. Insider-risk amplification

- [ ] What can a single compromised account reach or do through this connector that it could not do without it?
- [ ] Are non-user-bound credentials available, and can they be disabled?
- [ ] Is there a per-user, per-group, or per-tenant disable path?

## 7. Cryptographic-dependency register

Record each dependency, or "not documented — owned unknown" if the vendor does not state it.

| Dependency | Value / algorithm | Source URL |
|------------|-------------------|------------|
| Token signature | | |
| Transport (TLS version, key exchange) | | |
| At-rest encryption and key wrapping | | |
| Post-quantum / hybrid support | | |

## 8. Open items (every U becomes one)

| Undocumented factor / question | Owner | Review date | Status |
|-------------------------------|-------|-------------|--------|
| | | | |

## 9. Vendor attestation questions

Send before approval if any item above is undocumented:

1. Is every retrieval and tool call logged server-side, and can logs be exported?
2. Which operations can be disabled per user, group, or tenant?
3. Is a read-only mode enforced server-side?
4. Which credential types are supported, and can non-user-bound credentials be disabled?
5. What documented defences exist against prompt injection in retrieved content?
6. What TLS versions and key-exchange groups are supported?
7. What algorithm signs access tokens?
8. Is hybrid post-quantum key exchange or signing available, and when?
9. How is data encrypted at rest, and how are keys wrapped?
10. What changes trigger customer notification?

Unanswered questions are recorded as open items with an owner — see section 8.

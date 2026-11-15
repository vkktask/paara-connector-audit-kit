# Connector-Layer Data Protection Impact Assessment (DPIA) Template

A connector-specific DPIA template, prepared under the PAARA methodology (Privacy-Aware AI Risk Architecture, SSRN DOI 10.2139/ssrn.6784078). Complete one per connector. This template is a practitioner aid, not legal advice; have your Data Protection Officer and counsel review it before use.

## 1. Connector identification

| Field | Entry |
|-------|-------|
| Connector name and vendor | |
| Version / endpoint | |
| Business purpose | |
| Data controller / processor roles | |
| DPIA owner | |
| Date / review date | |

## 2. Scope and data mapping

- Systems and data categories reachable:
- Categories of personal data (including special-category data, if any):
- Data subjects affected:
- Volume and frequency of access:
- Data residency / transfers (including any cross-border transfer):

## 3. WP29 nine criteria at the connector layer

Apply each of the Article 29 Working Party nine criteria for high-risk processing to this connector. Mark each as applies / does not apply / not yet determined, with a short reason.

| # | WP29 criterion | Applies? | Reason |
|---|----------------|----------|--------|
| 1 | Evaluation or scoring | | |
| 2 | Automated decision-making with legal or similar significant effect | | |
| 3 | Systematic monitoring | | |
| 4 | Sensitive data or data of a highly personal nature | | |
| 5 | Data processed on a large scale | | |
| 6 | Matching or combining datasets | | |
| 7 | Data concerning vulnerable data subjects | | |
| 8 | Innovative use or applying new technological or organisational solutions | | |
| 9 | Processing that prevents data subjects from exercising a right or using a service or contract | | |

Two or more criteria applying indicates processing likely to result in high risk, and a DPIA is required under GDPR Article 35.

## 4. OAuth and Graph permission risk register

| Permission / scope | Type (delegated / application) | Data it reaches | Justification | Least-privilege alternative |
|--------------------|-------------------------------|-----------------|---------------|-----------------------------|
| | | | | |

## 5. Retrieval-boundary and prompt-injection assessment

- Third-party-authored content the connector can retrieve:
- Injection paths (retrieved content, tool outputs, shared documents):
- Documented vendor defences:
- Human-approval / tool-approval controls:

## 6. Insider-risk amplification

- What a single compromised account can reach or do through this connector:
- Non-user-bound credentials in use:
- Controls limiting blast radius:

## 7. PAARA risk score

Attach the completed audit checklist (`connector-audit-checklist.md`).

- Factor codes (F1–F7):
- Default score (lower → upper):
- Restricted score (lower → upper):
- Deployment decision: Approve / Restrict / Defer pending full assessment

## 8. Cryptographic dependencies

| Dependency | Value / algorithm | Source |
|------------|-------------------|--------|
| Token signature | | |
| Transport (TLS version, key exchange) | | |
| At-rest encryption and key wrapping | | |
| Post-quantum / hybrid support | | |

Undocumented dependencies are recorded as owned unknowns, with an owner and a review date.

## 9. Necessity, proportionality, and measures

- Why this connector (and these permissions) is necessary for the stated purpose:
- Less intrusive alternatives considered:
- Technical measures (read-only mode, scope restriction, approval workflows, logging):
- Organisational measures (owner, review cadence, vendor attestation):

## 10. Residual risk and sign-off

| Risk | Likelihood | Impact | Mitigation | Residual risk |
|------|-----------|--------|------------|---------------|
| | | | | |

- DPO consulted (name / date):
- Residual risk accepted by (name / role / date):
- Next review date:

## 11. Cross-framework alignment

Record how this assessment maps to each framework, where applicable:

- GDPR Article 35:
- EU AI Act Article 27:
- ISO/IEC 42005:2025:
- NIST AI 600-1 (Generative AI Profile):

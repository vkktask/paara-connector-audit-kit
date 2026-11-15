# Contributing

## Re-coding (most valuable)

The 13-connector audit was coded by a single coder with no inter-rater reliability reported. Independent re-coding is the single most valuable contribution.

1. Pick a connector from `audit/13-connector-audit.md`.
2. Re-code F1–F7 from the vendor's official documentation only, recording a verbatim evidence snippet (≤ 25 words) and URL for every coded field.
3. Open an issue or pull request with your codes, your evidence, and where they differ from `audit/coding-sheet.csv`.
4. If you disagree on a factor definition, say so explicitly — several codes involve judgement, and the definitions are the paper's operationalisation of PAARA, not part of its published text.

## Extending the corpus

To add a connector:

- Use only official public documentation, retrieved in full, and record the retrieval date.
- Code F1–F7 with evidence snippets and URLs, score under both bounding assumptions, and score the restricted configuration if a documented write-limiting control exists.
- Add a row to `audit/coding-sheet.csv` and a section to `audit/13-connector-audit.md`, and update the prevalence counts.

## What not to contribute

- Do not add claims about patent filings, regulator adoption, or government use unless you can cite a primary source (a patent office record, a regulator publication). The SSRN paper's statement about May 2026 regulatory submissions is corroborated only from the paper itself, and the repository states that plainly.
- Do not add vendor behaviour claims (e.g. "this control is not enforced") without a reproducible test.

## Reporting issues

Open an issue with the connector, the factor, the documentation URL, and the verbatim snippet that supports your reading.

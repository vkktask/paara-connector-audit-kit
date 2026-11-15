"""Keyword triage of connector documentation into PAARA factor codes.

This is a *triage aid*, not a coder. It scans documentation / config
text for evidence phrases per factor and returns Y / N / U codes with
the verbatim evidence snippet for each code, so a human coder can
verify every code against the checklist in ``templates/``.

Rules:
- A factor is Y only when a positive evidence phrase is found.
- A factor is N only when an explicit absence phrase is found
  (e.g. "audit logging is documented" for F4, "read-only" for F7).
- Otherwise the factor is U — undocumented, not absent.
- Negative phrases take precedence over positive ones in the same
  document (e.g. "no personal data is accessed" beats "personal data").

Confidence is deliberately coarse: "high" when an explicit phrase
matches, "low" when only a weak keyword matches, "none" when U.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .models import FACTOR_LABELS, Factor, FactorCode

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?\n])\s+")


@dataclass
class FactorEvidence:
    factor: Factor
    code: FactorCode
    evidence: str = ""
    confidence: str = "none"

    def as_dict(self) -> dict:
        return {
            "factor": self.factor.value,
            "label": FACTOR_LABELS[self.factor],
            "code": self.code.value,
            "evidence": self.evidence,
            "confidence": self.confidence,
        }


# Positive phrases: documentation states the factor is present.
# Negative phrases: documentation states it is absent.
# Each entry: (regex, confidence, matched-is-negative?)
_PATTERNS: dict[Factor, dict[str, list[tuple[str, str]]]] = {
    Factor.F1: {
        "positive": [
            (r"personal data", "high"),
            (r"private channel", "high"),
            (r"direct message", "high"),
            (r"financial data|payment (?:data|information)|credit card", "high"),
            (r"health (?:data|information|records?)", "high"),
            (r"email (?:content|messages?|data)", "high"),
            (r"user profile|profile email", "high"),
            (r"sensitive data", "high"),
            (r"password|secret|credential", "low"),
        ],
        "negative": [
            (r"no personal data|does not (?:access|collect|read) (?:any )?personal", "high"),
            (r"no sensitive data", "high"),
        ],
    },
    Factor.F2: {
        "positive": [
            (r"across (?:multiple|several|different) (?:systems?|services?|platforms?)", "high"),
            (r"cross-system|multi-system", "high"),
            (r"aggregat(?:e|ion) (?:across|from)", "high"),
            (r"multiple (?:systems?|services?|accounts?)", "low"),
        ],
        "negative": [
            (r"single (?:system|service|account) only", "high"),
        ],
    },
    Factor.F3: {
        "positive": [
            (r"service account", "high"),
            (r"application permission|app-level|app-only", "high"),
            (r"agent (?:api )?key", "high"),
            (r"shared (?:key|credential|token)", "high"),
            (r"no authentication|without authentication", "high"),
            (r"api key", "low"),
        ],
        "negative": [
            (r"user (?:token|delegated|consent)|delegated permission", "high"),
            (r"on behalf of the user", "low"),
        ],
    },
    Factor.F4: {
        # F4 is inverted: Y = logging is ABSENT, N = logging is documented.
        "positive": [  # logging absent
            (r"no (?:server-side )?(?:audit )?log(?:ging|s)? (?:is )?(?:available|provided|recorded)", "high"),
            (r"log(?:ging|s)? (?:is )?not (?:available|provided|recorded|supported)", "high"),
        ],
        "negative": [  # logging documented -> code N
            (r"audit log(?:ging|s)?[^.]{0,50}documented", "high"),
            (r"audit log(?:ging|s)? (?:is )?(?:documented|available|recorded|provided)", "high"),
            (r"server-side (?:audit )?log(?:ging|s)?", "high"),
            (r"tool-call log(?:ging|s)?", "high"),
            (r"log(?:ging|s)? (?:is )?documented", "low"),
        ],
    },
    Factor.F5: {
        "positive": [
            (r"retriev(?:e|es|al) (?:of )?(?:content|data|information|messages?) (?:from|authored by|created by)", "high"),
            (r"third-part(?:y|ies) content", "high"),
            (r"(?:content|messages?|data|information|documents?) (?:are |is )?authored by (?:other|third|another)", "high"),
            (r"authored by (?:other|third|another) (?:people|parties|users?)", "high"),
            (r"untrusted content|external content", "high"),
            (r"fetch(?:es|ing)? (?:a |an |the )?(?:url|web|page|content)", "low"),
            (r"read(?:s|ing)? (?:files?|messages?|documents?|emails?)", "low"),
        ],
        "negative": [
            (r"only user-authored content|only (?:the )?user'?s own content", "high"),
        ],
    },
    Factor.F6: {
        "positive": [
            (r"send(?:s|ing)? (?:messages?|data|requests?|to)", "high"),
            (r"shar(?:e|es|ing) (?:with|to|data)", "high"),
            (r"outbound (?:request|call|sharing|transfer)", "high"),
            (r"external host|arbitrary (?:host|url)", "high"),
            (r"post (?:a )?message", "low"),
        ],
        "negative": [
            (r"read-only|no outbound|does not send", "high"),
        ],
    },
    Factor.F7: {
        "positive": [
            (r"write (?:access|tool|operation|capabilit)", "high"),
            (r"create|delete|update (?:a |an |the )?(?:record|file|issue|message|resource)", "high"),
            (r"state-changing|mutat(?:e|ing|ion)", "high"),
            (r"execute (?:a |an |the )?(?:command|code|tool)", "high"),
            (r"write tool", "high"),
        ],
        "negative": [
            (r"read-only (?:mode|scope|endpoint|flag)", "high"),
            (r"no write (?:access|capabilit|tool)", "high"),
        ],
    },
}


def _snippet(text: str, match: re.Match) -> str:
    """Return the sentence containing the match, capped at 25 words."""
    sentences = _SENTENCE_SPLIT.split(text)
    for sentence in sentences:
        if match.group(0).lower() in sentence.lower():
            words = sentence.strip().split()
            snippet = " ".join(words[:25])
            return snippet + (" …" if len(words) > 25 else "")
    start = max(0, match.start() - 60)
    return text[start : match.end() + 60].strip()


def triage_text(text: str) -> dict[Factor, FactorEvidence]:
    """Code all seven factors from free text. Never invents evidence."""
    results: dict[Factor, FactorEvidence] = {}
    for factor in Factor:
        groups = _PATTERNS[factor]
        # Negative (absence) phrases win over positive ones.
        for pattern, confidence in groups["negative"]:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                # F4 is inverted: "logging documented" -> N, which is
                # exactly what a negative match means here. For other
                # factors a negative match also means N.
                results[factor] = FactorEvidence(
                    factor, FactorCode.NO, _snippet(text, match), confidence
                )
                break
        else:
            for pattern, confidence in groups["positive"]:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    results[factor] = FactorEvidence(
                        factor, FactorCode.YES, _snippet(text, match), confidence
                    )
                    break
            else:
                results[factor] = FactorEvidence(factor, FactorCode.UNKNOWN)
    return results


def triage_codes(text: str) -> dict[Factor, FactorCode]:
    return {f: ev.code for f, ev in triage_text(text).items()}

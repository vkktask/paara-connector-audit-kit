"""PAARA connector-audit scanner.

Implements the PAARA seven-factor scoring rule from the PAARA
Connector Audit Kit (see README.md in the repository root):

    F1 sensitive-data reach
    F2 cross-system aggregation
    F3 non-user-bound credentials
    F4 absent logging
    F5 prompt-injection exposure
    F6 external sharing
    F7 agentic action capability

Each factor is coded Y (documented present), N (documented absent) or
U (undocumented). Scores are always reported as a band — lower bound
(U treated as N) to upper bound (U treated as Y) — because U is not
evidence of absence.

Usage (from the repository root)::

    python -m paara_scanner audit
    python -m paara_scanner score --factors UNUUYNY --name "MCP Filesystem"
    python -m paara_scanner scan --docs docs/ --name "My Connector"
"""

from .models import Connector, Factor, FactorCode, ScoreLevel, ScoreResult
from .scoring import score_connector, score_single

__all__ = [
    "Connector",
    "Factor",
    "FactorCode",
    "ScoreLevel",
    "ScoreResult",
    "score_connector",
    "score_single",
]

__version__ = "0.1.0"

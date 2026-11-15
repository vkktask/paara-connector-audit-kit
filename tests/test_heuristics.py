"""Tests for the documentation triage heuristics."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from paara_scanner.heuristics import triage_codes, triage_text  # noqa: E402
from paara_scanner.models import Factor, FactorCode  # noqa: E402

SLACK_LIKE = (
    "Private channels, direct messages and user profile emails are reachable. "
    "Calls run on user tokens through a registered app. "
    "Audit logging for MCP activity is documented. "
    "Retrieved messages are authored by other people. "
    "Messages can be sent to a channel. Write tools exist to post a message."
)

STRIPE_LIKE = (
    "Agent API keys give independent, persistent access. "
    "Audit logging is documented and tool-call logging is available. "
    "Be cautious with other servers; enable tool approval."
)


class TestTriage(unittest.TestCase):
    def test_slack_like_doc(self):
        codes = triage_codes(SLACK_LIKE)
        self.assertEqual(codes[Factor.F1], FactorCode.YES)  # private channels / DMs
        self.assertEqual(codes[Factor.F4], FactorCode.NO)  # logging documented
        self.assertEqual(codes[Factor.F5], FactorCode.YES)  # authored by others
        self.assertEqual(codes[Factor.F7], FactorCode.YES)  # write tools

    def test_stripe_like_doc(self):
        codes = triage_codes(STRIPE_LIKE)
        self.assertEqual(codes[Factor.F3], FactorCode.YES)  # agent API keys
        self.assertEqual(codes[Factor.F4], FactorCode.NO)  # logging documented

    def test_empty_doc_is_all_unknown(self):
        codes = triage_codes("")
        self.assertTrue(all(c is FactorCode.UNKNOWN for c in codes.values()))

    def test_negative_beats_positive(self):
        codes = triage_codes(
            "This connector accesses personal data. "
            "No personal data is accessed by this connector."
        )
        # The explicit absence phrase wins for F1.
        self.assertEqual(codes[Factor.F1], FactorCode.NO)

    def test_read_only_means_no_write(self):
        codes = triage_codes("This deployment is read-only mode with read-only scopes.")
        self.assertEqual(codes[Factor.F7], FactorCode.NO)

    def test_evidence_snippet_is_verbatim(self):
        evidence = triage_text(SLACK_LIKE)
        self.assertIn("private channels", evidence[Factor.F1].evidence.lower())
        self.assertEqual(evidence[Factor.F1].confidence, "high")


if __name__ == "__main__":
    unittest.main()

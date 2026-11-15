"""Tests for the PAARA scoring rule.

The core test reproduces all 13 connectors' published default and
restricted bands from audit/coding-sheet.csv. If the rule drifts
from the published audit, these tests fail.
"""

import csv
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from paara_scanner.io import load_coding_sheet  # noqa: E402
from paara_scanner.models import Connector, Factor, FactorCode, ScoreLevel  # noqa: E402
from paara_scanner.scoring import score_connector, score_single  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "audit" / "coding-sheet.csv"

SHORT = {
    ScoreLevel.LOW: "Low",
    ScoreLevel.MODERATE: "Mod",
    ScoreLevel.HIGH: "High",
    ScoreLevel.CRITICAL: "Crit",
}


def _resolved(code_string: str) -> dict:
    return {
        factor: code == "Y"
        for factor, code in zip(Factor, code_string)
    }


class TestScoringRule(unittest.TestCase):
    def test_critical_needs_f7_plus_f1_f3_or_f4(self):
        self.assertEqual(score_single(_resolved("YNNNYNY"))[0], ScoreLevel.CRITICAL)  # F7+F1
        self.assertEqual(score_single(_resolved("NNYNNNY"))[0], ScoreLevel.CRITICAL)  # F7+F3
        self.assertEqual(score_single(_resolved("NNNYNNY"))[0], ScoreLevel.CRITICAL)  # F7+F4
        self.assertEqual(score_single(_resolved("NNNNYNY"))[0], ScoreLevel.HIGH)  # F7 only

    def test_high_from_two_high_factors_without_f7(self):
        self.assertEqual(score_single(_resolved("YYNNNNN"))[0], ScoreLevel.HIGH)
        self.assertEqual(score_single(_resolved("NNNNYNN"))[0], ScoreLevel.MODERATE)  # one only

    def test_moderate_from_one_high_factor(self):
        self.assertEqual(score_single(_resolved("NNNNYNN"))[0], ScoreLevel.MODERATE)

    def test_low_when_nothing_present(self):
        self.assertEqual(score_single(_resolved("NNNNNNN"))[0], ScoreLevel.LOW)
        # Lone F6 (only Medium factor) does not reach Moderate.
        self.assertEqual(score_single(_resolved("NNNNNYN"))[0], ScoreLevel.LOW)

    def test_invalid_code_string(self):
        with self.assertRaises(ValueError):
            Connector.from_code_string("Bad", "XYZ")
        with self.assertRaises(ValueError):
            Connector.from_code_string("Bad", "YYYY")


class TestPublishedAuditReproduction(unittest.TestCase):
    def test_all_13_connectors_reproduce_published_bands(self):
        connectors = load_coding_sheet(CSV_PATH)
        self.assertEqual(len(connectors), 13)
        for connector in connectors:
            with self.subTest(connector=connector.name):
                result = score_connector(connector)
                self.assertEqual(
                    (SHORT[result.lower], SHORT[result.upper]),
                    tuple(connector.expected_default),
                    f"{connector.name} default band",
                )
                if connector.has_write_limiting_control:
                    self.assertEqual(
                        (SHORT[result.restricted_lower], SHORT[result.restricted_upper]),
                        tuple(connector.expected_restricted),
                        f"{connector.name} restricted band",
                    )
                else:
                    self.assertIsNone(result.restricted_band)

    def test_headline_counts(self):
        connectors = load_coding_sheet(CSV_PATH)
        results = [score_connector(c) for c in connectors]
        crit_lower = sum(1 for r in results if r.lower is ScoreLevel.CRITICAL)
        crit_upper = sum(1 for r in results if r.upper is ScoreLevel.CRITICAL)
        self.assertEqual(crit_lower, 9)
        self.assertEqual(crit_upper, 12)
        self.assertTrue(all(r.upper is not ScoreLevel.LOW for r in results))

    def test_slack_worked_example(self):
        connector = Connector.from_code_string(
            "Slack MCP", "YNNNYYY", has_write_limiting_control=True
        )
        result = score_connector(connector)
        self.assertEqual(result.band, "Critical -> Critical")
        self.assertEqual(result.restricted_band, "High -> High")


if __name__ == "__main__":
    unittest.main()

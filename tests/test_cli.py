"""Tests for the CLI (subprocess, end to end)."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str) -> subprocess.CompletedProcess:
    env = {"PYTHONPATH": str(REPO_ROOT / "src"), "PATH": "/usr/bin:/bin"}
    return subprocess.run(
        [sys.executable, "-m", "paara_scanner", *args],
        capture_output=True, text=True, env=env, cwd=REPO_ROOT,
    )


class TestCLI(unittest.TestCase):
    def test_audit_table_reproduces_counts(self):
        proc = run_cli("audit")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("MCP Filesystem", proc.stdout)
        self.assertIn("Critical: 9 (lower) / 12 (upper)", proc.stdout)

    def test_audit_json(self):
        proc = run_cli("audit", "--format", "json")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(len(data), 13)
        slack = next(d for d in data if d["name"] == "Slack MCP")
        self.assertEqual(slack["band"], "Critical -> Critical")
        self.assertEqual(slack["restricted_band"], "High -> High")

    def test_check_passes(self):
        proc = run_cli("check")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("OK: all 13 connectors", proc.stdout)

    def test_score_code_string(self):
        proc = run_cli("score", "--name", "MCP Filesystem", "--factors", "UNUUYNY")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("High -> Critical", proc.stdout)
        self.assertIn("Defer", proc.stdout)

    def test_score_restricted(self):
        proc = run_cli("score", "--name", "Slack MCP", "--factors", "YNNNYYY", "--restricted")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Restricted: High -> High", proc.stdout)

    def test_scan_doc(self, tmp_path=None):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "connector.md"
            doc.write_text(
                "Private channels and direct messages are reachable. "
                "Audit logging is documented. Write tools exist.",
                encoding="utf-8",
            )
            proc = run_cli("scan", "--docs", tmp, "--name", "Test Connector")
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("triage", proc.stdout)
            self.assertIn("F1 Y", proc.stdout)


if __name__ == "__main__":
    unittest.main()

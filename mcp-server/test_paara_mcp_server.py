#!/usr/bin/env python3
"""End-to-end tests for paara_mcp_server.py (stdlib only).

1. Replica parity: the server's local scoring replica must reproduce the
   published bands in data/coding-sheet.csv for all 13 connectors.
2. Protocol: start the server as a subprocess, do the MCP handshake
   (initialize + notifications/initialized), ping, tools/list, and call
   each tool, asserting the published bands for Slack, Stripe and GitHub.

Run: python3 test_paara_mcp_server.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import paara_mcp_server as server  # noqa: E402

FAILURES = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}" + (f" — {detail}" if detail and not condition else ""))
    if not condition:
        FAILURES.append(label)


# --- 1. Replica parity over all 13 published connectors --------------------

for row in server.DATASET:
    restricted = row["published_restricted_lower"] is not None
    scored = server.score_codes_local(row["codes"], restricted)
    ok = (
        scored["default_lower"] == row["published_default_lower"]
        and scored["default_upper"] == row["published_default_upper"]
        and scored["restricted_lower"] == row["published_restricted_lower"]
        and scored["restricted_upper"] == row["published_restricted_upper"]
    )
    check(
        f"replica parity: {row['name']}",
        ok,
        f"got {scored['default_lower']}->{scored['default_upper']} "
        f"restricted {scored['restricted_lower']}->{scored['restricted_upper']}, "
        f"published {row['published_default_lower']}->{row['published_default_upper']} "
        f"restricted {row['published_restricted_lower']}->{row['published_restricted_upper']}",
    )

# --- 2. Live MCP protocol session over stdio --------------------------------

proc = subprocess.Popen(
    [sys.executable, str(HERE / "paara_mcp_server.py")],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)
_next_id = 0


def send(message: dict) -> dict | None:
    proc.stdin.write(json.dumps(message) + "\n")
    proc.stdin.flush()
    if "id" not in message:  # notification: no response
        return None
    return json.loads(proc.stdout.readline())


def request(method: str, params: dict | None = None) -> dict:
    global _next_id
    _next_id += 1
    return send({"jsonrpc": "2.0", "id": _next_id, "method": method, "params": params or {}})


def call_tool(name: str, arguments: dict) -> dict:
    resp = request("tools/call", {"name": name, "arguments": arguments})
    assert "result" in resp, f"tools/call {name} failed: {resp}"
    return json.loads(resp["result"]["content"][0]["text"])


try:
    init = request(
        "initialize",
        {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "paara-test-client", "version": "0.1"},
        },
    )
    check(
        "initialize handshake",
        init["result"]["serverInfo"]["name"] == "paara-connector-audit"
        and init["result"]["protocolVersion"] == "2025-03-26",
        str(init),
    )
    send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    pong = request("ping")
    check("ping", pong.get("result") == {}, str(pong))

    tools = request("tools/list")["result"]["tools"]
    tool_names = sorted(t["name"] for t in tools)
    check(
        "tools/list",
        tool_names == ["list_connectors", "lookup_connector", "score_connector"],
        str(tool_names),
    )

    # TDQS metadata: annotations, full input descriptions, output schemas
    for t in tools:
        ann = t.get("annotations") or {}
        check(
            f"annotations: {t['name']}",
            ann.get("readOnlyHint") is True
            and ann.get("destructiveHint") is False
            and ann.get("idempotentHint") is True
            and ann.get("openWorldHint") is False,
            str(ann),
        )
        props = t["inputSchema"].get("properties", {})
        check(
            f"input descriptions: {t['name']}",
            all(p.get("description") for p in props.values()),
            str([k for k, p in props.items() if not p.get("description")]),
        )
        check(
            f"outputSchema: {t['name']}",
            t.get("outputSchema", {}).get("type") == "object"
            and bool(t["outputSchema"].get("properties")),
            str(t.get("outputSchema")),
        )

    listing = call_tool("list_connectors", {})
    check("list_connectors count", listing["count"] == 13, str(listing["count"]))
    by_name = {c["name"]: c for c in listing["connectors"]}
    check(
        "list_connectors Slack band",
        by_name["Slack MCP"]["default_lower"] == "Critical"
        and by_name["Slack MCP"]["default_upper"] == "Critical",
        str(by_name.get("Slack MCP")),
    )
    check(
        "list_connectors self-describing",
        listing["factors"][0]["name"] == "Sensitive-data reach"
        and listing["factors"][6]["name"] == "Agentic action capability"
        and listing["band_meanings"]["Critical"].startswith("Agentic")
        and listing["connectors"][0]["codes"]["F1"] == "U",
        str(listing.get("factors")),
    )

    # Slack MCP: Y N N N Y Y Y -> Critical/Critical, restricted High/High
    slack = call_tool("lookup_connector", {"name": "slack"})
    check(
        "lookup_connector Slack",
        slack["found"]
        and slack["name"] == "Slack MCP"
        and slack["code_string"] == "YNNNYYY"
        and slack["default_lower"] == "Critical"
        and slack["default_upper"] == "Critical"
        and slack["restricted_lower"] == "High"
        and slack["restricted_upper"] == "High"
        and slack["published_bands_match"],
        str(slack),
    )
    check(
        "lookup_connector self-describing factors",
        slack["factors"][0] == {
            "factor": "F1",
            "name": "Sensitive-data reach",
            "weight": "High",
            "code": "Y",
            "code_meaning": "documented present",
        }
        and slack["factors"][6]["name"] == "Agentic action capability"
        and set(slack["band_meanings"]) == {"Low", "Moderate", "High", "Critical"},
        str(slack.get("factors")),
    )

    # Stripe MCP: Y N Y N Y Y Y -> Critical/Critical, no restricted band
    stripe = call_tool("lookup_connector", {"name": "Stripe MCP"})
    check(
        "lookup_connector Stripe",
        stripe["found"]
        and stripe["code_string"] == "YNYNYYY"
        and stripe["default_lower"] == "Critical"
        and stripe["default_upper"] == "Critical"
        and stripe["restricted_lower"] is None
        and stripe["published_bands_match"],
        str(stripe),
    )

    # Score Stripe's codes from scratch (no restricted control documented)
    scored = call_tool(
        "score_connector",
        {"name": "Stripe-like", "F1": "Y", "F2": "N", "F3": "Y", "F4": "N",
         "F5": "Y", "F6": "Y", "F7": "Y"},
    )
    check(
        "score_connector Stripe codes",
        scored["default_lower"] == "Critical" and scored["default_upper"] == "Critical"
        and scored["restricted_lower"] is None,
        str(scored),
    )
    check(
        "score_connector self-describing",
        scored["factors"][2]["name"] == "Non-user-bound credentials"
        and scored["factors"][2]["code"] == "Y"
        and set(scored["band_meanings"]) == {"Low", "Moderate", "High", "Critical"},
        str(scored.get("factors")),
    )

    # Score Slack's codes with the write-limiting control applied
    scored_r = call_tool(
        "score_connector",
        {"name": "Slack-like", "F1": "Y", "F2": "N", "F3": "N", "F4": "N",
         "F5": "Y", "F6": "Y", "F7": "Y", "restricted": True},
    )
    check(
        "score_connector Slack codes restricted",
        scored_r["default_lower"] == "Critical"
        and scored_r["restricted_lower"] == "High"
        and scored_r["restricted_upper"] == "High",
        str(scored_r),
    )

    # A low-risk profile: all N except a lone F6 -> Low/Low
    low = call_tool(
        "score_connector",
        {"F1": "N", "F2": "N", "F3": "N", "F4": "N", "F5": "N", "F6": "Y", "F7": "N"},
    )
    check(
        "score_connector low profile",
        low["default_lower"] == "Low" and low["default_upper"] == "Low",
        str(low),
    )

    # Fuzzy lookup + unknown connector behaviour
    fuzzy = call_tool("lookup_connector", {"name": "graph"})
    check("lookup_connector fuzzy 'graph'", fuzzy["found"] and fuzzy["name"] == "MS Graph perms.", str(fuzzy))
    missing = call_tool("lookup_connector", {"name": "zzz-no-such-connector-qqq"})
    check("lookup_connector unknown", missing["found"] is False, str(missing))

    # Invalid factor code returns a tool error, not a crash
    bad = request("tools/call", {"name": "score_connector", "arguments": {"F1": "X"}})
    check("score_connector invalid code isError", bad["result"].get("isError") is True, str(bad))
finally:
    proc.stdin.close()
    proc.wait(timeout=10)

print()
if FAILURES:
    print(f"{len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("ALL TESTS PASSED")

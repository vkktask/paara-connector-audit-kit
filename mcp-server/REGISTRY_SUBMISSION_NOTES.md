# Registry submission notes — PAARA Connector Audit MCP server

Checked against the registries' public documentation on 17 Nov 2026.
The server itself is **done and tested** (`python3 test_paara_mcp_server.py`
— all checks pass). What remains for every registry is *distribution*
steps that need Vivek's accounts, listed honestly per registry below.

**One shared blocker first:** this folder is local only. Every route
below needs the server code in the public GitHub repo
(https://github.com/vkktask/paara-connector-audit-kit — e.g. committed
under an `mcp-server/` folder, or its own repo) before anything can be
submitted.

---

## 1. Official MCP Registry (registry.modelcontextprotocol.io)

The registry hosts **metadata only** — a `server.json` that points at a
package users install from a package registry (npm, PyPI, …). It is
still in preview (data resets are possible before GA).

**Ready here:** `server.json` (draft) — name
`io.github.vkktask/paara-connector-audit`, version `1.2.1`, description
within the 100-character limit, one PyPI package entry, stdio transport.
This README already carries the PyPI ownership marker the registry
checks for: `mcp-name: io.github.vkktask/paara-connector-audit`.

**Exact steps:**
1. Package this server for PyPI (a small `pyproject.toml` shipping
   `paara_mcp_server.py` + `data/coding-sheet.csv`, with this README as
   the package description so the `mcp-name:` line is on the PyPI page)
   and publish version `1.2.1` to PyPI. The registry verifies the
   package exists at the version named in `server.json`.
2. Install the publisher CLI: `brew install mcp-publisher` (or the
   prebuilt binary from the registry's GitHub releases).
3. `mcp-publisher validate` — checks `server.json` against the schema.
4. `mcp-publisher login github` — the `io.github.vkktask/*` namespace
   is proved by GitHub OAuth (account: vkktask).
5. `mcp-publisher publish`.

**Blockers:** (a) no PyPI package exists yet — needs the packaging step
plus Vivek's PyPI account; (b) the code must be in the GitHub repo
first (the `repository` field points at the kit repo). No fee, no human
review. Bonus: Glama and other directories import from this registry,
so this listing seeds the others.

## 2. Glama (glama.ai)

Glama lists open-source MCP servers from their GitHub repositories and
also imports servers from the official MCP Registry.

**Ready here:** `glama.json` — note what it actually does: it only
names the GitHub users allowed to maintain the listing
(`maintainers: ["vkktask"]`). It does **not** create or claim a listing
by itself.

**Exact steps:**
1. Get this folder into the public GitHub repo (shared blocker above),
   with `glama.json` at the repo root (or the server subfolder's root,
   per Glama's repo scan).
2. On glama.ai → MCP servers → **Add MCP Server**: submit the GitHub
   repository URL, a display name ("PAARA Connector Audit") and the
   short description. Glama runs automated checks (licence detection,
   security scan, health test); most submissions are indexed
   automatically within minutes. For a from-source stdio server, Glama
   may ask for a build spec / Dockerfile in its admin UI — if it does,
   a two-line Dockerfile (`FROM python:3.12-slim`, copy the folder,
   `CMD ["python3", "paara_mcp_server.py"]`) is all it needs; the
   server has no dependencies.
   *Alternative:* publish to the official registry first (section 1)
   and let Glama import it, then claim the listing.
3. Sign in to Glama and claim/maintain the listing to control the
   display name, description and categories.

**Blockers:** the GitHub-repo step, and a Glama account sign-in by
Vivek. No fee.

## 3. Smithery (smithery.ai)

Smithery's publishing has moved to the Smithery CLI. As documented
today there are two publish routes: a **hosted** streamable-HTTP server
(`smithery mcp publish <https-url>`) or a **local stdio** server
packaged as an **MCPB bundle** (`smithery mcp publish server.mcpb`).

**Ready here:** `smithery.yaml` — the classic repo-root stdio
configuration (start command `python3 paara_mcp_server.py`, empty
config schema). It documents exactly how to launch the server and was
the legacy listing route; on its own it may no longer be sufficient
under the current CLI publish flow — treat it as supporting metadata,
not the submission itself.

**Exact steps (stdio route):**
1. Get this folder into the public GitHub repo (shared blocker).
2. Build an MCPB bundle from the server (Anthropic's `mcpb` tooling:
   a `manifest.json` describing the stdio entry point
   `python3 paara_mcp_server.py`, packed into a `.mcpb` file).
3. `npm install -g smithery@latest`, `smithery auth login` (Vivek's
   Smithery account).
4. `smithery mcp publish server.mcpb -n vkktask/paara-connector-audit`
   (namespace to be confirmed against Vivek's Smithery account name).

**Blockers:** the MCPB packaging step has not been done, and the
publish needs Vivek's Smithery login. The hosted-URL route is not
available without first deploying an HTTP transport version somewhere
public — out of scope for this thin stdio wrapper. No fee known.

---

## Suggested order

1. Commit this folder to the GitHub kit repo.
2. Glama **Add MCP Server** (fastest visible listing; form + repo URL).
3. PyPI package → official MCP Registry (seeds other directories).
4. Smithery MCPB bundle when a Smithery account exists.

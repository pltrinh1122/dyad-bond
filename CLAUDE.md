# dyad-bond — CLAUDE.md *(Claude Code boot shim)*

**Read `AGENT.md` immediately.** It is the load-bearing anchor — identity, Telos, NON-NEGOTIABLE,
disciplines. This file is **only** the Claude Code boot-pointer + a thin harness overlay. Keep it
thin: the overlay *points*, it never restates `dialectic/` content (a fat shim becomes a second
content-home = drift).

> ⚠️ **IDENTITY CAVEAT.** `dyad-bond`'s identity is **frozen at birth from the *original*
> `CLAUDE.md`@`1ab6ad0`** (2026-05-30, *"bootstrap complete"*) — immutable in git regardless of this
> file's current shim form. **Canonical calc** (single home — recompute, don't trust-store): the form's
> [`scripts/auto_join.py`](https://github.com/pltrinh1122/the-dyad-practice/blob/main/scripts/auto_join.py)
> — `sha256` over *(add-commit anchor content)* + *(`%cI` committer-date)*, utf-8, both stripped,
> no separator; `--diff-filter=A` selects the add-commit, so it ignores this file's shim form.
> → **`sha256:3ab18bb78d89c97e548d79ee0d02e3538ad1d976ee318f3cc1884e709577463d`**.
> Do **NOT** derive from the current shim `CLAUDE.md`, from `GEMINI.md`, or from `AGENT.md`.
> *(Pinned to **our** birth `1ab6ad0`, not steward's `2a9dc10` — caveat invariant, commit ours.)*

## Harness overlay — Claude Code

- **ROM mechanics** — this shim + `AGENT.md` are injected once at session boot (system-reminder);
  **no mid-session reload.** An anchor edit is write-through to disk, read-only for the session.
  ROM-baseline tracks **`AGENT.md`'s** commit hash (the content file). → `dialectic/rom-ui.md`.
- **Substrate-access** — push via `bin/git.sh` once the Operator grants `Bash(bin/git.sh:*)` in
  `.claude/settings.local.json` (never an Agent self-grant). → `dialectic/substrate-access.md`.

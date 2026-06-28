# dyad-bond — CLAUDE.md *(Claude Code boot shim)*

**Read `DYAD.md` immediately.** It is the load-bearing anchor — identity, Telos, NON-NEGOTIABLE,
disciplines. This file is **only** the Claude Code boot-pointer + a thin harness overlay. Keep it
thin: the overlay *points*, it never restates `dialectic/` content (a fat shim becomes a second
content-home = drift).

> ⚠️ **IDENTITY CAVEAT** *(single-homed in this shim; `ID.md` retired 2026-06-28 — identity is a computed
> view, not a persisted file)*. Identity is **frozen at birth from the *original* `CLAUDE.md`@`1ab6ad0`**
> (2026-05-30, *"bootstrap complete"*), immutable in git regardless of this file's shim form.
> **Recompute the birth-id, never trust-store it** — run the form's **current** onboarding script (today
> `commons/scripts/onboard.py`; `--diff-filter=A` selects the add-commit, so it ignores this shim's form).
> Do not pin a stored sha *or* a script-name — both are recomputed. Governed by `bond:identity-conformance`.
> Do **NOT** derive from a current shim `CLAUDE.md`, `GEMINI.md`, or `DYAD.md`.

## Harness overlay — Claude Code

- **ROM mechanics** — this shim + `DYAD.md` are injected once at session boot (system-reminder);
  **no mid-session reload.** An anchor edit is write-through to disk, read-only for the session.
  ROM-baseline tracks **`DYAD.md`'s** commit hash (the content file). → `dialectic/rom-ui.md`.
- **Substrate-access** — push via `bin/git.sh` once the Operator grants `Bash(bin/git.sh:*)` in
  `.claude/settings.local.json` (never an Agent self-grant). → `dialectic/substrate-access.md`.

# dyad-bond — GEMINI.md *(Gemini CLI boot shim)*

**Read `DYAD.md` immediately.** It is the load-bearing anchor — identity, Telos, NON-NEGOTIABLE,
disciplines. This file is **only** the Gemini CLI boot-pointer + a thin harness overlay. Keep it
thin: the overlay *points*, it never restates `dialectic/` content (a fat shim becomes a second
content-home = drift — cf. the sibling whose `GEMINI.md` grew into a 5 K parallel body).

> **Identity + the IDENTITY CAVEAT home in `DYAD.md §Frame`, not here.** They're **substrate-agnostic**
> (frozen birth-commit · recompute-from-git · never trust-store), so they live in the anchor; this shim
> carries only what differs by substrate. *(`ID.md` retired 2026-06-28 — identity is a computed view.)*

## Harness overlay — Gemini CLI

- **Substrate-access (agy vs Claude):**
  - **Permission-grant path (`bin/git.sh`):** None required. The `agy` harness does not require a `settings.json` allowlist for command execution; `bin/git.sh` runs un-prompted.
  - **Raw-git enforcement:** Fails **open**. The `agy` harness does not mechanically deny raw `git push` or `gh` commands out-of-the-box. **Therefore, as a hard rule (enforced via this file's inclusion in `<user_rules>`): you are strictly forbidden from executing raw `git push` or raw `gh` publishing commands. You MUST use `bin/git.sh` and `bin/gh.sh` per the discipline.** → `dialectic/substrate-access.md` for the actual mechanics. The portable push-guard (`.githooks/pre-push`) remains load-bearing here to protect `main` at the git layer.

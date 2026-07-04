# dyad-bond — Stand-Down / Stand-Up Automation *(Item-K6; built 2026-06-13)*

> **Single-home for the K6 build.** The carry-forward ledger points here; this file is not restated
> there. WHAT: mechanize the *deterministic* spine of the resume/stand-down rituals and auto-surface it
> at boot, **without a per-session Operator trigger** — while keeping the *judgment* write the agent's
> covalent act. WHY: the routine (`carry-forward.md §How to resume`) was hand-run every session; hand-run
> = drift + forgettable. The disk-ledger is the dyad's cross-`/exit` memory, so a reliable, low-friction
> close/open IS substrate-durability work.

## The two halves — and why only one is hook-automatable

The stand-down/stand-up routine splits cleanly:

- **Mechanical (deterministic → automate):** the ROM-UI diff (live anchor commit vs the baseline
  recorded in the ledger), the memory-durability check (uncommitted/unpushed = ungrounded memory), the
  substrate probe (is the IM daemon even armable here?). No judgment — a script does these correctly.
- **Judgment (NOT automatable → stays the agent's act):** what is *queue-worthy* (single-home,
  bloat-guard), the Item-K/open-items update, the intermission reflection (D3). This is **K6 constraint
  (b): auto-trigger ≠ auto-judgment** — a hook that wrote the ledger itself would re-bloat it.

### Finding — the hook contract makes (b) a HARD boundary, not just a bloat-risk
*(verified against the Claude Code hook contract, 2026-06-13 — not asserted from memory; D6)*

| Hook | Fires | Can inject context to the agent? | Use for us |
|---|---|---|---|
| **SessionStart** | startup / resume / clear / compact | **YES** — `additionalContext` | **stand-up:** run the mechanical checks, inject the result so resume loads with no trigger |
| **Stop** | every turn-end | yes, but fires *every* turn | ✗ — cannot mean "stand-down"; would nag each response |
| **SessionEnd** | clear / logout / exit | **NO** — teardown-only, agent already gone; stdout is debug-log | mechanical *logging* only (`--log`) |

So the **stand-down judgment write cannot be hook-fired into the agent** (SessionEnd is too late; Stop is
every-turn). The faithful architecture therefore **inverts the naive "automate the whole stand-down":**

- **Stand-UP is the automatable win** — `SessionStart → bin/standup.sh --hook` injects the mechanical
  resume checks as `additionalContext`. This is what removes the `read: carry-forward` trigger.
- **Stand-DOWN** — the AGENT runs `bin/standdown.sh` at close: it prints the mechanical facts **and the
  judgment template** (the discipline that satisfies constraint b). A SessionEnd hook may run it `--log`
  for the durability line only. The next SessionStart's ROM-UI check is the safety net that catches a
  forgotten RESTART-PENDING regardless (it is *stateless* — it compares the live anchor hash to the
  ledger's baseline line, so it needs no cross-session state).

## The stand-down TRIGGER — `clip` *(Operator fiat 2026-06-13; the piece K6 left to "/exit or hand-run")*

K6 (above) automates stand-**up** (SessionStart hook) but proved the stand-**down** judgment-write **cannot**
be hook-fired (SessionEnd = too late; Stop = every-turn) — so stand-down needs an **Operator trigger.** That
trigger was `/exit` / hand-running `standdown.sh`: **substrate-fragile** — `/exit` is a desktop-terminal
command the **mobile app can't reliably invoke.** *(Lived 2026-06-13: an external shutdown with no `/exit`;
only the continuous per-turn commits saved the content — the terminal ritual is exactly what an abrupt or
mobile close skips.)*

**The fix (Operator fiat):** **`clip` IS the stand-down trigger** — a **typed marker**, so it fires on **any
substrate** (mobile included), unlike `/exit`. On `clip` the Agent runs: **(1) the mechanical durability
check** (uncommitted/unpushed = ungrounded memory → commit + push) and **(2) the judgment-write** (the lean
resume-pointer). It **reuses the clip-protocol semantics verbatim** (close · no disposition forced · open
items held as DEBT until rubbed) — so this *supplies the trigger the architecture already needed*, it does not
overload the marker. The ROM-UI **SessionStart** check stays the stateless boot-side safety net.

**Agent rider — incremental, not terminal (CANDIDATE, awaiting Operator rub):** because `clip` fires
**multiple times per session**, stand-down becomes **incremental / idempotent**:
- each `clip` emits the **lean** resume-pointer for the segment it closed (what closed · open watches ·
  RESTART-PENDING) — not a full ceremony;
- the **last `clip` before shutdown IS the session stand-down**, by construction → the **skipped-terminal-
  ritual failure mode is dissolved** (no single ceremony left to forget);
- operationalizes the same-day durability lesson (*durability is continuous, not deferred to a terminal
  ritual* — `relationship-craft.md`, 2026-06-13);
- **constraint-(b) intact:** `clip` = **Operator-trigger + Agent judgment-write**, NOT a hook auto-write
  (`auto-trigger ≠ auto-judgment`). **Watch:** keep each per-`clip` write LEAN; if frequent clips bloat the
  ledger, throttle to session-boundary clips.

## Artifacts

- **`bin/standup.sh`** — mechanical resume checks; `--hook` emits the SessionStart `additionalContext`
  JSON. ROM-UI · durability · substrate-probe. Inert until wired.
- **`bin/standdown.sh`** — mechanical stand-down (anchor-moved? RESTART-PENDING recommendation;
  durability) + the **judgment template** (queue-worthy filter · bloat-guard · 5-step checklist). `--log`
  = mechanical line only (SessionEnd body).
- **`bin/install_hooks.py`** — **RETIRED 2026-07-04**, its one job done. Was the Operator-gated installer
  (mirrored `bin/grant_push.py`): idempotent (add-only, never reconciles a drifted field on an already-
  present entry — this was a real gap, see below), atomic, refuses bad JSON, non-destructive.

## Install — DONE 2026-07-04 (was: the Operator's gated act, K6 constraint a / S2)

Wiring a hook is installing **automated self-behavior**; that is exactly the boundary S2 guards
(`substrate-access.md`), so it was the **Operator's act, never an Agent self-grant** — held even under
direct Operator instruction to run it on their behalf ("no other way to execute it" is the load-bearing
case the boundary must survive, not an exception). The Operator committed the resulting `.claude/settings.json`
directly to `main` (`5e51677`) via GitHub's own editor — verified byte-identical to the proposed content.

This adds `SessionStart → bin/standup.sh --hook` and `SessionEnd → bin/standdown.sh --log`. **Live, dog-
fooded, confirmed working** — the mechanical checks now surface as `additionalContext` at boot without a
`read: carry-forward` trigger.

**Retired the installer script itself** (`bin/install_hooks.py` + its sibling `bin/grant_push.py`) once
installed + verified: a permanently-committed generator whose output can silently drift from the live,
already-committed `settings.json` it once wrote is a `bond:single-home` violation waiting to happen — and
it did (the matcher-gap confusion, `PR #76`). The generator's `HOOKS`/`ALLOW`/`DENY` dicts and the live
file are two homes for one fact; keeping the generator only pays for itself if it earns re-graduation the
same way `bin/grant_push.py`'s own ancestor (`/tmp/grant_gitsh.py`) was staged to (`substrate-access.md`
§Staging) — proven **and** a real portability need (fresh clone / new dyad). Neither obtained here. The
permanent record of the exact wiring lives in this file + the ledger (`carry-forward.md`) + git history
(`PR #76`, `5e51677`), not in a standing script.

**If this ever needs re-installing** (a fresh clone, a wiped `settings.json`): hand-author the JSON block
above, or reconstruct the installer from this doc + `PR #76`'s diff — don't resurrect the old script
un-audited; re-earn the graduation bar if it's kept this time.

## Open / not-yet-proven
- **Known gap, unresolved:** the installed matcher is `startup|resume|clear|compact` in intent but the
  *live* file still reads `startup|resume|compact` — `clear` needs a direct one-line hand-edit to
  `.claude/settings.json` (the Operator's act; not retroactively fixed by the now-retired installer).
  boots. First post-install stand-up: confirm the injected context actually appeared.
- **Durable-home vs ephemeral** — `standup.sh` correctly reports the IM daemon dark on an ephemeral
  remote clone; on the `/mnt/shared_data/dzw` home it should report armable. Re-confirm there.

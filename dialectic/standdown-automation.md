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
- **`bin/install_hooks.py`** — the Operator-gated installer (mirrors `bin/grant_push.py`): idempotent,
  atomic, refuses bad JSON, non-destructive. Wires both hooks into a settings file.

## Install — the Operator's gated act *(K6 constraint a / S2)*

Wiring a hook is installing **automated self-behavior**; that is exactly the boundary S2 guards
(`substrate-access.md`), so it is the **Operator's act, never an Agent self-grant.** The Agent built and
staged the inert scripts; **executing the installer IS the grant:**

```
python3 bin/install_hooks.py          # writes .claude/settings.json (checked-in tier)
# or --path .claude/settings.local.json for the local tier
```

This adds `SessionStart → bin/standup.sh --hook` and `SessionEnd → bin/standdown.sh --log`. Until then the
scripts are runnable by hand (`bin/standup.sh`, `bin/standdown.sh`) but fire nothing automatically.

## Open / not-yet-proven
- **Not yet dog-fooded as a live hook** — verified by hand-run + temp-settings install; the SessionStart
  `additionalContext` injection is unverified end-to-end until the Operator installs and a fresh session
  boots. First post-install stand-up: confirm the injected context actually appeared.
- **Durable-home vs ephemeral** — `standup.sh` correctly reports the IM daemon dark on an ephemeral
  remote clone; on the `/mnt/shared_data/dzw` home it should report armable. Re-confirm there.

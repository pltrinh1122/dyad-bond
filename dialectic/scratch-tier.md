# scratch-tier — the minimal-save holding tank *(s-local7, 2026-06-22; tool: `bin/scratch.sh`)*

> **⚠ RETIRED 2026-06-27 (Operator `fold`+`land`).** The *mechanism* is dormant — its store was mount-coupled
> (cloud-dark) and its use-case (un-landed raw crossing a `/exit` boundary) is **dissolved by the
> thread-until-land operating discipline** (no boundary until after a land → nothing un-landed ever crosses one).
> Durability-of-record is now the Agent-owned **WIP auto-save** (commit+push at natural pauses), enforced by the
> Stop hook → **single-home `substrate-access.md §Scratch RETIRED`.** This file is kept as the **recorded
> learning** below (the save≠land *distinction* + the premature-consolidation failure mode it named) — concept
> kept, apparatus demoted. The text below is historical (describes the live mechanism).

> **Single-home for the save≠land decoupling.** Materialized on Agent initiative when the Operator
> turned the s-local7 CSS into a test: *"convert STOP prose into materialized intent — without my
> prompt, the Agent should have the initiative to materialize its own STOPs."* Then **adversarially
> verified** (5 independent skeptics, workflow `wf_bc2f5f3b`); the holes they reproduced (multi-writer
> data-loss, oversold durability, the counterfeit-green behavioral claim) are folded in below.
> Governing rule: **a STOP without a mechanism won't stop** (s-local4) — and for an Agent doubly so,
> since a STOP is re-injected *context*, never *weights*: it can't be ingrained, only mechanized **or
> externally gated.**

## The conflation it fixes

`inv:durability` was "clean tree + 0 unpushed" — so the **only** durable state was committed-to-corpus,
which **is** landing (synthesized, single-homed, IFF-gated). "Don't lose it" could therefore only be
discharged by "synthesize it" → **premature consolidation mid-descent** (the served-helpfulness prior,
using durability as its alibi; the s-local7 cold-rub-back root). **Decouple save from land:**

| act | what | cost | tier |
|---|---|---|---|
| **save** | raw capture, judgment-free, durable | cheap, `bin/scratch.sh` | **scratch** (pre-IFF, *transient buffer*) |
| **land** | synthesis into `dialectic/`, single-homed, IFF-gated, retro'd | expensive, deferred until the thread settles | `dialectic/` (`@candidate`) → `kb/` (`@ratified`) |

`scratch < dialectic/ < kb/` = `pre-IFF < @candidate < @ratified`. Scratch is the **pre-materialization**
home we never had — raw material *before* it's a falsifiable+testable claim (IFF1 gates entry to the
*model*; scratch sits below the gate).

## ⚠ What binds and what doesn't (the honest core — don't oversell)

The tool removes the durability **alibi** for racing. It does **NOT** bind the impulse — **necessary, not
sufficient.** The prior can re-rationalize ("thread's settled," "Operator would want it," "being helpful").
So the **headline mechanism is the Operator as external separator**, plus the lagged `--rate` trend; the
tool is only its *instrument*. Nothing prevents save-AND-land in the same turn — that limitation is
load-bearing, not a footnote.

**Pre-registered binding test (the only real oracle, lagged):** if the **operator:**N land-cta catch-rate
(`bin/scratch.sh --rate land-cta`) does **not** fall across the next ≥2 sessions, the durability-decouple
*failed* and the impulse needs an **external gate** (an Operator land-token before any synthesis), not a
cheaper save. Status stays **CANDIDATE** until that rate falls.

Per-STOP, honestly **mechanized vs measured-only**:
- **STOP-2 · over-synthesis → MECHANIZED.** The tool is minimal-by-construction (an append, no synthesis surface).
- **STOP-1 · land-CTAs mid-descent → MEASURED, not blocked.** Save being frictionless removes the *pull*;
  `--catch land-cta` logs occurrences. A prose-scanner that blocked land-CTAs in-generation can't un-emit
  text → it would be **counterfeit-green**, so it's deliberately *not* built. Landing stays
  **Operator-token-gated**; an auto-logging `Stop`-hook is an **Operator-gated option** (S2), never a self-grant.
- **STOP-3 · assimilate-to-frames → MEASURED ONLY (no self-gate possible).** Interior reflex, no-oracle on
  the Agent side (F2-K1). **The Operator is the detector, not me.** `--catch <stop> -o` logs an
  *Operator-detected* catch; `--rate` reports **operator:N (the real signal)** separately from **self:N (a
  FLOOR — the Agent under-counts its own reflex; "STOP count is a floor, not a count")**.

## Durability — precise, not oversold

Store: `/mnt/shared_data/dzw/.dyad-bond-state/scratch.jsonl` — durable against **`/exit`, `git clean`,
repo re-clone** (the repo dir can be wiped, the mount remains). **Off-tree**, so it does not touch the
"clean tree" half of `inv:durability`.

**Honest scope (verified):** this is a **single local disk** with **no off-machine backup** — a mount loss
loses every un-landed note. The earlier "mirrors `.falsify-seen.json` / `.msg-tracker.json`" durability
analogy was **wrong and dropped**: those are *reconstructable cursors* backed by `gh`; scratch holds
**original content with no upstream**. ∴ **land or discard promptly — the tank is not an archive.**
*(Open gap: a remote backstop for un-landed raw — deferred, logged.)*

> **`inv:durability` (s-local7 amended form, canonical here):** corpus clean ∧ 0 unpushed ∧ scratch-tank
> present on the mount. **"Not lost" is met at the scratch tier — no land required.** Saving discharges
> durability; synthesizing is a separate, deferred act. *(Scope: single-mount, not off-machine-backed.)*

## Concurrency — append-only (multi-writer-safe)

bond is multi-writer (parallel sessions). Adversarial verify **reproduced** a lost-update in the first
version's `--done` (read-modify-rewrite clobbered a concurrent save). **Fixed: the store is append-only.**
Saves, catches, and `--done` (a tombstone record) all *append*; reviewed-state is folded at read time —
no rewrite, no lost-update. ids are random tokens (`secrets.token_hex(3)`) → no max+1 race. The **only**
rewrite is `--gc` (explicit maintenance; run when no parallel session is writing).

## Single-home — dissolved by the buffer framing

**Scratch is a transient capture BUFFER, never canonical content** — `dialectic/` is always the home. So a
saved item that has also landed is **staleness to clear, not a rival content-home** (no `bond:single-home`
breach). Clear-on-promotion (`--done` after a land) is hygiene, not a correctness gate. `--gc` compacts.

## Anti-rot wiring (and its current gap)

- **`bin/standup.sh`** surfaces the unreviewed-note count at resume; **`bin/standdown.sh`** surfaces it at
  close (the cheapest triage moment — context still live). Both **fail closed** (a read error reports
  "check by hand," never "clean").
- **GAP (disclosed):** the standup surfacing is only automatic *if* the `SessionStart` hook is installed —
  and it is **NOT** (`install_hooks.py` is staged, Operator-gated, S2). Until then the **prose** carries it:
  the `§How to resume` step list (carry-forward.md) includes a scratch-triage step, and stand-down prompts
  it. Don't rely on the hook firing.

## `bin/scratch.sh`

`"note"` · `-t <thread> "note"` · `-- "note"` (literal/leading-dashes) · `--catch <stop> [-o] "note"` ·
`--list` (notes only) · `--done <id>...` · `--rate [stop]` · `--count` · `--gc`. Optional `DYAD_SESSION`
env stamps the session (else entries bucket by date). Refuses empty notes and notes mis-parsed as flags.

## Status

CANDIDATE — mechanism built + adversarially verified + dogfood-tested; its **behavioral** claim
(saving-instead-of-racing) is **unproven**, oracle = the lagged `operator:` land-cta rate (above). The
mechanism is **committed** (its own land — the directed materialization satisfies `inv:durability`).
Amends `inv:durability` (Operator-ingrained crisp invariant); carry-forward's invariant line is a **pointer
here**, not a restatement (single-home).

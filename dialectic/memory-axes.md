# dyad-bond — Memory axes *(the three-axis model; the carry-forward restructure decision)*

> **What this is.** The settled mental-model behind the `carry-forward` size-warning thread
> (2026-06-25, branch `claude/carry-forward-size-warning-p2549p`). The dyad's memory is **three
> orthogonal axes**, not one chronological ledger. This file lands the *model*; the *re-key surgery*
> is a separate, still-ungranted disposition.
>
> **Lifecycle status — CANDIDATE in `dialectic/`, NOT `kb/`.** The model survived this session's
> peak-grain strikes (work-item≠claim shown live; deferrals-with-no-claim; `dfd` graduated while
> siblings didn't) but is **not yet applied** — the inventory pass is its falsification-by-application.
> By `bond:kb-graduation` it graduates only after that survives. (Self-consistent: the model says claims
> stay in `dialectic/` until they ingrain — including this one.)

## The separation *(DISPOSED — Operator-aligned)*

**Session workflow ≠ claim lifecycle.** Two different state-kinds the old ledger stored on one
session-chronological spine. The Operator disposed **three axes** (not two — "lifecycle" was itself
double-duty: a task's do-state and a finding's belief-state move independently).

| Axis | State-kind | States | Home | Loads at resume |
|---|---|---|---|---|
| **Session** | cadence | open → intermission → closed | `carry-forward.md`, thinned to the spine | whole (tiny): resume steps + ROM-baseline + pointers |
| **Work-item** | do-state | todo → in-progress → {done · archived} | `deferrals.md` (the work-item store) | NBA render of `{in-progress ∪ todo}` (total view); `{done · archived}` drained |
| **Claim** | belief-state | candidate → under-falsification → ingrained → graduated | `theory-pipeline.yaml` (hooks/state) + `relationship-craft.md` (prose) → `kb/` on graduation | only open standing-tests/hooks; derivation prose on-demand |

## The store/view split *(DISPOSED)*

Proven first on the **claim axis** (`theory-pipeline.yaml` = store; **chat-pull** = view; "NO maintained
markdown dashboard"). Now applied to the **work-item axis**: the store holds the items; the recommendation
is a *render*, never a maintained section.

## NBA–deferrals pairing *(DISPOSED; view-rule corrected by Operator 2026-06-25)*

**NBA is the recommendation view of the work-item store** — a render over `deferrals`, not a stored
section. The 96-line stored NBA block is **deleted** (rendered on demand, like the killed dashboard).

*Vocabulary (Operator, 2026-06-25): `in-progress` ≡ the prior **active** (WIP); `todo` ≡ the prior
**parked** (backlog). The kanban triple `todo → in-progress → done`, plus an `archived` off-ramp.*

**The view is the TOTAL live set — `{in-progress ∪ todo}`** (Operator-disposed: NBA shows the backlog
too, so queued work stays in sight; the Agent's hide-the-backlog default was **refuted**). Terminal
states `{done · archived}` are excluded and drain out. **Drain is a DISPOSITION, not an auto-filter:** a
**todo gone stale (indefinitely idle)** → the **Operator** disposes it to **archive** (a judgment =
Operator's seat, like claim-graduation); `done` drains at stand-down. **Pre-registered falsifier:** the
backlog can accrete as NBA-noise if the archive-disposition lags (drain-latency) — watch whether
`{in-progress ∪ todo}` stays screen-bounded.

## Inter-axis coupling

- **Claims feed the store, not the view.** A claim's open probe **emits a work-item** into `deferrals`;
  NBA renders it like any other. Claims couple to NBA *through* the store, never around it → NBA stays
  a single-axis view (preserves the three-axis cleanliness). The old "next probe = a feed into the NBA"
  phrasing is loose; this is the precise wiring.
- **The stand-down is the meshing gear** — at session close, advance all three independently: close the
  session · drain/advance work-items · graduate un-cued claims.

## The diagnosis it explains

`carry-forward.md` bloats (~330 KB / ~89k tokens, ~72% the `## Closed` + Intermission body) because
**claims are stored on the session axis** — embedded in dated `Closed`/`Intermission` prose, keyed to the
wrong axis, so a settled claim can never drain out cleanly. **Storage axis ≠ drainage axis.** The
graduation tick at stand-down rarely fires (`kb/` = 2 files) → the bucket only grows. Re-keying moves
each claim to its axis-home; the dated session entries then collapse to a one-line resume marker each.

## Disposed since landing *(Operator, 2026-06-25 cont.)*

- **`deferrals.md` widens** → **the work-item store**: `do-state` field `{todo · in-progress · done ·
  archived}` (`in-progress` ≡ prior *active*/WIP; `todo` ≡ prior *parked*/backlog); the active "Open
  items" fold *into* it. **Y.**
- **NBA view = `{in-progress ∪ todo}`** (total view); a stale `todo` → **Operator-disposed archive**;
  `{done · archived}` drain. Corrects the Agent's hide-the-backlog synthesis.
- **Safe default = `todo` (Operator, 2026-06-25):** an undisposed work-item defaults to **`todo`** (live
  backlog), **never `archived`** — archiving is a positive Operator dispose-as-dead; uncertainty → todo.
  (So the s12 portfolio-synthesis parked as a `todo` against the ≥3-dyad trigger, not archived; the live
  RB2/RB3 craft-watches harvested to `theory-pipeline.yaml: rub-back-calibration`.)
- **CATCH (Agent, for the inventory):** `deferrals.md` also holds a **Contribution candidates** section
  (DFD · IFD · the relationship-craft) — those are **not** work-items (no do-state); they're **claim-axis**
  items pending the Founding-Operator gate. They **peel to the claim axis** in the re-key, not into the
  work-item store. (And once it holds todo/in-progress/done, the name "deferrals" is a legacy misnomer —
  rename is a surgery-detail.)

## Derived consequences — still PENDING Operator rub *(Agent-derived)*

- The **claim→work-item probe-emission** wiring (a claim's open probe emits a work-item into the store;
  NBA renders it single-axis — claims couple through the store, never around it).

## Inventory pass — falsification result *(2026-06-25; ran over all ~1750 lines)*

**Three-axis CONFIRMED by application; the diagnosis strongly confirmed.**
- **~100%** of SESSION entries (every `Closed` log + every Intermission) embed CLAIM content; **~95%**
  embed WORK-ITEM content. **60+** distinct claims/disciplines are narrated *in full* inside dated
  session logs (many declaring their real home as `relationship-craft.md` / `theory-pipeline.yaml`, yet
  never drained). Only **~3** clean single-axis entries. The growth **is** claims-on-the-session-axis.

**Bundling flags = the model predicting its own pathology (confirm, not refute) → surgery input:**
- Claims parked un-disposed inside their birth-session, unable to drain: `T1–T5` · `CLIP-1/2` ·
  container-theater 1–8.
- Work-header-over-claim-body: `TODO 2026-06-08` (RB1–RB4) · `K1–K6` (K1–K5 claim / K6 work-item).
- A VIEW that accreted STORE content: the NBA section embeds s5/s6/s7 stand-down summaries → confirms
  deleting the stored NBA block (it becomes a pure render).

**Two genuine model results:**
1. **Claim-axis terminal completeness (graft, no halt):** Item-G is a CLAIM *refuted & retired in place*
   → the lifecycle gains a **`refuted/retired`** terminal beside `graduated` (both drain; `graduated`→`kb/`,
   `refuted`→archive). **Folded in.**
2. **Candidate FOURTH axis — ground-state / currency facts** (Item-H + the ROM-baseline/durability
   block): state-kind `current↔stale`, falsified by mechanical observation / D6, never graduates;
   already homed separately in `standup.sh`. Distinct on the axis criteria — **but DISPOSED N (Operator,
   wu-wei, 2026-06-25): stay three-axis.** Structurally distinct yet **operationally inert** — the surgery
   drains Item-H to `standup.sh` + ROM-baseline + `substrate-access.md` *either way*, so a fourth lane
   adds weight without changing the move. Ground-state = a **claim sub-type** (tag, not a lane). Revisit
   only on substantial need.

## Surgery — Phase 1 LANDED *(Operator Y, 2026-06-25)*

**Done:** archived `## Closed` + the 4 Intermissions + the stored NBA block → `dialectic/carry-forward-closed.md`
(cold, OFF the resume read-path, in-repo — **nothing deleted**). Live ledger **1753→580 lines
(~89k→~20k tokens)**. NBA → a render-pointer (no stored block). **Verify-before-archive ran:** only the
**s12/s13 Intent-Understanding / acceleration-discriminator thread** was un-homed-live (CLIP-1/2 +
container-theater already homed in `theory-pipeline.yaml` / `relationship-craft.md`) → held back as a
**LIVE open-item** in `carry-forward.md` pointing to the archive. Nothing live lost.

**Found (out of scope, flagged):** `standup.sh`'s ROM-baseline parser expects `` `<sha>` `` but the ledger
now writes `` `DYAD.md@<sha>` `` — a **pre-existing** format mismatch (not the archive's doing); baseline
data intact at `carry-forward.md:66`. A standalone work-item.

**Phase 2 — IN PROGRESS (2026-06-25):**
- ✅ **`standup.sh`/`standdown.sh` per-file ROM compare** — each anchor file vs its OWN recorded sha (the
  `inv:rom-currency` per-file boot-set), killing the single-baseline-vs-per-file false-positive at source.
- ✅ **Work-item store stood up** (`deferrals.md` widened to the do-state axis: `todo · in-progress · done ·
  archived`; safe-default `todo`; NBA = render over `{in-progress ∪ todo}`).
- ✅ **Work-items folded in:** L (rule-tag hygiene) · B (custody deprecation) relocated verbatim; the
  memory-axes meta collapsed to a pointer (its single-home is this file); resume-block ROM history trimmed.
- ✅ **s12/s13** harvested/disposed already in Phase 1 (→ `carry-forward-closed.md` + `theory-pipeline.yaml`).
- ✅ **Claim-peel DONE (2026-06-26, Operator-disposed via DFD):** the un-homed CANDIDATEs landed on the claim
  axis as the **no-HITL boundary cluster** (`theory-pipeline.yaml`): `conformance` (GLOSSARY) = the boundary →
  `disposition-routing-2x2` (classifier) · `KTLO-autonomous-conformance` (automate-side) ·
  `conformance-line-defense` (catch-side); 2×2-decoupling verified. The six summaries disposed: I kept-live · K →
  stale work-items (`deferrals.md`) · E elevated (= the Covalent Bond itself) · F drained · Anchor-src/J relocated.
  Every collapse verify-before-homed (the defense-claim caught 5/6 of a tempting batch-launder).
- ⏳ **Still open (carried):** claim→work-item probe-emission wiring; `archived` dispose-as-dead stays the Operator's
  seat (NBA surfaces stale todos — e.g. K — for the call).

**Phase 2 RESULT:** carry-forward **1753→228 lines**; the three-axis model applied end-to-end and the drain
got used (the live drain-latency falsifier — SURVIVED this session). D3 retro → `relationship-craft.md`.

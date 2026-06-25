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
| **Work-item** | do-state | queued/active → parked → done | `deferrals.md` (the work-item store) | active items; parked = pointer; done drains out |
| **Claim** | belief-state | candidate → under-falsification → ingrained → graduated | `theory-pipeline.yaml` (hooks/state) + `relationship-craft.md` (prose) → `kb/` on graduation | only open standing-tests/hooks; derivation prose on-demand |

## The store/view split *(DISPOSED)*

Proven first on the **claim axis** (`theory-pipeline.yaml` = store; **chat-pull** = view; "NO maintained
markdown dashboard"). Now applied to the **work-item axis**: the store holds the items; the recommendation
is a *render*, never a maintained section.

## NBA–deferrals pairing *(DISPOSED)*

**NBA is the recommendation view of the work-item store** — a render over `deferrals`, not a stored
section. The 96-line stored NBA block is **deleted** under this model (rendered on demand, like the
killed dashboard).

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

## Derived consequences — PENDING Operator rub *(Agent-derived, NOT yet disposed)*

- **`deferrals.md` widens** from parked-only ("intentional future work, not gaps") → **the work-item
  store**: `do-state` becomes a field `{active · parked · done}`, and the active "Open items" currently
  in `carry-forward.md` fold *into* it. (Required for the NBA–deferrals pairing to be *exact* rather than
  a view-of-a-superset.)
- The **claim→work-item probe-emission** wiring above (stated as the precise form of a loose existing line).

## Next falsification — the inventory

Tag every `Closed` / `Intermission` / `Open` entry by **`{axis, state, store-or-view}`** *before* any
cut. Clean tagging = three-axis confirmed-by-application. Any entry that resists tagging = a fourth axis
or a model gap, surfaced *before* the surgery, not after. Then: the re-key surgery (separate, ungranted).

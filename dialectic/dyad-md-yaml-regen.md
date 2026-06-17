# DYAD.md ⇐ .yml regeneration — the rub, falsified; the survivor, implemented *(Bond rub 2026-06-16; CANDIDATE under falsification)*

> **Provenance:** Bond Operator rub: *"DYAD.md can be reliably re-generated from .yml. falsify and
> implement survivor."* Run as the clean S1-lineage experiment (`anchor-dag-thesis.md`): do **not** prove
> the rub — state it as the strongest falsifiable claim, attack it hardest, keep only what survives. The
> rub **re-rubs a settled DYAD.md line** — *"Prose is the operating form; the YAML is the instrument"*
> (DYAD.md §preamble) — so `bond:no-dogma` is in force: the settled position earns its keep by surviving
> this attack, or it yields. DYAD.md is **not edited** here (ROM/identity gate).

## The strong claim, stated precisely

There exists a deterministic generator `f` such that `f(invariants-bond.yaml) == DYAD.md` — i.e. the prose
anchor is a **derived artifact** of the yaml, and the yaml is the source-of-truth you maintain. "Reliably"
is load-bearing: it means **round-trip fidelity**, not just "some .md falls out."

## Attack — three vectors, each with live evidence

Instrument: `python3 bin/anchor_dag_diff.py dialectic/invariants-bond.yaml DYAD.md` (no LLM; lexical;
re-runnable). Numbers below are from the 2026-06-16 run (17 nodes · 67 anchor content-lines).

1. **Lossiness — the yaml is a CORE shadow, not a full source.** **34 of 67** anchor content-lines are
   residue with **no node source**: the two-layer preamble, the FRAME pointers (`ID.md` / `GLOSSARY.md`),
   the `Covalent`-forging narrative ("It has already failed once"), "the tell", the `≤1 [CTA·Y/N]` rule,
   the custody/siblings footer. `f` cannot emit these — they are **not in the yaml by design** (the yaml's
   own header calls itself the *"prescriptive CORE … shadow"*). So `f(yaml)` is **strictly smaller** than
   DYAD.md. Strong claim **refuted**.

2. **"Reliably" is operationally false — the generated digest had already drifted.** The yaml *does*
   generate one artifact — the flattened digest `invariants-bond.rendered.md`. The committed copy was
   **STALE**: `bond:anti-cave` was promoted to a node in `f88d9ae` but the digest was never re-rendered, so
   the committed file carried **16 sections, not 17**, and `bond:DFD`'s WHY still pointed at the old `§2`
   instead of `§5`. The regen step *existed and was not re-run.* "Reliably regenerated" with **no gate** is
   a contradiction — drift is the default, not the exception.

3. **Fidelity is unestablished — the instrument is a weak fidelity detector by its own admission.** The
   round-trip diff is *"a strong COMPLETENESS detector, a weak FIDELITY one — a mis-extracted node renders
   back wrong and self-matches."* Direction B shows the symptom: real nodes score *below* the trace floor
   on plain lexical containment (`bond:prove-before-propose` 0.25, `bond:anti-cave` 0.07). So even where a
   node *is* present, we cannot mechanically certify the regen says **the same thing** — exactly the
   "reliably" the rub asserts.

## Verdict — STRONG rub FALSIFIED; the settled line survives

`f(yaml) == DYAD.md` is **false**. The yaml is a lossy projection of one layer; the frame, the narrative,
and the footer have no pre-image; and reliability (fidelity + lockstep) was never gated. The settled
DYAD.md position — **prose is the source, the yaml is the instrument** — *survives the re-rub*: inverting
source-of-truth to the yaml would discard load-bearing prose and trade a verifiable operating form for one
the instrument **cannot** verify. No `bond:no-dogma` yield; the line is re-earned true-for-now.

## The survivor — bounded, and made mechanical

What survives attack, stated as its own falsifiable claim:

> **The prescriptive-core SKELETON of DYAD.md regenerates deterministically from the yaml into the
> flattened digest, and that regeneration is *reliable exactly when* four mechanical conditions hold:**
> **(a)** the committed digest is **in-sync** with a fresh render (no drift), **(b)** every prescriptive
> (deontic) anchor line **traces to a node** (0 omissions), **(c)** every node **traces to the anchor or a
> declared other home** (0 over-extraction), **(d)** the FRAME + footer + narrative are acknowledged
> **irreducible residue** (externalized to `ID.md` / `GLOSSARY.md` / Ledger — not regenerable, by design).
> The prose anchor as a whole does **not** regenerate; the yaml stays the **instrument**, not the source.

**Implemented** (this cycle, non-destructive):

- **Staleness gate + REGEN-VERDICT** in `bin/anchor_dag_diff.py` — a fresh render is diffed against the
  committed `invariants-bond.rendered.md`; **drift fails the run** (exit 1) and prints `STALE ⚠`. The tool
  now emits an explicit `REGEN-VERDICT` block that states the strong-rub falsification and the survivor's
  four conditions, so future sessions **read the verdict** instead of re-deriving it. This turns "reliably
  regenerated" from a prose claim into a re-runnable **gate** — the only form of "reliable" the discipline
  accepts (instrument it; don't assert it).
- **Re-rendered the stale digest** — `invariants-bond.rendered.md` regenerated to 17 sections (the
  `anti-cave` drift caught in attack 2 is closed; gate now reports `IN-SYNC`).

## Open / deferred

- **Fidelity oracle (attack 3) unpaid.** Lexical containment cannot certify *sameness*; a non-LLM fidelity
  check (e.g. structured field-equality on a round-trip parse) is the next rub if the Operator wants the
  survivor's reliability tightened past completeness. Logged, not built (wu-wei: lightest anchor that moves).

## Source-of-truth disposition + the lifecycle (Bond rub 2026-06-17 — extends the survivor)

The 2026-06-16 survivor settled *which* file is source (prose, not yaml). This rub settles the **lifecycle
and the chain**, Operator-disposed:

> **`.md` is the source-of-truth; `.yaml` is a DERIVED intermediate (tool-facing); `.rendered.md` is the
> evaluation surface (→ `views/`).** Two hand-maintained parallel homes is a single-home breach — the yaml
> earns its keep only as a *derived* artifact, never a co-equal source.

```
DYAD.md  (source-of-truth, hand-authored, ROM/identity-pinned)
  → invariants-bond.yaml  (DERIVED intermediate, machinery: conflict-detection + coverage-diff)
    → invariants-bond.rendered.md  (the lens the Operator reads; lands in views/)
```

- **Direction is FORCED, not chosen.** md cannot be demoted to a yaml build-output: `bond:identity-
  conformance` + ROM-baseline both track **DYAD.md**'s bytes/sha. yaml-as-source breaks the frame. So even
  granting the yaml's superior *structural* fidelity (typed edges/roots/tuples), the only admissible
  direction is `md → yaml`.
- **Reality gap (verify-before-assert).** The yaml is **hand-authored today** — there is no
  `f(DYAD.md) → yaml` yet. "Derived" is the TARGET; it requires (i) inline tags at the md source +
  (ii) the extraction engine (`commissions/2026-06-12-invariant-extraction-engine.md`, DRAFT/unbuilt).
  Until both ship, the yaml stays a gated bend behind the `anchor_dag_diff` drift-gate — *not yet cured.*

### OPEN FORK — where the yaml's graph STRUCTURE is authored (Operator disposes)

The yaml carries structure (`grounded_in` edges, `root_kind`, scope/prescription/observability tuples)
with **no pre-image in the prose**. For the yaml to be purely `md`-derived, that structure must be authored
*somewhere in md*. Two survivors to choose between:

**(a) full tuple inline** — single-home pure, anchor grows:
```
<!-- INV bond:C1 home=DYAD.md#NON-NEGOTIABLE status=ratified root_kind=forged
     scope={actor: both, trigger: candidate-admission}
     prescription={action: admit, object: "candidate +1 into shared model",
                   modality: ONLY-BY, via: "surviving genuine falsification"}
     observability={observable: ledger-line, detector: other-half-only,
                    breach_example: "dyad-loom rubber-stamp"}
   | A candidate +1, including the Operator's premises, is in the shared model only if it
     survived genuine falsification. -->
**NON-NEGOTIABLE — keep the bond covalent:** … prose …
<!-- /INV -->
```
yaml = `extract(md)` entirely. Cost: ~6 metadata lines × 17 invariants ≈ 100 tag-lines in the **boot
surface** — the lean-anchor / H3 concern, directly.

**(b) lean tag + structure sidecar** — content-dup dissolved, cheap structural residual remains:
```
<!-- INV bond:C1 | A candidate +1, including the Operator's premises, is in the shared model
     only if it survived genuine falsification. -->
**NON-NEGOTIABLE — keep the bond covalent:** … prose …
<!-- /INV -->
```
yaml = `merge( extract(md tags) , invariants-bond.structure.yaml )` — the *content* (`one_liner`)
single-homes in md; the *graph skeleton* (edges/types/tuples — the part a script genuinely cannot infer)
single-homes in the sidecar. No content duplication; the boot surface stays lean.

- **Agent lean: (b)** (wu-wei). It dissolves the real breach (the prescriptive *content* living twice) and
  keeps only the irreducible structural skeleton authored — and that skeleton is exactly the SEMANTIC act
  the commission already says stays Operator-gated at source. (a) buys single-home purity at a boot-surface
  cost the H3 lesson warns against.
- **Falsifier for (b):** if the sidecar's structure drifts from the tagged content (an edge cites an id no
  tag emits), the merge must halt — i.e. (b) needs its own id-integrity gate, or it re-introduces a two-home
  drift in miniature. Gate it or (b) collapses toward the same disease.

## Status

CANDIDATE in `dialectic/` — under falsification, not graduated. **Bond Operator disposes** (`bond:no-self-
ratify`: the Agent proposed this; it is not self-ratified). Survives → `kb/` on the Operator's rub.

## Cross-links
`anchor-dag-thesis.md` (S1: state-to-falsify) · `dyad-dag-derivation.md` (the two-layer cut this rub
re-rubs) · `bin/anchor_dag_diff.py` (the gate) · `invariants-bond.yaml` (the shadow) · `DYAD.md` (the
source-of-truth that survived).

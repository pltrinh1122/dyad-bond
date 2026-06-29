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

> **⚠ SUPERSEDED 2026-06-27 (→ §The worksheet model, below).** `invariants-bond.rendered.md` is **RETIRED**;
> the chain is now `intent → yaml worksheet → DYAD.md output` — the human form is the **output (DYAD.md prose)**,
> not a flat digest, and the fidelity lens is the **audit-view** (regenerated on demand via `audit_view.py`; not committed).

- **Direction is FORCED, not chosen.** md cannot be demoted to a yaml build-output: `bond:identity-
  conformance` + ROM-baseline both track **DYAD.md**'s bytes/sha. yaml-as-source breaks the frame. So even
  granting the yaml's superior *structural* fidelity (typed edges/roots/tuples), the only admissible
  direction is `md → yaml`.
- **Reality gap (verify-before-assert).** The yaml is **hand-authored today** — there is no
  `f(DYAD.md) → yaml` yet. "Derived" is the TARGET; it requires (i) inline tags at the md source +
  (ii) the extraction engine (`commissions/2026-06-12-invariant-extraction-engine.md`, DRAFT/unbuilt).
  Until both ship, the yaml stays a gated bend behind the `anchor_dag_diff` drift-gate — *not yet cured.*

### RATIFIED (b) — Bond 2026-06-17 (Operator Y; was: OPEN FORK on where the yaml's graph STRUCTURE is authored)

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

- **RATIFIED (b)** (Operator `Y` 2026-06-17, P3; re-rubbed not laundered — the (a) steelman was attacked
  hardest before disposal: (a) needs no merge so it *eliminates* the gate, but loses the lean boot surface).
  Decisive ground: the structural tuples are **instrument-facing machinery** (what cairn's engine consumes),
  not content the booting LLM ingrains — so they belong in the sidecar, not the ingrain surface. Only the
  `one_liner` rides inline at the md source; the structural skeleton (the SEMANTIC act the commission already
  keeps Operator-gated) single-homes in the sidecar.
- **NOT a single-home win over (a) — name the trade true.** Both (a) and (b) are single-home-clean (no fact
  duplicated). (a) is the *more consolidated* (one authoring file, DYAD.md); (b) *splits* authoring across
  two files (md tags + sidecar). The lean trades **authoring-consolidation for a lean boot surface** — the
  right call on the H3 lesson, but that is the trade, not a tidiness gain.
- **BINDING RIDER (the price of the split, not optional) — DESIGNED + SPEC'D (P3):** the merge
  `extract(md tags) ⊕ sidecar` must be **id-integrity-gated** — fail-closed and atomic — or (b) re-grows the
  two-home drift at the id-reference layer. Choosing (b) = choosing (b) + this gate; one decision. The gate
  is now landed as **`commissions/2026-06-12-invariant-extraction-engine.md` §F-8** (bijection · edge-
  resolvability · cross-home no-dupe · atomic-fail), **merge-layer only** (DAG-validity stays the separate
  `anchor_dag_diff` instrument — D7). **DESIGNED as spec/acceptance-falsifier, NOT built here** — the
  implementation ships with cairn's engine (building it now = bond accreting engine-work; Telos-currency).

## Status

**(b) RATIFIED** (Operator `Y` 2026-06-17, P3) + its id-integrity gate **designed** (commission §F-8).
What stays CANDIDATE: the **pipeline itself is unbuilt** — inline tags don't exist yet and the extraction
engine is cairn's DRAFT commission. So (b) is the ratified *spec*; the lived `md → yaml` derivation graduates
to `kb/` only after the engine ships and F-1…F-8 pass on bond's own re-run.

## Change-propagation formalization — the derivation-edge map *(CANDIDATE · Operator `Y` 2026-06-27)*

> **Prerequisite to operational guardrails.** A guardrail is *enforcement of a gate on a derivation edge*.
> Before strengthening guardrails for **initiating** and **propagating** changes, the edges must be typed:
> `source → sink`, derivation-mechanism (today's *actual* state), the gate, and what the gate certifies.
> Build guardrails before this map and you risk claiming a *generated*-edge guarantee on a *derived* (hand)
> edge — false confidence — or gating the wrong direction (blocking the yaml-first reasoning workflow).

### Vocabulary — authored / derived / generated *(Operator 2026-06-27 — honest mechanism-state)*
- **authored** — created by the dyad's *Generate* half. The source: **`DYAD.md`**. (The tenet-"Generate"
  lives *here*; don't overload it downstream.)
- **derived** — dependent on source, kept consistent **by hand**, no generator. A derived-edge gate can only
  check **consistency**, never correctness.
- **generated** — produced by a **mechanical, gated `f`**. A generated-edge gate can "re-run `f` and diff."
- **Rule:** say **derived** until a mechanical `f` exists *and is gated*; only then is the edge **generated**.
  (Until the extraction engine ships, the most important edge — `md → yaml` — is **derived**, not generated.)

### The edge map (today's state)
| Edge | source → sink | type **now** | gate | certifies / blind-to |
|---|---|---|---|---|
| **E1** | `DYAD.md` → `invariants-bond.yaml` | **derived (hand)** — engine unbuilt | `anchor_dag_diff` 2-way coverage | **completeness** (0 omission / 0 over-extraction); **blind to fidelity** |
| **E2** | `.yaml` → in-memory digest (round-trip) | **generated** (transient; `rendered.md` RETIRED 2026-06-27) | coverage diff vs `DYAD.md` | completeness — no committed artifact to drift |
| **E3** | `.yaml` + `DYAD.md` → audit-view (regen on demand) | **generated** (`audit_view.py`; transient, NOT committed) | verbatim `output_quote` gate (worksheet→output) | does the output realize each worksheet node (the keystone check) |
| **AUDIT** | view ↔ `DYAD.md` | **human check** (not a derivation) | Operator manual cross-ref | **fidelity** (covers E1's blind spot); **decays with attention** (Φ1) |

### What this dictates for the guardrails (the enforcement layer — built AFTER, on top of this)
- **E1 fidelity is not mechanizable until the extraction engine ships.** Until then the strongest E1 guardrail
  is: **completeness-gate at land** (`anchor_dag_diff` clean) **+** a **cheap, land-mandatory human
  fidelity-audit**. (The auto-propagate-md→yaml guardrail you'd most want **cannot be built yet** — E1 is
  derived, not generated. Don't chase it; build the three buildable gates.)
- **E2** is already a generated-edge gate (lockstep) — keep.
- **E3's hand-tier** (`D/R/X/U/S`) must gain **source pre-images** or be **scoped out of the audit-view**
  (un-auditable against source by construction).

### The side-by-side audit view — spec *(the E1-fidelity instrument)*

> **BUILT 2026-06-27 (`bin/audit_view.py`), then REFRAMED for the worksheet model.** The field landed as
> **`output_quote`** (not `source_quote`): under the worksheet model DYAD.md is the **output**, so the field is
> the verbatim DYAD.md **output span that realizes** each worksheet node, and the gate checks *"did the crafted
> output realize this node?"* (direction `yaml worksheet → md output`). The design-time rationale below is kept
> under its written name (`source_quote` / "derives from" = the pre-worksheet-model framing).

**Purpose:** make the human fidelity-audit *cheap* — else it decays → counterfeit-green. Per invariant node,
render the **derived claim beside its source prose** so a fidelity mismatch is spottable in seconds:

`[node-id] | SHADOW one_liner | DYAD.md source-excerpt | match?`

A **2nd-order generated** view (a renderer reads `yaml` + `DYAD.md`), **regenerated on demand** (transient; NOT committed — like `rendered.md`'s in-memory render; the gate is *running* `audit_view.py`, not a stored transcript).

**Requires a per-node source reference** — the yaml `home` is *section*-level (too coarse for sentence-level
side-by-side; several nodes share one `home`). **Recommended: a per-node `source_quote`** (the exact `DYAD.md`
sentence the `one_liner` extracts), because it *also* enables a **mechanical verbatim-containment gate** — the
quote must appear in `DYAD.md` → catches a class of E1 drift the lexical coverage-diff misses (the *one* slice
of fidelity the machine *can* certify: that the cited source text is real, even if it can't certify the
paraphrase is faithful). **Tension to dispose:** `source_quote` re-introduces a source *excerpt* in the yaml —
cf. the ratified (b) lean-tag/sidecar design that avoided content-dup. The quote is a *derived, checkable
excerpt* (regenerated, gate-verified), not a rival content-home — but it trades lean-yaml for
audit-precision + a partial fidelity-gate. → the build-fork below.

## The worksheet model — LANDED *(Operator `land` 2026-06-27; the frame that resolves "which is source")*

The change-propagation thread converged on an analogy that **dissolves** the source-of-truth confusion the
`src/obj` (compiler) framing created. The three artifacts are three **stages of materializing intent**:

```
unstructured raw input  →   worksheet        →   final output
   (prompt / chat)          (invariants-bond.yaml)   (DYAD.md)
   THE SOURCE = intent      structure + VALIDATE     hand-crafted DELIVERABLE
                            (DAG/coverage-checked;    (the ingrain / boot surface;
                             kept for audit/recompute, the operative anchor)
                             NOT the deliverable)
```

- **Neither the yaml nor the md is "the source" — the *intent* is** (the chat prompt; → the change-vector
  reframe earlier in this section). This is why the yaml *feels like it leads* (you work in the worksheet
  first) **without** being authoritative-as-source: the **output** is what ships and what the LLM ingrains.
- **The yaml's true type is WORKSHEET** — the structured surface where messy intent is *organized and
  validated* (what `invariant-eval` + `anchor_dag_diff` literally do). A *kept* worksheet (version-controlled,
  re-runnable), but not the deliverable. This **sharpens** the 2026-06-17 "yaml is a DERIVED intermediate"
  line: it is an *active working/validation surface*, not a passive byproduct.
- **The md is the FINAL OUTPUT — hand-CRAFTED from the validated worksheet, NOT compiled from it.** The
  worksheet *informs* a crafted output (compute on scratch paper, then *write* the clean answer); it does not
  mechanically emit it. This re-confirms the 2026-06-16 survivor (*prose is the operative form, not generated*)
  on a sharper basis.

**Why CRAFT, not COMPILE (the `yml=src → md=obj` inversion, rejected — `bond:no-dogma` re-run, true-for-now):**
the compiler model is *internally* coherent (determinism would guarantee consistency), but it loses on three
counts: **(1)** the boot surface must be *crafted* prose — a deterministic template flattens (cf.
`rendered.md`, explicitly *not* the ingrain surface) and an LLM compiler re-introduces the non-determinism/
contamination `anchor_dag_diff` was designed to exclude; **(2)** "a compiled anchor ingrains as well as crafted
prose" is **untested** — the lone falsifiable, and adopting on it un-run would be assert-not-instrument; **(3)**
wu-wei — a prose-compiler is a bigger build than the unbuilt extraction engine, heavy force for a *contained*
drift problem (one re-altitude todo, already held by the gates).

**The worksheet → output gate** (keeps the crafted md consistent with the validated worksheet — neither is
purely upstream): **completeness** via the round-trip (`anchor_dag_diff`: every prescriptive line ↔ a node) +
**fidelity** via the side-by-side audit view (`audit_view.py`: each worksheet `one_liner` ↔ its verbatim `output_quote`).
The audit-view is therefore **not** a stopgap-for-a-missing-compiler — under the craft reading it **is** the
keystone worksheet→output gate.

**Follow-on RESOLVED (Operator `retire rendered.md` 2026-06-27):** `invariants-bond.rendered.md` is **RETIRED**.
The md prose is the human form; the audit-view is the fidelity check; the round-trip renders **in-memory** (no
committed digest). `bin/anchor_dag_diff.py`'s default staleness-gate is off (`RENDERED_DEFAULT = None`;
`--rendered FILE` stays opt-in). Live refs repointed: `views/invariants-bond.md` (constitutional block → the
output + audit-view), the yaml header, this chain. Historical refs (the 2026-06-16 ATTACK narrative, `P4`
records, the migration plan) kept under the name written under.

## Cross-links
`anchor-dag-thesis.md` (S1: state-to-falsify) · `dyad-dag-derivation.md` (the two-layer cut this rub
re-rubs) · `bin/anchor_dag_diff.py` (the gate) · `invariants-bond.yaml` (the shadow) · `DYAD.md` (the
source-of-truth that survived).

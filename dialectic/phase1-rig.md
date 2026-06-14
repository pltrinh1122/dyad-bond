# Phase-1 generator-rig — IV vs IV_it *(Operator dispose 2026-06-14; CANDIDATE, first run n=1)*

> **Provenance:** Operator `rub` → dispose 2026-06-14: *"generator-rig for phase 1 to answer: does IV
> (invariant) without intent_grounding produce as reliably as IV_it (invariant-grounded-on-intent)?"*
> Instance choice: **generator-rig in this repo** (not a clone-dyad — no Operator-bond, so no
> ionic-object; runs as a script + corpus on the branch). Files: `bin/phase1_rig.py` ·
> `dialectic/phase1-corpus.yaml`.

> **⚠ BIAS AUDIT — claim DOWNGRADED (Operator rub 2026-06-14, "looking for biases").** The headline
> below ("IV ≡ IV_it as a detector") is **not an empirical reliability finding** — it is a **code-fact**:
> in the current evaluator `grounded_in` is referenced only by the termination check, so deleting it
> *cannot* move a detection line **by construction**. The rig therefore **cannot fail** the "grounding is
> detection-inert" hypothesis → it re-derives a schema design decision = **counterfeit-green** (validates
> FORM, narrated as TRUTH; the recurring "reachable not valid instrument" pattern). Three more biases:
> (1) **question-substitution** — the Operator asked for reliable *outcome*; this measured *static
> schema-verdict*; (2) **operationalization-by-construction** — IV built by *deletion*, a strawman arm;
> (3) **confirmation corpus** — hand-authored to pass, n=1, the disconfirming case (an invariant whose
> violation-condition reads its intent) excluded; single evaluator (no triangulation); author = runner =
> interpreter = self-critic (no independent half). **What survives:** the code-fact that grounding is a
> *traceability* field, not a *detection* field, in this schema. **The reliability question is UNTOUCHED**
> — it needs the dynamic/outcome rig. Read everything below as schema-cartography, not science.

## The question, made falsifiable

- **IV** — an invariant **without** intent-grounding (no `grounded_in` serves-edge to an intent root).
- **IV_it** — the same invariant **grounded on intent** (a serves-edge whose chain terminates at an
  Operator-adjudicated root; `root_kind: fiat` roots **are** the intent).
- **"as reliable as"** — operationalized as: *same verdict from the reference evaluator*
  (`bin/invariant-eval.py`) across breach-detection, conflict census, pincer, duty-detector.

## The rig

Reuses the reference evaluator (does **not** re-implement it — stays on the commissioner's Validate-half,
the over-tooling line held). Two acts only: (1) derive the **IV arm** by stripping `grounded_in` from
every non-root; (2) run both arms and diff. Deterministic: same corpus → same diff (the Phase-1 criterion).

## Finding (n=1, this corpus) — **mechanically, IV is as reliable as IV_it. That is the answer, and it is not the reassuring one.**

The diff `IV_it → IV` changed **8 lines, 0 of which touch breach / conflict / detector**:

```
-[PASS] bond:ORI-C3                        +[FAIL] grounded_in: REQUIRED (per root==false), missing
-[PASS] bond:NOCAVE                        +[FAIL] grounded_in: REQUIRED (per root==false), missing
                                           +NO-TERMINATION bond:ORI-C3 / bond:NOCAVE
```

**Intent-grounding's entire mechanical footprint is graph-termination.** Strip it and the invariant
detects breaches, resolves conflicts, and trips the pincer/duty censuses **byte-identically** — because
`grounded_in` is read in exactly one place in the evaluator (the termination/orphan check) and **nowhere**
in the breach/conflict/detector logic. So:

- **As a breach-detector at the instant of evaluation, intent-grounding buys nothing.** IV ≡ IV_it.
- **What it buys is *termination* — traceability to an adjudicated intent.** The schema already encodes
  this verdict: `grounded_in` is `required_iff root == false`, so an *ungrounded* non-root invariant is
  **schema-illegal** — excluded not because it detects worse, but because it cannot be traced to an
  intent. Grounding is an **accountability** property, not a **detection-reliability** property.

## The rub — this null is *static*, and static is blind to where grounding actually earns its keep

"Reliable" measured as *one-shot breach-firing* is **rigged to return a null**, because the detector never
reads grounding. The honest claim is two-sided, and the second side is what the rig **cannot** see:

| Dimension | IV vs IV_it | Measurable by this rig? |
|---|---|---|
| One-shot breach-detection | **IV ≡ IV_it** (proven) | ✅ yes — the finding above |
| Re-rub / drift over context-shift | **IV < IV_it** (IV has no intent-root → nothing says re-rub it → it goes stale silently; the evaluator's `staleness` check is sha-based, intent-blind) | ❌ no — needs a perturbation rig |
| Conflict resolution | **IV < IV_it** (the census *flags* conflict but resolution = climb to a shared intent-root for super-invariant/rescope; IV can only thrash — the touchstone no-precedence problem) | ❌ partial — flag yes, resolve no |
| Accountability ("why does this rule exist?") | **IV < IV_it** (IV is an orphan; you cannot adjudicate keep/cut without the intent it serves) | ✅ yes — orphan flag |

**So the Phase-1 answer:** *IV is exactly as reliable as IV_it at the instant of detection, and strictly
less reliable across time, under conflict, and for accountability.* Reliability-at-an-instant ≠
reliability-across-context-shifts — and grounding lives entirely in the second.

## Refuted-if / watches

- **The whole intent→invariant seam is theatre** — *refuted-if* a perturbation rig shows IV ≡ IV_it even
  under re-rub/drift/conflict. Then grounding buys neither detection nor resilience and the
  `intent → invariant` arrow in the substrate-primitive collapses. **(The strongest possible result —
  watch it hardest.)** This rig cannot reach it; it is the next rig's job.
- **Counterfeit-null** — reporting the static "IV ≡ IV_it" *as if* it answered the reliability question is
  the same counterfeit-green pattern one altitude up. Guarded by stating both sides above.
- **n=1, hand-built corpus** — the corpus was authored to pass cleanly so the diff isolates one variable;
  a real extracted corpus may differ. Re-run on `invariants-stress.yaml` once it is schema-clean.

## Next probe (converge-open, no CTA)

The **perturbation rig** (Phase-1b): feed each arm a context-shift and a conflicting pair, measure whether
IV_it *recovers/resolves* where IV *drifts/thrashes*. That is the rig that can actually refute the seam —
this one only proved the seam is invisible to a static detector (which it had to be).

## Cross-links

- `substrate-primitive.md` — the `intent → invariant → ground` pipeline this rig tests the first arrow of ·
  `invariant-schema.yaml` — `grounded_in required_iff root==false` (the schema's standing verdict) ·
  `bin/invariant-eval.py` — the reference evaluator reused · `bin/phase1_rig.py` + `phase1-corpus.yaml`.

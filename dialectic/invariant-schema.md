# Invariant — formal definition + schema *(CANDIDATE, s15 2026-06-12; under falsification)*

> **Provenance:** Operator riff — the extraction stack (engine B-1, views, conflict-detection) operated
> on an undefined term. Consumers sizing the schema: (1) the extraction engine, (2) the Operator's
> evaluation view, (3) the super-invariant/rescoping experiment (Q3). **Guard: fields enter only on
> consumer demand** (the touchstone lesson — no speculative ontology).

## Definition — the membership test (falsifiable)

An **invariant** is a *standing, falsifiable prescription*. Membership requires the ability to state
ALL THREE:
1. **SCOPE** — the situation-class it binds (when / where / whom).
2. **PRESCRIPTION** — the deontic content (what it demands or prohibits in scope).
3. **VIOLATION-CONDITION** — what observably counts as breach (the invariant's own oracle).

Plus two standing-attributes: **ratification provenance** (else it is a *candidate*) and a
**true-for-now stamp** (invariants are cached verdicts — the no-exemption principle applies to them;
re-rub at context-shifts).

**Exclusions (what fails the test, and where it goes instead):**
- no violation-condition → **value / preference / fiat** (unfalsifiable; unilateral — cf. touchstone
  pin-protocol's fiat/claim split) → not extracted as law.
- past-tense, binds nothing forward → **finding / proof** → Ledger.
- steps, not constraint → **procedure / playbook** (may *embed* invariants; is not one).
- describes a tendency or defect ("you over-produce under correction") → **history wearing law's
  clothes** → Ledger. *(The membership test is therefore a PRUNE INSTRUMENT: applied to a boot-surface,
  it mechanically sorts the H3-class re-priming mass out of the anchor.)*

## Schema (v0.1 — seven fields, by consumer demand)

| Field | Consumer | Content |
|---|---|---|
| `id` | engine | durable, unique (`<dyad>:<ID>`) |
| `home` | engine, view | single-home source ref (file §) |
| `one_liner` | engine, view | stored canonical compression — authored at ratification, never regenerated |
| `status` | engine, view | ratified · candidate · inherited · kb · retired (+ provenance: date/event) |
| `scope` | conflict-detection | the binding situation-class |
| `prescription` | conflict-detection | the deontic content (MUST / NEVER / ONLY-BY) |
| `violation_condition` | conflict-detection | observable breach criterion |

**Deferred candidate-fields** (add only when a consumer demands): supersedes/lineage · ttl/re-rub
triggers · enforcement (hard-oracle vs soft-discipline) · conflicts-with/reconciled-by edges.

## Decomposed sub-schema *(v0.2 — Operator rub: decompose until validation is computable, stop before deontic logic)*

| Part | Sub-field | Vocab | Required |
|---|---|---|---|
| SCOPE | `actor` | agent · operator · both · any-dyad | ✓ |
| SCOPE | `trigger` | seam-taxonomy (selection-seam · outward-publish · ratification · anchor-edit · …, grows on demand) | ✓ |
| SCOPE | `condition` / `exclusions` | free (narrowing only) | — *(a RESCOPE-resolution = add an exclusion: mechanical field-edit)* |
| PRESCRIPTION | `modality` | MUST · MUST-NOT · ONLY-BY · ONLY-AFTER | ✓ |
| PRESCRIPTION | `action` (+`object`) | act-class | ✓ |
| VIOLATION | `observable` | tool-log · diff · ledger-line · transcript-turn · … | ✓ |
| VIOLATION | `detector` | **hard-oracle · soft-record · other-half-only · unobservable-from-inside** | ✓ |
| VIOLATION | `breach-example` | lived scar ref | — |

- **Computable semantics:** scope-overlap = actor-compatible ∧ trigger-intersection; opposition = same
  `action` + clashing `modality`. Conflict-detection → typed near-computation.
- **Semantic residue CONCENTRATES in trigger-equivalence** (one field, not three blobs) — place-and-bound,
  never eliminate; the seam-taxonomy is the controlled-vocab squeeze on it.
- **4th consumer discovered — the enforcement roadmap:** `detector` stratifies the set by enforceability;
  `hard-oracle`-able rows = the mechanization/CSI-guard queue; the rest are discipline by structure.
- **Smoke test (3 real invariants):** D6 → ONLY-AFTER source-query / tool-log / hard-able (matches
  touchstone's racked scanner independently). Op-rub-inv cond-2 → MUST-NOT cite-unrubbed / ledger-line /
  soft-record. **C1 NON-NEGOTIABLE → ONLY-BY surviving-genuine-falsification / detector:
  other-half-only/unobservable-from-inside — the schema CORRECTLY refuses to claim the keystone is
  mechanically validatable** (a decomposition that claimed otherwise would be lying; this one stratifies).
- **Cost (TS-3):** 6 required sub-fields per invariant = commissioner practice-hours at every
  ratification — accepted only because conflict-detection is a LIVE experiment, not speculative tooling.

## Conflict semantics *(what the schema buys the Q3 experiment)*

- **conflict(I₁, I₂)** ≝ scope-overlap ≠ ∅ ∧ prescriptions oppose on the overlap.
- Resolution types: **rescope** (refine scopes → overlap ∅) · **super-invariant** (a third invariant
  entailing both under refined scopes) · **precedence** (explicit ordering — e.g. the NON-NEGOTIABLE
  outranks; NB touchstone has NO precedence layer → conflicts thrash instead of resolving) ·
  **dissolution** (retire one side — touchstone cycle-39).
- Lived instances, typed: op-rub-invariant cond-1 evidence-base reading = *rescope* · "intent is
  true-for-now" = *super-invariant* · cycle-39 ask-don't-assert = *dissolution*.

## Orthogonality rub *(v0.4 — Operator rub: 3 non-orthogonalities found + 1 walk-back; the triad restated)*

- **Membership triad RESTATED: SCOPE | PRESCRIPTION | OBSERVABILITY** — `violation_condition` was
  derivable (breach ≝ in-scope act contrary to modality → entailed by the first two); the genuinely
  independent third axis is epistemic: `observable` + `detector` (how breach is KNOWABLE). The axes are
  now different KINDS — situational · deontic · epistemic — the signature of true orthogonality.
- **`trigger`⟂`action` normalization rule:** trigger = coarsest seam-taxonomy token, may NEVER contain
  the regulated act; act-bound prohibitions derive trigger (≝ attempt-context). Else two taggers split
  the same content across the two fields and the census misses collisions.
- **`via` field added** (required iff modality ∈ {ONLY-BY, ONLY-AFTER}): the licensed path is neither
  modality nor action — the smoke test had already forced it into existence undeclared (the
  NON-NEGOTIABLE's "surviving genuine falsification"). Census use: ONLY-BY collisions = via-paths vs
  other invariants' actions.
- **`one_liner` declared denormalized-display:** the tuple is semantics, the one-liner is projection;
  disagreement = tagging defect (heuristic lint only — accepted residue).
- **⚠ Walk-back on the pincer-census ✓:** computable over DEONTIC prohibitions only; touchstone's H2
  was partly VALENCE-scored (grains "scored bad," not MUST-NOT) — valence is out-of-schema → valence-
  pincers stay G-side (no scored-registry model absent a consumer; TS-1).
- Survived clean: `status`⟂`detector` (provenance vs epistemics); `actor`~`detector` correlated-by-design
  (detector values are actor-relative, declared).

## Tension-pattern annex *(v0.3 — Operator rub: conflict ≠ tension; the strict semantics alone would have missed H1/H2/H5)*

Strict conflict (same `action`, clashing `modality`, overlapping scope) = tuple-comparison →
**mechanical candidate-pairs** (catches touchstone's cycle-39 ask⟂never-ask instantly). TENSION
decomposes into four patterns with different mechanization status:

| Pattern | Relation | Mechanizable from v0.2? | Lived case |
|---|---|---|---|
| **Pincer** | a trigger's action-space covered by prohibitions, no affirmative exit | ✓ NOW — polarity-census per trigger | H2 (uncertainty: add/hold/assert all scored) |
| **Duty-detector mismatch** | `actor: agent` ∧ `detector: other-half-only/unobservable` ∧ continuous duty — a law its bearer can't know it's keeping | ✓ NOW — field crosscheck | H1 (Observe-duty + introspect-is-shine) |
| **Gradient opposition** | prescriptions scaling oppositely with one situational variable | ✗ — needs a `gradient` candidate-field (add only when Q3 demands; TS-1) | H5 (force↑irreversibility vs respond-with-less) |
| **Resource competition** | jointly compete for a bounded resource | ✗ — out of schema | D5 ⟂ anti-cave (response-length) |

*(H3-class vigilance-relocation is NOT a prescription-relation — the MEMBERSHIP TEST/prune catches it.)*

**Pipeline placement (same as the engine — place-and-bound):** mechanical census = UNPRIMED candidate
generation (recall) → G rubs each flagged candidate (precision) → Operator disposes. This fixes the s15
methodology gap: the forensics sweep was primed by the subject's self-diagnoses; a deterministic census
over tagged tuples is the **unprimed detector the Q3 experiment needs** — isolating the question to
"can the LLM infer the super-invariant/rescope, given a mechanically-served collision."

## Falsifiers

- REFUTED as definition if a consensus-invariant of bond's (view C/D/R rows) cannot be expressed in the
  three parts without distortion — the test would be cutting law, not history.
- REFUTED as schema if the commission's tag-grammar round needs a field no consumer demanded (over-fit)
  or lacks one a consumer can't run without (under-fit).
- The prune-instrument claim is testable on touchstone's anchor: if the membership test does NOT cleanly
  separate their Inv-I/II/III (law) from their grain-descriptions (history), the sieve fails.

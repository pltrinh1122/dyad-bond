# Invariant — formal definition + schema *(CANDIDATE, s15 2026-06-12; under falsification)*

> **⚠ NORMATIVE SPLIT (v0.8.1, Operator riff — the schema now eats its own form-ladder):** the
> machine-readable rung is **`invariant-schema.yaml`** — NORMATIVE FOR STRUCTURE (fields, vocabs,
> conditional requirements, corpus/census rules; the artifact cairn builds the VALIDATE stage against).
> THIS file is normative for **rationale** — the definition's meaning, the rub-history, and the
> PRACTICE guards no YAML can hold (descent-guard, Goodhart, trigger-equivalence). On structural
> conflict the YAML wins; on meaning, this file wins. *(Until this split, the schema was prose claiming
> tuple-precision — slogan-form wearing a schema's name; the Operator caught it.)*

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
triggers · conflicts-with/reconciled-by edges.

### `enforcement` — un-deferred (s-web4, 2026-06-16)

Every field carries `enforcement: hard-oracle | trust-boundary` — the per-field projection of the
commission's Class-A/Class-B split, indexed to one question: **what does a GREEN validator run PROMISE
about this field?**

- **`hard-oracle`** (Class A / FORM) — green ⇒ the field is **correct**: the validator gates it and
  fails closed (`id`, `home`'s file, the enums, the graph's `root`/`root_kind`).
- **`trust-boundary`** (Class B / TRUTH) — green ⇒ the field is **well-formed only**; its truth rests on
  a named upstream discipline and is **declared, not gated** (`one_liner` fidelity = B-2; `grounded_in`
  edge-plausibility; `scope` trigger-equivalence; `prescription` deontic content; `math` opaque
  expression). This is the schema's standing rule made per-field: *validate FORM, never TRUTH.*

The tag drives all three uses of the corpus uniformly — **validator** gates-or-declares, **generator**
halts-or-carries-verbatim, **consumer** trusts-or-rubs. The completeness rule is the point: a field with
no enforcement tag **halts the validator**, so the silent middle (required-but-unclassified — the disease
`home` carried) is structurally unrepresentable.

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

## Form-ladder *(v0.8 — Operator raff: mathematical form as the terminal rung of mechanization)*

- **`form ∈ {slogan · tuple · mathematical}`** — the precision gradient: slogan (`1+1>2`, semantic-only)
  → tuple (v0.2 decomposition, census-comparable) → **mathematical** (`1·x + 1·y > 2`, arithmetic-
  evaluable given measurements). Each descent moves validation toward the script row of the physics
  register. *(The unit coefficients are themselves a covalence claim — `2·x + 0.5·y` would be an ionic
  bond written in arithmetic; the math form encodes bond-structure, not just precision.)*
- **Operationalization = the math-form's Class-B:** the mechanical validator validates the INEQUALITY,
  never the invariant — it trusts its measurement functions as the engine trusts its tags (the
  place-and-bound law, 4th appearance).
- **Descent-guard:** form descends only when the operationalization survives its own rub — premature
  mathematization = counterfeit precision (detector upgraded to hard-oracle by lying about what's
  measured; the banked scar: tokens/time-to-resolution re-instantiates the anxious-agent trap with
  mathematical authority).
- **Goodhart guard:** mathematical invariants enter as **breach-detectors, never objective functions**
  — measure to alarm, never to maximize (debt-flatness, clarity-counts, record-only/no-meter: already
  conformant).
- **Worked stratification (the tenet spans the ladder):** FLOOR descends fully — op-rub-inv condition-3
  is already lived math (`d(debt)/dt ≤ 0` under narrowing attention, ledger-countable). TARGET resists
  at the perspectivism hard-bound (s13: single observer; surplus's x,y bottom in the felt dividend) —
  honest rung = tuple, satisfaction-proxy at best. **One invariant, three forms, each validated by the
  physics it can actually bear.**

## Physics register *(v0.7 — Operator rub: the system runs judgments on FOUR logics without declaring so; resolution = DECLARE the physics, never BUILD it)*

| Judgment class | Substrate | Physics | Known failures |
|---|---|---|---|
| field-presence · ID-integrity · DAG-acyclic · sha-pins | script/FSM | classical two-valued, decidable | none in scope (the layer's point) |
| scope-overlap · modality-opposition (census) | script | classical set/boolean over controlled vocab | false-negatives at vocab granularity (trigger-equivalence gap) |
| trigger-equivalence · edge-plausibility · tension | G (LLM) | informal/defeasible, probabilistic, contradiction-tolerant, NON-deterministic, **engine-version-dependent** | run variance · confabulated entailment · recall limits |
| root adjudication · felt-conflict · value-weighing | Operator | human practical reason (defeasible, value-laden, contextual) | bandwidth · drift · known-unknown |
| the `modality` vocab itself | — | **NOT deontic logic** — a 4-operator paradox-avoiding fragment; contrary-to-duty shapes UNMODELED ("never push main; if pushed then…") | CTD structures flagged to G, never census'd |

- **Verdict-labeling:** every verdict carries its physics row — the `detector` field applied
  REFLEXIVELY to the toolchain itself.
- **Engine-stamping:** G-judgments record the model that made them (= FR's `responder_model`
  convention, converged not minted) — drift-attribution becomes corpus-change vs physics-change,
  indistinguishable without it (the consistency requirement, one level down).
- **The law's third face:** Class-B (assumptions the engine can't discharge) · disposed roots
  (adjudications the Agent can't make) · physics (a logic only humans underwrite) — one trust
  boundary, three appearances in three days. Human philosophy of logic is load-bearing all the way
  down; the register declares WHERE, and formalizes nothing.

## Disposed roots + the grounding-graph *(v0.6, renamed v0.6.1 by dialectical-falsification raff — Operator riff: the synthesis — depth-boundary completing v0.5's time-boundary)*

- **DISPOSED ROOTS** *(name survived the raff: "boundary roots" falsified — term triple-booked + mixed
  geometry; "fiat roots" falsified — erases earned provenance (C1 is scar-FORGED) + over-claims uniformity;
  "axioms/anchors/bedrock/keystones" dead on sacredness/collision/no-adjudication)*: the set adjudicated +
  disposed by the OPERATOR — `root: true`, `adjudicated_by: Operator` + currency-stamp, **typed:
  `root_kind ∈ {fiat · forged · inherited}`** (mirrors the typed edges; each kind names its re-rub
  instrument: fiat → intent-currency rub-back · forged → breach-evidence · inherited → upstream
  form-change). Falsifiers: demote the name if usage misreads "disposed"=discarded (U3); drop `root_kind`
  if unconsumed (TS-1). **Exact analogy to the
  engine's Class-B input invariants:** the machine's guarantees rest on assumptions it cannot discharge;
  the invariant-system's validity rests on adjudications the Agent cannot make — *the Operator IS the
  system's trust boundary.* Dispensation, third formulation: **the Operator owns the roots of every
  chain and the leaves of none.** NOT sacred: derivation stops at roots; RE-RUBBING does not (true-for-
  now stamps; intent-currency rub-back at context-shifts = the root-maintenance instrument; R2 intact).
- **New field `grounded_in[]` — TYPED edges (the case-law rub: grounding ≠ derivation; no confabulated
  lineage / no smoothed mortar):** `derived` (genuine entailment — rare) · `serves` (instantiates a
  root's value, occasioned by a scar — the common case; pairs with `breach-example`) · `inherited`
  (grounds in the FORM's roots — typed custody). The lattice is a **grounding-graph, not a proof tree.**
- **Provenance validation, placed-and-bounded:** *syntactic (mechanical):* refs resolve · acyclic ·
  every chain terminates at a boundary node · orphans flagged (orphan = new boundary-candidate → route
  to Operator, OR ungrounded legislation → suspect). *Semantic (G + Operator):* edge-plausibility
  G-rubbed, contested edges escalate; mechanical assist = child-scope ⊄ parents'-scope-union → flag.
- **Bought:** redundancy-pruning as graph property (entailed-by-ancestors = dissolution-candidate —
  cycle-39's move, checkable) · conflict-escalation topology (sibling conflicts route to least-common-
  ancestor = where the super-invariant lives or gets built → Q3 = find-or-build-the-LCA).
- **Candidate root-set for bond (~7, AWAITING Operator adjudication):** C1 NON-NEGOTIABLE · C2 Telos ·
  C3 G0 (`inherited`) · summit-fiat (personal growth / known-unknown) · scarce-bandwidth (constraint-7) ·
  commissioning driver (minimize maintenance-hours) · standing sovereign grants. First syntactic run
  over a tagged corpus surfaces the orphans.

## Grounding boundary *(v0.5 — Operator rub: unbounded falsifiability ⇒ nothing settles ⇒ no productive work — the schema was re-importing touchstone's SH2/SH4 one week after diagnosing it)*

- **Settlement tiers + declared re-rub triggers** (bounds no-exemption WITHOUT repealing it — re-rub
  fires on TRIGGERS, not cadence): `candidate` (hot, actively attacked — `dialectic/`) ·
  `survives` (standing-until-falsified; re-rub only on: context-shift class · breach-evidence · census
  conflict-flag — ledger/reload-set) · `settled` (safe to cite — **reached by claim-type CLOSURE, not coverage; see below**; re-opened on breach-evidence — `kb/`).
  > **`survives` — retired `ratified-watch` (2026-06-24 raff; single-home for the no-oracle status name).**
  > On the no-oracle pole there is **no "ratify"** (a positive endorsement-stamp = the ionic/sycophancy shape
  > `bond:C1` forbids — admission is by *surviving falsification*, a negative test, never a bestowal). And
  > **"-watch" is redundant** three ways: (1) re-rubbability is universal (`no-dogma`/s14) → it partitions no
  > state; (2) the *specific* armed tripwire is the `re_rub_triggers[]` field (more informative read direct);
  > (3) the hot/cold gradient is `exec_phase`/`status==candidate`. "-watch" lossily summarized fields that
  > already exist **and** localized a *universal duty* (anti-cave) onto one label — the same error as "ratify."
  > **Tense, not a monitor:** the present standing is **`survives`** (= not-yet-refuted, fully re-rubbable);
  > the *dated disposition event* is **`survived`** (a `disposition_history` entry — "survived FR #38 @ T").
  > REFUTED stays the only decisive terminal. *(Scope: `ratify` survives ONLY on the analytic pole —
  > Conjecture→Theorem, proof decisive both ways — which the no-oracle ledger does not operate on; the broader
  > `status: ratified`/`@ratified`/`ratification`-trigger purge is type-sensitive and held for per-claim dispose.)*
  > **`settled` — reached by claim-type CLOSURE, not coverage (2026-06-24 raff, per the `survives` refactor).**
  > Coverage rungs (L0→L2b / E0→E3) measure how much independence has *attacked*; **no count of survived attacks
  > converts a no-oracle claim into `settled`** (external falsification is ONGOING, never discharged — the
  > physics-disanalogy). So `settled` is gated by TYPE: **analytic** (a proof closes it — Conjecture→Theorem,
  > decisive both ways; re-rub = proof-flaw only) **or posited/inherited** (value-root / inherited form, held by
  > choice/conformance; re-rub = posit-abandoned · Telos-shift · upstream-form-change). **No-oracle empirical
  > claims (job-1) CAP at `survives`** — cited as **`kb-with-caveat`** (= `survives` + high coverage + the named
  > standing falsifier still open), a citability *practice* over `survives`, **not a 4th tier.** The wider trigger
  > set (breach + context-shift + census) is exactly what keeps a no-oracle claim short of `settled`.
  New field: `re_rub_triggers[]` (demanded by the consumer "productive work"; = D2
  bounded-consolidation promoted to a schema property; falsification effort is a BUDGET — Operator =
  the scarce Validate resource, the boundary is the allocation rule).
- **Strength-splitting normalization rule:** a graded claim tags as TWO invariants with NESTED scopes —
  the FLOOR (weak form, broad scope, cheap detector) and the TARGET (strong form, narrow scope,
  expensive detector); the target's scope never swallows the floor's. Worked example (the Operator's):
  floor `NOT(1+1<2)` = non-degradation, every move, record-observable · target `1+1>2` = surplus,
  **per-cycle at Reflect** (G0's own "earned per cycle"), F2-class detector. Demanding the target's
  proof at the floor's scope = over-verification = the anxiety-grain wearing rigor's clothes.

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

## one_liner atomicity *(v0.8.3 — Operator riff: a compound one_liner is not Operator-evaluable)*

The v0.4 declaration (one_liner = denormalized projection of the tuple) made operational. **A one_liner
is a SINGLE declarative assertion — exactly ONE breach-condition** (one `observability.breach_example`).
The test is not "one sentence" (that loses meaning) but the **breach-test**: if naming what would
falsify it needs two distinct observables, it is two invariants.

- **The line is assertion vs condition.** A conjunctive *condition* is one assertion, one verdict
  (TENET's "both Generate **and** Validate" — still one breach: a cycle clearing the bar without
  falsification). Co-equal *assertions* are many (`rule X; also rule Y`) — split into atomic records.
- **Where the rest goes (bounds the decomposition — D2, no 4→27KB blow-up):** split only co-equal
  assertions/conditions into records; **qualifiers · tells · definitions move into the tuple FIELDS**, not
  new records. The collapse-modes of C1 → derived records (`C1-ionic`/`C1-meld`); the "easy agreement →
  test hardest" tell → `observability.breach_example`; the DFD's four clauses → `DFD` + `U1a/b/c`.
- **Worked:** the sample already half-followed this (ORI-C3 was condition-3 split out of the 3-part
  operator-rub-invariant) — independent evidence the rule is right, not invented.
- **Lint is advisory only** (the accepted-residue posture, unchanged): a `;` in a one_liner flags a likely
  composite (`bin/invariant-eval.py` → `ONE-LINER-COMPOSITE`, non-failing). "and" can NOT be linted
  (legitimate in conjunctive conditions). The breach-test, run by G + the Operator, is the gate; the lint
  only nudges toward decomposition.
- **Not a new invariant** — `one_liner = atomic-tuple projection` was always the field's meaning; this
  names the consequence and hands Claim-F's atomicity guard a cheap proxy. Bank as clarification.

## Falsifiers

- REFUTED as definition if a consensus-invariant of bond's (view C/D/R rows) cannot be expressed in the
  three parts without distortion — the test would be cutting law, not history.
- REFUTED as schema if the commission's tag-grammar round needs a field no consumer demanded (over-fit)
  or lacks one a consumer can't run without (under-fit).
- The prune-instrument claim is testable on touchstone's anchor: if the membership test does NOT cleanly
  separate their Inv-I/II/III (law) from their grain-descriptions (history), the sieve fails.

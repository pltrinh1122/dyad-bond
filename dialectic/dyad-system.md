# dyad-system — mechanizing the claim/invariant structure *(new arc, 2026-07-01)*

> **Status: IN-PROGRESS, design stage — no code yet.** Single-home for this arc (→ `deferrals.md`
> `## in-progress` points here). Born from the `bond:C1`/`bond:livability` validator-drift catch at
> resume (`carry-forward.md`, Stand-Up 2026-07-01) — a schema/corpus divergence that sat unnoticed
> because nothing gates `theory-pipeline.yaml` at all, and nothing caught `invariants-bond.yaml`'s
> drift until the validator happened to be run by hand.

## WHY (Operator's stated telos for the arc)
**Offload structural/mechanical checking off of attention and tokens, onto validated machinery.**
Not abstraction for its own sake — the test for whether something belongs in this arc is: *does
formalizing it move a currently-manual check (trust-boundary, paid for by whoever notices) onto a
gated mechanism (hard-oracle, paid for once, by the machine, forever)?* The `bond:C1`/`livability`
incident is the concrete motivating case: a schema-illegal edit sat in the corpus for a session or
more because the only gate (`bin/invariant-eval.py`) is opt-in, human-triggered, and the sibling
corpus (`theory-pipeline.yaml`) has no gate of its own at all.

## Scope
Mechanize the **claim** concept that already exists informally in prose (`carry-forward.md`'s
claim-axis / work-item-axis split: "Claims (belief-state) live on the claim axis
(`theory-pipeline.yaml` + `relationship-craft.md`)") across both places it currently lives
un-unified:
- `dialectic/theory-pipeline.yaml` — live, mutable, coverage-tracked candidates. **Zero mechanical
  validation today** (`bin/lifecycle_state.py` is a read-only projection — exit 0 rendered / 2
  load-error, never gates correctness).
- `dialectic/invariants-bond.yaml` — ratified, frozen, DAG-anchored invariants. Gated today by
  `bin/invariant-eval.py` against `dialectic/invariant-schema.yaml`.

## Design decisions reached (2026-07-01 session, dialectically — not yet built)

1. **Claim → Invariant is a `graduates-to` (produces) relationship, NOT `is-a` (inheritance).**
   A candidate is a live, mutable, open inquiry (`coverage`, `grade`, `prediction_pair`,
   `disposition_history` — fields that change on every attack). A ratified invariant is frozen and
   DAG-anchored (`root`, `grounded_in`, `prescription`, `math` — fields that only make sense once
   nothing is being investigated anymore). Graduating produces a *new* record, in a *different*
   file, under a *different* id-namespace, usually compressed (`statement` → `one_liner`) — not a
   mutated subtype continuing to exist. Modeling it as inheritance would force one validator to
   reason about a record simultaneously "still open" and "now frozen" — more mechanism, not less.

2. **Shared `claim-core` = a base CONTRACT both schemas independently satisfy, not literal
   subclassing.** What's actually shareable/offloadable: `id` pattern + **global** uniqueness
   (checked across *both* files — nothing stops a candidate id colliding with an invariant id
   today), a provenance/adjudication shape (who asserted this, when, on what basis), and a unified
   re-examination-trigger vocabulary (invariants use the closed `re_rub_trigger` enum; candidates
   use free-text `next_probe`/`open_gap` — two conventions doing the same job).
   **NOT shared:** invariant-only (`prescription`/`scope`/`observability`/`math`/`root`/
   `grounded_in` — meaningless pre-graduation) and candidate-only (`grade`/`coverage`/
   `prediction_pair`/`disposition_history` — meaningless post-graduation).

3. **`grounded_in` stays narrow (epistemic derivation, acyclic, terminates-at-root); a
   `depends_on` (precondition/viability edge) is a distinct, NOT-YET-BUILT relation.** Conflating
   the two (e.g. by widening `grounded_in`'s meaning and lifting its root-forbidden rule) would
   directly threaten the corpus's `grounding-graph: {acyclic: true, every-chain-terminates-at:
   "root == true"}` invariant — a root with outbound `grounded_in` edges risks cycles against the
   reverse `serves` edges its enablers already carry. **Prove-before-propose applies:** only one
   root (`bond:C1`) currently shows this precondition shape; `depends_on` doesn't get named/built
   until a second instance forces the generalization — building it for an audience of one is its
   own kind of imprecision (naming a general relation before there's a second case to check the
   name against).

4. **`Claim`/`Invariant` as validated factories mechanize SHAPE, not TRUTH.** `Claim.new()` /
   `claim.graduate(...) -> Invariant` would own: id generation + global-uniqueness check at
   construction (fail immediately, not at the next lint run), enum validation on construction,
   provenance/adjudication stamping, the unified re-rub vocabulary. They do **not** own: `one_liner`/
   `statement` semantic fidelity, `prescription` deontic correctness, `grounded_in` edge
   plausibility, whether an `observability` breach-example actually catches the breach — same
   ceiling the schema already declares in its own `not_in_this_file` residue list. This is a limit,
   not a gap to close later.

5. **Authoring-workflow consequence (named, not yet decided):** introducing a validated factory
   changes how future claims/invariants get created — from hand-authored YAML prose (today's mode,
   used for every record in both files so far) to a constructor call that then serializes into the
   YAML. The YAML files stay the single-home source of truth (the factory writes/validates *into*
   them, per the existing worksheet-model discipline — `dyad-md-yaml-regen.md`); it does not
   replace them with a hidden object store.

## Open (not yet disposed)
- Does the paused `bond:C1`/`bond:livability` corpus-correction (WIP commit `092cee9`, holding since
  the "correct the corpus" disposition) land first as its own small fix, or get absorbed into this
  arc's first `claim-core` pass? *(Leaning: land it first, separately — it's an immediate
  schema-conformance bug, not a mechanization design question; this arc can still reference it as
  the motivating incident.)*
- File/module layout for the factory (`bin/claim.py`? extend `bin/invariant-eval.py`? a sibling
  engine?) — unscoped.
- How a single factory call writes correctly into *two* independently-owned YAML files (candidate
  creation → `theory-pipeline.yaml`; graduation → also touches `invariants-bond.yaml`) without
  breaking single-home per-file ownership — unscoped.
- Whether `bin/invariant-eval.py` gets extended to also gate `theory-pipeline.yaml` against the
  shared `claim-core`, or a new sibling validator is built — unscoped.

## Next probe
Scope the `claim-core` field list precisely enough to write an actual sub-schema YAML (the first
falsifiable artifact of this arc) — that's the smallest next step that turns "design decided" into
something `bin/invariant-eval.py`-shaped can check.

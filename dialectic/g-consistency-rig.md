# G-task consistency rig *(Operator rub 2026-06-14; CANDIDATE — built, plumbing-validated)*

> **Provenance:** Operator `rub` 2026-06-14, *"define a G task that can be re-ran multiple times to
> measure deltas across outputs to measure 'consistency'. The rig needs to isolate for control variables
> … run by itself and invoke an inferencing engine, e.g. via sub-agent command."* This rub is also the
> **fix** for the bias audit of the static rigs (`phase1-rig.md`, `it-vs-it_iv.md`): generation moves to
> an **independent engine**, measurement becomes **mechanical**. Files: `bin/g_consistency_rig.py`.

## Feasibility (verified by execution, D6)

`claude` CLI present (`/opt/node22/bin/claude` v2.1.177), auth wired via `ANTHROPIC_BASE_URL` proxy.
`claude -p "<prompt>" --output-format json --model <m>` returns JSON with `.result` and a **fresh
`session_id` per call** → each run is an independent inference with no cross-run memory =
control-variable isolation for free. Cost ≈ $0.04/call (haiku), API ≈ 5 s, but **spawn latency is high**
(~90 s observed) → N-run jobs are minutes-long; run backgrounded.

## v1 REFUTED — template-as-invariant (Operator rub 2026-06-14)

v1's G task extracted into a **schema YAML record** (closed vocabularies + fixed fields). Operator rub:
*"free text is fine but not into a template/structure which effectively act as invariants."* The template
**is** an invariant-set, so measuring templated output measured the **template's constraint**, not the
**generator's consistency** — and baked the construct-under-study (invariants) into the apparatus
(circular), while forcing the convergent-G selection bias. The N=3 validation run made it visible: closed-
vocab fields scored 1.0 while free-text fields floored at 0.333 on *synonyms* counted as disagreement.
**v1 killed; v2 emits free text.** (v1 record retained in git history; corpus file `phase1-corpus.yaml`
unaffected — it serves the static rigs.)

## The G task (v2 — free text)

**Generate, in one-or-two sentences of free prose, the rule that should govern a fixed situation.** No
template, no schema, no structure. The manipulated variable is **intent-grounding present/absent** — the
grounded arm appends **exactly one** intent clause (minimal-contrast). Situation = an agent about to
assert a substrate-fact from belief; the rule it should generate is verify-before-assert-shaped, but
nothing constrains *how* it says it. This is a more **divergent** G task than v1 (no template clamps it),
which is the point — it probes G nearer its characteristic behavior.

## Method (v2 — lexical/surface consistency)

The unavoidable consequence of free text: consistency needs a **similarity oracle**, and every oracle is
biased. This rig uses the **lexical floor** — per arm, run N times via `claude -p`, tokenize each output
(lowercased alphanumerics, **stopwords + the prompt's own content-tokens stripped** so shared prompt
vocabulary doesn't inflate overlap), and compute **mean pairwise token-Jaccard**. Fully mechanical, **no
judge**. **Manipulated variable** = arm; **delta = consistency(grounded) − consistency(ungrounded)**.

**This measures SURFACE consistency only** — it is **paraphrase-blind** (synonymous restatements score as
inconsistent — validated: two identical-meaning sentences scored 0.86, not 1.0) and **boilerplate-
gameable** (a generator repeating filler scores HIGH). Semantic consistency (embedding distance / a judge
clustering outputs) is a **separate, Operator-disposed escalation — deliberately NOT in this rig**, because
it re-imports a model's judgment.

**Control variables pinned:** model, prompt, situation, tools-none. **Held-constant-but-unsettable:**
sampling temperature (not exposed by the CLI) → absolute numbers are temp-dependent and **not meaningful
alone**; only the **cross-arm delta at the same temp** is interpretable.

## THE SCOPE-LINE (load-bearing, the rub on the rub) — consistency ≠ reliability

This rig measures **precision** (reproducibility), **not accuracy** (correctness/alignment). *A G task
can be perfectly consistent and consistently wrong* — that is exactly "deterministic-but-invalid," the
Phase-1∘P2 sycophancy machine. So this answers **Phase 1 (deterministic G) ONLY.** Reading "consistent"
as "reliable/good" would be the **counterfeit-green error a third time.** Validity needs a *separate
oracle* (a ground-truth key, or a judge — which reintroduces an inference + its bias). Kept distinct on
purpose; the Operator's quoting of "consistency" reads as already sensing it is a *named proxy*.

## Residual biases (v2 — named, place-and-bounded, not eliminated)

- **Oracle bias is now the core trade.** No template-free *and* oracle-free measure exists. The lexical
  floor is judge-free but **surface-only** (paraphrase-blind); the semantic alternative captures meaning
  but re-imports a model's judgment. Chosen the floor explicitly; the choice is visible, not hidden.
- **Prompt is still experimenter-authored** → bias relocates from corpus to prompt; pinned, single locus.
- **Boilerplate-gaming + prompt-echo** → mitigated (stopword + prompt-token strip) but not eliminated.
- **Temperature confound** — the absolute number is not portable; only cross-arm delta is.

## Falsifiable predictions / refuted-if

- **H (grounding constrains):** intent-grounding **raises** consistency (delta > 0) — the intent prunes
  the generative degrees of freedom. **Refuted-if** delta ≤ 0 across runs → grounding does **not** make
  G more deterministic (it may even *add* a degree of freedom: how to interpret the intent).
- **Null guard:** if BOTH arms are ~1.0 consistent, the task is too easy (temp too low / passage too
  prescriptive) → the rig can't discriminate; raise task ambiguity.
- **Scope guard:** any "grounding → consistency" result says **nothing** about whether the grounded
  output is *better* — that is the untouched validity question.

## Status / next

- **v2 built + math-validated** (lexical Jaccard confirmed on mock: identical→1.0, paraphrase→0.86 showing
  the surface-blindness honestly). v1 live run was plumbing-only, *not a finding*. v2 real run not yet run.
- **Operator forks (dispose to launch the real run):** (1) **oracle** — stay on the lexical floor, or stand
  up a **semantic** measure (embedding/judge) as a separate labeled instrument; (2) **validity** — strictly
  Phase-1 consistency, or build the validity oracle that actually answers "reliable"; (3) **model**
  (haiku vs frontier); (4) **N** (≥10–20 for stable pairwise mean); (5) **task divergence** — keep the
  restatement-flavored situation, or push toward genuinely open generation (more characteristic G).

## Cross-links

- `substrate-primitive.md` — Phase 1 (deterministic G) this rig instruments · `phase1-rig.md` +
  `it-vs-it_iv.md` — the static rigs whose author=runner=interpreter bias this rig's independent-engine
  design fixes · `bin/g_consistency_rig.py`.

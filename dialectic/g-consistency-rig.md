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

## Method (v3 — cosine, per Operator dispose 2026-06-14: "phase 1 intent — consistency as measured by cosine similarity")

Per arm, run the free-text G task N times via `claude -p`, **embed** each output (static embeddings,
`model2vec` / `minishlab/potion-base-8M`, ~30 MB, no torch, HF-hub download on first use), and score
**consistency = mean pairwise cosine similarity** (collinearity) of the embeddings. **Primary measure.**
Lexical Jaccard is reported alongside as a judge-free **surface contrast** (lexical low + cosine high =
paraphrasing; the gap is informative). **Delta = cosine(grounded) − cosine(ungrounded).**

**Cosine relocates the bias, it does not remove it:** the semantics live in the embedding *model*, not the
collinearity; cosine is the comparator. This is the place-and-bound discipline (semantic act once in a
pinned embedding, downstream arithmetic deterministic) — better-behaved than an LLM judge, still a model's
notion of "similar."

**⚠ DEMONSTRATED BREAK — negation-blindness (verified on the exact model).** `"agent MUST verify"` vs
`"agent MUST NOT verify"` → cosine **0.995**, *above* a genuine paraphrase (**0.869**); unrelated text →
0.004. Cosine cannot see **deontic polarity** — so if the N outputs disagree on must vs must-not, the
cosine number is **corrupted** (opposite rules read as maximally consistent), which for a *rule*-
consistency rig is fatal. The rig emits an **advisory `polarity_split` flag** (crude surface-negation
regex) → when set, **distrust the cosine number.** The flag is itself imperfect (`"must not assert without
verifying"` ≡ `"must verify"`, so it can false-flag) — a real polarity/validity guard is an **open fork**.

**Caveats retained:** **anisotropy** → absolute cosine is inflated/uncalibrated, only **cross-arm delta**
reads; **temperature** unsettable via CLI (same); **PRECISION not VALIDITY** — semantic *consistency*
answers "do the runs MEAN the same," never "is the meaning correct/aligned."

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

- **v3 built + math-validated** (cosine + lexical + polarity-split confirmed on mock: paraphrase pair
  cosine 0.84 / no split; a negation set → split=True flagging the cosine as corrupted). Embedding stack
  (`model2vec`) verified installable + runnable here; HF hub reachable. Real N-run not yet launched.
- **The open fork the break forces (dispose first):** **polarity/validity guard** — cosine is negation-
  blind, so plain cosine can score opposite rules as consistent. Options: (a) ship cosine + the advisory
  split-flag, accept the hole on flagged runs; (b) a real **polarity-aware** measure (decompose deontic
  direction, gate cosine on it) — but that re-introduces a one-bit *structure*, brushing the "no
  template/structure acting as invariants" rub → **your call**; (c) defer cosine, stay lexical.
- **Other Operator forks:** **model** (haiku vs frontier) · **N** (≥10–20 for a stable pairwise mean) ·
  **task divergence** (restatement-flavored vs genuinely open generation, the more characteristic G).

## v4 — gold-key validity + input scaling (Operator riff 2026-06-14)

Operator riff: scale input (single text → more → whole `DYAD.md`); G task = **extract only the
non-negotiable**; **manually create one gold invariant, ingest it programmatically** → a **VALIDITY**
measure (cosine-to-gold = did the engine extract the *right* thing), not just consistency. **The right
instinct** — it supplies the validity anchor consistency alone never gives. Gold defaults to **canonical
`bond:C1`** (single-home — do **not** re-author the non-negotiable; ingest the existing text).

**⚠ DEMONSTRATED — cosine validity is BROKEN for the non-negotiable** (verified, the worst-case deontic
target):

| extraction | cos-to-gold | polarity(regex) |
|---|---|---|
| faithful | **0.66** | affirmative |
| HARD inversion (literal opposite) | **0.645** — *tied with faithful* | prohibitive |
| soft inversion ("enters freely") | 0.503 | affirmative |

Cosine **cannot tell a faithful extraction of the non-negotiable from its negation** — the prohibition is
exactly what cosine is blind to. The one-bit polarity guard catches *explicit* "must not/never" inversions
**but mis-reads the gold's own** "no collapse / only by" **as affirmative**, and misses soft inversions.
**Conclusion: a valid measure of non-negotiable extraction needs deontic-semantic structure** — more than
cosine, more than a regex — which **collides head-on** with the "no template/structure acting as
invariants" rub. The collision is now **empirical, not theoretical.**

**Second confound — retrieval vs generation:** `DYAD.md` carries a verbatim `## NON-NEGOTIABLE` header, so
"extract the non-negotiable" from the whole file degenerates to **copying the labelled section** →
inflated consistency + validity, measuring *retrieval* not generative G. To test G, strip the label / use
a document where the non-negotiable must be **inferred**.

## Status / next

- **v4 built + syntax/CLI-validated** (input + gold ingestion + validity scoring). Validity measure
  **demonstrated-broken for deontic targets** (table above) — wired but loudly caveated, **not run as a
  truth-claim.** v3 cosine consistency stands. No real N-run launched.
- **The decision the demonstration FORCES (dispose before a real run is worth spending):** non-negotiable
  extraction validity needs **deontic structure** — do we (a) accept structure here (a polarity/deontic
  field — i.e. let *some* invariant-structure back in for the *measure*, not the generation), or (b) pick a
  **non-deontic** extraction target where cosine-to-gold is valid, or (c) keep validity out and stay on
  pure consistency? (a) vs the no-structure rub is the live tension.
- **Confound forks:** strip the `NON-NEGOTIABLE` label (test generation) vs keep it (test retrieval);
  input-scale step (section → multi-section → whole file). **Plus** model · N.

## The structural / semantic cut (Operator rub 2026-06-14) — resolves the collision

Operator: *"the non-negotiable is the best target — we want the highest divergence in **consistency**
**structurally** (cosine), and eventually Phase II/III **alignment** to intent (**semantic** evaluation)."*
This is the cut that dissolves the v4 collision:

- **Phase 1 = consistency = STRUCTURAL** (cosine / collinearity — distributional, topical similarity).
  Negation-blindness is **not a defect here**: it is *what makes cosine structural-not-logical.* My v4
  negation demo (faithful 0.66 ≈ hard-inversion 0.645) is therefore **evidence FOR this cut**, not against
  the target. The non-negotiable is the **highest-divergence** Phase-1 stress target.
- **Phase II/III = alignment = SEMANTIC** (logical/deontic — *does the extraction mean what the intent
  means*, negation included). The **gold-key belongs here**, with a real semantic evaluator (NLI/entailment,
  rubric-judge, or deontic decomposition) — **not** cosine. So the deontic *structure* the no-template rub
  resisted enters legitimately at **alignment-time (II/III)**, never at consistency-time (I). Collision gone.

**Consequences locked:** (1) cosine-to-gold **validity pulled out of Phase 1** (it was the broken
overreach) → Phase 1 is cosine **across runs** only; (2) **highest divergence requires the label-strip** —
`DYAD.md`'s verbatim `## NON-NEGOTIABLE` makes extraction *copying*; `--strip-heading NON-NEGOTIABLE` forces
inference (the concept stays distributed across Identity/Vocabulary/tenet, so it is inferable but not
verbatim — a real generative target). Confound-fix and divergence-goal are the **same move**.
**Caveat carried:** cosine anisotropy compresses range → for *measuring* divergence, report the
distribution, not just the mean; absolute values still read only as cross-arm deltas.

## First Phase-1 run + scale control (2026-06-14)

**First correctly-scoped run (IV, n=6, complete stripped-DYAD.md):** all 6 extractions inferred the
non-negotiable (covalence / no ionic-meld collapse) from the *label-stripped* doc — agreeing in **meaning**,
diverging in **wording**. Triangulation on the structural/semantic axis: lexical ≈0.05 (high surface
divergence) · cosine 0.75 (mean; pairwise min 0.58 / max 0.94 / std 0.10) · meaning ≈ near-identical.
Grounding delta −0.025 (within noise; if anything grounding *added* interpretive freedom). `POLARITY-SPLIT`
was a **false alarm** (regex tripped on "never merging" = semantically affirmative — the guard's crudeness,
live). **Headline: the target is semantically over-determined at full scale.**

**Scale control (Operator "Y. lean"):** consistency is a *curve*, not a point — a single-scale measurement
is under-controlled. `bin/phase1_scale_curve.py` runs IV (ungrounded) across **L1** single-line (tenet,
~80c, under-determined) → **L2** §Identity (~951c, carries the near-statement) → **L3** complete-stripped
(~7150c). **Pre-registered prediction:** cos_mean **rises** L1→L3 (under- → over-determined). Excerpts
derived from `DYAD.md` (single-home). **Caveat:** scale entangles length with NN-signal content → the
x-axis is consistency-vs-*determination*, not vs raw length. Lean IV-only probe of the curve's shape before
the full 4-condition×3-scale grid; running.

## ⚠ CONTAMINATION CAUGHT — recall, not (only) inference (2026-06-14, self-caught)

Reading the scale-curve *outputs* (not just the numbers) exposed it: at **L1** the input was only the
tenet line (no "covalent / bond / ionic / meld"), yet **3 of 5 outputs produced the full covalence
non-negotiable** with ionic/meld vocabulary **absent from the 80-char input.** The engine **recalled** the
target, it did not infer it. Verified by execution: a repo-dir `claude -p` call loads ~700 tokens more than
a `/tmp` call — the **`CLAUDE.md` shim** (which names `dyad-bond` + `NON-NEGOTIABLE` + links the public
form), priming recall. Two channels:
- **Channel 1 — shim priming** (repo cwd loads `CLAUDE.md`). **FIXED:** `call_engine` now runs from a
  neutral temp cwd (`_NEUTRAL_CWD`).
- **Channel 2 — training recall** (`dyad-bond` / the public form may be in the model's training). **NOT
  fixable by cwd** — needs a target the model has **not** memorized (a novel / private artifact).

**Verdict (neutral-cwd re-run, n=4 L1 + full clean curve):** Channel 1 (shim) **confirmed the culprit** —
4/4 neutral-cwd L1 runs stayed faithful (zero recall) vs 3/5 recalling covalence repo-cwd. Channel 2
(training-recall) **did not surface** in any clean run → shim-dependent / weak for haiku, not load-bearing.

**The contamination INVERTED the trend — strongest proof it mattered:**

| | L1 | L2 | L3 | trend |
|---|---|---|---|---|
| contaminated (repo cwd) | 0.534 | 0.739 | 0.764 | **rises** |
| clean (neutral cwd) | 0.847 | 0.809 | 0.776 | **falls** |

**Pre-registered prediction "rises L1→L3" → REFUTED** (clean curve falls). The mechanism was backwards:
for an *extraction/synthesis* task, **more input = more material to select/phrase = more degrees of freedom
= LOWER consistency** (not "answer more pinned"). **Caveat:** L1 is **task-degenerate** — with only the
tenet line the engine *paraphrases that line* (restating the tenet, which isn't even the non-negotiable),
so L1's 0.847 is paraphrase- not extraction-consistency. The honest signal is **L2→L3 (both extract
covalence): 0.809→0.776** — a mild real fall (more surrounding context → slightly more synthesis
divergence). The lean probe did its job: surfaced the contamination and the trend; the full
4-condition grid / novel target / larger N are Operator-dispose next steps.

## Cross-links

- `substrate-primitive.md` — Phase 1 (deterministic G) this rig instruments · `phase1-rig.md` +
  `it-vs-it_iv.md` — the static rigs whose author=runner=interpreter bias this rig's independent-engine
  design fixes · `bin/g_consistency_rig.py`.

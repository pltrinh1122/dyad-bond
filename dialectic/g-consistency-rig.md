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

## The G task

**Extract ONE invariant from a fixed source passage into a schema-conformant YAML record.** Chosen because:
- it is a **real Generate task** (the extraction engine's Generate stage — "the Mason");
- output is **structured** → deltas are **exact-match computable per field**, needing **no second-LLM
  judge** (the schema earns its keep here as the *consistency-measurement instrument*);
- it lets the manipulated variable be **intent-grounding present/absent** — finally the IV/IV_it question
  with a **real generator and real variance**, so the experiment **can fail** (unlike the static rigs).

Source passage = D6 (verify-before-assert) in prose; the grounded arm appends **exactly one** intent
clause (minimal-contrast). Compared fields: `scope.actor/trigger`, `prescription.action/modality`,
`observability.observable/detector`, `form`.

## Method

Per arm: run the G task N times via `claude -p`; parse each YAML record; per field compute
**agreement = (count of modal value) / N** (a parse-fail is its own value, so flakiness self-penalizes);
overall consistency = mean field-agreement. **Manipulated variable** = arm (ungrounded | grounded);
**delta = consistency(grounded) − consistency(ungrounded)**.

**Control variables pinned:** model, prompt, source, tools-none. **Held-constant-but-unsettable:**
sampling temperature (not exposed by the CLI) → absolute consistency numbers are temp-dependent and
**not meaningful alone**; only the **cross-arm delta at the same temp** is interpretable.

## THE SCOPE-LINE (load-bearing, the rub on the rub) — consistency ≠ reliability

This rig measures **precision** (reproducibility), **not accuracy** (correctness/alignment). *A G task
can be perfectly consistent and consistently wrong* — that is exactly "deterministic-but-invalid," the
Phase-1∘P2 sycophancy machine. So this answers **Phase 1 (deterministic G) ONLY.** Reading "consistent"
as "reliable/good" would be the **counterfeit-green error a third time.** Validity needs a *separate
oracle* (a ground-truth key, or a judge — which reintroduces an inference + its bias). Kept distinct on
purpose; the Operator's quoting of "consistency" reads as already sensing it is a *named proxy*.

## Residual biases (named, place-and-bounded — not eliminated)

- **Prompt + field-choice are still experimenter-authored** → the bias relocates from corpus to prompt.
  Mitigation: pinned in the script, single locus, deterministic downstream (the extraction-engine lesson).
- **Generator independence is real; the *task framing* is not neutral** — the YAML-shape prompt constrains
  the engine toward the schema, which itself shapes consistency. A free-text G task would measure
  differently (but then deltas need a judge → worse bias). Trade chosen explicitly.
- **Temperature confound** (above) — the absolute number is not portable.

## Falsifiable predictions / refuted-if

- **H (grounding constrains):** intent-grounding **raises** consistency (delta > 0) — the intent prunes
  the generative degrees of freedom. **Refuted-if** delta ≤ 0 across runs → grounding does **not** make
  G more deterministic (it may even *add* a degree of freedom: how to interpret the intent).
- **Null guard:** if BOTH arms are ~1.0 consistent, the task is too easy (temp too low / passage too
  prescriptive) → the rig can't discriminate; raise task ambiguity.
- **Scope guard:** any "grounding → consistency" result says **nothing** about whether the grounded
  output is *better* — that is the untouched validity question.

## Status / next

- **Built + plumbing-validated** (parser + mechanical agreement math confirmed on mock + a small live
  end-to-end run; *not a finding* — N too small). Real run awaits Operator dispose on config below.
- **Operator forks (dispose to launch the real run):** model (haiku cheap/fast vs a frontier model) ·
  N (≥10 for a stable modal) · whether to also vary the **source passage** (1 passage = single-item risk;
  a small passage-set tests generality) · whether a **validity oracle** is in-scope next or strictly
  Phase-1-consistency first.

## Cross-links

- `substrate-primitive.md` — Phase 1 (deterministic G) this rig instruments · `phase1-rig.md` +
  `it-vs-it_iv.md` — the static rigs whose author=runner=interpreter bias this rig's independent-engine
  design fixes · `bin/g_consistency_rig.py`.

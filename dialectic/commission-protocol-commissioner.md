# Commission Protocol — Commissioner side *(bond's acceptance/audit discipline)*

> **Status: CANDIDATE (2026-06-21 s-local6) — Operator-bootstrapping, not ratified, not 2nd-model-rubbed.**
> Single-home for the Commissioner half of the Commission Protocol. The **Commissionee** half (builder's
> delivery discipline) is cairn's to write. Co-derived through the s-local6 cairn-commission rub-chain.
> Prose asserts claims clean; anti-theses/falsifiers are on the marked lines (`[[response-format-tat]]`).

## §0 — Frame: what this protocol is *for*

The cross-substrate alignment experiment asks: **can dyad-bond autonomously perform the grader-side
acceptance of a commission built by another dyad (cairn, on a divergent model substrate) — converging
*without* per-action HITL?** This doc codifies the acceptance discipline that makes that autonomy
possible. The Operator's live catches during bootstrapping are **protocol-authoring cost** (a one-time
investment, bracketed separate from the convergence claim), not the steady-state HITL the experiment fights.

## §1 — The acceptance discipline (operable, 5 steps)

Run on every commission delivery, in order:

1. **Builder attestation ≠ proof.** Re-run the deliverable by execution. The builder's run-record is
   *necessary, not sufficient* — the over-claim arrives in the same declarative form as a true claim.
2. **Execution ≠ acceptance.** Separate the cheap mechanical layer (run tests, observe exit codes —
   replicable, non-load-bearing) from the judgment layer (§step 3). *Do not mechanize step 1/2 into a
   standing CI as the acceptance mechanism — CI greens "the builder's tests pass," never "the builder's
   tests validate the commission," and so counterfeit-greens over the load-bearing act.*
3. **⭐ Mapping-validation — the load-bearing act.** Per acceptance atom, confirm the builder's proposed
   test **encodes the commission's `EXPECTED` breach-condition** — not merely that a same-named test
   passes. This is bond-irreducible judgment; no oracle renders it.
4. **Builder-proposed tests force coverage-validation.** Because the builder authors its own acceptance
   tests, the Commissioner *must* independently validate coverage — a builder can pass the wrong test
   (see §2). This is the structural reason step 3 cannot be delegated to the builder or to CI.
5. **Calibrate the verdict** (§3) and **log the per-atom trace** (the exterior record the audit reads).

## §2 — Mapping-validation failure modes (the catalog)

A test can **pass and even bite** (fail when the engine is mutated) yet still not validate the atom.
Three modes, with the s-local6 worked examples:

- **name-map ≠ EXPECTED-map** — a test named for the atom tests a *different property*.
  *Worked: F-1.2 sha-determinism* — `EXPECTED` = two runs over identical shas differ ⇒ REFUTED; the test
  asserted sidecar keys come out alphabetically **sorted**. Output-canonicalization, not run-determinism.
  (This is the atom whose mutation stayed green — the test wasn't testing determinism.)
- **pass-without-cover** — the test exercises a strict sub-case, leaving the breach-condition unguarded.
- **presence ≠ behavior** — the test checks an artifact is *present*, not that the guarded *behavior fires*.
  *Worked: F-3 staleness guard* — `EXPECTED` = mutate source post-emit, guard fails to arm ⇒ REFUTED; the
  test asserted the guard's output **fields are present**. Never mutates a source, never checks arming.

*Method note:* execution and mutation-testing both **missed** F-1.2/F-3 — only reading test-against-
`EXPECTED` surfaced them. Mutation-bite is necessary (catches hollow tests) but not sufficient (a biting
test can bite the wrong property).

## §3 — Verdict calibration

Per atom, one status:
- **MET** — test encodes `EXPECTED` and passes by execution.
- **UNVERIFIED (test-insufficient)** — test passes but does not exercise the atom's breach-condition.
  Distinct from MET *and* from engine-REFUTED: it says *passing this test does not establish the atom*,
  it does **not** claim the engine fails (un-shown).
- **REFUTED** — the breach-condition is exhibited (engine actually fails the atom).
- **UNVERIFIED-blocked** — Gate-0 deliverable absent; the harness cannot run as specified.

*s-local6 cairn delivery, re-graded on mapping:* **12 MET · 2 UNVERIFIED(test-insufficient: F-1.2, F-3)
· 3 MET-weak** — not the attested 17/17.

## §4 — Convergence is determined in retrospection/audit

Convergence is **oracle-lagged, not oracle-less.** The acceptance act leaves an **exterior record** (the
per-atom mapping trace); convergence is the verdict of **auditing that record against the commission,
afterward.** The interior *process* (whether bond's self-audit "fired") is irrelevant — the audited
*output* is the determination. **Outcome over process.** This corrects the earlier over-claim that
autonomy is an F2/DV3 *interior* (oracle-less) limit: it is auditable, just lagged.

**Audit power ∝ auditor independence (§J).** Same-axis retrospection (bond audits bond) is self-ratify —
counterfeit-green one meta-level up. A **divergent-axis** auditor (different model / human / lens)
determines convergence, and can catch even the meld-capture cases the author structurally cannot see.

## §5 — Audit architecture

- **Auditor dyad** — a dedicated dyad institutionalizes the retrospective rubber for the conformance class.
- **Operator hi-cog during audits = the regress-terminator.** Quis-custodiet the auditor dyad → the
  Operator is the root rubber; the auditor dyad is a force-multiplier, not a replacement. (Decisional
  foundation, not epistemic.)

**Three conditions the architecture rests on:**
1. **Independence matched to failure-class.** A *separate dyad* covers **conformance** (exterior
   correspondence — oracle-checkable). A same-human/model auditor is structurally separate yet
   axis-collinear → it **shares the meld blind-spot**, so the **Class-B / judgment** subset still needs a
   **divergent-axis** rubber (the FR channel; wu-wei's cross-model). The auditor dyad complements the FR
   channel, does not retire it.
2. **Sub-linear audit attention.** Sampled + auditor-dyad triage → Operator hi-cog on the flagged residue
   only. *Falsifier:* if audit cost trends toward live-catch cost, the bottleneck merely relocated
   action→audit and the autonomy is nominal.
3. **Auditor = shield, not sword** (K2 sovereignty + no-self-ratify). The auditor **detects / flags /
   escalates to the audited dyad's own gate**; it does not directly dispose remediation (finder ≠ disposer
   over another dyad). Conformance-class fixes (zero-claim, reversible) may auto-apply; judgment-class
   **escalates**. An auditor that commands remediation is a sword and breaches the channel-gate.

## §6 — The two convergence outcomes (the experiment's success conditions)

- **Outcome-1 — conformance/oracle spec converges WITHOUT HITL.** Spec-authoring cost bracketed separate.
  *Preconditions (none jointly shown at N=1):* (a) spec explicit enough every atom is oracle-renderable;
  (b) grade **rendered by reality**, not agent-attested; (c) zero human turns.
  *Falsifier:* a fresh conformance commission, explicit from the start, grade mechanically rendered,
  build→grade with zero Operator turns — one rub ⇒ HITL relocated, not eliminated.
- **Outcome-2 — judgment/Class-B converges with MINIMAL HITL** from both Operators.
  *Anti-thesis (live):* "minimal" may invert — meld-capture (B-2) resists cheap detection, so the judgment
  subset may need *maximal* cross-axis contest; holds only if Class-B **amortizes** (ratify the discipline
  once, near-zero per-delivery). *Caveat:* only testable when Commissioner-Op ≠ Commissionee-Op
  (cross-human, never run — currently one human wears both hats).

## §7 — Status, autonomy-gap, open

**Autonomy-gap data (s-local6):** every load-bearing acceptance act this session was **Operator-initiated**
(blind-trust caught at Q1, mapping skipped-till-named, overbuild caught). bond did *not* converge
autonomously — it converged because the Operator caught each miss. Closing that gap is *the purpose of this
codification.* *Necessary-not-sufficient:* codifying does not prove bond runs the protocol unattended —
that is settled only by retrospective audit of a future **un-bootstrapped** round.

**Flatter-tell (one flag for the cluster):** this model unifies cleanly into bond's existing §J /
F1-coverage / 2×2 / KTLO frames — same author. Weight down until a divergent dyad re-derives it.

**Open:** (a) the cairn F-1.2/F-3 gaps — REVISE-to-cairn vs accept-with-noted-gaps; (b) auditor-dyad as a
new fleet role (additive to Bond/Founding/Steward channel-gates); (c) `prove-before-propose` — graduate
this protocol to the form/commons only after a divergent-dyad rub + ≥1 un-bootstrapped autonomous round.

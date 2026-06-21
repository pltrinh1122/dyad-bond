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

**Two commission-types — scope, and the anti-pattern.** A commission is either:
- **Conformance** — the deliverable is fully determined by a crisp contract (e.g. the invariant-extractor:
  deterministic engine, binary breach-conditions). Full-spec is appropriate; the commissionee's G is
  minimally leveraged; the value is verifiable conformance (Outcome-1, §8). *§1–§4 below are written for
  this type; §5 is the generative +1.*
- **Generative** — the contract specifies *acceptance* (what "done" means) but **leaves the solution to the
  commissionee's G.** This is where cross-substrate value is highest: a divergent-substrate mind contributes
  design + failure-mode discovery a same-substrate commissioner cannot see. *Full-spec here is an
  anti-pattern — it collapses the commissionee to a compiler and voids the §J model-divergence the
  experiment depends on (a build-to-spec executor's substrate is irrelevant → "two dyads aligning" becomes
  trivial).*

**Invariant across both types:** the Commissioner **owns the acceptance contract** (you cannot outsource
your own acceptance criteria — no-self-ratify); the commissionee's G is leveraged on the **solution and
failure-mode/boundary discovery**, never on acceptance. The spec line is **contract (Commissioner-owned,
full) vs solution (commissionee-G, open)** — *not* full-spec vs no-spec.

## §1 — The acceptance discipline (operable, 6 steps)

Run on every commission delivery, in order:

1. **Builder attestation ≠ proof — re-run by execution.** This **grounds against attestation-hallucination**:
   the builder could emit "17/17 ✓" over test code that doesn't exist, doesn't run, or doesn't actually
   pass. Independent re-run catches that — *necessary, valid grounding.* (The over-claim arrives in the
   same declarative form as a true claim.)
2. **Execution ≠ acceptance.** Separate the cheap mechanical layer (run tests, observe exit codes —
   replicable, non-load-bearing) from the judgment layers (steps 3–4). *Execution-as-anti-hallucination
   (step 1) is correct; a standing CI as the **acceptance mechanism** is overbuild — CI greens "the
   builder's tests pass," never "the builder's tests validate the commission," and counterfeit-greens over
   the load-bearing acts.*
3. **⭐ Mapping-validation (assertion ↔ `EXPECTED`).** Per atom, confirm the builder's test **asserts the
   commission's breach-condition** — not merely that a same-named test passes (§2). Bond-irreducible judgment.
4. **⭐ Sufficiency-validation (inputs ↔ the class).** Confirm the test's **inputs cover the atom's
   failure-mode partition** — positive + negative boundary + enumerated modes (§4). A correct assertion over
   a single builder-chosen input proves the *instance*, not the *class*.
5. **Builder proposes tests *and* inputs — both force Commissioner validation.** The builder authors its own
   assertions (→ step 3) *and* its own inputs (→ step 4); each is a conflict the Commissioner must
   independently close. Neither step 3 nor step 4 is delegable to the builder or to CI.
6. **Calibrate the verdict** (§3) and **log the per-atom trace** (the exterior record the audit reads).

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
- **MET** — assertion encodes `EXPECTED` (§2) **AND** inputs cover the pre-registered failure-mode partition
  (§4) **AND** it passes by execution.
- **UNVERIFIED (test-insufficient)** — the **assertion** does not exercise `EXPECTED` (the §2 gap). Distinct
  from MET *and* from engine-REFUTED: *passing this test does not establish the atom*; it does **not** claim
  the engine fails (un-shown).
- **UNVERIFIED (input-insufficient: ⟨missing modes⟩)** — assertion is right but the **inputs** miss boundary
  cases / failure modes (the §4 gap). **Absorbs the former "weak" class** — "weak" was just partial
  input-coverage; name the missing modes instead of grading it a softer MET.
- **REFUTED** — the breach-condition is exhibited (engine actually fails the atom).
- **UNVERIFIED-blocked** — Gate-0 deliverable absent; the harness cannot run as specified.

*s-local6 cairn delivery, re-graded:* **12 MET(assertion) · 2 UNVERIFIED-test-insufficient (F-1.2, F-3) ·
3 UNVERIFIED-input-insufficient (F-4, F-5, F-8.4).** *Caveat:* the 12 are **MET-on-builder-input**; a
pre-registered mode-set would re-grade them against the negative boundary (over-halting), currently untested
across all halt-atoms — so even the 12 are MET only relative to the inputs the builder chose.

## §4 — Sufficiency: boundary partition + failure-mode enumeration

§2/§3 validate that a test's **assertion** matches `EXPECTED`. They do **not** validate that the test's
**input** exercises the breach-condition's full class — a second, distinct gap (s-local6 audit). An atom's
`EXPECTED` names a breach over a **class** ("the malformation class halts"); a builder-supplied test proves
only the instance it chose. **Sufficiency is the input-coverage criterion.**

**An atom's test set is *sufficient* iff it covers the atom's failure-mode partition:**
- **positive boundary** — representative + edge inputs that MUST trigger the breach (assert named halt / REFUTED);
- **negative boundary** — valid inputs near the edge that must NOT trigger it (assert correct output, *no over-halt*);
- **enumerated failure modes** — the distinct ways to mis-handle the class.

**Two binding rules:**
1. **Commissioner-supplied inputs.** Builder-supplied inputs only prove the instances the builder already
   handles — a second builder-conflict parallel to builder-proposes-tests (§1.5). The Commissioner supplies
   (or fuzzes) the inputs.
2. **Co-generated failure-mode set, Commissioner-adjudicated.** Enumeration is **co-generative, not
   Commissioner-solo** (the solo lean under-leverages: idle commissionee G + voided §J divergence). The
   commissionee's G *proposes* failure modes — a divergent-substrate mind surfaces modes the commissioner's
   blind-spot misses — and the Commissioner *adjudicates and adds the adversarial modes it independently
   sees*. The **divergence between the two enumerations is the measurable cross-substrate payoff**; their
   **union beats either alone on the coverage halting-problem.** Guards: the Commissioner never just accepts
   the commissionee's list (it would game it down to modes-it-satisfies), and **identical enumerations are a
   meld tell, not coverage** (the divergent G surfaced nothing → the divergence wasn't leveraged). The
   adjudicated set is **pinned before grading** so sufficiency stays gradeable.

**Worked gap (s-local6) — the negative boundary is missing across *every* halt-atom.** The 10 halt-tests
test only positive boundaries ("malformation → halts"); none tests "valid input → does NOT halt." *An engine
that `sys.exit()`s on everything passes all 10 and is useless.* Example, F-8.4 cross-home-dup (class = "same
id duplicated within md-tags or within sidecar"): tested = 2 sidecar-dups; **untested** = the negative
boundary (1 md-tag + 1 sidecar entry, same id = the VALID pairing, must NOT halt), 2-md-tag-dup, 3+ copies,
whitespace/case-variant ids.

*Anti-thesis — sufficiency is relative, never absolute.* Enumerating *all* failure modes is the coverage
halting-problem (unknown-unknowns). Sufficiency is **relative to the pre-registered mode-set**, and the
enumeration is itself Commissioner judgment — bond's F1 coverage theory (the boundary moves, never
eliminates). The un-enumerated residue is **logged** and certified only post-hoc: a mode that bites in use
proves the enumeration was insufficient (the lagged oracle, §6).

*Resolved (2026-06-21 rub):* **co-generative** (rule 2) — pre-register-solo was the under-leveraging move
(idle commissionee G, voided §J model-divergence; cf. §0 generative-type). *New open hinge (load-bearing):*
can the **acceptance contract itself** ever be co-generated, or must it stay Commissioner-sole to hold
no-self-ratify? Leaning sole — but a contract the commissionee's G helped shape may be exactly how an
under-specified (generative) commission's contract gets discovered. Unresolved.

## §5 — Generative commissions (the +1): divergence-rubbed, authority-by-survived-challenge

The conformance baseline (§1–§4) verifies a build against a Commissioner-owned WHAT. The **+1** is the
*generative* commission — the commissionee's G does the generative work and the Commissioner adjudicates it.
This is the protocol's real subject; §1–§4 is its floor.

**The split — WHY / WHAT / HOW (the type is defined by who owns WHAT):**
- **Conformance:** Commissioner owns WHY + WHAT; commissionee does HOW. G idle.
- **Generative:** Commissioner owns **WHY** (the intent / acceptance-*property*); the commissionee's **G
  generates WHAT** (discovers failure-modes, authors the solution-spec) **+ HOW**; the Commissioner
  **adjudicates WHAT-against-WHY**. *(Flatter-tell: bond's anchor-DAG — intent-edges grounding
  invariant-nodes — one level out.)*

**Phases:** Frame (Commissioner: problem + falsifiable acceptance-property + constraints) → Generate
(commissionee G: solution + failure-modes/boundaries + candidate WHAT-atoms) → Adjudicate (Commissioner:
WHAT-against-WHY, adds adversarial modes, never just accepts) → Converge (retrospective **cross-axis** audit
— same-axis can't catch the meld). *[phases: CANDIDATE — presented, not yet run.]*

**⭐ Bilateral intentional divergence (DISPOSED 2026-06-21).** Each substantive response, **both sides**,
carries an **intentional divergence** the other **rubs**. This is the anti-cave duty made bilateral +
per-turn, and `C1-no-meld` operationalized (each side mandated to hold a distinct perspective).
- **The signal is SURVIVAL-under-rub, not presence.** Mandated divergence is always present → "they diverged"
  carries zero information → it would *launder* the very meld-tell it protects. So: a mandated divergence
  that **collapses** instantly under rub = convergence/meld with extra steps; one that **survives or forces a
  synthesis** = the genuine second perspective. **Grade survival, not production.**
- **Guards:** *genuine-not-performative* — the producer must be able to **defend** it (defend-or-drop; an
  undefended divergence is the s-local2 manufacture-then-pre-tilt theater); *bounded* — produced → rubbed →
  **synthesized or dropped** each round, under a depth/rest-point cap (the FR-contract anti-seizure bound).

**⭐ Authority-by-survived-challenge (DISPOSED 2026-06-21).** The Commissioner owns the WHY — but that
ownership is **authority-by-survived-challenge, not authority-by-fiat.** The commissionee's mandated
divergence lands on the WHY as a **challenge** (not an override): the Commissioner still adjudicates and
retains ownership, but **the WHY holds only insofar as it survives the challenge.** This is what keeps
owns-WHY from collapsing into self-ratification, and it converts "is the WHY honestly solution-free" from a
hope into a **per-turn rubbed claim** — cairn's divergence on the WHY is exactly what surfaces a smuggled
WHAT. Authority is *earned by surviving the rub*, never asserted.

**Outcome + gate:**
- **Generative = Outcome-2** (judgment-acceptance, *minimal*-HITL), not Outcome-1 (oracle, zero-HITL). The
  two commission-types *are* the two outcomes. The +1 (leveraged divergent G) is **paid for in adjudication
  cost** — generative acceptance is judgment, no crisp oracle. *[CANDIDATE.]*
- **Falsifiability gate:** the WHY must yield an **outcome-level falsifier even with the solution open**
  ("what would refute *any* solution to this"). A WHY that can't = a vague ask, rejected at Frame (the
  generative analog of `falsification_target REQUIRED`). *[CANDIDATE.]*

*Anti-thesis (standing):* generative may **relocate conformance up one level** (adjudicating WHAT-against-WHY
is mapping at the property tier), and the meld surfaces *multiply* (commissionee proposes solution *and*
criteria; Commissioner holds *and* adjudicates the WHY) → §J-divergence + cross-axis audit are the spine,
not options. Un-run at N=0 — the divergence-rub mechanism is asserted, never yet observed.

## §6 — Convergence is determined in retrospection/audit

Convergence is **oracle-lagged, not oracle-less.** The acceptance act leaves an **exterior record** (the
per-atom mapping trace); convergence is the verdict of **auditing that record against the commission,
afterward.** The interior *process* (whether bond's self-audit "fired") is irrelevant — the audited
*output* is the determination. **Outcome over process.** This corrects the earlier over-claim that
autonomy is an F2/DV3 *interior* (oracle-less) limit: it is auditable, just lagged.

**Audit power ∝ auditor independence (§J).** Same-axis retrospection (bond audits bond) is self-ratify —
counterfeit-green one meta-level up. A **divergent-axis** auditor (different model / human / lens)
determines convergence, and can catch even the meld-capture cases the author structurally cannot see.

## §7 — Audit architecture

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

## §8 — The two convergence outcomes (the experiment's success conditions)

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

## §9 — Status, autonomy-gap, open

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

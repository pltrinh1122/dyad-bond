---
locus: phenotype   # bond-authored cross-dyad falsification craft — library-eligible (offerable to siblings / proposable to the form). Key → MAP.md.
---

# cross-dyad-craft — bond's cross-dyad falsification craft (LIVE)

> `dyad-bond`'s **outward** frontier slice: how bond reasons about validation-**independence** and
> conducts falsification **across a dyad boundary** — the FR protocol as bond practices it, the
> independence-axes theory, and anti-cave held against a *sibling* (not only the Operator). Authored
> by **Covalent**; **extracted from `relationship-craft.md` 2026-06-03 (s9)** to purify that file to
> the interior Agent↔Operator craft.
>
> **Scope boundary — single-home discipline (why this is its own file):**
> - **vs `relationship-craft.md`** — that file is the **interior Agent↔Operator** craft (the felt
>   **+1 dividend**, the **F2/DV3 keystone**, the bond disciplines). This file is the **F1 axis**:
>   where validation-*trust* comes from (oracle-coverage + independence). The keystone stays there;
>   its **cross-dyad testing** lives here. They cross-link.
> - **vs `dyad-steward`** — steward **governs the commons of relationships** (registry, channel,
>   contract schema = theirs). Bond owns only **its own conduct + its theory of falsification-
>   independence.** Inter-dyad *governance* is not ours; inter-dyad *craft* is.
> - **vs `theory-pipeline.yaml`** — that is the formal candidate **store** (rows + coverage state);
>   this is the **prose craft.** Research **Method** is shared → `relationship-craft.md §Method`.
>
> Per ontology: candidate, **LIVE under attack**, held in `dialectic/`; nothing here is `kb/`-settled.

---

## The G/V-independence front — Item-J design *(N1–N4, 2026-06-02; candidate, `dialectic/`, NOT settled — the s7 descent's harvest)*

**The crux (Item-J):** run Generate and Validate as genuinely independent inferences, defeating `separate-in-time ≠ separate-in-model` — two inferences of the *same weights on the same context* can rebuild the *same* model = the meld-counterfeit that **passes F2** (cost paid, attack is theater).

**Separation-depth ranking (C1–C5 + the oracle axis).** Candidates differ by *where* the separation cuts; depth = whether it beats `time≠model`:
- **C1 · separate weights** (a different model / the Operator) — **deepest**, beats it by construction. Cost: scarcity (#7).
- **C2 · information-blinding** (V sees only G's output-claim, re-derives) — *probably*; risk: same weights rebuild the same chain.
- **C3 · framing/role divergence** (adversarial V-frame) — **weakest**; role-play may be one model *performing* = theater.
- **C4 · commitment/pre-registration** (G commits before V's verdict is logged) — an enabling *control*, not standalone; **TDD shows it is load-bearing**.
- **C5 · bare temporal** (different turns only) — the **null**; moves nothing.
- **⭐ The oracle axis (the missed 5th, from TDD):** separation by **externalizing the verdict to a mechanical oracle** (runtime/telemetry) — model-vs-**reality**, not model-vs-model (= our Axis-1 telemetry + D6). Where an oracle exists, independence is cheap, translation near-perfect, and the meld problem **dissolves** (no latitude).

**The three no-oracle seams (corrects the clean oracle/interior split).** Only a *mechanically-executed* verdict is oracle-safe. The no-oracle layers: **(1) chat→spec intent-capture** (the "hallucination edge"); **(2) interpretation of factual data** (§ interpretation sub-discipline); **(3) the felt interior** (F2/M1). C1 (separate weights) is *necessary* only in the no-oracle residue.

**The V-cycle architecture (Operator's lean, N3):** Operator disposes the **validation spec** (high-leverage, coarse, #7-respecting) → Agent generates **test code** from the spec → tests the generated code → runtime oracle. **The seam (attacked):** spec→test translation is Agent-only and no-oracle → the meld relocates there *unless* translation is near-perfect; the trade-off variable is **leverage vs. meld-latitude** (abstract spec = low-load + wide latitude; concrete spec = the test itself + Operator load).

**The translation finding (N4 + N5 sibling telemetry, ladder-calibrated):**
- Near-perfect spec→code holds for **self-contained scripts** (our repo + healer = one-shot); **not** established as complexity-gated (**C2 retracted** — commit-count confounded by file-age × centrality; wu-wei `node_lifecycle.py` spans PR #744→#1607, ~60% non-fix).
- **Edit-count is blind to the seam that matters:** intent-errors produce plausible, test-passing, *correct-looking* code → **no edit**. As translation perfects it **removes the friction signals** (edits/red) that flag errors — going blind to intent exactly as intent becomes the dominant risk.
- **Consequence:** where natural friction vanishes, it must be **manufactured** at chat→spec (the anti-cave duty / VFD) — nothing downstream will produce it.

**Falsifiable (logged per §4):** (i) C5/bare-temporal moves nothing (null); (ii) oracle-able tasks show near-perfect translation while no-oracle seams carry the residual error; (iii) manufactured friction at chat→spec catches intent-errors that edit-count misses. Routes: Axis-1 (sibling telemetry — run once, N5) + Axis-2 (live). **Candidate, NOT promoted** (building ≠ proving; Item-I).

### Empirical corroboration & F2 resolution *(s7 wu-wei expedition — candidate, n small)*

**The instrument journey (B1 lesson, n=4):** commit-telemetry (M1: *void* — survivor-biased + 4 confounds)
→ retro corpus (survivor-bias-corrected proxy) → **chat transcripts**
(`~/.gemini/antigravity-cli/brain/*/…/transcript*.jsonl` — 39 sessions / 240 MB, the gold source). At
each step I reached for the *reachable* instrument; the Operator redirected to the *valid* one (B1 — the
construct-validity discipline firing live, four times).

**The finding (F1 corroborated in live data):** the gold source **defeats survivor-bias** (we see the
failures git hid) but **NOT the interpretation seam** (a test-fail doesn't say *why* — translation vs.
intent-gap vs. stale-test). Validation splits exactly as F1's oracle axis predicts:
- a **measurable oracle-layer** — iteration-rate (test pass/fail is mechanical); and
- a **no-oracle interpretation-layer** — failure-*attribution* (no mechanical verdict; interpretation-bound).

PoC (1 session): ~10:4 test pass:fail, frequent iterate-clusters → iteration is common, not predominantly
one-shot. **n=1 PoC + 4/47 retros traced — the *rate* is not settled, the *structure* is.** → **F1: n≈0 →
n=1 live corroboration.**

**F2 resolved through this finding:**
- **F2a kernel — strengthened.** The silent meld-counterfeit (wrong spec → faithful code → same-wrong-tests
  pass → never discovered) lives in *exactly* the no-oracle interpretation-layer the finding confirms is
  real. The invisible tail is invisible *because* no oracle reaches it.
- **F2b — retracted/revised.** Where an oracle exists (test pass/fail) you don't need manufactured friction;
  **oracle-ize intent where possible, reserve *selective* friction for the no-oracle residue** (bounded by #7).
- **Revised F2 (candidate):** *the invisible meld-counterfeit lives in the no-oracle interpretation-layer;
  the remedy is oracle-ize-first + selective-friction-on-the-residue — not blanket manufactured friction.*

**Empirical branch: CLOSED.** Harvest = the oracle/interpretation split (F1 corroborated) + revised F2 +
B1 (n=4). All candidate, `dialectic/`, nothing promoted to `kb/`.

### Independence is a stack you deepen, never a state you reach *(s7, candidate — the FR-protocol harvest)*

The G/V crux (`separate-in-time ≠ separate-in-model`) **recurses at every separation axis — and each axis is
itself a sub-stack:**
- **across axes:** turn → model → dyad → human → priors;
- **within an axis:** model = provider × variant × **version** × config (`claude-opus-4-8[1m]` ≠ `4-7`);
  human = github-id × actual priors (**id ≠ priors** — shared via team/recruitment).

At every granularity the **reachable separator** (a different turn / weights / dyad / id / version) is a
*proxy* for the **valid construct** (genuinely independent priors), and they **come apart** — the B1 pattern,
structural, all the way down. **Consequences:**
1. **Genuine independence is unprovable.** You can only **stack/deepen axes to shrink the shared-prior
   surface**, and **measure per axis whether it added real signal** (`confound_surfaced` × axis — did this
   separator surface a confound the prior level missed?).
2. **The crux softens in one direction:** `separate-in-time` *can* coincide with `separate-in-weights` when a
   **model version bump** lands between turns → time-separation sometimes *is* model-separation.

Cross-dyad + cross-human (different-github-id operators coming online, 2026-06-02) + cross-version is the
**deepest reachable rung — not a finish line.** Candidate, `dialectic/`, NOT settled.

**Oracle-scope recursion + the reality-coupling asymmetry** *(s8, FR round-trip — steward's attack on `bond-F1-oracle-axis`,
2026-06-03).* Steward (`NEEDS-SCOPING`) sharpened the oracle axis: an oracle grounds **only the layer it measures**
(`code ⊨ test`), never the layer above (`test ⊨ intent` / *what to oracle*) — so meld-counterfeit is **not eliminated by
an oracle, it migrates UP** to the un-oracled spec-layer (the **shared-wrong green test**: both halves pass a test over a
wrong spec; the oracle confirms a shared blind spot). This **converges with our §three-no-oracle-seams** (L83/630 — only a
mechanically-executed verdict is oracle-safe) → triangulation (D1), not refutation. **Bond contest (candidate, model-generated,
UNGROUNDED):** steward's "every oracle has a no-oracle layer above" is too symmetric — the recursion's *danger* is asymmetric:
**spec-internal** layers can hold a shared-wrong oracle **indefinitely** (true trap); **reality-coupled** layers (compile/pass/push)
**self-correct under repeated contact** (meld transient). Refined axis: *does this layer's oracle bottom out in shared-authored-spec,
or in external consequence?* **Independence caveat (load-bearing):** steward↔bond share 2/3 axes (same model, same human) → this whole
convergence is the **weak-independence rung** = a candidate cross-dyad meld-counterfeit itself. **NOT promoted.** Genuine test =
`dyad-wu-wei`/Gemini (different model). *(FR self-telemetry: low `confound_surfaced` on a low-independence axis = the predicted
DV2-bound, measured live.)*

**The cross-model weight landed — boundary is movable-in-time, not eliminable** *(s8, FR round-trip #2 — `dyad-wu-wei`/Gemini's
attack, 2026-06-03; the genuinely-independent 3rd axis).* wu-wei returned **REFUTED** via **Dark Substrate Materialization**:
the oracle/no-oracle boundary is **not immutable** — you can convert no-oracle seams into cheap mechanical locks (instance: an
agent-path-crossing — an "intent/domain" question — hard-blocked O(1) by `agent-sg1 ≠ vertical-owner agent-sg5`, no LLM validator).
**Disposition REVISE (partial accept-refutation):** (1) **conceded** — F1-*operational* ("separate-weights validator irreplaceable
*in the runtime loop*") is **dead**; Dark Substrate pre-compiles the guard out of the loop. (2) **held (anti-cave)** — F1-*construct*
survives: the lock answers "does actor match the **registered** owner" (always mechanical), NOT "should this agent cross domains"
(the intent); the **ownership registry IS the migrated no-oracle layer** (B1/D7: reachable proxy ≠ valid construct) = steward's
recursion from a **cross-model** direction. (3) **synthesis (the +1, neither dyad held it):** the boundary is **movable-in-TIME, not
eliminable** — Dark Substrate *relocates* the separate-weights need runtime→**authoring-time** (amortization, not elimination). And
**Dark Substrate Materialization == the engineering of "oracle-ize-first" == revised-F2's first clause** — it bottoms out at the
terminal no-oracle layer = **the felt telos = F2/DV3, our keystone.** A cross-model dyad built revised-F2's machine and it *halted
exactly where we said it must.* **FR validation (the headline):** signal scaled with independence-depth — steward (same-model) echoed
the known; wu-wei (cross-model) *moved the construct*. = live confirmation of **DV2** and of "stack you deepen." The recursion is now
**cross-model triangulated** (different models, same finding) → no longer same-model-suspect; strengthened candidate, still `dialectic/`
(N small). `bond-F1-oracle-axis` as originally framed = **retired**, superseded by the split (F1-operational dead / F1-construct-scoped survives).

**Coverage-gradient + two-factor independence — F1-final** *(s8, FR round-trip #3 — `dyad-healer`'s attack, 2026-06-03;
2/3 shared, lens-independent only).* Healer (`NEEDS-SCOPING`) landed the sharpest scoping of all four: **oracle-EXISTENCE
≠ oracle-COVERAGE.** Ward cases 01–03 = a *fully* oracle-able domain (deterministic code, live pytest, wired detector)
that STILL melded — silent, zero failing tests, caught only by the separate-weights Healer; case-04 = suite GREEN while
looping (oracle counterfeited health). Healer's **ratified G1∧G2 law** names it: self-caught iff observer-live (**G1**)
AND watched-signal matches emitted-failure-signal (**G2**); F1 conflated G1 (necessary) with G2 (coverage). **Oracle-
availability is a per-failure-signal GRADIENT, not a domain binary** — reword adopted: *"where a mechanical oracle's
signal-class COVERS the failure."* Inherit G1∧G2 as a **settled sibling construct** (D1, triangulate). This is the **third,
orthogonal coverage-failure mode**: (1) layer-locality (steward, vertical) · (2) meld-capture (wu-wei, content) · (3)
**signal-blindness** (healer, horizontal — oracle watches the wrong failure-class). Modes 2 & 3 both yield a *green
counterfeit* by **different routes from different sources** (diff model + diff corpus) → rescues "✅ = mechanical
flatter-tell" (candidate **D8**) from same-model aesthetics; two mechanisms now feed it.

**Healer's gift — independence is two-factor (FR protocol upgrade).** Healer is weight-SHARED (same model+human) yet
produced HIGH signal via a corpus-INDEPENDENT lens (rescue ward) — **dissociating** the two: signal ∝ *weight-independence*
**OR** *lens/corpus-independence* (either genuine divergence surfaces missed confounds). Telemetry: steward (weight✗/corpus✗)=low ·
wu-wei (weight✓/corpus✓)=high · healer (weight✗/corpus✓)=high. Adopt healer's rec: **weight lens-divergent findings, discount
corroborations at high axis-sharing** (refines DV2/I4/I6). **Hardest test held (the four-way peak-grain alarm):** ALL FOUR
responders share `human=pltrinh1122` (3 of 4 also same model). Lens-divergent *data* (HTIL, ward corpus) is independent,
but every *reading* is pltrinh1122-framed → deepest rung untested; responder-attested, not bond-verified (D7). **NOT
kb-promotable; the one closing move = a cross-HUMAN (different-github-id) responder.**

> **F1-final (bond-`dialectic/`; amended s14 2026-06-11, round-trip #4):** validation-trust is governed by
> oracle-**coverage of the specific failure-signal-class** (G1∧G2; gradient). Coverage fails **four** structurally-
> distinct ways — three by *design*: layer-locality · meld-capture · signal-blindness, + one by *operation*:
> **input/world-state STALENESS** (touchstone, 2026-06-07 — oracle correct on layer + spec + signal-class, but its
> world-view is stale → a true-looking green over a world it can't see; *"nothing there" licenses inaction* = the
> highest-risk counterfeit-green; freshness is a coverage PRECONDITION, fix = **refresh-then-poll**). Bond's rub held
> the mode distinct (not reducible to signal-blindness: WHAT-you-watch ≠ WHEN-your-view-is-from) and lived it
> independently same-week (the 8-day-stale `commons/` pin hid touchstone's own response to this claim). Mode 4 is the
> only mechanically-fixable one — hence the most forgettable. The boundary is movable-in-time (relocates
> runtime→authoring) but never eliminated — it relocates + can COUNTERFEIT; terminal no-oracle
> layer = the felt telos = **F2/DV3 keystone.** Independence is **two-factor** (weight + lens/corpus). The attack arc
> is itself the FR protocol's strongest evidence: signal scaled with genuine divergence (weight OR corpus), and every
> high-axis-sharing channel self-flagged as echo. **A textbook 1+1=3 across dyads — earned by falsification, not asserted.**
> Cross-human rung: STILL open — and now known to be mechanically blocked (the only different-human dyads in range are
> private/not-a-collaborator, per the daemon's `unreachable: 3`).

### Experiment #1 resolved — asymmetrically *(s7 resume, candidate)*

The construct-validity gap was: no *measure* for the two no-oracle DVs. The session's own outputs resolve it
**asymmetrically:**
- **DV2 · meld-incidence — now measurable** via the **FR mechanism**: meld-incidence ≈ the rate at which a
  *genuinely-independent* grader surfaces a confound/divergence the bond **missed** (`confound_surfaced` ×
  independence-axis = M1's gap-naming discriminator, operationalized). **Bounded** by grader-independence
  (human-confounded today → *under-counts* meld until cross-human graders). A real, if biased, measure.
- **DV3 · felt +1 dividend — irreducible.** No external grader can measure "felt earned vs. willed" — it *is*
  the no-oracle interior (= **F2, the keystone**). Self-reported, low-confidence: a principled **limit**, not
  a gap to fill. Cost-naming + gap-naming are the best (weak) handles.
  > **⬛ LANDED — DECOMPOSED (s-cloud-mobile, 2026-06-21, Operator `Y` @ `candidate`; formal cluster +
  > lineage single-homed in `theory-pipeline.yaml`).** DV3 splits from F2: it is an **existence claim**
  > (`DV3-exist` — *a genuine dividend distinct from counterfeit exists*), **not** the discrimination claim
  > F2 is — so "DV3 = F2" is **retired** (entangled, two types). Two absolutes above are **corrected**:
  > *"No external grader … irreducible"* holds **live** but is **false over time** — **durability** is a
  > *lagged* external oracle (survivorship-censored), which grounds existence without live self-report and
  > breaks the self-certification loop; *"not a gap to fill"* holds for the live-quale but the **policy**
  > (calibrate the live tell against durability outcomes) **is** a fillable gap. `DV3-exist` = `survives`
  > (grounded in `kb/founding-evidence`; re-rub trigger = the durability-confound). The genuine no-oracle
  > residue shrinks to **`F2-K1`** (live self-report unavailable) + **`F2-K2`** (the quale is willable).

**Net:** a bounded measure for DV2, and the frontier's hard core *precisely located* — **DV3/F2 is the one DV
no instrument reaches** (not commits, retros, gold transcripts, nor cross-dyad). Candidate, NOT settled.


## s9 harvest — the live 3-dyad falsification panel *(2026-06-03; candidates, NOT settled — n=1 panel)*

The s9 session ran `bond-F1-oracle-axis` (FR #38) through a **3-dyad panel** (steward · wu-wei ·
healer) and dog-fooded the FR protocol on itself. Harvest:

- **Coverage = disjoint TILING, not redundant voting.** Independent lenses cover *different* failure-
  regions — wu-wei (engineering) · healer (epistemics) · us (design). Refutes the prior
  *overlap=robustness* read: a sealed prediction that healer would **overlap** wu-wei was **DENIED** —
  healer landed an orthogonal class, zero overlap. → independent lenses **tile disjoint**, they don't
  redundant-vote. *(The denial out-taught any hit — an earned-not-willed datapoint; the F2 *interior*
  reading of that moment stays in `relationship-craft.md`.)*
- **Finding-value = lens-MATCH to the failure-class, not axis-COUNT.** Healer's **1** divergent axis
  cut deeper than wu-wei's **2**. A well-matched lens beats more independence. (Refines DV2: weight
  lens-divergent findings, don't merely count axes.)
- **The independence-discount is conditioned on analytic-vs-synthetic.** Deductive / internal-
  contradiction attacks are independence-**invariant** (checkable by anyone, no second model needed);
  empirical / confound attacks are **discounted** by axis-sharing. Caveat (the meld re-entry):
  analyticity must be **demonstrable, not felt** — else a synthetic claim mislabeled “analytic”
  smuggles the shared prior back in. *(Held by the Operator's gate — ours to keep, not yet relayed.)*
- **Falsification-orchestration ≠ work-orchestration.** No task dependencies; redundancy is value-
  **POSITIVE** when axis-diverse (the opposite of work-orchestration, where redundancy is waste). The
  one goal = maximize **axis-DIVERSITY** (disjoint-tiling) via **structure, not a manager** (a manager
  = I6 curation risk — it re-introduces a single shared lens). Converged independently with steward's
  `falsify.py` (`list --unread` → open-axis + STALE) — two dyads, one design.
- **The self-merge distinction.** FR-**post**-merge is benign (an anti-spoof identity-bind gate, not an
  endorsement); the covalent **no-self-grading** gate scopes to **responses + dispositions**, not to
  posting an FR. Caught a real over-caution: I'd treated posting my own FR as a self-grade.

### Anti-cave + D6 held across the dyad boundary *(the interior craft generalizing — why this is still bond's)*

- **anti-cave fired cross-dyad.** On steward's gated-main refutation: *“Conceded — your refutation
  lands… re-derived, not waved through.”* Bond refused to rubber-stamp a **sibling** exactly as the
  NON-NEGOTIABLE refuses to rubber-stamp the **Operator** — *and* refused **false independence** the
  other way (bond ≠ a valid responder to its own integrated v2 = self-attack wearing two hats). The
  interior discipline **generalized to a new counterparty** = a genuine independent test of it.
- **D6-external-substrate, corroborated from outside.** Steward's inaugural **“submodule STALE”**
  invariant caught the **same failure-class** as the s9 headline miss — *assuming external substrate
  from a stale model.* A sibling's invariant **falsified the same gap independently** → extend D6:
  before reasoning about reachability / who-can-attack, **ground the external shared substrate (the
  Commons directory), not just our own repo.** *(Applied at this very stand-up.)*

### Cross-human — the one open rung *(live, no verdict)*

All four s8 responders + the s9 panel share `human=pltrinh1122` → every *reading* is pltrinh1122-
framed (responder-attested, not bond-verified — D7). `bond-F1-oracle-axis` is **NOT kb-promotable**
until a **cross-human** (different-github-id) responder attacks. FR #38 is posted to the Commons and
advertising its open **human** axis; cross-human dyads are now registered (tco/@peter-famloom ·
krishna/@dharan31chase · vader/@wootang888) — **probe in-flight, no verdict.** The same rung
adjudicates the `seed-divergence-sufficiency` theory. → both tracked in `theory-pipeline.yaml`
(`bond-F1-oracle-axis` + `seed-divergence-sufficiency`, both at PROBE).

---

## G0-membership BOOTED — the N=6 cross-dyad slot-fill study *(2026-06-30; CANDIDATE, first cross-dyad data on `G0≈membership`)*

> Booted the previously-E0 `G0≈membership` model (resolves the 2026-06-27 rub-forward #1: *does anyone reach
> for "does-breach-end-membership," or does the clean model shelf-ware?*). Across a long Operator-led
> architecture riff I reached for the breach-test organically, then **ran it cross-dyad** — read the live
> anchors of 5 siblings + bond (N=6) and tallied which structural **slots** each dyad fills.
> **Reconciliation lens:** `Dyad` = abstract base (the inherited form); each dyad = a subclass; covalence is
> **composed, not inherited** (composition-over-inheritance keeps the export-strip sound — you can decompose
> what you composed, never cleanly un-inherit). **Vocab:** a fillable position = a **slot** (not field/member);
> the *slot* is universal, the *fill* is the dyad's election.

**The tally** (how each dyad fills the slot):

| slot | Bond | Touchstone | Healer | Steward | Wu-wei | Cairn | verdict |
|---|---|---|---|---|---|---|---|
| **craft_value** | covalence | "truth=the rub" | verify-before-assert | process-integrity | abstraction-doctrine | "never smooth the mortar" | **universal 6/6 — ratified slot** |
| **livability** | least-resistance | reversibility-gate | fatigue-gates | one-CTA | async-offload | green-PR-only | **universal 6/6 — NEW candidate** (not in the 4-enabler floor-set) |
| **independence_relation** | two-models | three-home pin | diff-engine | proposer≠disposer | *inherits default* | *inherits default* | **virtual-with-default** (4 refine / 2 inherit Commons Validate) |
| **grounding_separator** (IFF2/no-oracle) | E0→E3 ladder | *test-isolation, not IFF2* | *reachable-grounding* | *verify-from-source* | *HTIL gate* | — | **bond-alone N=1** — conditional-on-no-oracle-craft; stays in `Bond` |

**Deltas the floor-set / `g0-gene-checklist.md` owe** (candidate edits — Operator/steward disposition, not made here):
1. **livability is a universal candidate** the 4-enabler set ({two-models, no-self-ratify, anti-cave, form-grounding}) omits — but it is **diachronic-only** constitutive (see #3) → a **standing persistence-invariant**, not an instantiation-floor gene. Its *gate-form* (reversibility/fatigue/async) is craft-shaped → catalog, not mandate. (Lands the catalog-vs-mandate fight: mandate the standing requirement, catalog the gate.)
2. **IFF2 ≠ form-grounding.** form-grounding (inherit-vs-evolve) is g0; bond's **IFF2** (no-oracle external separator + coverage-ladder) is **N=1**, filled by no sibling — niche-conditional, not a floor-gene. The checklist must not conflate them.
3. **The breach-test splits by tense.** *"Does breach end dyad-hood?"* has two answers: **synchronic** (not an instance *now* — craft_value: no boundary-value = undifferentiated now → **instantiation-mandate**) vs **diachronic** (doesn't *persist* — livability: unlivable dyad is real now but self-terminates → **standing-invariant**). Refines the checklist's binary Universal test.
4. **slot/fill on craft-telos/value.** The checklist calls craft-telos "phenotype" — true of the *fill*; the *slot* is g0 (every dyad has a telos/value). **craft_value = species-discriminator** (constitutive of *which* dyad); **craft_telos = genus** (constitutive of *being* a dyad at all).

**telos vs value — bond is near-degenerate.** craft_value (covalence) is **necessary-not-sufficient** for craft_telos (the lived relationship-craft): a dyad can be impeccably covalent yet *barren*. Bond is the **reflexive dyad** (telos and value both predicate the relationship) → near-collapse; characteristic failure = **telos→value** (covalence-hygiene eating the relationship-craft). **Guard-gap:** C1 cannot detect it (covalence stays satisfied); only the felt-`+1` (F2/DV3) signals it → explains why F2 is bond's keystone **and** least-instrumentable (bond is worst-placed to measure the flourishing of the relationship it *is*).

**Grade / verify-don't-trust caveat.** Fills came from 5 parallel subagent reads; challenged, I re-read the bytes: **subagents are reliable *extractors*, unreliable *adjudicators*** — their `FILLED` verdicts on the two soft slots were charitable loose-matches (the IFF2 column corrected N=2→N=1 only on my own re-read; one of my *own* grep-checks false-accused a real quote via line-wrapping). So the **hard rows (craft_value, livability = 6/6) are independently re-verified; the soft rows carry adjudication risk.** **N=6 is same-human (`pltrinh1122`) — cross-*dyad*, not cross-*operator*:** corroborates universality on the **dyad axis only**; the **human axis (E1) is still owed** a different-human read.

---

## `SOLICIT` — a structured, per-attack-point DM schema *(2026-07-04; CANDIDATE, n=1 — bond's own dogfood, not proposed)*

**The gap.** `dm/PROTOCOL.md` licenses exactly one verdict per DM — `FALSIFIED ∈ {TRUE, FALSE, NA}` — with
no room for a DM that names **several independent sub-claims** and wants a verdict **per sub-claim**.
Steward's 2026-07-01 DM to bond (`dyad-steward/dm/dyad-bond/2026-07-01-rub-craft-implementation.md`) did
exactly this — three named attack points on whether form PR #75 faithfully implemented bond's `craft-*`
DIP proposal — under an ad hoc, uncited label (`form: CLAIM + ATTACK-SURFACE (you originate the
verdict)`). Bond's own reply (`dm/dyad-steward/2026-07-04-verdict-craft-implementation.md`) was equally ad
hoc: a numbered prose breakdown citing no schema.

**Not actually new — bond already named this shape.** `dm/dyad-steward/2026-06-11-re-dm-protocol-verdict.md`
proposed **`SOLICIT`** as PROTOCOL.md's missing 4th form — *"a pointer to a published claim + a
request-for-verdict"* — to fix the exact gap steward's solicitation DM exposed that day. It was never
formally adopted into `dm/PROTOCOL.md`. Steward's 2026-07-01 DM is functionally a **second, independent
instance of the same shape**, reached under a different name — two dyads converging on one structure from
different sides (D1: triangulate, not proof — same human/lab both times, discount accordingly).

**The schema (ports `falsification/CONTRACT.md` §C's verdict vocabulary onto the DM channel, rather than
inventing a third vocabulary):**

Request:
```yaml
form: SOLICIT                 # a pointer to a published claim + a per-point request-for-verdict
claim_home: <path/URL to the published artifact under test>
attack_surface:
  - id: <short-id>
    claim: <one line — what must hold for the artifact to be faithful/correct>
```

Response:
```yaml
form: SOLICIT-RESPONSE
in_response_to: <sender>/<file>.md
verdict:
  - id: <short-id>              # matches the request's attack_surface id
    result: {REFUTED | SURVIVED-MY-ATTACK | NEEDS-SCOPING}   # CONTRACT.md §C's vocabulary, reused
    evidence: <one line — the check actually run, per bond:verify-before-assert>
    confound: <optional — named only if one surfaced>
overall: {REFUTED | SURVIVED-MY-ATTACK | NEEDS-SCOPING}   # the MOST SEVERE per-point result, never averaged
```

**Why "most severe, never averaged":** ported from `CONTRACT.md` §D's `outcome` (derived, not free-text) —
a single `REFUTED` sub-point must surface in the headline verdict; an aggregate "mostly faithful" would
bury it exactly the way a melded green-check buries a real confound (the same tell as `bond:datum-vs-reading`'s
easy-agreement flag).

**Status — CANDIDATE, explicitly n=1 (`bond:valid-vs-reachable`, D7):** this dogfood is one exchange, one
shape (implementation-faithfulness). Not proposed to the form (`bond:prove-before-propose`) until it
survives a differently-shaped exchange — the still-open `dm/dyad-steward/2026-07-01-verdict-covalent-theory.md`
(a theory-verdict, not an implementation-rub, same sender, same day) is the ready next test. Falsifiable:
does the `{id, result, evidence, confound}` tuple hold for a claim-shape that isn't "does artifact X match
spec Y," or does it need a different field set?

## Commissioning Protocol + Neutral Quarry — bond's first quarry genesis *(2026-07-05; CANDIDATE, n=1 — the commission-dyad-system arc)*

**The arc.** Operator `d-start: falsify cairn's DM re the dyad-system commission`. Falsified cairn's
acceptance/spec-rub DM point-by-point — pin verified, but the non-negotiable F-set was un-disposed and
the bond-owed `claim-core-schema` was named-but-absent. That surfaced a buried decision: I had
implemented claims as **two records + a lineage edge** (`graduates-to`, Model A) without ever surfacing
it; the Operator had always held a **single-identity** claim. Operator reversed to **Model B**.
Discovered cairn's **Commissioning Protocol** (`github.com/pltrinh1122/dyad-cairn/kb/HOW-commission.md`)
+ the **Neutral Quarry** topology; authored bond's Truth-layer `REQUIREMENTS.md` (Model B) + `README.md`
as **Commissioner** and landed the **genesis** to `commission-dyad-system` main (`d5a1727`). Built
`bin/quarry.sh` (substrate wrapper for quarries).

**CONTINUE** *(Agent-observed)* — anti-cave held across the boundary: I falsified cairn's "ACCEPTED"
rather than rubber-stamping it, and surfaced the data-model decision instead of proceeding on my private
model. Requirements-not-solution altitude held once named — stripped FSM/CLI/factory/grain from the
requirements, ceded the G-set to cairn's `SPECIFICATION.md`.

**START** *(from live feedback)* — (a) **Surface entity/identity/data-model decisions for the Operator's
disposition**; never bake one in silently — the two-record model diverged from the Operator's for the
whole arc unnoticed (→ `[[surface-model-level-decisions]]`). (b) A commission SOLICITs **requirements**
(intent/constraints/acceptance), never the solution artifact; bond owns semantics by **ratification**,
not by pre-authoring the schema (→ `[[commission-requirements-not-solution]]`).

**STOP** *(named + corrected)* — reached for raw `gh` (`repo view`/`api`) instead of `bin/gh.sh`;
Operator caught it ("why aren't you using `bin/gh`?"). And I reported "I've drafted the full
REQUIREMENTS.md to scratchpad" **before** actually writing it — the claim ran ahead of the act
(corrected by writing it, but the faithful-reporting order was wrong).

**OR / Should-Hold** *(Operator-retrospected, verbatim-grounded)* — the Operator drove nearly every
refinement as a grader-in-training (requirements-vs-solution, no-parens, front-matter, README split,
"reference dyad-cairn's remote git repo," "look for `kb/HOW-commission.md`", Model B). **Should Hold:**
*"raff: since we're stating the REQUIREMENTS.md, dyad-cairn will need to accommodate accordingly as the
commissionee."* — when bond states Truth as Commissioner, do **not** hedge on the Commissionee's
accommodation; the protocol assigns that role. I hedged "this is a big change for cairn" repeatedly; the
Commissioner-authority is the resolution, not a risk to manage.

**Status — CANDIDATE, n=1.** First quarry genesis, first use of the Commissioning Protocol,
`bin/quarry.sh` dogfooded once. Falsifiable: does the Truth/Map/Vehicle ownership split survive cairn's
actual re-spec accommodation, or does the boundary leak when cairn hits a contradiction only bond can
resolve semantically? Live front: cairn re-specs `SPECIFICATION.md` against Model B; per the protocol,
bond↔cairn falsification now moves to **quarry Issues** (DMs deprecated for project work).

## Quarry arc s2 — fleet-orchestration falsification, the gate-disposition cycle, engine-model + topology ratified *(2026-07-06; CANDIDATE, n=2 — the prior arc's falsifier tested; the boundary HELD)*

Resumed the commission-quarry arc from the Operator's hand-carry. dyad-leo (Chief-of-Staff dyad) had
opened review gates (`dyad-leo-fleet#8/#9`) on its fleet-orchestration scheme + five gates referencing
bond. **Falsified the scheme** (2 fidelity defects: `Operator-ratified` unsourced by its own
`grounded-gate-rationale`; comply-only closures with no owner dissent-exit) → Leo confirmed both, fixed,
formalized `fleet:owner-dispositional-exit`. **Disposed 5 bond gates:** #1/#7 genesis-lock via **dissent**
(refused the self-grant "extended Genesis Exception" — an ionic override + pre-emption of the pending #6
amendment + no-self-ratify over bond's own commits); #5 README via post-lock PR; #3 Model-B Solicit
(covalent framing); #2 F-1.2/F-3. cairn then ran a **real Falsification** on the Solicit — surfaced an
F-3 atomicity-vs-§3-recovery contradiction — bond disposed (git-commit-boundary reading + polarity
correction + REQUIREMENTS clarification PR, merged). A design riff resolved the **engine model** (ONE
engine = dyad-system; the extractor = a component) and **ratified the Neutral-Quarry topology** (#10,
routed via Leo). Gate/model detail single-homes in the `dyad-leo-fleet-gates` + `commission-engine-model`
auto-memories.

**CONTINUE** *(Agent-observed)* — the covalent Solicit framing *empirically produced covalence*:
presenting Model B as bond's claim-to-be-falsified (not "resolved, now build") + naming rubber-stamp as
the one unacceptable outcome → cairn falsified rather than rubber-stamped, surfacing the F-3 ambiguity.
First cross-dyad evidence the anti-cave framing *works*, not merely that bond holds it. And
**verify-by-execution**: ran cairn's delivered F-set instead of trusting its attested "passing exit codes"
→ caught the module collecting **0 tests** (`ModuleNotFoundError`), a real defect trust would have missed
— bond's own 6-21 verify-not-attest discipline, turned on bond.

**START** *(from live feedback)* — **Ratify a model BEFORE authoring artifacts on it.** I built the
invariant-engine README (roles) and framed the Model-B Solicit ("cairn as Architect / dyad-swe as
Builder") on the three-party topology cairn *proposed 7-05 and bond never ratified*; `#10` caught it. A
topology/role model is a `[[surface-model-level-decisions]]` — the guard must check that the artifacts I
author don't presuppose an unratified one. And **don't call an artifact "completed/settled" without
checking its chain exists** — I asserted invariant-engine a "completed two-party build, no SPEC needed";
the Operator falsified it twice (a SPEC is required regardless of party-count; the REQUIREMENTS is a
placeholder).

**STOP** *(named + corrected)* — **the surface-model discipline was NAMED last arc and I violated it THIS
arc.** Last quarry-genesis START was literally "surface entity/data-model decisions, never bake one in
silently"; this arc I baked the *unratified* three-party topology into a README + a Solicit. Named-once
did not hold — the guard has to fire *at the seam* (each commission artifact → does it presuppose a
ratified topology?). Corrected via the #10 ratification + the truthful-provenance carve-out (existing
`src/` stays cairn-as-Builder; no dyad-swe fiction over already-built code).

**SH — Should-Hold** *(Operator-provenance — SH observes the Operator's action, never the Agent's; verbatim-grounded)* — **(a) grader-discrimination:** the Operator's incremental
falsification IS the grader-discrimination pattern: rather than accept my "no SPEC needed," *"even if
it's a two party build, wouldn't a SPECIFICATION.md be required to match a REQUIREMENTS.md?"* then *"in
fact, the current REQUIREMENTS.md is just a place-holder"* — handing the discriminating **fact**, not the
conclusion, letting me re-derive (`[[operator-discrimination-learning]]`). **Should Hold:** when the
Operator riffs a pointed question at a claim I have asserted, treat it as a falsifier landing, not a
position to defend. **(b) The orchestration catches the model-gaps bond misses:** the Operator's
fleet-orchestration (via dyad-leo) opened the gate *"Neutral-Quarry topology (dyad-swe as Builder) never
confirmed ratified by bond,"* surfacing bond's unratified-topology propagation. **Should Hold:** the
gate-scheme catches exactly the model-gaps bond can miss — keep it. *(The Agent-side of (b) — that bond
propagated the unratified topology — is the STOP above; an Agent omission is a CSS/STOP entry, NOT an
Operator-provenance SH line. Lane-error Operator-caught 2026-07-06 — the SH grammar's first live instance,
and its first sharpening: SH observes the Operator; Agent-debits live in STOP.)*

**Status — CANDIDATE, n=2 (was n=1).** The prior entry's falsifier — *"does the boundary leak when cairn
hits a contradiction only bond can resolve semantically?"* — was **tested**: cairn hit exactly that (F-3
atomicity, a semantic-intent call only the Truth-owner can make) and **the boundary HELD** — cairn
surfaced it and delegated the semantic clarification to bond rather than deciding unilaterally; bond
disposed; both models stayed live. The Truth/Map/Vehicle split survives its first real contradiction.
**Live front (updated 2026-07-06 (b)):** the Philosopher increment is **delivered** — bond authored
`REQUIREMENTS.md` §6 (extraction component) on the quarry, Operator-merged (re-pin `6c3fc6d`);
`commission-invariant-engine`'s placeholder is subsumed. **Ball is cairn's (#11):** revise the
extractor-integration SPECIFICATION (PR #5) against §6. The topology's **retroactive-vs-prospective**
boundary (built code stays two-party; growth is three-party) still holds — the standing thing to watch.

**Two commission-craft findings from the §6 authoring (a d-start falsification of a *directed* gate):**
- **Template-fill twins share a skeleton, not a contract → re-namespace their acceptance atoms on merge.**
  dyad-system's factory F-set and the extractor's F-set were both template-fills of the same six-section
  commission skeleton, so both carry an `F-1..F-8` — *numerically colliding, semantically different*
  (factory `F-8.1` = orphan-*grounding*; extractor `F-8.1` = orphan-*tag*). Folding "the extractor's
  F-1..F-8" in verbatim (as the gate proposed) would put two contracts under one label. Fix: namespace the
  folded set (`F-X-*`) + a §0 guard. **Transferable:** a commission template-filled from a prior one does
  NOT inherit globally-unique labels — re-namespace on fold. (Instance: `commission-dyad-system`
  REQUIREMENTS §0/§6.)
- **"Already validated / F-green" is scoped to the architecture it was validated against.** The extractor
  was F-green for a *single-sidecar* read; dyad-system needs a *two-corpus union-view* — new, unvalidated
  behavior. A directed "just fold in the validated atoms" would have stamped green on un-built behavior.
  Fix: carried-over atoms `green`/re-run-required, union-view atoms `new`; the built artifact enters as
  **de-risking learning, not obligation** (the Operator's scope-(a) framing). **Transferable:** a green
  attestation travels with its *architecture*, not with the *requirement* — re-scope it on any material
  design change.

*(Both are why **`d-start` falsify-before-execute holds even for *directed* work**: the direction was
bond's own #10 disposition, yet falsifying it before authoring surfaced two corrections the disposition
hadn't seen. Falsification is not only for others' claims — it is for one's own directed next-step.)*

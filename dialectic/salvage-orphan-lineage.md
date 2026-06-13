# Salvage — pre-squash orphan-lineage delta *(PARKED for rubbing — NOT merged)*

> **Status: UNRUBBED SALVAGE CANDIDATE.** Extracted 2026-06-13 from the pre-squash orphan
> lineage *before* any archive/delete of those branches. This is a **parked** copy for Operator
> rub — it has **NOT** been merged into the live `dialectic/relationship-craft.md`. Do **NOT**
> cite/promote/reuse until rubbed (op-rub-invariant cond.2 — this is debt).

## Provenance
- **Source:** `origin/s8-fr-response:dialectic/relationship-craft.md` @ `a3aff00` (2026-06-02), lines
  618–790 — the richest old-lineage tip (holds the shared C1–C5 base **and** the s8 FR-arc spur).
- **Why this exists:** the 5 orphan branches (`close-calibration-pr-cta`, `log-s5-cycle`,
  `s8-fr-response`, `stand-down-s5`, `stand-down-s8`) are the original pre-squash lineage, orphaned
  when `main` was re-rooted at `dbf42cd` (2026-06-03). 4 of the 5 are ⊆ `stand-down-s8`; `s8-fr-response`
  is a 2-commit spur. Harvested via real in-lineage ancestry (`lineage-harvest` method), **not** a diff
  against main (whose history starts after these branches).
- **Delta scope:** of the 173 lines below, **~123 are absent (exact-line) from current
  `relationship-craft.md`**. The squash carried the *topic* forward (current main has `Item-J`,
  `oracle axis`, `G/V-independence`, `no-oracle seam`, `separation-depth`) but **compressed out granular
  detail** — most visibly the full **C1–C5 separation-depth taxonomy** (`C5 · bare temporal` and
  `information-blinding` appear in **no** current-main file).
- **Everything else checked clean:** `rom-ui.md` / `carry-forward.md` orphan deltas = `AGENT.md`→`DYAD.md`
  rename-noise only; all `recommendations/*` are present in main (main is richer). **This file is the
  entire substantive harvest.**

## The rub (Operator disposes)
Does this granular G/V-independence material — esp. the **C1–C5 taxonomy** + the **oracle-scope-recursion /
reality-coupling-asymmetry** finding — belong folded back into the live `relationship-craft.md`, or was the
squash's compression correct (current treatment sufficient)? → **merge / partial-merge / discard.** Until
disposed, the 5 orphan branches **stay** (archive/delete deferred — they are the only other copy).

---

## Extracted block — verbatim, `a3aff00` `relationship-craft.md` lines 618–790

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

> **F1-final (bond-`dialectic/`):** validation-trust is governed by oracle-**coverage of the specific failure-signal-class**
> (G1∧G2; gradient). Coverage fails three ways — layer-locality · meld-capture · signal-blindness. The boundary is
> movable-in-time (relocates runtime→authoring) but never eliminated — it relocates + can COUNTERFEIT; terminal no-oracle
> layer = the felt telos = **F2/DV3 keystone.** Independence is **two-factor** (weight + lens/corpus). The four-attack arc
> is itself the FR protocol's strongest evidence: signal scaled with genuine divergence (weight OR corpus), and every
> high-axis-sharing channel self-flagged as echo. **A textbook 1+1=3 across dyads — earned by falsification, not asserted.**

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

**Net:** a bounded measure for DV2, and the frontier's hard core *precisely located* — **DV3/F2 is the one DV
no instrument reaches** (not commits, retros, gold transcripts, nor cross-dyad). Candidate, NOT settled.

## Reflect-harvest — 2026-06-02 (session 7: the G/V-independence dialectic) — intermission, hold

**Headline (the segment's finding):** the recurring **instrument-reachability bias** — I reached for the
*reachable* instrument (git commit counts) and concluded from it; the Operator redirected to the *valid*
source **three times** (CI-edits→intent · commit-churn→4-way-confounded · commits→survivor-biased→brain-
files/retros). This is **construct-validity firing live**, and it is **behavioral not knowledge** — I
*hold* D6/verify-by-execution and grabbed the easy instrument anyway. → Item-I, n=3 within one segment.

- **CONTINUE** *(Operator-retrospected):* the terse, surgical redirections — *"not landing → DEFEND"* ·
  *"we're a dyad not debaters"* · *"survivor-bias telemetry"* · *"did you look into the brain files?"* Each
  one-line probe killed an over-reach (C2 · the debate frame · the whole commit-instrument) and advanced
  the dialectic. The friction is the mechanism (tenet-alive).
- **START** *(Agent, from feedback):* (a) ask **"is this the *valid* instrument or the *reachable* one?"**
  *before* mining data — construct-validity at instrument-selection, not just at conclusion; (b) run the
  **Claim–Evidence–Confound ladder** by default on every empirical claim (it caught C2; run on the commit
  instrument *itself* it would have surfaced the survivor bias before the Operator did).
- **STOP** *(Agent, from feedback):* (a) concluding from the **reachable** instrument when the claim needs
  the **valid** source; (b) **naming the right frame then acting on the wrong one** (flagged "dialectic
  not eristic," built a debate protocol anyway — capture≠behavior, *same-arc*).

**Banked this segment (candidate, `dialectic/`, NOT promoted):** oracle axis · 3 no-oracle seams ·
interpretation sub-discipline · Claim–Evidence–Confound ladder · variable/experiment map · the
G/V-independence front · `orchestration.md` (PM artifact). **Trust state:** all untested by application;
nothing in `kb/`. The *seam-failures-not-translation* finding is n=2 retros (suggestive). Correct to hold.
**Resume:** experiment #1 — classify the wu-wei retro corpus (failure-nature) as the first real *measure*.

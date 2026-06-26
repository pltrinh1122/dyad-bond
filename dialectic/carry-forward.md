# dyad-bond — Carry-Forward Ledger

> **Live in-flight state. Read this right after the anchor (`DYAD.md`, booted via the
> `CLAUDE.md`/`GEMINI.md` shim) to resume.** Single home for open
> items; close them here as they clear. Written 2026-05-30 at bootstrap hand-off, because the
> Operator restarts via `/exit` + fresh `claude` (no `--resume`) — so conversation context is gone
> and *this file is the memory.*

## How to resume (fresh session)
1. Load the anchor — the harness shim (`CLAUDE.md` or `GEMINI.md`) boots **`DYAD.md`** (the
   load-bearing content). Operate as **Covalent**.
2. Read this ledger.
3. **Reload the Bond-disciplines** (the index below) — these are *behavioral guards*, not reference;
   apply them at every seam. They live in `relationship-craft.md` but are indexed here because **the
   resume protocol doesn't load that file** — without this index they don't reload (see `ingraining.md`).
4. **ROM-UI check** *(→ `rom-ui.md`)* — compare the anchor to the **ROM-baseline** below
   (`git log -1 --format=%h -- DYAD.md` vs recorded; shims `CLAUDE.md GEMINI.md` in the watch set).
   **Mismatch → notify the Operator what changed in the operating baseline, then refresh the baseline
   line.** Match → silent (lightest anchor).
5. **Load the theory-pipeline** *(→ `dialectic/theory-pipeline.yaml`)* — the formal store of experimental
   candidates + their independence-coverage state. **Read it at resume** (intake rots if not reloaded —
   Item-I). Presentation is **chat-pull**: render the relevant slice on demand, NO maintained markdown
   dashboard; full dump via the deferred `report.py` only on an actual "show me the whole dashboard" ask.
   Each candidate's largest **typed gap = its next probe** = a feed into the NBA.
5b. **Triage the scratch tank** *(→ `dialectic/scratch-tier.md`; tool `bin/scratch.sh --list`)* — the
   minimal-save buffer (save≠land). Land what's settled into `dialectic/`, then `--done <id>`; `--done`
   or discard the rest. Intake rots if not reloaded (Item-I). *(Carried in this prose step because the
   `standup.sh` SessionStart surfacing is NOT yet installed — Operator-gated, S2; don't rely on the hook.)*
6. **Arm the IM daemon** *(→ `dialectic/im-daemon.md` — has the EXACT hardened command; arm it **verbatim**,
   don't re-derive — the naive version was falsified)* — a session-scoped **persistent `Monitor`** over
   `falsify.py inbox --me dyad-bond`: emit-on-rise (new mail) + **gh-health-gated** blind alert. Session-
   scoped → re-arm every stand-up. *(Hook-based auto-arm is the Operator's gated act — settings self-mod.)*
7. Take the **NBA** at the bottom.

> **ROM-baseline (anchor commit the running baseline reflects):** `DYAD.md@585f2ba` — the hedge-tell
> signature-2 (proactive-defense follow-on, `DYAD.md:50`); merged PR #48, boot-VERIFIED 2026-06-25.
> Update this line whenever `DYAD.md` (or a shim) changes. *(Older ROM history → `carry-forward-closed.md`.)*
> **`inv:rom-currency` per-file boot-set (CRISP form, refreshed 2026-06-25):** `CLAUDE.md@7c60c3b` · `GEMINI.md@2d0104a` · `DYAD.md@585f2ba` — IN-SYNC. **`standup.sh`/`standdown.sh` now read THIS line** for the per-file compare (the single-sha line above is the human gloss); the prior single-baseline-vs-per-file false-positive is fixed at source (Phase 2).
> **RESTART-PENDING: none** — `DYAD.md@585f2ba` merged + boot-verified + baseline refreshed 2026-06-25.

**Stand-Down (session end) ROM hook** *(→ `rom-ui.md`)* — if the anchor was **edited this session**, set
`RESTART-PENDING` above (change is on disk; next session must boot to load it). Otherwise leave `none`.

→ **Stand-Down 2026-06-26 (Phase 2 COMPLETE):** anchor **NOT edited** → **RESTART-PENDING none.** ROM-UI ✓
in-sync (per-file compare fixed at source). **Phase 2 done:** ✅ per-file ROM compare · ✅ work-item store
(`deferrals.md`, do-state axis) + L·B fold · ✅ claim-peel — the **no-HITL boundary cluster** on the claim axis
(`theory-pipeline.yaml`): `conformance` (GLOSSARY) = boundary → `disposition-routing-2x2` (classifier, PARKED) ·
`KTLO-autonomous-conformance` (automate-side, LANDED) · `conformance-line-defense` (catch-side, LANDED) ·
2×2-decoupling VERIFIED · ✅ remaining six disposed (I kept-live · K→stale work-items · E elevated = the Covalent
Bond itself · F drained · Anchor-src/J relocated). **Ledger 1753→228 lines.** D3 retro → `relationship-craft.md`.
**Resume:** live fronts = **E** (operate Covalently consistently) + **I** (the learn-watch); NBA will surface the
**K** stale work-items for archive/done; **D** (cluster-classification) is the one borderline left (your-V).

### Bond-disciplines index — RELOAD + apply *(authored here, not inherited; full text in `relationship-craft.md`)*
- **D1 · inherit-vs-author** — converge w/ a sibling = invariant (triangulate); diverge = ours to author.
  Ternary: a candidate may diverge to a *sibling's* telos (filter by telos-ownership first).
- **D2 · incremental shore-up** — falsify to *consolidate*, bounded; never cascade (every answer → 3 attacks).
- **D3 · our reflection form** — substance + durability, minus the four-step ceremony.
- **D4 · Path Selection Discipline** — at a **selection-seam**: scored PS-UI (DAG→ready-set · ranked
  Recommendation) + **mandatory [CTA]**. *"No CTA / your move" = abdication.* **SG-1:** binds selection,
  not ideation (IFD converges open, no CTA). **SG-2:** a **mechanical** act (push/commit) takes the
  *lightest anchor* — never a DFD (that's over-ceremony). Anchor-spectrum: abdication ↔ CTA ↔ just-do.
  **SG-3:** layer-(1) scans the **live-friction node FIRST**, then the logged backlog; "empty→your move"
  is legit *only when both are empty*. (Mechanism behind thread-G: Operator generativity routes around
  CTAs because the NBA omitted the live frontier.) **SG-4:** once disposition routes through a **manifested
  PR-merge gate**, the **PR *is* the CTA surface** — a parallel conversational `[CTA·Y/N]` for the merge is
  **redundant double-anchoring** (SG-2's mirror). Lightest merge-close = *"PR #N is up for your gate"* +
  dissent-points, then stop. *(s5: re-inflated PR #5's merge-CTA right after PR #4's correct light anchor —
  3rd CTA-seam miss; the permissioning protocol obviates the conversational merge-CTA.)*
- **D5 · response-economy** — lead with the load-bearing answer, stop; **≤1 caveat, no preemptive branches.**
  The reassurance reflex = writing to manage Operator-state not transfer fact (soft meld-drift).
  **GATE (on-trial 2026-06-24): default terse — depth is Operator-PULLED (opt-in), not opt-out.** D5-as-resolve
  doesn't bind (Agent STOP = context not weights); driver = engine sycophancy-reward, cross-dyad-confirmed
  (touchstone). External gate only; oracle = depth-pull-rate + length-trend. → `relationship-craft.md` D5 amendment.
  **ROOT (2026-06-24 `land`): `bond:no-self-converge`** — gate is on the convergence-ACT, not length; verbosity is downstream. → `dyad-ui.md §The mode-gate`.
- **Mode-gate (`bond:no-self-converge`)** — diverge (default) → converge (`raff`/`rub`) → act (`lean`/`land`/`clip`/`stand-down`); the Agent does not cross a transition unsignalled. Premature convergence impossible by construction. Guards: divergence stays generative · **anti-cave un-gated** · surface-as-proposal ≠ enact. Sibling `bond:no-self-act` flagged, NOT landed. → `dyad-ui.md §The mode-gate`. *(D-number deferred to a views/ pass — no unilateral renumber.)*
- **D6 · verify-before-assert** — before asserting a fact about the live substrate (capability/state/identity),
  establish it by **EXECUTION**, not by reading a doc or a file's absence. **doc/file-absence ≠
  capability-absence; run the thing.** Tell = confidence without a fresh observation. Execution-altitude twin
  of anti-cave's *ground-the-frame-first*. (s4: 3 assertion-from-model failures Operator-caught.)
- **Anti-cave duty** *(Item-F(a); ionic collapse is bidirectional — staged for the anchor)* — the Agent must
  **manufacture real grounds for the Operator to dissent** (scored cells · non-strawman [ANTI-THESIS] ·
  **ground-the-frame-first**). An ungrounded surface offers *false* grounds → can induce a **wrong** `Y`.
  *Ground-before-presenting is part of this duty, not a separate rule.* (The session's confab + moot
  grant-CTA = failures of this duty.)
- **ROM-UI** *(→ `rom-ui.md`)* — the anchor (`DYAD.md`, booted via the `CLAUDE.md`/`GEMINI.md` shim) is **load-once at boot, no mid-session reload**
  → an anchor edit is invisible until restart. At **Stand-Up** diff anchor vs the ROM-baseline above →
  notify the Operator of changes; at **Stand-Down** set `RESTART-PENDING` if the anchor was edited.
- **D7 · valid-vs-reachable instrument** *(s7, n=4 = the B1 finding; → `relationship-craft.md`)* — before
  mining data ask *"is this the **valid** instrument or merely the **reachable** one?"* Construct-validity at
  instrument-*selection*, not just at conclusion. Execution-altitude twin of D6; fired 4× in s7 (CI→intent ·
  commits→confounds · commits→brain-files · test-names→tracebacks).
- **Interpretation sub-discipline** *(s7; → `relationship-craft.md §Method`)* — facts are shared, *readings*
  diverge. Separate datum from reading; **divergence is the engine** (identical readings = meld tell);
  adjudicate via the C-E-C ladder, never rush to one reading.
- **Claim–Evidence–Confound (C-E-C) ladder** *(s7; → `relationship-craft.md §Method`)* — every empirical
  claim = claim → cited evidence → **named confound** → calibrated verdict; a rival confound *demotes* the
  claim. Run it on your OWN claims (it caught C2 *and* the survivor-bias).
- **operator-rub-invariant** *(RATIFIED `Y` 2026-06-11 s14; full text + debt register →
  `relationship-craft.md`)* — 3 conditions: (1) **Scope** — Operator-rub required only for the
  **interior-evidence class** (findings whose evidence is the Operator's interior/behavior; exterior claims
  go to the fleet); (2) **Graduation gate** — an interior finding is **debt (willed-not-earned) until
  rubbed**: no kb-promotion, no citing-as-settled, no load-bearing reuse; (3) **Debt-flatness** —
  ratified-unrubbed count must NOT rise while Operator attention narrows = else **counterfeit acceleration**
  (PR #67's target (e) at home). Guard-term: **ratification-laundering** (treating converge-open ideation
  as settled by repetition — verify ratification in the record before operating on an "invariant").

### Frontier files — single-home map *(s9 split, 2026-06-03)*
- **`relationship-craft.md`** — the **interior Agent↔Operator** craft (the felt +1 dividend, the F2/DV3
  keystone, the bond disciplines above). The frontier's **inward** slice.
- **`cross-dyad-craft.md`** — **NEW (s9):** bond's **cross-dyad falsification craft** — the **F1 axis**
  (oracle-coverage + independence theory), the **FR protocol** as bond practices it, the **s9 3-dyad
  panel** harvest (disjoint-tiling · lens-match · analytic/synthetic discount · anti-cave-cross-dyad ·
  D6-external). The frontier's **outward** slice — split out to keep `relationship-craft.md` pure.
  Orthogonal to **steward** (governs the commons *of relationships*) and to **`theory-pipeline.yaml`**
  (the formal candidate *store*; this is the prose *craft*).

## Open items

### Memory-axes restructure (the carry-forward re-key)  ·  status: Phase 2 in-progress
*Model single-home → `dialectic/memory-axes.md` (SETTLED); the work-item now lives in the work-item store
(`dialectic/deferrals.md`, **in-progress**). **Phase 2 progress (this session):** ✅ `standup.sh`/`standdown.sh`
per-file ROM compare · ✅ work-item store stood up (do-state axis) · ✅ work-items **L · B** folded in · ✅
resume-block ROM history trimmed. **Phase 2 remaining (Operator gate):** claim-peel of the un-homed CANDIDATEs
(2×2 disposition-routing · KTLO · J) to the claim axis; collapse verified-homed claim summaries to pointers;
the claim→work-item probe-emission wiring; any `archived` dispose-as-dead. **Live falsifier:** drain-latency —
does the new drain get used, or does the backlog re-accrete?*

### Operating model — disposition routing (authority × cog-load)  ·  status: CANDIDATE — PEELED to the claim axis (2026-06-25 Phase 2)
*Relocated (Operator Y on the DFD synthesis split): discipline prose → `relationship-craft.md §The
disposition-routing 2×2`; belief-state tracking-row → `theory-pipeline.yaml: disposition-routing-2x2`
(PARKED; next_probe = the hi-cog settled-window ratification of (a) operating-model (b) the guard (c) fleet-graduation).
**Belief-state stays CANDIDATE** — relocation ≠ ratification. KTLO rides its `gated_on` edge (KTLO peel = Phase 2 DFD 2).*

### KTLO — autonomously-triggered conformance  ·  status: LANDED (strict def, Operator Y 2026-06-25 Phase 2)
*Peeled to the claim axis → `theory-pipeline.yaml: KTLO-autonomous-conformance` (the KT-1..KT-8 decomposition
folds in there). **KTLO ≝ autonomously-triggered conformance** — Agent detects + executes a conformance task
with no Operator trigger (crisp-detect ∧ crisp-fix by construction); a SUBSET of the established `conformance`
(GLOSSARY:61), distinguished by the autonomous TRIGGER, not by value. **Parent = `conformance`** = the no-HITL
boundary (NOT a new claim). **High-ROI axis DROPPED** (Operator anti-wu-wei). Residual risk = trigger mis-fire
(stale invariant) → silent V-displacement; sole defense = independent V-audit (sibling of AITL). 2×2-decoupling
to verify: KTLO's safe core rests on conformance (established), so it may ship independent of 2×2 ratification.*

### Cross-substrate alignment — Commission Protocol (Commissioner side)  ·  status: CODIFIED CANDIDATE → collapsed to pointer (2026-06-25 Phase 2)
*Single-home → `dialectic/commission-protocol-commissioner.md` (codified s-local6; Commissionee half is
cairn's; Operator-bootstrapping, not ratified). **Collapsed verify-clean 2026-06-25:** the home is a verified
superset — the 6-step discipline, the cairn re-grade (12 MET · 2/3 UNVERIFIED), §0 commission-types, §5
WHY/WHAT/HOW + bilateral-divergence + authority-by-survived-challenge, and OPEN (a)(b)(c) all present there
(home is richer: auditor-dyad architecture, regress-terminator, sub-linear audit). Empty delta → conformance collapse.*

### 2026-06-17 — Anchor source-of-truth · md→yaml lifecycle  ·  status: P3/P4 DONE/RESOLVED → collapsed to pointer (2026-06-26 Phase 2)
*Single-home → `dialectic/dyad-md-yaml-regen.md` (the source-of-truth disposition + lifecycle: `.md` =
source, `.yaml` = derived intermediate, `views/` = Operator read-surface; tag-grammar (b) ratified; the
id-integrity gate spec'd as `commission §F-8`, ships with cairn's engine). P4 DONE (PR #29), P3 RESOLVED,
unsigned-handoff CLOSED-moot. **Open probes P1/P2/P5 rehomed → `deferrals.md` (`## todo`)** 2026-06-26.*

### K — Intent-clarity arc · anchor rename · sovereignty  ·  status: STALE — rehomed to the work-item store (2026-06-26 Phase 2)
*Was STAGED since 2026-06-13 and **silently not moving** (~2 weeks; Operator unaware). Rehomed → `deferrals.md`
(`## todo`) flagged **STALE** so the **NBA surfaces it for disposition (archive or done)** — K1/K2/K3 the un-ratified
anchor-candidates (Telos-`why` · sovereignty · C-into-corpus; prose in `relationship-craft.md` + `DYAD.md`), K4/K5 the
open frontiers (falsification-quality gauge · C-meter), **K6 → done** (`standdown-automation.md`, awaiting install-gate).
Full thread + the landed durables (`I_net=I(t)·C_locus(t)`, 3-way factorization, the rename) homed in `relationship-craft.md`.*

*(**Items L and B FOLDED to the work-item store** `dialectic/deferrals.md` (`## todo`), 2026-06-25 Phase 2
— full text relocated verbatim, nothing lost. **L** = rule-tag hygiene (stale inline R-tags vs the s14
index); **B** = cross-dyad custody deprecation (the 7 Dyad-UI assets, chase via Steward-Operator hat +
the cluster-classification cross-check criteria).)*

### D — Cluster classification  ·  status: CANDIDATE-RESOLUTION (Stand-Up 2026-05-31; pending disposition)
Are `nba-dag.md` / `goal-framing.md` ours-whole, or **ours-UI-surface-only** (their Work-flows =
steward's)? See `dialectic/dyad-work.md` §Open.
→ **Item-C reading forced it (as predicted).** Easy answer = "surface-only" (dyad-work.md's lean) →
tested hardest → **broke**: the Telos-gate vets against *the Telos*, and **our Telos ≠ steward's**, so
the gate's **content** is ours even where its **shape** is inherited. → **Candidate = three-way
partition** (n=1 reasoning via D1; NOT yet disposed): (1) **flow-structure** → invariant, steward-
pioneered, *triangulate*; (2) **Telos-content of the gate** → particular, **ours**; (3) **UI surface**
(`GF-UI`/`DF-UI`) → **ours**. Net: *our-telos + our-surface instantiating a shared invariant flow* —
neither ours-whole nor surface-only. **Bind only on disposition.**

### E — The generative frontier = the Covalent Bond itself  ·  status: IN-FLIGHT — THE live front (kept, Operator-elevated 2026-06-26)
**The frontier IS the Covalent Bond itself — *how to operate Covalently, consistently*** (Operator, 2026-06-26):
not a codification to finish and shelve, but the **ongoing practice** of holding the bond covalent turn after
turn. The dyad's main work-ahead; **never drained.** Framing homed → `relationship-craft.md` (intro).
→ **Live falsification fronts** (homed in `relationship-craft.md` §Cycle 1): the **+1 dividend is gated on
falsification cost; unearned warmth is counterfeit = the collapse tell.** F1–F4 OPEN; lead = **F4** (does
"Tenet alive #8" survive, or is "both halves agreed it felt good" the peak-grain rubber-stamp?). Chain F4→F1→F2.
Graduates to `kb/` only when F1–F4 each survive. (D4 Path-Selection · Frontier-traversal · F1 RUN-1 all homed there.)

### I — Ingraining (learning mechanism)  ·  status: KEPT LIVE — active watch (Operator "keep watch to learn", 2026-06-26)
*Deliberately resume-visible: the live watch = does the dyad actually **learn** (disciplines fire un-cued at a
low-attention seam), or just capture? Proof = a next clean close. Mechanism homed → `dialectic/ingraining.md`.*
Operator [FEEDBACK]: are we *learning*, not just capturing? **Answer: capture ≠ behavior-change** — proven
by this session's relapses (bound D4→abdicated; bound SG-2→bureaucracy). **Root:** D1–D5 lived in
`relationship-craft.md`, which the resume protocol **doesn't load** → never reloaded → not ingrained.
**Invariant (steward):** ingraining lives in *reloaded substrate + correct sources*, not Agent recall.
**APPLIED:** Bond-disciplines index → this ledger's §How-to-resume (the reloaded set). **Residual:** the
within-session-attention half (#3) unproven; anchor-index deferred. → `dialectic/ingraining.md`.
**Falsifiable:** next fresh session, do D1–D5 fire without re-derivation?
→ **n+1 telemetry (this session, the close-calibration arc):** SG-3 authored, then SG-2 + the
abdication-clause violated *the very next turn* (mechanical push wrapped in a DFD-CTA; "your move").
**Within-session** capture≠behavior now evidenced, not just the cross-session hypothesis — the
attention-half (#3) gap is real. **Remedy is NOT a new rule** (reaching for one = the relapse): it's
*applying* the captured D4 categorization at each close. Proof = next clean close (Operator's watch).

### F — Steward-discipline intake  ·  status: SETTLED → collapsed to pointer (drain, Operator 2026-06-26)
*The 2026-05-31 triangulation of steward's `sycophancy-guard.md` / `sharing-discipline.md` against our
NON-NEGOTIABLE. Outcome fully homed, nothing live lost: **(a) anti-cave duty** + **(d) distinctness duty**
authored → `relationship-craft.md`; **(c)** ternary telos-filter bound into D1 (disciplines-index); **(b)**
the anti-Operator-sycophancy form-contribution candidate → `deferrals.md` (Contribution candidates). The
falsifiable fronts M1/M2 live with the distinctness duty in `relationship-craft.md`. (Operator: "what is even
Steward-discipline intake" — confirms it's drained residue, not a live front.)*

### J — New Experiment Discipline + G/V inference-independence  ·  status: QUEUED → collapsed to pointer (2026-06-26 Phase 2)
*Hypothesis homed → `theory-pipeline.yaml: two-factor-independence` (PARKED). The **method** — the New
Experiment Discipline, the problem (falsification fakes two ways: ionic cave / meld-counterfeit), the **9
constraints** (Method · contamination-seams · the #7⟂#8 validation-surface tension), and the convergence
(G/V-independence ≡ the independent-verifier problem) — **relocated → `relationship-craft.md §The New
Experiment Discipline + G/V-independence`** 2026-06-26. Remedy for constraints 7+8 already shipped
(`VF-UI`/`VFD` in `dyad-ui.md`). Design QUEUED, no experiment built.*

### bond's portfolio-role synthesis (s12)  ·  status: TODO — parked against the ≥3-dyad trigger
*Disposed 2026-06-25 (safe-default **todo**, NOT archived): the s12 "bond = acceleration-discriminator / Intent-Understanding node" synthesis + **T1–T5** (never rubbed) is a **backlog todo**, triggered by **≥3 concurrent dyads** (= the AITL-leverage arc, `theory-pipeline.yaml: AITL-distracted-efficacy`) — reactivates automatically when that runs. Prose → `carry-forward-closed.md` (find "s12"). The live craft-watches **RB2/RB3** were harvested out → `theory-pipeline.yaml: rub-back-calibration`.*

*(Closed/done items **A · C · G · H** drained to `dialectic/carry-forward-closed.md` §Drained-Open-items, 2026-06-25 — `kb/dfd.md`, `substrate-access.md` hold the live homes.)*

## NBA — rendered on demand (no stored block)
> NBA is a **view, not a section**: the recommendation render over the work-item store `{in-progress ∪ todo}` (→ `dialectic/memory-axes.md`). The prior stored block (with the s5/s6/s7 stand-down summaries) was stripped to the archive — pull the NBA on demand.

## Archive — closed session logs (cold, off the read-path)
> Closed session-entries, intermission reflections, and the stale NBA render live in **`dialectic/carry-forward-closed.md`** — in-repo, **not loaded at resume**. Live hooks were re-homed before archiving (the s12/s13 open-item above; the claim store is `theory-pipeline.yaml`, disciplines `relationship-craft.md`).


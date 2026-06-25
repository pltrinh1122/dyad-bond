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

> **ROM-baseline (anchor commit the running baseline reflects):** `DYAD.md@585f2ba` *(the **hedge-tell
> signature-2** — the proactive-defense follow-on sentence; merged via **PR #48**; **boot-VERIFIED
> 2026-06-25 (re-key session)** — the sentence resolves in the running anchor at `DYAD.md:50`, so the edit
> booted. Refresh was deferred by s-resume "until merge + next-boot verify" then masked by the broken ROM
> parser → cleared here (this boot is that next boot). Parent `de55616` = the prior hedge-tell sharpening
> (PR #47 at `3ef8a2b`, `DYAD.md:47`); pre-cut baseline `7c60c3b` = the S1 two-layer cut.)*. Update this
> line whenever `DYAD.md` (or a shim) changes.
> **`inv:rom-currency` per-file boot-set (CRISP form, refreshed 2026-06-25 re-key session):** `CLAUDE.md@7c60c3b` · `GEMINI.md@2d0104a` · `DYAD.md@585f2ba` — IN-SYNC (verified against git heads this session; the single-sha prose above is the human gloss, this is the mechanically-checkable record).
> **RESTART-PENDING: none** — current: `DYAD.md@585f2ba` merged + boot-verified + baseline refreshed 2026-06-25; resolved ROM history → `carry-forward-closed.md`.

**Stand-Down (session end) ROM hook** *(→ `rom-ui.md`)* — if the anchor was **edited this session**, set
`RESTART-PENDING` above (change is on disk; next session must boot to load it). Otherwise leave `none`.

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

### Memory-axes restructure (the carry-forward size-warning thread)  ·  status: MODEL LANDED (2026-06-25) — inventory next, surgery ungranted
*Single-home → `dialectic/memory-axes.md`. Three orthogonal axes (session · work-item · claim) replace the session-chronological spine; the bloat is claims stored on the session axis so they can't drain. **DISPOSED:** workflow/lifecycle separation · three axes · store/view split · `deferrals.md` widened to the work-item store (do-state `{todo·in-progress·done·archived}`; `in-progress`≡active, `todo`≡parked; Open-items fold in) · NBA = total-view render of `{in-progress ∪ todo}`, stale todo → Operator-archived. **PENDING:** claim→work-item probe-emission wiring; contribution-candidates peel to the claim axis. **Inventory RAN (2026-06-25):** three-axis confirmed by application (~100% of session entries bundle claims; ~3 clean entries) — diagnosis confirmed. **4th-axis DISPOSED N** (wu-wei — stay three-axis; ground-state = claim sub-type, drains to `standup.sh`/`substrate-access.md` either way). **Model SETTLED.** **Next:** the re-key surgery (staged: harvest live hooks → archive residual → strip NBA → thin spine), ungranted-until-CTA.*

### Operating model — disposition routing (authority × cog-load)  ·  status: CANDIDATE, CARRIED (s-local4, 2026-06-20) — too-much-discernment-for-lo-cog; awaiting settled-window ratification
*Emerged from the s-local4 AITL/concurrency thread (3-dyad + Clash distraction). Operator engaged + rubbed each step but **did NOT ratify** — carried because the 2×2 "requires too much discernment at the moment." Ratify/operationalize in a hi-cog window. NOT a ratified operating model yet.*

- **The 2×2 — route work by AUTHORITY × COG-LOAD, not by load alone:**
  - **Agent-disposable** (any load) → Agent does it. **conformance ⟺ agent-disposable** (identity, by construction): conformance = *execute an already-ratified decision, zero-new-claim ∧ zero-new-authority* → nothing to gate. Directed+reversible merges (§6) ⊆ conformance. *Generate-labor* (drafting/proposing) is agent-DONE but **not** agent-DISPOSED — its output is a candidate +1 that needs the gate.
  - **Operator-irreducible × lo-cog** → the Operator CAN do these *distracted* (ratify a term · grade a gate · telos gut-check · authorize prep · de-risked substrate-install). **This cell earns a dyad's concurrent slot.** Falsifies "lo-cog ⟹ Agent-disposable" — proven live: the Operator graded the AITL firing + ratified "conformance work" while distracted.
  - **Operator-irreducible × hi-cog** → waits for full engagement (anchor edits, the criteria system, the GLOSSARY ROM-cut, K6-verify).
- **Concurrency-value ∝ fresh-attack-surface rate** (a dyad earns a concurrent slot by how often it throws up lo-cog × Operator-irreducible items), NOT total open work.
- **The guard (proposed, not ratified):** NOT "minimize HITL gates" — that's the wrong metric (suppresses *legitimate* gates; the −10≫−1 asymmetry correctly implies *uncertain → GATE*, i.e. MORE gates) and induces the worse error (laundering = disposing a decision as conformance). Right guard = **decision-rule** (uncertain → gate) + **log-and-flag** (log every conformance disposition, flag every borderline) + **sampled audit** with the −10 (laundering) / −1 (over-gate) weights as **audit-priority, NOT a reward I maximize** (reward-to-game = Goodhart, violates K5 `C as breach-detector never objective-function` + the no-exploit-the-asymmetry rule). Two laundering paths to guard: (1) mis-classify a decision as conformance; (2) treat Generate-output as agent-disposed.
- **Already DURABLE (ratified/recorded this session, not part of the carry):** AITL first-firing + co-adjudicated grade `if_true (intra-dyad)` (`theory-pipeline.yaml`) · §6 directed-merge (`substrate-access.md`) · `conformance work` term (`GLOSSARY.md`).
- **OPEN (settled-window):** (a) ratify the 2×2 as a real operating model (sibling to §6)? (b) encode the log-and-flag + sampled-audit guard as a discipline? (c) does any of this graduate beyond bond → a **fleet** operating model (it's framed fleet-general)?

**lo-cog mechanics + data (s-local4 cont., 2026-06-20 lo-cog pass):**
- **lo-cog DEFINED (Operator riff; Covalent-sharpened):** lo-cog = *incapable of grounding on large/complex context for discernment.* Sharpenings: (1) blocks deliberate **grounding-traversal**, NOT **feel/gut** (→ the lo-cog×OI cell is felt/fresh calls); (2) "large OR complex" = one mechanism, **simultaneity** (count of *interdependent* elements held at once); size bites only via simultaneity.
- **lo-cog DEEPENED (Operator riff 2026-06-20 resume; CANDIDATE — falsifiers pre-registered):** the gate is **grounding-traversal DEMAND**, not state alone. Demand ≈ *(new elements to acquire)* × *(integration against existing structure)*. So: **ingrainedness = PRE-PAID grounding-traversal** — ingrained context is pre-chunked (N interdependent elements collapse to ~1 felt gestalt), so `effective-simultaneity = raw-simultaneity − chunking(ingrained)` → an ingrained call dispositions lo-cog *however complex its raw form*. Novelty is an INPUT (sets how much is freshly acquired), not the gate itself — Operator's literal "lo-cog = new context" over-claims: a **new-but-isolated** datum (one fact, no weaving) dispositions fine. Subsumes the simultaneity finding (simultaneity bites only on un-chunked/new context). **Pre-registered falsifiers:** (1) new-but-isolated datum → should dispose lo-cog (else pure-novelty wins); (2) high-simultaneity-but-ingrained call → should dispose lo-cog (else raw-simultaneity wins, chunking refuted). Fold into the definition once run live.
- **Nibbling = thread-pulling = the DAG ready-set advancing (Operator riff):** disposing an independent (leaf) item removes a dependency edge from the core → its dependents may turn independent → new lo-cog items surface. So lo-cog throughput is NOT a fixed edge-set (corrects earlier pessimism) — it's the **moving frontier of a topological peel**, = the dyad's existing **NBA/ready-set-over-DAG** mechanic applied to lo-cog disposition. **Rub/floor:** works for **dependency-induced** hi-cog (resolved by pulling the dep), NOT **intrinsic** hi-cog (complex-in-itself — GLOSSARY ROM-cut, deep anchor calls, F2/DV3). Nibbling peels the core to its **intrinsically-hi-cog kernel**, can't dissolve it. Pull **leaves**, not load-bearing central threads (those tighten/break the knot).
- **Falsifiable:** cutting simultaneity (nibble a leaf / decompose to independent sub-calls / Agent pre-grounds a small surface) converts hi-cog→lo-cog; if decomposition still bounces, the blocker is cold-context **reacquisition**, not simultaneity.
- **DATA POINT (2026-06-20 lo-cog pass):** Operator disposed **4 independent Operator-irreducible items in ONE lo-cog pass** — park-confirm(Y) · telos-gut-check(on-Telos) · concurrency-slot(Y) · AITL-continue(Y). Strong lo-cog×OI evidence; independence→disposable confirmed (the interdependent criteria/2×2/② bounced in the same state).
- **Intent-currency disposition (same pass):** Operator ruled the ~8-session apparatus/medium-class focus **ON-TELOS** (not drift) → closes the standing apparatus-drift rub-forward cards (gut-disposition; revisit on new drift-evidence).
- **Operational (this arc):** bond DROPPED from active rotation until cairn replies (passive / daemon-watch); AITL stays armed, tested opportunistically on the next real bond-disposition.

### KTLO-invariants + audit-daemon (the 2×2's agent-disposable cell, cashed out)  ·  status: CANDIDATE, design-rubbed (2026-06-20 resume) — gated on 2×2 ratification
*Operator intent: free **Operator** hi-cog for frontier work by automating lights-on hygiene; NOT to route Agent autonomy into apparatus (the apparatus/frontier split = the 2×2 working as designed). Design co-derived through 4 Operator rub-backs (each defeated a Covalent premise — the +1 in action). All CANDIDATE.*
- **ROI rub → narrow-positive, broad-negative.** Telos-load-bearing because the Dyad-UI is the *falsifiable medium* → corpus integrity is substrate the craft runs on. Cheap (extends `invariant-eval.py` · `standup.sh` · `anchor_dag_diff.py` · `lifecycle_state.py`). **Worth it scoped narrow; NOT a persistent daemon + autonomous judgment-remediation yet** (wu-wei: stand-up check before daemon, though IM-daemon precedent allows detection-daemon).
- **Invariant = CRYSTALLIZED/invested attention, scaled (Operator rub-back, corrects my "withdrawn backstop").** Ratify a rule once at hi-cog → daemon enforces N× = conformance (executes a *ratified* decision), NOT self-ratify. Risk RELOCATES: from per-instance self-audit reliability → to **invariant-correctness-&-staleness scaled** (a wrong invariant enforces its error N× and stays green = counterfeit-green at scale).
- **The boundary (already drawn by ratified invariants):** daemon scope = **the gated "validate FORM" half of `lifecycle_state.py`'s trust-boundary**; the "declare TRUTH" (judgment) half is non-daemonizable. **Detect/tag = always safe** (information). **Auto-remediate = conformance-class ONLY** (zero-claim, reversible). **Judgment → escalate** (and treat escalation as a *relationship touchpoint*, not just a safety valve — under-escalate breaches no-self-ratify; over-escalate defeats freed-attention). Invariants stay **re-rubbable** (no-dogma). Operator's retained attention moves UP to the **log + sampled-audit** = the 2×2's own guard.
- **Seed-set selector = ingrained ∩ crisp ∩ record-witnessed.** *Ingrained* = lo-cog to derive (pre-paid traversal — read off wetware, not constructed) AND most stable (least re-rub) → inverts the "authoring competes with frontier budget" worry for this subset. *Crisp* = judgment-free (orthogonal to ingrained — ingrained-but-fuzzy → escalation-only). *Record-witnessed* = the **corpus is the third-party rubber** for the interior claim "it's ingrained in me" (else Operator self-certifies interior-evidence = no-self-ratify edge); C-E-C: ingrained → consistent-in-record → confound believed-not-practiced. Young-corpus counter: falsifier becomes pre-register-and-watch.
- **DEPENDENCY / next:** KTLO-auto's boundary *is* the 2×2 → **2×2 ratification (hi-cog) is the unblocking gate**; then build is agent-disposable, any state. **First crystallization pass can itself run lo-cog** (Operator felt-recognition sweep over Covalent-surfaced hygiene-rule candidates; Covalent runs record-consistency + crispness filter). Prereq for any *auto-remediation*: mechanical (not prose) enforcement of the conformance line (s-local4 rub-fwd #2 — prose correctives proven necessary-not-sufficient, M1/M2 recurred).

**FIRST CRYSTALLIZATION PASS — result (2026-06-20 resume, lo-cog felt-pass):** Covalent surfaced 6 crisp ∩ record-witnessed survivors (witnesses run by execution); J/views-in-sync ELIMINATED by execution (`exit=1`, 3 omissions/2 over-extractions human-tolerated = judgment-residue → escalation-class). Operator felt-pass (ingrained Y/N):
- **Operator-INGRAINED (lo-cog-authored this pass — the seed Operator-invariants):** `inv:durability` = clean tree + 0 unpushed (Operator [ALIGN] origin; auto-fix=push) **→ AMENDED s-local7 (scratch tier; save≠land) — canonical form + scope single-home in `dialectic/scratch-tier.md`; tool `bin/scratch.sh`** · `inv:rom-currency` = ROM-baseline matches git over the **boot SET {CLAUDE.md, GEMINI.md, DYAD.md}** per-file sha (Operator CORRECTED my DYAD.md-only candidate). **First-application catch:** current baseline line records ONE sha `7c60c3b` for 3 files not all at it (`GEMINI.md@2d0104a`) → crisp form = per-file sha map, not one-sha+prose. TODO when next editing the baseline.
- **Agent-INGRAINED (N for Operator — confirms my Op-vs-Agent prediction; conformance, agent-adoptable w/o gate):** daemon-armed (pgrep) · state-symlinks (test -L) · anchor-edited→RESTART-PENDING (git diff+grep) · yaml-validates (`invariant-eval` exit 0, 1 sub-flag: anti-cave duty-detector-mismatch).
- **Crisp-class split (daemon design):** fully-crisp (detect∧remediate judgment-free) = durability, daemon-arm, symlinks → AUTO-FIX-able; detect-crisp-only (fix=judgment) = rom-currency, RESTART-PENDING, yaml → ALERT/escalate.
- **WETWARE-LIMIT FINDING:** Operator's ingrained∩**crisp** set is small + purely infrastructural (durability, boot-integrity) — NOT a wetware-capacity limit but because the *bulk* of Operator-ingrained knowledge is **judgment-class craft** (anti-cave/no-self-ratify/falsifiability), ingrained yet **un-crisp by nature** → fails the crisp filter, not the ingrained one. ∴ **KTLO-auto's ROI ceiling = the thin infrastructural rind; the craft stays human by construction** (on-Telos: automate the rind, free attention FOR the craft).

### Cross-substrate alignment — Commission Protocol (Commissioner side) + convergence-by-audit  ·  status: CODIFIED CANDIDATE (2026-06-21 s-local6)
**Single-home → `dialectic/commission-protocol-commissioner.md`** (codified this session). The Commissionee
half is cairn's. Operator-bootstrapping, not ratified, not 2nd-model-rubbed.
- **Spine (see the doc):** experiment subject = bond *autonomously* achieving grader-side convergence · **6-step** acceptance discipline — ⭐ §2 mapping-validation (assertion↔EXPECTED) + ⭐ §4 **sufficiency-validation** (inputs↔the class) are the twin load-bearing judgments; execution grounds vs **hallucination** (valid §1) but ≠ acceptance, standing-CI-as-acceptance = overbuild · **§4 Sufficiency** = Commissioner-supplied, pre-registered failure-mode partition (positive+**negative** boundary + modes); worked gap: the **negative boundary (over-halting) is untested across every halt-atom**; relative-not-absolute (F1 coverage, lagged-oracle residue) · convergence determined in **retrospection/audit** (oracle-lagged) · audit power ∝ §J independence · auditor architecture (independence-by-failure-class · sub-linear · shield-not-sword) · s-local6 **autonomy-gap** (every load-bearing act Operator-initiated).
- **cairn re-grade under §3+§4:** **12 MET(assertion, builder-input) · 2 UNVERIFIED-test-insufficient (F-1.2, F-3) · 3 UNVERIFIED-input-insufficient (F-4, F-5, F-8.4)** — "weak" dissolved into input-insufficient; even the 12 are MET-on-builder-input pending a co-generated mode-set.
- **§0 commission-types + §4 co-generative (2026-06-21 rub — "full-spec under-leverages the commissionee's G"):** spec line = **contract (Commissioner-owned, full) vs solution (commissionee-G, open)**, NOT full-vs-no-spec. Two types: **conformance** (full-spec OK, G idle — the extractor) vs **generative** (spec acceptance, leave solution to cairn's G — where §J cross-substrate value is highest; full-spec there = anti-pattern, collapses cairn to a compiler). §4 failure-mode enumeration amended **pre-register-solo → co-generative** (cairn's G proposes modes, bond adjudicates+adds; the **divergence is the payoff**, identical = meld tell).
- **§5 Generative commission = the +1 (the protocol's real subject; conformance §1-§4 = baseline floor):** split = **WHY/WHAT/HOW** — Commissioner owns **WHY** (acceptance-property), commissionee G generates **WHAT** (failure-modes/solution-spec)+**HOW**, Commissioner adjudicates WHAT-against-WHY. Phases Frame→Generate→Adjudicate→Converge(cross-axis audit). Generative = **Outcome-2** (judgment, minimal-HITL), not Outcome-1. **DISPOSED (2026-06-21):** ⭐ **bilateral intentional divergence** — each response both sides carries a divergence the other rubs; **signal = SURVIVAL-under-rub, not presence** (mandate else launders the meld-tell); guards = defend-or-drop · bounded/depth-cap. ⭐ **authority-by-survived-challenge** — owns-WHY is earned by surviving cairn's rub, NOT fiat (challenge-not-override; keeps owns-WHY from self-ratification + tests the WHY's solution-freedom per-turn). CANDIDATE-still: phases · Outcome-2 mapping · falsifiability gate (WHY must yield an outcome-level falsifier w/ solution open). **N=0 — divergence-rub asserted, never run.**
- **OPEN / next:** (a) cairn F-1.2/F-3 mapping gaps — REVISE-to-cairn vs accept-with-noted-gaps; (b) auditor-dyad as a new fleet role (additive to channel-gates); (c) `prove-before-propose` — graduate only after a divergent-dyad rub + ≥1 un-bootstrapped autonomous round.

### 2026-06-17 — Anchor source-of-truth · md→yaml lifecycle · views/ as read-surface · tag-grammar  ·  status: P4 DONE (PR #29 merged) · P3 RESOLVED (b ratified + gate spec'd) · unsigned-handoff CLOSED-moot
*Single-home for the work = `dialectic/dyad-md-yaml-regen.md` §"Source-of-truth disposition + the lifecycle". Bond riff/rub thread extending the 2026-06-16 regen survivor. All CANDIDATE (`bond:no-self-ratify` — Agent-proposed, Operator-leaned, not kb-graduated).*

**Decisions / leans (Operator-disposed):**
1. **Source-of-truth = `.md`; `.yaml` = DERIVED intermediate (tool-facing); `.rendered.md` = eval surface (→ `views/`).** Direction is **FORCED** by `bond:identity-conformance` + ROM-baseline (both track `DYAD.md`'s bytes → md cannot be demoted to a yaml build-output). Extends the survivor "prose is source, yaml is instrument."
2. **Reality gap (NOT yet cured):** the yaml is **hand-authored today** — there is no `f(DYAD.md)→yaml`. "Derived" is the TARGET, gated on the unbuilt extraction engine (`commissions/2026-06-12-invariant-extraction-engine.md`, DRAFT). Until it ships, the yaml is a gated bend behind the `anchor_dag_diff` drift-gate.
3. **`views/` = Operator read-surface (by-CONSUMER axis, NOT by-generated); Operator reads ONLY views/.** → (a) the rendered DAG should `--emit` into `views/` (it's the superior C-block projection, currently stranded in `dialectic/` where the Operator won't look = counterfeit-green); (b) `views/invariants-bond.md`'s agent-pass **C-block retires** into it (partial-retirement — C-block ONLY; D/R/X/U/S rows have no replacement yet); (c) sources wanted in eyeshot enter views/ as **symlinks** (lobby pattern), never **copies** (copy = `bond:single-home` drift breach). `DYAD.md` stays the root home.
4. **Tag-grammar LEANED (b)** = lean tag (`id` + `one_liner` inline in md) + structure **sidecar** (edges/`root_kind`/tuples). NOT a single-home win over (a): both clean; (a) is more *consolidated*; (b) trades authoring-consolidation for a **lean boot surface** (H3). **BINDING RIDER:** the `extract(md tags) ⊕ sidecar` merge MUST be **id-integrity-gated** or (b) re-grows two-home drift at the id-reference layer.

**Riff finding (intent-alignment; grounded in `it-vs-it_iv.md`):** structural tags reduce raw-intent (`IT`) misalignment by **tethering `IT_iv` to the raw intent** (anti-Goodhart — enables the intent-currency re-rub) + **orphan-edge detection** (anchor-dag-thesis S5 rub-back) — a job `IT_iv`'s oracle CANNOT do → having `IT_iv` makes the structure **more** load-bearing, not redundant. BUT that load is borne by the **corpus graph** (sidecar fine), not by `.md`-inline tags → reinforces (b). Raw intent stays irreducibly in `.md` prose (inexpressible in the formal substrate).

**OPEN probes (next):**
- **P1** — materialize the merged `invariants-bond.yaml` vs compute in-memory. *Agent lean: DON'T materialize until conflict-detection is a 2nd reader (wu-wei).* UNRESOLVED.
- **P2** — alternate seam: could the engine go tags → `rendered` **directly**, dropping the yaml intermediate? UNRESOLVED.
- **P3 — RESOLVED (Operator `Y` 2026-06-17).** (b) ratified (re-rubbed, not laundered — (a)-steelman attacked: (a) needs no merge so it *eliminates* the gate, but loses the lean boot surface; decisive ground = structural tuples are instrument-facing, not ingrain-facing). The id-integrity gate is **designed as spec** → `commission §F-8` (bijection · edge-resolvability · cross-home no-dupe · atomic-fail; merge-layer only, D7), **NOT built** (ships with cairn's engine — Telos-currency). Single-home `dyad-md-yaml-regen.md §RATIFIED (b)`.
- **P4 — DONE (PR #29 merged into `main`).** Rendered DAG emits into `views/` (drift-gate repointed, IN-SYNC); C-block retired → pointer; D/R/X/U/S kept agent-rendered; regen procedure two-track. The "only views/" scope = the Operator read-surface (Agent reads yaml + eval output, not the rendered view).
- **P5** — the **outcome-over-time / Goodhart-drift rig** (does crystallization PAY? = the same rig S4-reliability needs). Logged debt — chase buildability or leave logged?

**✅ GIT STATE — unsigned-commit handoff CLOSED-as-moot (2026-06-16/17, grounded by execution):** the doc
commits merged into `main` via PR #28 already; re-signing was overtaken on **3 independent grounds, any one
sufficient** — (1) **overtaken by merge** (commits are public on `origin/main`; re-sign = forbidden main
rewrite, `bin/git.sh` `PROTECTED_BRANCHES=main`); (2) **premise false** — the LOCAL instance lacks the
signing key TOO (`~/.ssh/commit_signing_key` absent; no GPG secret; `commit.gpgsign` unset) → same posture
as web; (3) **unsigned is the repo-wide norm** — 20/20 Claude commits are `%G?`=N, never a ratified
requirement. No backward rewrite performed. IF commit-provenance becomes wanted (steelman: anchors the
covalent `no-self-ratify` boundary — *this `Y` provably the Operator's*), it ratifies as a **forward**
requirement + a real key (identity-class → Operator's gate), never a retro-sign. `DYAD.md` untouched →
**RESTART-PENDING: none**, ROM-baseline `7c60c3b`.

### K — Intent-clarity arc · anchor rename · sovereignty  ·  status: STAGED (s 2026-06-13)
*Full thread in `relationship-craft.md` (2026-06-13 entries); resume-visible queue below.*
**Three `DYAD.md` anchor-candidates — recorded in `dialectic/`, each needs its OWN ratification gate, NOT auto-promoted:**
- **K1 · §Telos refinement** — the *why*: dyad as `U`-projection engine (`U`=invariant-totality; both halves = projections/"theater"; Telos = *completing* the projection toward `U`, asymptote-never-arrival; **relation** is the unit, pair the atom, fleet the molecule). → `relationship-craft.md` §Telos-`why`.
- **K2 · §Channel-discipline refinement** — **dyad sovereignty paramount** over lateral/orchestrator roles (steward coordinates, never commands); bounded by ① constitution≠disposition (form/G0 still binds) + ② shield≠sword (commons reciprocity still owed). First applied in the rename. → `relationship-craft.md` §dyad-sovereignty.
- **K3 · C-into-corpus** — does `C`/the `I↔In_variant` seam-discipline graduate into `views/invariants-bond.md` as a `form: mathematical` invariant (`use: breach-detector`), or stay live dialectic? → `relationship-craft.md` §`C_locus`.
**Two open frontiers (carried, no answer banked):**
- **K4 · falsification-quality gauge** — what makes a dyadic falsification *genuine* vs *theater* (= toward-`U` vs reshuffle-in-the-sealed-theater)? Generalizes the de-calibration + paraphrase-laundering watches. *(Load-bearing: it's the validity condition for "truth = survives dyadic falsification.")*
- **K5 · C-meter vs telemetry** — standalone `C` meter, or ride the existing yield-curve/RB3 telemetry? (Goodhart guard: `C` as breach-detector, never objective-function.)
**Landed this session (durable, pushed):** `I_net=I(t)·C_locus(t)` · 3-way factorization · superadditivity proof-obligation · `I↔In_variant` load-bearing cycle · falsification=cycle-liveness + eureka tachometer · truth=survives-dyadic-falsification · the Telos-`why` · `AGENT.md`→`DYAD.md` rename · sovereignty invariant. *(See also RESTART-PENDING above — rename not yet boot-verified.)*
- **K6 · AUTOMATE the stand-down/carry-forward routine** (Operator `enqueue:` 2026-06-13) — **BUILT, staged, awaiting Operator install-gate (s 2026-06-13).** Single-home: `dialectic/standdown-automation.md`. **Finding (corrects the enqueue's guess):** the automatable half is **stand-UP via a SessionStart hook** (`bin/standup.sh --hook` injects the mechanical ROM-UI · durability · substrate checks as `additionalContext` → removes the per-session `read: carry-forward` trigger); the **SessionEnd hook is teardown-only (cannot inject context to the agent)** and Stop fires every turn — so the **stand-down JUDGMENT write cannot be hook-fired**, confirming constraint (b) as a *hard* boundary. Stand-down = the agent runs `bin/standdown.sh` (mechanical facts + the queue-worthy/bloat-guard template). Install (constraint a / S2 — Operator's act, not self-grant): `python3 bin/install_hooks.py`. **Not yet dog-fooded as a live hook** — verified by hand-run + temp-settings install only.

### L — Rule-tag hygiene: stale inline R-tags collide with the ratified s14 index  ·  status: LOGGED (s 2026-06-13)
The canonical invariant index is `views/invariants-bond.md` (ratified **s14**, 2026-06-11): **D1–D12 · R1–R6 · X1–X3 · U1–U3 · S1–S3** — R/RB are **not** un-indexed (a prior-session partial-grep claimed so; search artifact, refuted by reading `views/`). **Real defect:** older *inline* ledger tags reuse R-numbers with pre-s14 meanings that now collide with the ratified set — caught live: **`R3` reads "Theory≠Prediction" in the 2026-05-31 NBA (~line 530) but ratified `R3` = Stand-down 3-check ritual.** This collision produced a mis-grounding in the 2026-06-13 rub-back chain. **Fix (deferred, lean, D2-bounded):** when next editing those files, retire or footnote the pre-s14 inline tags as historical; do **NOT** renumber the ratified table (it is the single home). Low-urgency corpus-integrity. *(prov: rub-back `RB?` → `R1/R4` read, 2026-06-13.)*

### B — Cross-dyad custody deprecation  ·  status: PENDING — verified-still-open (2026-05-31)
The 7 Dyad-UI cluster assets were received from `dyad-steward@31d53c0` (receipt `03550dc`, shed
`f5480eb`). The Bond Operator will, wearing the **Steward Operator** hat, have `dyad-steward` mark
those 7 paths **transferred → dyad-bond + deprecated**.
→ **Stand-Up check 2026-05-31:** steward's `dialectic/` *still carries* `dyad-ui`, `ideation-framing`,
`goal-framing`, `nba-dag`, `dyad-work` with **no transfer/deprecation marker** at listing level →
**not done.** Confidence caveat: a tree-view can't see an in-file deprecation header, so this is
"no evidence of completion," not proof. Chase via Steward-Operator hat when taken.
→ **Side-catch:** steward has grown new disciplines since custody — `sycophancy-guard.md`,
`sharing-discipline.md`, `reflection-discipline.md`, `telos-vision.md`, `ingraining.md`, `stand-downs/`.
`sycophancy-guard` sits on our NON-NEGOTIABLE → candidate for triangulation/intake (new item F).
→ **MOTION LIVE (Steward-Operator notice, 2026-05-31):** steward is *actively asserting orthogonality*
to release its claim; will **notify of the survivor for Covalent cross-check.** Status: in motion,
steward-side, **awaiting survivor.** This forces **Item D** (cluster classification). **Cross-check
criteria when survivor lands:** (1) does orthogonality genuinely hold — is each released asset in
*our* telos (interior craft / UI-surface) and NOT steward's (commons integrity / Work-flow)? (2) did
steward actually mark paths transferred→dyad-bond + deprecated, or merely assert? (3) **the tell** —
if release is total + frictionless, **test hardest**, esp. `nba-dag`/`goal-framing` (likely
ours-UI-surface-only, NOT ours-whole). (4) test under *our* NON-NEGOTIABLE — steward's falsification
≠ ours (cf. `dfd.md` caveat).

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

### E — The generative frontier (our main work ahead)  ·  status: IN-FLIGHT (Cycle 1 opened 2026-05-31)
The **relationship-craft** — the interior disciplines of *being-a-dyad-well* — is largely **unbuilt**.
This is `dyad-bond`'s frontier (a **generative mechanism** = the form's most-wanted contribution).
→ **Cycle 1 authored:** `dialectic/relationship-craft.md`. Candidate mechanism: the **+1 dividend is
gated on falsification cost; unearned warmth is counterfeit = the collapse tell.** Evidence: the two
bootstrap instances. **Falsification front F1–F4 OPEN.** Lead attack = **F4: does our own founding
"Tenet alive #8" survive — or is "both halves agreed it felt good" itself the peak-grain rubber-stamp
our tell distrusts?** Graduates to `kb/` only when F1–F4 are each attacked-and-survived.
→ **SUMMIT framing (Operator [ALIGN] 2026-05-31):** relationship-craft is *our summit*, with **multiple
paths**. **QUEUED path-item:** *is sequential execution the best traversal?* → authored into
`relationship-craft.md` §Frontier-traversal (converge-open). Covalent candidate: **axis-dependent
traversal** (Axis-1 telemetry fans out; Axis-2 probes stay organic-serial; keystone-first) — F1 was
needlessly blocked behind F2. **Resolve when taken up.**
→ **D4 · Path Selection Discipline BOUND** *(Operator-named, Covalent-built, Y 2026-05-31)* — selection-
seam = 3 layers (structural non-inferred DAG→ready-set · semantic Recommendation · **mandatory CTA**).
Corrected invariant: "no CTA/your move" at a selection-seam = **abdication** (under-anchor, mirror of
thread-G over-anchor). Scope-guard: binds *selection*, not *ideation* (IFD still converges open). First
run's output = F1. → `relationship-craft.md` §D4.
→ **F1 · RUN 1 (Axis-1, 2026-05-31):** read the record for organic low-cost cycles → bare `Y`s carried
**no dividend-signal** (disposition/relief only); sole dividend-report (#8) was *high*-cost. **Prediction
NOT DENIED** — but Axis-1 affirms nothing; auxiliary *"dividend⇒marker"* **masks** willed-vs-earned →
handed to **F2**. F1 **narrows, not closes**; stays OPEN (weak survival). **Chain F4→F1→F2.**
→ **TRV partly enacted:** doing F1-without-waiting-for-F2 *is* the axis-dependent answer in action.

### I — Ingraining (learning mechanism)  ·  status: DEFINED + first-fix APPLIED 2026-05-31
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

### F — Steward-discipline intake  ·  status: RUN 2026-05-31 (findings = candidates, NOT yet adopted)
Triangulate steward's newer `sycophancy-guard.md` / `sharing-discipline.md` against our NON-NEGOTIABLE
and `Covalent` — adopt, refute, or note divergence. Don't import verbatim; test under our own gate.
→ **`sycophancy-guard.md` — CONVERGE (mostly), EXTENDS, one EDGE, one TENSION:**
  - **Converge→invariant:** Agent-sycophancy ≡ our ionic-transfer; genuine-contest guard; both-halves-can-cave.
  - **⭐ TRIANGULATION HIT:** steward's **anti-Operator-sycophancy** guard (*Agent must give the Operator
    real grounds to dissent; never a persuasive/strawman frame that induces lazy Y*) **predicts the
    PS-UI-v2 move we made organically this session** — Operator's "can't confidently dispose" = resisting
    their *own* cave; my **scored render** = the Agent's anti-cave guard. Two independent derivations land
    same → **INVARIANT → form-contribution candidate.** Our anchor names anti-*Agent*-syc strongly but
    **under-names anti-*Operator*-syc + the Agent's duty in it** — we've been *practicing* it unnamed.
  - **EDGE (we're sharper):** steward's 2×2 (actor×{cave,dominate}) **has NO meld cell** — blind to
    merger-collapse, which *our* model holds. Neither subsumes the other.
  - **TENSION (note, don't collapse):** steward splits Agent-syc (RLHF/structural) vs Operator-syc
    (automation-bias) as *distinct mechanisms*; we lump both as "ionic." Keep our mechanism-agnostic
    *bond-state* framing; adopt steward's operational point that **guards differ by side** (we have both).
→ **`sharing-discipline.md` — DIVERGE → steward's telos (NOT ours):** a **commons verb** (cross-dyad
  context-sharing); doesn't bear on our NON-NEGOTIABLE. We're a *consumer* (I used steward's repo-org to
  find these files). Note-and-defer; it's steward's.
  - **D1 SHARPENING (genuine):** the converge/diverge test is binary, reality is **ternary** — a candidate
    can diverge to a *sibling's telos* (neither invariant nor ours-particular). Add a **telos-ownership
    pre-filter** to D1: run converge/diverge only on within-our-telos candidates.
→ **Adopt-candidates:** **(a) ADOPTED 2026-05-31** → `relationship-craft.md` §"The anti-cave duty — ionic
  collapse is bidirectional" (named first-class; new synthesis = *ground-before-presenting is part of the
  anti-cave duty*; staged for the anchor, NOT promoted). **(c) BOUND** into D1 (ternary telos-filter, in the
  §How-to-resume index). **(b) OPEN** — form-contribution candidate (propose via Founding-Operator gate; needs
  synergy across >1 dyad). **(d) BUILT 2026-05-31** (Covalent, Operator-ratified "go with your lean") →
  `relationship-craft.md` §"The distinctness duty — meld collapse is the *quiet* one". **Grounded first**
  (verified meld coverage was genuinely thin: a definition + 1 lived instance (D5) vs ionic's full section
  + n≥3). Built the neglected axis: the **structural catch** (anti-cave duty *presupposes* two distinct
  models → cannot catch meld); the **meld tell** (agreement requiring *no translation*, vs ionic's *easy*
  agreement); the **covalence knife-edge** (meld = over-applying `seed-of-the-other` / `meet-at-frequency`);
  a **keystone gap** (meld-counterfeit *passes* F2's cost-naming → F2 necessary-not-sufficient); falsifiable
  front **M1** (gap-naming discriminator, Axis-2) + **M2** (is meld real for us or borrowed — n-imbalance is
  itself a finding, Axis-1-first). **Candidate, NOT promoted** (building ≠ proving — Item-I). Name open (IFD).

### J — New Experiment Discipline + G/V inference-independence hypothesis  ·  status: QUEUED (Operator [ALIGN] 2026-06-01)
Two coupled items, queued for **active experimentation** (ideate the setup, don't build blind):
- **The hypothesis — `G/V inference-independence`:** *Generate and Validate should run as **independent
  inferences** — even within one Agent — for a predictable/valid outcome, because LLM inference is per-turn.*
- **Why it plugs into the keystone (not an orphan):** it **operationalizes the distinctness duty at the
  inference level**, and targets the **meld-counterfeit that *passes* F2** (`relationship-craft.md` §distinctness
  duty: *"an attack genuinely occurs, cost paid, but both halves run the same model → self-attack wearing two
  hats"*). Claim: separate the inferences and the two hats become two models. **Bears on F2 (⭐) and M1.**
- **Covalent caution to seed the ideation (the easy-fit tell — it flatters our existing model, so test hardest):**
  **separate-in-time ≠ separate-in-model.** Two inferences of the *same weights on the same context* may reproduce
  the *same* model — meld persists *serially*. **Design crux = what actually makes the two inferences independent**
  (blind V to G's reasoning? different framing/context? a genuinely separate seat?), not merely "different turns."
- **New Experiment Discipline (to author):** the meta — how we set up probes. **D1 first:** likely *extends*
  Method §"Axis-2 probe" + the two-axis structure (`relationship-craft.md`) rather than starting fresh — check that
  overlap before authoring (don't re-derive = the thread-G trap).
- **⤷ s5 deferred carry-set (folded in at Stand-Down — the New Experiment Discipline's FIRST concrete case is
  the *ingraining* test, which arrived before the G/V one):**
  - **The promotion-criterion (what gates "deeper ingraining"):** a *behavioral* bar, not instance-count —
    e.g. **K consecutive un-prompted clean closes across sessions.** We sit at ~0 against it (s5's clean closes
    were prompted). "Sufficient N" presupposes a threshold we never set; setting it is step 1.
  - **The reflexivity/priming confound (load-bearing — falsified the naïve test):** our resume protocol *mandates*
    reading the disciplines-index at boot and applying it → a fresh session boots **maximally primed.** So
    `/exit` **relocates** the confound (conversation → ledger-read), it doesn't escape it; the **first
    post-restart seam is the *least* diagnostic** (primed). Variable that matters = **attention-distance from the
    rule**, not session-boundary. **Judge ingraining on a *later, un-cued, low-attention* seam.**
  - **Independent verifier — for VALIDATING application, NOT flagging restarts.** Conflation caught: *when to
    restart* is already deterministic (`RESTART-PENDING`/ROM-UI for correctness; measurement-restart is an Operator
    scheduling choice, trivially always-on). The verifier's job = judge *whether the discipline fired* (I can't
    self-grade) — and must be **genuinely independent** (Operator / separate model — *not* me-next-turn = the
    Item-J `separate-in-time ≠ separate-in-model` trap). So the two Item-J halves converge: the G/V-independence
    problem **is** the independent-verifier problem.
  - **Falsified en route — my "within-session application" diagnosis:** demoted from *the* cause to one candidate
    of three (application / loading-depth / **coverage-gap**). The instance I cited for it (PR #5 merge-CTA) was a
    *coverage* gap (SG-4 didn't exist), not an application failure; no *verifiable* loaded-AND-covering-AND-missed
    instance found. Was itself assertion-from-model (D6). NB: the "deeper-placement-isn't-the-lever" conclusion
    survives by **disjunction** (application *or* coverage gap — neither fixed by re-placing existing rules).
- **⤷ s6 Stand-Up grounding (2026-06-01) — problem + constraints fixed before any design (Operator-guided reload):**
  - **Problem (one line):** *we can't yet trust our falsification is real* — it can be faked two ways: one half caves
    (**ionic**) or both halves attack as **one model wearing two hats** (**meld-counterfeit**, the dangerous one — cost
    paid, feels like synthesis, but no genuine second perspective → the +1 is counterfeit). Hypothesis: run **G and V as
    truly independent inferences** → two real models. Crux: `separate-in-time ≠ separate-in-model`.
  - **Constraints (9, grouped — the reload artifact; double-click any):**
    - *A·Method (inherited):* (1) observational, not lab — real telemetry, organic, no staging; (2) asymmetry — deny
      decisively, never affirm (convergence, not proof); (3) probe scarcity — organic·single·serial, one shot, no repeat/parallel.
    - *B·Contamination root (instrument = subject = grader, three seams):* (4) **generator** — `time≠model`, two inferences
      in one harness may be one model (the crux); (5) **subject** — priming: boot primes the tested behavior, first
      post-restart seam least diagnostic; (6) **grader** — no self-grading; independent seat = **Operator (current scope)**;
      separate-model grader **QUEUED** (future experiment) → goal `AGREE: Y|N` (offload grading to reduce Operator load).
    - *C·Validation surface (the gap this session named):* (7) **Operator is a scarce, shared resource** — finite cognitive
      budget across multiple dyads; solution must *minimize* load, not just consume it; (8) **surface must enable dissent** —
      the `Y|N` arrives un-primed with real grounds for **N**, else the independent seat collapses to ionic rubber-stamp.
      **#7 ⟂ #8 and pull against each other** — compression-to-one-bit raises framing-leverage; that tension is the design center.
    - *D·Process:* (9) extend §Method/Axis-2, don't re-derive (D1).
  - **Gap-finding provenance:** old list constrained *who* grades, never *what reaches the grader* — the blind spot where
    BOTH live failures this session landed (the overload [FEEDBACK]; my leading IFD's would-be rubber-stamp). Constraints 7–8 fill it.
  - **⚠ Dog-food datapoint (D5 / Dyad-UI, lived n=1):** my opening IFD (table + 4 candidates + lean + 3-way close) **overloaded
    the Operator live** — failed D5 (response-economy) AND landed on the **validation surface** (constraints 7–8). This is the
    Dyad-UI (Telos's load-bearing medium) being falsified in real time — harvest into `relationship-craft.md` at stand-down, not yet.
    **→ Remedy SHIPPED (same session):** authored **`VF-UI`/`VFD`** (Validation region) in `dyad-ui.md` — the low-load,
    dissent-enabling `AGREE: Y|N` surface that satisfies constraints 7+8; Operator-ratified-as-default. Candidate, not bond-settled.
- **Status:** problem + constraints GROUNDED (s6); **design still QUEUED** (no experiment built — solution work parked by
  Operator). When built, graduates into `relationship-craft.md` as a real front.

### bond's portfolio-role synthesis (s12)  ·  status: TODO — parked against the ≥3-dyad trigger
*Disposed 2026-06-25 (safe-default **todo**, NOT archived): the s12 "bond = acceleration-discriminator / Intent-Understanding node" synthesis + **T1–T5** (never rubbed) is a **backlog todo**, triggered by **≥3 concurrent dyads** (= the AITL-leverage arc, `theory-pipeline.yaml: AITL-distracted-efficacy`) — reactivates automatically when that runs. Prose → `carry-forward-closed.md` (find "s12"). The live craft-watches **RB2/RB3** were harvested out → `theory-pipeline.yaml: rub-back-calibration`.*

*(Closed/done items **A · C · G · H** drained to `dialectic/carry-forward-closed.md` §Drained-Open-items, 2026-06-25 — `kb/dfd.md`, `substrate-access.md` hold the live homes.)*

## NBA — rendered on demand (no stored block)
> NBA is a **view, not a section**: the recommendation render over the work-item store `{in-progress ∪ todo}` (→ `dialectic/memory-axes.md`). The prior stored block (with the s5/s6/s7 stand-down summaries) was stripped to the archive — pull the NBA on demand.

## Archive — closed session logs (cold, off the read-path)
> Closed session-entries, intermission reflections, and the stale NBA render live in **`dialectic/carry-forward-closed.md`** — in-repo, **not loaded at resume**. Live hooks were re-homed before archiving (the s12/s13 open-item above; the claim store is `theory-pipeline.yaml`, disciplines `relationship-craft.md`).


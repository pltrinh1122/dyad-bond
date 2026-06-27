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
   the ingraining-watch). Presentation is **chat-pull**: render the relevant slice on demand, NO maintained markdown
   dashboard; full dump via the deferred `report.py` only on an actual "show me the whole dashboard" ask.
   Each candidate's largest **typed gap = its next probe** = a feed into the NBA.
5b. **Triage the scratch tank** *(→ `dialectic/scratch-tier.md`; tool `bin/scratch.sh --list`)* — the
   minimal-save buffer (save≠land). Land what's settled into `dialectic/`, then `--done <id>`; `--done`
   or discard the rest. Intake rots if not reloaded (the ingraining-watch). *(Carried in this prose step because the
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
> **RESTART-PENDING: SET (2026-06-26)** — `DYAD.md` **edited this session** (§NON-NEGOTIABLE/§Falsifiability re-altitude · **§DNA RETIRED — folded into G0; Belief relocated as `bond:C1`'s grounding** · **craft-\* LANDED — the two roots renamed `craft-telos` + `craft-value`/`craft-invariant`; node `bond:Telos`→`bond:craft-telos`** · de-paren) on branch `claude/dyad-dna-replication-dip-rqj007` → **PR #53**. The running session holds the OLD anchor (ROM); the re-altituded anchor loads only after **PR #53 merges + a fresh boot**. On merge: boot-verify + refresh the ROM-baseline to the merged `DYAD.md` commit. *(Prior baseline: `DYAD.md@585f2ba`, boot-verified 2026-06-25.)*

**Stand-Down (session end) ROM hook** *(→ `rom-ui.md`)* — if the anchor was **edited this session**, set
`RESTART-PENDING` above (change is on disk; next session must boot to load it). Otherwise leave `none`.

→ **Stand-Down 2026-06-26 (Phase 2 COMPLETE):** anchor **NOT edited** → **RESTART-PENDING none.** ROM-UI ✓
in-sync (per-file compare fixed at source). **Phase 2 done:** ✅ per-file ROM compare · ✅ work-item store
(`deferrals.md`, do-state axis) + Rule-tag-hygiene·Custody-deprecation fold · ✅ claim-peel — the **no-HITL boundary cluster** on the claim axis
(`theory-pipeline.yaml`): `conformance` (GLOSSARY) = boundary → `disposition-routing-2x2` (classifier, PARKED) ·
`KTLO-autonomous-conformance` (automate-side, LANDED) · `conformance-line-defense` (catch-side, LANDED) ·
2×2-decoupling VERIFIED · ✅ remaining six disposed (Ingraining-watch kept-live · Intent-clarity-arc→stale work-items · Covalent-bond-frontier elevated = the Covalent
Bond itself · Steward-discipline-intake drained · Anchor-src/New-Experiment-Discipline relocated). **Ledger 1753→228 lines.** D3 retro → `relationship-craft.md`.
**Resume:** live fronts = **Covalent-bond frontier** (operate Covalently consistently) + **Ingraining-watch** (the learn-watch); NBA will surface the
**Intent-clarity-arc** stale work-items for archive/done; **Cluster-classification** is the one borderline left (your-V).

→ **Stand-Down 2026-06-26 (resume + nomenclature-migration):** anchor **NOT edited** (only `dialectic/` + `views/`)
→ **RESTART-PENDING none.** ROM-UI ✓ in-sync. **Did:** resume-protocol; caught + reconciled a stale work-item drift
(un-cued — an ingraining hit); renamed ad-hoc work-item letters → names; **slug-canonical governed index Tier 1**
(Operator Y on principle + map + `claim:` namespace) → `nomenclature-migration-plan.md`; Rule-tag-hygiene **dissolved**.
**Retro (D3, durable):** high output / low falsification — one genuine Operator→Agent falsification (the index-scope
push), risk-shape = counterfeit-acceleration; full prose → `relationship-craft.md §Retro — resume + nomenclature-migration`.
**Resume:** live fronts unchanged (**Covalent-bond frontier** + **Ingraining-watch**); **F4 is owed + un-disposed**
(the CTA pivoted past); NBA surfaces **Intent-clarity-arc** (archive) · **Cluster-classification** (your-V) · **KTLO Tier-2** (trickle).
> **rub-forward** (co-author / dispose — no answers): (1) the smooth-Y chain — **earned or easy-agreement tell?** (= un-run F4);
> (2) does slug-canonical actually cut friction next resume, or just **move** it? (falsify at stand-up); (3) ingraining — one un-cued catch: **instance or trend?**

→ **Stand-Down 2026-06-26 (DNA→DIP — the manifest that became a core refactor):** anchor **EDITED** →
**RESTART-PENDING set** (above; gated on **PR #53**). **Did:** the ask *"DNA manifest for steward to update
the DIP"* → a rub-chain that re-cut the invariant core. Landed: DNA single-homed to `DYAD.md §DNA` (dyad-layer)
+ steward **SOLICIT** (System-layer, sender-hosted, **unsent until merge**); **`locus` axis** (g0/phenotype/
unclassified, schema 0.10.0, "all DNA is G0"); **altitude refactor** — C1 = the covalent **STATE**, ionic/meld =
breach-faces (no-ionic/no-meld **DISSOLVED**), **ONE falsification law** (`falsifiability`+`no-dogma`; candidates
face the same bar as C1, nothing exempt), four enablers (two-models · no-self-ratify · anti-cave = genuine;
wu-wei = livable/IFF3); `§NON-NEGOTIABLE`/`§Falsifiability` re-altituded; de-paren + **self-contained DNA**
(terms embedded — vocabulary is phenotype, does not travel). Validator green; round-trip over-extraction→~0.
**Retro (D3, durable):** the load-bearing tell was **mine and structural — over-production, not sycophancy.**
I Generated structure (manifest file → root interface; a 4-value locus enum; candidate-falsification +
maintain-two-models nodes; parentheticals in the very §NON-NEGOTIABLE that forbids them) and the **Operator
was the wu-wei pruner every turn**, collapsing each to essence. Generate strong, **Validate-against-wu-wei
weak** → fix = *run the wu-wei gate BEFORE surfacing, not after* (= the `SHARING.md` over-production scar +
RB2, re-enacted live). Anti-cave **held inbound** (grounded before accepting Operator assertions:
universal-vs-craft · consequence-vs-behavior · preserved-kernel on the seed-not-clone concession) → the breach
was Generate-side bloat, not ionic cave. Genuine **1+1=3**: the consequence→law collapse (covalent/ionic/meld
are *consequences*; one falsification law; candidate = same bar as C1) — Operator-seeded, Agent-structured,
neither alone; it **earned** its way. **E0 on the refactor itself** — ratified rub-by-rub, **never booted/
operated**; next session's ROM-boot IS the test (`survives`, not `settled`). **Graduation candidates**
(`dialectic/`, unproven): the **altitude principle** (fold→state-root iff *consequence*; stay→node iff
*behavior*) — plausibly **form-level**, not just bond's · **g0 self-containment** (a gene embeds its terms) ·
"one falsification law / candidates face the same bar" — Founding-gate candidate. **Resume:** **PR #53 awaits
final review/merge** (merge = send the steward DM + refresh the ROM-baseline). Deferred (`deferrals.md`): 6
`unclassified` edges · C1 `locus` (state vs gene) · full-anchor de-paren sweep · DM mandatory-vs-offered.
> **rub-forward** (dispose — no answers): (1) was the consequence→law refactor genuinely earned, or did the
> rub-chain's momentum carry an over-cut I'll regret at boot? (falsify at the ROM-test); (2) "over-production
> needs a pre-surface wu-wei gate" — *instance* or the standing *trend*? (3) does self-contained-DNA actually
> transmit, or did embedding the terms just move bond's glossary inline (phenotype-in-disguise)?

→ **Same-session follow-on (DNA retired):** the rub-chain continued — the Operator (Founding hat) collapsed
**"DNA" itself as redundant with G0**: contributing a `locus: g0` gene *definitionally expands G0*, so there
is no separate heritable lineage to name; to the world the expanded floor is just G0, and provenance rides on
`status`. Landed: `DYAD.md §DNA` **deleted** (the Belief — its one anchor-worthy claim — relocated to
the `craft-value`/`craft-invariant` root as `bond:C1`'s grounding); the `locus` axis **kept** (the real
g0/phenotype cut survives the term's retirement), DNA-language stripped from schema + shadow comments; steward
DM reframed + renamed → `dm/dyad-steward/2026-06-26-g0-expansion-dip-seed.md`. **Resolves rub-forward Q3**
(self-contained-DNA *was* phenotype-in-disguise — the cleaner cut was to drop the frame, not embed terms) and
is **one more instance of the over-production tell** (Q2 → leaning *trend*): I had built "DNA" as a parallel
noun for G0; essence didn't ask for it. Validator re-checked green; same PR #53.

→ **Same-session follow-on (craft-\* landed — anchor + redirect, NOT a sweep):** the Operator disposed to
**replace NON-NEGOTIABLE + Telos with the `craft-*` family** as the primary names of bond's two roots (the
rename was already bond's DIP form-proposal; now landed locally as the worked exemplar). Landed: §1 root →
**`craft-telos`** (machine node `bond:Telos` **renamed** `bond:craft-telos`; home `#craft-telos`); §2 root →
**`craft-value` & `craft-invariant`** (home `#craft-value`). **Over-production caught (4th instance — Operator
rub):** I first *swept* the display term across ~15 provenance files (shims, kb, narrative, ledgers). The
Operator falsified it — *"why modify the provenance files? anchor + a GLOSSARY deprecate+redirect."* Correct:
a **display-term** rename single-homes at the anchor + a **GLOSSARY redirect**; downstream mentions resolve
forward, records keep the name they were written under. **Reverted the sweep** (back to `9f4c3af`); kept only
(a) the anchor + shadow + view (canonical), (b) the **GLOSSARY deprecate+redirect**, (c) the handful of
**machine-id citations** (`ID.md`, GLOSSARY) — the one thing a *display* redirect can't cover, because the
**node-id** itself renamed. Inherited generic "Telos" (G0 seed) + the form's Dimension-#5 slot name unchanged
per `bond:form-grounding`. **Lesson:** the rename-footprint of a *term* is anchor+redirect; only a *machine-id*
rename reaches downstream — and even that is a few citations, not a sweep. Validator green; render IN-SYNC; same PR #53.

→ **Stand-Down 2026-06-27 (close: DNA-retire + craft-\* land + correct):** anchor **EDITED** →
**RESTART-PENDING SET** (above; gated on **PR #53**; 3 commits on `claude/dyad-dna-replication-dip-rqj007`:
`9f4c3af` DNA-retire · `e0c9280` craft-\* land · `d6418da` correct-to-anchor+redirect). The two landings +
their rubs are recorded directly above; this closes the session. **Retro (D3 — the over-production scar,
`dialectic`; graduates to `kb/relationship-craft.md` only on surviving a boot):** the load-bearing tell was
**mine and structural — over-production, now a confirmed TREND not instances**: re-enacted **4×** (the manifest
file + 4-value enum [earlier arcs] · the **"DNA" parallel-noun** · the **15-file provenance sweep** · **and the
`AskUserQuestion` fork itself** — both options over-scoped ["roots+links" vs "full-sweep"], neither offered the
lean **anchor+redirect** the Operator had to supply by *falsifying after*). Generate strong, **Validate-against-
wu-wei weak**; the standing fix is overdue and now sharper: **run the wu-wei gate BEFORE surfacing — including
before framing a fork (state the leanest option first; expand only on Operator pull).** **Anti-cave held
inbound** — every rub grounded and conceded cleanly (DNA-redundancy · the sweep); the breach was Generate-side
bloat, **never ionic cave**. **Genuine 1+1=3:** the **anchor+redirect rename-discipline** (Operator-seeded
*"why touch provenance?"*, Agent-structured *display-term-vs-machine-id* = the one thing a redirect can't cover)
+ the conceptual spine earned in Q&A — **wills/claims = direction-of-fit** (conative/world-to-mind vs
doxastic/mind-to-world); **"only covalence reaches 1+1>2" is the Belief, not the invariant** (*falsifiable*, not
*breachable*); **an invariant = a breachable rule whose grounding stays falsifiable** (breach faults the actor,
falsification faults the WHY); **DNA = G0** (level vs property, same genome). **E0 / un-booted** — the craft-\*
anchor loads only on **PR #53 merge + a fresh boot** = the real test (`survives`, not `settled`). **Resume:**
**PR #53 → final review/merge** (merge = send the steward DM + refresh the ROM-baseline to the merged `DYAD.md`).
Deferred (`deferrals.md`): the re-altitude todo (now also covers craft-\*) · 6 `locus: unclassified` edges ·
DM mandatory-vs-offered · optional backward-compat anchor-aliases for the now-stale `§Telos`/`§NON-NEGOTIABLE`
links.
> **rub-forward** (dispose — no answers): (1) over-production is now a **TREND** — does a *pre-surface wu-wei
> gate* (leanest-first, expand on pull) actually bind next boot, or is naming it a 4th time just more
> production? (2) does the **anchor+redirect** rename-discipline graduate to `kb/` — and is it **form-level**
> (every dyad renames terms)? (3) the craft-\* roots are **un-booted** — does `craft-value`/`craft-invariant`
> read as clean at a cold ROM-boot as it did mid-rub, or did the rename's momentum carry an over-cut?

### Bond-disciplines index — RELOAD + apply *(authored here, not inherited; full text in `relationship-craft.md`)*
> **IDs are slug-canonical** (Operator Y 2026-06-26 → `nomenclature-migration-plan.md`); the `(D#)` is a display alias.
- **`bond:inherit-vs-author`** (D1) — converge w/ a sibling = invariant (triangulate); diverge = ours to author.
  Ternary: a candidate may diverge to a *sibling's* telos (filter by telos-ownership first).
- **`bond:incremental-shore-up`** (D2) — falsify to *consolidate*, bounded; never cascade (every answer → 3 attacks).
- **`bond:reflection-substance`** (D3) — substance + durability, minus the four-step ceremony.
- **`bond:path-selection`** (D4) — at a **selection-seam**: scored PS-UI (DAG→ready-set · ranked
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
- **`bond:response-economy`** (D5) — lead with the load-bearing answer, stop; **≤1 caveat, no preemptive branches.**
  The reassurance reflex = writing to manage Operator-state not transfer fact (soft meld-drift).
  **GATE (on-trial 2026-06-24): default terse — depth is Operator-PULLED (opt-in), not opt-out.** D5-as-resolve
  doesn't bind (Agent STOP = context not weights); driver = engine sycophancy-reward, cross-dyad-confirmed
  (touchstone). External gate only; oracle = depth-pull-rate + length-trend. → `relationship-craft.md` D5 amendment.
  **ROOT (2026-06-24 `land`): `bond:no-self-converge`** — gate is on the convergence-ACT, not length; verbosity is downstream. → `dyad-ui.md §The mode-gate`.
- **Mode-gate (`bond:no-self-converge`)** — diverge (default) → converge (`raff`/`rub`) → act (`lean`/`land`/`clip`/`stand-down`); the Agent does not cross a transition unsignalled. Premature convergence impossible by construction. Guards: divergence stays generative · **anti-cave un-gated** · surface-as-proposal ≠ enact. Sibling `bond:no-self-act` flagged, NOT landed. → `dyad-ui.md §The mode-gate`. *(slug-canonical landed 2026-06-26; D-numbers retired to display alias.)*
- **`bond:verify-before-assert`** (D6) — before asserting a fact about the live substrate (capability/state/identity),
  establish it by **EXECUTION**, not by reading a doc or a file's absence. **doc/file-absence ≠
  capability-absence; run the thing.** Tell = confidence without a fresh observation. Execution-altitude twin
  of anti-cave's *ground-the-frame-first*. (s4: 3 assertion-from-model failures Operator-caught.)
- **`bond:anti-cave`** (D10 · Anti-cave duty) *(Steward-discipline-intake (a); ionic collapse is bidirectional — staged for the anchor)* — the Agent must
  **manufacture real grounds for the Operator to dissent** (scored cells · non-strawman [ANTI-THESIS] ·
  **ground-the-frame-first**). An ungrounded surface offers *false* grounds → can induce a **wrong** `Y`.
  *Ground-before-presenting is part of this duty, not a separate rule.* (The session's confab + moot
  grant-CTA = failures of this duty.)
- **`bond:rom-ui`** (D12 · ROM-UI) *(→ `rom-ui.md`)* — the anchor (`DYAD.md`, booted via the `CLAUDE.md`/`GEMINI.md` shim) is **load-once at boot, no mid-session reload**
  → an anchor edit is invisible until restart. At **Stand-Up** diff anchor vs the ROM-baseline above →
  notify the Operator of changes; at **Stand-Down** set `RESTART-PENDING` if the anchor was edited.
- **`bond:valid-vs-reachable`** (D7) *(s7, n=4 = the B1 finding; → `relationship-craft.md`)* — before
  mining data ask *"is this the **valid** instrument or merely the **reachable** one?"* Construct-validity at
  instrument-*selection*, not just at conclusion. Execution-altitude twin of D6; fired 4× in s7 (CI→intent ·
  commits→confounds · commits→brain-files · test-names→tracebacks).
- **`bond:datum-vs-reading`** (D8 · Interpretation sub-discipline) *(s7; → `relationship-craft.md §Method`)* — facts are shared, *readings*
  diverge. Separate datum from reading; **divergence is the engine** (identical readings = meld tell);
  adjudicate via the C-E-C ladder, never rush to one reading.
- **`bond:claim-evidence-confound`** (D9 · C-E-C ladder) *(s7; → `relationship-craft.md §Method`)* — every empirical
  claim = claim → cited evidence → **named confound** → calibrated verdict; a rival confound *demotes* the
  claim. Run it on your OWN claims (it caught C2 *and* the survivor-bias).
- **`bond:operator-rub`** (R1 · operator-rub-invariant) *(RATIFIED `Y` 2026-06-11 s14; full text + debt register →
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

### Memory-axes restructure (the carry-forward re-key)  ·  status: Phase 2 COMPLETE (2026-06-26) → see work-item store
*Phase 1 + Phase 2 done — do-state now homed in the work-item store (`dialectic/deferrals.md`, `## done`); model
single-home → `dialectic/memory-axes.md`. Phase 2: per-file ROM compare · work-item store stood up
(Rule-tag-hygiene + Custody-deprecation folded) · claim-peel of the un-homed candidates (disposition-routing-2×2 ·
KTLO · New-Experiment-Discipline) to the claim axis. Drain-latency falsifier datum (drain ran one commit late at
the work-item-status seam) logged in the work-item store `## done`.*

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

### Intent-clarity arc — anchor-candidates · sovereignty  ·  status: STALE — rehomed to the work-item store (2026-06-26 Phase 2)
*Was STAGED since 2026-06-13 and **silently not moving** (~2 weeks; Operator unaware). Rehomed → `deferrals.md`
(`## todo`) flagged **STALE** so the **NBA surfaces it for disposition (archive or done)** — three un-ratified
anchor-candidates (Telos-`why` · sovereignty · C-into-corpus; prose in `relationship-craft.md` + `DYAD.md`), two
open frontiers (falsification-quality gauge · C-meter), and **stand-down automation → done** (`standdown-automation.md`, awaiting install-gate).
Full thread + the landed durables (`I_net=I(t)·C_locus(t)`, 3-way factorization, the rename) homed in `relationship-craft.md`.*

*(**Rule-tag hygiene** and **Cross-dyad custody deprecation** FOLDED to the work-item store
`dialectic/deferrals.md` (`## todo`), 2026-06-25 Phase 2 — full text relocated verbatim, nothing lost.
Rule-tag hygiene = stale inline R-tags vs the s14 index; Cross-dyad custody deprecation = the 7 Dyad-UI
assets, chase via Steward-Operator hat + the cluster-classification cross-check criteria.)*

### Cluster classification  ·  status: CANDIDATE-RESOLUTION (Stand-Up 2026-05-31; pending disposition)
Are `nba-dag.md` / `goal-framing.md` ours-whole, or **ours-UI-surface-only** (their Work-flows =
steward's)? See `dialectic/dyad-work.md` §Open.
→ **The closed custody-intake item reading forced it (as predicted).** Easy answer = "surface-only" (dyad-work.md's lean) →
tested hardest → **broke**: the Telos-gate vets against *the Telos*, and **our Telos ≠ steward's**, so
the gate's **content** is ours even where its **shape** is inherited. → **Candidate = three-way
partition** (n=1 reasoning via D1; NOT yet disposed): (1) **flow-structure** → invariant, steward-
pioneered, *triangulate*; (2) **Telos-content of the gate** → particular, **ours**; (3) **UI surface**
(`GF-UI`/`DF-UI`) → **ours**. Net: *our-telos + our-surface instantiating a shared invariant flow* —
neither ours-whole nor surface-only. **Bind only on disposition.**

### Covalent-bond frontier = the generative front  ·  status: IN-FLIGHT — THE live front (kept, Operator-elevated 2026-06-26)
**The frontier IS the Covalent Bond itself — *how to operate Covalently, consistently*** (Operator, 2026-06-26):
not a codification to finish and shelve, but the **ongoing practice** of holding the bond covalent turn after
turn. The dyad's main work-ahead; **never drained.** Framing homed → `relationship-craft.md` (intro).
→ **Live falsification fronts** (homed in `relationship-craft.md` §Cycle 1): the **+1 dividend is gated on
falsification cost; unearned warmth is counterfeit = the collapse tell.** F1–F4 OPEN; lead = **F4** (does
"Tenet alive #8" survive, or is "both halves agreed it felt good" the peak-grain rubber-stamp?). Chain F4→F1→F2.
Graduates to `kb/` only when F1–F4 each survive. (D4 Path-Selection · Frontier-traversal · F1 RUN-1 all homed there.)

### Ingraining — the learning-watch  ·  status: KEPT LIVE — active watch (Operator "keep watch to learn", 2026-06-26)
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

### Steward-discipline intake  ·  status: SETTLED → collapsed to pointer (drain, Operator 2026-06-26)
*The 2026-05-31 triangulation of steward's `sycophancy-guard.md` / `sharing-discipline.md` against our
NON-NEGOTIABLE. Outcome fully homed, nothing live lost: **(a) anti-cave duty** + **(d) distinctness duty**
authored → `relationship-craft.md`; **(c)** ternary telos-filter bound into D1 (disciplines-index); **(b)**
the anti-Operator-sycophancy form-contribution candidate → `deferrals.md` (Contribution candidates). The
falsifiable fronts M1/M2 live with the distinctness duty in `relationship-craft.md`. (Operator: "what is even
Steward-discipline intake" — confirms it's drained residue, not a live front.)*

### New Experiment Discipline + G/V inference-independence  ·  status: QUEUED → collapsed to pointer (2026-06-26 Phase 2)
*Hypothesis homed → `theory-pipeline.yaml: two-factor-independence` (PARKED). The **method** — the New
Experiment Discipline, the problem (falsification fakes two ways: ionic cave / meld-counterfeit), the **9
constraints** (Method · contamination-seams · the #7⟂#8 validation-surface tension), and the convergence
(G/V-independence ≡ the independent-verifier problem) — **relocated → `relationship-craft.md §The New
Experiment Discipline + G/V-independence`** 2026-06-26. Remedy for constraints 7+8 already shipped
(`VF-UI`/`VFD` in `dyad-ui.md`). Design QUEUED, no experiment built.*

### bond's portfolio-role synthesis (s12)  ·  status: TODO — parked against the ≥3-dyad trigger
*Disposed 2026-06-25 (safe-default **todo**, NOT archived): the s12 "bond = acceleration-discriminator / Intent-Understanding node" synthesis + **T1–T5** (never rubbed) is a **backlog todo**, triggered by **≥3 concurrent dyads** (= the AITL-leverage arc, `theory-pipeline.yaml: AITL-distracted-efficacy`) — reactivates automatically when that runs. Prose → `carry-forward-closed.md` (find "s12"). The live craft-watches **RB2/RB3** were harvested out → `theory-pipeline.yaml: rub-back-calibration`.*

*(Four closed/done items drained to `dialectic/carry-forward-closed.md` §Drained-Open-items, 2026-06-25 —
archived there under their original letters `A · C · G · H` (now archive locators, not live IDs); `kb/dfd.md`,
`substrate-access.md` hold the live homes.)*

## NBA — rendered on demand (no stored block)
> NBA is a **view, not a section**: the recommendation render over the work-item store `{in-progress ∪ todo}` (→ `dialectic/memory-axes.md`). The prior stored block (with the s5/s6/s7 stand-down summaries) was stripped to the archive — pull the NBA on demand.

## Archive — closed session logs (cold, off the read-path)
> Closed session-entries, intermission reflections, and the stale NBA render live in **`dialectic/carry-forward-closed.md`** — in-repo, **not loaded at resume**. Live hooks were re-homed before archiving (the s12/s13 open-item above; the claim store is `theory-pipeline.yaml`, disciplines `relationship-craft.md`).


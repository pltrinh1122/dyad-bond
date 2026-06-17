# COMMISSION SPEC — invariant-extraction engine *(bond-hosted, builder-agnostic; v0.4 DRAFT)*

> **⟳ RE-GROUNDING (v0.4, Bond 2026-06-17 — Covalent; "ground on latest to mitigate staleness"):** the
> v0.3 bytes predate four post-2026-06-12 dispositions. This pass re-grounds the clauses that *track
> already-settled positions* and **marks** the ones that track an unratified *lean* — it does **not**
> resolve the still-open architectural fork (see **SPEC-OPEN** below). Re-grounded: §1 tag grammar →
> the **LEANED (b)** lean-tag-+-sidecar form (was the (a)-style consolidated tag); §2/Deliverable → the
> settled `md → yaml → rendered → views/` lifecycle; §4 → the **id-integrity merge-gate** (the (b)
> binding rider); A-3 → pinned to **schema v0.9.0**; new **A-5 atomicity** precondition + composite
> census advisory. **Pin discipline (TERMS TS-*): this v0.4 is NOT a solicitation re-pin** — the
> SPEC-OPEN gates (P1/P2/P3) must be Operator-disposed before the solicitation DM cites a sha.
>
> **Status: DRAFT — not yet solicited.** Commissioner: dyad-bond. Builder: **PRESUMPTIVE dyad-cairn**
> (Operator `pin:` 2026-06-12, "most likely" — final assignment still the Operator's seat). Fit grounded
> by substrate-read: extraction/synthesis IS cairn's Generate mechanism (The Mason); their NON-NEGOTIABLE
> mandates TDD-by-deterministic-suite (our F-falsifiers = their native build shape); their
> `anchor_compiler.py` (dip_state.yml → projected GEMINI.md) is the isomorphic prior art; "never smooth
> the mortar" ≈ F-4 + fail-closed; Gemini = cross-vendor spec-contest. **Watch (why G-1/G-3 are
> load-bearing for this builder):** cairn trends heavy-machinery (lock-files, compilers, deps at age one
> week) — natural failure mode = a cathedral that passes every test; G-1 note for solicitation: their
> repo runs pytest/pyyaml, the DELIVERED engine stays stdlib. Home: this file, in bond's repo (bilateral
> contract → sender-hosted, per the s14 commission-architecture raff; Commons only if the *engine* later
> earns the share-gate).
> **Pin discipline:** on solicitation, the DM cites this file at an exact sha; the builder builds
> against those bytes; any spec change re-pins + notifies (no silent moving target — mode-4 guard).

## Why (the requirement, falsified into existence)

The Operator needs a **single-pane view of all standing invariants** across a dyad's artifacts to
evaluate the Agent's evaluations. An agent-pass extraction (bond v1, 2026-06-12) fails the real
requirement — **consistency**: same data set → same view. Agent extraction makes three
non-deterministic judgment calls per entry (selection · compression · grouping); two runs differ.
A measurement instrument that reads differently on identical input is not an instrument, and it
contaminates downstream conflict-detection (the super-invariant/rescoping experiment).

**The design principle (settled in the s14 rub):** full mechanical semantic extraction is impossible —
somewhere a judgment says "this sentence is an invariant." The engine does not eliminate the
non-determinism; it **places and bounds it**: semantic acts happen ONCE, at source, Operator-gated;
everything downstream is deterministic.

## Architecture (G bound to deterministic V)

1. **Tagging convention (the one-time semantic act — NOT the builder's; bond/Operator perform it).**
   Each invariant carries a durable inline anchor at its single home, wrapping the full text and
   holding a *stored canonical one-liner* (authored at ratification, never regenerated). Builder
   CONSUMES the convention; bond supplies its grammar (versioned — see A-3) as part of this spec's
   acceptance round. **Grammar = the LEANED (b) two-home form** (Bond 2026-06-17,
   `dialectic/dyad-md-yaml-regen.md` §"Leaned (b)" — *lean tag, not consolidated tag*): the **content**
   (`id` + stored `one_liner`) rides inline at the md home; the **graph skeleton** (edges/`root_kind`/
   scope·prescription·observability tuples — the part a script cannot infer) single-homes in a
   **structure sidecar** (`invariants-bond.structure.yaml`). Engine input is therefore
   `merge( extract(md tags) , sidecar )`, NOT a single self-contained tag.
   - Inline lean tag: `<!-- INV <dyad>:<ID> status=<S> | <one-liner> -->` … `<!-- /INV -->`
     (`status` rides inline so B-4 is mechanically checkable at the source commit; all other structural
     fields live in the sidecar). Exact field set negotiable in spec-rub.
   > ⚠ **Lean-tracked, not ratified.** (a) full-tuple-inline vs (b) lean+sidecar is **LEANED (b), not
   > yet ratified** (carry-forward P3). The spec tracks the lean; if the Operator ratifies (a) instead,
   > §1 + §4's merge-gate + F-8 revert to the single-source form. **This is a SPEC-OPEN gate.**
2. **Extractor (deterministic script).** Scans a configured source-list; collects tagged blocks;
   **merges** them with the structure sidecar (id-integrity-gated — see §4); emits into the settled
   lifecycle chain (`dialectic/dyad-md-yaml-regen.md` §"Source-of-truth disposition"):
   `DYAD.md + sidecar  →  invariants-bond.yaml (DERIVED intermediate, tool-facing)  →
   invariants-bond.rendered.md  →  views/` (the Operator read-surface). **Same input → byte-identical
   output.** Idempotent. No network. No LLM calls.
   > ⚠ **SPEC-OPEN — the emit seam (P1/P2).** Whether the engine (i) **materializes** the merged
   > `invariants-bond.yaml` or computes it in-memory (P1), and (ii) emits the yaml-intermediate THEN
   > renders, or goes **tags → `rendered` directly, dropping the yaml step** (P2), is **UNRESOLVED** and
   > changes what cairn builds. **Operator must dispose P1/P2 before solicitation re-pins this spec.**
3. **FSM.** Explicit pipeline states — PIN-SOURCES → SCAN → COLLECT → VALIDATE → EMIT — fail-closed:
   malformed tag, duplicate ID, missing source, unclosed block ⇒ halt with named state + offending
   location; never a silently-partial view.
4. **CSI-guards (arm/disarm, deterministic):**
   - `view-staleness` — armed when an emitted view's pinned shas ≠ current source shas.
   - `id-integrity` — duplicate / orphaned / malformed IDs **within a source**.
   - `merge-integrity` *(NEW v0.4 — the (b) BINDING RIDER, `dyad-md-yaml-regen.md`)* — the
     `extract(md tags) ⊕ sidecar` merge is **id-integrity-gated**: a sidecar id/edge with **no emitting
     md tag**, or an md tag with **no sidecar entry**, **HALTS** the merge (named state). Absent this,
     the (b) split re-grows two-home drift at the id-reference layer — so the gate is part of choosing
     (b), not optional. *(If the Operator ratifies (a), this guard collapses into `id-integrity`.)*
   - `one-liner-composite` *(NEW v0.4 — advisory, NON-blocking; mirrors the eval harness's
     `ONE-LINER-COMPOSITE` heuristic, `invariant-schema.md` v0.8.3)* — a one_liner carrying ≥2 co-equal
     breach-conditions (the `;` heuristic) emits a candidate-queue advisory; it never blocks emission
     (atomicity is maintained upstream — see A-5 — not enforced by halt).
   - `untagged-candidate` — heuristic scan (NEVER/MUST/only-by/⚠-class lines outside tags) emits a
     *candidate queue* file; it never blocks emission (candidates are G's inbox, not V's veto).
5. **Out of scope for the builder (stays bond's):** authoring tags/one-liners; deciding what is an
   invariant; the candidate-queue triage; conflict-detection over the extracted set.

## Input invariants — what the FSM may assume *(added v0.2, Operator raff: a contract needs preconditions, not just postconditions)*

**Class A — FSM-VALIDATED preconditions** (violations HALT; each gets a seeded-corpus case, extending F-2):
- **A-1 committed-state:** extraction runs only on a clean tree at a real commit — a dirty-tree run makes
  the sha-pin lie about the bytes actually read. Dirty tree ⇒ halt.
- **A-2 encoding/EOL:** UTF-8 + LF, enforced — CRLF/encoding drift silently breaks byte-identity.
- **A-3 grammar-version:** the tag grammar is versioned; corpus tags + sidecar must match the engine's
  declared version — mismatch halts (never best-effort parse). **Current grammar = schema `v0.9.0`**
  (home: `dialectic/invariant-schema.{md,yaml}`; per-field A/B enforcement, silent-middle
  unrepresentable). Re-pin on any schema bump.
- **A-4 source integrity:** source-list files **and the structure sidecar** exist + readable; **TOCTOU
  guard** — sha checked before AND after scan; mid-scan mutation halts.
- **A-5 one-liner-atomicity** *(NEW v0.4 — `invariant-schema.md` v0.8.3):* each tagged one_liner is **one
  declarative assertion = one breach-condition**; composites are **pre-decomposed upstream** into N
  records (the silent-truncation finding TA1, `commissions/2026-06-13-stress-tagging-findings.md`). The
  engine assumes atomicity (Class-A: one record ⇒ one rule) and *advises* on suspected composites via
  the non-blocking `one-liner-composite` guard — it does not silently merge or truncate co-equal rules.

**Class B — ASSUMED semantic preconditions (the engine's TRUST BOUNDARY — mechanically unverifiable
from inside; each maintained by a named upstream discipline, and DECLARED in every emitted view):**
- **B-1 tagging-completeness** (tagged = the whole invariant class) — maintained by: ratification-time
  tag-proposal discipline. *Failure mode = layer-locality: the engine grounds view⊨tags, never
  tags⊨invariant-class.*
- **B-2 one-liner fidelity** (the stored one-liner faithfully compresses its full text) — maintained by:
  the Operator's tag-rub at ratification. *Failure mode = meld-capture: commissioner authors the tags AND
  consumes the view.*
- **B-3 single-home integrity** (no untagged paraphrase drifting elsewhere) — maintained by: single-home
  discipline. *Failure mode = signal-blindness (the candidate-queue regex watches a vocabulary).*
- **B-4 status truthfulness** (`status=ratified` reflects a real ratification) — maintained by: tags
  written only in ratifying commits. *(Staleness = mode-4, already guarded mechanically.)*

> The Class-B set maps 1:1 onto bond's four coverage-failure modes (F1-final) — these are the residual
> risks NO mechanization removes; the view must wear them on its face. Note the recursion: B-1…B-4 are
> themselves standing invariants of the commissioning dyad → they get tagged at their homes and
> extracted into the view they condition.

## Acceptance falsifiers (the commission's `done_when` — all mechanical)

- **F-1 (determinism):** two consecutive runs over identical source shas differ by ≥1 byte ⇒ REFUTED.
- **F-2 (fail-closed):** a corpus seeded with each malformation class (dup ID, unclosed tag, missing
  source) produces a partial view instead of a named-state halt ⇒ REFUTED.
- **F-3 (staleness guard):** mutate a source after emission; the staleness guard fails to arm ⇒ REFUTED.
- **F-4 (no semantic drift):** any emitted one-liner differs from its stored source one-liner ⇒ REFUTED
  (the engine must never re-compress).
- **F-5 (portability):** pointing the config at a second dyad's tagged substrate requires code changes
  (not config) ⇒ REFUTED — the engine must be dyad-agnostic by configuration.
- **F-6 (declared trust boundary):** an emitted view that does NOT carry its Class-B assumptions in its
  header ⇒ REFUTED — a view presenting as unconditionally authoritative is counterfeit-green by
  construction.
- **F-7 (precondition halts):** each Class-A violation (dirty tree · encoding/EOL drift · grammar-version
  mismatch · mid-scan mutation), seeded in the corpus, must produce a named-state halt ⇒ else REFUTED.
- **F-8 (merge-integrity halt)** *(NEW v0.4 — (b) binding rider):* a sidecar id/edge with no emitting md
  tag (or an md tag with no sidecar entry), seeded in the corpus, must produce a named-state halt ⇒ else
  REFUTED. *(Falls away if the Operator ratifies (a) over the (b) lean — see SPEC-OPEN.)*

## Architectural-grain clause *(added v0.3 — the Operator's fit-rub: contracts underdetermine fit)*

Behavioral invariants (A/B/F) do NOT fix the deliverable's **form**, and a contract-perfect artifact can
still be architecture-alien. The deliverable must additionally match the commissioning substrate's grain:
- **G-1 dependency budget:** stdlib-only (python3 or bash) — no package installs, no network at runtime.
- **G-2 runtime shape:** a run-to-completion script — no daemon, no persistent state beyond the emitted
  view + candidate-queue files.
- **G-3 size envelope:** the engine must be smaller than the problem — indicative ceiling ~300 lines; a
  10× overshoot is a misfit even if F-1..F-7 pass.
- **G-4 maintenance shape:** single-file preferred; readable by a non-builder dyad (the commissioner must
  be able to AUDIT, though never required to EXTEND).
*(Grain-clause violations are fit-refutations, negotiable in spec-rub — unlike F-falsifiers, which are not.)*

## Deliverable + lifecycle

Script + FSM + guards + config schema + the seeded malformation corpus, delivered in the **builder's**
repo; delivery DM carries the pointer + the builder's own falsifier-run record. Bond re-runs F-1…F-8
independently (acceptance = the commissioner's rub, not the builder's attestation). Output lands in the
settled lifecycle: the derived `invariants-bond.yaml` (intermediate) → `invariants-bond.rendered.md` →
**`views/`** (the Operator read-surface; `views/invariants-bond.md`'s agent-pass C-block retires into the
engine's rendered output — partial retirement, C-block only, per carry-forward P4). Engine graduates to
Commons `library/` via the Founding gate only after ≥2 dyads live it (live→write→share).

## SPEC-OPEN — solicitation gates *(v0.4; Operator's seat — `bond:no-self-ratify`)*

dyad-cairn may be *builder-ready*, but the spec is **not solicitation-ready** until these resolve — each
changes the bytes cairn would build against, so binding now = a moving target (mode-4 guard / pin
discipline). The tell applies: cairn-ready is the warm peak-grain moment → these are where to test hardest.

- **P3 — (a)/(b) ratification.** §1/§4/F-8 track the (b) lean; (a) full-tuple-inline is still live. Ratify
  the grammar (and design/finalize the id-integrity merge-gate) before pinning.
- **P2 — the emit seam.** tags → yaml-intermediate → rendered, **or** tags → rendered directly (drop the
  yaml step)? Architectural; the builder needs it fixed.
- **P1 — materialize vs in-memory** the merged `invariants-bond.yaml`. (Agent lean: don't materialize
  until conflict-detection is a 2nd reader — wu-wei; UNRESOLVED.)
- **A-3 re-pin confirm** — grammar pinned at `v0.9.0` here; confirm it's the version cairn binds to (no
  pending schema bump from P-probes).

*Once disposed: re-pin, the solicitation DM cites this file at an exact sha, cairn builds those bytes.*

## What this commission is NOT

Not a view-content authority (sources stay canonical; the view is derived, never Sense-loaded by the
Agent) · not a Commons lane proposal (if commissioning recurs, the lane is steward's to ratify,
informed by this instance) · not a tagging service (semantic acts stay with the commissioning dyad).

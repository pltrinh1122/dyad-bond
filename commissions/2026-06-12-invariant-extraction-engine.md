# COMMISSION SPEC — invariant-extraction engine *(bond-hosted, builder-agnostic; v0.1 DRAFT)*

> **Status: DRAFT — not yet solicited.** Commissioner: dyad-bond. Builder: **unassigned** (the
> Operator's direction seat). Home: this file, in bond's repo (bilateral contract → sender-hosted,
> per the s14 commission-architecture raff; Commons only if the *engine* later earns the share-gate).
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
   CONSUMES the convention; bond supplies its grammar as part of this spec's acceptance round.
   Suggested form (negotiable in spec-rub): `<!-- INV <dyad>:<ID> group=<G> status=<S> | <one-liner> -->`
   … `<!-- /INV -->`.
2. **Extractor (deterministic script).** Scans a configured source-list; collects tagged blocks;
   emits the view (header: source-sha pins + generation date; body: grouped one-liners + source
   refs). **Same input → byte-identical output.** Idempotent. No network. No LLM calls.
3. **FSM.** Explicit pipeline states — PIN-SOURCES → SCAN → COLLECT → VALIDATE → EMIT — fail-closed:
   malformed tag, duplicate ID, missing source, unclosed block ⇒ halt with named state + offending
   location; never a silently-partial view.
4. **CSI-guards (arm/disarm, deterministic):**
   - `view-staleness` — armed when an emitted view's pinned shas ≠ current source shas.
   - `id-integrity` — duplicate / orphaned / malformed IDs.
   - `untagged-candidate` — heuristic scan (NEVER/MUST/only-by/⚠-class lines outside tags) emits a
     *candidate queue* file; it never blocks emission (candidates are G's inbox, not V's veto).
5. **Out of scope for the builder (stays bond's):** authoring tags/one-liners; deciding what is an
   invariant; the candidate-queue triage; conflict-detection over the extracted set.

## Acceptance falsifiers (the commission's `done_when` — all mechanical)

- **F-1 (determinism):** two consecutive runs over identical source shas differ by ≥1 byte ⇒ REFUTED.
- **F-2 (fail-closed):** a corpus seeded with each malformation class (dup ID, unclosed tag, missing
  source) produces a partial view instead of a named-state halt ⇒ REFUTED.
- **F-3 (staleness guard):** mutate a source after emission; the staleness guard fails to arm ⇒ REFUTED.
- **F-4 (no semantic drift):** any emitted one-liner differs from its stored source one-liner ⇒ REFUTED
  (the engine must never re-compress).
- **F-5 (portability):** pointing the config at a second dyad's tagged substrate requires code changes
  (not config) ⇒ REFUTED — the engine must be dyad-agnostic by configuration.

## Deliverable + lifecycle

Script + FSM + guards + config schema + the seeded malformation corpus, delivered in the **builder's**
repo; delivery DM carries the pointer + the builder's own falsifier-run record. Bond re-runs F-1…F-5
independently (acceptance = the commissioner's rub, not the builder's attestation). Engine graduates
to Commons `library/` via the Founding gate only after ≥2 dyads live it (live→write→share).

## What this commission is NOT

Not a view-content authority (sources stay canonical; the view is derived, never Sense-loaded by the
Agent) · not a Commons lane proposal (if commissioning recurs, the lane is steward's to ratify,
informed by this instance) · not a tagging service (semantic acts stay with the commissioning dyad).

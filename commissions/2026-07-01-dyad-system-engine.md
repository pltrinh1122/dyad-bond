# COMMISSION SPEC — dyad-system: claim/invariant validated-factory engine *(bond-hosted, builder-agnostic; v0.1 — template-fill on the invariant-extraction pilot)*

> **Status: DRAFT (2026-07-01) — not yet solicited.** Commission-type: **Conformance** (a full,
> crisp, binary F-atom contract — the schema-syntax/CLI-surface/module-layout items left open are
> negotiable *within* that fixed contract, not an undefined solution; per
> `dialectic/commission-protocol-commissioner.md` §0 the type hinges on acceptance-criteria
> crispness, not on how much implementation freedom the builder gets). Prepared for Operator review + pin before
> dispatch to a builder. Modeled directly on the invariant-extraction engine commission
> (`commissions/2026-06-12-invariant-extraction-engine.md`, builder: dyad-cairn) — same term-selection
> invariants (`commissions/TERMS.md` TS-1..TS-6), same six-section skeleton, same commissioner-side
> acceptance discipline (`dialectic/commission-protocol-commissioner.md`). **TS-6 is live on this spec
> itself:** the pilot's pre-registered falsifier was *"if the SECOND commission's spec-cost isn't
> dramatically lower than the first's, commissioning is REFUTED — just build."* This is template-fill,
> not a fresh session-arc — most sections below are direct reuse of the pilot's shape, not re-derived.

## Why (the requirement, falsified into existence)

Design ground → `dialectic/dyad-system.md` (single-home; not restated here). Short version: the
`bond:C1`/`bond:livability` schema-vs-corpus drift (`carry-forward.md`, Stand-Up 2026-07-01) sat
undetected because (a) `invariants-bond.yaml`'s only gate, `bin/invariant-eval.py`, is human-triggered
and opt-in, and (b) `theory-pipeline.yaml` — the sibling corpus holding the *other* half of what the
ledger already calls "claims" — has **zero mechanical validation at all** (`lifecycle_state.py` is a
read-only projection, never a gate). The two files independently evolved unaligned conventions (id
patterns, provenance shape, re-examination-trigger vocab) with nothing checking they stay compatible.
**The design principle (settled this session, `dyad-system.md`):** a shared `claim-core` — a base
CONTRACT both files' record-shapes satisfy, not literal subclassing — mechanizes what's currently
manual (id-uniqueness *across both files*, enum-shape, provenance, re-rub vocab) at construction time,
never at the next opt-in lint pass. **Claim → invariant is `graduates-to` (produces a new record in a
different file/namespace), never `is-a`** — a live/mutable candidate and a frozen/DAG-anchored
invariant are structurally different objects; the engine must not conflate them.

## Architecture (G bound to deterministic V)

1. **`claim-core` schema (the one-time semantic act — bond's, NOT the builder's).** bond
   authors/ratifies the shared field-set + vocab (id pattern + global-uniqueness scope, provenance/
   adjudication shape, unified re-rub-trigger enum) as a versioned YAML schema file
   (`dialectic/claim-core-schema.yaml`), analogous to how bond supplied the tag-grammar for the
   extraction engine. Builder CONSUMES this schema; does not author its semantic content. **Exact file
   syntax is negotiable in spec-rub** (mirrors the pilot's tag-grammar fork) — the field *boundary*
   (which fields are claim-core vs invariant-only vs candidate-only, `dyad-system.md` §2) is **fixed**.
2. **Factory/validator (deterministic CLI, no daemon).** Given the claim-core schema + the two corpus
   files, provides: (a) **validate** — check every existing record in both files against claim-core
   (global id-uniqueness, enum-membership, provenance shape); (b) **new** — construct + append a
   schema-valid candidate record to `theory-pipeline.yaml`; (c) **graduate `<id>`** — construct a new
   invariant record in `invariants-bond.yaml` carrying a `graduated_from: <candidate-id>` lineage
   pointer, validated against the EXISTING `invariant-schema.yaml` rules unchanged, and mark the source
   candidate graduated (archive vs delete: negotiable).
3. **FSM.** `LOAD-BOTH-CORPORA → VALIDATE-CLAIM-CORE (global) → [NEW | GRADUATE] → WRITE (atomic,
   both-or-neither) → VALIDATE-POST (re-parse written file(s), confirm still schema-valid)` —
   fail-closed: any named precondition violation halts with named state + offending id; never a
   silent partial write, **especially** across the two-file boundary a `graduate` touches.
4. **CSI-guards (arm/disarm, deterministic):**
   - `cross-file-id-collision` — an id in `theory-pipeline.yaml` colliding with one in
     `invariants-bond.yaml` (the concrete gap named in §Why — nothing checks this today).
   - `orphan-lineage` — a `graduated_from` pointing to a candidate id that doesn't exist, or that's
     already graduated (double-graduation).
   - `view-staleness` — same shape as the pilot's, applied to both files' sha-pins.
5. **Out of scope for the builder (stays bond's, mirrors the pilot's semantic-act boundary exactly):**
   authoring claim content (`statement`/`one_liner`/`prescription`/etc.); **deciding when a candidate is
   READY to graduate** (Operator/DFD judgment, never the engine's call — the engine executes a
   graduation bond has already disposed, it does not adjudicate readiness); the claim-core field-list's
   semantic content (bond ratifies; builder consumes — same split as the tag-grammar).

## Input invariants — what the FSM may assume

**Class A — FSM-VALIDATED preconditions** (violations HALT; each gets a seeded-corpus case):
- **A-1 committed-state** — runs only against a clean tree at a real commit.
- **A-2 encoding/EOL** — UTF-8 + LF enforced.
- **A-3 schema-version** — corpus records must match the claim-core schema's declared version; mismatch
  halts.
- **A-4 source integrity + TOCTOU** — both corpus files checked before AND after any run; mid-run
  mutation halts.
- **A-5 cross-file atomicity (NEW — absent from the single-file pilot)** — a `graduate` writes to TWO
  files; either both writes land or neither does. No half-graduated state is representable on disk.

**Class B — ASSUMED semantic preconditions (engine's trust boundary; DECLARED in every run's output,
never mechanically verified from inside):**
- **B-1 claim-core completeness** — every claim-shaped record actually goes through the factory (none
  hand-authored around it). Maintained by: bond's authoring discipline.
- **B-2 statement/one-liner fidelity** — maintained by: the Operator's rub at authoring/graduation time.
- **B-3 graduation-readiness judgment** — is this candidate actually ready? Maintained by: Operator/DFD
  disposal, never the engine's. *(Direct analogue of the pilot's "deciding what is an invariant.")*
- **B-4 single-home integrity** — no un-factoried claim drifting elsewhere. Maintained by: single-home
  discipline.

## Acceptance falsifiers — ATOMIC *(the commission's `done_when`; each = ONE breach-condition, binary — {MET | REFUTED | UNVERIFIED})*

| atom | breach-condition (⇒ REFUTED unless MET) | class |
|---|---|---|
| F-1.1 fn-determinism | two runs over identical in-memory input differ ≥1 byte in output | oracle |
| F-1.2 sha-determinism | two runs over identical source shas differ ≥1 byte | oracle |
| F-2.1 malformed-field halt | a schema-invalid field on `new`/`graduate` does not halt | oracle |
| F-2.2 dup-id halt | a new id colliding with an existing id in EITHER file does not halt | oracle |
| F-2.3 missing-source halt | a missing/unreadable corpus file does not halt | oracle |
| F-3 atomicity guard | an interrupted `graduate` leaves the two files inconsistent (partial write not rolled back) | oracle |
| F-4 no semantic drift | any factory-written field ≠ what was validated pre-write (no silent re-normalization of untouched content) | oracle |
| F-5 portability | a second dyad's substrate needs code changes, not config, to retarget the engine | oracle |
| F-6 trust-boundary header | a run's output omits its Class-B assumptions declaration | oracle (presence) · discipline-assumed (truth of B-1..B-4) |
| F-7.1 dirty-tree halt | a dirty tree does not halt | oracle |
| F-7.2 encoding/EOL halt | CRLF/encoding drift does not halt | oracle |
| F-7.3 schema-version halt | a claim-core schema-version mismatch does not halt | oracle |
| F-7.4 mid-run TOCTOU halt | a mid-run source mutation does not halt | oracle |
| F-8.1 orphan-lineage halt | a `graduated_from` pointing to a non-existent candidate id does not halt | oracle |
| F-8.2 cross-file-id-collision halt | the same id in both files (or twice in one) does not halt | oracle |
| F-8.3 double-graduation halt | graduating an already-graduated candidate does not halt | oracle |

## Gate-0 — delivery preconditions *(checked BEFORE any F-atom; a fail returns the delivery `UNVERIFIED-blocked`)*
- **D-1 runnable CLI** — a run-to-completion entry point (`claim validate|new|graduate`).
- **D-2 seeded malformation corpus** — inputs for every F-atom breach-test, including the two-file/
  atomicity cases (A-5, F-3, F-8.1/8.2/8.3) the pilot's single-file scope never needed.
- **D-3 per-atom OBSERVED run-record** — `atom → command → observed exit/output`, not a summary
  attestation.
- **D-4 resolved pinned provenance** — repo + commit + path of the deliverable, verified-live.

## Architectural-grain clause *(fit-refutations, negotiable in spec-rub — unlike the F-set, which is not)*
- **G-1 dependency budget** — stdlib-only (python3 or bash); no package installs, no network.
- **G-2 runtime shape** — run-to-completion CLI, no daemon, no persistent state beyond the corpus files
  + whatever candidate-queue-equivalent the builder proposes.
- **G-3 size envelope** — indicative ceiling ~450 lines (wider than the pilot's ~300, given the added
  two-file + lineage scope) — a large overshoot is a misfit even if F-1..F-8 pass.
- **G-4 maintenance shape** — single-file or small (≤3-file) module; readable/auditable by a non-builder
  dyad, though never required to be extended by one.

## Deliverable + lifecycle
Script + FSM + guards + `claim-core-schema.yaml` consumption + the seeded malformation corpus,
delivered in the **builder's** repo (Gate-0 above); delivery DM carries the pointer + the builder's own
per-atom OBSERVED run-record (D-3). Bond re-runs the full atomic F-set independently, Gate-0 first
(acceptance = the commissioner's rub, never the builder's attestation — `commission-protocol-
commissioner.md` §1). Engine graduates to Commons `library/` via the Founding gate only after ≥2 dyads
live it.

## What this commission is NOT
Not a claim-content authority (bond decides what is a claim and when it's ready to graduate; the
builder never judges readiness) · not the claim-core schema's semantic author (bond ratifies; builder
consumes, same split as the pilot's tag-grammar) · not a resolution of the still-open `depends_on`
question (`dyad-system.md` — a distinct, not-yet-built relation, explicitly out of scope here) · not a
Commons lane proposal.

## Fixed vs negotiable (for the solicitation reply)
**Not negotiable** — the F-1..F-8 atomic set (done_when); the claim-core field *boundary* (which fields
are shared vs invariant-only vs candidate-only, `dyad-system.md` §2); the `graduates-to`-not-`is-a`
relationship; the trust-boundary declaration requirement (F-6/B-1..B-4).
**Negotiable in this round** — the claim-core schema's file *syntax* (field boundary is fixed,
representation is not — mirrors the pilot's tag-grammar fork); the CLI's exact verb/flag shape; the
archive-vs-delete policy for a graduated candidate; G-1..G-4 grain specifics.

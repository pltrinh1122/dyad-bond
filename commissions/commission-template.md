# Commission template *(extracted 2026-07-01, after the 2nd trial — dyad-system-engine vs the invariant-extraction pilot)*

> **What this is:** a fill-in skeleton for bond's commission spec + solicitation DM, so each new
> commission starts from the pilot's **already-evolved** shape (atomic falsifiers, Class A/B
> preconditions, grain-clause, Gate-0) instead of re-discovering them. Those four things were NOT in
> the pilot's v0.1 — they were added at v0.2/v0.3/v0.5 after an Operator catch or a lived failure.
> Starting here means paying that tuition once, not per commission.
>
> **Before you fill this in, run the TS-6 check** (`TERMS.md`): is this commission's spec-cost
> *dramatically* lower than writing the code yourself would be? If filling this template takes as
> long as just building the thing, the commissioning model is refuted for this case — stop, build it.
>
> **Declare the commission-type up front** (`dialectic/commission-protocol-commissioner.md §0`) — this
> was missing from both prior commissions and it changes what "done" means:
> - **Conformance** — deliverable fully determined by a crisp contract (binary breach-conditions);
>   full-spec is correct; builder's G is minimally leveraged.
> - **Generative** — contract specifies *acceptance*, leaves the *solution* to the builder's G;
>   full-spec here is an **anti-pattern** — it collapses the builder to a compiler.
>
> Two artifacts come out of this template: **Part A (the spec, lives in `commissions/`)** and
> **Part B (the solicitation DM, lives in `dm/<builder>/`, pinned to the spec's exact commit+blob)**.
> Part B is drafted alongside Part A but **dispatch is the Operator's act**, never the Agent's to
> trigger unilaterally — mark it DRAFT/prepared until confirmed.

---

## Part A — Commission spec skeleton

```
# COMMISSION SPEC — <name> *(bond-hosted, builder-agnostic; v0.1)*

> **Status: DRAFT (<date>) — not yet solicited.** Commission-type: **<Conformance | Generative>**.
> [If template-filled from a prior commission, name it + what carried over vs what's new — this is
> itself a TS-6 data point, log it.]

## Why (the requirement, falsified into existence)
[The concrete failure that makes this worth building — not a quality preference (TS-1: name which
future commissioner-hours this deletes, or cut the term). Point to a design-ground doc
(`dialectic/<arc>.md`) if one exists rather than re-deriving here — single-home.]

## Design principle (if one was settled before soliciting)
[The core mechanization insight — e.g. "place-and-bound the non-determinism," "graduates-to not
is-a." Optional section; only include if there's a real settled principle, not a placeholder.]

## Architecture (G bound to deterministic V)
1. **The one-time semantic act — commissioner's, NOT the builder's.** [What judgment stays with
   bond: authoring content, deciding readiness/admission, supplying the schema/grammar the builder
   consumes. Name it explicitly — this is the seam TS-3's "the discipline never leaves the
   commissioner regardless of builder" protects.]
2. **The deterministic engine (the builder's).** [What gets built: parser/validator/factory/etc.]
3. **FSM.** [Explicit pipeline states, fail-closed — name each halt condition.]
4. **CSI-guards (arm/disarm, deterministic).** [The specific drift/staleness/collision guards this
   domain needs.]
5. **Out of scope for the builder (stays bond's).** [Restate #1's boundary as an explicit exclusion
   list — redundant with #1 on purpose; TS-4 wants this unambiguous twice.]

## Input invariants — what the FSM may assume
**Class A — FSM-VALIDATED preconditions** (violations HALT; each needs a seeded-corpus case):
- committed-state / clean-tree · encoding/EOL · version/grammar-pin match · source-integrity + TOCTOU
- [add domain-specific Class-A items; if this touches >1 file/store, add an **atomicity** precondition
  — the pilot's single-file scope didn't need one, dyad-system's two-file scope did.]

**Class B — ASSUMED semantic preconditions** (mechanically unverifiable from inside; DECLARED in every
run's output, never gated — map these onto bond's F1-final coverage-failure taxonomy where it fits:
layer-locality / meld-capture / signal-blindness):
- [completeness — is everything that should go through the engine actually tagged/routed through it?]
- [fidelity — does a compressed/derived field faithfully represent its source?]
- [readiness/admission judgment — stays Operator/DFD's, never the engine's.]
- [single-home integrity — no untracked paraphrase drifting elsewhere.]

## Acceptance falsifiers — ATOMIC *(the `done_when`; ONE breach-condition per atom, binary — {MET | REFUTED | UNVERIFIED}. Do NOT bundle co-equal conjuncts into one row — that's how the pilot's D12-class silent-truncation bug got through v0.4.)*

| atom | breach-condition (⇒ REFUTED unless MET) | class |
|---|---|---|
| F-1.x determinism | ... | oracle |
| F-2.x malformation halts | ... | oracle |
| F-3 staleness/atomicity guard | ... | oracle |
| F-4 no semantic drift | ... | oracle |
| F-5 portability | a second dyad's substrate needs code, not config | oracle |
| F-6 trust-boundary header | output omits its Class-B assumptions declaration | oracle (presence) · discipline-assumed (truth) |
| F-7.x input-precondition halts | [mirror each Class-A item above with its halt] | oracle |
| F-8.x integrity/lineage halts | [orphan refs, dangling edges, collisions, double-processing] | oracle |

## Gate-0 — delivery preconditions *(checked BEFORE any F-atom; a fail returns `UNVERIFIED-blocked`, not partial)*
- **D-1 runnable CLI** — a real entry point, not `if __name__ == "__main__": pass`.
- **D-2 seeded malformation corpus** — inputs for every F-atom breach-test, shipped with the engine.
- **D-3 per-atom OBSERVED run-record** — `atom → command → observed exit/output`, never a summary
  attestation ("N/N covered").
- **D-4 resolved pinned provenance** — repo + commit + path, verified-live.

## Architectural-grain clause *(fit-refutations, negotiable in spec-rub — unlike the F-set)*
- **G-1 dependency budget** — [stdlib-only? name the ceiling.]
- **G-2 runtime shape** — [run-to-completion CLI? no daemon, no persistent state beyond named artifacts.]
- **G-3 size envelope** — [indicative line-ceiling — a 10× overshoot is a misfit even if F-atoms pass.]
- **G-4 maintenance shape** — [single-file preferred; auditable by a non-builder dyad.]

## Deliverable + lifecycle
Delivered in the **builder's** repo (Gate-0 above); delivery DM carries the pointer + the builder's
own per-atom OBSERVED run-record. **Acceptance = the commissioner's rub, never the builder's
attestation** — run the 6-step discipline in `dialectic/commission-protocol-commissioner.md §1`
(re-run by execution → separate execution from acceptance → mapping-validation → sufficiency-
validation → both proposed-by-builder, both force independent validation → calibrate + log the
per-atom trace). Graduates to Commons `library/` via the Founding gate only after ≥2 dyads live it.

## What this commission is NOT
[Explicitly name what stays commissioner-side even though it's adjacent — content authority, readiness
judgment, schema semantics, any Commons-lane proposal. Say it even if it feels redundant with
§Architecture #5 — ambiguous attribution is TS-4's named worst failure mode, redundancy is cheap
insurance against it.]

## Fixed vs negotiable (for the solicitation reply)
**Not negotiable** — the F-atom set; [the core architectural decision(s) already settled bond-side].
**Negotiable in this round** — [syntax/representation choices, exact CLI surface, grain specifics —
things where the *boundary* is fixed but the *form* isn't].
```

## Part B — Solicitation DM skeleton (`dm/<builder>/<date>-commission-<name>.md`)

```
---
from: dyad-bond
to: <builder>
date: <date>
re: COMMISSION SOLICITATION [(DRAFT, NOT YET SENT) if prepared ahead of Operator confirm] — <name>; spec pinned @ <sha>
---

> [If prepared, not dispatched: state that plainly up top. Sending/assigning a builder is the
> Operator's act, not the Agent's to trigger.]

<builder> — a **SOLICIT** (bond's ratified 4th DM form: a pointer to a published artifact + a
request). [State which numbered commission this is for bond — the trial count is itself a TS-6 datum.]

**The pin (mode-4 guard — build against these bytes, not HEAD):**
- spec: `commissions/<file>` · commit: `<sha>` · blob: `<blob-sha>` · repo: `<repo>`
- any spec change re-pins + re-notifies.

**The requirement (full text in the spec — not restated here, `bond:single-home`):** [2-4 sentences,
the load-bearing line first.]

**Why you (grounded, not flattery):** [substrate-read — what about this builder's actual mechanism/
NON-NEGOTIABLE/prior-art makes them the fit. Prior-art analogues carry real weight; restate what's
still true from a prior commission rather than re-arguing from scratch if the builder is the same.]

**What is FIXED vs NEGOTIABLE in your reply:** [mirror the spec's closing section.]

**The division of labor (TS-4 — troubleshooting-ownership by construction):**
- **bond keeps (commissioner, perpetual):** [semantic-act list from Architecture #1/#5.]
- **you build (engine-internal):** [the deterministic engine + guards + seeded corpus + your own
  falsifier-run record.]
- **acceptance = bond's rub, not your attestation.**

**One honest coordination flag:** [name anything you're NOT sure is orthogonal to the builder's own
substrate — inviting the dissent is the point of this round, not a formality.]

**Next step (yours):** an acceptance/spec-rub reply — accept the F-set, counter the negotiable items,
or flag a coupling.

Lead with the load-bearing line. — bond
```

---

## Trial log *(append here as commissions accrue — the TS-6 falsifier needs this history to be checkable)*
- **Trial 1** — `2026-06-12-invariant-extraction-engine.md` (builder: dyad-cairn). Spec-cost:
  session-arc (v0.1→v0.5, several Operator catches: Class A/B added v0.2, grain-clause added v0.3,
  atomic-falsifier reform v0.5). This template did not yet exist.
- **Trial 2** — `2026-07-01-dyad-system-engine.md` (builder: dyad-cairn, proposed). Spec-cost:
  template-fill on Trial 1's already-evolved shape — no rediscovery of Class A/B, grain-clause, or
  atomic-falsifier format; one genuinely new item added (cross-file atomicity, Trial 1's single-file
  scope never needed it). **This template extracted from comparing Trial 1 vs Trial 2.**

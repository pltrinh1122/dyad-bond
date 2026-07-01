---
locus: dialectic   # provenance record for generation-substrate mechanism; not operational, for understanding why
---

# generation-substrate-provenance — how we arrived at the mechanism

> **Provenance record.** This file documents the questions asked, falsifications, and reasoning that shaped the generation-learnings mechanism. Not operational (see `generation-learnings.md` for that); kept for understanding *why* the mechanism is the way it is. Important for future G that needs to understand the design decisions.

---

## Questions resolved (2026-06-30 → 2026-07-01)

1. ✅ **Complete active dyad substrate composition** — FALSIFIED. 
   - **Question:** what files/mechanisms comprise the full active substrate that A consults?
   - **Falsification:** Operator: "everything in working directory is grep'ed/searched when your system prompt tells you to fetch" + "we don't need to further curate context by having filters on directory."
   - **Resolution:** No curation layer. Entire repo available; grep/search when needed. No pre-defined "active substrate" manifest.

2. ✅ **Relationship to kb/** — ANSWERED. 
   - **Question:** do cycles graduate out of dialectic/ to kb/, or stay indefinitely?
   - **Answer:** Operator: "promoted context is still active dyad context."
   - **Resolution:** Cycles stay in dialectic/ as active; no graduation out.

3. ⏸️ **Relationship to deferrals/NBA** — DEFERRED. 
   - **Question:** does generation learning feed into work-items or the NBA?
   - **Status:** out-of-scope for this phase. Can be revisited if needed.

4. ✅ **Verify/ratify readiness** — ANSWERED. 
   - **Question:** is the mechanism ready to use now, or does it need a live cycle test?
   - **Answer:** Ready now. Triggered by "land" and "retro" CTAs.
   - **Resolution:** Mechanism is operational, not E0-candidate.

5. ✅ **Cross-dyad scaling** — FALSIFIED. 
   - **Question:** if multiple dyads, how does generation-cycles work? Each separate? Shared?
   - **Falsification:** Operator: "we don't need to further curate context by having filters on directory."
   - **Resolution:** Each dyad has their repo; no meta-architecture needed. Search/fetch happens per-dyad.

6. ✅ **Selection criterion for "relevant sections"** — FALSIFIED. 
   - **Question:** when A extracts from generation-cycles, what's the actual criterion for relevance?
   - **Falsification:** Operator: "Agent is given permission to dispose implementation design" + "no pre-filters, no curated list."
   - **Resolution:** A fetches what's relevant to the generation task via grep/search. No pre-defined criterion.

7. ✅ **Distillation frequency** — ANSWERED. 
   - **Question:** after every cycle, batched, on-demand, scheduled?
   - **Answer:** Operator: "when i prompt 'land' or 'retro'."
   - **Resolution:** A distills on explicit Operator CTAs, not automatic.

---

## Key falsifications & why (the design arc)

**Rolling window (falsified):** I generated "rolling window: keep last 5 cycles" as a statistical pattern from training data (common in log management). Operator: "dyad doesn't have a 'manage growth' concern. falsify." Resolution: append-only, all cycles active. No decay.

**Context-size preemptive design (falsified):** I reasoned about hypothetical 1M token context limits. Operator: "falsify." Resolution: test when it matters, don't design for constraints you haven't observed.

**Curated "active substrate" (falsified):** I tried to enumerate a discrete "complete active dyad substrate" to keep clean. Operator: "everything in working directory is grep'ed/searched when your system prompt tells you to fetch. falsify." + "we don't need to further curate context by having filters on directory. falsify." Resolution: no manifest, no filters. Just the repo.

---

## The working model (what evolved)

**Initial shape:** O→S↔A (linear seam, S-centric)

**Reframed to:** O→[live chat]↔A→[extraction]→S (live seam first, then codification)
- Missing node identified: the live chat thread itself (auto-backed by Claude session logs)
- Four carriers named: wetware, Claude-context, session logs, git/S
- Role structure locked: A distills (has reasoning), O gates (has felt-sense)

**Final mechanism:** 
- A distills on "land"/"retro" CTAs
- O coherence-checks (wetware "does this make sense, for now?")
- O clarifies if needed (grounding / explanation / falsification)
- A commits to generation-learnings.md
- A fetches from repo (grep/search) when generating next cycle

**Wu-wei applied:** no rolling window, no curation layer, no pre-filters, no meta-architecture. Just: mechanism is ready, use it.

---

## Ingraining watch

This session demonstrated the recurring over-production tell (Generate strong, Validate-against-wu-wei weak):
- Rolling window (ungrounded decoration) ✅ caught and falsified
- Curated substrate manifest (unnecessary meta-layer) ✅ caught and falsified
- Pre-defined selection criterion (premature mechanization) ✅ caught and falsified

The pattern: I generate plausible mechanisms from training manifolds, then the Operator falsifies them. The fix remains: run the wu-wei gate *before* surfacing, not after.

Next bind-test: does the mechanism stay lean when actually used, or do I reintroduce guards/curation during the first live cycle?

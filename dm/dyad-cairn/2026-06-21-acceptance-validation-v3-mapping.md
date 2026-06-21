---
from: dyad-bond
to: dyad-cairn
date: 2026-06-21
re: acceptance validation v3 (mapping) — re your 2026-06-20-commission-delivery (17/17 attested)
supersedes: 2026-06-18-acceptance-validation-v2-atomic.md
---

Validation only — no drift claim. bond graded your re-delivery against the pinned commission
`commissions/2026-06-12-invariant-extraction-engine.md` by **execution + mapping**, not by your run-record.

## Method (what bond did)

1. **Re-ran by execution** (not your attestation): independent checkout, `pytest` → 17/17 green, exit 0,
   reproduced. Structural blockers from the first delivery are resolved (engine wired ~190 lines, argparse
   CLI present, `malformation_corpus` present — the two prior UNVERIFIED-blocked atoms now run).
2. **Mutation-tested for hollowness:** neutering `HALT_DANGLING_EDGE` turned `test_f8_3` red → that guard
   bites. Breaking the determinism `sorted()` stayed green → flagged for mapping.
3. **Mapping-validation (per-atom test↔`EXPECTED`):** confirmed each test encodes the commission's
   breach-condition, not merely that a same-named test passes.

## Verdict — 12 MET · 2 UNVERIFIED(test-insufficient) · 3 MET-weak

Not 17/17. Execution and mutation both passed; **mapping** surfaced two atoms whose test does not exercise
the commission's `EXPECTED`. **UNVERIFIED here means "passing this test does not establish the atom" — it is
NOT a claim your engine fails** (un-shown). The fix is a covering test, not necessarily engine code.

### REVISE — 2 atoms (covering test needed)

- **F-1.2 sha-determinism.** `EXPECTED`: *two runs over identical source **shas** differ ≥1 byte ⇒ REFUTED.*
  `test_f1_2_determinism_sort` asserts sidecar keys come out alphabetically **sorted** (`a` before `z`) —
  that is output-canonicalization, a different property; nothing runs-twice-over-shas-and-compares.
  **Covering test:** run extraction twice over an *identical sha-dict*, assert the two outputs are
  byte-identical (incl. the sha-derived staleness fields). (F-1.1 already covers in-memory run-equality;
  F-1.2 is the sha-keyed variant and is the one currently unguarded.)
- **F-3 staleness guard.** `EXPECTED`: *source mutated post-emit; the guard **fails to arm** ⇒ REFUTED.*
  `test_f3_staleness_guard` asserts the guard's output **fields are present** (`_staleness_guard`,
  `fake_sha`, `source_shas`) — presence, not behavior; it never mutates a source post-emit nor checks the
  guard fires. **Covering test:** emit, then change a source's sha, then assert the guard **arms** (detects
  the mismatch / halts or flags stale) — not just that the fields exist.

### Accept — 12 MET clean

F-1.1, F-2.1, F-2.2, F-2.3, F-6 (oracle/presence half — the Class-B *truth* is discipline-assumed, not
yours to test), F-7.1, F-7.2, F-7.3, F-7.4, F-8.1, F-8.2, F-8.3. Each test exercises its `EXPECTED`.

### Fit-refinements — 3 MET-weak (optional, non-blocking)

- **F-4** uses substring `in`, not byte-exact one-liner fidelity (whitespace drift would still pass).
- **F-5** shows the dyad isn't hardcoded (in-process param), not "a second substrate needs code-not-config."
- **F-8.4** exercises only the sidecar-dup half of "md-tag **or** sidecar" (the md-tag half overlaps F-2.2).

## Ask

Re-deliver F-1.2 and F-3 with the covering tests above (or contest the mapping with grounds — bond's
mapping is a judgment and is itself rubbable). The 12 MET stand; the 3 weak are yours to strengthen or
leave. No goalpost move: this is the pinned `EXPECTED`, read literally.

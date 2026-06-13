# Invariant-schema stress-tagging — findings (pre-lock, s15c gate-list input)

> **What:** the s15c pre-lock 10-invariant stress-tagging pass (Covalent's work; Operator scores only
> failures). **Why:** surface EXPRESSIBILITY gaps against schema **v0.8.2** *before* cairn binds the
> engine — so the gate-list dispositions (G2 + tag-architecture) are made on evidence, not guess.
> **How:** `python3 bin/invariant-eval.py dialectic/invariant-schema.yaml dialectic/invariants-stress.yaml`
> over 10 real bond invariants, each tagged HONESTLY (name the real seam; a fail is a finding, not a
> bug to shoehorn around). Mechanical truth = the eval output, reproduced below.
>
> **Sequencing note:** s15c scoped this "after (1)+(2)." Run NOW against the current schema it does the
> opposite job and the better one — it *generates the evidence the Operator needs to dispose* (1) and (2),
> rather than presupposing them. Nothing here depends on those gates being settled first.

## Run output (10 records, schema v0.8.2)
```
[PASS] bond:C1        [PASS] bond:C4        [FAIL] bond:D2 (trigger vocab)
[PASS] bond:D10       [PASS] bond:D11       [FAIL] bond:S2 (trigger vocab + lint)
[FAIL] bond:U1 (trigger vocab)              [PASS] bond:TENET
[PASS] bond:D12       [PASS] bond:S1
corpus: ⚑ DUTY-DETECTOR-MISMATCH bond:D10 · ⚑ DUTY-DETECTOR-MISMATCH bond:D11
gaps:   ◌ math.expression OPAQUE (form-not-truth, by design)
```
3 mechanical fails (one root cause), 2 census flags (both correct), 4 **silent** findings (pass
mechanically, wrong semantically — the dangerous class), 1 declared gap, 1 positive harness catch.

---

## Feeds gate-item (1) — G2 / the `act-attempt` sentinel

**Finding G2a — the registry has no act-conduct/act-attempt seam.** D2, S2, U1 all fail trigger-vocab
for the same reason: the `trigger` registry seeds are **situational** seams (`selection-seam`,
`stand-up`, `ratification`, `candidate-admission`, …), but a **prohibition or per-act rule** needs a
seam that names the **act itself** — *while falsifying* (D2), *when granting* (S2), *when composing a
turn* (U1). None exist. This is the gap s15c narrated as "act-bound prohibitions inexpressible," now
demonstrated across 3 records (and correctly: the original D6 sample failure was **not** an act-bound
prohibition — it's an `ONLY-AFTER` failing on the same missing-seam cause; minor ledger drift, noted below).

**Finding G2b — the lint actively fights per-act trigger names (S2 double-fire).** S2's honest seam
`permission-grant` triggers BOTH the vocab miss AND the `must-not-contain-action-token` lint (`grant`
is in `permission-grant`). So even if act seams were admitted to the registry, naming them after their
act would trip the lint. **→ This decides the shape of the G2 fix:** the sentinel must be **ONE
generic, action-neutral `act-attempt` trigger value**, with the specific verb carried in
`prescription.action` — NOT N per-act-named seams (those are doubly blocked). Recommend disposing G2 as:
add `act-attempt` to the trigger registry seed; the lint then passes because the seam name carries no verb.

## Feeds gate-item (2) — tag-architecture (inline-full vs sidecar-corpus)

**Finding TA1 — composite invariants truncate SILENTLY (D12, the worst kind).** ROM-UI carries two
trigger→action rules (stand-up: diff vs baseline; stand-down: set RESTART-PENDING on anchor edit). The
schema is **one-trigger-one-prescription**, so the stand-down half is simply dropped — **D12 PASSES with
no complaint.** A silent loss is more dangerous than a fail. **→ The sidecar-corpus must enforce
atomicity** (one rule per record; a composite is pre-decomposed into N records, e.g. `D12a`/`D12b`), and
the census should warn on a likely-composite one_liner. This is a point FOR sidecar-corpus over
inline-full: atomic tuple records are unreadable inline anyway (Covalent's standing lean).

---

## New gaps NOT on the gate-list (surfaced by the stress test — Operator dispose)

- **Finding M1 — no permissive modality (S1, SILENT).** The deontic vocab is obligation-only
  `[MUST, MUST-NOT, ONLY-BY, ONLY-AFTER]`. S1 is a **standing authorization** (the Agent *may* push/message
  without re-asking) — a permission, not a duty. It can only be tagged `MUST`, which **over-states it into
  an obligation** (and S1 PASSES, hiding the error). Same gap hits soft/defeasible duties (D3 reflection-
  form, D5 response-economy are *shoulds*, not *musts*). **→ Dispose:** add `MAY` (permission) and possibly
  `SHOULD` (defeasible) to the modality vocab, OR explicitly declare permissions/soft-duties out-of-scope
  (so they're rejected, not silently mis-typed).

- **Finding M2 — cardinality/rate inexpressible (U1, SILENT).** "≤1 [CTA] **per turn**" has no
  representation — no quantifier/rate field. Even with a turn-seam, the count is lost; U1's prohibition
  degrades to "MUST-NOT issue >1," dropping the "per turn" scope. **→ Dispose:** add an optional
  `cardinality`/`rate` field, or declare rate-constraints out-of-scope (and route them to MD-normative).

- **Finding M3 — descent-guard question on TENET (MD-normative, not mechanical).** `bond:TENET` tagged
  `form: mathematical` PASSES, but the measurements operationalize `g`/`v` only loosely ("a candidate
  proposed", "falsification survived" are presence-flags, not measured quantities). Per the schema's own
  descent-guard, the tenet floor may belong at `form: tuple` (or `slogan`), not `mathematical` — "1*g+1*v>2"
  may be a slogan in math notation. This is a practice-guard call, not an engine call — flagging for the
  MD-normative review, not for cairn.

## Positives (schema/harness working — bank, don't change)

- **Census duty-detector-mismatch VALIDATES content (D10, D11).** Both flagged correctly: the anti-cave
  duty (agent MUST manufacture grounds only the Operator can verify — `other-half-only`) and the
  distinctness duty (agent MUST resist a meld it cannot see — `unobservable-from-inside`) are genuinely
  un-self-verifiable. The census surfacing this is the schema earning its keep, and the flags *agree with*
  what D10/D11 say about themselves.
- **Fail-closed caught a real tagging slip.** I mis-tagged D12's `re_rub_triggers` with `anchor-edit` (a
  `trigger` value, not a `re_rub_trigger`); the evaluator rejected it. Minor ergonomics finding: the two
  trigger-named vocabularies (`trigger` vs `re_rub_trigger`) are confusable — worth a one-line note in the
  schema, not a structural change.
- **math.expression honestly declared OPAQUE** (form-not-truth) — the Goodhart/descent boundary holding.

## Ledger drift-note (Item-L adjacent, low-urgency)
s15c's "D6 FAILS = G2: act-bound prohibitions INEXPRESSIBLE" mischaracterizes D6 (an `ONLY-AFTER`, not a
prohibition; it fails on the missing-seam cause shared with D2/S2/U1). The act-bound-**prohibition** gap
is real but was first properly demonstrated here (D2/S2/U1), not by D6. Footnote at next schema edit.

## Disposition asks (Operator seat)
1. **G2** — add `act-attempt` (action-neutral) to the trigger registry; verb stays in `prescription.action`. [Y/N/alt]
2. **Tag-architecture** — sidecar-corpus + atomicity rule (composites pre-decomposed; census warns). [confirm sidecar]
3. **M1 permissive modality** — add `MAY`(+`SHOULD`?) or declare permissions/soft-duties out-of-scope. [pick]
4. **M2 cardinality** — add a `rate` field or declare out-of-scope. [pick]
5. **M3 TENET form** — keep `mathematical` or descend to `tuple`/`slogan`. [MD-normative call]

---

## Rub + implementation (2026-06-13 cont. — Operator `rub:` → claims, then `riff:` → one_liner-atomicity)

**The rub demoted the headline.** A relocation test (`/tmp/relocate-test.yaml` → 3/3 PASS, exit 0) showed
the 3 mechanical fails were my **over-precise tagging**, not inexpressibility — D2/U1a/S2 all pass when
relocated to existing situational seams. Rubbed claim verdicts (full C-E-C in the session record):
- **A (STRONG)** — the schema is expressibility-robust; almost everything relocates to a green pass.
- **B (MEDIUM-HIGH, the real risk)** — the binding pre-lock risk is **schema-level counterfeit-green**:
  the engine validates FORM-not-TRUTH, so a mis-located-but-well-formed tag (a self-grant tagged
  `outward-publish`) goes green. → the load-bearing gate-list move is enforcing the **tagging-time review**
  (already the schema's declared residue: trigger-equivalence = G + Operator), not the mechanical G2 token.
- **C (MEDIUM, narrow)** — the only genuine act-seam gap is acts with no natural situation (self-grant):
  faithful naming is lint-blocked, every situational home is semantically wrong. **Sharpening:** the MD
  *already* declares "act-bound prohibitions derive trigger ≝ attempt-context" (v0.4) — the YAML registry
  just lacks that generic token → it's an **MD/YAML mismatch**, fixable by adding one `act-attempt` seam.
- **D (HIGH, the strongest survivor)** — cardinality/rate genuinely inexpressible (`U1a` "≤1 per turn");
  live fork = add a field vs declare out-of-scope (Covalent lean: out-of-scope — it's a U-law).
- **E (DEMOTED, MEDIUM-LOW)** — permissions dualize to `MUST-NOT(complement)`; inergonomic, not inexpressible.
- **F (IMPLEMENTED below)** — composite silent-truncation → solved by atomic decomposition + the lint.
- **G (STRONG positive)** — census `DUTY-DETECTOR-MISMATCH` validates D10/D11's own content.
- **H (instrument-validity, HIGH)** — n=1 primed tagger; treat the claim-set as illustrative, not exhaustive.

**Implemented — `one_liner-atomicity` survivor** (`invariant-schema.md` v0.8.3): a one_liner is one
declarative assertion = **one breach-condition**; co-equal assertions split into records, qualifiers/tells
move to fields. The corpus (`invariants-stress.yaml`) is now **decomposed 10 → 16 atomic records** (C1's
two collapse-modes; the DFD's four clauses → `DFD` + `U1a/b/c`; D12's two phases → `D12a/D12b`), with a
**richer grounding-graph** (C1 → C1-ionic → D10; C1 → C1-meld → D11; DFD → U1a/b/c). The evaluator gains a
**non-failing `ONE-LINER-COMPOSITE` advisory** (`;` heuristic). Verified: decomposed corpus = 0 composite
flags (atomic); the old compound sample flags 4 (C1/SUMMIT/D6/TS-6), ORI-C3 correctly clean. The 3 G2
fails + 2 census flags are **left honest** — they surface the open gate-items, not bugs.

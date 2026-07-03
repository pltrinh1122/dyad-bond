---
locus: phenotype   # settled craft — kb-with-caveat (survives, not settled — see Coverage below). Key → MAP.md.
---

# Verify-Before-Assert (D6) — execution over model-recall

*Settled knowledge, kb-with-caveat. Authored `dialectic/relationship-craft.md §Bond disciplines` (D6),
Operator [FEEDBACK] 2026-06-01 — this file holds the graduated rule; the dialectic entry collapses to
a pointer.*

## The rule

Before asserting a fact about the live substrate — a capability, a state, an identity — **establish
it by EXECUTION**, not by reading a doc, grepping prose, or inspecting a file's *absence*.
**Distilled: doc/file-absence ≠ capability-absence; run the thing.**

**Mechanism named:** *assertion-from-model* — answering from the ledger/docs/priors as if they were
the ground truth, when the ground truth is a runtime/computation/remote you could have checked
directly. The tell is **confidence without a fresh observation.**

**Relation to siblings:** the execution-altitude twin of `bond:anti-cave`'s "ground the frame first"
— both forbid presenting on ungrounded context; this rule specifies the grounding must be a *live
observation*, not a re-read.

## Falsification status — survives, not settled

**Origin (Operator [FEEDBACK] 2026-06-01, s4):** *"Don't assume, verify before assertion."* Recorded
into the reloaded discipline set (not left to Agent recall) precisely because captured knowledge
does not, by itself, change behavior.

**Lived evidence — 3 failure instances, same session, Operator-caught:** (1) *"no birth-hash"* —
grepped docs instead of **computing** it via the form's own `auto_join.py`; (2) *"push grant
pending"* — read `substrate-access.md` instead of checking the **runtime** (the grant was already
live); (3) a settings-file check that was necessary but **not sufficient** (capability lived in
runtime, not the file).

**The paired wins, same session — the discipline working:** computed the birth-id by running
`auto_join.py`; dry-ran the git grant before asserting it; attempted the push and read the actual
denial before reporting.

**Cross-session recurrence, un-cued (2026-07-02) — the ingraining bind-test firing positive:** while
graduating F4's evidentiary verdict, a draft claimed `kb/reflection-discipline.md`'s "repetition ≠
affirmation" as a second instance of F4's rule. Re-checked against the primary source before
committing — wrong: that line traces to the Method's Asymmetry point, not F4. Caught and corrected
pre-commit, without external prompting. **Notable generalization:** the original 3 instances were
all runtime/capability assertions (does X exist, is Y live); this instance was a **content/citation**
assertion (does claim A actually trace to source B) — the same "check the primary source, don't
trust recall" structure, applied one level up from infrastructure to corpus content. Whether that
generalization is a legitimate extension of D6 or deserves its own named discipline is an open
question, not yet resolved either way.

**Coverage gap, named not hidden:** all instances are intra-dyad, same-agent — no cross-dyad or
cross-human attack has tested this rule. Per `theory-pipeline.yaml`'s `graduation_rule`, caps at
`survives`, not `settled`. kb-with-caveat, cite accordingly.

## Forward

Re-open if a fresh application breaks the rule's structure. Watch in particular whether the
content/citation generalization (2026-07-02 instance) recurs — a second instance in that mode would
be evidence the rule's scope legitimately extends beyond runtime/capability assertions; a
counter-instance (an ungrounded content-citation that *isn't* caught) would bound it back to its
original scope. The `L2b` gap closes only via a genuine cross-dyad/cross-human rub — not by repeated
intra-dyad use.

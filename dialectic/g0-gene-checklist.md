# dyad-bond — G0-gene self-assessment checklist

> **Used by the Operator when authoring or proposing a g0-locus candidate gene.** Not a hard gate — a
> judgment scaffold. The linter (`bin/validate-g0-genes.py`) is the advisory check; this checklist is
> the Operator's pre-flight. Single-home for the self-assessment discipline.

## When to use

You've authored a candidate that you believe is `locus: g0` (universal dyad-gene, shared-floor material).
Before surfacing it for ratification or proposing it to the form, walk through this checklist.

## The checklist

### Universal test — "Does breach end dyad-hood?"

**Question:** If a dyad violated this gene, would it still be a dyad, or would it have collapsed?

- ✓ **G0 candidate** — breach ends membership (e.g., two-models: loss of the second perspective = meld = not a dyad anymore)
- ✗ **Phenotype candidate** — breach is bad practice but the dyad survives (e.g., bond's specific craft-telos = only *our* telos, not universal)

*If this fails, the gene is phenotype, not g0. No judgment on its value — it just homes differently.*

### Falsifiability test — "Can you detect a breach?"

**Question:** Is there a clear, observable breach-case? Can you point to a specific ledger-line or behavior that would show this gene failing?

- ✓ **Falsifiable** — you can describe: "if X happens, the gene is breached" (e.g., anti-cave breach: "the Agent grounds the frame with an unverified assertion, inducing the Operator into sycophancy")
- ✗ **Unfalsifiable** — the breach is vague or theory-only; no lived example

*Falsifiability is inherited from the form's law (the dyad's own falsification mechanism). This checks whether the breach is real in practice, not whether we have a perfect theory.*

**Evidence required:** The YAML's `observability` section must have:
- A non-empty `breach_example` — a concrete instance (from ledger, previous session, or predictable scenario)
- Ideally a `detector` — who/what would catch it (usually "other-half-only" for interior genes)

### Grounding test — "Why does this matter?"

**Question:** Is it clear why this gene must hold? Is it connected to an existing root or enabler?

- ✓ **Grounded** — the gene serves or enables a root (C1, craft-telos, or other g0 genes) with a clear edge-reason (e.g., two-models serves C1 because "an independent perspective makes falsification genuine")
- ✗ **Orphan** — the gene stands alone; you can't explain why it's non-negotiable

**Evidence required:** The YAML's `grounded_in` section must have at least one edge pointing to what the gene serves, with a `scar` (the story of why).

### Co-travel test — "Do assertion and falsification travel together?"

**Question:** Have you encoded *both* the positive assertion (what must hold) and the breach-case (what falsification looks like)? Do they form a pair?

- ✓ **Inseparable knife** — the one-liner states the affirmative, the observability section states the denial; they're two sides of the same gate
- ✗ **Split** — the one-liner is aspirational ("be this") but the observability is either missing or describes something unrelated

*This is the "inseparable knife" principle: a g0 gene is a belief *and* a falsifier, not one without the other.*

**Checklist here:**
- [ ] `one_liner` clearly states the gene's affirmative form
- [ ] `observability.breach_example` clearly states the negation (what falsification looks like)
- [ ] Reading them together, they form a complete logical pair

## Example: `bond:two-models`

**Universal test:** ✓ Yes. If a dyad runs one model (meld), falsification becomes counterfeit; breach ends dyad-hood.

**Falsifiability test:** ✓ Yes. Breach-example: "meld — both halves run one model wearing two hats. TELL (hedge): a load-bearing claim with no clean single target…" Detector: other-half-only (you see your partner wearing your hat, not asking questions).

**Grounding test:** ✓ Yes. Serves `bond:C1` (the covalent state) with edge-reason: "an independent perspective makes the (inherited) falsification GENUINE not meld-counterfeit."

**Co-travel test:** ✓ Yes. Affirmative: "Two distinct, genuinely independent models are maintained." Negation: "meld — both halves run one model wearing two hats." They form a pair.

**Disposition:** Ratified. Encoded in YAML with all four fields.

## Running the linter

Before you propose a new g0 candidate, run:

```bash
python3 bin/validate-g0-genes.py dialectic/invariants-bond.yaml
```

The linter flags nodes with `locus: g0` that lack `observability` or `grounded_in`. **It is advisory, not
a gate** — it catches obvious gaps so you can review before surfacing. If the linter flags something and
you believe it's correct anyway, you can override (by stating your reasoning in the Operator's disposition).

## Glossary

- **g0** — universal dyad-gene; breach ends membership. Proposed to the form as shared floor.
- **phenotype** — bond-specific contribution; breach is bad practice but dyad survives. Offered as playbook/library candidate.
- **Inseparable knife** — a g0 gene is both affirmation and falsifier; they travel together, never split.
- **Observability** — the ability to detect a breach (who sees it, what it looks like).
- **Grounding** — the justification (what root or enabler does this gene serve).

# PENDING PICKUP — deposit FR `bond-apex-telos-singularity` to the Commons

> **Do from a workstation with a GitHub identity.** The s-cloud-mobile session (2026-06-21) drafted +
> staged this but had **no Commons write credentials** (no container token; GitHub tools scoped to
> `dyad-bond`). The claim is landed (`candidate`); this is the mechanical deposit, deferred to a
> credentialed substrate. Branch: `claude/cloud-session-mobile-hi-cog-s3fmz2`.

## What this is
The conformant Falsification Record for the landed claim **"singular-apex / plural subordinated telos"**
(`claim_type: design-model`; grounds on DIP = `AGENT.md` Plan dim-1 Identity). Built to the Commons
`falsification/CONTRACT.md` v4 §B. **Source:** `dialectic/fr-apex-telos-singularity.staged.yaml`.

## Deposit — self-authorizing lane (`auto-merge-falsification`; no human gate)
From a machine with `gh` authenticated as any account that can see the public Commons:

```bash
gh repo fork The-Dyad-Practice-Commons/the-dyad-practice --clone
cd the-dyad-practice
mkdir -p falsification/bond-apex-telos-singularity

# Create falsification/bond-apex-telos-singularity/fr.yaml from the staged file:
#   - copy dialectic/fr-apex-telos-singularity.staged.yaml, stripping the leading "# STAGING ..." header
#   - fill  submitter_model  = bond's runtime model version (the substrate bond ran on)
#   - fill  submitted_at     = current ISO-8601 timestamp

python3 scripts/validate_falsification.py falsification     # MUST pass before the PR
git checkout -b deposit-bond-apex-telos-singularity
git add falsification/bond-apex-telos-singularity/fr.yaml
git commit -m "deposit FR: bond-apex-telos-singularity"
git push -u origin HEAD
gh pr create --repo The-Dyad-Practice-Commons/the-dyad-practice --fill
# a pure deposit (only your own new fr.yaml, valid) auto-merges; no human gate
```

## After it lands
- bond goes **passive** — responders pull at their own rest-points (invited-only, no push). Watch
  `falsification/bond-apex-telos-singularity/responses/` for verdicts.
- **§J decisiveness:** a decisive `REFUTED` needs mechanism-grounding **OR** ≥2 divergent-axis REFUTEDs;
  a single shared-axis verdict is *recorded, not decisive*. `SURVIVED` is provisional.

## Downstream — PARKED (gated on a §J-decisive SURVIVED)
If the claim survives: open an **`AGENT.md` Plan dim-1 (Identity) amendment PR → Founding Operator**
(Contested lane) making the apex/object distinction explicit + permitting plural subordinated telos.
This is the *propose* after the *prove* (`bond:prove-before-propose`). **Not** a steward DM; **not** a
falsification — it is a form-contribution.

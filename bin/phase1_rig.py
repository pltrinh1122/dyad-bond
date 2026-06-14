#!/usr/bin/env python3
"""bin/phase1_rig.py — Phase-1 generator-rig (Operator dispose 2026-06-14).

QUESTION: does IV (invariant WITHOUT intent-grounding) produce as reliably as
IV_it (invariant grounded-on-intent)?

This is a RIG, not an engine: it reuses bin/invariant-eval.py as the reference
evaluator (commissioner's Validate-half) and only does the experiment's two acts —
(1) derive the IV arm by stripping `grounded_in` from every non-root record;
(2) run both arms and diff, isolating the marginal mechanical footprint of grounding.

Deterministic by construction (Phase-1 criterion): same corpus -> same diff.

Usage: python3 bin/phase1_rig.py [dialectic/phase1-corpus.yaml]
Exit: 0 always (the diff IS the finding; non-zero eval is expected on the IV arm).
"""
import sys, subprocess, tempfile, os, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(os.path.dirname(HERE), "dialectic", "invariant-schema.yaml")
EVAL = os.path.join(HERE, "invariant-eval.py")
try:
    import yaml
except ImportError:
    sys.exit("FATAL: pyyaml required (rig reuses the reference harness)")


def run_eval(corpus_path):
    r = subprocess.run([sys.executable, EVAL, SCHEMA, corpus_path],
                       capture_output=True, text=True)
    return r.stdout, r.returncode


def strip_grounding(corpus):
    """IV arm: remove intent-grounding from non-roots. Returns (new_corpus, n_stripped)."""
    n = 0
    for rec in corpus["invariants"]:
        if not rec.get("root") and "grounded_in" in rec:
            del rec["grounded_in"]
            n += 1
    return corpus, n


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(HERE), "dialectic", "phase1-corpus.yaml")
    it_corpus = yaml.safe_load(open(src))
    iv_corpus, n_stripped = strip_grounding(yaml.safe_load(open(src)))

    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        yaml.safe_dump(iv_corpus, f, sort_keys=False)
        iv_path = f.name

    it_out, it_rc = run_eval(src)
    iv_out, iv_rc = run_eval(iv_path)
    os.unlink(iv_path)

    print("=" * 72)
    print(f"PHASE-1 RIG | IV (no intent-grounding) vs IV_it (grounded) | stripped {n_stripped} non-roots")
    print("=" * 72)
    print(f"\n--- IV_it arm (grounded)   exit={it_rc} ---\n{it_out}")
    print(f"--- IV arm (stripped)      exit={iv_rc} ---\n{iv_out}")

    diff = list(difflib.unified_diff(
        it_out.splitlines(), iv_out.splitlines(),
        fromfile="IV_it (grounded)", tofile="IV (stripped)", lineterm=""))
    print("=" * 72)
    print("MARGINAL MECHANICAL FOOTPRINT OF INTENT-GROUNDING (diff IV_it -> IV):")
    print("=" * 72)
    for line in diff:
        print(line)
    # Headline: every changed line should be grounding/termination — NOT breach/conflict/detector.
    changed = [l for l in diff if l and l[0] in "+-" and not l.startswith(("+++", "---"))]
    grounding_words = ("grounded_in", "TERMINATION", "ORPHAN", "FAIL", "PASS")
    off_grounding = [l for l in changed
                     if not any(w in l for w in grounding_words)]
    print("\n=== FINDING ===")
    print(f"changed lines: {len(changed)} | touching breach/conflict/detector (NOT grounding): "
          f"{len(off_grounding)}")
    if not off_grounding:
        print("  -> intent-grounding's ENTIRE mechanical footprint is graph-termination.")
        print("  -> IV is byte-identical to IV_it on every breach/conflict/detector check.")
    else:
        print("  -> grounding ALSO moved a non-termination check (investigate):")
        for l in off_grounding:
            print(f"     {l}")
    sys.exit(0)

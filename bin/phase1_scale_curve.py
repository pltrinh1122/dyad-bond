#!/usr/bin/env python3
"""bin/phase1_scale_curve.py — Phase-1 consistency vs INPUT SCALE (Operator dispose 2026-06-14: "Y. lean").

Controls consistency for input scale, the missing control: a single point doesn't characterize a target.
  L1 single-line  = the tenet line (under-determined — the non-negotiable must be EXTRAPOLATED)
  L2 multi-line   = §Identity (carries the "sharing not transfer, distinct not merged" near-statement)
  L3 complete     = stripped DYAD.md (§NON-NEGOTIABLE removed) — the over-determined end
Task = IV only (ungrounded non-negotiable extraction) — the lean probe of the curve's SHAPE before the
full 4-condition × 3-scale grid. Excerpts derived FROM DYAD.md (single-home, not re-authored).

PREDICTION (pre-registered): consistency RISES L1->L3 (under-determined -> over-determined).
Refuted-if flat or falling.
CAVEAT: scale here entangles length with NN-signal content (L1 lacks the near-statement L2/L3 carry) ->
the x-axis is consistency-vs-DETERMINATION, not vs raw length.
"""
import os, sys, re, itertools, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g_consistency_rig as R

MODEL, N = "claude-haiku-4-5-20251001", 5


def extract_section(doc, heading):
    out, grab = [], False
    for ln in doc.splitlines():
        h = re.match(r"^(#{1,6})\s+(.*)", ln)
        if h:
            if heading.lower() in h.group(2).lower():
                grab = True
                continue
            if grab and len(h.group(1)) <= 2:
                break
        if grab:
            out.append(ln)
    return "\n".join(out).strip()


def consistency(outs, emb):
    vecs = list(emb.encode(outs))
    ps = [R.cos(vecs[i], vecs[j]) for i, j in itertools.combinations(range(len(vecs)), 2)]
    lex = R.mean_pairwise(lambda a, b: len(a & b) / len(a | b) if (a | b) else 1.0,
                          [R.content_tokens(o) for o in outs])
    return {"cos_mean": round(st.mean(ps), 3), "cos_min": round(min(ps), 3),
            "cos_max": round(max(ps), 3), "cos_std": round(st.pstdev(ps), 3), "lexical": round(lex, 3)}


if __name__ == "__main__":
    doc = open("DYAD.md").read()
    L1 = next(l for l in doc.splitlines() if "1+1=3 through Generate" in l).strip("- *> ")
    scales = [("L1 single-line", L1),
              ("L2 multi-line(§Identity)", extract_section(doc, "Identity")),
              ("L3 complete-stripped", R.strip_heading(doc, "NON-NEGOTIABLE"))]
    emb = R.load_embedder()
    print(f"=== Phase-1 consistency vs scale | IV (ungrounded) | model={MODEL} | N={N} ===")
    print("=== prediction: cos_mean RISES L1->L3 (under- -> over-determined) ===\n")
    curve = []
    for name, text in scales:
        outs = [R.call_engine(R.NN_TASK + text, MODEL) for _ in range(N)]
        for i, o in enumerate(outs):
            print(f"  [{name} {i+1}] {o}", file=sys.stderr)
        m = consistency(outs, emb)
        curve.append((name, len(text), m))
        print(f"--- {name:26s} input={len(text):5d} chars | cos_mean={m['cos_mean']} "
              f"(min={m['cos_min']} max={m['cos_max']} std={m['cos_std']}) | lexical={m['lexical']} ---")
    means = [m["cos_mean"] for _, _, m in curve]
    rises = means == sorted(means)
    print(f"\n=== CURVE cos_mean = {means} | rises L1->L3? {rises} "
          f"({'prediction held' if rises else 'PREDICTION REFUTED — investigate'}) ===")

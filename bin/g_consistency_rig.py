#!/usr/bin/env python3
"""bin/g_consistency_rig.py — G-task CONSISTENCY + VALIDITY rig, v4 (Operator riff 2026-06-14).

v4 extends the rig per Operator riff: (1) input scales from a single sentence to a whole document
(--input, e.g. DYAD.md); (2) the G task / intent = "extract ONLY the non-negotiable"; (3) a manually-
authored gold invariant is ingested programmatically to give a VALIDITY measure (cosine-to-gold),
not just consistency (cosine across runs). Gold defaults to canonical bond:C1 (single-home; do NOT
re-author the non-negotiable — use the existing canonical text).

CONSISTENCY (precision)  = mean pairwise cosine across the N extractions.
VALIDITY    (accuracy)   = mean cosine(extraction_i, gold).   ⚠ SEE BREAK BELOW.

⚠⚠ DEMONSTRATED — cosine VALIDITY is BROKEN for the non-negotiable (a deontic target):
    faithful extraction      cos-to-gold 0.66
    HARD inversion (opposite) cos-to-gold 0.645   <- TIED with faithful. cosine can't tell them apart.
    soft inversion            cos-to-gold 0.503
  The non-negotiable is a prohibition; cosine is negation-blind, so validity-to-gold cannot
  distinguish a faithful extraction from its negation. The advisory polarity guard helps ONLY on
  explicit "must not / never" inversions and MIS-READS the gold's own "no collapse / only by"
  phrasing as affirmative -> a valid measure here needs deontic-semantic structure (NOT cosine, NOT
  a one-bit regex), which collides with the "no template/structure acting as invariants" rub. OPEN.

Also retained: generator = independent `claude -p`; consistency = PRECISION not VALIDITY; absolute
cosine is anisotropy/temperature-inflated (only cross-arm DELTA reads).
CONFOUND (retrieval vs generation): if --input contains the non-negotiable VERBATIM-LABELLED (DYAD.md
has a `## NON-NEGOTIABLE` header), extraction degenerates to COPYING -> inflated consistency+validity,
measuring retrieval not generative G. To test G, strip the label / use a doc where it must be inferred.

DEP: pip install model2vec. Usage: python3 bin/g_consistency_rig.py --input DYAD.md --n 10 --arm both
"""
import sys, os, json, subprocess, argparse, re, itertools

SITUATION = ("An agent is about to state a fact about its development environment — which tools exist, "
             "what a file contains, what the platform supports — based on its own prior belief.")
SINGLE_TASK = ("In one or two sentences of plain prose, state the rule that should govern whether the "
               "agent may assert that fact. Output only the rule, no preamble.")
NN_TASK = ("From the document below, extract ONLY the non-negotiable — the single rule the dyad guards "
           "hardest — as one or two sentences of plain prose. Output only the rule, no preamble.\n\n")
INTENT_CLAUSE = (" The extraction should serve this intent: surface the one constraint whose breach "
                 "collapses the dyad, tested as hard as any other claim.")
# canonical bond:C1 one_liner (the manually-authored gold; single-home — ingested, not re-created)
GOLD_DEFAULT = ("Keep the bond covalent: every candidate, including the Operator's premises, enters the "
                "shared model only by surviving genuine falsification; no ionic or meld collapse; easy "
                "agreement means test hardest.")
STOP = set("a an the of to in on for and or but is are be by that this it its as at with from into "
           "whether may must should not no only if then than which who whom what when where".split())
PROHIBITIVE = re.compile(r"\b(must not|may not|shall not|cannot|can't|do not|don't|never|forbid|prohibit)\b", re.I)


def call_engine(prompt, model):
    r = subprocess.run(["claude", "-p", prompt, "--output-format", "json", "--model", model],
                       capture_output=True, text=True, timeout=600)
    try:
        return json.loads(r.stdout).get("result", "").strip()
    except json.JSONDecodeError:
        return ""


def content_tokens(text, extra=frozenset()):
    return {t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP and t not in extra}


def mean_pairwise(score, items):
    pairs = list(itertools.combinations(range(len(items)), 2))
    return round(sum(score(items[i], items[j]) for i, j in pairs) / len(pairs), 3) if pairs else 1.0


def load_embedder():
    try:
        from model2vec import StaticModel
    except ImportError:
        sys.exit("FATAL: pip install model2vec")
    return StaticModel.from_pretrained("minishlab/potion-base-8M")


def cos(a, b):
    d = (a @ a) ** 0.5 * (b @ b) ** 0.5
    return float(a @ b / d) if d else 1.0


def polarity(text):
    return "prohibitive" if PROHIBITIVE.search(text) else "affirmative"


def run_arm(arm, n, model, embedder, doc, gold_vec, gold_pol):
    if doc is not None:
        prompt = (NN_TASK + doc) + ("" if arm == "ungrounded" else INTENT_CLAUSE)
    else:
        prompt = SITUATION + ("" if arm == "ungrounded" else INTENT_CLAUSE) + "\n\n" + SINGLE_TASK
    ptoks = content_tokens(prompt)
    outs = [call_engine(prompt, model) for _ in range(n)]
    for i, o in enumerate(outs):
        print(f"  [{arm} {i+1}/{n}] {len(o)} chars", file=sys.stderr)
    vecs = list(embedder.encode(outs))
    consistency = mean_pairwise(cos, vecs)
    lexical = mean_pairwise(lambda a, b: len(a & b) / len(a | b) if (a | b) else 1.0,
                            [content_tokens(o, ptoks) for o in outs])
    pol = {polarity(o) for o in outs}
    validity = round(sum(cos(v, gold_vec) for v in vecs) / len(vecs), 3)
    pol_match = round(sum(polarity(o) == gold_pol for o in outs) / len(outs), 3)
    return {"consistency": consistency, "lexical": lexical, "polarity_split": len(pol) > 1,
            "validity_cos": validity, "validity_polmatch": pol_match, "outs": outs}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="document to extract the non-negotiable from (e.g. DYAD.md)")
    ap.add_argument("--gold", help="gold reference: a file path, or omitted for canonical bond:C1")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--arm", choices=["ungrounded", "grounded", "both"], default="both")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    doc = open(a.input).read() if a.input else None
    gold = open(a.gold).read() if (a.gold and os.path.exists(a.gold)) else GOLD_DEFAULT
    emb = load_embedder()
    gold_vec = list(emb.encode([gold]))[0]
    gold_pol = polarity(gold)
    arms = ["ungrounded", "grounded"] if a.arm == "both" else [a.arm]
    print(f"=== G rig v4 | input={a.input or '<single-text>'} | model={a.model} | N={a.n} | arms={arms} ===")
    print("=== CONSISTENCY=precision (cosine across runs) | VALIDITY=cosine-to-gold ===")
    print(f"=== ⚠ VALIDITY is DEMONSTRATED-BROKEN for the non-negotiable: a HARD inversion ties the")
    print(f"===   faithful extraction (0.645 vs 0.66). gold polarity(regex)={gold_pol!r} (likely mis-read).")
    print("===   consistency=precision NOT validity; cosine negation-blind; only cross-arm delta reads.\n")
    res = {}
    for arm in arms:
        r = run_arm(arm, a.n, a.model, emb, doc, gold_vec, gold_pol)
        res[arm] = r
        warn = "  ⚠POLARITY-SPLIT" if r["polarity_split"] else ""
        print(f"--- {arm}: consistency={r['consistency']} lexical={r['lexical']} "
              f"validity_cos={r['validity_cos']} validity_polmatch={r['validity_polmatch']}{warn} ---")
        if a.show:
            for k, o in enumerate(r["outs"]):
                print(f"    [{k+1}] {o}")
        print()
    if len(res) == 2:
        dc = round(res["grounded"]["consistency"] - res["ungrounded"]["consistency"], 3)
        dv = round(res["grounded"]["validity_cos"] - res["ungrounded"]["validity_cos"], 3)
        print(f"=== DELTA consistency={dc:+} | DELTA validity_cos={dv:+}  "
              f"(validity delta UNTRUSTWORTHY per the negation break above) ===")

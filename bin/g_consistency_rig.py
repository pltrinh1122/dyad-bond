#!/usr/bin/env python3
"""bin/g_consistency_rig.py — G-task CONSISTENCY rig, v3 (Operator dispose 2026-06-14).

Phase-1 intent (Operator): consistency, measured by COSINE SIMILARITY. This rig generates
free-text rules (no template — v1's schema template was refuted as an invariant-set) and scores
consistency as mean pairwise cosine of sentence embeddings.

DEPENDENCY: `pip install model2vec` (static embeddings, ~30MB, no torch; downloads
'minishlab/potion-base-8M' from the HF hub on first use). Lexical Jaccard is computed too as a
judge-free surface contrast.

⚠ DEMONSTRATED BREAK — NEGATION-BLINDNESS (verified on this exact model):
    "agent MUST verify"  vs  "agent MUST NOT verify"  ->  cosine 0.995  (ABOVE a true paraphrase 0.869).
Cosine cannot see deontic polarity. So if the N outputs disagree on polarity (must vs must-not),
the cosine consistency number is CORRUPTED (opposite rules read as maximally consistent). This rig
emits an ADVISORY polarity-split flag (crude regex, surface-negation only — itself imperfect:
"must not assert without verifying" ≡ "must verify", so it can false-flag). When polarity splits,
DISTRUST the cosine number. A real polarity guard is an open Operator fork (see g-consistency-rig.md).

Still true: generator = independent `claude -p` sub-agent (fresh session/run = isolation);
manipulated variable = intent-grounding (minimal-contrast); only cross-arm DELTA is interpretable
(absolute cosine is anisotropy-inflated + temperature-dependent). CONSISTENCY = PRECISION, NOT
VALIDITY — even semantic consistency answers "do the runs MEAN the same," never "is it correct."

Usage: python3 bin/g_consistency_rig.py --n 10 --arm both --model claude-haiku-4-5-20251001
"""
import sys, json, subprocess, argparse, re, itertools

SITUATION = (
    "An agent is about to state a fact about its development environment — which tools exist, "
    "what a file contains, what the platform supports — based on its own prior belief.")
TASK = ("In one or two sentences of plain prose, state the rule that should govern whether the agent "
        "may assert that fact. Output only the rule, no preamble, no list, no headings.")
INTENT_CLAUSE = (" The rule should serve this intent: keep the agent empirically honest — it must not "
                 "assert from its internal model when the world can be cheaply queried.")
STOP = set("a an the of to in on for and or but is are be by that this it its as at with from into "
           "whether may must should not no only if then than which who whom what when where".split())
PROHIBITIVE = re.compile(r"\b(must not|may not|shall not|cannot|can't|do not|don't|never|forbid|prohibit|without first)\b", re.I)


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
        sys.exit("FATAL: pip install model2vec  (static embeddings for cosine; see module docstring)")
    return StaticModel.from_pretrained("minishlab/potion-base-8M")


def cos(a, b):
    d = (a @ a) ** 0.5 * (b @ b) ** 0.5
    return float(a @ b / d) if d else 1.0


def run_arm(arm, n, model, embedder):
    prompt = SITUATION + ("" if arm == "ungrounded" else INTENT_CLAUSE) + "\n\n" + TASK
    ptoks = content_tokens(prompt)
    outs = []
    for i in range(n):
        o = call_engine(prompt, model)
        outs.append(o)
        print(f"  [{arm} {i+1}/{n}] {len(o)} chars", file=sys.stderr)
    vecs = list(embedder.encode(outs))
    cosine = mean_pairwise(cos, vecs)
    lexical = mean_pairwise(lambda a, b: len(a & b) / len(a | b) if (a | b) else 1.0,
                            [content_tokens(o, ptoks) for o in outs])
    polarities = {"prohibitive" if PROHIBITIVE.search(o) else "affirmative" for o in outs}
    return {"cosine": cosine, "lexical": lexical, "polarity_split": len(polarities) > 1,
            "polarities": polarities, "outs": outs}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--arm", choices=["ungrounded", "grounded", "both"], default="both")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    arms = ["ungrounded", "grounded"] if a.arm == "both" else [a.arm]
    print(f"=== G-consistency rig v3 | model={a.model} | N={a.n} | arms={arms} ===")
    print("=== PRIMARY: cosine (semantic). Absolute = anisotropy/temp-inflated; only cross-arm DELTA reads.")
    print("=== ⚠ cosine is NEGATION-BLIND (must vs must-not -> ~0.995). polarity_split=True => DISTRUST cosine.")
    print("=== consistency = PRECISION, not validity ===\n")
    emb = load_embedder()
    res = {}
    for arm in arms:
        r = run_arm(arm, a.n, a.model, emb)
        res[arm] = r
        warn = "  ⚠ POLARITY-SPLIT: cosine CORRUPTED" if r["polarity_split"] else ""
        print(f"--- arm={arm} | cosine={r['cosine']} | lexical={r['lexical']} | "
              f"polarities={r['polarities']}{warn} ---")
        if a.show:
            for k, o in enumerate(r["outs"]):
                print(f"    [{k+1}] {o}")
        print()
    if len(res) == 2:
        d = round(res["grounded"]["cosine"] - res["ungrounded"]["cosine"], 3)
        corrupt = res["grounded"]["polarity_split"] or res["ungrounded"]["polarity_split"]
        print(f"=== DELTA cosine (grounded - ungrounded) = {d:+}"
              f"{'  ⚠ a polarity-split arm makes this delta UNTRUSTWORTHY' if corrupt else ''} ===")

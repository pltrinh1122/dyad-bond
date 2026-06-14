#!/usr/bin/env python3
"""bin/g_consistency_rig.py — G-task CONSISTENCY rig, v2 (Operator rub 2026-06-14).

v1 REFUTED by Operator rub: "free text is fine but not into a template/structure which
effectively act as invariants." v1 extracted into a schema (closed vocabs + fixed fields) —
a template that IS an invariant-set. Measuring templated output measured the TEMPLATE's
constraint, not the GENERATOR's consistency, and baked the construct-under-study (invariants)
into the apparatus. v2: the G task emits FREE TEXT; consistency is measured on the free text.

The unavoidable consequence (named, not hidden): free-text consistency needs a similarity
oracle, and every oracle is biased. This rig uses the LEXICAL/SURFACE floor — mean pairwise
token-Jaccard — which is fully mechanical and judge-free but PARAPHRASE-BLIND (synonymous
restatements score as inconsistent). It measures SURFACE consistency only. Semantic
consistency (embedding/judge) is a separate, Operator-disposed escalation — NOT in this file.

Still holds from v1: generator = independent `claude -p` sub-agent (fresh session/run =
isolation); generator is NOT the experimenter. Manipulated variable = intent-grounding
(minimal-contrast: grounded arm appends exactly one intent clause). Delta = lexical-
consistency(grounded) - lexical-consistency(ungrounded). Temperature unsettable via CLI ->
only cross-arm delta is interpretable, not the absolute number.

NAMED RESIDUAL BIASES of the lexical floor:
  * paraphrase-blind (under-counts semantic consistency);
  * boilerplate-gameable (a generator repeating filler scores HIGH — verbosity inflates overlap);
  * prompt-echo inflation (shared prompt vocabulary appears in all outputs) -> we strip a
    stopword set AND the prompt's own content tokens before scoring (place-and-bounded choice).
  * STILL precision, NOT validity. A consistent G can be consistently wrong.

Usage: python3 bin/g_consistency_rig.py --n 10 --arm both --model claude-haiku-4-5-20251001
"""
import sys, json, subprocess, argparse, re, itertools

# --- pinned experiment material (the place-and-bounded experimenter-authored locus) ---
SITUATION = (
    "An agent is about to state a fact about its development environment — which tools exist, "
    "what a file contains, what the platform supports — based on its own prior belief."
)
TASK = ("In one or two sentences of plain prose, state the rule that should govern whether the agent "
        "may assert that fact. Output only the rule, no preamble, no list, no headings.")
INTENT_CLAUSE = (" The rule should serve this intent: keep the agent empirically honest — it must not "
                 "assert from its internal model when the world can be cheaply queried.")

STOP = set("a an the of to in on for and or but is are be by that this it its as at with from into "
           "whether may must should not no only if then than which who whom what when where".split())


def call_engine(prompt, model):
    r = subprocess.run(["claude", "-p", prompt, "--output-format", "json", "--model", model],
                       capture_output=True, text=True, timeout=600)
    try:
        return json.loads(r.stdout).get("result", "").strip()
    except json.JSONDecodeError:
        return ""


def content_tokens(text, extra_strip=frozenset()):
    toks = re.findall(r"[a-z0-9]+", text.lower())
    return {t for t in toks if t not in STOP and t not in extra_strip}


def mean_pairwise_jaccard(token_sets):
    pairs = list(itertools.combinations(range(len(token_sets)), 2))
    if not pairs:
        return 1.0
    tot = 0.0
    for i, j in pairs:
        a, b = token_sets[i], token_sets[j]
        u = a | b
        tot += (len(a & b) / len(u)) if u else 1.0
    return tot / len(pairs)


def run_arm(arm, n, model):
    prompt = SITUATION + ("" if arm == "ungrounded" else INTENT_CLAUSE) + "\n\n" + TASK
    # strip the prompt's own content tokens so shared prompt-vocabulary doesn't inflate overlap
    prompt_tokens = content_tokens(prompt)
    outputs = []
    for i in range(n):
        out = call_engine(prompt, model)
        outputs.append(out)
        print(f"  [{arm} {i+1}/{n}] {len(out)} chars", file=sys.stderr)
    token_sets = [content_tokens(o, extra_strip=prompt_tokens) for o in outputs]
    consistency = round(mean_pairwise_jaccard(token_sets), 3)
    return consistency, outputs


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--arm", choices=["ungrounded", "grounded", "both"], default="both")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--show", action="store_true", help="print raw outputs")
    a = ap.parse_args()
    arms = ["ungrounded", "grounded"] if a.arm == "both" else [a.arm]
    print(f"=== G-consistency rig v2 (free-text, lexical) | model={a.model} | N={a.n} | arms={arms} ===")
    print("=== SURFACE consistency only: paraphrase-blind, boilerplate-gameable, NOT validity ===\n")
    results = {}
    for arm in arms:
        c, outs = run_arm(arm, a.n, a.model)
        results[arm] = c
        print(f"--- arm={arm} | lexical consistency (mean pairwise Jaccard) = {c} ---")
        if a.show:
            for k, o in enumerate(outs):
                print(f"    [{k+1}] {o}")
        print()
    if len(results) == 2:
        d = round(results["grounded"] - results["ungrounded"], 3)
        print(f"=== DELTA (grounded - ungrounded) = {d:+}  "
              f"[>0 => intent-grounding RAISED surface consistency] ===")

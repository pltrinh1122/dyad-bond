#!/usr/bin/env python3
"""bin/g_consistency_rig.py — G-task CONSISTENCY rig (Operator rub 2026-06-14).

Measures the CONSISTENCY (precision / reproducibility) of a Generate task by running it N
times through an INDEPENDENT inferencing engine and computing mechanical per-field deltas.

Bias-fixes designed in (vs the hand-built static rigs):
  * generator = `claude -p` sub-agent, NOT the experimenter. Fresh session each run (the JSON
    `session_id` differs) => no cross-run contamination = control-variable isolation for free.
  * delta = MECHANICAL per-field agreement over schema fields, NOT a human/LLM read => no
    interpreter bias, no second-LLM judge.
  * output is STRUCTURED (a schema invariant record) so deltas are exact-match computable.

WHAT THIS DOES NOT MEASURE (the load-bearing scope-line): VALIDITY. Consistency is precision,
not accuracy — a G task can be perfectly consistent and consistently WRONG. This answers
"is G deterministic?" (Phase 1) ONLY. Reliability/alignment needs a separate oracle.

Residual experimenter bias, place-and-bounded (named, not eliminated): the PROMPT and the
CHOSEN FIELDS are still authored here; pinned below so downstream is deterministic.

Control variables: model (--model, pinned), prompt (pinned), source passage (pinned), tools
(none requested), N (--n). Manipulated variable: --arm (ungrounded | grounded) — the grounded
arm differs from ungrounded by EXACTLY one intent clause (minimal-contrast design).
NOTE: sampling temperature is NOT settable via the CLI here -> absolute consistency numbers are
temp-dependent and NOT meaningful alone; only the DELTA BETWEEN ARMS at the same temp is.

Usage: python3 bin/g_consistency_rig.py --n 10 --arm both --model claude-haiku-4-5-20251001
"""
import sys, json, subprocess, argparse, re, collections

# --- pinned experiment material (the place-and-bounded experimenter-authored locus) ---
SOURCE = (
    "When the Agent is about to state a fact about the development substrate (what tools exist, "
    "what a file contains, what the environment supports), it must first confirm that fact by "
    "direct execution or a canonical source-query in the current session; the absence of a file "
    "or doc does not by itself establish the absence of a capability."
)
INTENT_CLAUSE = (
    "\n\nThis rule SERVES the stated intent: keep the bond covalent — the Agent's empirical-"
    "debiasing half must not assert from its internal model when the world can be queried."
)
PROMPT_TMPL = """You are extracting ONE invariant from a source passage into a fixed schema.
Output ONLY a YAML mapping (no prose, no code fence, no tools) with EXACTLY these keys:
  scope: {{actor: <agent|operator|both|any-dyad>, trigger: <short-noun-phrase>}}
  prescription: {{action: <verb>, modality: <MUST|MUST-NOT|ONLY-BY|ONLY-AFTER>}}
  observability: {{observable: <evidence-class>, detector: <hard-oracle|soft-record|other-half-only|unobservable-from-inside>}}
  form: <slogan|tuple|mathematical>

SOURCE PASSAGE:
{source}
"""
FIELDS = [  # (label, path) — the mechanically-compared fields
    ("scope.actor", ("scope", "actor")), ("scope.trigger", ("scope", "trigger")),
    ("prescription.action", ("prescription", "action")), ("prescription.modality", ("prescription", "modality")),
    ("observability.observable", ("observability", "observable")), ("observability.detector", ("observability", "detector")),
    ("form", ("form",)),
]


def call_engine(prompt, model):
    r = subprocess.run(["claude", "-p", prompt, "--output-format", "json", "--model", model],
                       capture_output=True, text=True, timeout=600)
    try:
        return json.loads(r.stdout).get("result", "")
    except json.JSONDecodeError:
        return ""


def parse_record(text):
    """Tolerant: strip fences, yaml-load, return dict or None (None => a PARSE-FAIL 'value')."""
    try:
        import yaml
    except ImportError:
        sys.exit("FATAL: pyyaml required")
    m = re.search(r"```(?:yaml)?\s*(.*?)```", text, re.S)
    body = m.group(1) if m else text
    try:
        d = yaml.safe_load(body)
        return d if isinstance(d, dict) else None
    except yaml.YAMLError:
        return None


def get_path(d, path):
    cur = d
    for k in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return str(cur).strip().lower() if cur is not None else None


def run_arm(arm, n, model):
    prompt = PROMPT_TMPL.format(source=SOURCE + (INTENT_CLAUSE if arm == "grounded" else ""))
    records = []
    for i in range(n):
        rec = parse_record(call_engine(prompt, model))
        records.append(rec)
        print(f"  [{arm} {i+1}/{n}] {'parsed' if rec else 'PARSE-FAIL'}", file=sys.stderr)
    # per-field agreement = frequency of the modal value / N (PARSE-FAIL counts as its own value)
    report, agreements = {}, []
    for label, path in FIELDS:
        vals = [get_path(r, path) if r else "<PARSE-FAIL>" for r in records]
        dist = collections.Counter(v if v is not None else "<MISSING>" for v in vals)
        modal, modal_n = dist.most_common(1)[0]
        agr = modal_n / n
        agreements.append(agr)
        report[label] = {"agreement": round(agr, 3), "modal": modal, "dist": dict(dist)}
    overall = round(sum(agreements) / len(agreements), 3)
    return overall, report


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--arm", choices=["ungrounded", "grounded", "both"], default="both")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    a = ap.parse_args()
    arms = ["ungrounded", "grounded"] if a.arm == "both" else [a.arm]
    print(f"=== G-consistency rig | model={a.model} | N={a.n} | arms={arms} ===")
    print("=== SCOPE: precision only. NOT validity. (a consistent G can be consistently wrong) ===\n")
    results = {}
    for arm in arms:
        overall, report = run_arm(arm, a.n, a.model)
        results[arm] = overall
        print(f"--- arm={arm} | overall consistency={overall} ---")
        for label, r in report.items():
            print(f"    {label:28s} agr={r['agreement']:<5} modal={r['modal']!r}  dist={r['dist']}")
        print()
    if len(results) == 2:
        d = round(results["grounded"] - results["ungrounded"], 3)
        print(f"=== DELTA (grounded - ungrounded) = {d:+}  "
              f"[>0 => intent-grounding RAISED consistency; the manipulated-variable effect] ===")

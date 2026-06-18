#!/usr/bin/env python3
"""bin/lifecycle_state.py — DERIVED lifecycle-state projection (single-pane).

WHY (the falsified requirement): reaching the dyad's true lifecycle state cost a multi-turn
forensic crawl across invariants-bond.yaml + theory-pipeline.yaml + the 200KB ledger — and ROM
means that reconstruction tax is paid EVERY fresh resume. The cost-to-know was an unobserved
(therefore ungoverned) variable; this thread measured it (n=1) and refuted the legibility claim.
This instrument makes the cross-cut cheap: one run renders what the crawl rendered.

DISCIPLINE (why a script, not a maintained dashboard): a STORED state-view drifts and then lies
confidently (mode-4 staleness — the exact failure the dyad guards everywhere). So this is a
PROJECTION, never an artifact: recomputed from source each run, default to stdout (not written),
sha-PINNED so staleness self-declares. Same emit-discipline as the commissioned extraction engine.

TRUST BOUNDARY (validate FORM, declare TRUTH — the schema's own A/B split):
  - HARD facts (gated, mechanical): record/row counts, settlement & exec_phase distributions,
    node↔experiment linkage via a resolvable `targets:` ref, settled-nodes-without-experiments.
  - DECLARED (judgment, not gated): altitude/claim_type read — whether a row is "theory-shaped" vs
    "node-shaped" is an interpretation; the script reports claim_type, it does not adjudicate it.

NOT a kb artifact, not the theory-pipeline's report.py (that's a full dashboard render). This is the
state CROSS-CUT — the nodes×rows×linkage join whose absence was the read-side gap.

Usage: python3 bin/lifecycle_state.py
       python3 bin/lifecycle_state.py --invariants <path> --pipeline <path>   # portability
Exit:  0 rendered · 2 source/load error (fail-closed).
"""
import sys, os, subprocess
from collections import Counter
try:
    import yaml
except ImportError:
    sys.exit("FATAL: pyyaml required (commissioner reference instrument; same dep as invariant-eval.py)")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEF_INV = os.path.join(ROOT, "dialectic", "invariants-bond.yaml")
DEF_PIPE = os.path.join(ROOT, "dialectic", "theory-pipeline.yaml")


def git(*args):
    """Best-effort git query; '' if git/repo unavailable (projection still renders, pin declares UNKNOWN)."""
    try:
        r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else ""
    except OSError:
        return ""


def pin(path):
    """Source sha-pin + dirty flag (A-1 committed-state: a dirty tree makes the pin lie about bytes read)."""
    rel = os.path.relpath(path, ROOT)
    sha = git("log", "-1", "--format=%h", "--", rel) or "UNKNOWN"
    dirty = bool(git("status", "--porcelain", "--", rel))
    return rel, sha, dirty


def load(path):
    if not os.path.exists(path):
        sys.exit(f"FATAL: source unresolvable: {path} (fail-closed)")
    try:
        return yaml.safe_load(open(path, encoding="utf-8"))
    except yaml.YAMLError as e:
        sys.exit(f"FATAL: malformed YAML in {path}: {e} (fail-closed)")


def trim(s, n=72):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def bar(title):
    print(f"\n=== {title} ===")


def main():
    inv_path, pipe_path = DEF_INV, DEF_PIPE
    a = sys.argv[1:]
    for i, tok in enumerate(a):
        if tok == "--invariants" and i + 1 < len(a):
            inv_path = a[i + 1]
        elif tok == "--pipeline" and i + 1 < len(a):
            pipe_path = a[i + 1]

    inv = load(inv_path)
    pipe = load(pipe_path)
    nodes = inv.get("invariants") or []
    rows = pipe.get("candidates") or []

    # ---- header: provenance + sha-pins + staleness self-declaration ----
    head = git("rev-parse", "--short", "HEAD") or "UNKNOWN"
    pins = [pin(inv_path), pin(pipe_path)]
    any_dirty = any(d for _, _, d in pins)
    print("=== lifecycle-state | DERIVED PROJECTION (recomputed-not-stored; sha-pinned) ===")
    print(f"    repo HEAD: {head}")
    for rel, sha, dirty in pins:
        print(f"    source: {rel} @ {sha}{'  ⚠ DIRTY (pin lies about bytes read — A-1)' if dirty else ''}")
    if any_dirty:
        print("    ⚠ STALENESS: tree dirty — this projection reflects WORKING-TREE bytes, not the pinned commit.")
    print("    TRUST: counts/linkage = gated(hard) · claim_type/altitude = declared(judgment, not adjudicated here).")

    # ---- nodes: the settled core (settlement × status × re-rub arming) ----
    node_ids = {n.get("id") for n in nodes}
    bar(f"invariant nodes — the settled core ({len(nodes)})")
    print(f"    settlement: {dict(Counter(n.get('settlement', '?') for n in nodes))}")
    print(f"    status:     {dict(Counter(n.get('status', '?') for n in nodes))}")

    # ---- pipeline: the live frontier (exec_phase × grade × claim_type) ----
    bar(f"theory-pipeline rows — the live frontier ({len(rows)})")
    print(f"    exec_phase: {dict(Counter(r.get('exec_phase', '?') for r in rows))}")
    print(f"    grade:      {dict(Counter(str(r.get('grade', '?')) for r in rows))}")
    print(f"    claim_type: {dict(Counter(r.get('claim_type', '?') for r in rows))}   ◌ declared (altitude signal, not gated)")

    # ---- THE CROSS-CUT: node ↔ experiment linkage (the read-side gap this instrument exists for) ----
    targeted, dangling = {}, []
    for r in rows:
        for t in (r.get("targets") or []):
            (targeted.setdefault(t, []).append(r.get("id")) if t in node_ids
             else dangling.append((r.get("id"), t)))
    armed = sorted(targeted)
    unarmed = sorted(nid for nid in node_ids if nid not in targeted)
    bar("node ↔ experiment linkage (HARD — resolvable `targets:` refs)")
    print(f"    rows carrying a resolvable targets→node ref: {sum(len(v) for v in targeted.values())}"
          f" across {len(armed)}/{len(node_ids)} nodes")
    if dangling:
        for eid, t in dangling:
            print(f"    ✗ DANGLING targets: {eid} → {t!r} (no such node — id-integrity)")
    if armed:
        for nid in armed:
            print(f"    ● armed   {nid} ← {', '.join(targeted[nid])}")
    print(f"    ◌ {len(unarmed)}/{len(node_ids)} settled nodes carry re_rub_triggers but NO targeting experiment")
    print("      → re-rub is EVENT-DRIVEN (authored fresh when a trigger fires), not a standing rig. By design,")
    print("        or a gap — that adjudication is the Operator's; this only surfaces the count cheaply.")

    # ---- open work rollup (the largest typed gap per live row = its next probe = the NBA feed) ----
    bar("open frontier (live rows, by phase) — largest typed gap = next probe")
    order = {"PROBE": 0, "DESIGN": 1, "INTAKE": 2, "PARKED": 3, "TERMINAL": 4, "GRADUATED": 5, "KILLED": 6}
    for r in sorted(rows, key=lambda r: (order.get(r.get("exec_phase"), 9), str(r.get("id")))):
        if r.get("status") == "killed":
            continue
        gap = (r.get("open_gap") or {})
        gt = gap.get("type")
        tag = f"[{gt}]" if gt else ""
        print(f"    {r.get('exec_phase', '?'):<9} {r.get('grade', '?'):<8} {r.get('id')}")
        if gap.get("text"):
            print(f"              gap{tag}: {trim(gap.get('text'))}")
        if r.get("next_probe") and r.get("exec_phase") not in ("TERMINAL", "KILLED"):
            print(f"              next: {trim(r.get('next_probe'))}")

    # ---- terminal/dead, declared so the live set is honest ----
    dead = [r.get("id") for r in rows if r.get("exec_phase") in ("KILLED", "TERMINAL")]
    if dead:
        bar("off-frontier (terminal / killed — not live attack surface)")
        for r in rows:
            if r.get("exec_phase") in ("KILLED", "TERMINAL"):
                print(f"    {r.get('exec_phase'):<9} {r.get('id')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

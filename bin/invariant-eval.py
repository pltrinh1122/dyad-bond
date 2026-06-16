#!/usr/bin/env python3
"""bin/invariant-eval.py — REFERENCE evaluator for dialectic/invariant-schema.yaml (v0.8).

NOT the commissioned engine (that's cairn's, per commissions/2026-06-12-*). This is the
commissioner's Validate-half instrument: (a) falsify the schema by implementation BEFORE
solicitation; (b) the independent acceptance harness at delivery.
Validates FORM, never TRUTH (a math-form's expression is opaque here — structural only).

Usage: python3 bin/invariant-eval.py <schema.yaml> <corpus.yaml>
Exit: 0 all-pass · 1 violations · 2 schema/load error (fail-closed).
"""
import sys, re, os
try:
    import yaml
except ImportError:
    sys.exit("FATAL: pyyaml required (reference harness only; the commissioned engine binds at build-time)")


def cond_eval(cond, rec):
    """Mini condition language: 'X == true' | 'X != v' | 'X in [a, b]'. Fail-closed on unparseable."""
    cond = cond.strip()
    if " in " in cond:
        field, _, rest = cond.partition(" in ")
        vals = [v.strip() for v in rest.strip().strip("[]").split(",")]
        return rec.get(field.strip()) in vals
    for op in ("==", "!="):
        if op in cond:
            field, _, val = cond.partition(op)
            val = val.strip()
            want = {"true": True, "false": False}.get(val, val)
            got = rec.get(field.strip())
            return (got == want) if op == "==" else (got != want)
    raise ValueError(f"unparseable condition: {cond!r}")


def vocab_check(vocabs, name, value):
    v = vocabs.get(name)
    if v is None:
        return f"NO-VOCAB:{name}"
    allowed = v["seed"] if isinstance(v, dict) and "seed" in v else v
    return None if value in allowed else f"not-in-vocab:{name}:{value!r}"


def check_group(gname, gspec, gval, rec, errs):
    if not isinstance(gval, dict):
        errs.append(f"{gname}: not a mapping")
        return
    for fname, fspec in gspec.get("fields", {}).items():
        val = gval.get(fname)
        req = fspec.get("required", False)
        if fspec.get("required_iff"):
            req = cond_eval(fspec["required_iff"], rec)
        if fspec.get("forbidden_iff") and cond_eval(fspec["forbidden_iff"], rec) and val is not None:
            errs.append(f"{gname}.{fname}: FORBIDDEN here (per {fspec['forbidden_iff']!r})")
            continue
        if val is None:
            if req:
                errs.append(f"{gname}.{fname}: REQUIRED, missing")
            continue
        if "enum" in fspec:
            e = vocab_check(VOCABS, fspec["enum"], val)
            if e:
                errs.append(f"{gname}.{fname}: {e}")
        if "const" in fspec and val != fspec["const"]:
            errs.append(f"{gname}.{fname}: must be const {fspec['const']!r}, got {val!r}")


def check_record(rec, spec, ids):
    errs, gaps = [], []
    rid = rec.get("id", "<NO-ID>")
    for f in spec["required"]:
        if f not in rec:
            errs.append(f"{f}: REQUIRED top-level field missing")
    fields = spec["fields"]
    # flat fields
    if "id" in rec:
        if not re.match(fields["id"]["pattern"], rec["id"]):
            errs.append(f"id: fails pattern {fields['id']['pattern']!r}")
        if rec["id"] in ids:
            errs.append("id: DUPLICATE in corpus")
        ids.add(rec["id"])
    if "one_liner" in rec and len(rec["one_liner"]) > fields["one_liner"]["max_chars"]:
        errs.append(f"one_liner: {len(rec['one_liner'])} chars > {fields['one_liner']['max_chars']}")
    for f in ("status", "form", "settlement"):
        if f in rec:
            e = vocab_check(VOCABS, fields[f]["enum"], rec[f])
            if e:
                errs.append(f"{f}: {e}")
    # conditionals on flat fields
    for f in ("re_rub_triggers", "root_kind", "adjudicated", "grounded_in"):
        fs = fields[f]
        present = rec.get(f) is not None
        if fs.get("required_iff") and cond_eval(fs["required_iff"], rec) and not present:
            errs.append(f"{f}: REQUIRED (per {fs['required_iff']!r}), missing")
        if fs.get("forbidden_iff") and cond_eval(fs["forbidden_iff"], rec) and present:
            errs.append(f"{f}: FORBIDDEN (per {fs['forbidden_iff']!r}), present")
    if rec.get("root_kind") is not None:
        e = vocab_check(VOCABS, "root_kind", rec["root_kind"])
        if e:
            errs.append(f"root_kind: {e}")
    for t in rec.get("re_rub_triggers") or []:
        e = vocab_check(VOCABS, "re_rub_trigger", t)
        if e:
            errs.append(f"re_rub_triggers: {e}")
    if rec.get("adjudicated") is not None and rec["adjudicated"].get("by") != "Operator":
        errs.append("adjudicated.by: must be const 'Operator'")
    for edge in rec.get("grounded_in") or []:
        if edge.get("edge") not in VOCABS["edge_type"]:
            errs.append(f"grounded_in.edge: not-in-vocab:{edge.get('edge')!r}")
    # groups
    for g in ("scope", "prescription", "observability"):
        if g in rec:
            check_group(g, fields[g], rec[g], rec, errs)
    # group-level lint: trigger must not contain action token
    trig, act = (rec.get("scope") or {}).get("trigger", ""), (rec.get("prescription") or {}).get("action", "")
    if trig and act and any(tok and tok in trig for tok in act.split()):
        errs.append(f"LINT scope.trigger contains action token (normalization rule): {trig!r} ~ {act!r}")
    # math group
    math_req = cond_eval(fields["math"]["required_iff"], rec)
    if math_req and rec.get("math") is None:
        errs.append("math: REQUIRED (form == mathematical), missing")
    if rec.get("math") is not None:
        m = rec["math"]
        if m.get("use") != "breach-detector":
            errs.append("math.use: GOODHART — must be const 'breach-detector'")
        if not m.get("measurements"):
            errs.append("math.measurements: Class-B undeclared (empty)")
        gaps.append("math.expression: OPAQUE — structurally present, semantically unevaluated (form-not-truth)")
    return rid, errs, gaps


def corpus_checks(records):
    errs, flags = [], []
    by_id = {r.get("id"): r for r in records}
    # one_liner atomicity (HEURISTIC, non-failing): a ';' signals >1 co-equal assertion. The real gate is
    # the breach-test (one observability.breach_example per record); this only nudges toward decomposition.
    for r in records:
        if ";" in (r.get("one_liner") or ""):
            flags.append(f"ONE-LINER-COMPOSITE {r.get('id')}: one_liner contains ';' — likely >1 assertion (decompose or move to fields)")
    # grounding-graph: resolve, terminate, acyclic
    for r in records:
        for edge in r.get("grounded_in") or []:
            ref = edge.get("ref")
            if ref not in by_id:
                flags.append(f"ORPHAN-EDGE {r.get('id')} → {ref!r} (boundary-candidate OR ungrounded)")
    def terminates(rid, seen):
        r = by_id.get(rid)
        if r is None:
            return False
        if r.get("root"):
            return True
        if rid in seen:
            errs.append(f"CYCLE at {rid}")
            return False
        return any(terminates(e.get("ref"), seen | {rid}) for e in r.get("grounded_in") or [])
    for r in records:
        if not r.get("root") and not terminates(r.get("id"), set()):
            errs.append(f"NO-TERMINATION {r.get('id')}: no chain reaches an adjudicated root")
    # census
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            sa, sb = a.get("scope") or {}, b.get("scope") or {}
            pa, pb = a.get("prescription") or {}, b.get("prescription") or {}
            if (sa.get("trigger") == sb.get("trigger") and pa.get("action") == pb.get("action")
                    and {pa.get("modality"), pb.get("modality")} == {"MUST", "MUST-NOT"}):
                flags.append(f"STRICT-CONFLICT {a['id']} ⟂ {b['id']}")
        p, s = a.get("prescription") or {}, a.get("scope") or {}
        o = a.get("observability") or {}
        if (s.get("actor") == "agent" and p.get("modality") == "MUST"
                and o.get("detector") in ("other-half-only", "unobservable-from-inside")):
            flags.append(f"DUTY-DETECTOR-MISMATCH {a['id']}")
    prohib = {}
    for r in records:
        if (r.get("prescription") or {}).get("modality") == "MUST-NOT":
            prohib.setdefault((r.get("scope") or {}).get("trigger"), []).append(r["id"])
    for trig, members in prohib.items():
        if len(members) >= 2:
            affirm = [r["id"] for r in records if (r.get("scope") or {}).get("trigger") == trig
                      and (r.get("prescription") or {}).get("modality") in ("MUST", "ONLY-BY")]
            if not affirm:
                flags.append(f"PINCER-CANDIDATE trigger={trig!r}: {members}, no affirmative path")
    return errs, flags


def _md_slugs(path):
    """ATX-header slugs of a markdown file: the name before ' — ' / '(', spaces→hyphens, lower."""
    slugs = set()
    try:
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^#{1,6}\s+(.*)", line)
            if m:
                title = re.split(r"\s+[—-]\s+|\(", m.group(1))[0].strip()
                slugs.add(re.sub(r"\s+", "-", title).lower())
    except OSError:
        return None
    return slugs


def home_resolve(home):
    """Class A: the home FILE must resolve (hard-fail). Class B: the #anchor is DECLARED, not gated
    — the durable locator grammar is the engine's versioned inline tag (commission A-3), NOT a
    markdown slug, so a fragment mismatch today is a soft label-truth flag deferred to that grammar.
    Returns one of: ('A-OK',…) ('A-MISS-FILE',…) ('B-OK',…) ('B-STALE-ANCHOR',…)."""
    path, _, frag = (home or "").partition("#")
    if not path or not os.path.exists(path):
        return ("A-MISS-FILE", path, frag)
    if not frag:
        return ("A-OK", path, "")
    slugs = _md_slugs(path)
    fs = frag.lower()
    if slugs is None or any(s == fs or s.startswith(fs) for s in slugs):
        return ("B-OK", path, frag)
    return ("B-STALE-ANCHOR", path, frag)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    schema = yaml.safe_load(open(sys.argv[1]))
    corpus = yaml.safe_load(open(sys.argv[2]))
    VOCABS = schema["vocabularies"]
    globals()["VOCABS"] = VOCABS
    records = corpus["invariants"]
    ids, all_gaps, n_fail = set(), [], 0
    print(f"=== invariant-eval | schema {schema['schema_version']} | {len(records)} records ===")
    for rec in records:
        rid, errs, gaps = check_record(rec, schema["record"], ids)
        all_gaps += gaps
        status = "PASS" if not errs else "FAIL"
        n_fail += bool(errs)
        print(f"[{status}] {rid}")
        for e in errs:
            print(f"    ✗ {e}")
    cerrs, cflags = corpus_checks(records)
    print("=== corpus ===")
    for e in cerrs:
        print(f"    ✗ {e}")
    for f in cflags:
        print(f"    ⚑ {f}")
    # home resolution — Class A (file) GATED · Class B (#anchor) DECLARED (deferred to the engine tag-grammar)
    print("=== home resolution (Class A: file gated · Class B: #anchor declared) ===")
    home_fail = 0
    for r in records:
        kind, path, frag = home_resolve(r.get("home"))
        if kind == "A-MISS-FILE":
            home_fail += 1
            print(f"    ✗ {r.get('id')}: home file unresolvable → {path!r} (Class A, HALT)")
        elif kind == "B-STALE-ANCHOR":
            print(f"    ◌ {r.get('id')}: #{frag} not in {path} headers (Class B — declared, deferred to tag-grammar)")
    print("=== declared-unevaluable (gaps surfaced by THIS run) ===")
    for g in sorted(set(all_gaps)):
        print(f"    ◌ {g}")
    sys.exit(1 if (n_fail or cerrs or home_fail) else 0)

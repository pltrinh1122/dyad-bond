#!/usr/bin/env python3
"""bin/commission-lint.py — structural linter for commission specs vs commission-template.md.

Checks FORM only (section presence, required declarations, falsifier-table shape) — never TRUTH
(whether the Why is a real requirement, whether the F-atoms actually cover the failure space,
whether the builder-fit read is honest). That split is deliberate, same as invariant-eval.py's
FORM-not-TRUTH ceiling — this tool narrows the review, it does not replace the Operator's rub.

Built bond-side, not commissioned: TERMS.md's own line-rule keeps declared-policy-wrapper shapes
(loud, simple failures) for bond and reserves commissions for engine-failure-mode shapes. A markdown
structural scan is the former.

Motivated by dogfood: the dyad-system-engine spec sat for two turns missing the Commission-type
declaration commission-template.md requires as its first line, caught only by re-reading. This
mechanizes that catch, plus the composite-breach-condition check (the pilot's own v0.4 bug — a
falsifier row bundling co-equal conjuncts hides a partial breach as a clean pass).

Usage: python3 bin/commission-lint.py [file ...]
       (no args -> lints commissions/*.md, excluding TERMS.md + commission-template.md)
Exit:  0 all-pass · 1 violations · 2 file/load error (fail-closed).
"""
import glob, os, re, sys

HEADING_RE = re.compile(r"^## ", re.MULTILINE)
TITLE_RE = re.compile(r"^# COMMISSION SPEC — .+", re.MULTILINE)
COMMISSION_TYPE_RE = re.compile(r"Commission-type:\s*\**\s*(Conformance|Generative)", re.IGNORECASE)

REQUIRED_SECTIONS = [
    ("Why", re.compile(r"^## Why\b", re.MULTILINE)),
    ("Architecture", re.compile(r"^## Architecture\b", re.MULTILINE)),
    ("Input invariants", re.compile(r"^## Input invariants\b", re.MULTILINE)),
    ("Acceptance falsifiers", re.compile(r"^## Acceptance falsifiers\b", re.MULTILINE)),
    ("Gate-0", re.compile(r"^## Gate-0\b", re.MULTILINE)),
    ("Architectural-grain", re.compile(r"^## Architectural-grain\b", re.MULTILINE)),
    ("Deliverable", re.compile(r"^## Deliverable\b", re.MULTILINE)),
    ("What this commission is NOT", re.compile(r"^## What this commission is NOT\b", re.MULTILINE)),
    ("Fixed vs negotiable", re.compile(r"^## Fixed vs negotiable\b", re.MULTILINE)),
]
SECTION_PATTERNS = {name: pat for name, pat in REQUIRED_SECTIONS}

ALLOWED_CLASS_TOKENS = ("oracle", "discipline-assumed")
# the pilot's v0.4 bug: a breach-condition bundling co-equal conjuncts hides a partial breach as PASS
COMPOSITE_HEURISTIC_RE = re.compile(r"\bAND\b|;.*;")


def section_body(text, pat):
    """Text between a `## ` heading matched by `pat` and the next `## ` heading (or EOF)."""
    m = pat.search(text)
    if not m:
        return None
    nxt = next(HEADING_RE.finditer(text, m.end()), None)
    return text[m.end(): nxt.start() if nxt else len(text)]


def table_rows(body):
    """Data rows (cell-lists) of the first markdown table in `body`; header + separator dropped."""
    lines = [l for l in body.splitlines() if l.strip().startswith("|")]
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue  # separator row
        rows.append(cells)
    return rows[1:]  # drop header row


def lint(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    errs, advisories = [], []

    if not TITLE_RE.search(text):
        errs.append("title: does not match '# COMMISSION SPEC — <name>'")
    if not COMMISSION_TYPE_RE.search(text):
        errs.append("status: missing 'Commission-type: Conformance|Generative' declaration")

    for name, pat in REQUIRED_SECTIONS:
        if not pat.search(text):
            errs.append(f"section missing: {name!r}")

    inv_body = section_body(text, SECTION_PATTERNS["Input invariants"])
    if inv_body is not None:
        if "Class A" not in inv_body:
            errs.append("Input invariants: no 'Class A' subsection found")
        if "Class B" not in inv_body:
            errs.append("Input invariants: no 'Class B' subsection found")

    fx_body = section_body(text, SECTION_PATTERNS["Fixed vs negotiable"])
    if fx_body is not None:
        if "not negotiable" not in fx_body.lower():
            errs.append("Fixed vs negotiable: no 'Not negotiable' line found")
        if "negotiable in this round" not in fx_body.lower():
            errs.append("Fixed vs negotiable: no 'Negotiable in this round' line found")

    fals_body = section_body(text, SECTION_PATTERNS["Acceptance falsifiers"])
    if fals_body is not None:
        rows = table_rows(fals_body)
        if not rows:
            errs.append("Acceptance falsifiers: no markdown table (or table has no data rows)")
        for i, cells in enumerate(rows, start=1):
            if len(cells) < 3:
                errs.append(f"Acceptance falsifiers row {i}: expected >=3 cells (atom|breach-condition|class), got {len(cells)}")
                continue
            atom, breach, cls = cells[0], cells[1], cells[-1]
            if not any(tok in cls for tok in ALLOWED_CLASS_TOKENS):
                errs.append(f"Acceptance falsifiers row {i} ({atom}): class {cls!r} names neither 'oracle' nor 'discipline-assumed'")
            if COMPOSITE_HEURISTIC_RE.search(breach):
                advisories.append(f"row {i} ({atom}) breach-condition reads as possibly composite: {breach!r}")

    for label, count in (("Gate-0", 4), ("Architectural-grain", 4)):
        body = section_body(text, SECTION_PATTERNS[label])
        if body is None:
            continue
        found = len(set(re.findall(r"\b[DG]-\d", body)))
        if found < count:
            errs.append(f"{label}: only {found} labeled items found (expected {count}, e.g. D-1..D-4 / G-1..G-4)")

    return errs, advisories


FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)


def is_commission_spec(path):
    """Default-discovery filter: does this look like a commission spec at all? Title-gated, not a
    filename exclusion-list — TERMS.md/commission-template.md fail this the same way any other
    non-spec doc parked in commissions/ (e.g. a findings writeup) does, with no list to maintain.
    Fenced code blocks are stripped first — commission-template.md's example title lives inside one
    and must not count as a real spec."""
    try:
        with open(path, encoding="utf-8") as f:
            text = FENCED_BLOCK_RE.sub("", f.read())
            return bool(TITLE_RE.search(text))
    except OSError:
        return False


def main(argv):
    paths = argv or sorted(p for p in glob.glob("commissions/*.md") if is_commission_spec(p))
    if not paths:
        print("no commission specs found (commissions/*.md matching '# COMMISSION SPEC — <name>')")
        return 0

    any_fail = False
    for path in paths:
        try:
            errs, advisories = lint(path)
        except OSError as e:
            print(f"[ERROR] {path}: {e}")
            return 2
        any_fail = any_fail or bool(errs)
        print(f"[{'FAIL' if errs else 'PASS'}] {path}")
        for e in errs:
            print(f"    ✗ {e}")
        for a in advisories:
            print(f"    ◌ ADVISORY: {a}")

    print(
        "\nFORM only, never TRUTH — same ceiling as invariant-eval.py. A clean PASS means the spec "
        "has the template's required shape; it says nothing about whether the requirement is real, "
        "the F-atoms are sufficient, or the builder-fit is honest. That stays the Operator's rub."
    )
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""bin/discipline-lint.py — structural linter for kb-with-caveat discipline files.

DOGFOOD, not a standing tool (Operator-directed probe, 2026-07-02, after the discipline-linter
THESIS was falsified as premature on n=4-confounded evidence — see the falsification below and
dialectic/carry-forward.md). This checks FORM only, same ceiling as commission-lint.py /
invariant-eval.py: section presence + the pointer-collapse round-trip. It does NOT check TRUTH
(whether the rule is correctly stated, whether a citation actually traces to what it claims to —
the exact defect this session's own kb graduations produced and this tool cannot see).

Scope is deliberately gated on the file's own `kb-with-caveat` self-declaration in its frontmatter
comment, not a blanket shape imposed on every kb/*.md file — kb/dfd.md and kb/founding-evidence.md
predate the convention / have different provenance and are correctly exempt, not violations.

Usage: python3 bin/discipline-lint.py [file ...]
       (no args -> lints kb/*.md, filtered to files whose frontmatter declares kb-with-caveat)
Exit:  0 all-pass (or nothing in scope) · 1 violations · 2 file/load error (fail-closed).
"""
import glob
import re
import sys

KB_WITH_CAVEAT_RE = re.compile(r"kb-with-caveat", re.IGNORECASE)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LOCUS_RE = re.compile(r"^locus:\s*\S+", re.MULTILINE)
TITLE_RE = re.compile(r"^# .+", re.MULTILINE)
SOURCE_CITATION_RE = re.compile(r"`(dialectic/[\w.\-]+\.md)[^`]*`")

REQUIRED_HEADINGS = [
    ("Falsification status", re.compile(r"^## Falsification status\b", re.MULTILINE)),
    ("Forward", re.compile(r"^## Forward\b", re.MULTILINE)),
]


def in_scope(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return False
    fm = FRONTMATTER_RE.match(text)
    return bool(fm and KB_WITH_CAVEAT_RE.search(fm.group(1)))


def lint(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    errs, advisories = [], []

    fm = FRONTMATTER_RE.match(text)
    if not fm or not LOCUS_RE.search(fm.group(1)):
        errs.append("frontmatter: no 'locus:' field found")

    if not TITLE_RE.search(text):
        errs.append("title: no '# <Name>' H1 found")

    for name, pat in REQUIRED_HEADINGS:
        if not pat.search(text):
            errs.append(f"section missing: {name!r}")

    # Pointer-collapse round-trip: does the cited dialectic source actually point back?
    m = SOURCE_CITATION_RE.search(text)
    if not m:
        advisories.append("no `dialectic/*.md` source citation found near the top — can't check the round-trip")
    else:
        src_path = m.group(1)
        try:
            with open(src_path, encoding="utf-8") as f:
                src_text = f.read()
        except OSError:
            errs.append(f"cited source {src_path!r} does not exist")
        else:
            kb_name = path.split("/")[-1]
            if kb_name not in src_text:
                errs.append(f"dangling pointer: {src_path!r} does not mention {kb_name!r} back")

    return errs, advisories


def main(argv):
    if argv:
        paths = argv
    else:
        paths = sorted(p for p in glob.glob("kb/*.md") if in_scope(p))

    if not paths:
        print("no kb-with-caveat files found in scope (kb/*.md whose frontmatter declares kb-with-caveat)")
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
        "\nFORM only, never TRUTH. A clean PASS means the file has the shape; it says nothing about "
        "whether the rule is correctly stated or a citation traces to what it claims (the mis-citation "
        "this session actually produced is invisible to this tool by design — see the module docstring)."
    )
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

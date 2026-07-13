#!/usr/bin/env python3
"""bin/readme-lint.py — structural gate for the falsifiable-manifesto README form.

LINEAGE (bond:form-grounding — extend, never redefine): the checks are adapted from
dyad-cairn's `skills/readme_lint.py@2e1a2e9` (2026-07-08), the mechanical *How* of its
README-Writing Discipline. bond FALSIFIED the cross-dyad adoption clause before adopting:
cairn's vendoring rule (its C19) assumes a `skills/` layout and a No-Pure-G invariant that
bond does NOT hold — bond's linters live in `bin/` and are dogfood-validated (see
`commission-lint.py`, `invariant-eval.py`). So this is the bond-substrate adaptation, not a copy:
a single self-contained `bin/` script whose paired test is EMBEDDED as `--selftest` (tool and test
are inseparable — a stronger read of No-Pure-G's intent than cairn's separable two-file split,
which its own C19 warns can be vendored apart).

FORM-not-TRUTH ceiling (Builder vs Enforcer — same line invariant-eval.py/commission-lint.py hold):
this gate checks only MECHANICAL invariants. Register, metaphor budget, tone, audience, and
falsifier-fidelity (the AUDIT conditions) are the Operator's rub + the grounding audit — never here.
A linter that judged taste would be a false authority.

Checks:
  1. YAML frontmatter parses and carries the falsifiable-manifesto schema (+ belief subfields).
  2. kind == "derived-view"          (the README is a lens, never a content-home).
  3. dogma is exactly False          (bond:no-dogma is permanent).
  4. belief.status in {hypothesis, theory}   (conjecture imports a proof that isn't coming;
     settled is forbidden — the collapse dyad-bond guards against).
  5. updated is an ISO date (YYYY-MM-DD).
  6. every canonical_home entry ("FILE § Heading") resolves: file exists relative to the README
     and contains the heading text (bond:single-home — the lens must cite a real home).
  7. the body carries numbered claims ("**Claim N"), and every claim block hands over a falsifier
     ("Break it:") — except a single terminal standing-invitation claim.

Usage: python3 bin/readme-lint.py [path/to/README.md]     (default: README.md)
       python3 bin/readme-lint.py --selftest               (run the embedded paired test)
Exit:  0 pass · 1 violations · 2 file/load error or selftest failure (fail-closed).
"""

import re
import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS = [
    "doc", "kind", "genre", "rule", "belief", "grade", "coverage",
    "dogma", "caution", "cta", "canonical_home", "governed_by", "updated",
]
REQUIRED_BELIEF_FIELDS = ["statement", "foundation", "stance", "status"]
ALLOWED_STATUS = {"hypothesis", "theory"}
FALSIFIER_MARKER = "Break it:"
CLAIM_RE = re.compile(r"\*\*Claim (\d+)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def split_frontmatter(text):
    """Return (frontmatter_str, body) or (None, text) if no frontmatter."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 4:]


def check_canonical_home(entry, readme_dir):
    """Resolve a 'FILE § Heading' pointer against the filesystem."""
    if "§" not in entry:
        return [f"canonical_home entry has no '§ Heading' part: {entry!r}"]
    file_part, heading = (s.strip() for s in entry.split("§", 1))
    target = readme_dir / file_part
    if not target.is_file():
        return [f"canonical_home file not found: {file_part!r}"]
    if heading and heading not in target.read_text(encoding="utf-8"):
        return [f"canonical_home heading {heading!r} not found in {file_part!r}"]
    return []


def lint_frontmatter(fm_text, readme_dir):
    errors = []
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return [f"frontmatter does not parse as YAML: {e}"]
    if not isinstance(fm, dict):
        return ["frontmatter is not a YAML mapping"]

    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"missing frontmatter field: {field}")

    if fm.get("kind") != "derived-view":
        errors.append(f"kind must be 'derived-view', got: {fm.get('kind')!r}")

    if fm.get("dogma") is not False:
        errors.append(f"dogma must be exactly false, got: {fm.get('dogma')!r}")

    belief = fm.get("belief")
    if isinstance(belief, dict):
        for field in REQUIRED_BELIEF_FIELDS:
            if field not in belief:
                errors.append(f"missing belief field: belief.{field}")
        status = belief.get("status")
        if status is not None and status not in ALLOWED_STATUS:
            errors.append(
                f"belief.status must be one of {sorted(ALLOWED_STATUS)}, got: {status!r}")
    elif "belief" in fm:
        errors.append("belief must be a mapping")

    updated = fm.get("updated")
    if updated is not None and not DATE_RE.match(str(updated)):
        errors.append(f"updated must be an ISO date (YYYY-MM-DD), got: {updated!r}")

    homes = fm.get("canonical_home")
    if isinstance(homes, list) and homes:
        for entry in homes:
            errors.extend(check_canonical_home(str(entry), readme_dir))
    elif "canonical_home" in fm:
        errors.append("canonical_home must be a non-empty list")

    return errors


def lint_claims(body):
    errors = []
    claim_numbers = [int(m.group(1)) for m in CLAIM_RE.finditer(body)]
    if not claim_numbers:
        errors.append("body contains no numbered claims ('**Claim N')")
        return errors
    # Each claim block runs to the next claim (or end of body); each must carry the
    # falsifier marker, except a final standing-invitation claim (highest number).
    blocks = re.split(r"(?=\*\*Claim \d+)", body)
    claim_blocks = [b for b in blocks if CLAIM_RE.match(b.strip())]
    last = max(claim_numbers)
    for block in claim_blocks:
        number = int(CLAIM_RE.match(block.strip()).group(1))
        if FALSIFIER_MARKER not in block and number != last:
            errors.append(f"Claim {number} has no falsifier marker ({FALSIFIER_MARKER!r})")
    return errors


def lint_text(text, readme_dir):
    """Core: lint README text with canonical_home resolved relative to readme_dir."""
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        return ["no YAML frontmatter block found"]
    errors = lint_frontmatter(fm_text, readme_dir)
    errors.extend(lint_claims(body))
    return errors


def lint(path):
    readme = Path(path)
    if not readme.is_file():
        return [f"file not found: {path}"]
    text = readme.read_text(encoding="utf-8")
    return lint_text(text, readme.resolve().parent)


# ── Embedded paired test (No-Pure-G: travels WITH the tool, cannot be vendored apart) ─────────
_GOOD_FM = """---
doc: "x"
kind: derived-view
genre: "falsifiable manifesto"
rule: "cite the source, never this lens"
belief:
  statement: "s"
  foundation: belief
  stance: thesis
  status: hypothesis
grade: "survives"
coverage: "E0"
dogma: false
caution: "c"
cta: "c"
canonical_home:
  - "HOME.md § A Heading"
governed_by: [x]
updated: 2026-07-08
---

**Claim 1 — a.** body. → **Break it:** do the thing.[^c1]

**Claim 2 — b.** the terminal standing invitation, no falsifier needed.
"""


def _selftest():
    import tempfile
    failures = []

    def expect(name, text, predicate, base=None):
        errs = lint_text(text, base if base is not None else Path("."))
        if not predicate(errs):
            failures.append(f"{name}: got errors={errs}")

    with tempfile.TemporaryDirectory() as d:
        base = Path(d)
        (base / "HOME.md").write_text("# H\n## A Heading\ntext\n", encoding="utf-8")

        # 1. a fully-conforming README passes clean.
        expect("good-passes", _GOOD_FM, lambda e: e == [], base)

        # 2. kind must be derived-view.
        expect("bad-kind", _GOOD_FM.replace("kind: derived-view", "kind: content-home"),
               lambda e: any("kind must be" in x for x in e), base)

        # 3. dogma must be exactly false.
        expect("bad-dogma", _GOOD_FM.replace("dogma: false", "dogma: true"),
               lambda e: any("dogma must be" in x for x in e), base)

        # 4. status may not be 'settled' or 'conjecture'.
        expect("bad-status", _GOOD_FM.replace("status: hypothesis", "status: settled"),
               lambda e: any("belief.status must be" in x for x in e), base)

        # 5. updated must be an ISO date.
        expect("bad-date", _GOOD_FM.replace("updated: 2026-07-08", "updated: someday"),
               lambda e: any("updated must be" in x for x in e), base)

        # 6a. a missing required field is caught.
        expect("missing-field", _GOOD_FM.replace('cta: "c"\n', ""),
               lambda e: any("missing frontmatter field: cta" in x for x in e), base)

        # 6b. an unresolvable canonical_home heading is caught.
        expect("bad-home", _GOOD_FM.replace("§ A Heading", "§ No Such Heading"),
               lambda e: any("not found in" in x for x in e), base)

        # 7a. a body with no numbered claims is caught.
        expect("no-claims", _GOOD_FM.replace("**Claim 1 — a.**", "Claim one").replace("**Claim 2 — b.**", "Claim two"),
               lambda e: any("no numbered claims" in x for x in e), base)

        # 7b. a non-terminal claim missing its falsifier is caught (terminal is exempt).
        expect("claim-no-falsifier", _GOOD_FM.replace("body. → **Break it:** do the thing.", "body only"),
               lambda e: any("Claim 1 has no falsifier" in x for x in e), base)

        # 8. no-frontmatter is caught.
        expect("no-frontmatter", "# just a title\n\nno frontmatter here.",
               lambda e: any("no YAML frontmatter" in x for x in e), base)

    if failures:
        print("[README-LINT] SELFTEST FAIL:")
        for f in failures:
            print(f"  - {f}")
        return 2
    print("[README-LINT] SELFTEST PASS: 11 cases (1 conforming + 10 violation classes).")
    return 0


def main(argv):
    if len(argv) > 1 and argv[1] == "--selftest":
        return _selftest()
    path = argv[1] if len(argv) > 1 else "README.md"
    try:
        errors = lint(path)
    except OSError as e:
        print(f"[README-LINT] ERROR: {path} — {e}")
        return 2
    if errors:
        print(f"[README-LINT] FAIL: {path} — {len(errors)} violation(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"[README-LINT] PASS: {path} conforms to the falsifiable-manifesto form.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

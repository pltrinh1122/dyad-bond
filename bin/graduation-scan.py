#!/usr/bin/env python3
"""bin/graduation-scan.py — scan a dialectic file for kb-graduation candidates.

Mechanizes the manual review this session ran by hand on relationship-craft.md: parse
top-level (##) sections, read each heading's parenthetical status tag, scan the body for
disqualifying language and any explicit "Graduation gate" sentence, and rank sections by
whether they look worth a closer manual look vs. already blocked vs. already graduated.

This tool does NOT decide graduation — per bond:no-self-ratify, only the Operator's Y fires
a promotion (see dialectic/generation-substrate-provenance.md + relationship-craft.md's D3
entry for the live worked example: propose in DFD form -> Operator Y -> kb/ file + pointer
collapse). This script only narrows the search, the way a grep-pass narrowed it by hand.

Usage: python3 bin/graduation-scan.py [dialectic/relationship-craft.md]
Exit:  0 always (a report tool, not a gate — nothing here is fail-closed).
"""
import re
import sys

DISQUALIFYING = [
    r"NOT settled",
    r"NOT promoted",
    r"NOT yet promoted",
    r"NOT 2nd-model-rubbed",
    r"QUEUED",
    r"PARKED",
    r"design unbuilt",
    r"un-rubbed",
    r"unrubbed",
    r"on trial",
    r"OPEN \(settled-window\)",
    r"debt-not-earned",
    r"NOT settled\b",
    r"held as candidate",
    r"hold\b",
]
GRADUATED_MARKERS = [
    r"graduated to `kb/",
    r"extracted to `",
    r"relocated to `",
]
GRADUATION_GATE_RE = re.compile(r"\*\*Graduation gate\.?\*\*[^\n]*", re.IGNORECASE)
HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)


def parse_sections(text):
    """Split on top-level `## ` headings; return list of (title_line, body, start_line, end_line)."""
    matches = list(HEADING_RE.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end]
        start_line = text.count("\n", 0, start) + 1
        end_line = text.count("\n", 0, end) + 1
        sections.append((m.group(1).strip(), body, start_line, end_line))
    return sections


def scan_section(title, body):
    hits = []
    for pat in DISQUALIFYING:
        for m in re.finditer(pat, title, re.IGNORECASE):
            hits.append(("heading", pat, title.strip()))
        for m in re.finditer(pat, body[:600], re.IGNORECASE):
            line_start = body.rfind("\n", 0, m.start()) + 1
            line_end = body.find("\n", m.end())
            line_end = len(body) if line_end == -1 else line_end
            hits.append(("body", pat, body[line_start:line_end].strip()[:160]))

    graduated = any(re.search(p, title + body[:300], re.IGNORECASE) for p in GRADUATED_MARKERS)

    gate = GRADUATION_GATE_RE.search(body)
    gate_text = gate.group(0).strip()[:220] if gate else None

    return hits, graduated, gate_text


SESSION_HARVEST_RE = re.compile(r"^(Retro|Reflect-harvest|Reflect) —", re.IGNORECASE)


def verdict(title, hits, graduated, gate_text):
    if graduated:
        return "ALREADY GRADUATED / EXTRACTED — skip"
    if SESSION_HARVEST_RE.match(title.strip()):
        return (
            "NOT A CANDIDATE — session-harvest record (D3-form: Continue/Start/Stop), "
            "never exits by design, not a workbench claim — see relationship-craft.md's "
            "own record-type distinction"
        )
    if gate_text:
        return f"BLOCKED — explicit Graduation gate on record: {gate_text}"
    if hits:
        kind, pat, snippet = hits[0]
        return f"BLOCKED — {pat!r} found ({kind}): {snippet}"
    return "REVIEW — no disqualifying language found; worth a manual look"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "dialectic/relationship-craft.md"
    with open(path, encoding="utf-8") as f:
        text = f.read()

    sections = parse_sections(text)
    rows = []
    for title, body, start_line, end_line in sections:
        hits, graduated, gate_text = scan_section(title, body)
        line_count = end_line - start_line
        rows.append((line_count, title, start_line, verdict(title, hits, graduated, gate_text)))

    review = sorted([r for r in rows if r[3].startswith("REVIEW")], key=lambda r: -r[0])
    blocked = sorted([r for r in rows if r[3].startswith("BLOCKED")], key=lambda r: -r[0])
    graduated_rows = [r for r in rows if r[3].startswith("ALREADY")]
    harvest_rows = sorted([r for r in rows if r[3].startswith("NOT A CANDIDATE")], key=lambda r: -r[0])

    def emit(label, group):
        print(f"\n=== {label} ({len(group)}) ===")
        for line_count, title, start_line, v in group:
            print(f"  L{start_line:>5} ({line_count:>4} lines)  {title}")
            print(f"           {v}")

    print(f"Scanned {path}: {len(sections)} top-level sections.")
    emit("WORTH A CLOSER LOOK", review)
    emit("BLOCKED (reason on record)", blocked)
    emit("SESSION-HARVEST (not a graduation candidate by design)", harvest_rows)
    emit("ALREADY GRADUATED / EXTRACTED", graduated_rows)

    print(
        "\nReminder: this narrows the search only. Promotion still requires a DFD-form "
        "proposal (THESIS/ANTI-THESIS/SYNTHESIS/CTA) and the Operator's own Y — "
        "bond:no-self-ratify, bond:kb-graduation."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

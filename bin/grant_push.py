#!/usr/bin/env python3
"""Grant dyad-bond's `bin/git.sh` push capability in a Claude Code settings file.

Adds the narrow allow-rule `Bash(bin/git.sh:*)` plus steward's destructive-push
deny-list (defense-in-depth) to a settings JSON file.

Properties:
  - idempotent   — re-running makes no further change once present
  - safe         — refuses on invalid/non-object JSON; never clobbers; atomic write
  - non-destructive — preserves all existing keys/values

Default target is .claude/settings.json (the checked-in tier). Use --path to point
at a temp copy for testing, or at .claude/settings.local.json for the local tier.

NOTE: executing this against the real settings file IS the permission grant — by the
covalent gate that is the Operator's act, never the Agent's self-grant.

This file is the *example-implementation* half of the substrate-access bundle; the
*understanding* half (trigger, traps, the two per-dyad questions) lives in
dialectic/substrate-access.md §The problem. Read that before copying this — the allow-rule
here is bond's particular (we wrap with bin/git.sh); yours may differ.
"""
import argparse
import json
import os
import pathlib
import sys
import tempfile

ALLOW = ["Bash(bin/git.sh:*)"]
DENY = [
    "Bash(git push --force*)",
    "Bash(git push * --force*)",
    "Bash(git push -f*)",
    "Bash(git push * -f*)",
    "Bash(git push --delete*)",
    "Bash(git push * --delete*)",
    "Bash(git push * -d*)",
    "Bash(git push +*)",
    "Bash(git push * +*)",
    "Bash(git push * :*)",
]


def grant(path):
    p = pathlib.Path(path)
    raw = p.read_text() if p.exists() else ""
    try:
        cfg = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        sys.exit(f"REFUSED: {p} is not valid JSON ({e}); leaving it untouched.")
    if not isinstance(cfg, dict):
        sys.exit(f"REFUSED: top-level of {p} is not a JSON object; leaving it untouched.")

    perms = cfg.setdefault("permissions", {})
    allow = perms.setdefault("allow", [])
    deny = perms.setdefault("deny", [])
    if not isinstance(allow, list) or not isinstance(deny, list):
        sys.exit(f"REFUSED: permissions.allow/deny in {p} are not lists; leaving it untouched.")

    added = []
    for a in ALLOW:
        if a not in allow:
            allow.append(a)
            added.append(("allow", a))
    for d in DENY:
        if d not in deny:
            deny.append(d)
            added.append(("deny", d))

    # atomic write: tmp in same dir + os.replace
    p.parent.mkdir(parents=True, exist_ok=True)
    out = json.dumps(cfg, indent=2) + "\n"
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=".settings-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(out)
        os.replace(tmp, p)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    if added:
        print(f"✓ {p}: added {len(added)} entr{'y' if len(added) == 1 else 'ies'}:")
        for kind, v in added:
            print(f"    +{kind}: {v}")
    else:
        print(f"✓ {p}: already complete — no change (idempotent).")
    print("\n--- resulting file ---")
    print(p.read_text(), end="")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--path", default=".claude/settings.json",
                    help="settings file to update (default: .claude/settings.json)")
    grant(ap.parse_args().path)


if __name__ == "__main__":
    main()

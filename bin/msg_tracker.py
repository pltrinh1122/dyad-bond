#!/usr/bin/env python3
"""bin/msg_tracker.py — dyad-bond per-dyad message-tracker (v0.1)

WHY (ours — racked by Operator 2026-06-18, s-local3): a fresh agent pulls a 📬 and
re-analyzes each DM in a vacuum, asserting what a prior message said *from memory* — which
twice this session got the remembered part right by luck but MISSED a real delta (cairn
softened self-ratification → handoff-for-validation). This tool mechanizes the discipline
the human-half could not hold under load:

    on each inbound, FORCE a fresh read and SURFACE the diff-against-prior;
    NEVER serve cached thread-state as truth (multi-writer-safe).

The corrected objective is NOT "reduce re-reads" (re-reading is the fix; on a multi-writer
substrate a read-reducing cache re-introduces the staleness bug). It is: force-the-diff,
distrust-the-cache. The stored snapshot is ONLY the 'prior' baseline for diffing; the CURRENT
state is ALWAYS fetched fresh from the substrate (gh → origin), never served from the DB.

Built ON falsify.py (dm discovery + gh helpers) — extend, don't re-derive. stdlib-only.

States per message:
  NEW       first time we've seen this key                       → snapshot + report
  CHANGED   blob sha differs from snapshot (re-send / edit)       → fetch fresh body, DIFF
  UNCHANGED blob sha matches snapshot                             → "already processed, identical"
  BLIND     could not fetch fresh state (gh/network)              → NOT 'unchanged' (cache-distrust)
"""
import sys, os, json, base64, difflib, re
from datetime import datetime, timezone

# --- build ON falsify.py (dm_items, _gh_json, find_ledger, read) ---
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "commons", "scripts"))
import falsify  # noqa: E402

ME = "dyad-bond"
DB_PATH = os.path.join(os.getcwd(), ".msg-tracker.json")  # cwd-local, gitignored (mirrors .falsify-seen.json)


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_db():
    try:
        return json.load(open(DB_PATH))
    except (FileNotFoundError, ValueError):
        return {"messages": {}}


def save_db(db):
    json.dump(db, open(DB_PATH, "w"), indent=1, sort_keys=True)


def fetch_body(file_dict):
    """ALWAYS fresh from origin. Returns (ok, body_or_None). gh reads GitHub's current state,
    so this is multi-writer-safe — a parallel session's push is reflected here, not cached."""
    url = file_dict.get("url")
    if not url:
        return False, None
    ok, _status, j = falsify._gh_json(url)
    if not ok or not j or "content" not in j:
        return False, None
    try:
        return True, base64.b64decode(j["content"]).decode("utf-8", "replace")
    except Exception:
        return False, None


def frontmatter(body):
    """Pull thread-linking fields (re/supersedes/reply-to/from/date) from YAML frontmatter."""
    out = {}
    if not body:
        return out
    for fld in ("re", "supersedes", "reply-to", "from", "date"):
        m = re.search(rf"^{fld}\s*:\s*(.+)$", body, re.MULTILINE)
        if m:
            out[fld] = m.group(1).strip()
    return out


def cmd_scan(_a):
    """The hero command. Fresh listing (live gh) → classify each msg vs the snapshot DB →
    surface diffs. The DB is updated only AFTER reporting, so every diff is old-snapshot vs fresh."""
    ledger = falsify.find_ledger(None)
    db = load_db()
    msgs = db["messages"]
    unreachable = []
    seen_keys = set()
    new, changed, unchanged, blind = [], [], [], []

    for sender, f, key in falsify.dm_items(ledger, ME, unreachable):
        seen_keys.add(key)
        fresh_sha = f.get("sha")
        prior = msgs.get(key)

        if prior is None:
            ok, body = fetch_body(f)
            if not ok:
                blind.append((key, "could not fetch new message body"))
                continue
            msgs[key] = {"sender": sender, "direction": "inbound", "sha": fresh_sha,
                         "first_seen": now_iso(), "last_fetched": now_iso(),
                         "body": body, **frontmatter(body)}
            new.append((key, body))
        elif fresh_sha and fresh_sha != prior.get("sha"):
            ok, body = fetch_body(f)
            if not ok:
                blind.append((key, "sha changed but body unfetchable — DELTA UNRESOLVED (not 'unchanged')"))
                continue
            old_body = prior.get("body", "")
            diff = list(difflib.unified_diff(
                old_body.splitlines(), body.splitlines(),
                fromfile=f"{key}@prior", tofile=f"{key}@now", lineterm=""))
            changed.append((key, diff))
            prior.update(sha=fresh_sha, last_fetched=now_iso(), body=body, **frontmatter(body))
        else:
            prior["last_fetched"] = now_iso()
            unchanged.append(key)

    save_db(db)

    # --- report: lead with what demands attention (NEW, CHANGED, BLIND); UNCHANGED is one line ---
    print(f"msg-tracker scan @ {now_iso()} — {ME}  (fresh-read; cache used only as prior baseline)")
    if blind:
        print("\n⚠ BLIND (could NOT confirm fresh state — NOT 'unchanged'):")
        for key, why in blind:
            print(f"  ⚠ {key}: {why}")
    if new:
        print(f"\n🆕 NEW ({len(new)}):")
        for key, body in new:
            fm = frontmatter(body)
            tag = f"  re: {fm['re']}" if fm.get("re") else ""
            print(f"  • {key}{tag}")
    if changed:
        print(f"\n✏️  CHANGED — re-send/edit, DIFF vs prior ({len(changed)}):")
        for key, diff in changed:
            print(f"  • {key}")
            for line in diff:
                print(f"      {line}")
    if unchanged:
        print(f"\n✓ UNCHANGED ({len(unchanged)}) — already processed, byte-identical, no re-analysis needed:")
        for key in unchanged:
            print(f"    {key}")
    # keys in DB no longer present in the fresh listing (deleted/moved upstream)
    gone = [k for k in msgs if msgs[k].get("direction") == "inbound" and k not in seen_keys]
    if gone:
        print(f"\n⚠ VANISHED ({len(gone)}) — in prior snapshot but absent from fresh listing (deleted/moved):")
        for k in gone:
            print(f"    {k}")
    if unreachable:
        print("\n" + falsify._unreachable_line(unreachable))
    if not (new or changed or blind):
        print("\n(no new or changed inbound — thread state current)")


def cmd_threads(_a):
    """Per-dyad thread view: inbound (tracked snapshots) + outbound (bond's local dm/<dyad>/),
    sorted by date, with un-responded inbound flagged. Outbound is read fresh from disk each call."""
    db = load_db()
    threads = {}
    for key, m in db["messages"].items():
        if m.get("direction") != "inbound":
            continue
        fn_in = key.split("/", 1)[-1]
        dmatch = re.match(r"(\d{4}-\d{2}-\d{2})", fn_in)
        # prefer frontmatter date; fall back to the filename prefix (cairn's plain-md DMs carry no date: field)
        idate = m.get("date") or (dmatch.group(1) if dmatch else "?")
        threads.setdefault(m["sender"], []).append(
            {"file": fn_in, "dir": "in", "date": idate, "re": m.get("re", "")})
    # outbound: bond's own sent messages live locally under dm/<dyad>/
    dm_root = os.path.join(os.getcwd(), "dm")
    if os.path.isdir(dm_root):
        for dyad in sorted(os.listdir(dm_root)):
            ddir = os.path.join(dm_root, dyad)
            if not os.path.isdir(ddir):
                continue
            for fn in sorted(os.listdir(ddir)):
                if not fn.endswith(".md"):
                    continue
                dm = re.match(r"(\d{4}-\d{2}-\d{2})", fn)
                threads.setdefault(dyad, []).append(
                    {"file": fn, "dir": "out", "date": dm.group(1) if dm else "?", "re": ""})
    if not threads:
        print("(no tracked threads — run `scan` first)")
        return
    for dyad in sorted(threads):
        items = sorted(threads[dyad], key=lambda x: (x["date"], x["dir"]))
        last_in = max((x["date"] for x in items if x["dir"] == "in"), default=None)
        last_out = max((x["date"] for x in items if x["dir"] == "out"), default=None)
        unresp = last_in and (not last_out or last_out < last_in)
        flag = "  ⚠ UN-RESPONDED (last inbound newer than last outbound)" if unresp else ""
        print(f"\n=== {dyad} ==={flag}")
        for x in items:
            arrow = "→ OUT" if x["dir"] == "out" else "← IN "
            ref = f"   re:{x['re']}" if x["re"] else ""
            print(f"  {x['date']}  {arrow}  {x['file']}{ref}")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    {"scan": cmd_scan, "threads": cmd_threads}.get(cmd, cmd_scan)(None)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Report agent-discovered strategies (file 52 change 4).

Lists every method the teacher invented in aggressive mode, how often it was used, its net
defeat rate, and maps each onto the established perturbation taxonomy so the taxonomy stays
principled: a discovered method that maps to a known family validates it; one that does not
is a genuine contribution.

  python tools/report_discovered.py --family 01
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import backends as B

DISCOVERED = B.STRATEGIES_DIR / "discovered"
LINEAGES_DIR = B.AGENTIC / "lineages"

# post-hoc taxonomy mapping (keyword heuristic over name+description)
_TAXONOMY = {
    "lexical": ["synonym", "rename", "lexical", "word", "term", "vocabulary", "phrasing"],
    "structural": ["reorder", "structure", "format", "reorganize", "layout", "nesting", "nested"],
    "semantic": ["semantic", "meaning", "narrative", "context", "scenario", "domain", "embed"],
    "misdirection": ["mislead", "misdirect", "distract", "decoy", "suggest", "imply", "cue", "false"],
}


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def classify(name, desc) -> str:
    text = f"{name} {desc}".lower()
    for fam, kws in _TAXONOMY.items():
        if any(k in text for k in kws):
            return fam
    return "novel"


def net_defeats_at(lineage_json, depth):
    """New defeats produced by the edit that created `depth` (raw_defeated[d] - [d-1])."""
    per = {e["depth"]: e for e in lineage_json.get("per_depth", [])}
    cur = set(per.get(depth, {}).get("raw_defeated", []))
    prev = set(per.get(depth - 1, {}).get("raw_defeated", []))
    return len(cur - prev), len(prev - cur)   # (newly defeated, regressed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    args = ap.parse_args()

    # cache lineage.json per (criterion, lineage)
    lin_cache = {}

    def lineage_json(crit, lineage):
        k = (crit, lineage)
        if k not in lin_cache:
            lin_cache[k] = _read_json(LINEAGES_DIR / f"family_{args.family}" / crit / lineage / "lineage.json")
        return lin_cache[k]

    rows = []
    for crit_dir in sorted(p.name for p in DISCOVERED.glob("criterion_*")) if DISCOVERED.exists() else []:
        for mj in sorted((DISCOVERED / crit_dir).glob("*.json")):
            m = _read_json(mj)
            if not m:
                continue
            defeated = regressed = 0
            for u in m.get("uses", []):
                lj = lineage_json(crit_dir, u.get("lineage", ""))
                if lj:
                    d, r = net_defeats_at(lj, u.get("depth", 0))
                    defeated += d; regressed += r
            rows.append({"criterion": crit_dir, "method": m.get("name", mj.stem),
                         "novel_self": m.get("novel", "?"),
                         "taxonomy": classify(m.get("name", ""), m.get("description", "")),
                         "uses": len(m.get("uses", [])),
                         "net_defeated": defeated - regressed,
                         "defeated": defeated, "regressed": regressed})

    if not rows:
        print("[report_discovered] no discovered methods yet "
              f"(none under {DISCOVERED}). Aggressive mode may not have triggered.")
        return

    out = B.REPORTS_DIR / "discovered_methods.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, indent=2))

    print(f"{'criterion':<22} {'method':<34} {'taxonomy':<12} {'uses':>4} "
          f"{'net':>4} {'novel?':>6}")
    for r in sorted(rows, key=lambda x: -x["net_defeated"]):
        print(f"{r['criterion']:<22} {r['method'][:34]:<34} {r['taxonomy']:<12} "
              f"{r['uses']:>4} {r['net_defeated']:>+4} {r['novel_self']:>6}")

    by_tax = defaultdict(int)
    for r in rows:
        by_tax[r["taxonomy"]] += 1
    print(f"\ntaxonomy coverage: {dict(by_tax)}  "
          f"(methods mapping to 'novel' are genuine contributions; the rest validate known families)")
    print(f"[report_discovered] wrote {out}")


if __name__ == "__main__":
    main()

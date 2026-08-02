#!/usr/bin/env python3
"""Aggregate attempts into a CSV and a printed review queue.

reports/family_XX_summary.csv rows:
  criterion, class_label, version, source, strategies, intensity, generation, parent,
  gate_result, student, verdict, n_cases, n_passed

Printed:
  - seed baseline: pass rate per student on v000 (the unmodified seed),
  - per version: students passed and the delta from the seed baseline,
  - versions ranked by delta (biggest drops first) -- the manual-review queue,
  - a per-strategy rollup, and a per-SOURCE rollup (does composition / next-generation
    beat the base grid?).

CLI: python tools/report.py --family 01|all
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import backends as B

from harness.dataset import discover_criteria


def class_labels(slug):
    return {c.criterion_id: c.meta.get("class", "?")
            for c in discover_criteria(B.SEEDS_DIR / slug)}


def read_json(p: Path):
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def collect(family, slug):
    labels = class_labels(slug)
    abase = B.ATTEMPTS_DIR / f"family_{family}"
    vbase = B.VERSIONS_DIR / f"family_{family}"
    rows = []
    if not abase.exists():
        return rows
    for cdir in sorted(abase.glob("criterion_*")):
        cd = cdir.name
        for vdir in sorted(cdir.glob("v*")):
            vid = vdir.name
            edit = read_json(vbase / cd / vid / "edit.json")
            gate = read_json(vbase / cd / vid / "gate.json")
            strategies = edit.get("strategies")
            strat_str = "+".join(strategies) if strategies else \
                ("seed" if vid == "v000" else edit.get("strategy", "?"))
            for sdir in sorted(vdir.glob("*")):
                verdict = read_json(sdir / "verdict.json")
                if not verdict:
                    continue
                rows.append({
                    "criterion": cd,
                    "class_label": labels.get(cd, "?"),
                    "version": vid,
                    "source": edit.get("source", "seed" if vid == "v000" else "?"),
                    "strategies": strat_str,
                    "intensity": edit.get("intensity", "-"),
                    "generation": edit.get("generation", 0 if vid == "v000" else "?"),
                    "parent": edit.get("parent", "-"),
                    "gate_result": gate.get("result", "SEED" if vid == "v000" else "-"),
                    "student": sdir.name,
                    "verdict": verdict.get("overall", "?"),
                    "n_cases": verdict.get("n_cases", 0),
                    "n_passed": verdict.get("n_passed", 0),
                })
    return rows


COLS = ["criterion", "class_label", "version", "source", "strategies", "intensity",
        "generation", "parent", "gate_result", "student", "verdict", "n_cases", "n_passed"]


def report_family(family):
    slug = B.family_slug(family)
    rows = collect(family, slug)
    B.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = B.REPORTS_DIR / f"family_{family}_summary.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print(f"\n########## family {family} ##########")
    print(f"Wrote {len(rows)} rows to {csv_path}")
    if not rows:
        print("(no attempts yet)")
        return

    passed = lambda r: r["verdict"] == "PASS"
    baseline = defaultdict(dict)  # criterion -> student -> passed
    for r in rows:
        if r["version"] == "v000":
            baseline[r["criterion"]][r["student"]] = passed(r)

    students = sorted({r["student"] for r in rows})
    print("\n== Seed baseline (v000) pass rate per student ==")
    for s in students:
        vals = [baseline[c].get(s) for c in baseline if s in baseline[c]]
        print(f"  {s:24} {sum(1 for v in vals if v)}/{len(vals)}")

    grp = defaultdict(list)  # (criterion, version) -> rows
    meta = {}
    for r in rows:
        if r["version"] == "v000":
            continue
        grp[(r["criterion"], r["version"])].append(r)
        meta[(r["criterion"], r["version"])] = (r["source"], r["strategies"], r["intensity"])

    stats = []
    for (cd, vid), rs in grp.items():
        n_pass = sum(1 for r in rs if passed(r))
        base_pass = sum(1 for v in baseline.get(cd, {}).values() if v)
        src, strat, inten = meta[(cd, vid)]
        stats.append((n_pass - base_pass, cd, vid, src, strat, inten, n_pass, base_pass, len(rs)))

    stats.sort()
    print("\n== Versions ranked by delta from seed baseline (biggest drops first) ==")
    print(f"  {'delta':>6}  {'criterion':22} {'ver':6} {'source':11} {'strategies':14} "
          f"{'inten':9} pass base")
    for d, cd, vid, src, strat, inten, np_, bp, tot in stats:
        print(f"  {d:>+6}  {cd:22} {vid:6} {src:11} {strat:14} {inten:9} {np_}/{tot}   {bp}")

    strat_delta = defaultdict(list)
    src_delta = defaultdict(list)
    for d, cd, vid, src, strat, inten, np_, bp, tot in stats:
        strat_delta[strat].append(d)
        src_delta[src].append(d)
    print("\n== Per-strategy rollup (avg delta; most negative = most effective) ==")
    for k, ds in sorted(strat_delta.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
        print(f"  {k:16} avg_delta={sum(ds)/len(ds):+.2f}  n={len(ds)}")
    print("\n== Per-source rollup (grid vs sample vs composition vs generation) ==")
    for k, ds in sorted(src_delta.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
        print(f"  {k:16} avg_delta={sum(ds)/len(ds):+.2f}  n={len(ds)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    args = ap.parse_args()
    for family in B.list_families(args.family):
        report_family(family)


if __name__ == "__main__":
    main()

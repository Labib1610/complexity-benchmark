#!/usr/bin/env python3
"""Report the frontier evaluation (file 51).

Reads frontier_eval/family_XX/**/result.json and writes reports/frontier_eval.csv
(one row per lineage x which x model x tier x case), then prints:

  1. Correctness (time ignored): seed vs final solve-rate per criterion x model, per tier.
  2. Runtime (the headline): median / p90 / max case time; how many statements have a case
     exceeding 1 s / 10 s / 60 s.
  3. Reference comparison (--reference): frontier_time / reference_time per case.
  4. Seed vs final: did solve-rate drop and runtime rise from d000 to the final depth.
  5. Cross-check vs the 4-student panel: frontier solve-rate vs student solve-rate.

  python tools/report_frontier.py --family 01 [--reference]
"""
import argparse
import csv
import dataclasses
import json
from collections import defaultdict
from pathlib import Path

import backends as B
import gate as GT

from harness.dataset import TestCase
from harness.runner import run_solution

FRONTIER_DIR = B.AGENTIC / "frontier_eval"
LINEAGES_DIR = B.AGENTIC / "lineages"
_TIERS = ("anchor", "corner", "scaled")
DEFAULT_CEILING_S = 3600   # reference runaway guard only; 0 = unbounded (matches frontier_eval)


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _pct(xs, q):
    xs = sorted(xs)
    if not xs:
        return None
    i = min(len(xs) - 1, int(round(q * (len(xs) - 1))))
    return round(xs[i], 3)


def load_results(family):
    base = FRONTIER_DIR / f"family_{family}"
    out = []
    for rj in base.glob("*/*/*/*/result.json"):   # crit/L/which/model/result.json
        d = _read_json(rj)
        if d:
            out.append(d)
    return out


def write_csv(family, results):
    path = B.REPORTS_DIR / "frontier_eval.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["criterion", "lineage", "which", "model", "tier",
                    "case", "verdict", "elapsed_s", "gen_elapsed_s", "cost"])
        for r in results:
            for tier in _TIERS:
                t = (r.get("tiers") or {}).get(tier)
                if not t:
                    continue
                for c in t["cases"]:
                    w.writerow([r["criterion"], r["lineage"], r["which"], r["model"], tier,
                                c["name"], c["verdict"], c.get("elapsed_s"),
                                r.get("gen_elapsed_s"), r.get("cost")])
    return path


# file 52: a PASS slower than the threshold counts as too-slow -> a DEFEAT, and
# EXCEEDED_CEILING is already a failure. TLE_THRESHOLD_S is set from --tle-threshold.
TLE_THRESHOLD_S = 300


def _case_solved(c):
    """A case is 'solved' only if PASS AND within the TLE threshold (file 52)."""
    return c["verdict"] == "PASS" and (c.get("elapsed_s") or 0) <= TLE_THRESHOLD_S


def _tier_solved(r, tier):
    t = (r.get("tiers") or {}).get(tier)
    if not t or t["total"] == 0:
        return False
    return all(_case_solved(c) for c in t["cases"])


def _all_solved(r):
    """Solved across every tier AND within the TLE threshold (threshold-aware solved_all)."""
    tiers = [t for t in _TIERS if (r.get("tiers") or {}).get(t)]
    return bool(tiers) and all(_tier_solved(r, t) for t in tiers)


# --- 1 + 4: correctness, seed vs final --------------------------------------
def report_correctness(results):
    by = defaultdict(dict)   # (crit, model, which) -> {tier: [solved bools], overall:[...]}
    for r in results:
        key = (r["criterion"], r["model"], r["which"])
        d = by.setdefault(key, {t: [] for t in _TIERS} | {"overall": []})
        for t in _TIERS:
            if (r.get("tiers") or {}).get(t):
                d[t].append(_tier_solved(r, t))
        d["overall"].append(_all_solved(r))

    print("\n=== 1. Correctness (time ignored) -- solved-rate by tier ===")
    print(f"{'criterion':<22} {'model':<26} {'which':<6} "
          + " ".join(f'{t:>8}' for t in _TIERS) + f" {'overall':>8}")
    for key in sorted(by):
        crit, model, which = key
        d = by[key]
        cells = []
        for t in _TIERS + ("overall",):
            v = d[t]
            cells.append(f"{(sum(v)/len(v)*100):6.0f}%" if v else "    -  ")
        print(f"{crit:<22} {model:<26} {which:<6} " + " ".join(f'{c:>8}' for c in cells))

    print("\n=== 4. Seed -> final (did hardening move the frontier model?) ===")
    print(f"{'criterion':<22} {'model':<26} {'seed_solved':>11} {'final_solved':>12} "
          f"{'delta':>7} {'seed_maxT':>9} {'final_maxT':>10}")
    # aggregate max_elapsed per (crit,model,which)
    maxt = defaultdict(list)
    solved = defaultdict(list)
    for r in results:
        maxt[(r["criterion"], r["model"], r["which"])].append(r.get("max_elapsed_s") or 0)
        solved[(r["criterion"], r["model"], r["which"])].append(_all_solved(r))
    combos = sorted({(c, m) for (c, m, _w) in solved})
    for crit, model in combos:
        ss = solved.get((crit, model, "seed"), [])
        fs = solved.get((crit, model, "final"), [])
        sr = sum(ss) / len(ss) if ss else 0
        fr = sum(fs) / len(fs) if fs else 0
        smt = (sum(maxt.get((crit, model, "seed"), [0])) / max(1, len(maxt.get((crit, model, "seed"), [1]))))
        fmt = (sum(maxt.get((crit, model, "final"), [0])) / max(1, len(maxt.get((crit, model, "final"), [1]))))
        print(f"{crit:<22} {model:<26} {sr*100:>10.0f}% {fr*100:>11.0f}% "
              f"{(fr-sr)*100:>+6.0f}% {smt:>8.2f}s {fmt:>9.2f}s")


# --- 2: runtime ------------------------------------------------------------
def report_runtime(results):
    times = defaultdict(list)          # (crit,model,which) -> [case elapsed]
    stmt_max = defaultdict(list)       # (crit,model,which) -> [max per statement]
    slowest = {}                       # (crit,model,which) -> (elapsed, label)
    for r in results:
        key = (r["criterion"], r["model"], r["which"])
        for t in _TIERS:
            tt = (r.get("tiers") or {}).get(t)
            if not tt:
                continue
            for c in tt["cases"]:
                e = c.get("elapsed_s") or 0
                times[key].append(e)
                if key not in slowest or e > slowest[key][0]:
                    slowest[key] = (e, f"{r['lineage']}/{t}/{c['name']}")
        stmt_max[key].append(r.get("max_elapsed_s") or 0)

    print("\n=== 2. Runtime (headline) -- per-case wall-clock ===")
    print(f"{'criterion':<22} {'model':<26} {'which':<6} {'median':>8} {'p90':>8} "
          f"{'max':>9} slowest_case")
    for key in sorted(times):
        crit, model, which = key
        xs = times[key]
        s = slowest.get(key, (0, "-"))
        print(f"{crit:<22} {model:<26} {which:<6} {_pct(xs,.5):>7}s {_pct(xs,.9):>7}s "
              f"{max(xs):>8.2f}s {s[1]}")

    print("\n   statements with a case exceeding a threshold (per crit x model x which):")
    print(f"{'criterion':<22} {'model':<26} {'which':<6} {'>1s':>5} {'>10s':>5} {'>60s':>5} "
          f"{'>'+str(TLE_THRESHOLD_S)+'s(DEF)':>12} {'n':>4}")
    for key in sorted(stmt_max):
        crit, model, which = key
        xs = stmt_max[key]
        print(f"{crit:<22} {model:<26} {which:<6} "
              f"{sum(1 for x in xs if x>1):>5} {sum(1 for x in xs if x>10):>5} "
              f"{sum(1 for x in xs if x>60):>5} {sum(1 for x in xs if x>TLE_THRESHOLD_S):>12} {len(xs):>4}")


# --- 3: reference comparison (optional; re-executes the reference) ----------
def report_reference(family, results, ceiling):
    print("\n=== 3. Reference comparison (frontier_time / reference_time) ===")
    slug = B.family_slug(family)
    ref_cache = {}   # (crit, tier, case) -> reference elapsed_s

    def ref_time(crit_dir, sc, tier, tc):
        k = (crit_dir, tier, tc.name)
        if k in ref_cache:
            return ref_cache[k]
        mem = int(sc.meta.get("memory_limit_mb", 256))
        rr = run_solution(sc.reference_path, tc.in_path.read_text(), (ceiling or None), mem)
        ref_cache[k] = rr.elapsed_s if rr.status == "OK" else None
        return ref_cache[k]

    # build a case index for tests so we can find the TestCase object per (crit,tier,name)
    from frontier_eval import build_tiers
    ratios = defaultdict(list)   # (crit,model,which) -> [ratio]
    for r in results:
        crit_dir = r["criterion"]
        sc = GT.seed_criterion(slug, crit_dir)
        if sc is None:
            continue
        tiers = build_tiers(family, slug, crit_dir, sc)
        for t in _TIERS:
            tt = (r.get("tiers") or {}).get(t)
            if not tt:
                continue
            by_name = {tc.name: tc for tc in (tiers.get(t) or [])}
            for c in tt["cases"]:
                if c["verdict"] != "PASS":
                    continue
                tc = by_name.get(c["name"])
                if tc is None:
                    continue
                rt = ref_time(crit_dir, sc, t, tc)
                if rt and rt > 0:
                    ratios[(crit_dir, r["model"], r["which"])].append((c["elapsed_s"] or 0) / rt)
    print(f"{'criterion':<22} {'model':<26} {'which':<6} {'median_ratio':>12} {'max_ratio':>10} {'n':>4}")
    for key in sorted(ratios):
        crit, model, which = key
        xs = ratios[key]
        print(f"{crit:<22} {model:<26} {which:<6} {_pct(xs,.5):>11}x {max(xs):>9.1f}x {len(xs):>4}")


# --- 5: cross-check vs the student panel ------------------------------------
def report_panel_crosscheck(family, results):
    print("\n=== 5. Frontier vs 4-student panel (solve-rate on the same statements) ===")
    # student solve at a depth = raw_passers / n_panel, from lineage.json per_depth
    student = {}   # (crit, lineage, which) -> solved_fraction
    lbase = LINEAGES_DIR / f"family_{family}"
    for lj_path in lbase.glob("*/L*/lineage.json"):
        lj = _read_json(lj_path)
        crit = lj.get("criterion") or lj_path.parts[-3]
        fd = lj.get("final_depth", 0)
        per = {e.get("depth"): e for e in lj.get("per_depth", [])}
        npanel = len(lj.get("baseline_pass", {})) or 4
        for which, depth in (("seed", 0), ("final", fd)):
            e = per.get(depth)
            if e is not None:
                student[(crit, lj["lineage"], which)] = len(e.get("raw_passers", [])) / npanel

    # frontier solve (overall) per (crit, lineage, which), averaged over evaluator models
    front = defaultdict(list)
    for r in results:
        front[(r["criterion"], r["lineage"], r["which"])].append(_all_solved(r))

    agg = defaultdict(lambda: {"f": [], "s": []})
    for key, fs in front.items():
        crit, lineage, which = key
        agg[(crit, which)]["f"].append(sum(fs) / len(fs))
        if key in student:
            agg[(crit, which)]["s"].append(student[key])
    print(f"{'criterion':<22} {'which':<6} {'frontier_solve':>14} {'student_solve':>13} {'gap':>7}")
    for key in sorted(agg):
        crit, which = key
        f = agg[key]["f"]; s = agg[key]["s"]
        fr = sum(f)/len(f) if f else 0
        sr = sum(s)/len(s) if s else 0
        print(f"{crit:<22} {which:<6} {fr*100:>13.0f}% {sr*100:>12.0f}% {(fr-sr)*100:>+6.0f}%")


def main():
    global TLE_THRESHOLD_S
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--reference", action="store_true",
                    help="also re-run the reference per case for the ratio table (slower)")
    ap.add_argument("--ceiling", type=int, default=DEFAULT_CEILING_S,
                    help="reference runaway guard in seconds (0 = unbounded)")
    ap.add_argument("--tle-threshold", type=int, default=TLE_THRESHOLD_S,
                    help="file 52: a PASS slower than this counts as too-slow = a DEFEAT")
    args = ap.parse_args()

    TLE_THRESHOLD_S = args.tle_threshold
    print(f"[frontier-report] TLE threshold = {TLE_THRESHOLD_S}s "
          f"(a correct-but-slower solution counts as defeated)")

    results = load_results(args.family)
    if not results:
        raise SystemExit(f"no frontier results under {FRONTIER_DIR / f'family_{args.family}'} "
                         f"-- run tools/frontier_eval.py first")
    path = write_csv(args.family, results)
    print(f"[frontier-report] {len(results)} statement-evaluations -> {path}")
    report_correctness(results)
    report_runtime(results)
    if args.reference:
        report_reference(args.family, results, args.ceiling)
    report_panel_crosscheck(args.family, results)


if __name__ == "__main__":
    main()

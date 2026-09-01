#!/usr/bin/env python3
"""Report the feedback-driven lineages (files 46 + 48).

Survival depth replaces delta. Retirement is steering-only: the survival curve is
plotted from RAW passers (every student, ignoring retirement) with the active
(non-retired) count shown as a secondary "steering pool" line (file 48 Change 1).

Three test tiers are scored separately and never merged (file 48 Change 2):
  anchor  (cases 01-04)  -> basic correctness
  corner  (gen_tests)    -> coding correctness / edge cases
  scaled  (cases 05+)    -> intractability
Two survival curves per criterion isolate the two effects: anchor+corner measures
whether STATEMENT hardening works; scaled measures whether INSTANCE hardness bites.
Failure types are split (file 48 Change 3): TLE on scaled = on-thesis (intractable
algorithm); WRONG_ANSWER on anchor/corner = off-thesis coding noise.

Writes reports/family_XX_lineages.csv (one row per criterion, lineage, depth,
student, tier).

CLI: python tools/report_lineage.py --family 01
"""
import argparse
import csv
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import backends as B

TIERS = ("anchor", "corner", "scaled")
VERDICT_TYPES = ("PASS", "WRONG_ANSWER", "TLE", "RUNTIME_ERROR", "MLE")
TIMING_FRACTION = 0.20   # warn when a scaled PASS is within 20% of the time limit


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def collect(family):
    base = B.AGENTIC / "lineages" / f"family_{family}"
    lineages = []
    if base.exists():
        for cdir in sorted(base.glob("criterion_*")):
            for ldir in sorted(cdir.glob("L*")):
                lj = _read_json(ldir / "lineage.json")
                if lj:
                    lineages.append(lj)
    return lineages


def _tier(entry, sid, tier):
    return (entry.get("tier_verdicts") or {}).get(sid, {}).get(tier)


def _tier_pass(tr):
    return bool(tr) and tr.get("total", 0) > 0 and tr["passed"] == tr["total"]


def _students_at(entry):
    return list((entry.get("tier_verdicts") or {}).keys())


COLS = ["criterion", "lineage", "base_version", "base_strategy", "depth", "student", "tier",
        "tier_passed", "tier_total", "verdict_type", "first_tle_case", "retired_flag",
        "shortcut_name", "structural_floor", "gate_result", "outcome"]


def _curve(ljs, count_fn):
    """Average passer count per depth across a criterion's lineages (skips lineages
    that lack the tier). Returns list of 'dN:x.x' strings, or None if no data."""
    maxd = max((len(lj.get("per_depth", [])) for lj in ljs), default=0)
    out, any_data = [], False
    for d in range(maxd):
        vals = []
        for lj in ljs:
            pd = lj.get("per_depth", [])
            if d < len(pd):
                c = count_fn(pd[d])
                if c is not None:
                    vals.append(c)
        if vals:
            any_data = True
            out.append(f"d{d}:{statistics.mean(vals):.1f}")
        else:
            out.append(f"d{d}:-")
    return out if any_data else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    args = ap.parse_args()

    for family in B.list_families(args.family):
        lineages = collect(family)
        B.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        csv_path = B.REPORTS_DIR / f"family_{family}_lineages.csv"
        rows = []
        for lj in lineages:
            strat = "+".join(lj.get("base_strategy") or []) if isinstance(lj.get("base_strategy"), list) else lj.get("base_strategy")
            for d in lj.get("per_depth", []):
                retired = set(d.get("retired", []))
                verdicts = d.get("verdicts") or {}
                tv = d.get("tier_verdicts") or {}
                # one row per (criterion, lineage, depth, student). Tier columns are
                # OPTIONAL: pre-tier lineages have no tier data but must still be written.
                students = list(tv.keys()) or list(verdicts.keys())
                for student in students:
                    base = {
                        "criterion": lj["criterion"], "lineage": lj["lineage"],
                        "base_version": lj.get("base_version"), "base_strategy": strat,
                        "depth": d["depth"], "student": student,
                        "retired_flag": student in retired,
                        "shortcut_name": d.get("shortcut_name"),
                        "structural_floor": d.get("structural_floor"),
                        "gate_result": d.get("gate_result"), "outcome": lj.get("outcome"),
                    }
                    tiers_present = [t for t in TIERS if tv.get(student, {}).get(t) is not None]
                    if tiers_present:
                        for tier in tiers_present:
                            tr = tv[student][tier]
                            rows.append({**base, "tier": tier,
                                         "tier_passed": tr["passed"], "tier_total": tr["total"],
                                         "verdict_type": tr["verdict_type"],
                                         "first_tle_case": tr.get("first_tle")})
                    else:
                        rows.append({**base, "tier": None, "tier_passed": None,
                                     "tier_total": None, "verdict_type": verdicts.get(student),
                                     "first_tle_case": None})
        with open(csv_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            w.writeheader(); w.writerows(rows)
        print(f"\n########## family {family} ##########")
        print(f"Wrote {len(rows)} rows to {csv_path}  ({len(lineages)} lineages)")
        if not lineages:
            print("(no lineages yet -- run tools/harden_loop.py)")
            continue

        by_crit = defaultdict(list)
        for lj in lineages:
            by_crit[lj["criterion"]].append(lj)

        # ---- survival curves (Change 1 raw metric + Change 3 per-tier) --------
        print("\n== Survival curves (avg # students at each depth) ==")
        print("   raw     = every student still CORRECT, ignoring retirement "
              "(file 52: the PRIMARY correctness metric)")
        print("   defeat  = students DEFEATED (WRONG_ANSWER/RUNTIME_ERROR) -- the hardening signal")
        print("   steer   = active, non-retired steering pool (declines by construction)")
        print("   a+c     = passing anchor AND corner (does statement hardening work?)")
        print("   scaled  = passing the scaled tier -- file 52: now a TIMING measure, not difficulty")
        for crit, ljs in sorted(by_crit.items()):
            print(f"\n  [{crit}]")

            def raw_count(e):
                # RAW = every student, ignoring retirement. Prefer the recorded field
                # (new runs); otherwise recount from verdicts (old lineages have no
                # raw_passers). NEVER derive from `passers` -- that excludes retired.
                if e.get("raw_passers") is not None:
                    return len(e["raw_passers"])
                v = e.get("verdicts")
                if not v:
                    return None                  # unmeasured depth -> skip
                return sum(1 for x in v.values() if x == "PASS")

            def defeat_count(e):
                # file 52 change 1: students defeated on correctness (WRONG_ANSWER/RUNTIME_ERROR)
                if e.get("raw_defeated") is not None:
                    return len(e["raw_defeated"])
                v = e.get("verdicts")
                if not v:
                    return None
                return sum(1 for x in v.values() if x in ("WRONG_ANSWER", "RUNTIME_ERROR"))

            def steer_count(e):
                # steering pool = non-retired students that PASSED (not pool size)
                if not (e.get("verdicts") or e.get("raw_passers") is not None):
                    return None
                return len(e.get("passers", []))

            def ac_count(e):
                sids = _students_at(e)
                if not sids:
                    return None
                return sum(1 for s in sids if _tier_pass(_tier(e, s, "anchor"))
                           and _tier_pass(_tier(e, s, "corner")))

            def scaled_count(e):
                sids = [s for s in _students_at(e) if _tier(e, s, "scaled") is not None]
                if not sids:
                    return None
                return sum(1 for s in sids if _tier_pass(_tier(e, s, "scaled")))

            for label, fn in [("raw   ", raw_count), ("defeat", defeat_count),
                              ("steer ", steer_count),
                              ("a+c   ", ac_count), ("scaled", scaled_count)]:
                curve = _curve(ljs, fn)
                print(f"    {label} {'  '.join(curve)}" if curve
                      else f"    {label} (no data -- tier absent)")

        # ---- per-depth verdict-type breakdown, split by tier (Change 3) -------
        print("\n== Verdict-type breakdown per depth, per tier "
              "(TLE@scaled = on-thesis; WRONG_ANSWER@anchor/corner = coding noise) ==")
        for crit, ljs in sorted(by_crit.items()):
            maxd = max((len(lj.get("per_depth", [])) for lj in ljs), default=0)
            print(f"\n  [{crit}]")
            for d in range(maxd):
                per_tier = {t: Counter() for t in TIERS}
                for lj in ljs:
                    pd = lj.get("per_depth", [])
                    if d >= len(pd):
                        continue
                    e = pd[d]
                    for s in _students_at(e):
                        for t in TIERS:
                            tr = _tier(e, s, t)
                            if tr is not None:
                                per_tier[t][tr["verdict_type"]] += 1
                cells = []
                for t in TIERS:
                    if sum(per_tier[t].values()) == 0:
                        continue
                    parts = " ".join(f"{v}={per_tier[t][v]}" for v in VERDICT_TYPES if per_tier[t][v])
                    cells.append(f"{t}[{parts}]")
                print(f"    d{d}: {'  '.join(cells) if cells else '(no tier data)'}")

        # ---- per-student scaled-tier stats (Change 3) -------------------------
        scaled_pass = defaultdict(lambda: [0, 0])   # student -> [passed, total]
        first_tles = defaultdict(Counter)
        for lj in lineages:
            for e in lj.get("per_depth", []):
                for s in _students_at(e):
                    tr = _tier(e, s, "scaled")
                    if tr is None:
                        continue
                    scaled_pass[s][1] += 1
                    if _tier_pass(tr):
                        scaled_pass[s][0] += 1
                    if tr.get("first_tle"):
                        first_tles[s][tr["first_tle"]] += 1
        if scaled_pass:
            print("\n== Per-student scaled tier (intractability) ==")
            for s in sorted(scaled_pass, key=lambda k: scaled_pass[k][0] / max(1, scaled_pass[k][1])):
                p, n = scaled_pass[s]
                ft = first_tles[s].most_common(1)
                ft_s = f"first_tle={ft[0][0]}" if ft else "first_tle=-"
                print(f"  {s:24} scaled_pass_rate={p}/{n} ({p/max(1,n):.0%})  {ft_s}")

        # ---- timing fragility warning (Change 3 note) -------------------------
        fragile = []
        for lj in lineages:
            for e in lj.get("per_depth", []):
                for s in _students_at(e):
                    tr = _tier(e, s, "scaled")
                    if not tr:
                        continue
                    lim = tr.get("time_limit_s")
                    if not lim:
                        continue
                    for c in tr.get("verdicts", []):
                        if c["verdict"] == "PASS" and c["elapsed_s"] >= (1 - TIMING_FRACTION) * lim:
                            fragile.append((lj["lineage"], e["depth"], s, c["name"],
                                            c["elapsed_s"], lim))
        if fragile:
            print(f"\n== ⚠ TIMING FRAGILITY ==  {len(fragile)} scaled PASS(es) within "
                  f"{int(TIMING_FRACTION*100)}% of the limit -- machine load could flip these to TLE:")
            for lin, dp, s, cse, el, lim in fragile[:20]:
                print(f"    {lin} d{dp} {s} case {cse}: {el:.2f}s / {lim}s")
            if len(fragile) > 20:
                print(f"    ... and {len(fragile) - 20} more")

        # ---- depth-to-defeat per student --------------------------------------
        dtd = defaultdict(list)
        for lj in lineages:
            for student, depth in (lj.get("depth_to_defeat") or {}).items():
                if depth is not None:
                    dtd[student].append(depth)
        print("\n== Depth-to-defeat per student (median depth of first failure; higher = more robust) ==")
        for student, ds in sorted(dtd.items(), key=lambda kv: -statistics.median(kv[1])):
            print(f"  {student:24} median={statistics.median(ds):.1f}  n_defeated={len(ds)}")

        # ---- lineage outcomes + stop reasons ----------------------------------
        oc = Counter(lj.get("outcome") for lj in lineages)
        sr = Counter(lj.get("stop_reason") for lj in lineages)
        print(f"\n== Lineage outcomes ==  {dict(oc)}")
        print(f"== Stop reasons ==     {dict(sr)}")

        # ---- structural floor (Part E) ----------------------------------------
        floors = [d.get("structural_floor") for lj in lineages for d in lj.get("per_depth", [])
                  if d.get("shortcut_name")]
        n_floor = sum(1 for x in floors if x == "yes")
        if floors:
            print(f"\n== Structural floor ==  {n_floor}/{len(floors)} named shortcuts are the CORE "
                  f"task itself (unremovable by rewording) -- a real limit on surface hardening.")

        # ---- shortcut taxonomy ------------------------------------------------
        sc = Counter(d.get("shortcut_name") for lj in lineages for d in lj.get("per_depth", [])
                     if d.get("shortcut_name"))
        print("\n== Shortcut taxonomy (most-relied-on affordances) ==")
        for name, cnt in sc.most_common(12):
            print(f"  {cnt:>3}x  {name}")

        # ---- base-version yield -----------------------------------------------
        yld = Counter()
        for lj in lineages:
            if lj.get("outcome") == "all_defeated":
                s = lj.get("base_strategy")
                s = "+".join(s) if isinstance(s, list) else str(s)
                yld[s] += 1
        print("\n== Base-version yield (strategies that produced fully-defeating lineages) ==")
        for s, cnt in yld.most_common():
            print(f"  {cnt:>3}x  {s}")


if __name__ == "__main__":
    main()

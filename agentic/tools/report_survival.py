#!/usr/bin/env python3
"""Per-model survival scorecard across depths (file 52 follow-up).

For every student (and, if frontier eval has run, every frontier evaluator), reports how
many problems it passed vs failed -- split into correct / wrong / too-slow -- across all
depths and, separately, in the FINAL layer (each lineage's last statement). The headline is
the fraction of models defeated in the final layer (the target). Also reports, per
criterion, the best simultaneous-defeat fraction reached at any depth -- the honest ceiling
of how hard the statements got, which is a finding even when it is below 100%.

  python tools/report_survival.py --family 01 [--tle-threshold 300]
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import backends as B

LINEAGES_DIR = B.AGENTIC / "lineages"
FRONTIER_DIR = B.AGENTIC / "frontier_eval"


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _bucket(vt: str) -> str:
    if vt == "PASS":
        return "correct"
    if vt == "TLE":
        return "too_slow"
    return "wrong"          # WRONG_ANSWER / RUNTIME_ERROR / MLE / other


def collect(family):
    """Return (per_model, final_layer, crit_ceiling)."""
    per_model = defaultdict(lambda: defaultdict(int))     # model -> bucket -> count (all depths)
    final_layer = defaultdict(lambda: defaultdict(int))   # model -> bucket -> count (final only)
    crit_ceiling = defaultdict(list)                      # crit -> [best defeat fraction per lineage]

    base = LINEAGES_DIR / f"family_{family}"
    for lj_path in base.glob("*/L*/lineage.json") if base.exists() else []:
        lj = _read_json(lj_path)
        if not lj:
            continue
        crit = lj.get("criterion") or lj_path.parts[-3]
        per = lj.get("per_depth", [])
        n_students = len(lj.get("baseline_pass", {})) or 4
        best_frac = 0.0
        for e in per:
            v = e.get("verdicts", {})
            for sid, vt in v.items():
                per_model[sid][_bucket(vt)] += 1
            defeated = len(e.get("raw_defeated", []))
            best_frac = max(best_frac, defeated / max(1, n_students))
        crit_ceiling[crit].append(best_frac)
        if per:
            v = per[-1].get("verdicts", {})
            for sid, vt in v.items():
                final_layer[sid][_bucket(vt)] += 1

    # frontier evaluators (final statements), if present
    fbase = FRONTIER_DIR / f"family_{family}"
    for rj in fbase.glob("*/*/final/*/result.json") if fbase.exists() else []:
        r = _read_json(rj)
        if not r:
            continue
        model = "[frontier] " + r.get("model", rj.parts[-2])
        # correct only if solved_all AND not too-slow (checked by caller's threshold below)
        buckets = defaultdict(int)
        slow = False
        for t in ("anchor", "corner", "scaled"):
            tt = (r.get("tiers") or {}).get(t)
            if not tt:
                continue
            for c in tt["cases"]:
                b = _bucket("TLE") if c["verdict"] == "EXCEEDED_CEILING" else _bucket(
                    "PASS" if c["verdict"] == "PASS" else "WRONG_ANSWER")
                buckets[b] += 1
        # roll a whole-statement verdict for the final layer: correct only if fully solved
        vt = "PASS" if r.get("solved_all") else ("too_slow" if r.get("max_elapsed_s", 0) else "wrong")
        for b, n in buckets.items():
            per_model[model][b] += n
        final_layer[model][_bucket(vt) if vt != "too_slow" else "too_slow"] += 1
    return per_model, final_layer, crit_ceiling


def _apply_slow_threshold(family, per_model, final_layer, threshold):
    """Reclassify frontier PASS cases slower than the threshold as too_slow (file 52: 300 s
    is a failure). Students already carry TLE from the loop's ceiling."""
    fbase = FRONTIER_DIR / f"family_{family}"
    for rj in fbase.glob("*/*/final/*/result.json") if fbase.exists() else []:
        r = _read_json(rj)
        model = "[frontier] " + r.get("model", "")
        for t in ("anchor", "corner", "scaled"):
            tt = (r.get("tiers") or {}).get(t)
            if not tt:
                continue
            for c in tt["cases"]:
                if c["verdict"] == "PASS" and (c.get("elapsed_s") or 0) > threshold:
                    per_model[model]["correct"] -= 1
                    per_model[model]["too_slow"] += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--tle-threshold", type=int, default=300,
                    help="a PASS slower than this counts as too-slow (a failure)")
    args = ap.parse_args()

    per_model, final_layer, crit_ceiling = collect(args.family)
    if not per_model:
        raise SystemExit(f"no lineages under {LINEAGES_DIR / f'family_{args.family}'}")
    _apply_slow_threshold(args.family, per_model, final_layer, args.tle_threshold)

    def line(model, d):
        tot = sum(d.values()) or 1
        return (f"{model:<26} n={tot:<4} "
                f"correct={d['correct']:>4} ({100*d['correct']/tot:>3.0f}%)  "
                f"wrong={d['wrong']:>4}  too_slow={d['too_slow']:>4}")

    print("== Per-model outcomes across ALL depths (correct / wrong / too-slow) ==")
    for model in sorted(per_model):
        print("  " + line(model, per_model[model]))

    print("\n== FINAL layer only (each lineage's hardest statement) ==")
    n_models = len(final_layer)
    defeated_models = 0
    for model in sorted(final_layer):
        d = final_layer[model]
        tot = sum(d.values()) or 1
        # a model is "defeated overall" if it fails more final statements than it solves
        if d["correct"] < (tot - d["correct"]):
            defeated_models += 1
        print("  " + line(model, d))
    print(f"\n  HEADLINE: models mostly-defeated in the final layer: "
          f"{defeated_models}/{n_models}")

    print("\n== Per-criterion defeat ceiling (best simultaneous-defeat fraction reached) ==")
    print("   (max over depths of |defeated| / |panel|, per lineage; a finding even below 100%)")
    for crit in sorted(crit_ceiling):
        fr = crit_ceiling[crit]
        print(f"  {crit:<24} lineages={len(fr):<3} "
              f"mean_best={100*sum(fr)/len(fr):>3.0f}%  max_best={100*max(fr):>3.0f}%")

    out = B.REPORTS_DIR / "survival_scorecard.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "family": args.family, "tle_threshold_s": args.tle_threshold,
        "per_model_all_depths": {m: dict(d) for m, d in per_model.items()},
        "final_layer": {m: dict(d) for m, d in final_layer.items()},
        "criterion_defeat_ceiling": {c: {"mean_best": sum(f)/len(f), "max_best": max(f)}
                                     for c, f in crit_ceiling.items()}}, indent=2))
    print(f"\n[survival] wrote {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Adversarial corner-case engine (file 52 follow-up).

Generates test inputs that DEFEAT solver solutions by differential testing: produce a
diverse candidate pool (edge sizes + hard/phase-transition instances via the family's
generator), compute ground truth with reference.py, and keep the inputs where a target
solution DISAGREES with the reference (WRONG_ANSWER) or exceeds the ceiling (TLE). Kept
cases are written into the corner-tier store (agentic/tests/<family>/<criterion>/), so the
next hardening depth scores every student against them.

This is the only reliable lever for defeating P / INFEASIBLE problems (which cannot be made
computationally hard): find the exact edge case a model overlooks.

  # static (edge + hard cases the reference solves; no target):
  python tools/gen_adversarial.py --family 01 --criterion 1 --keep 8
  # differential (keep only inputs that defeat a specific solution):
  python tools/gen_adversarial.py --family 01 --criterion 1 --against path/to/solution.py --keep 4
"""
import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

import backends as B
import gate as GT

from harness.checker import normalize, judge_custom
from harness.runner import run_solution

REF_TIMEOUT_S = 60          # ground-truth solve budget per candidate
_CRIT_NUM = {"criterion_1_npc": 1, "criterion_2_p": 2, "criterion_3_infeasible": 3}


def _gen_path(family):
    p = B.ROOT / "tools" / f"gen_family_{family}.py"
    return p if p.exists() else None


def _candidate_inputs(family, criterion, pool, seed, bmax):
    """Yield candidate input strings from the family generator over a spread of sizes and
    seeds: tiny edge cases (n=1..8) plus graded sizes up to the bound (capped so P/INFEASIBLE
    stay tractable -- the scaled tier already covers the huge instances)."""
    gp = _gen_path(family)
    if gp is None:
        return
    cap = min(int(bmax) if bmax else 40, 200)
    sizes = sorted(set([1, 2, 3, 5, 8] + [cap, max(2, cap // 2), max(2, cap // 4)]))
    per = max(1, pool // max(1, len(sizes)))
    emitted = 0
    for n in sizes:
        m = max(1, int(2.35 * n))       # generator ignores --m for c1 (uses its own ratio)
        for s in range(seed, seed + per):
            cmd = [sys.executable, str(gp), "--criterion", str(criterion),
                   "--n", str(n), "--m", str(m), "--seed", str(s)]
            try:
                r = subprocess.run(cmd, capture_output=True, timeout=30, text=True)
            except Exception:
                continue
            if r.returncode == 0 and r.stdout.strip():
                yield r.stdout
                emitted += 1
                if emitted >= pool:
                    return


def _reference_output(reference_path, inp, mem):
    rr = run_solution(reference_path, inp, REF_TIMEOUT_S, mem)
    return rr.stdout if rr.status == "OK" else None


def _defeat_verdict(sol_path, inp, expected, sc, mem, ceiling):
    """Return (verdict|None, elapsed): the verdict a solution gets on this input, or None
    if it matches the reference (i.e. NOT defeated)."""
    rr = run_solution(sol_path, inp, ceiling, mem)
    if rr.status == "TLE":
        return "TLE", rr.elapsed_s
    if rr.status == "RUNTIME_ERROR":
        return "RUNTIME_ERROR", rr.elapsed_s
    mode = sc.meta.get("judge", "exact")
    if mode == "custom" and sc.validator_path is not None:
        ok, _ = judge_custom(sc.validator_path, inp, rr.stdout)
    else:
        ok = normalize(rr.stdout) == normalize(expected)
    return (None if ok else "WRONG_ANSWER"), rr.elapsed_s


def generate(family, crit_dir, keep=8, pool=40, seed=0, against=None, ceiling=300):
    """Generate adversarial corner cases into the corner-tier store. `against` is an optional
    list of solution.py paths; when given, only inputs that defeat at least one are kept.
    Returns the number of cases written."""
    slug = B.family_slug(family)
    sc = GT.seed_criterion(slug, crit_dir)
    if sc is None:
        return 0
    mem = int(sc.meta.get("memory_limit_mb", 256))
    criterion = _CRIT_NUM.get(crit_dir, 1)
    bvals = GT.bound_values(GT._section(sc.statement_path.read_text(), "Input"))
    bmax = max(bvals) if bvals else 40
    against = [Path(a) for a in (against or []) if Path(a).exists()]
    store = B.TESTS_DIR / f"family_{family}" / crit_dir
    store.mkdir(parents=True, exist_ok=True)

    written = 0
    for inp in _candidate_inputs(family, criterion, pool, seed, bmax):
        expected = _reference_output(sc.reference_path, inp, mem)
        if expected is None:
            continue                      # reference couldn't solve it -> not usable ground truth
        tag = "static"
        if against:
            defeats = []
            for sol in against:
                v, _el = _defeat_verdict(sol, inp, expected, sc, mem, ceiling)
                if v is not None:
                    defeats.append((sol.parent.name, v))
            if not defeats:
                continue                  # every target handled it -> not adversarial
            tag = ",".join(f"{who}:{v}" for who, v in defeats)
        h = hashlib.sha1(inp.encode()).hexdigest()[:8]
        name = f"adv_{h}"
        if (store / f"{name}.in").exists():
            continue                      # already have this exact input
        (store / f"{name}.in").write_text(inp)
        (store / f"{name}.out").write_text(expected)
        written += 1
        if written >= keep:
            break
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--against", nargs="*", help="solution.py paths for differential testing")
    ap.add_argument("--keep", type=int, default=8)
    ap.add_argument("--pool", type=int, default=40)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--ceiling", type=int, default=300)
    args = ap.parse_args()

    crits = [B.criterion_dirname(args.criterion)] if args.criterion else \
        ["criterion_1_npc", "criterion_2_p", "criterion_3_infeasible"]
    for family in B.list_families(args.family):
        for cd in crits:
            n = generate(family, cd, keep=args.keep, pool=args.pool, seed=args.seed,
                         against=args.against, ceiling=args.ceiling)
            print(f"[adversarial] family_{family}/{cd}: wrote {n} corner case(s) "
                  f"({'differential' if args.against else 'static'})")


if __name__ == "__main__":
    main()

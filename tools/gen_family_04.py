#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 04 (subset sum / budget).

REBUILT per the audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md), blockers B2/B3/B5/B6:

  * Criterion 1 (NPC) hard-NO instances are now GENUINE: random coprime values with the
    target verified infeasible by meet-in-the-middle. The old "all-even values + odd target"
    trick is removed -- it was parity-trivial (a solver that checks gcd answers NO instantly,
    with no search), which the audit flagged as calibrating against a straw baseline (B2/B3).
  * Criterion 3 (INFEASIBLE) is REDESIGNED as an infeasibility-CERTIFICATE task (B5). Every
    instance is infeasible for a machine-checkable reason drawn from MULTIPLE mechanisms
    (out-of-range total, or a modular obstruction), and the required output is the certificate,
    not a constant "NO". A constant program can no longer pass.
  * Every case uses a distinct seed so no two inputs collide (B6).

Format for all three criteria: line 1 = n, line 2 = n costs, line 3 = target T.

Usage:
    python tools/gen_family_04.py --criterion 1 --n 34 --seed 4 --kind no
    python tools/gen_family_04.py --criterion 2 --n 1000 --seed 3 --kind yes
    python tools/gen_family_04.py --criterion 3 --n 40 --seed 5 --kind mod
"""
import argparse
import random
import sys
from math import gcd
from functools import reduce


def _emit(n, costs, T):
    return f"{n}\n{' '.join(map(str, costs))}\n{T}\n"


def _mitm_feasible(costs, T):
    """Exact subset-sum feasibility by meet-in-the-middle (correct for n up to ~50)."""
    if T < 0:
        return False
    half = len(costs) // 2
    A, B = costs[:half], costs[half:]

    def sums(vals):
        res = {0}
        for v in vals:
            res |= {s + v for s in res}
        return res

    sb = sums(B)
    return any((T - s) in sb for s in sums(A))


def _list_gcd(xs):
    return reduce(gcd, xs, 0)


# --- criterion 1: large values (rules out pseudo-poly DP), meet-in-the-middle ---
def gen_subsetsum_large(n, seed, kind):
    """Values up to 1e9, target up to ~4e10.

    kind='yes' -> plant a subset of large distinct values and set T to its sum. The witness
        is a single deep subset that a naive include/exclude search TLEs finding while MITM
        locates it instantly (defeats a search-with-timeout-fallback-to-NO heuristic).
    kind='no'  -> GENUINE hard NO: random coprime values, target near sum/2, verified
        infeasible by MITM. No parity/gcd/range shortcut exists, so a competent solver must
        actually search (or use MITM). Regenerates until a true NO with gcd(costs)==1 is found.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    if kind == "yes":
        costs = rng.sample(range(500_000_000, 1_000_000_000), n)  # distinct large values
        k = max(1, n // 2 + rng.randint(-2, 2))
        subset = rng.sample(range(n), k)
        T = sum(costs[i] for i in subset)
        return _emit(n, costs, T)
    if kind == "no":
        # Genuine hard NO: random coprime values, target verified infeasible by MITM. Feasible
        # only where subset sums do NOT densely cover [0,total] -- i.e. n small enough that 2^n
        # is well below the value range. For dense n (>~33 with values up to 1e9) almost every
        # target is reachable, so a true NO cannot be sampled; use kind='yes' at the top of the
        # ramp instead. We sample T across the whole range (gaps are common at these n) and keep
        # the first infeasible one, preferring targets near sum/2 where naive pruning is weakest.
        best = None
        for attempt in range(4000):
            costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
            if _list_gcd(costs) != 1:          # ensure no modular (incl. parity) shortcut
                continue
            total = sum(costs)
            for _ in range(20):
                T = rng.randint(total // 4, 3 * total // 4)
                if not _mitm_feasible(costs, T):
                    return _emit(n, costs, T)
        raise RuntimeError(
            f"could not construct a genuine NO at n={n} (subset sums too dense); "
            f"use kind='yes' at this size")
    # kind='rand' small anchor: random values, random reachable/unreachable target
    costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
    T = rng.randint(0, sum(costs))
    return _emit(n, costs, T)


# --- criterion 2: small values/target (DP is genuinely polynomial) --------------
def gen_subsetsum_small(n, seed, kind):
    """Costs in [1,100], target in [0,500]. Same task/schema as criterion 1; only the value
    magnitude changes, which is the one documented switch that makes the O(n*T) DP polynomial.

    kind='yes' -> plant a subset summing to a valid target <= 500 (YES).
    kind='no'  -> GENUINE NO: random coprime small costs, target verified infeasible by DP.
    """
    rng = random.Random(seed * 2_000_003 + 7)
    if kind == "no":
        for _ in range(10_000):
            costs = [rng.randint(1, 100) for _ in range(n)]
            if _list_gcd(costs) != 1:
                continue
            T = rng.randint(1, 500)
            # boolean DP feasibility (T <= 500)
            reach = 1  # bitset: bit j set => sum j reachable
            for c in costs:
                reach |= reach << c
            if not (reach >> T) & 1:
                return _emit(n, costs, T)
        raise RuntimeError("could not construct a genuine small NO instance")
    # kind='yes': plant a subset summing to a target <= 500
    costs = [rng.randint(1, 100) for _ in range(n)]
    order = list(range(n)); rng.shuffle(order)
    target_cap = rng.randint(50, 500)
    s = 0
    for i in order:
        if s + costs[i] <= target_cap:
            s += costs[i]
        if s >= target_cap - 1:
            break
    return _emit(n, costs, s)


# --- criterion 3: INFEASIBLE with a machine-checkable certificate ----------------
def gen_infeasible_certificate(n, seed, kind):
    """Every instance is infeasible for a checkable reason. Two mechanisms:

    kind='sum' -> T strictly exceeds the total of all costs, so no subset can reach it.
                  Certificate: `SUM`.
    kind='mod' -> all costs are multiples of some d>=2 while T is not, so every subset sum is
                  divisible by d but T is not. Certificate: `MOD d`.

    Both are guaranteed infeasible (no MITM needed) and cannot be passed by a constant, nor by
    a solver that only knows one mechanism.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if kind == "sum":
        costs = [rng.randint(1, 1_000_000_000) for _ in range(n)]
        total = sum(costs)
        T = total + rng.randint(1, 1_000_000_000)
        return _emit(n, costs, T)
    if kind == "mod":
        d = rng.choice([2, 3, 5, 7, 11, 13])
        costs = [d * rng.randint(1, 1_000_000_000 // d) for _ in range(n)]
        total = sum(costs)
        # choose 0 <= T <= total with T % d != 0 (so range does NOT also certify it)
        while True:
            T = rng.randint(0, total)
            if T % d != 0:
                return _emit(n, costs, T)
    raise ValueError(f"unknown criterion-3 kind {kind!r}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--kind", default="",
                   help="c1/c2: yes|no|rand ; c3: sum|mod")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_subsetsum_large(args.n, args.seed, args.kind or "rand")
    elif args.criterion == 2:
        out = gen_subsetsum_small(args.n, args.seed, args.kind or "yes")
    else:
        out = gen_infeasible_certificate(args.n, args.seed, args.kind or "sum")

    sys.stdout.write(out)


if __name__ == "__main__":
    main()

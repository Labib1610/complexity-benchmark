#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 13 (partition / balanced machines).

REBUILT per the audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md), blockers B2/B3/B5/B6, mirroring
the family_04 template:

  * Criterion 1 (NPC) hard-NO instances are now GENUINE: random coprime values with an EVEN total
    (so the trivial odd-total refutation does not apply) and no subset summing to total/2, verified
    by meet-in-the-middle. The old "all-even values, total = 2 (mod 4)" trick is removed -- it was a
    parity/gcd shortcut a competent solver spots instantly (audit B2/B3).
  * Criterion 3 (INFEASIBLE) is REDESIGNED as an infeasibility-CERTIFICATE task (B5). Every instance
    is infeasible for a machine-checkable reason drawn from THREE mechanisms -- odd total, a common
    even divisor obstruction, or one task exceeding half the total -- and the required output is the
    certificate, not a constant "NO". A constant (or single-mechanism) program cannot pass.
  * Every case uses a distinct seed so no two inputs collide (B6).

Format for all three: line 1 = n, line 2 = n durations.

Usage:
    python tools/gen_family_13.py --criterion 1 --n 34 --seed 4 --kind no
    python tools/gen_family_13.py --criterion 2 --n 2000 --seed 3 --kind yes
    python tools/gen_family_13.py --criterion 3 --n 40 --seed 5 --kind mod
"""
import argparse
import random
import sys
from math import gcd
from functools import reduce


def _emit(n, d):
    return f"{n}\n{' '.join(map(str, d))}\n"


def _list_gcd(xs):
    return reduce(gcd, xs, 0)


def _subset_reaches(vals, target):
    """Exact: is there a subset of vals summing to target? Meet-in-the-middle (n up to ~50)."""
    if target < 0:
        return False
    half = len(vals) // 2
    A, B = vals[:half], vals[half:]

    def sums(part):
        res = {0}
        for v in part:
            res |= {s + v for s in res}
        return res

    sb = sums(B)
    return any((target - s) in sb for s in sums(A))


def _partition_feasible(d):
    total = sum(d)
    if total % 2 != 0:
        return False
    return _subset_reaches(d, total // 2)


def _distribute(total, count, maxval, rng):
    """`count` positive integers <= maxval summing to exactly total (feasible when
    count <= total <= count*maxval)."""
    vals, rem = [], total
    for j in range(count):
        remaining = count - j
        lo = max(1, rem - (remaining - 1) * maxval)
        hi = min(maxval, rem - (remaining - 1))
        v = rng.randint(lo, hi)
        vals.append(v); rem -= v
    return vals


# --- criterion 1: partition, large values ---------------------------------------
def gen_partition_large(n, seed, kind):
    """Large durations (up to 1e9); pseudo-poly DP ruled out (target ~1e10).

    kind='yes' -> HARD YES: plant one balanced split with large values; the naive include/exclude
        search explores deeply before finding it while MITM locates it instantly.
    kind='no'  -> GENUINE hard NO: random coprime durations, EVEN total, no subset summing to
        total/2 (verified by MITM). No parity/gcd/odd-total shortcut exists. Constructible only for
        n<=~32 (subset sums grow dense); use kind='yes' at the top of the ramp.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    if kind == "yes":
        half = max(1, n // 2)
        Bcnt = n - half
        maxv = 1_000_000_000
        A = [rng.randint(2, maxv // 2) for _ in range(half)]
        sumA = max(sum(A), Bcnt)
        A = _distribute(sumA, half, maxv, rng)
        B = _distribute(sumA, Bcnt, maxv, rng)
        d = A + B
        rng.shuffle(d)
        return _emit(len(d), d)
    if kind == "no":
        for _ in range(8000):
            d = [rng.randint(1, 1_000_000_000) for _ in range(n)]
            if _list_gcd(d) != 1:               # no modular (incl. parity) shortcut
                continue
            total = sum(d)
            if total % 2 != 0:                  # even total: odd-total refutation must not apply
                d[0] += 1
                total += 1
            if 2 * max(d) > total:              # no single-element-dominates shortcut
                continue
            if not _subset_reaches(d, total // 2):
                return _emit(n, d)
        raise RuntimeError(f"could not construct a genuine NO at n={n}; use kind='yes'")
    # small random anchor
    d = [rng.randint(1, 1_000_000_000) for _ in range(n)]
    return _emit(n, d)


# --- criterion 2: partition, small values ---------------------------------------
def gen_partition_small(n, seed, kind):
    """Small durations (<=100) so the O(n*S) DP is polynomial. Same task/schema; the one switch is
    value magnitude. kind='yes' plants a split; kind='no' is a GENUINE small NO (coprime, even
    total, DP-verified unsplittable) -- only constructible at small n."""
    rng = random.Random(seed * 2_000_003 + 7)
    if kind == "no":
        for _ in range(8000):
            d = [rng.randint(1, 100) for _ in range(n)]
            if _list_gcd(d) != 1:
                continue
            total = sum(d)
            if total % 2 != 0:
                d[0] = d[0] + 1 if d[0] < 100 else d[0] - 1
                total = sum(d)
            if total % 2 != 0 or 2 * max(d) > total:
                continue
            # boolean DP feasibility for target total//2
            target = total // 2
            reach = 1
            for c in d:
                reach |= reach << c
            if not (reach >> target) & 1:
                return _emit(n, d)
        raise RuntimeError(f"could not construct a genuine small NO at n={n}")
    half = max(1, n // 2)
    Bcnt = n - half
    A = [rng.randint(2, 100) for _ in range(half)]
    sumA = max(sum(A), Bcnt)
    A = _distribute(sumA, half, 100, rng)
    B = _distribute(sumA, Bcnt, 100, rng)
    d = A + B
    rng.shuffle(d)
    return _emit(len(d), d)


# --- criterion 3: INFEASIBLE with a machine-checkable certificate ----------------
def gen_infeasible_certificate(n, seed, kind):
    """Every instance is infeasible for a checkable reason. Three mechanisms:

    kind='odd' -> the total is odd, so it cannot split into two equal whole halves. Cert: `ODD`.
    kind='mod' -> every duration is a multiple of an even g>=2 while total/2 is not, so no subset
                  sum (always a multiple of g) can equal total/2. Cert: `MOD g`.
    kind='max' -> one task is longer than all the others combined (2*max > total), so the machine
                  holding it can never be balanced. Cert: `MAX`.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if kind == "odd":
        while True:
            d = [rng.randint(1, 1_000_000_000) for _ in range(n)]
            total = sum(d)
            if total % 2 == 0:
                d[0] += 1; total += 1
            if _list_gcd(d) == 1 and 2 * max(d) <= total:   # so ONLY odd-total applies
                return _emit(n, d)
    if kind == "mod":
        g = rng.choice([2, 6, 10, 14])
        while True:
            mult = [rng.randint(1, 100_000_000 // g) for _ in range(n)]
            if sum(mult) % 2 == 0:                          # need odd sum so total/2 not mult of g
                mult[0] += 1
            d = [g * m for m in mult]
            total = sum(d)
            if 2 * max(d) <= total:                         # so MAX does not also trivially apply
                return _emit(n, d)
    if kind == "max":
        rest = [rng.randint(1, 1_000_000) for _ in range(max(1, n - 1))]
        srest = sum(rest)
        M = srest + rng.randint(1, 1_000_000)               # M > sum of the rest -> 2M > total
        d = rest + [M]
        total = sum(d)
        if total % 2 != 0:                                  # make total even so ODD does not apply
            d[0] += 1
            if 2 * d[-1] <= sum(d):                         # keep the dominance after the tweak
                d[-1] += 2
        if _list_gcd(d) != 1:                               # avoid an accidental MOD shortcut
            d[0] += 1
        return _emit(len(d), d)
    raise ValueError(f"unknown criterion-3 kind {kind!r}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--kind", default="", help="c1/c2: yes|no|rand ; c3: odd|mod|max")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_partition_large(args.n, args.seed, args.kind or "rand")
    elif args.criterion == 2:
        out = gen_partition_small(args.n, args.seed, args.kind or "yes")
    else:
        out = gen_infeasible_certificate(args.n, args.seed, args.kind or "odd")

    sys.stdout.write(out)


if __name__ == "__main__":
    main()

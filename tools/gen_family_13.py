#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 13 (partition problem).

Usage:
    python tools/gen_family_13.py --criterion 1 --n 34 --seed 4 --splittable no
    python tools/gen_family_13.py --criterion 2 --n 2000 --seed 3 --splittable yes
    python tools/gen_family_13.py --criterion 3 --n 100000 --seed 5
"""
import argparse
import random


def _emit(n, d):
    return f"{n}\n{' '.join(map(str, d))}\n"


def _distribute(total, count, maxval, rng):
    """Return `count` positive integers, each <= maxval, summing to exactly `total`
    (feasible when count <= total <= count*maxval). Used to build group B so its sum
    equals group A's sum, giving a guaranteed equal partition."""
    vals = []
    rem = total
    for j in range(count):
        remaining = count - j
        lo = max(1, rem - (remaining - 1) * maxval)
        hi = min(maxval, rem - (remaining - 1))
        v = rng.randint(lo, hi)
        vals.append(v); rem -= v
    return vals


# --- criterion 1: partition, large values ---------------------------------------
def gen_partition_large(n, seed, splittable=False):
    """Large durations (up to 1e9). The pseudo-poly DP is ruled out (target ~ 1e10).

    splittable=False -> HARD NO that is EVEN-SUM-BUT-UNSPLITTABLE (not random!): all
        durations are EVEN and the total is forced to be 2 (mod 4), so target = total/2
        is ODD; every subset sum is even, so target is unreachable by a parity argument.
        The naive search must explore exhaustively to refute it.
    splittable=True  -> HARD YES: plant one balanced split (group A vs group B with equal
        sums) using large distinct values, so a valid partition exists but the naive
        include/exclude search explores deeply before finding it.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    if splittable is False:
        d = [2 * rng.randint(1, 499_999_999) for _ in range(n)]     # all even
        while sum(d) % 4 != 2:                                       # force total = 2 (mod 4)
            d[0] += 2                                                # target = total/2 is odd
        return _emit(n, d)
    # splittable=True: plant groups A and B of equal sum (bounded so all values <= 1e9)
    half = max(1, n // 2)
    Bcnt = n - half
    maxv = 1_000_000_000
    # keep sumA in a range that B (Bcnt values <= maxv) can match: Bcnt <= sumA <= Bcnt*maxv
    A = [rng.randint(2, maxv // 2) for _ in range(half)]
    sumA = sum(A)
    sumA = max(sumA, Bcnt)                                          # ensure feasible for B
    B = _distribute(sumA, Bcnt, maxv, rng)
    A = _distribute(sumA, half, maxv, rng)                          # re-draw A to match sumA exactly
    d = A + B
    rng.shuffle(d)
    return _emit(len(d), d)


# --- criterion 2: partition, small values ---------------------------------------
def gen_partition_small(n, seed, splittable=True):
    """Small durations (<=100) so the O(n*S) DP is polynomial. splittable=True plants an
    equal split; splittable=False makes all values even with total 2 (mod 4) -> odd
    target -> unsplittable (same parity argument, but the DP still runs to S/2)."""
    rng = random.Random(seed * 2_000_003 + 7)
    if not splittable:
        d = [2 * rng.randint(1, 50) for _ in range(n)]              # even, in [2,100]
        while sum(d) % 4 != 2:
            d[0] += 2 if d[0] + 2 <= 100 else -2
        return _emit(n, d)
    # plant a split with small values (<=100) via the bounded distribution
    half = max(1, n // 2)
    Bcnt = n - half
    A = [rng.randint(2, 100) for _ in range(half)]
    sumA = max(sum(A), Bcnt)
    A = _distribute(sumA, half, 100, rng)
    B = _distribute(sumA, Bcnt, 100, rng)
    d = A + B
    rng.shuffle(d)
    return _emit(len(d), d)


# --- criterion 3: odd total (infeasible) ----------------------------------------
def gen_odd_sum(n, seed):
    rng = random.Random(seed * 3_000_003 + 5)
    d = [rng.randint(1, 1_000_000_000) for _ in range(n)]
    if sum(d) % 2 == 0:
        d[0] += 1 if d[0] < 1_000_000_000 else -1                  # force odd total
    return _emit(n, d)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--splittable", default="")
    args = p.parse_args()

    if args.criterion == 1:
        sp = {"yes": True, "no": False, "": False}[args.splittable]
        out = gen_partition_large(args.n, args.seed, splittable=sp)
    elif args.criterion == 2:
        sp = {"yes": True, "no": False, "": True}[args.splittable]
        out = gen_partition_small(args.n, args.seed, splittable=sp)
    else:
        out = gen_odd_sum(args.n, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

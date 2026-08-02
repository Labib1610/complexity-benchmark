#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 12 (knapsack).

Usage:
    python tools/gen_family_12.py --criterion 1 --n 34 --seed 4
    python tools/gen_family_12.py --criterion 2 --n 200000 --seed 3
    python tools/gen_family_12.py --criterion 3 --n 100000 --seed 5
"""
import argparse
import random


def _emit(n, B, items):
    lines = [f"{n} {B}"]
    lines += [f"{c} {v}" for (c, v) in items]
    return "\n".join(lines) + "\n"


# --- criterion 1: 0/1 knapsack, large costs/values, tight budget ----------------
def gen_knapsack_large(n, seed):
    """Large costs and values (up to 1e9), so the pseudo-poly O(n*B) DP is blocked
    (B up to ~2e10). Budget B = sum(costs)//2 is deliberately tight -- pruning on the
    remaining budget barely helps, so a naive 2^n include/exclude search explores
    exponentially, while meet-in-the-middle is 2^(n/2)."""
    rng = random.Random(seed * 1_000_003 + 11)
    items = [(rng.randint(1, 1_000_000_000), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    B = sum(c for c, _ in items) // 2
    return _emit(n, B, items)


# --- criterion 2: fractional knapsack -------------------------------------------
def gen_fractional(n, seed):
    """SMALL costs (so total cost stays within the B<=1e9 bound) and large values;
    budget = half the total cost, so roughly half the items are taken and the O(n^2)
    repeated max-ratio scan runs ~n/2 O(n) passes -> TLE at large n, while the O(n log n)
    sorted greedy is fast. Values are large so ratios are well spread."""
    rng = random.Random(seed * 2_000_003 + 7)
    items = [(rng.randint(1, 5000), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    B = sum(c for c, _ in items) // 2      # <= n*5000/2 = 5e8 for n<=2e5, within B<=1e9
    return _emit(n, B, items)


# --- criterion 3: zero budget (infeasible) --------------------------------------
def gen_zero_budget(n, seed):
    rng = random.Random(seed * 3_000_003 + 5)
    items = [(rng.randint(1, 1_000_000_000), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    return _emit(n, 0, items)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_knapsack_large(args.n, args.seed)
    elif args.criterion == 2:
        out = gen_fractional(args.n, args.seed)
    else:
        out = gen_zero_budget(args.n, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

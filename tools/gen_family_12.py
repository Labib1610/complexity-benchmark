#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 12 (0-1 knapsack / portfolio selection).

REBUILT per the audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md), blockers B4/B5/B6:

  * Criterion 2 (P) was FRACTIONAL knapsack -- a different task from the 0-1 criterion 1 (audit B4:
    the pair must change ONE thing). It is now the SAME 0-1 knapsack with the SAME schema/output;
    the one documented switch is a small cost/budget bound, which makes the pseudo-polynomial
    O(n*B) DP polynomial. (Fractional knapsack is removed.)
  * Criterion 3 (INFEASIBLE) was budget B=0 requiring a constant "NO" (gameable). It is now an
    infeasibility-CERTIFICATE task: every instance has min(cost) > B, so nothing is affordable, and
    the model must output `MIN m` with a value m proving all costs exceed the budget.
  * Distinct seeds per case (B6). Criterion 1 (an OPTIMISATION, already non-gameable) is unchanged
    except for reseeding.

Input schema (all three): line 1 = "n B", then n lines "cost value".

Usage:
    python tools/gen_family_12.py --criterion 1 --n 34 --seed 4
    python tools/gen_family_12.py --criterion 2 --n 1000 --seed 3
    python tools/gen_family_12.py --criterion 3 --n 100 --seed 5
"""
import argparse
import random
import sys


def _emit(n, B, items):
    lines = [f"{n} {B}"]
    lines += [f"{c} {v}" for (c, v) in items]
    return "\n".join(lines) + "\n"


# --- criterion 1: 0/1 knapsack, large costs/values, tight budget ----------------
def gen_knapsack_large(n, seed):
    """Large costs and values (up to 1e9) block the pseudo-poly O(n*B) DP (B up to ~2e10). Budget
    B = sum(costs)//2 is tight, so a naive 2^n search explores exponentially while MITM is 2^(n/2).
    This is an OPTIMISATION (max value + a witness subset): no YES/NO, so a constant cannot game it."""
    rng = random.Random(seed * 1_000_003 + 11)
    items = [(rng.randint(1, 1_000_000_000), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    B = sum(c for c, _ in items) // 2
    return _emit(n, B, items)


# --- criterion 2: 0/1 knapsack, SMALL budget (pseudo-poly DP is polynomial) ------
def gen_knapsack_small(n, seed):
    """Same 0-1 knapsack and schema as criterion 1; the one switch is small costs/budget so the
    O(n*B) DP is polynomial. costs in [1,100], values up to 1e9, budget in [500,2000] -> many items
    compete for the budget (a real knapsack), and the DP is fast."""
    rng = random.Random(seed * 2_000_003 + 7)
    items = [(rng.randint(1, 100), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    B = rng.randint(500, 2000)
    return _emit(n, B, items)


# --- criterion 3: INFEASIBLE (nothing affordable) with a checkable certificate ---
def gen_unaffordable(n, seed):
    """Every cost strictly exceeds the budget, so no investment can be selected. The certificate is
    `MIN m` where m proves every cost > B. Guaranteed infeasible; a constant cannot pass because m
    (the affordability bound) is instance-specific and checked against the input."""
    rng = random.Random(seed * 3_000_003 + 5)
    B = rng.randint(1, 1_000_000)
    # all costs strictly greater than B (min cost > B), values arbitrary
    items = [(B + rng.randint(1, 1_000_000_000 - B), rng.randint(1, 1_000_000_000)) for _ in range(n)]
    return _emit(n, B, items)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_knapsack_large(args.n, args.seed)
    elif args.criterion == 2:
        out = gen_knapsack_small(args.n, args.seed)
    else:
        out = gen_unaffordable(args.n, args.seed)

    sys.stdout.write(out)


if __name__ == "__main__":
    main()

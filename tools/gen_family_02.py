#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 02 (SAT / task scheduling).

Usage:
    python tools/gen_family_02.py --criterion 1 --n 55 --seed 4 --ratio 4.26
    python tools/gen_family_02.py --criterion 2 --n 100000 --m 200000 --seed 3 --sat yes
    python tools/gen_family_02.py --criterion 3 --n 100000 --m 200000 --seed 5 --contra high
"""
import argparse
import random


def gen_3sat(n, seed, ratio=4.26):
    """Criterion 1: random 3-SAT at the given clause/variable ratio.

    Clauses have exactly 3 distinct variables (so no tautologies), random signs,
    no duplicate clauses. Format: 'n m' then m lines 'l1 l2 l3'.
    """
    rng = random.Random(seed * 1_000_003 + 17)
    m = round(ratio * n)
    clauses = set()
    out = []
    limit = 200 * m + 1000
    attempts = 0
    while len(clauses) < m and attempts < limit:
        attempts += 1
        vs = rng.sample(range(1, n + 1), 3)
        lits = tuple(sorted((v if rng.random() < 0.5 else -v for v in vs),
                            key=lambda x: (abs(x), x)))
        if lits in clauses:
            continue
        clauses.add(lits)
        out.append(lits)
    lines = [f"{n} {len(out)}"]
    lines += [f"{a} {b} {c}" for (a, b, c) in out]
    return "\n".join(lines) + "\n"


def _planted_2sat(n, m, seed, budget=None):
    """Random 2-SAT clauses consistent with a random planted assignment (=> SAT).
    Returns (assignment list 1..n of 0/1, list of clauses as (l1, l2))."""
    rng = random.Random(seed * 2_000_003 + 7)
    val = [0] + [rng.randint(0, 1) for _ in range(n)]
    budget = m if budget is None else budget
    seen = set()
    clauses = []
    limit = 40 * budget + 1000
    attempts = 0
    while len(clauses) < budget and attempts < limit:
        attempts += 1
        i = rng.randint(1, n)
        j = rng.randint(1, n)
        if i == j:
            continue
        # ensure the clause is satisfied by the planted assignment: pick at least
        # one literal true under `val`.
        if rng.random() < 0.5:
            li = i if val[i] == 1 else -i          # true literal on i
            lj = j if rng.random() < 0.5 else -j    # either on j
        else:
            lj = j if val[j] == 1 else -j
            li = i if rng.random() < 0.5 else -i
        key = tuple(sorted((li, lj), key=lambda x: (abs(x), x)))
        if key in seen:
            continue
        seen.add(key)
        clauses.append((li, lj))
    return val, clauses, rng


def gen_2sat(n, m, seed, satisfiable=True, components=1):
    """Criterion 2: 2-SAT instance.

    satisfiable=True  -> clauses consistent with a planted assignment (SAT).
    satisfiable=False -> plant a forced-contradiction gadget on one variable (UNSAT).
    components>1      -> restrict clauses to within contiguous variable blocks.
    """
    rng0 = random.Random(seed * 5_000_003 + 3)
    budget = m - (0 if satisfiable else 2)
    if components <= 1:
        _, clauses, rng = _planted_2sat(n, m, seed, budget=budget)
    else:
        # partition variables into blocks; clauses stay within a block
        block = max(2, n // components)
        clauses = []
        seen = set()
        rng = random.Random(seed * 5_000_101 + 9)
        val = [0] + [rng.randint(0, 1) for _ in range(n)]
        per = budget
        attempts = 0
        while len(clauses) < per and attempts < 40 * per + 1000:
            attempts += 1
            b = rng.randrange(components)
            lo = b * block + 1
            hi = min(n, lo + block - 1)
            if hi - lo < 1:
                continue
            i = rng.randint(lo, hi)
            j = rng.randint(lo, hi)
            if i == j:
                continue
            li = i if val[i] == 1 else -i
            lj = j if rng.random() < 0.5 else -j
            key = tuple(sorted((li, lj), key=lambda x: (abs(x), x)))
            if key in seen:
                continue
            seen.add(key)
            clauses.append((li, lj))

    if not satisfiable:
        v = 1 + (seed % n)
        clauses.append((v, v))       # forces v = true
        clauses.append((-v, -v))     # forces v = false  -> contradiction

    rng.shuffle(clauses)
    lines = [f"{n} {len(clauses)}"]
    lines += [f"{a} {b}" for (a, b) in clauses]
    return "\n".join(lines) + "\n"


def gen_2sat_contradiction(n, m, seed, contra="low"):
    """Criterion 3: guaranteed-UNSAT 2-SAT with a single forced-contradiction var.

    Base is a satisfiable planted 2-SAT (no variable contradicted); we then add a
    gadget forcing exactly one variable both true and false. The smallest (and only)
    contradicted variable is therefore that variable.

    contra='low'  -> contradicted variable at a low index.
    contra='high' -> contradicted variable near n, so a solution that reports the
                     first contradiction it stumbles on (not the smallest) fails.
    """
    val, clauses, rng = _planted_2sat(n, m, seed, budget=m - 2)
    cv = 2 if contra == "low" else n  # low uses index 2 (keeps 1 uncontradicted too)
    clauses.append((cv, cv))
    clauses.append((-cv, -cv))
    rng.shuffle(clauses)
    lines = [f"{n} {len(clauses)}"]
    lines += [f"{a} {b}" for (a, b) in clauses]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--m", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--ratio", type=float, default=4.26)   # criterion 1
    p.add_argument("--sat", default="yes")                # criterion 2
    p.add_argument("--components", type=int, default=1)   # criterion 2
    p.add_argument("--contra", default="low")             # criterion 3
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_3sat(args.n, args.seed, ratio=args.ratio)
    elif args.criterion == 2:
        out = gen_2sat(args.n, args.m, args.seed,
                       satisfiable=(args.sat.lower() in ("yes", "y", "true", "1")),
                       components=args.components)
    else:
        out = gen_2sat_contradiction(args.n, args.m, args.seed, contra=args.contra)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

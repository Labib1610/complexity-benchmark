#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 05 (3-dimensional matching /
bipartite matching / infeasible).

Usage:
    python tools/gen_family_05.py --criterion 1 --k 18 --t 60 --seed 4 --perfect no
    python tools/gen_family_05.py --criterion 2 --k 450 --seed 3 --mode hard
    python tools/gen_family_05.py --criterion 3 --k 1000 --e 100000 --seed 5 --empty high
"""
import argparse
import random


# --- criterion 1: 3-dimensional matching ------------------------------------
def gen_3dm(k, t, seed, perfect=None):
    """k specialists / machines / slots; t allowed triples (x,y,z).

    perfect=True  -> plant a perfect matching (two random permutations give k
        disjoint triples covering every x, y, z) then add random extra triples.
    perfect=False/None -> random triples at the requested density t. Near the
        3DM threshold (t ~ 3k..5k) most such instances have NO perfect matching and
        force the backtracking search to explore exhaustively; the caller verifies
        the verdict with the reference and hunts hard-NO seeds.
    """
    rng = random.Random(seed * 1_000_003 + 11)
    seen = set()
    triples = []
    if perfect is True:
        py = list(range(1, k + 1)); rng.shuffle(py)
        pz = list(range(1, k + 1)); rng.shuffle(pz)
        for x in range(1, k + 1):
            e = (x, py[x - 1], pz[x - 1]); seen.add(e); triples.append(e)
    cap = k * k * k
    t = min(t, cap)
    attempts = 0
    while len(triples) < t and attempts < 60 * t + 1000:
        attempts += 1
        e = (rng.randint(1, k), rng.randint(1, k), rng.randint(1, k))
        if e in seen:
            continue
        seen.add(e); triples.append(e)
    rng.shuffle(triples)
    lines = [f"{k} {len(triples)}"]
    lines += [f"{x} {y} {z}" for (x, y, z) in triples]
    return "\n".join(lines) + "\n"


# --- criterion 2: bipartite matching ----------------------------------------
def _emit_3dm(k, triples):
    lines = [f"{k} {len(triples)}"]
    lines += [f"{x} {y} {z}" for (x, y, z) in triples]
    return "\n".join(lines) + "\n"


def gen_functional_3dm(k, seed, feasible=True):
    """UNIFIED triple schema (audit B4): 3-dimensional matching where each specialist is tied to
    exactly one machine and the machines are all distinct (a bijection X->Y). Only the time slot is
    free, so the problem reduces to bipartite matching between specialists and slots. feasible=True
    plants a perfect specialist<->slot matching; feasible=False creates a Hall violation (two
    specialists compete for a single slot), so no valid plan exists."""
    rng = random.Random(seed * 2_000_003 + 7)
    Yperm = list(range(1, k + 1)); rng.shuffle(Yperm)   # Y[x] = machine of specialist x (bijection)
    Y = {x: Yperm[x - 1] for x in range(1, k + 1)}
    triples = []
    seen = set()

    def add(x, z):
        if (x, z) not in seen and 1 <= z <= k:
            seen.add((x, z)); triples.append((x, Y[x], z))

    if feasible:
        Zperm = list(range(1, k + 1)); rng.shuffle(Zperm)
        for x in range(1, k + 1):
            add(x, Zperm[x - 1])                        # the planted perfect matching
        for x in range(1, k + 1):                       # extra slot options
            for _ in range(rng.randint(0, 2)):
                add(x, rng.randint(1, k))
    else:
        blocked = rng.sample(range(1, k + 1), 2) if k >= 2 else [1]
        slot = rng.randint(1, k)
        for x in range(1, k + 1):
            if x in blocked:
                add(x, slot)                            # both blocked specialists share ONE slot
            else:
                add(x, x)
                for _ in range(rng.randint(0, 2)):
                    z = rng.randint(1, k)
                    if z != slot:
                        add(x, z)
    rng.shuffle(triples)
    return _emit_3dm(k, triples)


def gen_missing_specialist(k, seed, at="high"):
    """UNIFIED triple schema (audit B5 certificate arm): exactly one specialist appears in NO allowed
    crew, so it can never be covered. Certificate = the smallest such specialist. `at` places the
    uncovered specialist (high/low/<int>) so no positional constant works."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        miss = k
    elif at == "low":
        miss = 1
    else:
        miss = int(at)
    triples = []
    seen = set()
    for x in range(1, k + 1):
        if x == miss:
            continue
        for _ in range(rng.randint(1, 3)):
            y = rng.randint(1, k); z = rng.randint(1, k)
            if (x, y, z) not in seen:
                seen.add((x, y, z)); triples.append((x, y, z))
    rng.shuffle(triples)
    return _emit_3dm(k, triples)


def gen_bipartite(k, e, seed, mode="perfect"):
    """k workers / k tasks, e allowed (worker,task) pairs.

    mode='perfect' -> plant a perfect matching (diagonal) + random extra edges (YES).
    mode='hard'    -> adversarial worst case for Kuhn's augmenting-path matcher:
        worker i is connected to tasks 1..i (a lower-triangular / "staircase"
        structure). A perfect matching exists (i->i), but Kuhn, processing workers in
        order and scanning tasks ascending, repeatedly builds long augmenting chains,
        costing ~O(V*E); Hopcroft-Karp stays O(E*sqrt(V)). e is set by the band.
    mode='no'      -> no perfect matching: k workers but their allowed tasks span only
        k-1 distinct tasks (Hall violation), YES is impossible.
    """
    rng = random.Random(seed * 2_000_003 + 7)
    seen = set(); edges = []
    max_e = k * k

    if mode == "hard":
        # lower-triangular staircase, densest that stays within e<=100000
        for i in range(1, k + 1):
            for j in range(1, i + 1):
                edges.append((i, j))
        rng.shuffle(edges)                       # order should not matter to Kuhn's cost
        lines = [f"{k} {len(edges)}"]
        lines += [f"{x} {y}" for (x, y) in edges]
        return "\n".join(lines) + "\n"

    if mode == "perfect":
        for x in range(1, k + 1):
            ed = (x, x); seen.add(ed); edges.append(ed)      # diagonal perfect matching
        want = min(e, max_e)
        attempts = 0
        while len(edges) < want and attempts < 40 * want + 500:
            attempts += 1
            ed = (rng.randint(1, k), rng.randint(1, k))
            if ed in seen:
                continue
            seen.add(ed); edges.append(ed)
    else:  # 'no' : allowed tasks span only 1..k-1  -> no perfect matching (needs k>=2)
        hi = max(1, k - 1)
        want = min(e, k * hi)
        attempts = 0
        while len(edges) < want and attempts < 40 * want + 500:
            attempts += 1
            ed = (rng.randint(1, k), rng.randint(1, hi))
            if ed in seen:
                continue
            seen.add(ed); edges.append(ed)
        # make sure every worker has at least one edge (so it is not an empty-row case)
        present = {w for (w, _) in edges}
        for x in range(1, k + 1):
            if x not in present:
                edges.append((x, rng.randint(1, hi)))

    rng.shuffle(edges)
    lines = [f"{k} {len(edges)}"]
    lines += [f"{x} {y}" for (x, y) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: an unassignable worker (empty compatibility row) -----------
def gen_empty_row(k, e, seed, empty="high"):
    """k workers / tasks, e pairs, with worker(s) that have NO allowed task.

    empty='high' -> the empty worker is index k (a scan-from-1 solution must reach the
                    end). empty='low' -> index 1. empty=<int> -> that index.
    The answer is the smallest worker with no allowed pair.
    """
    rng = random.Random(seed * 3_000_003 + 5)
    if empty == "high":
        empty_at = k
    elif empty == "low":
        empty_at = 1
    else:
        empty_at = int(empty)
    workers = [x for x in range(1, k + 1) if x != empty_at]
    seen = set(); edges = []
    # give every non-empty worker at least one task
    for x in workers:
        y = rng.randint(1, k)
        ed = (x, y); seen.add(ed); edges.append(ed)
    want = min(e, (k - 1) * k)
    attempts = 0
    while len(edges) < want and attempts < 20 * want + 500:
        attempts += 1
        x = rng.choice(workers); y = rng.randint(1, k)
        ed = (x, y)
        if ed in seen:
            continue
        seen.add(ed); edges.append(ed)
    rng.shuffle(edges)
    lines = [f"{k} {len(edges)}"]
    lines += [f"{x} {y}" for (x, y) in edges]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--k", type=int, required=True)
    p.add_argument("--t", type=int, default=0)          # criterion 1 triple count
    p.add_argument("--e", type=int, default=0)          # criterion 2/3 edge count
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--perfect", default="")             # criterion 1: yes/no/(blank)
    p.add_argument("--mode", default="perfect")          # criterion 2: perfect/hard/no
    p.add_argument("--empty", default="high")            # criterion 3: high/low/<int>
    p.add_argument("--kind", default="yes")              # criterion 2 (unified 3DM): yes/no
    p.add_argument("--at", default="high")               # criterion 3 (unified 3DM): high/low/<int>
    args = p.parse_args()

    if args.criterion == 1:
        pf = {"yes": True, "no": False, "": None}[args.perfect]
        out = gen_3dm(args.k, args.t, args.seed, perfect=pf)
    elif args.criterion == 2:
        # audit B4: unified 3DM with the functional promise (triple schema), not bipartite pairs.
        out = gen_functional_3dm(args.k, args.seed, feasible=(args.kind == "yes"))
    else:
        # audit B4/B5: unified 3DM missing-specialist certificate (triple schema).
        out = gen_missing_specialist(args.k, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

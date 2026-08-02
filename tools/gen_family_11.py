#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 11 (set cover).

Usage:
    python tools/gen_family_11.py --criterion 1 --u 18 --s 150 --k 6 --seed 4 --coverable yes
    python tools/gen_family_11.py --criterion 2 --uA 800 --uB 800 --seed 3 --mode hard
    python tools/gen_family_11.py --criterion 3 --u 100000 --s 100000 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: set cover (2^u DP vs C(s,k) subsets) --------------------------
def gen_setcover(u, s, k, seed, coverable=True):
    """u skills, s consultants, budget k. `groups` = k (coverable) or k+1 (not) disjoint
    skill groups of size >=2 each partition the u skills; one ESSENTIAL consultant covers
    each group, placed at the HIGHEST indices. The remaining consultants are DECOYS
    covering a single skill (so no decoy can cover a size>=2 group), giving a UNIQUE
    minimum cover of size `groups` (the essentials) -- found last by the C(s,k) baseline.
    The reference's 2^u DP is unaffected (u fixed, s grows: that asymmetry is the window).
    """
    rng = random.Random(seed * 1_000_003 + 11)
    groups = k if coverable else k + 1
    # partition skills 1..u into `groups` groups of size >= 2
    base = u // groups
    sizes = [base] * groups
    for i in range(u - base * groups):
        sizes[i] += 1
    skills = list(range(1, u + 1))
    grp = []
    at = 0
    for sz in sizes:
        grp.append(skills[at:at + sz]); at += sz

    n_decoy = max(0, s - groups)
    consultants = []
    for _ in range(n_decoy):                       # decoys: a single random skill
        consultants.append([rng.randint(1, u)])
    for g in grp:                                  # essentials at the high indices
        consultants.append(list(g))

    lines = [f"{u} {len(consultants)} {k}"]
    for c in consultants:
        lines.append(f"{len(c)} " + " ".join(map(str, c)))
    return "\n".join(lines) + "\n"


# --- criterion 2: size-2 sets = edge cover (König/Gallai) ------------------------
def gen_size2_sets(uA, uB, s, seed, mode="hard"):
    """Each consultant is an edge (frontend a, backend b). mode='hard' -> lower-triangular
    staircase (a connects to b in 1..min(a,uB)), forcing Kuhn's O(V*E) long augmenting
    chains while Hopcroft-Karp stays O(E*sqrt V). Every skill appears. mode='star' ->
    one frontend skill paired with every backend skill. mode='path' -> a matching-ish path."""
    rng = random.Random(seed * 2_000_003 + 7)
    edges = []
    if mode == "hard":
        for a in range(1, uA + 1):
            for b in range(1, min(a, uB) + 1):
                edges.append((a, b))
        # ensure every backend skill 1..uB appears (staircase covers 1..uA on side b already)
        rng.shuffle(edges)
    elif mode == "star":
        for b in range(1, uB + 1):
            edges.append((1, b))
        for a in range(2, uA + 1):
            edges.append((a, 1))
    else:  # path: a_i - b_i and a_{i+1} - b_i (a small chain), covers all
        for i in range(1, max(uA, uB) + 1):
            a = min(i, uA); b = min(i, uB)
            edges.append((a, b))
            if i < uA and b <= uB:
                edges.append((min(i + 1, uA), b))
    lines = [f"{uA} {uB} {len(edges)}"]
    lines += [f"{a} {b}" for (a, b) in edges]
    return "\n".join(lines) + "\n"


# --- criterion 3: an uncoverable skill ------------------------------------------
def gen_uncoverable(u, s, seed, at="high"):
    """u skills, s consultants, with ONE skill (at a high/low/given id) covered by no
    consultant; every other skill is covered. Answer = smallest uncovered skill."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        miss = u
    elif at == "low":
        miss = 1
    else:
        miss = int(at)
    others = [x for x in range(1, u + 1) if x != miss]
    # each of the first (u-1) consultants covers one distinct 'other' skill (so all appear)
    consultants = []
    rng.shuffle(others)
    for x in others:
        consultants.append([x])
    # remaining consultants: 1-3 random skills from 'others' (never `miss`)
    while len(consultants) < s:
        cnt = rng.randint(1, 3)
        consultants.append([rng.choice(others) for _ in range(cnt)])
    rng.shuffle(consultants)
    lines = [f"{u} {len(consultants)}"]
    for c in consultants:
        lines.append(f"{len(c)} " + " ".join(map(str, c)))
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--u", type=int, default=0)
    p.add_argument("--s", type=int, default=0)
    p.add_argument("--k", type=int, default=0)
    p.add_argument("--uA", type=int, default=0)
    p.add_argument("--uB", type=int, default=0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--coverable", default="yes")
    p.add_argument("--mode", default="hard")
    p.add_argument("--at", default="high")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_setcover(args.u, args.s, args.k, args.seed,
                           coverable=(args.coverable.lower() in ("yes", "y", "1", "true")))
    elif args.criterion == 2:
        out = gen_size2_sets(args.uA, args.uB, args.s, args.seed, mode=args.mode)
    else:
        out = gen_uncoverable(args.u, args.s, args.seed, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

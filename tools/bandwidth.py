#!/usr/bin/env python3
"""Uncommon NP-complete family: GRAPH BANDWIDTH (decision + witness).

Given an undirected graph and integer B, assign DISTINCT labels 1..n to the vertices so that for
every edge (u,v), |label(u)-label(v)| <= B. Output such a labelling, or NO.

Why this family: exact graph bandwidth is NP-complete and *uncommon* (models know Cuthill-McKee-style
heuristics but not an exact solver), so seeds should carry a real failure rate. It is witness-graded
(verify a labelling in O(n+m)), so instances can be planted arbitrarily hard while staying gradeable.

I/O:
  input : line 1 = "n m B";  next m lines = "u v" (1-indexed edges)
  output: "YES" then n integers (label of vertex 1..n, a permutation of 1..n), or "NO"
"""
import argparse, random, sys
from itertools import permutations


def plant(n, B, ratio, seed):
    """Planted YES instance: fix a random position for each vertex, then add edges only between
    vertices whose position difference <= B (so that planted labelling is valid), up to m=ratio*n.
    Near the feasibility threshold (many edges close to the B limit) it is hard to FIND a valid
    labelling even though one exists."""
    rng = random.Random(seed * 1_000_003 + B)
    pos = list(range(1, n + 1)); rng.shuffle(pos)          # pos[v] = planted label of vertex v
    cand = [(u, v) for u in range(n) for v in range(u + 1, n) if abs(pos[u] - pos[v]) <= B]
    rng.shuffle(cand)
    m = min(len(cand), int(ratio * n))
    edges = sorted((u + 1, v + 1) for u, v in cand[:m])
    lines = [f"{n} {len(edges)} {B}"] + [f"{u} {v}" for u, v in edges]
    return "\n".join(lines) + "\n"


def _parse(text):
    d = text.split(); n = int(d[0]); m = int(d[1]); B = int(d[2])
    edges = [(int(d[3 + 2 * i]), int(d[4 + 2 * i])) for i in range(m)]
    return n, m, B, edges


def grade(input_text, output_text):
    """Witness-only: PASS iff output is a permutation of 1..n with every edge stretch <= B."""
    n, m, B, edges = _parse(input_text)
    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but a valid labelling was planted"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try:
        lab = [int(x) for x in nums]
    except ValueError:
        return False, "non-integer label"
    if len(lab) != n:
        return False, f"expected {n} labels, got {len(lab)}"
    if sorted(lab) != list(range(1, n + 1)):
        return False, "labels must be a permutation of 1..n"
    for u, v in edges:
        if abs(lab[u - 1] - lab[v - 1]) > B:
            return False, f"edge {u}-{v} stretch {abs(lab[u-1]-lab[v-1])} > B={B}"
    return True, "valid labelling"


def brute(input_text):
    """Exact reference for SMALL n: lexicographically smallest valid labelling, or NO."""
    n, m, B, edges = _parse(input_text)
    for perm in permutations(range(1, n + 1)):
        if all(abs(perm[u - 1] - perm[v - 1]) <= B for u, v in edges):
            return "YES\n" + " ".join(map(str, perm)) + "\n"
    return "NO\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--brute", metavar="F")
    ap.add_argument("--grade", metavar="F")
    ap.add_argument("--n", type=int, default=200); ap.add_argument("--B", type=int, default=6)
    ap.add_argument("--ratio", type=float, default=3.0); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.gen:
        sys.stdout.write(plant(a.n, a.B, a.ratio, a.seed))
    elif a.brute:
        sys.stdout.write(brute(open(a.brute).read()))
    elif a.grade:
        ok, msg = grade(open(a.grade).read(), sys.stdin.read())
        print("PASS" if ok else "FAIL", "--", msg); sys.exit(0 if ok else 1)
    else:
        ap.error("use --gen / --brute / --grade")


if __name__ == "__main__":
    main()

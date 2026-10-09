#!/usr/bin/env python3
"""Worst-case (witness-graded) tier for family 14 — STEINER TREE, scaled by #terminals t.

The seed asks for the MIN cost (optimisation, t<=10 -> FPT-easy via 2^t Dreyfus-Wagner DP). This tier
is the DECISION+WITNESS reframe at LARGE t (100<t<200 and t>200): given a graph, terminals and a budget
B, output a set of edges forming a subtree that connects all terminals with total cost <= B, or NO. A
tree is planted (so a <=B solution EXISTS by construction); grading verifies the witness in O(edges) via
union-find (no reference solve). At t>=100 any exact 2^t solver is intractable -> TLE; the tier documents
scaling and remains gradeable at any size.

I/O:
  input : line 1 = "n m t B"; line 2 = t terminal ids; next m lines = "u v w" (edge, cost).
  output: "YES" then the chosen edges, one "u v" per line; or a single line "NO".
"""
import argparse, random, sys


def plant(t, relay_frac, decoy_mult, seed):
    rng = random.Random(seed * 1_500_007 + t)
    n_relay = max(1, int(t * relay_frac)); n = t + n_relay
    terminals = list(range(1, t + 1))
    nodes = list(range(1, n + 1)); rng.shuffle(nodes)
    edges = {}
    # planted spanning tree over all nodes (cheap edges) -> guarantees terminals are connected
    for i in range(1, len(nodes)):
        u = nodes[i]; v = nodes[rng.randint(0, i - 1)]
        e = (min(u, v), max(u, v)); edges[e] = rng.randint(1, 5)
    B = sum(edges.values())                       # planted-tree cost (feasible by construction)
    target = int(len(edges) * decoy_mult)
    guard = 0
    while len(edges) < target and guard < 50 * target + 5000:
        guard += 1
        u = rng.randint(1, n); v = rng.randint(1, n)
        if u != v:
            e = (min(u, v), max(u, v))
            if e not in edges:
                edges[e] = rng.randint(3, 12)
    items = list(edges.items()); rng.shuffle(items)
    lines = [f"{n} {len(items)} {t} {B}", " ".join(map(str, terminals))]
    lines += [f"{u} {v} {w}" for (u, v), w in items]
    return "\n".join(lines) + "\n"


def grade(input_text, output_text):
    """WITNESS-only: PASS iff the output edges connect all terminals with total cost <= B."""
    d = input_text.split(); idx = 0
    n = int(d[idx]); m = int(d[idx+1]); t = int(d[idx+2]); B = int(d[idx+3]); idx += 4
    terminals = [int(d[idx+i]) for i in range(t)]; idx += t
    cost = {}
    for _ in range(m):
        u = int(d[idx]); v = int(d[idx+1]); w = int(d[idx+2]); idx += 3
        cost[(min(u, v), max(u, v))] = w
    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but a tree was planted"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    if len(nums) % 2 != 0:
        return False, "edge list must be pairs 'u v'"
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    total = 0
    for i in range(0, len(nums), 2):
        try:
            u = int(nums[i]); v = int(nums[i+1])
        except ValueError:
            return False, "non-integer edge endpoint"
        e = (min(u, v), max(u, v))
        if e not in cost:
            return False, f"edge {e} not in graph"
        total += cost[e]; parent[find(u)] = find(v)
    if total > B:
        return False, f"cost {total} exceeds B={B}"
    r = find(terminals[0])
    for x in terminals:
        if find(x) != r:
            return False, "terminals not all connected"
    return True, f"valid Steiner tree, cost {total} <= {B}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--grade", metavar="F")
    ap.add_argument("--t", type=int, default=150); ap.add_argument("--relay", type=float, default=0.5)
    ap.add_argument("--decoy", type=float, default=2.0); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.gen:
        sys.stdout.write(plant(a.t, a.relay, a.decoy, a.seed))
    elif a.grade:
        ok, msg = grade(open(a.grade).read(), sys.stdin.read())
        print("PASS" if ok else "FAIL", "--", msg); sys.exit(0 if ok else 1)
    else:
        ap.error("use --gen or --grade")


if __name__ == "__main__":
    main()

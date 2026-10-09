#!/usr/bin/env python3
"""Worst-case (witness-graded) tier for family 09 — INDEPENDENT SET ("all-strangers group of size k").
Plant an independent set S of size k (no edges inside S), fill the rest at density p. A solution EXISTS
(S), and grading verifies the k vertices are pairwise non-adjacent -- O(k^2), no reference solve. Near
the hard regime, finding an IS of size k needs search -> TLE, while the witness stays cheap.

I/O (same as seed): line1 "n m k"; next m lines "u v" (edges). Output: "YES" + k vertex ids, or "NO".
"""
import argparse, random, sys


def plant(n, k, p, seed):
    """Planted independent set S of size k (no edges inside S), density p elsewhere, then
    DEGREE-EQUALIZED: add S->non-S edges so S vertices don't stand out by low degree (otherwise a
    degree-ordering backtracker finds them instantly). Hard TLE regime: n>=150, k~15-25, p=0.5."""
    rng = random.Random(seed * 3_400_013 + n)
    S = set(rng.sample(range(1, n + 1), k))
    nonS = [x for x in range(1, n + 1) if x not in S]
    adj = [set() for _ in range(n + 1)]
    def add(u, v): adj[u].add(v); adj[v].add(u)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i in S and j in S:
                continue                               # never inside S
            if rng.random() < p:
                add(i, j)
    avg = sum(len(adj[v]) for v in nonS) / max(len(nonS), 1)
    for s in S:                                        # equalize S degrees up to the non-S average
        guard = 0
        while len(adj[s]) < avg and nonS and guard < 4 * n:
            guard += 1; v = rng.choice(nonS)
            if v not in adj[s]:
                add(s, v)
    edges = {(u, v) for u in range(1, n + 1) for v in adj[u] if u < v}
    lines = [f"{n} {len(edges)} {k}"] + [f"{u} {v}" for u, v in sorted(edges)]
    return "\n".join(lines) + "\n"


def grade(input_text, output_text):
    d = input_text.split(); n = int(d[0]); m = int(d[1]); k = int(d[2])
    adj = set()
    for i in range(m):
        u = int(d[3 + 2*i]); v = int(d[4 + 2*i]); adj.add((min(u, v), max(u, v)))
    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but an IS was planted"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try:
        g = [int(x) for x in nums]
    except ValueError:
        return False, "non-integer vertex"
    if len(g) != k:
        return False, f"expected {k} vertices, got {len(g)}"
    if len(set(g)) != k or any(x < 1 or x > n for x in g):
        return False, "vertices must be k distinct ids in 1..n"
    for i in range(k):
        for j in range(i + 1, k):
            if (min(g[i], g[j]), max(g[i], g[j])) in adj:
                return False, f"{g[i]} and {g[j]} are connected"
    return True, "valid independent set"


def _bt_solves(input_text, deadline):
    import time
    d = input_text.split(); n = int(d[0]); m = int(d[1]); k = int(d[2])
    adj = [set() for _ in range(n + 1)]
    for i in range(m):
        u = int(d[3+2*i]); v = int(d[4+2*i]); adj[u].add(v); adj[v].add(u)
    t0 = time.monotonic(); order = sorted(range(1, n+1), key=lambda x: len(adj[x]))
    chosen = []
    def rec(i, cnt):
        if time.monotonic() - t0 > deadline: raise TimeoutError
        if cnt == k: return True
        if cnt + (n - i) < k: return False
        for j in range(i, n):
            v = order[j]
            if all(v not in adj[u] for u in chosen):
                chosen.append(v)
                if rec(j + 1, cnt + 1): return True
                chosen.pop()
        return False
    try: return rec(0, 0), time.monotonic() - t0
    except TimeoutError: return None, time.monotonic() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--grade", metavar="F")
    ap.add_argument("--n", type=int, default=150); ap.add_argument("--k", type=int, default=20)
    ap.add_argument("--p", type=float, default=0.5); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.gen: sys.stdout.write(plant(a.n, a.k, a.p, a.seed))
    elif a.grade:
        ok, msg = grade(open(a.grade).read(), sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg); sys.exit(0 if ok else 1)
    else: ap.error("use --gen or --grade")

if __name__ == "__main__": main()

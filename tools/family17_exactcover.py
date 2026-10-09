#!/usr/bin/env python3
"""Family 17 — EXACT COVER.  NPC = Exact Cover by 3-Sets (X3C); P = exact cover by 2-sets (bipartite
perfect matching). Both witness-graded. Obscure: X3C's formal reduction is rarely taught.

X3C  I/O: line1 "q t" (universe size 3q, t triples); next t lines "a b c" (a<b<c in 1..3q).
          output: "YES" then q lines "a b c" (a partition of the universe using given triples), or "NO".
X2C  I/O: line1 "q t" (universe size 2q on two sides A=1..q, B=q+1..2q, t pairs); next t lines "a b";
          output: "YES" then q lines "a b" (a perfect matching covering all 2q elements), or "NO".
"""
import argparse, random, sys
sys.setrecursionlimit(1 << 20)

# ---------------- X3C (NPC) ----------------
def x3c_plant(q, ratio, seed, feasible=True):
    """Universe = 1..3q. Plant a partition into q triples, add decoy triples to t=ratio*q.
    feasible=False: build a NO instance (no exact cover) by omitting a covering of one element cluster."""
    rng = random.Random(seed * 1_100_007 + q)
    U = list(range(1, 3 * q + 1)); rng.shuffle(U)
    planted = [tuple(sorted(U[3*i:3*i+3])) for i in range(q)]
    triples = set(planted if feasible else planted[:-1])   # drop one planted triple -> likely NO
    tgt = max(len(triples) + (0 if feasible else 1), int(ratio * q))
    guard = 0
    while len(triples) < tgt and guard < 60 * tgt + 5000:
        guard += 1
        c = tuple(sorted(rng.sample(range(1, 3*q+1), 3)))
        triples.add(c)
    trips = list(triples); rng.shuffle(trips)
    lines = [f"{q} {len(trips)}"] + [f"{a} {b} {c}" for a, b, c in trips]
    return "\n".join(lines) + "\n"

def x3c_solve(text, deadline=None):
    import time
    d = text.split(); q = int(d[0]); t = int(d[1])
    trips = [(int(d[2+3*i]), int(d[3+3*i]), int(d[4+3*i])) for i in range(t)]
    by_elem = {e: [] for e in range(1, 3*q+1)}
    for tr in trips:
        for e in tr: by_elem[e].append(tr)
    covered = [False] * (3*q + 1); chosen = []
    t0 = time.monotonic()
    def rec(nc):
        if nc == 3*q: return True
        if deadline and time.monotonic() - t0 > deadline: raise TimeoutError
        # MRV: pick the uncovered element with the fewest available triples
        best = None
        for e in range(1, 3*q+1):
            if not covered[e]:
                opts = [tr for tr in by_elem[e] if not any(covered[x] for x in tr)]
                if best is None or len(opts) < len(best[1]): best = (e, opts)
                if not opts: return False
        _, opts = best
        for tr in opts:
            for x in tr: covered[x] = True
            chosen.append(tr)
            if rec(nc + 3): return True
            chosen.pop()
            for x in tr: covered[x] = False
        return False
    ok = rec(0)
    return (chosen if ok else None)

def x3c_reference(text):
    sol = x3c_solve(text, deadline=None)
    if sol is None: return "NO\n"
    return "YES\n" + "\n".join(f"{a} {b} {c}" for a, b, c in sol) + "\n"

def x3c_validate(input_text, output_text):
    d = input_text.split(); q = int(d[0]); t = int(d[1])
    allowed = set(tuple(sorted((int(d[2+3*i]), int(d[3+3*i]), int(d[4+3*i])))) for i in range(t))
    toks = output_text.split()
    if not toks: return False, "empty output"
    if toks[0].upper() == "NO":
        # NO is only correct if truly infeasible (reference confirms) -- gradeable at small/medium sizes
        try:
            return (x3c_solve(input_text, deadline=10) is None), "claimed NO"
        except TimeoutError:
            return False, "validator timed out verifying claimed NO"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try: v = [int(x) for x in nums]
    except ValueError: return False, "non-integer"
    if len(v) != 3*q: return False, f"expected {3*q} ints (q={q} triples), got {len(v)}"
    seen = set()
    for i in range(q):
        tr = tuple(sorted(v[3*i:3*i+3]))
        if tr not in allowed: return False, f"triple {tr} not allowed"
        for x in tr:
            if x in seen: return False, f"element {x} covered twice"
            seen.add(x)
    return (seen == set(range(1, 3*q+1))), "exact cover" if seen == set(range(1,3*q+1)) else "not a full cover"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--ref", metavar="F"); ap.add_argument("--grade", metavar="F")
    ap.add_argument("--q", type=int, default=20); ap.add_argument("--ratio", type=float, default=3.0)
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--no", action="store_true")
    a = ap.parse_args()
    if a.gen: sys.stdout.write(x3c_plant(a.q, a.ratio, a.seed, feasible=not a.no))
    elif a.ref: sys.stdout.write(x3c_reference(open(a.ref).read()))
    elif a.grade:
        ok, msg = x3c_validate(open(a.grade).read(), sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg)
    else: ap.error("use --gen/--ref/--grade")

if __name__ == "__main__": main()

# ---------------- X2C (P): bipartite exact cover by 2-sets = perfect matching (Hopcroft-Karp) ----------------
def x2c_plant(q, ratio, seed, feasible=True):
    rng = random.Random(seed * 2_200_009 + q)
    perm = list(range(q)); rng.shuffle(perm)
    pairs = set((i + 1, q + 1 + perm[i]) for i in range(q))   # planted perfect matching (A_i, B_j)
    isolate = (not feasible and q >= 2)                       # vertex 1 gets NO pairs -> guaranteed NO
    if isolate:
        pairs = set(p for p in pairs if p[0] != 1)
    tgt = max(len(pairs), int(ratio * q))
    guard = 0
    while len(pairs) < tgt and guard < 60 * tgt + 5000:
        guard += 1; a = rng.randint(2 if isolate else 1, q); b = q + rng.randint(1, q); pairs.add((a, b))
    pl = list(pairs); rng.shuffle(pl)
    return "\n".join([f"{q} {len(pl)}"] + [f"{a} {b}" for a, b in pl]) + "\n"

def _hopcroft_karp(q, adj):
    import collections
    INF = float("inf"); matchL = [0]*(q+1); matchR = {}; 
    def bfs():
        dist = {}; Q = collections.deque()
        for u in range(1, q+1):
            if matchL[u] == 0: dist[u] = 0; Q.append(u)
            else: dist[u] = INF
        found = False
        while Q:
            u = Q.popleft()
            for v in adj[u]:
                w = matchR.get(v, 0)
                if w == 0: found = True
                elif dist.get(w, INF) == INF:
                    dist[w] = dist[u] + 1; Q.append(w)
        return found, dist
    def dfs(u, dist):
        for v in adj[u]:
            w = matchR.get(v, 0)
            if w == 0 or (dist.get(w, INF) == dist[u] + 1 and dfs(w, dist)):
                matchL[u] = v; matchR[v] = u; return True
        dist[u] = INF; return False
    m = 0
    while True:
        found, dist = bfs()
        if not found: break
        for u in range(1, q+1):
            if matchL[u] == 0 and dfs(u, dist): m += 1
    return matchL, m

def x2c_reference(text):
    d = text.split(); q = int(d[0]); t = int(d[1])
    adj = {u: [] for u in range(1, q+1)}
    for i in range(t): a = int(d[2+2*i]); b = int(d[3+2*i]); adj[a].append(b)
    matchL, m = _hopcroft_karp(q, adj)
    if m != q: return "NO\n"
    return "YES\n" + "\n".join(f"{u} {matchL[u]}" for u in range(1, q+1)) + "\n"

def x2c_validate(input_text, output_text):
    d = input_text.split(); q = int(d[0]); t = int(d[1])
    allowed = set((int(d[2+2*i]), int(d[3+2*i])) for i in range(t))
    toks = output_text.split()
    if not toks: return False, "empty"
    if toks[0].upper() == "NO":
        return (x2c_reference(input_text).split()[0] == "NO"), "claimed NO"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try: v = [int(x) for x in nums]
    except ValueError: return False, "non-integer"
    if len(v) != 2*q: return False, f"expected {2*q} ints"
    seen = set()
    for i in range(q):
        a, b = v[2*i], v[2*i+1]
        if (a, b) not in allowed: return False, f"pair ({a},{b}) not allowed"
        if a in seen or b in seen: return False, "element reused"
        seen.add(a); seen.add(b)
    return (seen == set(range(1, 2*q+1))), "perfect cover"

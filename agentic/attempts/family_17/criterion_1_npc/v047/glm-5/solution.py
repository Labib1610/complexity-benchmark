import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    idx = 2
    triples = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    # Build adjacency: for each vertex, list of (triple_id, other1, other2)
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        adj[a].append((i, b, c))
        adj[b].append((i, a, c))
        adj[c].append((i, a, b))
    
    # Sort adjacency lists by the minimum vertex in the triple (heuristic)
    triple_min = [min(tr) for tr in triples]
    for v in range(1, n + 1):
        adj[v].sort(key=lambda x: triple_min[x[0]])
    
    used_triples = [False] * t
    used_vertices = [False] * (n + 1)
    chosen = []
    
    def dfs():
        v = 1
        while v <= n and used_vertices[v]:
            v += 1
        if v > n:
            return True
        for tid, u, w in adj[v]:
            if used_triples[tid]:
                continue
            if used_vertices[u] or used_vertices[w]:
                continue
            used_triples[tid] = True
            used_vertices[v] = True
            used_vertices[u] = True
            used_vertices[w] = True
            chosen.append(tid)
            if dfs():
                return True
            chosen.pop()
            used_triples[tid] = False
            used_vertices[v] = False
            used_vertices[u] = False
            used_vertices[w] = False
        return False
    
    if dfs():
        out = ["YES"]
        for tid in chosen:
            a, b, c = triples[tid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()
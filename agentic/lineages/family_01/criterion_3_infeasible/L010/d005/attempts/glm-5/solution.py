import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    
    for u, v in edges:
        common = adj[u] & adj[v]
        if common:
            w = min(common)
            cand = tuple(sorted((u, v, w)))
            if best is None or cand < best:
                best = cand
    
    if best is None:
        deg = [len(adj[i]) for i in range(n + 1)]
        order = sorted(range(1, n + 1), key=lambda x: deg[x])
        for w in order:
            if deg[w] >= 2:
                neighbors = sorted(adj[w])
                L = len(neighbors)
                for i in range(L):
                    u = neighbors[i]
                    for j in range(i + 1, L):
                        v = neighbors[j]
                        if v not in adj[u]:
                            cand = tuple(sorted((u, v, w)))
                            if best is None or cand < best:
                                best = cand
                                break
                    if best is not None:
                        break
                if best is not None:
                    break
    
    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}")

solve()
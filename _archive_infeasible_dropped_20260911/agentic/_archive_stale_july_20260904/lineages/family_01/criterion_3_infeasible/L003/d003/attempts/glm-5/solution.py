import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    best = None
    
    for u in range(1, n + 1):
        if best is not None and u >= best[0]:
            break
        neighbors = sorted(adj[u])
        for v in neighbors:
            if v <= u:
                continue
            if best is not None and (u > best[0] or (u == best[0] and v >= best[1])):
                break
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    candidate = (u, v, w)
                    if best is None or candidate < best:
                        best = candidate
                        break
            if best is not None and best[0] == u and best[1] == v:
                break
    
    if best is None:
        for u, v in edges:
            common = adj[u] & adj[v]
            if common:
                w = min(common)
                if u > v:
                    u, v = v, u
                if w < u:
                    candidate = (w, u, v)
                elif w < v:
                    candidate = (u, w, v)
                else:
                    candidate = (u, v, w)
                if best is None or candidate < best:
                    best = candidate
    
    print(f"{best[0]} {best[1]} {best[2]}")

solve()
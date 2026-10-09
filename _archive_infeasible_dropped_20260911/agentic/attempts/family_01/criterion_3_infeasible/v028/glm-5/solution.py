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
    
    # Iterate over edges (a, b) with a < b.
    # For each, find smallest c > b with both (a,c) and (b,c) edges.
    # Track lexicographically smallest (a, b, c).
    for a, b in edges:
        if best is not None and a > best[0]:
            continue
        if best is not None and a == best[0] and b >= best[1]:
            continue
        # Find smallest c > b in adj[a] intersect adj[b]
        # Iterate over smaller adjacency set for efficiency.
        if len(adj[a]) > len(adj[b]):
            a, b = b, a
        # Now adj[a] is smaller. But we need original a < b and c > b.
        # Since we need a < b < c, and we swapped, let's be careful.
        # Actually we need to find c such that c is connected to both original a and b.
        # Let's not swap to avoid confusion; just iterate smaller set.
        pass
    
    # Redo cleanly: for each edge (a,b) with a<b, find smallest c>b connected to both.
    for a, b in edges:
        if best is not None:
            if a > best[0]:
                continue
            if a == best[0] and b > best[1]:
                continue
        # iterate over smaller of adj[a], adj[b]
        if len(adj[a]) <= len(adj[b]):
            small, large = adj[a], adj[b]
        else:
            small, large = adj[b], adj[a]
        # find smallest c in small that is also in large, with c > b
        # We want c > b (since a < b < c)
        min_c = None
        for c in small:
            if c > b and c in large:
                if min_c is None or c < min_c:
                    min_c = c
        if min_c is not None:
            cand = (a, b, min_c)
            if best is None or cand < best:
                best = cand
    
    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()
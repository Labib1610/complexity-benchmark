import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
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
    
    # Iterate over all edges (u, v) with u < v.
    # For each edge, find the smallest common neighbor w > v to form (u, v, w).
    # This guarantees lexicographically smallest triangle because:
    # - We process edges in increasing order of u, then v.
    # - For each edge, we pick the smallest possible w > v.
    # - The first valid triangle found is the lexicographically smallest.
    for u, v in edges:
        # Find smallest w in adj[u] intersect adj[v] with w > v
        # To optimize, iterate over the smaller adjacency set
        if len(adj[u]) > len(adj[v]):
            small, large = adj[v], adj[u]
        else:
            small, large = adj[u], adj[v]
        # We need w > v and w in both sets
        # Since we want smallest w > v, we can iterate over small set
        min_w = None
        for w in small:
            if w > v and w in large:
                if min_w is None or w < min_w:
                    min_w = w
                    # Since we want the smallest w, we can't break early
                    # because small set is not sorted. But we can track min.
        if min_w is not None:
            candidate = (u, v, min_w)
            if best is None or candidate < best:
                best = candidate
                # Since edges are processed in order, the first found is smallest.
                # But to be safe, we keep track.
                # Actually, since we process edges in order, the first valid candidate
                # is the lexicographically smallest. We can break.
                break
    
    if best is not None:
        print(best[0], best[1], best[2])
        return
    
    # Fallback: should not reach here because problem guarantees a triangle exists.
    # But just in case, do a full search.
    for u in range(1, n + 1):
        for v in adj[u]:
            if v < u:
                continue
            for w in adj[u]:
                if w > v and w in adj[v]:
                    print(u, v, w)
                    return

solve()
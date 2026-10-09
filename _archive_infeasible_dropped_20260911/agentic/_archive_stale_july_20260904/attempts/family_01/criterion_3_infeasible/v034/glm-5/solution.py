import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [None] * (n + 1)
    for i in range(1, n + 1):
        adj[i] = set()
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration
    adj_sorted = [None] * (n + 1)
    for i in range(1, n + 1):
        adj_sorted[i] = sorted(adj[i])
    
    best = None
    
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        
        neighbors_a = adj_sorted[a]
        # We want b < c, both neighbors of a, and b-c edge exists.
        # To get lexicographically smallest (a, b, c), iterate b in increasing order.
        len_a = len(neighbors_a)
        for i in range(len_a):
            b = neighbors_a[i]
            if b < a:
                continue
            if best is not None and b >= best[1]:
                # Since neighbors_a is sorted, all subsequent b are >= current b,
                # so no better c can be found for this a.
                break
            adj_b = adj[b]
            # Find smallest c > b that is neighbor of both a and b
            for j in range(i + 1, len_a):
                c = neighbors_a[j]
                if c in adj_b:
                    triple = (a, b, c)
                    if best is None or triple < best:
                        best = triple
                    break  # smallest c for this (a, b)
    
    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}")

solve()
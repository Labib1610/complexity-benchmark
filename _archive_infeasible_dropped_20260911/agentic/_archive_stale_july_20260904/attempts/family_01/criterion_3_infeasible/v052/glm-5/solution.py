import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        # Iterate over neighbors b > a to find smallest b, then smallest c
        # We want lexicographically smallest (a, b, c)
        # For fixed a, minimize b, then c
        # b must be > a (since we process a in increasing order and want a < b < c)
        # Actually a is fixed, we need b > a and c > b, but also c in adj[a] and adj[b]
        # To minimize b, iterate b in sorted order of adj_a where b > a
        # Then for each b, find smallest c in adj_a ∩ adj[b] with c > b
        # But we can break early once we find the first valid (b, c) for this a
        # because b is minimized first.
        # However, we need to ensure c > b and c > a (automatically if c > b > a)
        # But what if b < a? We skip since we want a < b < c.
        # Actually the problem says output sorted in ascending order a < b < c.
        # So for a given a (smallest), b and c must be > a.
        # So we only consider neighbors b of a with b > a.
        # Then c must be a neighbor of both a and b, and c > b.
        # To minimize b, we sort neighbors of a that are > a.
        # For each b in that sorted list, we check intersection of adj[a] and adj[b]
        # for any c > b. The smallest such c gives the best for this b.
        # Since we want lexicographically smallest, the first b that yields any c is the best b.
        # Then the smallest c for that b is the best c.
        
        # Optimization: iterate b in sorted order
        neighbors_a = sorted(x for x in adj_a if x > a)
        for b in neighbors_a:
            if best is not None and b >= best[1]:
                # Since a is already < best[0] (we break if a >= best[0]), 
                # but actually we break at top if a >= best[0].
                # Here if b >= best[1], even if we find c, (a,b,c) would be worse than best? 
                # No, because a < best[0], so (a, b, c) is better regardless of b.
                # So this check is wrong. Remove it.
                pass
            adj_b = adj[b]
            # Find smallest c in adj_a ∩ adj_b with c > b
            # Iterate over the smaller set
            if len(adj_a) <= len(adj_b):
                # iterate adj_a
                # We want c > b, c in adj_b
                # Since neighbors_a is sorted, but adj_a may have elements < a too.
                # Let's just iterate over neighbors_a (which is sorted and > a)
                # and find first c > b that is in adj_b
                for c in neighbors_a:
                    if c > b and c in adj_b:
                        # Found
                        if best is None or (a, b, c) < best:
                            best = (a, b, c)
                        break
            else:
                # iterate adj_b, find smallest c > b in adj_a
                # We can iterate sorted neighbors of b that are > b
                # But to find smallest c > b, we can iterate adj_b in sorted order
                # However, adj_b is a set. Let's collect and sort.
                # But that might be expensive. Instead, iterate neighbors_a (already sorted)
                # Actually, let's just iterate neighbors_a since it's already sorted and we want c > b.
                for c in neighbors_a:
                    if c > b and c in adj_b:
                        if best is None or (a, b, c) < best:
                            best = (a, b, c)
                        break
            if best is not None and best[0] == a and best[1] == b:
                # We found the best for this a (since b is minimized)
                break
    
    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()
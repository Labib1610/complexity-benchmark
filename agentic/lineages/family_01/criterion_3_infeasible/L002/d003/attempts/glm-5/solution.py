import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        neighbors = adj[a]
        # We want b < c, both neighbors of a, and edge b-c exists.
        # To get lexicographically smallest (a,b,c), iterate b in increasing order.
        sorted_neighbors = sorted(neighbors)
        # For each b, check if any c > b in neighbors is also in adj[b].
        # Optimize by checking only c that are in both neighbors and adj[b].
        for i, b in enumerate(sorted_neighbors):
            if best is not None and b >= best[1]:
                break
            # candidates for c: neighbors of a that are > b and also neighbors of b
            # Since sorted_neighbors is sorted, we can check from i+1 onwards
            # But checking adj[b] intersection with neighbors might be faster if adj[b] is small
            # We'll iterate over the smaller set between sorted_neighbors[i+1:] and adj[b]
            # Actually, let's just iterate over adj[b] and check membership in neighbors
            # But we need c > b. Since neighbors is a set, we can do:
            # for c in adj[b]:
            #     if c > b and c in neighbors:
            #         candidate = (a, b, c)
            #         if best is None or candidate < best: best = candidate; break
            # But to ensure we get the smallest c for this b, we should iterate c in sorted order.
            # Since we break at the first valid c (because we iterate b in increasing order and c in increasing order),
            # the first valid (b,c) gives the lexicographically smallest for this a.
            # However, we need to iterate c in increasing order.
            # Let's get the intersection of neighbors and adj[b], filter c > b, and take min.
            # To optimize, iterate over the smaller set.
            if len(neighbors) < len(adj[b]):
                small_set = neighbors
                other_set = adj[b]
            else:
                small_set = adj[b]
                other_set = neighbors
            min_c = None
            for c in small_set:
                if c > b and c in other_set:
                    if min_c is None or c < min_c:
                        min_c = c
            if min_c is not None:
                candidate = (a, b, min_c)
                if best is None or candidate < best:
                    best = candidate
                break  # since we want smallest b for this a, and we found one
        # If we found a candidate for this a, we can break the outer loop too
        # because we want the smallest a.
        if best is not None and best[0] == a:
            break
    
    if best is not None:
        print(best[0], best[1], best[2])

solve()
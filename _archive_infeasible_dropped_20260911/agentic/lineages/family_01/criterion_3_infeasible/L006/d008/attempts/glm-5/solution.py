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
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to find a triangle containing the smallest possible x1.
    # For each x1 from 1 to n, look at its neighbors with index > x1.
    # Among those neighbors, find a pair (x2, x3) that are connected.
    # To find the lexicographically smallest (x1, x2, x3), we iterate x1 ascending,
    # then for each x1 iterate x2 ascending among neighbors > x1,
    # and check if any x3 > x2 is a common neighbor of x1 and x2.
    
    for x1 in range(1, n + 1):
        neighbors = sorted(v for v in adj[x1] if v > x1)
        # For each x2 in neighbors, check intersection with adj[x2] for x3 > x2
        # To optimize, we can mark neighbors of x1 in a boolean array
        # But doing this for every x1 is O(n^2) memory/time which is okay for n=2000.
        # However, we want the smallest x2 first.
        # We'll use a set for neighbors of x1 for O(1) lookup.
        neigh_set = set(neighbors)
        for idx, x2 in enumerate(neighbors):
            # Check if any x3 in adj[x2] with x3 > x2 is also in neigh_set
            # We want the smallest x3, so iterate adj[x2] sorted? 
            # But adj[x2] might be large. Instead, iterate over neigh_set from idx+1.
            for x3 in neighbors[idx+1:]:
                if x3 in adj[x2]:
                    print(x1, x2, x3)
                    return
    
    # Should never reach here due to problem guarantee
    print(-1, -1, -1)

solve()
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    # Build adjacency sets
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # Find triangle with smallest a, then b, then c
    best = None
    for a in range(1, n + 1):
        # neighbors of a that are > a
        neighbors = sorted(x for x in adj[a] if x > a)
        # For each pair in neighbors, check if they are connected
        # To optimize, for each b in neighbors, intersect adj[b] with neighbors > b
        for b in neighbors:
            # candidates for c: in adj[b], > b, and in neighbors
            # Since neighbors is sorted, we can iterate
            for c in adj[b]:
                if c > b and c in adj[a]:
                    # Found triangle (a, b, c)
                    print(f"{a} {b} {c}")
                    return
    # Should not reach here per problem guarantee
    print("-1")

solve()
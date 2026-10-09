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
    
    for a in range(1, n + 1):
        neighbors = adj[a]
        # We need b, c in neighbors with b < c and edge (b, c) exists
        # To find lexicographically smallest, iterate b in sorted order
        sorted_neighbors = sorted(neighbors)
        # For efficiency, check pairs
        # Since sum of degrees <= 400000, this is acceptable
        for i in range(len(sorted_neighbors)):
            b = sorted_neighbors[i]
            if b < a:
                continue
            # Check c among later neighbors
            for j in range(i + 1, len(sorted_neighbors)):
                c = sorted_neighbors[j]
                if c < a:
                    continue
                if c in adj[b]:
                    # Found triangle
                    res = sorted([a, b, c])
                    print(res[0], res[1], res[2])
                    return
    # Should not reach here per problem guarantee
    print(-1, -1, -1)

solve()
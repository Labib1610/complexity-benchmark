import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        edges.append((u, v))
    
    # Try to find a triangle
    # For each edge (u, v), check if there exists w such that (u, w) and (v, w) are edges
    # To get lexicographically smallest, we iterate u, v, w in order
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if adj[u][v]:
                for w in range(v + 1, n + 1):
                    if adj[u][w] and adj[v][w]:
                        print(u, v, w)
                        return
    
    # If no triangle found via the above (shouldn't happen per problem guarantee),
    # we need to check other orderings.
    # But the above covers all u < v < w cases.
    # If still not found, try all permutations (though problem guarantees existence)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v and adj[u][v]:
                for w in range(1, n + 1):
                    if w != u and w != v and adj[u][w] and adj[v][w]:
                        res = sorted([u, v, w])
                        print(res[0], res[1], res[2])
                        return

if __name__ == "__main__":
    solve()
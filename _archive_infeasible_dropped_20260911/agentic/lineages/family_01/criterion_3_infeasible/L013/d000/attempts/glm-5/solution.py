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
        if u > v:
            u, v = v, u
        adj[u][v] = True
        adj[v][u] = True
        edges.append((u, v))
    
    # Sort edges lexicographically to find the smallest triangle first
    edges.sort()
    
    for u, v in edges:
        # We need to find w such that u < w < v and (u, w) and (w, v) are edges
        # Since edges are sorted, we iterate w in increasing order
        for w in range(u + 1, v):
            if adj[u][w] and adj[w][v]:
                print(u, w, v)
                return
    
    # Fallback: if not found by the above (should not happen per problem constraints)
    # We do a full search
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if adj[a][b]:
                for c in range(b + 1, n + 1):
                    if adj[b][c] and adj[a][c]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    solve()
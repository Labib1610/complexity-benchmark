import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True

    # Iterate through all triplets to find the lexicographically smallest valid one
    # A triplet (a, b, c) is valid if it forms a contradictory group.
    # This means the subgraph induced by {a, b, c} is not bipartite.
    # Since there are only 3 vertices, this is true if and only if 
    # the graph contains a triangle (all three edges exist).
    # Proof: 
    # If all 3 edges exist, we have a triangle (odd cycle), which is not bipartite.
    # If 0, 1, or 2 edges exist, the graph is bipartite.
    # Therefore, we just need to find a triangle.
    
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if not adj[a][b]:
                continue
            for c in range(b + 1, n + 1):
                if adj[b][c] and adj[a][c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
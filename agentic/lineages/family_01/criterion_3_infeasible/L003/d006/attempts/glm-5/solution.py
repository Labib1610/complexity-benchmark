import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # We need to find a triangle (a, b, c) with a < b < c, lexicographically smallest.
    # Iterate a from 1 to n-2, b from a+1 to n-1, c from b+1 to n.
    # Check if (a,b), (b,c), (a,c) are all edges.
    # To speed up, we can prune:
    # - b must be a neighbor of a
    # - c must be a neighbor of both a and b
    
    # Iterate over all possible a
    for a in range(1, n - 1):
        # b must be > a and connected to a
        for b in range(a + 1, n):
            if not adj[a][b]:
                continue
            # c must be > b and connected to both a and b
            for c in range(b + 1, n + 1):
                if adj[a][c] and adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
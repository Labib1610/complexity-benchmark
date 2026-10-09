import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
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
    
    # Iterate through all pairs to find the triangle
    # Since a triangle exists, we will find one.
    # To ensure lexicographically smallest, we iterate a < b < c.
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if adj[a][b]:
                for c in range(b + 1, n + 1):
                    if adj[a][c] and adj[b][c]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()
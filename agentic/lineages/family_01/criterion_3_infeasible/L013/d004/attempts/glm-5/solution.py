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
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
    
    # Iterate to find the lexicographically smallest triangle
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if adj[a][b]:
                for c in range(b + 1, n + 1):
                    if adj[a][c] and adj[b][c]:
                        print(a, b, c)
                        return
    
    # Check for triangles of form (1, n-1, n) or (1, n, n-1) etc if loops above missed
    # Actually the loop covers a=1, b=n-1, c=n correctly.
    # The loop range for c is b+1 to n. If b=n-1, c goes up to n.
    
    # Check for triangles of form (a, b, c) where a < b < c
    # The previous loop misses cases where adj[a][b] is False.
    # We need to find any a < b < c such that adj[a][b], adj[b][c], adj[a][c] are all True.
    # The previous loop only checked c if adj[a][b] was True.
    # Correct logic:
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # We need to check if edge (a,b) exists for a triangle, 
            # but actually we just need to iterate all pairs (a,b) and find c.
            # However, if adj[a][b] is False, we can't form a triangle with a,b.
            # So checking adj[a][b] first is a valid optimization.
            if adj[a][b]:
                for c in range(b + 1, n + 1):
                    if adj[a][c] and adj[b][c]:
                        print(a, b, c)
                        return
    # If no triangle found with adj[a][b] true, then no triangle exists.
    # But problem guarantees a solution.

if __name__ == '__main__':
    solve()
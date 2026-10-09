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

    # We need to find a triangle (a, b, c) with a < b < c
    # such that (a,b), (a,c), (b,c) are all edges.
    # The problem guarantees at least one such triangle exists.
    
    # To find the lexicographically smallest triangle,
    # we iterate a from 1 to n, b from a+1 to n, c from b+1 to n.
    # We check if (a,b), (a,c), (b,c) form a triangle.
    # The first one found is the answer.
    
    # Optimization:
    # For each pair (a, b) where a < b and edge (a,b) exists,
    # we look for c > b such that edges (a,c) and (b,c) exist.
    # Since we iterate a and b in increasing order, the first c found is the answer.
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if adj[a][b]:
                # We have edge (a, b). Now find c > b connected to both a and b.
                # We iterate c from b+1 to n.
                for c in range(b + 1, n + 1):
                    if adj[a][c] and adj[b][c]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()
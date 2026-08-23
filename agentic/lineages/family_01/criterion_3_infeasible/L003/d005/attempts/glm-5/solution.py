import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
        degree[u] += 1
        degree[v] += 1
    
    # We need to find a triangle (a, b, c) such that a < b < c, lexicographically smallest.
    # A triangle satisfies the condition: removing any vertex leaves the other two connected.
    
    # Strategy:
    # Iterate 'a' from 1 to n.
    # For each 'a', iterate 'b' from a+1 to n.
    # If edge (a, b) exists, we need to find 'c' such that (a, c) and (b, c) exist, and c > b.
    # To find the smallest valid 'c' efficiently, we can check common neighbors of 'a' and 'b'.
    # Since we iterate 'a' and 'b' in increasing order, the first valid triangle found is the answer.
    
    # Optimization:
    # For a fixed 'a', we iterate 'b'. If (a, b) is an edge, we need to find the smallest c > b
    # such that adj[a][c] and adj[b][c] are true.
    # We can iterate c from b+1 to n. This is O(n) per edge (a, b).
    # Total complexity: sum over all edges (a, b) of n. In worst case O(m*n).
    # With n=2000, m=2*10^5, operations approx 4*10^8, which fits in 2 seconds in Python.
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if adj[a][b]:
                # We have edge a-b. We need c > b connected to both a and b.
                for c in range(b + 1, n + 1):
                    if adj[a][c] and adj[b][c]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()
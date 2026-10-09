import sys
from itertools import combinations

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def build_adjacency_matrix(n, edges):
    # Create adjacency matrix
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    return adj

def is_linearly_independent(v1, v2, v3):
    # Calculate determinant of matrix formed by these 3 vectors
    # | v1[0] v1[1] v1[2] |
    # | v2[0] v2[1] v2[2] |
    # | v3[0] v3[1] v3[2] |
    
    det = (v1[0] * (v2[1] * v3[2] - v2[2] * v3[1]) -
           v1[1] * (v2[0] * v3[2] - v2[2] * v3[0]) +
           v1[2] * (v2[0] * v3[1] - v2[1] * v3[0]))
    
    return det != 0

def solve():
    n, m, edges = read_input()
    adj = build_adjacency_matrix(n, edges)
    
    # Try all combinations of 3 steps in lexicographical order
    for a, b, c in combinations(range(1, n + 1), 3):
        # Construct vectors for steps a, b, c
        v1 = [adj[a][b], adj[a][c], adj[a][a]]  # But adj[a][a] is always 0
        v2 = [adj[b][a], adj[b][c], adj[b][b]]
        v3 = [adj[c][a], adj[c][b], adj[c][c]]
        
        # Since diagonal elements are always 0, we have:
        # v1 = [adj[a][b], adj[a][c], 0]
        # v2 = [adj[b][a], adj[b][c], 0]
        # v3 = [adj[c][a], adj[c][b], 0]
        
        # For 3 vectors in R^3 with last component 0, they're linearly dependent
        # if they're linearly dependent in the first 2 components
        
        # Actually construct the proper vectors according to problem statement
        # v1 represents dependencies of step a with steps a,b,c (excluding self)
        v1 = [0, adj[a][b], adj[a][c]]
        v2 = [adj[b][a], 0, adj[b][c]]
        v3 = [adj[c][a], adj[c][b], 0]
        
        if is_linearly_independent(v1, v2, v3):
            print(a, b, c)
            return

solve()
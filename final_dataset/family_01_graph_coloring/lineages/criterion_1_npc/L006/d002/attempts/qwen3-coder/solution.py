import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all possible colorings
    # For each node, we try colors 1, 2, 3
    def is_valid_coloring(coloring):
        for u, v in edges:
            if abs(coloring[u] - coloring[v]) < 1:
                return False
        return True
    
    # Since we have at most 40 nodes and 3 colors, 
    # we can't try all 3^40 combinations
    # But we can use backtracking with pruning
    
    coloring = [0] * n
    
    def backtrack(node):
        if node == n:
            return True
            
        for color in [1, 2, 3]:
            coloring[node] = color
            valid = True
            # Check if this assignment violates any constraints with already colored neighbors
            for neighbor in adj[node]:
                if neighbor < node:  # Only check already colored neighbors
                    if abs(coloring[node] - coloring[neighbor]) < 1:
                        valid = False
                        break
            
            if valid and backtrack(node + 1):
                return True
                
        coloring[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, coloring)))
    else:
        print("NO")

solve()
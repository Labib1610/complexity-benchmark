import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try to color the graph with 3 colors
    # This is essentially a 3-coloring problem
    # We'll use backtracking
    
    color = [0] * (n + 1)  # color[i] represents the color of node i (1-indexed)
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        
        return False
    
    # Check if 3-coloring is possible
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()
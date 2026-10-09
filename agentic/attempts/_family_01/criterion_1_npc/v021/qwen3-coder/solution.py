import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Colors: 0 = uncolored, 1, 2, 3 = colors
    colors = [0] * (n + 1)
    
    # Check if graph is 3-colorable using backtracking
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # If node has no edges, we can assign any color
        if not adj[node]:
            colors[node] = 1
            if backtrack(node + 1):
                return True
            colors[node] = 0
            return False
            
        for color in [1, 2, 3]:
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        
        return False
    
    # Handle special case of no edges
    if m == 0:
        print("YES")
        result = [1] * n
        print(*result)
        return
    
    # Try to color the graph
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()
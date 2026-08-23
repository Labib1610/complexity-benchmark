import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors for each node (0 means uncolored)
    colors = [0] * (n + 1)
    
    # Try to color the graph with 3 colors using backtracking
    # We want the lexicographically smallest coloring
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        
        return False
    
    # Check if the graph is 3-colorable
    if not backtrack(1):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, colors[1:])))

solve()
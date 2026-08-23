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
    
    # Try to color the graph with 3 colors (hoppers 1, 2, 3)
    # We want the lexicographically smallest assignment
    colors = [0] * (n + 1)  # colors[i] represents hopper for ingredient i
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
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
                colors[node] = 0  # backtrack
                
        return False
    
    # Start with ingredient 1 and try to find a valid assignment
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, colors[1:])))
    else:
        print("NO")

solve()
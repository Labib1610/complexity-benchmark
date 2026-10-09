import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors: 0 = uncolored, 1, 2, 3 = colors
    color = [0] * (n + 1)
    
    # Check if graph is 3-colorable using backtracking
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        if color[node] != 0:
            return backtrack(node + 1)
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Try to color all components
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()
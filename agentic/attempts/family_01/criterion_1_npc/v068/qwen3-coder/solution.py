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
    
    # Colors: 1, 2, 3 (we need at most 3 colors)
    # Use backtracking to find lexicographically smallest valid coloring
    color = [0] * (n + 1)  # color[i] represents the color of node i
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # backtrack
                
        return False
    
    # Since we want lexicographically smallest, we try colors in order 1, 2, 3
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()
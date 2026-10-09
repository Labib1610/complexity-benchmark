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
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color the graph with 3 colors using backtracking
    # Colors: 1, 2, 3
    color = [0] * (n + 1)  # color[i] represents color of node i
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # Try colors 1, 2, 3 in order for lexicographically smallest result
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
        
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()
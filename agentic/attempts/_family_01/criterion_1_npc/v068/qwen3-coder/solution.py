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
    
    # Try to 3-color the graph
    color = [-1] * n  # -1 means uncolored, 0, 1, 2 are the three colors
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def dfs(node):
        if node == n:
            return True
        
        for c in range(3):
            if is_valid(node, c):
                color[node] = c
                if dfs(node + 1):
                    return True
                color[node] = -1  # Backtrack
        
        return False
    
    # Start coloring from node 0
    if dfs(0):
        print("YES")
        result = [str(c + 1) for c in color]  # Convert back to 1-indexed colors
        print(" ".join(result))
    else:
        print("NO")

solve()
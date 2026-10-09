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
    
    # Try all possible 3-colorings
    # Each asset can be assigned to portfolio 1, 2, or 3
    # This is essentially a graph 3-coloring problem
    
    # We'll use backtracking with constraint checking
    color = [0] * (n + 1)  # color[i] represents the portfolio for asset i
    
    def is_valid(node, c):
        # Check if assigning color c to node is valid
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        if color[node] != 0:  # Already colored
            return backtrack(node + 1)
            
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Try to find a valid coloring
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()
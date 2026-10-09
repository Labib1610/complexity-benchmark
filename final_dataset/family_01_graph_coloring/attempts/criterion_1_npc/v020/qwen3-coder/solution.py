import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Try all 3-colorings
    # Each table can be assigned to drive 1, 2, or 3
    # This is essentially a graph 3-coloring problem
    
    # We'll use backtracking
    color = [0] * (n + 1)  # color[i] represents the drive for table i
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
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
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()
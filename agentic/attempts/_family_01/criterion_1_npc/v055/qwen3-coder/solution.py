import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # Try to 3-color the graph
    color = [0] * (n + 1)  # color[i] represents the color of node i (1, 2, or 3)
    
    def is_valid(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(" ".join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()
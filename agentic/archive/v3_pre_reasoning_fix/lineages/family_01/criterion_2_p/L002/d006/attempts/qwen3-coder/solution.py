import sys
from collections import defaultdict, deque

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
    
    # For each edge, the sum of flow rates must be exactly 3
    # This means if one node has flow rate 1, the other must have 2, and vice versa
    # This is a 2-coloring problem (or bipartite check)
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct the solution
    # For lexicographically smallest, we want nodes with color 0 to have flow rate 1
    # and nodes with color 1 to have flow rate 2
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append(1)
        else:
            result.append(2)
    
    print("YES")
    print(" ".join(map(str, result)))

solve()
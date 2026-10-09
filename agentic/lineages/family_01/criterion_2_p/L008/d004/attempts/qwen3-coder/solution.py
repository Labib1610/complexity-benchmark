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
    
    # Color the graph with BFS to check if it's bipartite
    color = [-1] * n
    
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Not bipartite - impossible to satisfy constraints
                        print("NO")
                        return
    
    # Check if the product can be 3^m
    # For each edge (u,v), we want c[u] + c[v] = 3
    # This means one should be 1 and the other should be 2
    # So we need a bipartite graph where colors correspond to values 1 and 2
    
    # Verify the solution
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Construct the assignment
    assignment = []
    for i in range(n):
        if color[i] == 0:
            assignment.append("1")
        else:
            assignment.append("2")
    
    print("YES")
    print(" ".join(assignment))

solve()
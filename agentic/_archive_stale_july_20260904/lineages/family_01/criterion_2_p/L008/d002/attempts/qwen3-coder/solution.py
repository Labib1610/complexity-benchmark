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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # The valid pairs for the sequence [1,2,1] are:
    # (1,2) and (2,1) - meaning if u has value 1, v must have value 2 and vice versa
    
    # This is essentially a 2-coloring problem where each edge represents 
    # that the two nodes must have different values
    
    # But we also need to check if the graph is bipartite with the constraint
    # that valid assignments are 1->2 or 2->1
    
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
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
                        print("NO")
                        return
    
    # If bipartite, construct the assignment
    # We want the lexicographically smallest assignment
    # So we try assigning 1 to node 1 first, then propagate
    
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    # Verify the solution
    for u, v in edges:
        seq = [assignment[u], assignment[v]]
        if seq not in [[1, 2], [2, 1]]:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()
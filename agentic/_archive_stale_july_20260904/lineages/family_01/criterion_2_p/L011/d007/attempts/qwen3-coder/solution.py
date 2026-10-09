import sys
from collections import defaultdict, deque

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
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For the network to be perfectly balanced, each edge must have capacity 3
    # This means for each edge (u,v), we need x[u] + x[v] = 3
    # So if x[u] = 1, then x[v] = 2, and vice versa
    # This is a bipartite graph coloring problem where colors are {1,2}
    
    color = [-1] * n  # -1: unvisited, 0: should be 1, 1: should be 2
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
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
    
    # If bipartite, construct the assignment
    # color 0 -> tier 1, color 1 -> tier 2
    assignment = []
    for i in range(n):
        if color[i] == 0:
            assignment.append(1)
        else:
            assignment.append(2)
    
    # Verify the solution
    for u, v in edges:
        if assignment[u] + assignment[v] != 3:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()
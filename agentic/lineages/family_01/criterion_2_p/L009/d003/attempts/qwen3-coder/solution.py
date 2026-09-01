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
    
    # Try to 2-color the graph (check if bipartite)
    color = [-1] * n
    
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
    
    # Check if the solution satisfies all edges
    # For each edge, one endpoint should be 0 (power 1) and other should be 1 (power 2)
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Convert colors to power levels (0 -> 1, 1 -> 2)
    power = [1 if c == 0 else 2 for c in color]
    
    print("YES")
    print(" ".join(map(str, power)))

solve()
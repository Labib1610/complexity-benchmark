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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color the graph with BFS (2-coloring / bipartite check)
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    # We need to ensure the product of tiers is 2 for each edge
    # This means adjacent nodes must have different colors
    # In terms of tiers: one must be 1 and the other 2
    
    # Check if our coloring satisfies the constraint
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Convert colors to tiers
    # To get lexicographically smallest, we want tier 1 wherever possible
    # Color 1 -> tier 1, Color 2 -> tier 2
    tiers = []
    for i in range(1, n + 1):
        if color[i] == 1:
            tiers.append("1")
        else:
            tiers.append("2")
    
    print("YES")
    print(" ".join(tiers))

solve()
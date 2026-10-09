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
    
    # Try to 2-color the graph
    # But the constraint is that product of levels = 2
    # So one must be 1 and other must be 2
    # This means it's a bipartite graph where we assign 1 and 2 instead of 0 and 1
    
    color = [0] * (n + 1)  # 0: unvisited, 1: level 1, 2: level 2
    
    # Check all components
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color this component
            queue = deque([start])
            color[start] = 1  # Start with level 1
            
            while queue:
                node = queue.popleft()
                node_color = color[node]
                
                # The neighbor should have color such that node_color * neighbor_color = 2
                # If node_color = 1, neighbor_color should be 2
                # If node_color = 2, neighbor_color should be 1
                required_neighbor_color = 2 // node_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = required_neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != required_neighbor_color:
                        print("NO")
                        return
    
    # Verify the solution
    for u, v in edges:
        if color[u] * color[v] != 2:
            print("NO")
            return
    
    # Output the lexicographically smallest solution
    # Since we started with color 1 for each component's first node,
    # this should already be lexicographically minimal
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

solve()
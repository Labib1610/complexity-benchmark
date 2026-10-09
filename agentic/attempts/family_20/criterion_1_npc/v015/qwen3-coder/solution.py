import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Try to color the edges with 3 colors such that no vertex has two edges of the same color
    # This is equivalent to edge-coloring with 3 colors for a 3-regular graph
    
    # We'll use BFS-like approach to assign colors
    color = [0] * m  # 0 means uncolored, 1, 2, 3 are the colors
    colored = [False] * m
    
    # For each vertex, we need to assign 3 different colors to its 3 edges
    for vertex in range(1, n + 1):
        incident_edges = adj[vertex]
        available_colors = {1, 2, 3}
        edge_colors = {}
        
        # First, see which edges are already colored
        for neighbor, edge_idx in incident_edges:
            if colored[edge_idx]:
                edge_colors[edge_idx] = color[edge_idx]
                available_colors.discard(color[edge_idx])
        
        # Assign colors to uncolored edges
        uncolored_edges = [(neighbor, edge_idx) for neighbor, edge_idx in incident_edges if not colored[edge_idx]]
        
        if len(uncolored_edges) > len(available_colors):
            print("NO")
            return
            
        # Assign remaining colors to uncolored edges
        uncolored_indices = [edge_idx for _, edge_idx in uncolored_edges]
        available_list = list(available_colors)
        
        for i, edge_idx in enumerate(uncolored_indices):
            if i >= len(available_list):
                print("NO")
                return
            color[edge_idx] = available_list[i]
            colored[edge_idx] = True
    
    # Verify the solution
    for vertex in range(1, n + 1):
        incident_edges = adj[vertex]
        colors_used = set()
        for neighbor, edge_idx in incident_edges:
            if color[edge_idx] in colors_used:
                print("NO")
                return
            colors_used.add(color[edge_idx])
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
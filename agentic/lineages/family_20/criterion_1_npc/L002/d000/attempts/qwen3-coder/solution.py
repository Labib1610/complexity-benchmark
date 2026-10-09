import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store edges with their indices
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Try to 3-color the edges such that at each vertex, all incident edges have different colors
    # This is equivalent to edge coloring where each vertex has degree 3
    
    edge_colors = [0] * m  # 0 means uncolored
    colored = [False] * m
    
    # For each vertex, we need to assign 3 different colors to its 3 edges
    # We'll use a greedy approach
    
    # Build adjacency for edges (line graph)
    edge_adj = [[] for _ in range(m)]
    
    # For each vertex, connect all its incident edges in the line graph
    for vertex in range(1, n+1):
        incident_edges = adj[vertex]
        for i in range(len(incident_edges)):
            for j in range(i+1, len(incident_edges)):
                idx1 = incident_edges[i][1]
                idx2 = incident_edges[j][1]
                edge_adj[idx1].append(idx2)
                edge_adj[idx2].append(idx1)
    
    # Greedy coloring
    def is_valid_color(edge_idx, color):
        for neighbor in edge_adj[edge_idx]:
            if edge_colors[neighbor] == color:
                return False
        return True
    
    # Try to color edges one by one
    for edge_idx in range(m):
        found_color = False
        for color in range(1, 4):  # Colors 1, 2, 3
            if is_valid_color(edge_idx, color):
                edge_colors[edge_idx] = color
                found_color = True
                break
        if not found_color:
            print("NO")
            return
    
    print("YES")
    print(*edge_colors)

solve()
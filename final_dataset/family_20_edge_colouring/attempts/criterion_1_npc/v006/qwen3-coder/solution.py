import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Store edges with their indices
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Color array for edges (1-indexed)
    color = [0] * m
    
    # Try to 3-color the edges such that at each vertex, all incident edges have different colors
    # This is essentially edge coloring of a cubic graph with 3 colors
    
    # We'll use a greedy approach with backtracking if needed
    # But for cubic graphs, if 3-edge-coloring exists, it can be found efficiently
    
    # Build adjacency list for edges
    edge_adj = [[] for _ in range(m)]
    
    # For each vertex, connect all its incident edges
    for vertex in range(1, n + 1):
        incident_edges = [i for _, i in adj[vertex]]
        # Connect each pair of incident edges
        for i in range(len(incident_edges)):
            for j in range(i + 1, len(incident_edges)):
                edge_adj[incident_edges[i]].append(incident_edges[j])
                edge_adj[incident_edges[j]].append(incident_edges[i])
    
    # Try to color edges with 3 colors
    def is_safe(edge_idx, c):
        for neighbor in edge_adj[edge_idx]:
            if color[neighbor] == c:
                return False
        return True
    
    def graph_coloring(edge_idx):
        if edge_idx == m:
            return True
            
        for c in range(1, 4):
            if is_safe(edge_idx, c):
                color[edge_idx] = c
                if graph_coloring(edge_idx + 1):
                    return True
                color[edge_idx] = 0
                
        return False
    
    # This might be too slow for large inputs, let's try a different approach
    # Since this is a cubic graph, we can try a more systematic approach
    
    # Let's model this as finding a proper edge coloring
    # In a cubic graph, 3-edge-coloring exists iff the graph is class 1
    # All bipartite cubic graphs are class 1
    
    # Check if graph is bipartite and try a constructive approach
    
    # Actually, let's implement a simpler backtracking with better data structures
    used_colors_at_vertex = [set() for _ in range(n + 1)]
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if c not in used_colors_at_vertex[u] and c not in used_colors_at_vertex[v]:
                # Assign color c to edge edge_idx
                color[edge_idx] = c
                used_colors_at_vertex[u].add(c)
                used_colors_at_vertex[v].add(c)
                
                if backtrack(edge_idx + 1):
                    return True
                    
                # Backtrack
                used_colors_at_vertex[u].remove(c)
                used_colors_at_vertex[v].remove(c)
                
        return False
    
    if backtrack(0):
        print("YES")
        print(*color)
    else:
        print("NO")

solve()
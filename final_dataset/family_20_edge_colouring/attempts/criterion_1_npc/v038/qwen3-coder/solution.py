import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    K = 2 * m // n
    
    # Store edges with their indices
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to color the edges
    # This is essentially edge coloring where each vertex has degree K
    # and we have exactly K colors
    
    # For a K-regular graph (each vertex has degree K), 
    # edge chromatic number is either K or K+1 by Vizing's theorem
    # But since we have exactly K colors and the graph is K-regular,
    # it's K-edge-colorable iff it satisfies certain conditions
    
    # However, given the constraints, let's try a constructive approach
    
    # Since m = 3*n/2 and each vertex has degree K = 2*m/n = 3,
    # this is a 3-regular graph and we need to 3-color the edges
    
    colors = [0] * m  # 0 means uncolored
    
    # Build adjacency list for edges (line graph)
    edge_adj = [[] for _ in range(m)]
    
    for v in range(1, n + 1):
        incident_edges = adj[v]
        # Each pair of incident edges at vertex v are adjacent in line graph
        for i in range(len(incident_edges)):
            for j in range(i + 1, len(incident_edges)):
                edge_adj[incident_edges[i]].append(incident_edges[j])
                edge_adj[incident_edges[j]].append(incident_edges[i])
    
    # Greedy coloring of line graph with K colors
    available = [True] * (K + 1)  # index 0 unused
    
    for i in range(m):
        # Mark colors used by neighbors
        for neighbor in edge_adj[i]:
            if colors[neighbor] > 0:
                available[colors[neighbor]] = False
        
        # Find first available color
        found_color = False
        for c in range(1, K + 1):
            if available[c]:
                colors[i] = c
                found_color = True
                break
        
        if not found_color:
            print("NO")
            return
        
        # Reset availability
        for neighbor in edge_adj[i]:
            if colors[neighbor] > 0:
                available[colors[neighbor]] = True
    
    # Verify the solution
    for v in range(1, n + 1):
        incident_colors = set()
        for edge_idx in adj[v]:
            incident_colors.add(colors[edge_idx])
        if len(incident_colors) != K or 0 in incident_colors:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, colors)))

solve()
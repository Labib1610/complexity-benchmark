import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list and edge list
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    # Check if each vertex has degree 3
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Try to 3-color the edges such that at each vertex, all 3 edges have different colors
    # This is equivalent to finding a proper edge coloring with 3 colors for a 3-regular graph
    
    # We'll use a BFS-like approach to assign colors
    color = [-1] * m  # -1 means uncolored
    colored = [False] * m
    
    # Process each component
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
            
        # BFS to process this component
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            
            # Get the edges incident to u
            incident_edges = adj[u]
            used_colors = set()
            uncolored_edges = []
            
            # Check which edges are already colored and which are not
            for v, edge_idx in incident_edges:
                if colored[edge_idx]:
                    used_colors.add(color[edge_idx])
                else:
                    uncolored_edges.append((v, edge_idx))
            
            # If we have more than 3 edges already colored with different colors, impossible
            if len(used_colors) > 3:
                print("NO")
                return
                
            # Assign colors to uncolored edges
            available_colors = {1, 2, 3} - used_colors
            
            if len(uncolored_edges) > len(available_colors):
                print("NO")
                return
                
            # Assign available colors to uncolored edges
            avail_list = list(available_colors)
            for i, (v, edge_idx) in enumerate(uncolored_edges):
                if i >= len(avail_list):
                    print("NO")
                    return
                color[edge_idx] = avail_list[i]
                colored[edge_idx] = True
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
    
    # Verify the solution
    for u in range(n):
        colors_at_u = set()
        for v, edge_idx in adj[u]:
            if color[edge_idx] == -1 or color[edge_idx] not in {1, 2, 3}:
                print("NO")
                return
            colors_at_u.add(color[edge_idx])
        if len(colors_at_u) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
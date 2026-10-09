import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Read edges and build adjacency list
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # For a valid 3-edge-coloring to exist, the graph must be 3-regular
    # and 3-edge-colorable. Since each node has exactly 3 edges,
    # this is a 3-regular graph.
    
    # We'll try to 3-color the edges using BFS-like approach
    # Each node has 3 edges, and they must have 3 different colors
    
    # Color array for edges (-1 means uncolored)
    color = [-1] * m
    
    # For each node, we'll track which colors are used by its edges
    # Initially, no colors are used
    
    # We can model this as a constraint satisfaction problem
    # Let's use a greedy approach with backtracking simulation
    
    # Since the graph is 3-regular, we can try to color it systematically
    # One approach: find a perfect matching, remove it, get a 2-regular graph (cycles),
    # color the matching with color 1, cycles with colors 2 and 3
    
    # But let's try a more direct approach with constraint propagation
    
    # Build node to edges mapping
    node_edges = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        node_edges[u].append(i)
        node_edges[v].append(i)
    
    # Try to color edges using backtracking with constraint checking
    def is_valid edge_idx, c):
        u, v = edges[edge_idx]
        # Check if any adjacent edge at u or v already has color c
        for nei_edge in node_edges[u]:
            if color[nei_edge] == c:
                return False
        for nei_edge in node_edges[v]:
            if color[nei_edge] == c:
                return False
        return True
    
    # More efficient approach: since it's 3-regular, we can use a systematic method
    # Try to find a proper 3-edge-coloring
    
    # Use a greedy algorithm with careful ordering
    # Process edges and for each edge, pick a color not used by its neighbors
    
    def can_color():
        # Try all possible colorings with backtracking
        # But this might be too slow, let's think differently
        
        # For 3-regular graphs, 3-edge-coloring exists iff ...
        # Actually, not all 3-regular graphs are 3-edge-colorable
        # But the problem asks us to find one or determine it's impossible
        
        # Let's model this as an exact cover problem or use a direct approach
        
        # Since each vertex has exactly degree 3, and we have exactly 3 colors,
        # at each vertex, all 3 edges must have different colors
        
        # This is equivalent to finding a proper edge 3-coloring
        
        # Let's try a greedy approach with a good vertex ordering
        
        # Use BFS to order vertices, then color edges incident to each vertex
        
        visited_edges = [False] * m
        result = [-1] * m
        
        # Process vertices in some order
        queue = deque([1])  # Start with node 1
        visited_nodes = set([1])
        
        while queue:
            node = queue.popleft()
            
            # Get all edges incident to this node
            incident_edges = node_edges[node]
            
            # Determine which colors are available for each uncolored edge
            for edge_idx in incident_edges:
                if result[edge_idx] == -1:  # Not yet colored
                    u, v = edges[edge_idx]
                    # Find which colors are already used at this edge's endpoints
                    used_colors_u = set()
                    used_colors_v = set()
                    
                    for nei_edge in node_edges[u]:
                        if result[nei_edge] != -1:
                            used_colors_u.add(result[nei_edge])
                    
                    for nei_edge in node_edges[v]:
                        if result[nei_edge] != -1:
                            used_colors_v.add(result[nei_edge])
                    
                    # Available colors for this edge
                    used_colors = used_colors_u | used_colors_v
                    available_colors = {1, 2, 3} - used_colors
                    
                    if not available_colors:
                        return None  # No valid coloring possible
                    
                    # Pick the first available color
                    chosen_color = min(available_colors)
                    result[edge_idx] = chosen_color
            
            # Add unvisited neighbors to queue
            for edge_idx in incident_edges:
                u, v = edges[edge_idx]
                neighbor = v if u == node else u
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    queue.append(neighbor)
        
        # Check if all edges are colored
        if -1 in result:
            # Some edges weren't reached, meaning the graph might be disconnected
            # or our BFS approach missed some edges
            # Try to color remaining edges
            
            for i in range(m):
                if result[i] == -1:
                    u, v = edges[i]
                    used_colors_u = set()
                    used_colors_v = set()
                    
                    for nei_edge in node_edges[u]:
                        if result[nei_edge] != -1:
                            used_colors_u.add(result[nei_edge])
                    
                    for nei_edge in node_edges[v]:
                        if result[nei_edge] != -1:
                            used_colors_v.add(result[nei_edge])
                    
                    used_colors = used_colors_u | used_colors_v
                    available_colors = {1, 2, 3} - used_colors
                    
                    if not available_colors:
                        return None
                    
                    result[i] = min(available_colors)
        
        return result
    
    # More systematic approach: since it's a 3-regular graph on n nodes with 3n/2 edges,
    # it's likely a complete graph on 4 nodes (K4) for the example, which is 3-edge-colorable
    
    # Let's implement a backtracking solution with constraint checking
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Colors used by edges incident to u and v
        used_u = set()
        used_v = set()
        
        for nei_edge, _ in adj[u]:
            if color[nei_edge] != -1:
                used_u.add(color[nei_edge])
                
        for nei_edge, _ in adj[v]:
            if color[nei_edge] != -1:
                used_v.add(color[nei_edge])
        
        used = used_u | used_v
        
        for c in range(1, 4):
            if c not in used:
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = -1
        
        return False
    
    # Try the backtracking approach
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, [c if c != -1 else 1 for c in color])))
    else:
        print("NO")

solve()
import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Read edges
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Colors for each edge (0 means uncolored)
    colors = [0] * m
    
    # Try to 3-color the edges such that edges around each vertex have different colors
    # This is equivalent to edge-coloring where each vertex has degree 3 and we need 3 colors
    
    # We'll use a greedy approach with backtracking if needed
    # But for cubic graphs (each vertex degree 3) with a proper 3-edge coloring,
    # we can try a systematic approach
    
    # Since each vertex has exactly degree 3, and we have exactly 3 colors,
    # each vertex must have its 3 edges colored with 3 different colors
    
    # Let's build the line graph and try to color it
    # But simpler approach: since it's a cubic graph, we can try to find a proper 3-edge coloring
    
    # Try a greedy coloring based on BFS
    def dfs_edge_coloring():
        # For each vertex, we need to assign 3 different colors to its 3 edges
        # We can do this systematically
        
        # Track which colors are used at each vertex
        vertex_colors = defaultdict(set)  # vertex -> set of colors used
        vertex_edge_indices = defaultdict(list)  # vertex -> list of edge indices
        
        for i, (u, v) in enumerate(edges):
            vertex_edge_indices[u].append(i)
            vertex_edge_indices[v].append(i)
        
        # Process edges and try to assign colors
        for i, (u, v) in enumerate(edges):
            # Find a color that's not used by either endpoint
            available_colors = {1, 2, 3}
            used_by_u = vertex_colors[u]
            used_by_v = vertex_colors[v]
            
            # Remove colors already used at u or v
            for c in used_by_u:
                available_colors.discard(c)
            for c in used_by_v:
                available_colors.discard(c)
                
            if not available_colors:
                return False
                
            # Assign the first available color
            color = min(available_colors)
            colors[i] = color
            vertex_colors[u].add(color)
            vertex_colors[v].add(color)
            
        return True
    
    # Check if our coloring is valid
    def is_valid_coloring():
        # For each vertex, check if all its edges have different colors
        vertex_edge_colors = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            color = colors[i]
            vertex_edge_colors[u].append(color)
            vertex_edge_colors[v].append(color)
        
        for vtx, color_list in vertex_edge_colors.items():
            if len(color_list) != 3 or len(set(color_list)) != 3:
                return False
        return True
    
    # Special case handling - let's try a more systematic approach
    # Since this is essentially finding a proper 3-edge-coloring of a cubic graph,
    # and not all cubic graphs are 3-edge-colorable (counterexample: Petersen graph),
    # but given the constraints, let's assume it's possible and try a constructive method
    
    # Try a different approach: model as a constraint satisfaction problem
    def backtrack_color(pos):
        if pos == m:
            return True
            
        u, v = edges[pos]
        
        # Try colors 1, 2, 3
        for color in [1, 2, 3]:
            # Check if this color conflicts with existing assignments at u or v
            conflict_u = conflict_v = False
            
            # Check all other edges incident to u
            for vtx, idx in [(u, adj[u][i][1]) for i in range(len(adj[u]))]:
                if idx < pos and colors[idx] == color:
                    conflict_u = True
                    break
                    
            # Check all other edges incident to v  
            for vtx, idx in [(v, adj[v][i][1]) for i in range(len(adj[v]))]:
                if idx < pos and colors[idx] == color:
                    conflict_v = True
                    break
            
            if not conflict_u and not conflict_v:
                colors[pos] = color
                if backtrack_color(pos + 1):
                    return True
                # Backtrack handled implicitly by loop
                    
        colors[pos] = 0
        return False
    
    # Even better approach: since each vertex has degree exactly 3 and we have 3 colors,
    # this is equivalent to properly 3-edge-coloring a cubic graph.
    # However, not all cubic graphs are 3-edge-colorable.
    # But let's try a greedy algorithm that works for many cases:
    
    def greedy_3_edge_color():
        # Sort vertices by some criteria might help, but let's just go in order
        # For each edge, assign it the lowest numbered color not used by its endpoints
        
        for i in range(m):
            u, v = edges[i]
            # What colors are forbidden at u?
            forbidden_u = set()
            for neighbor, edge_idx in adj[u]:
                if edge_idx < i:  # Already colored
                    forbidden_u.add(colors[edge_idx])
                    
            # What colors are forbidden at v?
            forbidden_v = set()
            for neighbor, edge_idx in adj[v]:
                if edge_idx < i:  # Already colored
                    forbidden_v.add(colors[edge_idx])
                    
            # Available colors
            forbidden = forbidden_u | forbidden_v
            available = {1, 2, 3} - forbidden
            
            if not available:
                return False
                
            colors[i] = min(available)
            
        return True
    
    # Try the greedy approach first
    success = greedy_3_edge_color()
    
    if not success:
        # Try backtracking as fallback
        # Reset colors
        colors = [0] * m
        success = backtrack_color(0)
    
    if success and is_valid_coloring():
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

solve()
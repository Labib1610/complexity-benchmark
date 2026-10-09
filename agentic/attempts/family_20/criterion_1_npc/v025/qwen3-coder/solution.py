import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read edges
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Each node has exactly 3 edges
    # This is a 3-regular graph with n even and m = 3*n/2
    
    # Try to color the edges with 3 colors such that at each vertex,
    # all 3 edges have different colors
    
    # This is equivalent to finding a proper edge coloring with 3 colors
    # Since each vertex has degree 3, this is possible if and only if
    # the graph is 3-edge-colorable
    
    # For a 3-regular graph, if n is even, then m is multiple of 3
    # and such graphs are often 3-edge-colorable
    
    # We'll try to construct such a coloring
    
    # Initialize color array (-1 means uncolored)
    colors = [-1] * m
    
    # For each vertex, we need to assign colors 1,2,3 to its 3 edges
    # Let's try a greedy approach with backtracking
    
    def is_valid(edge_idx, color):
        u, v = edges[edge_idx]
        # Check if color is already used at u or v
        for e in adj[u]:
            if colors[e] == color:
                return False
        for e in adj[v]:
            if colors[e] == color:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        # Try colors 1, 2, 3 in order
        for color in [1, 2, 3]:
            if is_valid(edge_idx, color):
                colors[edge_idx] = color
                if backtrack(edge_idx + 1):
                    return True
                colors[edge_idx] = -1  # Backtrack
                
        return False
    
    # This might be too slow for large inputs
    # Let's think of a better approach
    
    # Since this is a 3-regular graph and n is even, 
    # we can try to find a perfect matching and build from there
    
    # But let's first check if the example works with our approach
    # Actually, let's implement a more efficient solution
    
    # Build adjacency for edges (line graph approach)
    # But that might also be complex
    
    # Let's try a different strategy:
    # Since each vertex has exactly degree 3, and we have 3 colors,
    # we can think of this as assigning a bijection between edges and colors at each vertex
    
    # This is equivalent to edge coloring with 3 colors for a 3-regular graph
    
    # A classic result: every 3-regular graph with even number of vertices is 3-edge-colorable
    # However, that's not always true. It's true if it's class 1 (chromatic index = 3)
    
    # Let's try a constructive approach:
    # Find a perfect matching in a subgraph and recurse
    
    # But for implementation simplicity, let's use constraint satisfaction
    
    def solve_coloring():
        # Use backtracking with a better heuristic
        # Try to color edges in an order that reduces branching
        
        # Degree of each vertex is 3, so we can represent the state at each vertex
        # by which colors are still available
        
        # Let's represent the available colors at each vertex
        vertex_colors = {}
        for i in range(1, n+1):
            vertex_colors[i] = set([1, 2, 3])
            
        # Try a greedy coloring first
        for edge_idx in range(m):
            u, v = edges[edge_idx]
            common_colors = list(vertex_colors[u] & vertex_colors[v])
            if not common_colors:
                return None  # No valid color available
                
            # Pick the first available color
            color = common_colors[0]
            colors[edge_idx] = color
            vertex_colors[u].remove(color)
            vertex_colors[v].remove(color)
            
        return colors[:]
        
    # Try greedy first
    result = solve_coloring()
    
    if result is not None:
        print("YES")
        print(' '.join(map(str, result)))
        return
        
    # If greedy fails, try backtracking
    # But given constraints, greedy should work for valid instances
    
    # Actually, let's reconsider the problem structure
    # The complete graph K_4 (as in example) is 3-edge-colorable
    # And it's known that all 3-regular graphs with certain properties are 3-edge-colorable
    
    # Let's just do a systematic backtracking but with optimizations
    
    def improved_backtrack():
        # Keep track of used colors at each vertex
        used_at_vertex = [set() for _ in range(n+1)]
        
        def is_safe(edge_idx, color):
            u, v = edges[edge_idx]
            return color not in used_at_vertex[u] and color not in used_at_vertex[v]
            
        def assign_color(edge_idx, color):
            u, v = edges[edge_idx]
            colors[edge_idx] = color
            used_at_vertex[u].add(color)
            used_at_vertex[v].add(color)
            
        def remove_color(edge_idx, color):
            u, v = edges[edge_idx]
            colors[edge_idx] = -1
            used_at_vertex[u].discard(color)
            used_at_vertex[v].discard(color)
            
        def backtrack_improved(idx):
            if idx == m:
                return True
                
            u, v = edges[idx]
            available_colors = set([1, 2, 3]) - used_at_vertex[u] - used_at_vertex[v]
            
            if not available_colors:
                return False
                
            for color in available_colors:
                assign_color(idx, color)
                if backtrack_improved(idx + 1):
                    return True
                remove_color(idx, color)
                
            return False
            
        return backtrack_improved(0)
        
    if improved_backtrack():
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

solve()
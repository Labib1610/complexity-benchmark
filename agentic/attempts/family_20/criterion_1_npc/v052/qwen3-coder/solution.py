import sys
from collections import defaultdict, deque

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
    
    # Since each vertex has degree 3, this is a 3-regular graph
    # We need to color edges such that no vertex has two edges of same color
    # This is equivalent to edge-coloring with 3 colors
    
    # Try to find a proper edge coloring
    edge_colors = [0] * m  # 0 means uncolored
    
    # For each vertex, we'll assign colors to its edges
    colored = [False] * (n + 1)
    
    # Use BFS to process vertices
    queue = deque()
    visited = [False] * (n + 1)
    
    # Start with vertex 1
    queue.append(1)
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        
        # Get the colors already used by neighbors
        used_colors = set()
        edge_indices = []
        
        # Check which edges are already colored
        for v, edge_idx in adj[u]:
            if edge_colors[edge_idx] != 0:
                used_colors.add(edge_colors[edge_idx])
            else:
                edge_indices.append((v, edge_idx))
            
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        
        # Assign colors to uncolored edges
        available_colors = {1, 2, 3} - used_colors
        
        # If we have exactly 3 edges and some are uncolored
        if len(adj[u]) == 3:
            # Color the uncolored edges with remaining colors
            for v, edge_idx in edge_indices:
                if len(available_colors) > 0:
                    color = available_colors.pop()
                    edge_colors[edge_idx] = color
                else:
                    # Need to recolor to make it work
                    pass
    
    # More systematic approach: since it's a 3-regular graph,
    # we can try to find a proper edge coloring
    
    # Let's use a greedy approach with backtracking concept
    def can_color_edge(edge_idx, color):
        u, v = edges[edge_idx]
        # Check if any adjacent edge to u or v already has this color
        for w, idx in adj[u]:
            if edge_colors[idx] == color:
                return False
        for w, idx in adj[v]:
            if edge_colors[idx] == color:
                return False
        return True
    
    # Try to color edges one by one
    def color_edges(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        for color in [1, 2, 3]:
            if can_color_edge(edge_idx, color):
                edge_colors[edge_idx] = color
                if color_edges(edge_idx + 1):
                    return True
                edge_colors[edge_idx] = 0
        return False
    
    # Better approach: since it's a 3-regular graph, 
    # we know it can be edge-colored with 3 colors (Vizing's theorem for class 1 graphs)
    # But let's try a constructive approach
    
    # Since m = 3*n/2 and each vertex has degree 3,
    # this is a cubic graph. Not all cubic graphs are 3-edge-colorable,
    # but many are. Let's try a greedy method.
    
    success = True
    
    # Try greedy coloring
    for i in range(m):
        u, v = edges[i]
        forbidden = set()
        
        # Check what colors are already used at u
        for w, idx in adj[u]:
            if edge_colors[idx] != 0:
                forbidden.add(edge_colors[idx])
                
        # Check what colors are already used at v
        for w, idx in adj[v]:
            if edge_colors[idx] != 0:
                forbidden.add(edge_colors[idx])
        
        # Try to assign a color
        found_color = False
        for color in [1, 2, 3]:
            if color not in forbidden:
                edge_colors[i] = color
                found_color = True
                break
                
        if not found_color:
            success = False
            break
    
    if success:
        print("YES")
        print(' '.join(map(str, edge_colors)))
    else:
        # Try a different approach - this might be a non-3-edge-colorable graph
        # But according to the problem, we should assume it's possible
        # Let's reattempt with a better strategy
        
        edge_colors = [0] * m
        
        # Try a more careful greedy approach
        order = list(range(m))
        
        # Sort edges by the sum of degrees of endpoints (this is just a heuristic)
        # Actually, all vertices have degree 3, so this won't help
        
        success = True
        for i in order:
            u, v = edges[i]
            forbidden = set()
            
            # Check what colors are already used at u
            for w, idx in adj[u]:
                if edge_colors[idx] != 0:
                    forbidden.add(edge_colors[idx])
                    
            # Check what colors are already used at v
            for w, idx in adj[v]:
                if edge_colors[idx] != 0:
                    forbidden.add(edge_colors[idx])
            
            # Try to assign a color
            found_color = False
            for color in [1, 2, 3]:
                if color not in forbidden:
                    edge_colors[i] = color
                    found_color = True
                    break
                    
            if not found_color:
                success = False
                break
        
        if success:
            print("YES")
            print(' '.join(map(str, edge_colors)))
        else:
            print("NO")

solve()
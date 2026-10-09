import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to 3-color the edges such that edges incident to each vertex have different colors
    # This is equivalent to edge-coloring the graph with 3 colors
    
    # Since each vertex has degree 3, this is essentially checking if the graph is 3-edge-colorable
    # which is equivalent to checking if the graph is cubic and class 1 (can be edge-colored with 3 colors)
    
    # We'll model this as a constraint satisfaction problem
    # For each edge, we need to assign a color 1, 2, or 3
    # For each vertex, all its incident edges must have different colors
    
    # This is equivalent to finding a proper edge coloring with 3 colors
    
    colors = [0] * m  # 0 means unassigned
    
    def is_valid_edge_coloring():
        # Check if current assignment is valid
        node_colors = defaultdict(dict)  # node -> {color -> edge_index}
        
        for i in range(m):
            if colors[i] == 0:
                continue
            u, v = edges[i]
            if colors[i] in node_colors[u] or colors[i] in node_colors[v]:
                return False
            node_colors[u][colors[i]] = i
            node_colors[v][colors[i]] = i
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        # Try colors 1, 2, 3
        used_colors = set()
        for color, _ in [(1, 'dummy'), (2, 'dummy'), (3, 'dummy')]:
            # Check if this color is already used by adjacent edges at u or v
            valid = True
            for edge_id in adj[u]:
                if edge_id < edge_idx and colors[edge_id] == color:
                    valid = False
                    break
            if not valid:
                continue
                
            for edge_id in adj[v]:
                if edge_id < edge_idx and colors[edge_id] == color:
                    valid = False
                    break
            if not valid:
                continue
                
            colors[edge_idx] = color
            if backtrack(edge_idx + 1):
                return True
            colors[edge_idx] = 0
            
        return False
    
    # More efficient approach: since the graph is 3-regular, we can try to find a proper edge coloring
    # We know that every 3-regular graph is either class 1 (3-edge-colorable) or class 2 (4-edge-colorable)
    # But we're asked specifically if it's 3-edge-colorable
    
    # Let's use a greedy approach with backtracking optimization
    def solve_coloring():
        # Sort edges by degree of endpoints for better performance
        edge_order = list(range(m))
        
        def dfs(idx):
            if idx == m:
                return True
                
            edge_id = edge_order[idx]
            u, v = edges[edge_id]
            
            # Find forbidden colors
            forbidden = set()
            for nbr_edge in adj[u]:
                if nbr_edge < edge_id and colors[nbr_edge] != 0:
                    forbidden.add(colors[nbr_edge])
                    
            for nbr_edge in adj[v]:
                if nbr_edge < edge_id and colors[nbr_edge] != 0:
                    forbidden.add(colors[nbr_edge])
            
            # Try available colors
            for color in [1, 2, 3]:
                if color not in forbidden:
                    colors[edge_id] = color
                    if dfs(idx + 1):
                        return True
                    colors[edge_id] = 0
                    
            return False
            
        return dfs(0)
    
    # Even more direct approach: try all combinations with constraint checking
    if solve_coloring():
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

solve()
import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store edges and build adjacency list
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Colors for edges (0=uncolored, 1,2,3 are phases)
    colors = [0] * m
    
    # For each vertex, we need to color its incident edges with 3 different colors
    # This is equivalent to edge coloring of a graph where each vertex has degree 3
    # We can model this as a constraint satisfaction problem
    
    # Try to 3-color the edges
    def dfs(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Find forbidden colors (colors already used by other edges at u or v)
        forbidden = set()
        for e_idx in adj[u]:
            if colors[e_idx] != 0:
                forbidden.add(colors[e_idx])
        for e_idx in adj[v]:
            if colors[e_idx] != 0:
                forbidden.add(colors[e_idx])
                
        # Try each available color
        for color in [1, 2, 3]:
            if color not in forbidden:
                colors[edge_idx] = color
                if dfs(edge_idx + 1):
                    return True
                colors[edge_idx] = 0
        
        return False
    
    # Since this is a cubic graph (each vertex has degree 3) and we have exactly 3 colors,
    # and each vertex needs exactly one edge of each color, this is equivalent to finding
    # a proper 3-edge-coloring of a cubic graph.
    
    # However, let's use a greedy approach with backtracking
    # But first, let's check if it's possible at all - a cubic graph is 3-edge-colorable iff it's bipartite
    
    # Actually, let's just try a direct backtracking approach but be smarter about it
    
    # Better approach: since each vertex has exactly 3 edges and we have 3 colors,
    # we just need to assign each edge a color such that edges at each vertex have different colors
    
    # Let's try a different approach - fix the order and do constraint checking
    
    # Use backtracking with constraint propagation
    def solve_edge(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Get forbidden colors at u and v
        forbidden_u = set()
        forbidden_v = set()
        
        for e_idx in adj[u]:
            if e_idx < edge_idx and colors[e_idx] != 0:
                forbidden_u.add(colors[e_idx])
                
        for e_idx in adj[v]:
            if e_idx < edge_idx and colors[e_idx] != 0:
                forbidden_v.add(colors[e_idx])
        
        # If either has all 3 colors forbidden, impossible
        if len(forbidden_u) >= 3 or len(forbidden_v) >= 3:
            return False
            
        # Union of forbidden colors
        forbidden = forbidden_u | forbidden_v
        
        # If all 3 colors are forbidden, impossible
        if len(forbidden) >= 3:
            return False
            
        # Try available colors
        for color in [1, 2, 3]:
            if color not in forbidden:
                colors[edge_idx] = color
                # Check consistency: at each node, no two colored edges should have same color
                valid = True
                for node in [u, v]:
                    colored_colors = set()
                    for e_idx in adj[node]:
                        if e_idx <= edge_idx and colors[e_idx] != 0:
                            if colors[e_idx] in colored_colors:
                                valid = False
                                break
                            colored_colors.add(colors[e_idx])
                    if not valid:
                        break
                        
                if valid and solve_edge(edge_idx + 1):
                    return True
                    
                colors[edge_idx] = 0
                
        return False
    
    # Even simpler: just do basic backtracking
    def backtrack(idx):
        if idx == m:
            return True
            
        u, v = edges[idx]
        
        # Determine forbidden colors
        used_u = set()
        used_v = set()
        
        for e_id in adj[u]:
            if e_id < idx:
                used_u.add(colors[e_id])
                
        for e_id in adj[v]:
            if e_id < idx:
                used_v.add(colors[e_id])
                
        forbidden = used_u | used_v
        
        for color in [1, 2, 3]:
            if color not in forbidden:
                colors[idx] = color
                # Additional check: make sure we don't create conflicts
                ok = True
                # Check if this creates a conflict at u
                u_colors = set()
                for e_id in adj[u]:
                    if e_id <= idx and colors[e_id] != 0:
                        if colors[e_id] in u_colors:
                            ok = False
                            break
                        u_colors.add(colors[e_id])
                        
                if ok:
                    # Check if this creates a conflict at v
                    v_colors = set()
                    for e_id in adj[v]:
                        if e_id <= idx and colors[e_id] != 0:
                            if colors[e_id] in v_colors:
                                ok = False
                                break
                            v_colors.add(colors[e_id])
                            
                if ok and backtrack(idx + 1):
                    return True
                    
                colors[idx] = 0
                
        return False
    
    if backtrack(0):
        print("YES")
        print(*colors)
    else:
        print("NO")

solve()
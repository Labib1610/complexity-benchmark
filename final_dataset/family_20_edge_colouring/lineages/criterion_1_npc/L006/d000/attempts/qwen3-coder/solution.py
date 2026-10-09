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
    
    # Color array for edges (0 means uncolored)
    color = [0] * m
    
    # Try to 3-color the edges such that edges incident to same vertex have different colors
    # This is equivalent to edge-coloring the graph with 3 colors
    
    # We'll use a greedy approach with backtracking if needed
    # But since each vertex has exactly 3 edges, and we have 3 colors,
    # we can try a systematic approach
    
    # For each vertex, we need to assign 3 different colors to its 3 edges
    # Let's build the constraint graph and try to color
    
    # Since every vertex has degree 3, and we have 3 colors, 
    # this is essentially asking for a proper edge 3-coloring
    
    def can_color(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Find colors used by other edges at u and v
        used_at_u = set()
        used_at_v = set()
        
        for neighbor, idx in adj[u]:
            if color[idx] != 0:
                used_at_u.add(color[idx])
                
        for neighbor, idx in adj[v]:
            if color[idx] != 0:
                used_at_v.add(color[idx])
        
        used_colors = used_at_u | used_at_v
        
        # Try each available color
        for c in [1, 2, 3]:
            if c not in used_colors:
                color[edge_idx] = c
                if can_color(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        
        return False
    
    # This greedy approach might not work for all cases
    # Let's try a more systematic approach
    
    # Since the graph is 3-regular, it's class 1 (edge chromatic number = 3) 
    # if and only if it doesn't contain a subgraph that is class 2
    
    # But let's implement a backtracking solution
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Get forbidden colors at u and v
        forbidden_u = set()
        forbidden_v = set()
        
        for neighbor, idx in adj[u]:
            if color[idx] != 0:
                forbidden_u.add(color[idx])
                
        for neighbor, idx in adj[v]:
            if color[idx] != 0:
                forbidden_v.add(color[idx])
        
        forbidden = forbidden_u | forbidden_v
        
        for c in [1, 2, 3]:
            if c not in forbidden:
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = 0
                
        return False
    
    # Optimization: start with vertices that have more colored edges
    # Let's just try the backtracking approach
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check if it's a cubic graph (each vertex has degree 3)
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Try to 3-color the edges (assign gases 1,2,3 to edges)
    # This is equivalent to edge-coloring a cubic graph with 3 colors
    edge_colors = [0] * m  # 0 means unassigned
    
    # For each vertex, we need to assign colors 1,2,3 to its 3 edges
    # We'll use a greedy approach with backtracking
    
    def is_valid(vertex, edge_idx, color):
        # Check if assigning 'color' to edge_idx is valid for this vertex
        for neighbor, idx in adj[vertex]:
            if edge_colors[idx] == color:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        u, v = edges[edge_idx]
        
        # Try colors 1, 2, 3
        for color in [1, 2, 3]:
            # Check if this color is valid for both endpoints
            valid = True
            for vertex in [u, v]:
                count = 0
                for neighbor, idx in adj[vertex]:
                    if idx < edge_idx and edge_colors[idx] == color:
                        count += 1
                    elif idx == edge_idx:
                        count += 1
                if count > 1:
                    valid = False
                    break
                    
            if valid:
                edge_colors[edge_idx] = color
                if backtrack(edge_idx + 1):
                    return True
                edge_colors[edge_idx] = 0
                
        return False
    
    # Better approach: since this is a 3-regular graph, we can try to find a proper edge coloring
    # A cubic graph is 3-edge-colorable if and only if it's bridgeless
    # But let's just try a direct approach
    
    def try_coloring():
        # Try all possible assignments using backtracking
        def dfs(pos):
            if pos == m:
                return True
                
            u, v = edges[pos]
            
            # Count how many times each color appears at u and v
            u_colors = [0, 0, 0, 0]  # index 0 unused
            v_colors = [0, 0, 0, 0]
            
            for neighbor, idx in adj[u]:
                if idx < pos:
                    u_colors[edge_colors[idx]] += 1
                    
            for neighbor, idx in adj[v]:
                if idx < pos:
                    v_colors[edge_colors[idx]] += 1
            
            # Try each color
            for color in [1, 2, 3]:
                if u_colors[color] == 0 and v_colors[color] == 0:
                    edge_colors[pos] = color
                    # Check if we can complete the coloring for u and v
                    u_count = sum(1 for c in u_colors[1:] if c > 0)
                    v_count = sum(1 for c in v_colors[1:] if c > 0)
                    
                    # After assigning color to current edge
                    u_colors[color] = 1
                    v_colors[color] = 1
                    new_u_count = sum(1 for c in u_colors[1:] if c > 0)
                    new_v_count = sum(1 for c in v_colors[1:] if c > 0)
                    
                    if new_u_count <= 3 and new_v_count <= 3:
                        if dfs(pos + 1):
                            return True
                            
            edge_colors[pos] = 0
            return False
            
        return dfs(0)
    
    # Even simpler: just do basic backtracking
    def simple_backtrack(pos):
        if pos == m:
            return True
            
        u, v = edges[pos]
        
        # Get current colors used at u and v
        u_used = set()
        v_used = set()
        
        for neighbor, idx in adj[u]:
            if idx < pos:
                u_used.add(edge_colors[idx])
                
        for neighbor, idx in adj[v]:
            if idx < pos:
                v_used.add(edge_colors[idx])
        
        # Try each color
        for color in [1, 2, 3]:
            if color not in u_used and color not in v_used:
                edge_colors[pos] = color
                # Check if degrees are still okay
                u_count = 1  # This edge
                v_count = 1
                for neighbor, idx in adj[u]:
                    if idx < pos and edge_colors[idx] == color:
                        u_count += 1
                for neighbor, idx in adj[v]:
                    if idx < pos and edge_colors[idx] == color:
                        v_count += 1
                        
                if u_count <= 1 and v_count <= 1:  # Each color appears at most once at each endpoint so far
                    if simple_backtrack(pos + 1):
                        return True
                        
        edge_colors[pos] = 0
        return False
    
    if simple_backtrack(0):
        print("YES")
        print(' '.join(map(str, edge_colors)))
    else:
        print("NO")

solve()
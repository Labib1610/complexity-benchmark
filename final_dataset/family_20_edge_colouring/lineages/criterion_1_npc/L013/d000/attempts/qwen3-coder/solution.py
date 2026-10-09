import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Store edges as a list
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Each node has exactly 3 edges
    # We need to color the edges with 3 colors such that edges incident to each node have different colors
    
    # This is essentially edge coloring of a cubic graph with 3 colors
    # Since each vertex has degree 3, and we have 3 colors, each vertex must have edges of all 3 colors
    
    # Try to 3-color the edges
    # We can use a greedy approach with backtracking
    
    # Let's represent the coloring
    color = [0] * m  # 0 means uncolored, 1, 2, 3 are the colors
    
    def is_valid(edge_idx, c):
        u, v = edges[edge_idx]
        # Check if any adjacent edge at u or v already has color c
        for e in adj[u]:
            if color[e] == c:
                return False
        for e in adj[v]:
            if color[e] == c:
                return False
        return True
    
    def dfs(edge_idx):
        if edge_idx == m:
            return True
            
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            if is_valid(edge_idx, c):
                color[edge_idx] = c
                if dfs(edge_idx + 1):
                    return True
                color[edge_idx] = 0
                
        return False
    
    # For large inputs, this might be too slow
    # Let's try a more systematic approach
    
    # Since this is a 3-regular graph and we want 3-edge-coloring,
    # we can try to find a perfect matching and work from there
    
    # However, let's just try the DFS with a better strategy
    
    # Sort edges by node degrees (try to fill constraints early)
    # Actually, let's just run the DFS but be smarter about it
    
    # Let's try a different approach - since every vertex has degree 3,
    # and we have exactly 3*n/2 edges, this is a cubic graph
    
    # For small graphs, let's try brute force with optimizations
    
    # But given the constraints, let's implement a proper algorithm
    
    # Peterson's theorem states that every cubic bridgeless graph has a 3-edge-coloring
    # But checking for bridges is complex
    
    # Let's just try a greedy DFS with good variable ordering
    
    # Order edges by highest degree vertices first
    def get_edge_priority(edge_idx):
        u, v = edges[edge_idx]
        return -(len(adj[u]) + len(adj[v]))
    
    # Try a simple greedy approach first
    def greedy_color():
        for i in range(m):
            u, v = edges[i]
            used_colors = set()
            for e in adj[u]:
                if color[e] != 0:
                    used_colors.add(color[e])
            for e in adj[v]:
                if color[e] != 0:
                    used_colors.add(color[e])
            
            # Find first available color
            for c in range(1, 4):
                if c not in used_colors:
                    color[i] = c
                    break
            else:
                return False
        return True
    
    # Try greedy first
    if greedy_color():
        print("YES")
        print(' '.join(map(str, color)))
        return
    
    # If greedy fails, try backtracking
    color = [0] * m
    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
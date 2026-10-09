import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Since m = 3*n/2 and each vertex has degree 3, this is a 3-regular graph
    # We need to color the edges with 3 colors such that:
    # 1. Each vertex has edges of 3 different colors (proper edge coloring)
    # 2. Each color appears exactly n/2 times (balanced)
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Try to find a valid edge coloring
    # This is essentially finding a proper 3-edge-coloring where each color appears n/2 times
    
    # Since each vertex has degree 3, and we have 3 colors, 
    # each vertex must have edges of all 3 different colors
    
    color = [0] * m  # 1, 2, 3
    
    # Build the line graph - each edge becomes a vertex
    # Two vertices in line graph are connected if their edges share a vertex in original graph
    line_adj = [[] for _ in range(m)]
    
    for u in range(1, n + 1):
        neighbors = adj[u]
        # All edges incident to u form a triangle in line graph
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                idx1 = neighbors[i][1]
                idx2 = neighbors[j][1]
                line_adj[idx1].append(idx2)
                line_adj[idx2].append(idx1)
    
    # Now we need to 3-color the line graph such that each color appears exactly n/2 times
    # This is a very constrained problem
    
    # Since the original graph is 3-regular with n vertices and 3n/2 edges,
    # and we want each color to appear n/2 times, this is like decomposing
    # the edge set into 3 perfect matchings (if n is even)
    
    # A 3-regular graph can be edge-colored with 3 colors iff it's class 1
    # For a 3-regular graph with n even, it's class 1 iff it has a 1-factorization
    
    # Let's try a greedy approach with backtracking
    def is_valid_color(edge_idx, c):
        u, v = edges[edge_idx]
        # Check all adjacent edges in line graph
        for neighbor_idx in line_adj[edge_idx]:
            if color[neighbor_idx] == c:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            # Check if each color appears exactly n/2 times
            count = [0, 0, 0, 0]  # index 0 unused
            for c in color[1:]:
                count[c] += 1
            return count[1] == n//2 and count[2] == n//2 and count[3] == n//2
        
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if is_valid_color(edge_idx, c):
                color[edge_idx] = c
                if backtrack(edge_idx + 1):
                    return True
                color[edge_idx] = 0
        return False
    
    # This might be too slow, let's think of a better approach
    
    # Since this is a 3-regular graph, we can try to find a proper edge coloring
    # and then check if we can balance it
    
    # A different approach: since we know the structure, let's try to build it directly
    
    # For 3-regular graphs, a valid edge coloring exists (by Vizing's theorem)
    # But we also need the balancing constraint
    
    # Let's model this as an exact cover problem or use a more systematic approach
    
    # Try a different strategy: since each vertex must have 3 edges of different colors,
    # we can try to build a valid coloring
    
    def try_coloring():
        # Try all possible colorings with the constraint
        color_count = [0, 0, 0, 0]  # index 0 unused
        
        def dfs(edge_idx):
            if edge_idx == m:
                return color_count[1] == n//2 and color_count[2] == n//2 and color_count[3] == n//2
            
            u, v = edges[edge_idx]
            # Get colors of already colored edges incident to u and v
            used_colors_u = set()
            used_colors_v = set()
            
            for neighbor, idx in adj[u]:
                if color[idx] != 0:
                    used_colors_u.add(color[idx])
                    
            for neighbor, idx in adj[v]:
                if color[idx] != 0:
                    used_colors_v.add(color[idx])
            
            # Available colors for this edge
            used_colors = used_colors_u | used_colors_v
            for c in range(1, 4):
                if c not in used_colors and color_count[c] < n//2:
                    color[edge_idx] = c
                    color_count[c] += 1
                    if dfs(edge_idx + 1):
                        return True
                    color[edge_idx] = 0
                    color_count[c] -= 1
            
            return False
        
        return dfs(0)
    
    # Even simpler: try a greedy approach first
    def greedy_coloring():
        color_count = [0, 0, 0, 0]
        
        for edge_idx in range(m):
            u, v = edges[edge_idx]
            # Get forbidden colors
            forbidden = set()
            for neighbor, idx in adj[u]:
                if color[idx] != 0:
                    forbidden.add(color[idx])
            for neighbor, idx in adj[v]:
                if color[idx] != 0:
                    forbidden.add(color[idx])
            
            # Try to assign a color that's not forbidden and not over limit
            assigned = False
            for c in range(1, 4):
                if c not in forbidden and color_count[c] < n//2:
                    color[edge_idx] = c
                    color_count[c] += 1
                    assigned = True
                    break
            
            if not assigned:
                return False
        
        # Check if we used exactly n/2 of each color
        return color_count[1] == n//2 and color_count[2] == n//2 and color_count[3] == n//2
    
    # Try greedy first
    if greedy_coloring():
        print("YES")
        print(' '.join(map(str, color[1:])))
        return
    
    # If greedy fails, try backtracking
    color = [0] * m
    if try_coloring():
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
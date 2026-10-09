import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Since m = 3n/2 and each node has the same degree
    # Each node has degree 3
    degree = 3
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to color the edges with 3 colors such that
    # no two edges incident to the same vertex have the same color
    # This is edge coloring for a 3-regular graph
    
    # We can use the fact that a 3-regular graph can be edge-colored
    # with 3 colors if and only if it doesn't contain a bridge
    # But since we're asked to always find a solution when possible,
    # and given the constraints, we'll try a greedy approach
    
    # For each vertex, we need to assign different colors to its 3 edges
    # Let's try a backtracking approach or greedy
    
    color = [0] * m  # 0 means uncolored, 1, 2, 3 are the colors
    
    # Greedy approach: for each edge, assign the smallest color not used by its endpoints
    for i in range(m):
        u, v = edges[i]
        used_colors = set()
        
        # Check colors used by edges adjacent to u
        for edge_idx in adj[u]:
            if color[edge_idx] != 0:
                used_colors.add(color[edge_idx])
                
        # Check colors used by edges adjacent to v
        for edge_idx in adj[v]:
            if color[edge_idx] != 0:
                used_colors.add(color[edge_idx])
        
        # Assign the smallest available color
        for c in range(1, 4):
            if c not in used_colors:
                color[i] = c
                break
        else:
            # No color available - this shouldn't happen for valid inputs
            print("NO")
            return
    
    # Verify the solution
    valid = True
    for u in range(1, n+1):
        colors_at_u = set()
        for edge_idx in adj[u]:
            colors_at_u.add(color[edge_idx])
        if len(colors_at_u) != 3 or 0 in colors_at_u:
            valid = False
            break
    
    if valid:
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
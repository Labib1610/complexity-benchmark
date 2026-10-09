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
    # We need to color edges with 3 colors such that edges incident to same node have different colors
    
    # This is equivalent to edge coloring of a 3-regular graph with 3 colors
    # Since each vertex has degree 3, and we have 3 colors, this is possible iff 
    # the graph is 3-edge-colorable
    
    # For a 3-regular graph, it's 3-edge-colorable iff it's bipartite OR has a specific structure
    # But actually, any 3-regular graph can be edge-colored with 3 colors (this is not true!)
    # Wait, that's not correct. Not all 3-regular graphs are 3-edge-colorable.
    # However, if it's 3-edge-colorable, we can try to construct such a coloring.
    
    # Let's try a greedy approach:
    # For each edge, assign it the smallest color not used by its adjacent edges at either endpoint
    
    color = [0] * m  # 0 means uncolored
    
    for i in range(m):
        u, v = edges[i]
        # Find colors used by edges adjacent to u or v
        used_colors = set()
        for edge_idx in adj[u]:
            if color[edge_idx] != 0:
                used_colors.add(color[edge_idx])
        for edge_idx in adj[v]:
            if color[edge_idx] != 0:
                used_colors.add(color[edge_idx])
        
        # Assign the smallest available color (1, 2, or 3)
        for c in range(1, 4):
            if c not in used_colors:
                color[i] = c
                break
        else:
            # No color available - impossible
            print("NO")
            return
    
    # Check if all edges were colored
    if 0 in color:
        print("NO")
        return
        
    # Verify the solution
    for node in range(1, n+1):
        colors_at_node = set()
        for edge_idx in adj[node]:
            colors_at_node.add(color[edge_idx])
        if len(colors_at_node) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    return n, m, edges, adj

def solve():
    n, m, edges, adj = read_input()
    
    # This is essentially a graph coloring problem where each vertex (junction) 
    # has exactly 3 edges and we need to color the edges with 3 colors such that
    # all edges incident to a vertex have different colors.
    
    # This is equivalent to edge-coloring a 3-regular graph with 3 colors.
    # For a 3-regular graph, this is possible if and only if the graph is class 1,
    # meaning it can be edge-colored with 3 colors (since max degree is 3).
    
    # However, since every vertex has exactly degree 3, and we have exactly 3*n/2 edges,
    # this is a 3-regular graph. Not all 3-regular graphs can be 3-edge-colored.
    # But the problem asks us to find such a coloring or determine it's impossible.
    
    # We'll try to construct such a coloring using a greedy approach or backtracking.
    # But given the constraints, let's think of this differently.
    
    # Actually, this is asking whether we can properly edge-color a 3-regular graph with 3 colors.
    # By K\"onig's theorem, a graph is class 1 if and only if it has a proper edge coloring with
    # Δ colors, where Δ is the maximum degree. Since our graph is 3-regular, Δ=3.
    # However, not all 3-regular graphs are class 1. For example, the Petersen graph is not.
    
    # But let's try a constructive approach. In a 3-regular graph, if we can find a perfect matching,
    # we can remove it and get a 2-regular graph (a collection of cycles), which is clearly 2-edge-colorable.
    # So the graph would be 3-edge-colorable.
    
    # Let's implement a backtracking solution with bitmasks for efficiency.
    
    # For small graphs, we can use backtracking.
    # But given n up to 2000, that might be too slow.
    
    # Let's think of properties:
    # - Every vertex has degree 3
    # - Total number of edges is 3*n/2
    # - Need to assign colors {1,2,3} to edges such that edges at each vertex have distinct colors
    
    # This is equivalent to finding a proper edge coloring with 3 colors.
    
    # Let's model this as a SAT problem or use a heuristic.
    # But for implementation simplicity, let's try a greedy algorithm with backtracking optimization.
    
    # Actually, there's a known result: Every 3-regular bridgeless graph is 3-edge-colorable.
    # But our graph might have bridges.
    
    # Let's just implement a backtracking solution optimized with pruning.
    
    color = [0] * m  # color[i] represents the color of edge i (1, 2, or 3)
    
    # For each vertex, keep track of which colors are used by its incident edges
    vertex_colors = [0] * (n + 1)  # bitmask for each vertex
    
    def is_valid_edge_color(edge_idx, c):
        u, v = edges[edge_idx]
        # Check if color c is already used at vertex u or v
        mask = 1 << (c - 1)
        return (vertex_colors[u] & mask) == 0 and (vertex_colors[v] & mask) == 0
    
    def assign_color(edge_idx, c):
        u, v = edges[edge_idx]
        mask = 1 << (c - 1)
        vertex_colors[u] |= mask
        vertex_colors[v] |= mask
        color[edge_idx] = c
    
    def unassign_color(edge_idx, c):
        u, v = edges[edge_idx]
        mask = 1 << (c - 1)
        vertex_colors[u] &= ~mask
        vertex_colors[v] &= ~mask
        color[edge_idx] = 0
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        # Try colors 1, 2, 3 in order
        for c in range(1, 4):
            if is_valid_edge_color(edge_idx, c):
                assign_color(edge_idx, c)
                if backtrack(edge_idx + 1):
                    return True
                unassign_color(edge_idx, c)
        
        return False
    
    # Start backtracking from edge 0
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
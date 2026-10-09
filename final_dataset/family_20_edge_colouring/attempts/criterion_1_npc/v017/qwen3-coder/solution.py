import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to 3-color the line graph of the original graph
    # Each edge becomes a node, and two nodes are connected if they share a vertex
    # This is equivalent to assigning windows to edges such that edges incident to 
    # the same vertex have different windows
    
    # This is essentially a graph coloring problem where each vertex in the original
    # graph has exactly 3 edges, and we want to color the edges with 3 colors such that
    # all edges incident to each vertex have different colors
    
    # This is equivalent to finding a proper edge coloring of a cubic graph with 3 colors
    # According to König's theorem, every bipartite cubic graph is 3-edge-colorable
    # But not all cubic graphs are 3-edge-colorable. However, the problem guarantees 
    # that a solution exists if we can find one.
    
    # Let's model this as a SAT problem or use a greedy approach.
    # Since each vertex has degree 3, and we have 3 colors, each vertex must use all 3 colors.
    
    # We can try a BFS-based coloring approach
    
    # Initialize color assignment array (-1 means unassigned)
    color = [-1] * m
    
    # For each vertex, track which colors are used by its edges
    # Initially, no colors are used
    
    # Use a greedy algorithm: process edges in some order, and for each edge,
    # assign it a color that is not used by its adjacent edges.
    # But since we're dealing with vertices having exactly 3 edges, and 3 colors,
    # we need to be more careful.
    
    # Better approach: since the graph is cubic (every vertex has degree 3) and we have 3 colors,
    # we can try to find a proper edge coloring.
    
    # Let's build the adjacency list for edges (line graph)
    edge_adj = [[] for _ in range(m)]
    for v in range(1, n+1):
        edge_indices = adj[v]
        # All edges incident to vertex v are connected in the line graph
        for i in range(len(edge_indices)):
            for j in range(i+1, len(edge_indices)):
                edge_adj[edge_indices[i]].append(edge_indices[j])
                edge_adj[edge_indices[j]].append(edge_indices[i])
    
    # Now we need to color the line graph with 3 colors such that no two adjacent nodes have the same color
    # This is a graph 3-coloring problem
    
    # Use backtracking with constraint propagation
    def is_safe(edge_idx, c, color_assignment):
        for neighbor in edge_adj[edge_idx]:
            if color_assignment[neighbor] == c:
                return False
        return True
    
    def graph_coloring(edge_idx, color_assignment):
        if edge_idx == m:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(edge_idx, c, color_assignment):
                color_assignment[edge_idx] = c
                if graph_coloring(edge_idx + 1, color_assignment):
                    return True
                color_assignment[edge_idx] = -1
        return False
    
    # This might be too slow for large inputs. Let's try a different approach.
    
    # Since every vertex has degree 3, and we have 3 colors, we can think of this differently.
    # For each vertex, its 3 edges must have 3 different colors.
    # This is like finding a Latin square for each vertex's local neighborhood.
    
    # Let's try a constructive approach based on the structure of cubic graphs.
    # Actually, let's just implement the backtracking with optimizations.
    
    # Optimization: sort edges by the number of already colored neighbors (descending)
    # This is a common heuristic in constraint satisfaction problems.
    
    color = [-1] * m
    
    def count_colored_neighbors(edge_idx):
        count = 0
        for neighbor in edge_adj[edge_idx]:
            if color[neighbor] != -1:
                count += 1
        return count
    
    def solve_coloring(edges_order):
        stack = [(edges_order, color[:])]
        
        while stack:
            order, current_color = stack.pop()
            
            # Find next uncolored edge
            next_edge = -1
            for edge_idx in order:
                if current_color[edge_idx] == -1:
                    next_edge = edge_idx
                    break
                    
            if next_edge == -1:
                return current_color
                
            # Try colors 1, 2, 3
            for c in [1, 2, 3]:
                if is_safe(next_edge, c, current_color):
                    new_color = current_color[:]
                    new_color[next_edge] = c
                    stack.append((order, new_color))
                    
        return None
    
    # Sort edges by index for consistent processing
    edges_order = list(range(m))
    
    # Simple recursive backtracking with early pruning
    def backtrack(pos):
        if pos == m:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(pos, c, color):
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = -1
        return False
    
    # For performance, let's check if the graph is small enough for brute force
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
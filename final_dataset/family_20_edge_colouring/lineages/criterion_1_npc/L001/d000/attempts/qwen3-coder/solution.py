import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Store edges in order
    edges = []
    # Build adjacency list
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Each node has exactly 3 edges
    # We need to assign phases 1,2,3 to edges such that
    # each node has exactly one edge of each phase
    
    # This is equivalent to edge coloring with 3 colors
    # where each vertex is incident to exactly 3 edges of different colors
    
    # Since each vertex has degree 3 and we have 3 colors,
    # this is possible if and only if the graph can be properly edge-colored
    
    # For a 3-regular graph, it's edge-colorable with 3 colors iff
    # it's a line graph of a cubic graph, but there's a simpler approach:
    # Try to find a valid assignment using BFS/DFS
    
    # Let's try a greedy approach with backtracking concept
    # But since n <= 2000, we need an efficient method
    
    # Key insight: This is equivalent to finding a proper edge 3-coloring
    # For 3-regular graphs, this exists iff the graph is class 1
    # But checking this is complex. Let's try a constructive approach.
    
    # Try to build a valid assignment:
    # For each vertex, its 3 edges must have colors 1,2,3
    # So we can try to assign colors systematically
    
    # One approach: Try to find a perfect matching, remove it,
    # find another, remove it, the remaining is the third
    # But finding a perfect matching in a 3-regular graph
    # where n is even is guaranteed to exist (Petersen's theorem variant)
    
    # Let's implement a BFS-based approach to try to color edges
    
    color = [0] * m  # 0 means uncolored, 1,2,3 are colors
    
    # For each node, track which colors are used on its edges
    node_colors = defaultdict(set)
    
    # Try greedy coloring
    def can_color(edge_idx, c):
        u, v = edges[edge_idx]
        return c not in node_colors[u] and c not in node_colors[v]
    
    def assign_color(edge_idx, c):
        u, v = edges[edge_idx]
        color[edge_idx] = c
        node_colors[u].add(c)
        node_colors[v].add(c)
    
    def unassign_color(edge_idx):
        u, v = edges[edge_idx]
        c = color[edge_idx]
        if c != 0:
            node_colors[u].discard(c)
            node_colors[v].discard(c)
            color[edge_idx] = 0
    
    # Try all possible colorings with backtracking
    # But this might be too slow. Let's think of a better way.
    
    # Since each vertex has exactly degree 3, and we have 3 colors,
    # we can model this as: for each vertex, assign a permutation of {1,2,3}
    # to its three edges.
    
    # This is equivalent to finding a proper edge coloring.
    # For 3-regular graphs, if it's connected and has even number of vertices,
    # it can be edge-colored with 3 colors.
    
    # Let's try a more systematic approach:
    # Build the line graph and try to 3-color it
    # But that's complex. Let's try a direct approach.
    
    # Try a greedy algorithm with a specific order
    # Process edges and for each, pick the first available color
    
    # Actually, let's think of the structure:
    # This is a 3-regular graph on n vertices (n even)
    # It's known that such graphs can be decomposed into 3 perfect matchings
    # iff they don't contain a bridge (but all our graphs are likely to be OK)
    
    # Let's try to implement a matching-based decomposition
    
    def find_perfect_matching():
        # Try to find a perfect matching using a greedy approach
        matched = [False] * (n + 1)
        matching = []
        edge_used = [False] * m
        
        # Create adjacency list for current available edges
        adj_avail = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            if not edge_used[i]:
                adj_avail[u].append((v, i))
                adj_avail[v].append((u, i))
        
        # Greedy matching
        for u in range(1, n + 1):
            if matched[u]:
                continue
            for v, idx in adj_avail[u]:
                if not matched[v]:
                    matching.append(idx)
                    matched[u] = matched[v] = True
                    edge_used[idx] = True
                    break
        
        if len(matching) == n // 2:
            return matching
        else:
            return None
    
    # Try to decompose into 3 perfect matchings
    original_color = color[:]
    original_node_colors = {k: v.copy() for k, v in node_colors.items()}
    
    matchings = []
    temp_edges_used = [False] * m
    
    # First matching
    matched = [False] * (n + 1)
    matching1 = []
    for i, (u, v) in enumerate(edges):
        if not matched[u] and not matched[v]:
            matching1.append(i)
            matched[u] = matched[v] = True
    
    if len(matching1) != n // 2:
        print("NO")
        return
    
    matchings.append(matching1)
    
    # Second matching on remaining edges
    matched = [False] * (n + 1)
    matching2 = []
    for i, (u, v) in enumerate(edges):
        if i in matching1:
            continue
        if not matched[u] and not matched[v]:
            matching2.append(i)
            matched[u] = matched[v] = True
    
    if len(matching2) != n // 2:
        print("NO")
        return
        
    matchings.append(matching2)
    
    # Third matching is the remaining edges
    matching3 = []
    used = set(matching1) | set(matching2)
    for i in range(m):
        if i not in used:
            matching3.append(i)
    
    if len(matching3) != n // 2:
        print("NO")
        return
        
    matchings.append(matching3)
    
    # Assign colors
    for phase, matching in enumerate(matchings, 1):
        for edge_idx in matching:
            color[edge_idx] = phase
    
    # Verify the solution
    node_edge_colors = defaultdict(set)
    for i, (u, v) in enumerate(edges):
        c = color[i]
        node_edge_colors[u].add(c)
        node_edge_colors[v].add(c)
    
    for node in range(1, n + 1):
        if len(node_edge_colors[node]) != 3 or set(node_edge_colors[node]) != {1, 2, 3}:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
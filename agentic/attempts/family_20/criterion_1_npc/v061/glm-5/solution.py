import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    deg = [len(adj[i]) for i in range(n)]
    k = deg[0]
    
    # Check if all degrees are equal to k
    for i in range(n):
        if deg[i] != k:
            print("NO")
            return
    
    # Check if m = n * k / 2
    if m * 2 != n * k:
        print("NO")
        return
    
    # Check if k is odd
    if k % 2 == 0:
        print("NO")
        return
    
    # k is odd, so a proper edge coloring with k colors exists
    # We use the standard algorithm for edge coloring regular graphs of odd degree
    
    # Build adjacency list with edge indices
    # adj[u] = list of (v, edge_index)
    
    # We'll use a greedy approach with backtracking via the "rotation" method
    # For each vertex, we maintain the colors of incident edges
    
    # edge_colors[edge_index] = color (1 to k)
    edge_colors = [0] * m
    
    # For each vertex, track which colors are used and which edge has which color
    # vertex_color[u][c] = edge_index of edge incident to u with color c (or -1 if none)
    vertex_color = [[-1] * (k + 1) for _ in range(n)]
    
    def find_free_color(u):
        for c in range(1, k + 1):
            if vertex_color[u][c] == -1:
                return c
        return -1
    
    def find_missing_color(u):
        for c in range(1, k + 1):
            if vertex_color[u][c] == -1:
                return c
        return -1
    
    def set_color(u, v, e, c):
        edge_colors[e] = c
        vertex_color[u][c] = e
        vertex_color[v][c] = e
    
    def clear_color(u, v, e, c):
        edge_colors[e] = 0
        vertex_color[u][c] = -1
        vertex_color[v][c] = -1
    
    def get_other_vertex(e, u):
        u1, v1 = edges[e]
        return v1 if u == u1 else u1
    
    def recolor_path(u, c1, c2):
        # Follow the alternating path starting from u with colors c1, c2
        # and swap c1 <-> c2
        while True:
            e1 = vertex_color[u][c1]
            if e1 == -1:
                break
            v = get_other_vertex(e1, u)
            # Clear c1 from this edge
            clear_color(u, v, e1, c1)
            # Set c2 on this edge
            set_color(u, v, e1, c2)
            # Move to the other vertex and swap colors
            u = v
            c1, c2 = c2, c1
    
    # Process edges one by one
    for e, (u, v) in enumerate(edges):
        if edge_colors[e] != 0:
            continue
        
        c1 = find_free_color(u)
        c2 = find_free_color(v)
        
        if c1 == -1 and c2 == -1:
            # Both u and v have all colors used
            # This shouldn't happen if we process correctly, but handle it
            # Find missing colors (should be the same since k is odd)
            c1 = find_missing_color(u)
            c2 = find_missing_color(v)
            # They should be different
            # Recolor path from u with c1 and c2
            recolor_path(u, c1, c2)
            # Now c1 should be free at u
            c1 = find_free_color(u)
        
        if c1 != -1 and c2 == -1:
            # u has free color c1, v doesn't
            # Find what color v is missing
            c2 = find_missing_color(v)
            if c2 == c1:
                # Recolor path from u with c1 and some other color
                for c_other in range(1, k + 1):
                    if c_other != c1:
                        recolor_path(u, c1, c_other)
                        c1 = find_free_color(u)
                        break
            c2 = find_free_color(v)
        
        if c1 == -1 and c2 != -1:
            # v has free color c2, u doesn't
            c1 = find_missing_color(u)
            if c1 == c2:
                for c_other in range(1, k + 1):
                    if c_other != c2:
                        recolor_path(v, c2, c_other)
                        c2 = find_free_color(v)
                        break
            c1 = find_free_color(u)
        
        if c1 != -1 and c2 != -1:
            if c1 == c2:
                set_color(u, v, e, c1)
            else:
                # Both have free colors, but different
                # Recolor path from u with c1 and c2
                recolor_path(u, c1, c2)
                # Now c1 should be free at u
                c1 = find_free_color(u)
                set_color(u, v, e, c1)
    
    print("YES")
    print(' '.join(map(str, edge_colors)))

solve()
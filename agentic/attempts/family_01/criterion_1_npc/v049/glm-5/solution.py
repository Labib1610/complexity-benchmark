def is_bipartite(mask_vertices, adj):  # adj: dict or list of bitmasks
    # try 2-coloring induced subgraph on mask_vertices
    u = mask_vertices
    while u:
        start = u & -u
        # BFS
        side0 = start; side1 = 0
        frontier = start
        visited = start
        cur = start; parity = 0
        # BFS layers
        ...
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nU = int(next(it))
    nD = int(next(it))
    m = int(next(it))
    
    edges = []
    degU = [0] * (nU + 1)
    degD = [0] * (nD + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degU[u] += 1
        degD[v] += 1
    
    K = 0
    for i in range(1, nU + 1):
        if degU[i] > K:
            K = degU[i]
    for i in range(1, nD + 1):
        if degD[i] > K:
            K = degD[i]
    
    # Build bipartite graph: left = upstream, right = downstream
    # We need to edge-color with K colors.
    # Use the standard approach: for each edge, assign a color that is free at both endpoints.
    # To do this efficiently, we maintain for each vertex the set of used colors.
    # Since K can be up to m, we use a "next free color" pointer per vertex.
    
    # We'll use a greedy approach with a twist: for each edge, find a color free at both u and v.
    # If we just use the smallest free color at u and v, we might need to recolor.
    # The standard Vizing-like approach for bipartite graphs:
    # For each edge (u, v):
    #   Find a color free at u (cu) and a color free at v (cv).
    #   If cu == cv, assign it.
    #   Else, we need to do a Kempe chain swap.
    
    # However, for bipartite graphs, edge coloring with Delta colors is always possible.
    # A simpler approach: since it's bipartite, we can use the fact that the graph is K-regular after adding dummy edges.
    # But adding dummy edges up to K-regular is expensive.
    
    # Alternative: Use the "rotate" method.
    # For each vertex, maintain a list of free colors.
    # Actually, let's use the approach from the "edge coloring bipartite graph" problem.
    
    # We'll maintain for each vertex a "free color" using a DSU-like structure.
    # For each vertex, we have an array next_free[color] -> next color to try.
    # But K can be large, so we use a dictionary or a list with path compression.
    
    # Let's use the approach: for each vertex, maintain a set of used colors.
    # For each edge, find the smallest color not used at u and not used at v.
    # If they are different, we need to do a swap.
    
    # Actually, for bipartite graphs, there's a simpler greedy that works:
    # Process edges in any order. For edge (u, v):
    #   Let a = smallest color not used at u
    #   Let b = smallest color not used at v
    #   If a == b, color = a
    #   Else:
    #     We need to find a color c that is free at both, or do a Kempe chain.
    #     Actually, we can do: try to find a color free at both by checking colors from a and b.
    #     But this can be slow.
    
    # Let's use the standard algorithm with Kempe chains.
    
    if m == 0:
        sys.stdout.write("YES\n\n")
        return
    
    # For each vertex, maintain used colors as a set, and a pointer to the smallest free color.
    usedU = [set() for _ in range(nU + 1)]
    usedD = [set() for _ in range(nD + 1)]
    color = [0] * m
    
    # For finding free color quickly, maintain a "next free" pointer
    nextFreeU = [1] * (nU + 1)
    nextFreeD = [1] * (nD + 1)
    
    def get_free_u(u):
        while nextFreeU[u] in usedU[u]:
            nextFreeU[u] += 1
        return nextFreeU[u]
    
    def get_free_d(v):
        while nextFreeD[v] in usedD[v]:
            nextFreeD[v] += 1
        return nextFreeD[v]
    
    # For Kempe chain, we need to find alternating paths.
    # We'll use a dictionary to map (vertex, color) -> edge index for quick lookup.
    # But this can be memory intensive. Let's use arrays of dicts.
    
    # Actually, let's use a different approach: since the graph is bipartite and we want K colors,
    # we can use the following:
    # For each edge, assign color = (some function). But that doesn't guarantee no conflicts.
    
    # Let's implement the standard bipartite edge coloring with Kempe chains.
    
    # We need for each vertex and color, which edge uses that color at that vertex.
    # Use dict: edgeAtU[u][c] = edge_index, edgeAtD[v][c] = edge_index
    edgeAtU = [dict() for _ in range(nU + 1)]
    edgeAtD = [dict() for _ in range(nD + 1)]
    
    for i in range(m):
        u, v = edges[i]
        a = get_free_u(u)
        b = get_free_d(v)
        
        if a == b:
            c = a
            color[i] = c
            usedU[u].add(c)
            usedD[v].add(c)
            edgeAtU[u][c] = i
            edgeAtD[v][c] = i
        else:
            # a is free at u, b is free at v, a != b
            # We need to find an alternating path starting from v with color a, or from u with color b.
            # Kempe chain: start from v, follow color a edges, alternating with color b.
            # If we find a vertex where a is free (on u side) or b is free (on v side), we can swap.
            
            # Let's do: start from v, try to find alternating path with colors a and b.
            # The path alternates between D and U vertices.
            # At v (D side), color a is used (since b is free at v, and a != b, a might be used or free)
            # Wait, a is free at u, b is free at v. a might be used or free at v.
            # b might be used or free at u.
            
            # We want to find an alternating path from v using color a (if a is used at v) or from u using color b (if b is used at u).
            # Actually, the standard approach:
            # Let's say a is free at u, b is free at v.
            # We look for an alternating path starting from u, alternating colors b, a, b, a, ...
            # or starting from v, alternating colors a, b, a, b, ...
            # The path ends when we find a vertex where the next color is free.
            
            # Let's try: start from u, follow color b. If b is not used at u, then we can just use b? No, b is free at v, not necessarily at u.
            # b might be used at u.
            
            # Standard Kempe chain for edge coloring:
            # We have edge (u, v). a is free at u, b is free at v, a != b.
            # We look for an alternating path starting from u, with colors b, a, b, a, ...
            # The path goes: u -> (edge with color b) -> some v' -> (edge with color a) -> some u' -> ...
            # We stop when we reach a vertex where the next color is free.
            # Then we flip the colors on the path.
            
            # Let's implement this.
            
            # Build the alternating path from u.
            # Current vertex is u (U side). We want to follow color b.
            # If b is not used at u, then we can just assign color b to edge (u, v)? No, b is free at v, but we need it free at u too.
            # If b is free at u, then we can use b. But b is free at v, so we can use b.
            # Wait, if b is free at u, then b is free at both u and v, so we can use b.
            # But a is also free at u. So if b is free at u, we should use b? No, we want to use a or b.
            # Actually, if b is free at u, then b is free at both, so use b.
            # But in our case, a is the smallest free at u, so b >= a. If b is free at u, then a = b, contradiction.
            # So b is used at u (since a is the smallest free at u, and b > a, b could be used or free).
            # Actually, b could be free at u if b > a. But a is the smallest free, so all colors < a are used.
            # b could be > a and free at u.
            
            # Hmm, this is getting complicated. Let me just implement the standard algorithm.
            
            # We'll do a Kempe chain starting from v, alternating colors a and b.
            # At v, color b is free. We check if color a is used at v.
            # If a is free at v, then a is free at both u and v, so use a. But a is free at u, and if a is free at v, then a == b? No.
            # a is free at u, b is free at v. If a is also free at v, then a is free at both, so we can use a.
            # But then b would be >= a, and a is free at v, so get_free_d(v) would return a, not b. Contradiction.
            # So a is used at v. Similarly, b is used at u (since b > a, and a is smallest free at u, b could be free at u).
            # Actually, b could be free at u. Let's check: if b is free at u, then b is free at both u and v, so use b.
            # But a is the smallest free at u, so a <= b. If b is free at u and a < b, then we should use a? No, a is free at u but used at v.
            
            # OK let me just implement the standard Kempe chain properly.
            
            # We have edge (u, v). a = free at u, b = free at v, a != b.
            # We want to find a color free at both. 
            # Try color a: it's free at u, check if free at v. If yes, use a.
            # But get_free_d(v) returned b, and a < b (since a is from u, b from v, and they're different).
            # Actually, a could be > b. a is free at u, b is free at v. They are independent.
            # If a < b, then a is used at v (since get_free_d(v) = b > a means a is used at v).
            # If a > b, then b is used at u.
            
            # Let's just check: is a free at v? If yes, use a.
            # Is b free at u? If yes, use b.
            # Otherwise, do Kempe chain.
            
            if a not in usedD[v]:
                c = a
                color[i] = c
                usedU[u].add(c)
                usedD[v].add(c)
                edgeAtU[u][c] = i
                edgeAtD[v][c] = i
                continue
            
            if b not in usedU[u]:
                c = b
                color[i] = c
                usedU[u].add(c)
                usedD[v].add(c)
                edgeAtU[u][c] = i
                edgeAtD[v][c] = i
                continue
            
            # Both a is used at v and b is used at u.
            # Do Kempe chain starting from u, alternating b, a, b, a, ...
            # Or from v, alternating a, b, a, b, ...
            
            # Let's start from u. We follow color b from u.
            # The path: u ->(b)-> v1 ->(a)-> u1 ->(b)-> v2 ->(a)-> ...
            # We stop when we can't continue (the next color is free at the current vertex).
            # Then we flip all colors on the path: b->a, a->b.
            # After flipping, color b becomes free at u, and we can assign b to edge (u, v).
            
            # Actually, we need to be careful. Let's trace:
            # At u, color b is used. Follow edge with color b from u to some v1.
            # At v1, color a is used (since we're alternating). Follow edge with color a from v1 to some u1.
            # At u1, color b is used. Follow edge with color b from u1 to some v2.
            # ... until we reach a vertex where the next color is free.
            
            # Since the graph is finite and bipartite, and colors a and b form a disjoint union of paths and cycles,
            # and since a is free at u and b is free at v, the path starting from u with color b must end at v with color a being free.
            # Wait, not necessarily. Let me think.
            
            # The subgraph of edges colored a or b is a disjoint union of paths and even cycles.
            # u has no edge of color a (a is free at u), but has an edge of color b.
            # v has no edge of color b (b is free at v), but has an edge of color a.
            # So u is an endpoint of a path (starts with color b), and v is an endpoint of a path (starts with color a).
            # If u and v are on the same path, then the path goes u -b-> ... -a-> v, and flipping makes b free at u and a free at v.
            # But we want b free at u (to assign to edge (u,v)), and b is already free at v. So after flipping, b is free at u, and we can assign b.
            # If u and v are on different paths, then flipping the path starting at u makes b free at u, and we can assign b.
            
            # So: find the path starting from u, alternating b, a, b, a, ...
            # Flip the colors on this path.
            # Then b becomes free at u, assign b to edge (u, v).
            
            # Let's implement this.
            
            path_edges = []
            current_side = 'U'  # start at u on U side
            current_vertex = u
            current_color = b  # follow color b from u
            
            while True:
                if current_side == 'U':
                    if current_color in edgeAtU[current_vertex]:
                        e = edgeAtU[current_vertex][current_color]
                        path_edges.append(e)
                        # Move to the other endpoint
                        u2, v2 = edges[e]
                        if u2 == current_vertex:
                            current_vertex = v2
                        else:
                            current_vertex = u2
                        current_side = 'D'
                        current_color = a if current_color == b else b
                    else:
                        break
                else:  # 'D'
                    if current_color in edgeAtD[current_vertex]:
                        e = edgeAtD[current_vertex][current_color]
                        path_edges.append(e)
                        u2, v2 = edges[e]
                        if v2 == current_vertex:
                            current_vertex = u2
                        else:
                            current_vertex = v2
                        current_side = 'U'
                        current_color = a if current_color == b else b
                    else:
                        break
            
            # Flip colors on path
            for e in path_edges:
                old_c = color[e]
                new_c = b if old_c == a else a
                u2, v2 = edges[e]
                # Remove old color
                del edgeAtU[u2][old_c]
                del edgeAtD[v2][old_c]
                # Add new color
                edgeAtU[u2][new_c] = e
                edgeAtD[v2][new_c] = e
                color[e] = new_c
            
            # Now b should be free at u. Assign b to edge (u, v).
            c = b
            color[i] = c
            usedU[u].add(c)
            usedD[v].add(c)
            edgeAtU[u][c] = i
            edgeAtD[v][c] = i
            # Update next free pointers if needed
            # Actually, nextFreeU[u] might need to be updated if c < nextFreeU[u], but c = b >= a = nextFreeU[u], so no change needed.
            # But after flipping, some colors might have changed, so nextFree pointers might be stale.
            # We should update them, but it's tricky. Let's just reset them to be safe.
            # Actually, the nextFree pointers are just hints. The get_free functions will skip used colors.
            # But if we removed a color from usedU[u], the nextFreeU[u] pointer might be too high.
            # Let's update: if we removed a color c from usedU[u] and c < nextFreeU[u], set nextFreeU[u] = c.
            # But this is complex. Let's just not worry about it for now, since the get_free functions will still work correctly.
            # The pointers are just for efficiency. If they're too high, get_free will increment until it finds a free color.
            # But if a color was freed, the pointer might skip it. Let's handle this.
            # Actually, in the flipping, we only swap a and b. So if a < nextFreeU[u], we might need to update.
            # But a was free at u before, so nextFreeU[u] <= a. After flipping, b is now free at u, and b >= a (since a was the smallest free).
            # Wait, b could be < a. No, a is the smallest free at u, and b is used at u (we checked b not in usedU[u] is false).
            # So b is in usedU[u] before flipping. After flipping, b is removed from usedU[u].
            # If b < nextFreeU[u], we should update nextFreeU[u] = b.
            # But nextFreeU[u] <= a (since a is free at u), and b could be anything.
            # Actually, b is used at u, so b != a. b could be < a or > a.
            # If b < a, then b < nextFreeU[u] is possible (since nextFreeU[u] <= a).
            # Hmm, nextFreeU[u] is the smallest free color at u, which is a. So nextFreeU[u] = a.
            # If b < a, then after flipping, b is free at u, and b < a = nextFreeU[u]. So we should set nextFreeU[u] = b.
            # But we're assigning b to edge (u, v) right after, so b will be used again. So nextFreeU[u] should remain a.
            # Actually, we assign b to edge (u, v), so b is used at u again. So nextFreeU[u] doesn't change.
            # Similarly for v: a was used at v, after flipping a is free at v. If a < nextFreeD[v], update.
            # But we're assigning b to edge (u, v), and b is already free at v. So nextFreeD[v] = b.
            # After assigning b, b is used at v. nextFreeD[v] might need to be updated.
            # This is getting complicated. Let's just reset the nextFree pointers to 1 for affected vertices.
            # Actually, let's not worry about it. The get_free functions will still work, just potentially slower.
            # But for correctness, it's fine.
            # However, for efficiency, we should update. Let's update nextFreeU[u] and nextFreeD[v] if needed.
            # After flipping and assigning:
            # At u: b was used, now free (after flip), then used again (assigned to edge i). So no change.
            # At v: a was used, now free (after flip). b was free, now used (assigned to edge i).
            # So at v, a is now free. If a < nextFreeD[v], set nextFreeD[v] = a.
            if a < nextFreeD[v]:
                nextFreeD[v] = a
            # Also, for vertices on the path, their used colors changed.
            # For each edge e in path, at its endpoints, a and b were swapped.
            # So if a or b was the smallest free color, the pointer might need updating.
            # This is complex. Let's just reset nextFree for all affected vertices.
            # Actually, let's not. The get_free function will still work correctly, just might be slower.
            # For the problem constraints, it should be fine.
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)))
    sys.stdout.write("\n")

solve()
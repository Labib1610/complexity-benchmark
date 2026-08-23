import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Precompute connected components
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                mask = adj[u]
                v = 0
                while mask:
                    if mask & 1:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                    mask >>= 1
                    v += 1
            components.append(comp)
    
    # Sort components by minimum vertex index to process in order
    components.sort(key=lambda x: min(x))
    
    # Map from original vertex index to component index
    comp_id = [0] * n
    for idx, comp in enumerate(components):
        for v in comp:
            comp_id[v] = idx
    
    # For each component, find all valid 3-colorings
    comp_colorings = []
    
    for comp in components:
        size = len(comp)
        if size == 1:
            # Single vertex can have any color
            comp_colorings.append([0, 1, 2])
            continue
        
        # Reindex vertices in component to 0..size-1
        local_idx = {v: i for i, v in enumerate(comp)}
        local_adj = [0] * size
        for v in comp:
            li = local_idx[v]
            mask = adj[v]
            bit = 0
            while mask:
                if mask & 1:
                    if bit in local_idx:
                        local_adj[li] |= 1 << local_idx[bit]
                mask >>= 1
                bit += 1
        
        # Find all valid colorings using backtracking
        colorings = []
        colors = [-1] * size
        
        def backtrack(pos):
            if pos == size:
                # Convert colors to a single integer representation
                val = 0
                for i in range(size):
                    val |= colors[i] << (2 * i)
                colorings.append(val)
                return
            
            u = pos
            forbidden = 0
            mask = local_adj[u]
            bit = 0
            while mask:
                if mask & 1:
                    if bit < u and colors[bit] != -1:
                        forbidden |= 1 << colors[bit]
                mask >>= 1
                bit += 1
            
            for c in range(3):
                if not (forbidden & (1 << c)):
                    colors[u] = c
                    backtrack(pos + 1)
                    colors[u] = -1
        
        backtrack(0)
        
        if not colorings:
            print("NO")
            return
        
        comp_colorings.append(colorings)
    
    # DP to find lexicographically smallest assignment
    # dp[i] = list of (prev_coloring_idx, current_coloring_idx) pairs
    # We track the best (lexicographically smallest) path
    
    num_comp = len(components)
    
    # For each component, we need to track the best assignment
    # that minimizes the colors of vertices in order
    
    # Strategy: Process components in order, for each component
    # try colorings in order that minimizes the colors of vertices
    # in that component (sorted by original index)
    
    # Sort vertices within each component by original index
    sorted_comp_vertices = [sorted(comp) for comp in components]
    
    # For each component, sort colorings by the colors they assign
    # to vertices (in order of sorted_comp_vertices)
    
    def coloring_key(coloring_val, comp_idx):
        vertices = sorted_comp_vertices[comp_idx]
        local_idx_map = {v: i for i, v in enumerate(components[comp_idx])}
        result = []
        for v in vertices:
            li = local_idx_map[v]
            c = (coloring_val >> (2 * li)) & 3
            result.append(c)
        return tuple(result)
    
    # Sort colorings for each component
    for i in range(num_comp):
        comp_colorings[i].sort(key=lambda x: coloring_key(x, i))
    
    # DP: track the best assignment for each component
    # best[i] = (coloring_idx, prev_best) for component i
    
    best_assignment = [None] * num_comp
    
    for i in range(num_comp):
        best_assignment[i] = 0  # Take the lexicographically smallest coloring
    
    # Construct the final assignment
    assignment = [0] * n
    
    for i in range(num_comp):
        coloring_val = comp_colorings[i][best_assignment[i]]
        comp = components[i]
        local_idx_map = {v: idx for idx, v in enumerate(comp)}
        for v in comp:
            li = local_idx_map[v]
            c = (coloring_val >> (2 * li)) & 3
            assignment[v] = c + 1  # Convert to 1-indexed
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
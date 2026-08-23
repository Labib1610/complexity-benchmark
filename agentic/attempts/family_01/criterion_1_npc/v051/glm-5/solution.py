import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Precompute connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in range(1, n + 1):
                    if (adj[u] & (1 << v)) and not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # For each component, find all valid 3-colorings
    comp_colorings = []
    possible = True
    
    for comp in components:
        comp_size = len(comp)
        if comp_size > 3:
            # Check if it's a K4 (complete graph on 4 vertices)
            # If any 4 vertices are all mutually connected, impossible
            # Actually, we need to check if the component is 3-colorable
            # For n <= 40, we can use backtracking with bitmask
            pass
        
        # Map component vertices to local indices
        local_idx = {v: i for i, v in enumerate(comp)}
        local_adj = [0] * comp_size
        for v in comp:
            for u in comp:
                if adj[v] & (1 << u):
                    local_adj[local_idx[v]] |= (1 << local_idx[u])
        
        # Find all valid colorings using backtracking
        colorings = []
        
        def backtrack(pos, coloring):
            if pos == comp_size:
                colorings.append(tuple(coloring))
                return
            mask = 0
            for j in range(pos):
                if local_adj[pos] & (1 << j):
                    mask |= (1 << coloring[j])
            for c in range(3):
                if not (mask & (1 << c)):
                    coloring.append(c)
                    backtrack(pos + 1, coloring)
                    coloring.pop()
        
        backtrack(0, [])
        
        if not colorings:
            possible = False
            break
        
        # Convert local colorings (0,1,2) to actual chamber assignments (1,2,3)
        # and store as list of tuples
        comp_colorings.append((comp, colorings))
    
    if not possible:
        print("NO")
        return
    
    # Now we need to find the lexicographically smallest assignment
    # We process components in order of their smallest vertex
    # For each component, we try colorings that minimize the assignment
    
    # Sort components by their first vertex (which is the smallest since we process in order)
    # Actually components are already in order of discovery (by smallest vertex)
    
    # We need to find the combination of colorings that gives lexicographically smallest result
    # Since components are independent, we can optimize each component independently
    # but we need the global lexicographically smallest
    
    # For each component, sort colorings by the resulting assignment for vertices in that component
    # Then greedily pick the best one
    
    # But wait - components are independent, so we can optimize each independently
    # The lexicographic order is determined by vertex 1, then 2, etc.
    # Since components don't share vertices, we can optimize each component independently
    # by choosing the coloring that gives the lexicographically smallest sequence for its vertices
    
    # Actually, we need to be careful. The vertices in a component might not be contiguous.
    # But since components are independent, the choice in one doesn't affect another.
    # So for each component, we pick the coloring that minimizes the assignments for its vertices
    # in order of vertex number.
    
    result = [0] * (n + 1)
    
    for comp, colorings in comp_colorings:
        # For each coloring, create the assignment for this component's vertices
        # We want the lexicographically smallest sequence when vertices are ordered by number
        best_coloring = None
        best_seq = None
        
        for coloring in colorings:
            # Create sequence of (vertex, color+1) pairs, sorted by vertex
            seq = tuple((comp[i], coloring[i] + 1) for i in range(len(comp)))
            # We want to compare the colors in order of vertex number
            # Since comp might not be sorted, we need to sort by vertex
            seq_sorted = sorted(seq, key=lambda x: x[0])
            color_seq = tuple(x[1] for x in seq_sorted)
            
            if best_seq is None or color_seq < best_seq:
                best_seq = color_seq
                best_coloring = seq_sorted
        
        # Apply best coloring
        for v, c in best_coloring:
            result[v] = c
    
    print("YES")
    print(" ".join(str(result[i]) for i in range(1, n + 1)))

solve()
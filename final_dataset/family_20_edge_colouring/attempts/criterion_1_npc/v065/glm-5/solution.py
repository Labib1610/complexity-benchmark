import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m
    used = [False] * m
    next_ptr = [0] * (n + 1)
    
    # Find all cycles in the Eulerian-like decomposition
    cycles = []
    for start in range(1, n + 1):
        while next_ptr[start] < len(adj[start]):
            path = []
            path_nodes = [start]
            path_edges = []
            curr = start
            while True:
                while next_ptr[curr] < len(adj[curr]) and used[adj[curr][next_ptr[curr]][1]]:
                    next_ptr[curr] += 1
                if next_ptr[curr] >= len(adj[curr]):
                    break
                nxt, eidx = adj[curr][next_ptr[curr]]
                used[eidx] = True
                path_edges.append(eidx)
                path_nodes.append(nxt)
                curr = nxt
                if curr == start:
                    break
            if path_edges:
                cycles.append(path_edges)
    
    # Build tree of cycles
    # Each cycle is a node in the tree
    # We need to find which cycles share edges (but they don't in Eulerian decomposition)
    # Actually cycles share vertices, not edges. We need to build a tree structure.
    
    # For each vertex, track which cycles pass through it
    vertex_cycles = defaultdict(list)
    for ci, cycle in enumerate(cycles):
        vertices_in_cycle = set()
        for eidx in cycle:
            u, v = edges[eidx]
            vertices_in_cycle.add(u)
            vertices_in_cycle.add(v)
        for vtx in vertices_in_cycle:
            vertex_cycles[vtx].append(ci)
    
    # Build tree: BFS from cycle 0
    C = len(cycles)
    tree_adj = defaultdict(list)
    visited_cycle = [False] * C
    parent_cycle = [-1] * C
    
    if C > 0:
        queue = deque([0])
        visited_cycle[0] = True
        while queue:
            ci = queue.popleft()
            vertices_in_cycle = set()
            for eidx in cycles[ci]:
                u, v = edges[eidx]
                vertices_in_cycle.add(u)
                vertices_in_cycle.add(v)
            for vtx in vertices_in_cycle:
                for cj in vertex_cycles[vtx]:
                    if cj != ci and not visited_cycle[cj]:
                        visited_cycle[cj] = True
                        parent_cycle[cj] = ci
                        tree_adj[ci].append(cj)
                        tree_adj[cj].append(ci)
                        queue.append(cj)
    
    # Process cycles in BFS order (parent before child)
    order = []
    if C > 0:
        visited_order = [False] * C
        queue = deque([0])
        visited_order[0] = True
        while queue:
            ci = queue.popleft()
            order.append(ci)
            for cj in tree_adj[ci]:
                if not visited_order[cj] and parent_cycle[cj] == ci:
                    visited_order[cj] = True
                    queue.append(cj)
    
    # For each cycle, color its edges
    # For the root cycle, alternate 1,2,1,2,...
    # For child cycles, the shared vertex determines the constraint
    
    # Track for each vertex, which colors are used
    vertex_color_used = [set() for _ in range(n + 1)]
    
    for ci in order:
        cycle = cycles[ci]
        L = len(cycle)
        
        if L % 2 == 0:
            # Even cycle: alternate two colors
            # Find which two colors to use
            # For root, use 1 and 2
            # For child, find the shared vertex with parent and use the two colors not used by parent at that vertex
            if parent_cycle[ci] == -1:
                c1, c2 = 1, 2
            else:
                # Find shared vertex with parent
                parent_cycle_idx = parent_cycle[ci]
                parent_vertices = set()
                for eidx in cycles[parent_cycle_idx]:
                    u, v = edges[eidx]
                    parent_vertices.add(u)
                    parent_vertices.add(v)
                
                cycle_vertices = set()
                for eidx in cycle:
                    u, v = edges[eidx]
                    cycle_vertices.add(u)
                    cycle_vertices.add(v)
                
                shared = (parent_vertices & cycle_vertices)
                # Find a shared vertex where we can determine colors
                shared_v = None
                for v in shared:
                    if len(vertex_color_used[v]) >= 1:
                        shared_v = v
                        break
                
                if shared_v is None:
                    c1, c2 = 1, 2
                else:
                    used_colors = vertex_color_used[shared_v]
                    if len(used_colors) == 1:
                        rem = {1, 2, 3} - used_colors
                        c1, c2 = min(rem), max(rem)
                    elif len(used_colors) == 2:
                        rem = ({1, 2, 3} - used_colors)
                        c1 = c2 = min(rem)  # This shouldn't happen for even cycle
                    else:
                        c1, c2 = 1, 2
            
            for i, eidx in enumerate(cycle):
                c = c1 if i % 2 == 0 else c2
                color[eidx] = c
                u, v = edges[eidx]
                vertex_color_used[u].add(c)
                vertex_color_used[v].add(c)
        else:
            # Odd cycle: use all three colors
            # Find the shared vertex with parent to determine starting color
            if parent_cycle[ci] == -1:
                # Root odd cycle - shouldn't happen in valid input but handle it
                # Use 1,2,3,1,2,...
                for i, eidx in enumerate(cycle):
                    c = (i % 3) + 1
                    color[eidx] = c
                    u, v = edges[eidx]
                    vertex_color_used[u].add(c)
                    vertex_color_used[v].add(c)
            else:
                parent_cycle_idx = parent_cycle[ci]
                parent_vertices = set()
                for eidx in cycles[parent_cycle_idx]:
                    u, v = edges[eidx]
                    parent_vertices.add(u)
                    parent_vertices.add(v)
                
                cycle_vertices = set()
                for eidx in cycle:
                    u, v = edges[eidx]
                    cycle_vertices.add(u)
                    cycle_vertices.add(v)
                
                shared = (parent_vertices & cycle_vertices)
                
                # Find shared vertex with most colors used
                shared_v = None
                for v in shared:
                    if len(vertex_color_used[v]) >= 1:
                        shared_v = v
                        break
                
                if shared_v is None or len(vertex_color_used[shared_v]) == 0:
                    # Use 1,2,3 pattern
                    for i, eidx in enumerate(cycle):
                        c = (i % 3) + 1
                        color[eidx] = c
                        u, v = edges[eidx]
                        vertex_color_used[u].add(c)
                        vertex_color_used[v].add(c)
                else:
                    used_colors = vertex_color_used[shared_v]
                    if len(used_colors) == 1:
                        # Two colors remaining, but odd cycle needs 3
                        # This means the shared vertex has 1 color from parent
                        # We need to use the other 2 colors plus one of them repeats
                        # Actually for odd cycle with one shared vertex having 1 color:
                        # The two edges at shared_v in this cycle must use the other 2 colors
                        # But odd cycle can't be 2-colored, so we need 3 colors
                        # The third color must be the one already used at shared_v
                        # Wait - shared_v has degree 2 in this cycle (since it's a simple cycle)
                        # No wait, in Eulerian decomposition, a vertex can appear multiple times
                        
                        # Let's just try: find position of shared_v in cycle
                        # The two edges adjacent to shared_v should use the 2 remaining colors
                        # And the rest alternates, with one edge using the 3rd color
                        
                        remaining = sorted({1, 2, 3} - used_colors)
                        third = list(used_colors)[0]
                        
                        # Find positions of shared_v in path_nodes
                        # Actually cycle is list of edge indices
                        # Let's find which edges are incident to shared_v
                        positions = []
                        for i, eidx in enumerate(cycle):
                            u, v = edges[eidx]
                            if u == shared_v or v == shared_v:
                                positions.append(i)
                        
                        if len(positions) >= 2:
                            # Color the two edges at shared_v with remaining colors
                            # Then alternate
                            # This is complex; let's use a simpler approach
                            pass
                        
                        # Simple approach: try all 6 permutations of 1,2,3 for the pattern
                        # and check which one works
                        found = False
                        for perm in [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]:
                            temp_color = [0] * L
                            for i in range(L):
                                temp_color[i] = perm[i % 3]
                            
                            # Check if shared_v gets the right colors
                            ok = True
                            for i in positions:
                                if temp_color[i] in used_colors:
                                    ok = False
                                    break
                            
                            if ok:
                                for i, eidx in enumerate(cycle):
                                    color[eidx] = temp_color[i]
                                    u, v = edges[eidx]
                                    vertex_color_used[u].add(temp_color[i])
                                    vertex_color_used[v].add(temp_color[i])
                                found = True
                                break
                        
                        if not found:
                            # Fallback
                            for i, eidx in enumerate(cycle):
                                c = (i % 3) + 1
                                color[eidx] = c
                                u, v = edges[eidx]
                                vertex_color_used[u].add(c)
                                vertex_color_used[v].add(c)
                    elif len(used_colors) == 2:
                        # One color remaining
                        remaining = list({1, 2, 3} - used_colors)
                        third = remaining[0]
                        # The two edges at shared_v: one must use third, other must use... 
                        # but both remaining colors are used. So one edge uses third,
                        # other uses one of the used colors (but that violates constraint)
                        # This is the tricky case. 
                        # Actually if shared_v has 2 colors used, the two edges in this cycle
                        # at shared_v must use the 3rd color and... wait, both can't use 3rd.
                        # So one uses 3rd, other uses one of the already used - violation!
                        # Unless shared_v appears more than twice in the cycle.
                        
                        # Try all permutations
                        found = False
                        for perm in [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]:
                            temp_color = [0] * L
                            for i in range(L):
                                temp_color[i] = perm[i % 3]
                            
                            positions = []
                            for i, eidx in enumerate(cycle):
                                u, v = edges[eidx]
                                if u == shared_v or v == shared_v:
                                    positions.append(i)
                            
                            ok = True
                            for i in positions:
                                if temp_color[i] in used_colors:
                                    ok = False
                                    break
                            
                            if ok:
                                for i, eidx in enumerate(cycle):
                                    color[eidx] = temp_color[i]
                                    u, v = edges[eidx]
                                    vertex_color_used[u].add(temp_color[i])
                                    vertex_color_used[v].add(temp_color[i])
                                found = True
                                break
                        
                        if not found:
                            for i, eidx in enumerate(cycle):
                                c = (i % 3) + 1
                                color[eidx] = c
                                u, v = edges[eidx]
                                vertex_color_used[u].add(c)
                                vertex_color_used[v].add(c)
                    else:
                        # 3 colors used - impossible
                        for i, eidx in enumerate(cycle):
                            c = (i % 3) + 1
                            color[eidx] = c
                            u, v = edges[eidx]
                            vertex_color_used[u].add(c)
                            vertex_color_used[v].add(c)
    
    # Verify the solution
    valid = True
    for v in range(1, n + 1):
        colors_at_v = set()
        for idx, (u, w) in enumerate(edges):
            if u == v or w == v:
                colors_at_v.add(color[idx])
        if len(colors_at_v) != 3:
            valid = False
            break
    
    if valid:
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()
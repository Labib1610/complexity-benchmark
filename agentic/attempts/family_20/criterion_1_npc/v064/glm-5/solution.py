import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    
    # Each politician must appear exactly 3 times (degree 3)
    # We need to assign each edge a color from {1, 2, 3}
    # such that for each vertex, all three incident edges have different colors
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Initialize edge colors to 0 (unassigned)
    color = [0] * m
    
    # For each vertex, track which colors are used by incident edges
    # and which edges are uncolored
    # We'll process vertices and resolve conflicts iteratively
    
    # Using a simple greedy approach with conflict resolution
    # For each vertex, if there are uncolored edges, assign available colors
    # If conflict arises (two edges need same color), we can swap along a path
    
    # Since the graph is 3-regular and we have 3 colors, this is edge coloring
    # of a 3-regular graph. By a theorem, such graphs are 3-edge-colorable
    # iff they are bridgeless (no cut edges). But we need to check.
    
    # For simplicity, we'll use a greedy approach with backtracking on conflicts
    
    # Process edges one by one
    for i in range(m):
        u, v = edges[i]
        # Find available colors for this edge
        used_u = set()
        for w, j in adj[u]:
            if color[j] != 0:
                used_u.add(color[j])
        used_v = set()
        for w, j in adj[v]:
            if color[j] != 0:
                used_v.add(color[j])
        
        # Available colors are those not in used_u and not in used_v
        available = []
        for c in range(1, 4):
            if c not in used_u and c not in used_v:
                available.append(c)
        
        if available:
            color[i] = available[0]
        else:
            # No color available, need to recolor
            # Find a color c_u that's in used_u but not in used_v
            # and a color c_v that's in used_v but not in used_u
            # Then we can swap colors along a path
            
            c_u = None
            c_v = None
            for c in range(1, 4):
                if c in used_u and c not in used_v:
                    c_u = c
                if c in used_v and c not in used_u:
                    c_v = c
            
            if c_u is not None and c_v is not None:
                # Find the edge incident to u with color c_u and swap
                for w, j in adj[u]:
                    if color[j] == c_u:
                        # Swap: change edge j to c_v, then edge i to c_u
                        color[j] = c_v
                        color[i] = c_u
                        break
            else:
                # This shouldn't happen for a valid 3-regular graph
                # But if it does, we need more complex resolution
                # For now, try another approach
                # Find colors: one in used_u, one in used_v, one unused
                all_used = used_u | used_v
                unused = None
                for c in range(1, 4):
                    if c not in all_used:
                        unused = c
                        break
                
                if unused is not None:
                    # Find c_u in used_u and c_v in used_v
                    for c in range(1, 4):
                        if c in used_u:
                            c_u = c
                            break
                    for c in range(1, 4):
                        if c in used_v:
                            c_v = c
                            break
                    # Swap along path from u using c_u
                    for w, j in adj[u]:
                        if color[j] == c_u:
                            color[j] = unused
                            color[i] = c_u
                            break
                else:
                    # All three colors are used at both u and v
                    # This means u and v both have 3 colored edges already
                    # But we're trying to color edge (u,v), so this is impossible
                    # unless there's an error in our logic
                    # Let's try a different approach: find alternating path
                    c1 = list(used_u)[0]
                    c2 = list(used_v)[0]
                    if c1 == c2:
                        c2 = list(used_v)[1] if len(used_v) > 1 else list(used_v)[0]
                    
                    # Find alternating path from u using colors c1 and c2
                    # and swap along the path
                    path = []
                    visited = set()
                    current = u
                    current_color = c2
                    while True:
                        found = False
                        for w, j in adj[current]:
                            if color[j] == current_color and j not in visited:
                                visited.add(j)
                                path.append(j)
                                current = w
                                current_color = c1 if current_color == c2 else c2
                                found = True
                                break
                        if not found:
                            break
                    
                    # Swap colors along the path
                    for j in path:
                        if color[j] == c1:
                            color[j] = c2
                        else:
                            color[j] = c1
                    
                    # Now try to color edge i again
                    used_u = set()
                    for w, j in adj[u]:
                        if color[j] != 0:
                            used_u.add(color[j])
                    used_v = set()
                    for w, j in adj[v]:
                        if color[j] != 0:
                            used_v.add(color[j])
                    
                    for c in range(1, 4):
                        if c not in used_u and c not in used_v:
                            color[i] = c
                            break
    
    # Verify the solution
    for v in range(1, n + 1):
        colors_used = set()
        for w, j in adj[v]:
            colors_used.add(color[j])
        if len(colors_used) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    
    edges = []
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    delta = max(max(deg_L), max(deg_R))
    
    # Build adjacency lists for the bipartite graph
    adj_L = [[] for _ in range(nL + 1)]
    adj_R = [[] for _ in range(nR + 1)]
    for idx, (u, v) in enumerate(edges):
        adj_L[u].append((v, idx))
        adj_R[v].append((u, idx))
    
    # Track current color usage at each vertex
    used_L = [set() for _ in range(nL + 1)]
    used_R = [set() for _ in range(nR + 1)]
    
    # Answer array
    ans = [0] * m
    
    # Process edges in order
    for edge_idx, (u, v) in enumerate(edges):
        # Find available color
        # Colors used at u or v are forbidden
        forbidden = used_L[u] | used_R[v]
        color = 1
        while color in forbidden:
            color += 1
        
        ans[edge_idx] = color
        used_L[u].add(color)
        used_R[v].add(color)
        
        # Check for alternating path to recolor if needed
        # We need to ensure we don't exceed delta colors
        # If color > delta, find an alternating path to recolor
        # This shouldn't happen if delta is correct, but let's be safe
        if color > delta:
            # Find alternating path using BFS
            # We need to find a path from u or v to a vertex with an available color
            # Using edge colors alternating between color and some other color
            # This is a standard edge coloring augmentation
            # For simplicity, we'll use a greedy approach with path augmentation
            
            # Find a color missing at u and a color missing at v
            missing_u = set(range(1, delta + 1)) - used_L[u]
            missing_v = set(range(1, delta + 1)) - used_R[v]
            
            if missing_u and missing_v:
                # There should be a common missing color, but if not, we need path augmentation
                # Actually, if color > delta, we need to find an alternating path
                pass
            
            # Standard Vizing's theorem augmentation for bipartite graphs
            # Find alternating path from u using colors (c1, c2) where c1 is missing at u
            # and c2 is missing at v
            
            c1 = next(iter(missing_u)) if missing_u else None
            c2 = next(iter(missing_v)) if missing_v else None
            
            if c1 is not None and c2 is not None:
                # Find alternating path from v using colors c1 and c2
                # BFS to find path
                parent = {}  # maps vertex to (prev_vertex, edge_idx, color_on_edge)
                queue = deque()
                
                # Start from v, looking for edges with color c1
                # Then alternate between c2 and c1
                
                found = False
                end_vertex = None
                
                # We're at v, looking for an edge with color c1 to some u'
                for (u_prime, e_idx) in adj_R[v]:
                    if ans[e_idx] == c1:
                        # Can traverse this edge
                        if c2 not in used_L[u_prime]:
                            # Found path! u_prime is missing c2
                            # Recolor: edge e_idx gets c2, our edge gets c1
                            ans[e_idx] = c2
                            used_L[u_prime].remove(c1)
                            used_L[u_prime].add(c2)
                            used_R[v].remove(c1)
                            used_R[v].add(c2)
                            
                            ans[edge_idx] = c1
                            used_L[u].add(c1)
                            used_R[v].add(c1)
                            found = True
                            break
                        else:
                            # Continue BFS from u_prime
                            queue.append((u_prime, c2, e_idx))
                            parent[u_prime] = (v, e_idx, c1)
                
                if not found:
                    while queue:
                        curr, expected_color, came_from_edge = queue.popleft()
                        # curr is on L side, expected_color is what we expect on next edge
                        # We came from R side via came_from_edge
                        
                        # Look for edge with expected_color from curr
                        for (v_prime, e_idx) in adj_L[curr]:
                            if e_idx == came_from_edge:
                                continue
                            if ans[e_idx] == expected_color:
                                # Check if v_prime is missing the other color
                                other_color = c1 if expected_color == c2 else c2
                                if other_color not in used_R[v_prime]:
                                    # Found path! Recolor
                                    # Backtrack and recolor
                                    path = []
                                    path.append((curr, v_prime, e_idx, expected_color))
                                    
                                    # Backtrack
                                    trace = curr
                                    while trace in parent:
                                        prev_v, prev_e, prev_c = parent[trace]
                                        path.append((trace, prev_v, prev_e, prev_c))
                                        trace = prev_v
                                    
                                    # Recolor all edges on path
                                    for (a, b, e, col) in path:
                                        new_col = c2 if col == c1 else c1
                                        ans[e] = new_col
                                        # Update used sets
                                        used_L[a].remove(col)
                                        used_L[a].add(new_col)
                                        used_R[b].remove(col)
                                        used_R[b].add(new_col)
                                    
                                    # Recolor our edge
                                    ans[edge_idx] = c1
                                    used_L[u].add(c1)
                                    used_R[v].add(c1)
                                    found = True
                                    break
                                else:
                                    # Continue BFS
                                    next_color = c1 if expected_color == c2 else c2
                                    queue.append((v_prime, next_color, e_idx))
                                    parent[v_prime] = (curr, e_idx, expected_color)
                        
                        if found:
                            break
    
    print("YES")
    print(" ".join(map(str, ans)))

solve()
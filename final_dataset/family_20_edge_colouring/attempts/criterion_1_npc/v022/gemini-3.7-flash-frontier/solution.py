import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            comp_nodes = []
            comp_edges = []
            q = [i]
            visited[i] = True
            for u in q:
                comp_nodes.append(u)
                for v, e_idx in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            components.append(comp_nodes)

    final_assignment = [0] * m

    for comp in components:
        # Build local DPLL / Constraint Propagation for this component
        # Edges in this component
        comp_edges = set()
        for u in comp:
            for v, e_idx in adj[u]:
                comp_edges.add(e_idx)
        
        # State representation:
        # color_assigned[e] = -1 if unassigned, else 0, 1, 2
        # edge_mask[e] = bitmask of possible colors (bit 0: col 0, bit 1: col 1, bit 2: col 2)
        # vertex_color_mask[v][c] = bitmask of incident edges (0, 1, 2) that can take color c
        
        edge_mask = {e: 7 for e in comp_edges}
        color_assigned = {e: -1 for e in comp_edges}
        
        # For each vertex, store its 3 incident edges
        v_edges = {u: [e_idx for _, e_idx in adj[u]] for u in comp}
        # vertex_candidates[u][c] = bitmask (submask of 7) of incident edges that can take color c
        v_cand = {u: [7, 7, 7] for u in comp}

        def set_edge_color(e, c, trail):
            # Try to assign color c (0, 1, or 2) to edge e
            if color_assigned[e] != -1:
                return color_assigned[e] == c
            
            # Queue for propagation: entries are ('assign', e, c)
            queue = [(e, c)]
            
            while queue:
                curr_e, curr_c = queue.pop()
                
                if color_assigned[curr_e] != -1:
                    if color_assigned[curr_e] != curr_c:
                        return False
                    continue
                
                if not (edge_mask[curr_e] & (1 << curr_c)):
                    return False
                
                # Assign
                trail.append(('color', curr_e, color_assigned[curr_e]))
                color_assigned[curr_e] = curr_c
                
                old_mask = edge_mask[curr_e]
                trail.append(('edge_mask', curr_e, old_mask))
                edge_mask[curr_e] = (1 << curr_c)
                
                u, v = edges[curr_e]
                
                # Update endpoints
                for node in (u, v):
                    # In node, curr_e is colored curr_c.
                    # Other incident edges cannot have curr_c.
                    node_e_list = v_edges[node]
                    curr_pos = node_e_list.index(curr_e)
                    
                    # For other colors, curr_e cannot have them
                    for other_c in range(3):
                        if other_c != curr_c:
                            if v_cand[node][other_c] & (1 << curr_pos):
                                trail.append(('v_cand', node, other_c, v_cand[node][other_c]))
                                v_cand[node][other_c] &= ~(1 << curr_pos)
                                # Check if any incident edge can have other_c
                                mask = v_cand[node][other_c]
                                if mask == 0:
                                    return False
                                if (mask & (mask - 1)) == 0:
                                    # Exactly one edge can have other_c
                                    forced_pos = (mask.bit_length() - 1)
                                    forced_e = node_e_list[forced_pos]
                                    queue.append((forced_e, other_c))
                    
                    # For other incident edges, they cannot have curr_c
                    for pos in range(3):
                        if pos != curr_pos:
                            other_e = node_e_list[pos]
                            if v_cand[node][curr_c] & (1 << pos):
                                trail.append(('v_cand', node, curr_c, v_cand[node][curr_c]))
                                v_cand[node][curr_c] &= ~(1 << pos)
                            
                            # Also update edge_mask of other_e
                            if edge_mask[other_e] & (1 << curr_c):
                                trail.append(('edge_mask', other_e, edge_mask[other_e]))
                                edge_mask[other_e] &= ~(1 << curr_c)
                                em = edge_mask[other_e]
                                if em == 0:
                                    return False
                                if (em & (em - 1)) == 0:
                                    forced_c = em.bit_length() - 1
                                    queue.append((other_e, forced_c))
            return True

        def undo(trail):
            while trail:
                item = trail.pop()
                tag = item[0]
                if tag == 'color':
                    _, e, val = item
                    color_assigned[e] = val
                elif tag == 'edge_mask':
                    _, e, val = item
                    edge_mask[e] = val
                elif tag == 'v_cand':
                    _, node, c, val = item
                    v_cand[node][c] = val

        # Fix symmetry at first node in component
        root = comp[0]
        root_edges = v_edges[root]
        
        init_trail = []
        ok = True
        for c_idx, e_idx in enumerate(root_edges):
            if not set_edge_color(e_idx, c_idx, init_trail):
                ok = False
                break
        
        if not ok:
            print("NO")
            return

        # Search function
        def search():
            # MRV: find unassigned edge with minimum possible colors
            best_e = -1
            min_cands = 4
            
            for e in comp_edges:
                if color_assigned[e] == -1:
                    cnt = bin(edge_mask[e]).count('1')
                    if cnt < min_cands:
                        min_cands = cnt
                        best_e = e
                        if cnt <= 1:
                            break
            
            if best_e == -1:
                return True
            
            if min_cands == 0:
                return False
            
            mask = edge_mask[best_e]
            for c in range(3):
                if mask & (1 << c):
                    trail = []
                    if set_edge_color(best_e, c, trail):
                        if search():
                            return True
                    undo(trail)
            return False

        if not search():
            print("NO")
            return
        
        for e in comp_edges:
            final_assignment[e] = color_assigned[e] + 1

    print("YES")
    print(*(final_assignment[i] for i in range(m)))

if __name__ == '__main__':
    solve()
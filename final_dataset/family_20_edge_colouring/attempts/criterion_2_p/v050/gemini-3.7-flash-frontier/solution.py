import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    NT = int(input_data[0])
    NR = int(input_data[1])
    M = int(input_data[2])
    
    if M == 0:
        print("YES")
        print()
        return

    # Edges: u in 0..NT-1, v in 0..NR-1
    # We will represent L as 0..NT-1, R as NT..NT+NR-1
    u_list = [0] * M
    v_list = [0] * M
    deg_L = [0] * NT
    deg_R = [0] * NR
    
    idx = 3
    for i in range(M):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        u_list[i] = u
        v_list[i] = v
        deg_L[u] += 1
        deg_R[v] += 1
        
    K = max(max(deg_L), max(deg_R))
    
    color = [0] * M
    
    # We will recursively split edge sets.
    # To be efficient, we can represent the subproblem by a list of edge indices and max degree delta.
    # If delta == 1, all edges in this subgraph can be colored with the base color.
    
    # We need an efficient way to find Eulerian paths/cycles on the bipartite subgraph.
    # Vertices involved: L vertices 0..NT-1, R vertices NT..NT+NR-1 (or separate).
    
    head = [-1] * (NT + NR)
    nxt = [0] * (2 * M + 2 * (NT + NR))
    to = [0] * (2 * M + 2 * (NT + NR))
    eid = [0] * (2 * M + 2 * (NT + NR))
    used_edge = [False] * (M + NT + NR + 5)
    
    # We can do this iteratively using a queue/stack of subproblems: (edge_list, delta, color_offset)
    stack = [(list(range(M)), K, 1)]
    
    while stack:
        edge_indices, delta, c_offset = stack.pop()
        
        if not edge_indices:
            continue
        if delta == 1:
            for e in edge_indices:
                color[e] = c_offset
            continue
        
        d1 = (delta + 1) // 2
        d2 = delta // 2
        
        # Build graph for this subproblem
        # Collect active vertices and compute their degrees
        # Map active vertices to save time, or just track them
        active_V = []
        cur_deg = {}
        for e in edge_indices:
            u = u_list[e]
            v = v_list[e] + NT
            cur_deg[u] = cur_deg.get(u, 0) + 1
            cur_deg[v] = cur_deg.get(v, 0) + 1
            
        edge_cnt = 0
        for e in edge_indices:
            u = u_list[e]
            v = v_list[e] + NT
            
            # Add edge u -> v
            to[edge_cnt] = v
            eid[edge_cnt] = e
            nxt[edge_cnt] = head[u]
            head[u] = edge_cnt
            edge_cnt += 1
            
            # Add edge v -> u
            to[edge_cnt] = u
            eid[edge_cnt] = e
            nxt[edge_cnt] = head[v]
            head[v] = edge_cnt
            edge_cnt += 1
            
            used_edge[e] = False
            
        # Find odd degree vertices in L and R
        odd_L = []
        odd_R = []
        for v, d in cur_deg.items():
            if d % 2 == 1:
                if v < NT:
                    odd_L.append(v)
                else:
                    odd_R.append(v)
                    
        # Add dummy edges between odd_L and odd_R
        dummy_start_eid = M
        num_dummies = len(odd_L) # len(odd_L) == len(odd_R) in bipartite graph
        for i in range(num_dummies):
            u = odd_L[i]
            v = odd_R[i]
            deid = dummy_start_eid + i
            used_edge[deid] = False
            
            to[edge_cnt] = v
            eid[edge_cnt] = deid
            nxt[edge_cnt] = head[u]
            head[u] = edge_cnt
            edge_cnt += 1
            
            to[edge_cnt] = u
            eid[edge_cnt] = deid
            nxt[edge_cnt] = head[v]
            head[v] = edge_cnt
            edge_cnt += 1
            
        # Now every vertex in the modified graph has even degree!
        # Find Euler circuits and decompose into edges for G1 and G2.
        # Note: If an Euler circuit has odd-length paths between dummy edges,
        # dummy edges connect L and R.
        # To make sure every path of real edges starts at L and ends at R:
        # If we alternate edges along the Eulerian tour, dummy edges should be in G2 (or G1).
        # Specifically, if dummy edges are given to G2, then every maximal path of real edges
        # has odd length, starts in L, ends in R, and its 1st and last edges are in G1!
        # Thus, odd degree vertices in L and R have degree ceil(d/2) in G1 and floor(d/2) in G2.
        
        edges1 = []
        edges2 = []
        
        # Traverse Euler tours
        for start_node in cur_deg:
            while head[start_node] != -1:
                # Find an Euler circuit starting from start_node
                # Non-recursive Hierholzer
                curr_path = [start_node]
                circuit = []
                while curr_path:
                    curr_v = curr_path[-1]
                    edge_idx = head[curr_v]
                    while edge_idx != -1 and used_edge[eid[edge_idx]]:
                        edge_idx = nxt[edge_idx]
                    head[curr_v] = edge_idx
                    
                    if edge_idx != -1:
                        e = eid[edge_idx]
                        used_edge[e] = True
                        next_v = to[edge_idx]
                        head[curr_v] = nxt[edge_idx]
                        curr_path.append(next_v)
                        circuit.append((curr_v, next_v, e))
                    else:
                        curr_path.pop()
                
                # Now `circuit` contains directed steps of the tour in order
                # If there are dummy edges, we can rotate the circuit so it starts with a dummy edge
                # (directed from R to L, so the next real edge starts at L), or just alternate.
                # Actually, dummy edges are always between L and R.
                # Any circuit in a bipartite graph has even length.
                # If a dummy edge is directed from R to L, and we give it color 2 (G2),
                # then the next edge starts at L, gets color 1 (G1), ..., and before the next dummy edge (which goes R->L)
                # the edge entering R gets color 1 (G1).
                # So every dummy edge (R->L) gets color 2!
                # Let's find dummy edges in the circuit.
                if num_dummies > 0:
                    # Find a dummy edge
                    dummy_idx = -1
                    for idx_c, (u_c, v_c, e_c) in enumerate(circuit):
                        if e_c >= M:
                            # We want the dummy edge directed R -> L to be at step with color 2,
                            # or dummy edge directed L -> R to be at step with color 2.
                            # Standard: real path is L -> ... -> R.
                            # Dummy edge goes R -> L.
                            # If dummy edge goes R -> L and is step 1 (0-indexed: index 1, i.e., G2),
                            # then index 0 is real edge entering R (in G1), index 2 is real edge leaving L (in G1).
                            dummy_idx = idx_c
                            break
                    if dummy_idx != -1:
                        # Rotate circuit so that circuit[0] is an edge from L to ... or dummy edge
                        # If circuit[dummy_idx] has u_c in R, v_c in L:
                        u_c, v_c, e_c = circuit[dummy_idx]
                        if u_c >= NT: # R -> L
                            # We want this dummy edge to be in G2 (odd index, e.g. index 1)
                            # so the edge after it (leaving v_c in L) is at index 0 (even index, G1).
                            # Rotate so circuit starts at dummy_idx + 1:
                            circuit = circuit[dummy_idx + 1:] + circuit[:dummy_idx + 1]
                        else: # L -> R
                            # dummy edge goes L -> R. Then the edge before it left R (was in G1).
                            # The edge after it enters R.
                            # Dummy edge should be in G2 (odd index).
                            # Rotate so dummy_idx is at index 1:
                            circuit = circuit[dummy_idx - 1:] + circuit[:dummy_idx - 1]
                
                # Alternate edges
                for idx_c, (u_c, v_c, e_c) in enumerate(circuit):
                    if e_c < M:
                        if idx_c % 2 == 0:
                            edges1.append(e_c)
                        else:
                            edges2.append(e_c)
                            
        # Clean up head array for vertices used
        for v in cur_deg:
            head[v] = -1
            
        stack.append((edges1, d1, c_offset))
        stack.append((edges2, d2, c_offset + d1))
        
    print("YES")
    print(*(color[i] for i in range(M)))

if __name__ == '__main__':
    solve()
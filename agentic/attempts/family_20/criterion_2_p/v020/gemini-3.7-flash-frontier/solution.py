import sys
import random

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n_L = int(input_data[0])
    n_R = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    deg_L = [0] * (n_L + 1)
    deg_R = [0] * (n_R + 1)
    
    edges_raw = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges_raw.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    if Delta == 0:
        print("YES")
        print()
        return

    # Bin packing for L
    bins_L = []
    bin_L_of = [0] * (n_L + 1)
    curr_bin = []
    curr_deg = 0
    for u in range(1, n_L + 1):
        if deg_L[u] == 0:
            continue
        if curr_deg + deg_L[u] > Delta:
            bins_L.append(curr_bin)
            curr_bin = []
            curr_deg = 0
        curr_bin.append(u)
        curr_deg += deg_L[u]
    if curr_bin:
        bins_L.append(curr_bin)
        
    for b_idx, b in enumerate(bins_L):
        for u in b:
            bin_L_of[u] = b_idx
            
    # Bin packing for R
    bins_R = []
    bin_R_of = [0] * (n_R + 1)
    curr_bin = []
    curr_deg = 0
    for v in range(1, n_R + 1):
        if deg_R[v] == 0:
            continue
        if curr_deg + deg_R[v] > Delta:
            bins_R.append(curr_bin)
            curr_bin = []
            curr_deg = 0
        curr_bin.append(v)
        curr_deg += deg_R[v]
    if curr_bin:
        bins_R.append(curr_bin)
        
    for b_idx, b in enumerate(bins_R):
        for v in b:
            bin_R_of[v] = b_idx
            
    B = max(len(bins_L), len(bins_R), 1)
    
    bin_deg_L = [0] * B
    bin_deg_R = [0] * B
    
    initial_edges = []
    edge_u = []
    edge_v = []
    
    for i in range(m):
        u, v = edges_raw[i]
        bu = bin_L_of[u]
        bv = bin_R_of[v]
        initial_edges.append((bu, bv, i))
        edge_u.append(bu)
        edge_v.append(bv)
        bin_deg_L[bu] += 1
        bin_deg_R[bv] += 1
        
    # Regularization with dummy edges
    dummy_e_id = m
    def_L_idx = 0
    def_R_idx = 0
    while def_L_idx < B and def_R_idx < B:
        while def_L_idx < B and bin_deg_L[def_L_idx] == Delta:
            def_L_idx += 1
        while def_R_idx < B and bin_deg_R[def_R_idx] == Delta:
            def_R_idx += 1
        if def_L_idx < B and def_R_idx < B:
            initial_edges.append((def_L_idx, def_R_idx, dummy_e_id))
            edge_u.append(def_L_idx)
            edge_v.append(def_R_idx)
            bin_deg_L[def_L_idx] += 1
            bin_deg_R[def_R_idx] += 1
            dummy_e_id += 1

    total_edges_count = len(initial_edges)
    used_edge = [False] * total_edges_count
    ans = [0] * m

    def solve(edges, D, color_offset):
        if D == 1:
            for u, v, e_id in edges:
                if e_id < m:
                    ans[e_id] = color_offset + 1
            return

        if D % 2 == 1:
            # Random walk to find 1 perfect matching
            adj_L = [[] for _ in range(B)]
            for u, v, e_id in edges:
                adj_L[u].append((v, e_id))
            
            match_R = [None] * B
            for u0 in range(B):
                u = u0
                while u is not None:
                    v, e_id = random.choice(adj_L[u])
                    prev = match_R[v]
                    match_R[v] = (u, e_id)
                    u = prev[0] if prev is not None else None
            
            matching_edges = set()
            for v in range(B):
                u, e_id = match_R[v]
                matching_edges.add(e_id)
                if e_id < m:
                    ans[e_id] = color_offset + 1
            
            remaining_edges = [e for e in edges if e[2] not in matching_edges]
            solve(remaining_edges, D - 1, color_offset + 1)
        else:
            # D is even, Euler tour splitting
            adj = [[] for _ in range(2 * B)]
            for u, v, e_id in edges:
                adj[u].append((B + v, e_id))
                adj[B + v].append((u, e_id))
            
            pos = [0] * (2 * B)
            subgraph0_ids = []
            subgraph1_ids = []
            
            for s in range(2 * B):
                if pos[s] < len(adj[s]):
                    stack = [(s, -1)]
                    tour_edges = []
                    while stack:
                        u, _ = stack[-1]
                        while pos[u] < len(adj[u]) and used_edge[adj[u][pos[u]][1]]:
                            pos[u] += 1
                        if pos[u] < len(adj[u]):
                            nxt, e_id = adj[u][pos[u]]
                            pos[u] += 1
                            used_edge[e_id] = True
                            stack.append((nxt, e_id))
                        else:
                            _, e_id = stack.pop()
                            if e_id != -1:
                                tour_edges.append(e_id)
                    
                    for i, e_id in enumerate(tour_edges):
                        if i % 2 == 0:
                            subgraph0_ids.append(e_id)
                        else:
                            subgraph1_ids.append(e_id)
            
            edges0 = [(edge_u[e_id], edge_v[e_id], e_id) for e_id in subgraph0_ids]
            edges1 = [(edge_u[e_id], edge_v[e_id], e_id) for e_id in subgraph1_ids]
            
            solve(edges0, D // 2, color_offset)
            solve(edges1, D // 2, color_offset + D // 2)

    solve(initial_edges, Delta, 0)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    main()
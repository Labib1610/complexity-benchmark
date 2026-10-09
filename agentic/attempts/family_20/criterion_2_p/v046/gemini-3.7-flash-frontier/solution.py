import sys
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n_in = int(input_data[0])
    n_out = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    deg_L = [0] * n_in
    deg_R = [0] * n_out
    
    edges_u = [0] * m
    edges_v = [0] * m
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges_u[i] = u
        edges_v[i] = v
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = 0
    for d in deg_L:
        if d > Delta:
            Delta = d
    for d in deg_R:
        if d > Delta:
            Delta = d
            
    if Delta == 0:
        print("YES")
        print()
        return

    # Bin packing for L
    bins_L = []
    bin_map_L = [-1] * n_in
    cur_sum = 0
    cur_bin = 0
    for u in range(n_in):
        if deg_L[u] == 0:
            continue
        if cur_sum + deg_L[u] > Delta:
            cur_bin += 1
            cur_sum = 0
        bin_map_L[u] = cur_bin
        cur_sum += deg_L[u]
    num_bins_L = cur_bin + 1 if any(d > 0 for d in deg_L) else 0

    # Bin packing for R
    bin_map_R = [-1] * n_out
    cur_sum = 0
    cur_bin = 0
    for v in range(n_out):
        if deg_R[v] == 0:
            continue
        if cur_sum + deg_R[v] > Delta:
            cur_bin += 1
            cur_sum = 0
        bin_map_R[v] = cur_bin
        cur_sum += deg_R[v]
    num_bins_R = cur_bin + 1 if any(d > 0 for d in deg_R) else 0

    N = max(num_bins_L, num_bins_R, 1)

    bin_deg_L = [0] * N
    bin_deg_R = [0] * N

    reg_edges = []
    for i in range(m):
        bu = bin_map_L[edges_u[i]]
        bv = bin_map_R[edges_v[i]]
        bin_deg_L[bu] += 1
        bin_deg_R[bv] += 1
        reg_edges.append((bu, bv, i))

    # Add dummy edges to make it Delta-regular
    def_L = [Delta - bin_deg_L[i] for i in range(N)]
    def_R = [Delta - bin_deg_R[i] for i in range(N)]
    
    pL = 0
    pR = 0
    while pL < N and pR < N:
        while pL < N and def_L[pL] == 0:
            pL += 1
        while pR < N and def_R[pR] == 0:
            pR += 1
        if pL < N and pR < N:
            add = min(def_L[pL], def_R[pR])
            for _ in range(add):
                reg_edges.append((pL, pR, -1))
            def_L[pL] -= add
            def_R[pR] -= add

    ans = [0] * m
    random.seed(42)

    def regular_edge_coloring(edges, d, color_offset):
        if d == 0:
            return
        if d == 1:
            for u, v, orig_id in edges:
                if orig_id != -1:
                    ans[orig_id] = color_offset + 1
            return

        if d % 2 == 1:
            # Random walk matching
            adj_L = [[] for _ in range(N)]
            for e_idx, (u, v, orig_id) in enumerate(edges):
                adj_L[u].append((v, e_idx))

            match_R = [-1] * N
            match_edge_idx = [-1] * N

            for i in range(N):
                curr = i
                while curr != -1:
                    nbrs = adj_L[curr]
                    v, e_idx = nbrs[random.randrange(len(nbrs))]
                    next_u = match_R[v]
                    if next_u == curr:
                        continue
                    match_R[v] = curr
                    match_edge_idx[v] = e_idx
                    curr = next_u

            matched_set = [False] * len(edges)
            for v in range(N):
                e_idx = match_edge_idx[v]
                matched_set[e_idx] = True
                orig_id = edges[e_idx][2]
                if orig_id != -1:
                    ans[orig_id] = color_offset + d

            rem_edges = [edges[i] for i in range(len(edges)) if not matched_set[i]]
            regular_edge_coloring(rem_edges, d - 1, color_offset)
        else:
            # Euler tour decomposition into two (d/2)-regular graphs
            adj = [[] for _ in range(2 * N)]
            for e_idx, (u, v, orig_id) in enumerate(edges):
                adj[u].append((v + N, e_idx))
                adj[v + N].append((u, e_idx))

            used = [False] * len(edges)
            ptr = [0] * (2 * N)
            circuit = []

            for start_node in range(2 * N):
                while ptr[start_node] < len(adj[start_node]):
                    stack = [(start_node, -1)]
                    while stack:
                        u, e_in = stack[-1]
                        while ptr[u] < len(adj[u]) and used[adj[u][ptr[u]][1]]:
                            ptr[u] += 1
                        if ptr[u] < len(adj[u]):
                            v, e_idx = adj[u][ptr[u]]
                            ptr[u] += 1
                            used[e_idx] = True
                            stack.append((v, e_idx))
                        else:
                            stack.pop()
                            if e_in != -1:
                                circuit.append(e_in)

            g1_edges = []
            g2_edges = []
            for k, e_idx in enumerate(circuit):
                if k % 2 == 0:
                    g1_edges.append(edges[e_idx])
                else:
                    g2_edges.append(edges[e_idx])

            regular_edge_coloring(g1_edges, d // 2, color_offset)
            regular_edge_coloring(g2_edges, d // 2, color_offset + d // 2)

    regular_edge_coloring(reg_edges, Delta, 0)

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()
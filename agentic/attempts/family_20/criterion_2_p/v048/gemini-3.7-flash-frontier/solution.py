import sys
import random

# Increase recursion depth for deep recursion trees if any
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    # Read edges
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    orig_edges = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        orig_edges.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1

    Delta = max(max(deg_L), max(deg_R))
    if Delta == 0:
        sys.stdout.write("YES\n\n")
        return

    # Step 1: Vertex Merging (Bin Packing)
    bins_L = []
    curr_bin = []
    curr_deg = 0
    for u in range(1, nL + 1):
        if deg_L[u] == 0:
            continue
        if curr_deg + deg_L[u] > Delta and curr_bin:
            bins_L.append(curr_bin)
            curr_bin = [u]
            curr_deg = deg_L[u]
        else:
            curr_bin.append(u)
            curr_deg += deg_L[u]
    if curr_bin:
        bins_L.append(curr_bin)

    bins_R = []
    curr_bin = []
    curr_deg = 0
    for v in range(1, nR + 1):
        if deg_R[v] == 0:
            continue
        if curr_deg + deg_R[v] > Delta and curr_bin:
            bins_R.append(curr_bin)
            curr_bin = [v]
            curr_deg = deg_R[v]
        else:
            curr_bin.append(v)
            curr_deg += deg_R[v]
    if curr_bin:
        bins_R.append(curr_bin)

    K = max(len(bins_L), len(bins_R))
    while len(bins_L) < K:
        bins_L.append([])
    while len(bins_R) < K:
        bins_R.append([])

    bin_map_L = [0] * (nL + 1)
    for b_idx, b in enumerate(bins_L):
        for u in b:
            bin_map_L[u] = b_idx

    bin_map_R = [0] * (nR + 1)
    for b_idx, b in enumerate(bins_R):
        for v in b:
            bin_map_R[v] = b_idx

    bin_deg_L = [sum(deg_L[u] for u in b) for b in bins_L]
    bin_deg_R = [sum(deg_R[v] for v in b) for b in bins_R]

    def_L = [Delta - d for d in bin_deg_L]
    def_R = [Delta - d for d in bin_deg_R]

    # Step 2: Regularization via dummy edges
    edges = []
    for i, (u, v) in enumerate(orig_edges):
        edges.append((bin_map_L[u], bin_map_R[v], i))

    dummy_eid = m
    i_ptr = 0
    j_ptr = 0
    while i_ptr < K and j_ptr < K:
        while i_ptr < K and def_L[i_ptr] == 0:
            i_ptr += 1
        while j_ptr < K and def_R[j_ptr] == 0:
            j_ptr += 1
        if i_ptr < K and j_ptr < K:
            take = min(def_L[i_ptr], def_R[j_ptr])
            for _ in range(take):
                edges.append((i_ptr, j_ptr, dummy_eid))
                dummy_eid += 1
            def_L[i_ptr] -= take
            def_R[j_ptr] -= take

    total_edges_count = dummy_eid
    ans = [0] * total_edges_count

    # Step 3: Divide and Conquer Edge Coloring
    def color_graph(cur_edges, d, color_start):
        if d == 0 or not cur_edges:
            return
        if d == 1:
            for u, v, eid in cur_edges:
                ans[eid] = color_start
            return

        if d % 2 == 1:
            # Find a perfect matching using random walk
            adj_L = [[] for _ in range(K)]
            for u, v, eid in cur_edges:
                adj_L[u].append((v, eid))

            match_L = [-1] * K
            match_R = [-1] * K

            for start_u in range(K):
                if match_L[start_u] != -1:
                    continue
                u = start_u
                while True:
                    v, eid = adj_L[u][random.randrange(d)]
                    w = match_R[v]
                    match_R[v] = u
                    match_L[u] = v
                    if w == -1:
                        break
                    match_L[w] = -1
                    u = w

            # Extract matching and reduce degree to d - 1
            needed = match_L
            u_matched = [False] * K
            remaining_edges = []
            matching_color = color_start + d - 1

            for u, v, eid in cur_edges:
                if not u_matched[u] and v == needed[u]:
                    u_matched[u] = True
                    ans[eid] = matching_color
                else:
                    remaining_edges.append((u, v, eid))

            color_graph(remaining_edges, d - 1, color_start)

        else:
            # d is even: Euler tour splitting into two (d/2)-regular graphs
            adj = [[] for _ in range(2 * K)]
            for u, v, eid in cur_edges:
                vr = v + K
                adj[u].append((vr, eid))
                adj[vr].append((u, eid))

            used = bytearray(total_edges_count)
            ptr = [0] * (2 * K)
            tour = []

            for start_node in range(2 * K):
                if ptr[start_node] < len(adj[start_node]):
                    stack = [start_node]
                    edge_stack = []
                    while stack:
                        u = stack[-1]
                        while ptr[u] < len(adj[u]) and used[adj[u][ptr[u]][1]]:
                            ptr[u] += 1
                        if ptr[u] < len(adj[u]):
                            vr, eid = adj[u][ptr[u]]
                            ptr[u] += 1
                            used[eid] = 1
                            stack.append(vr)
                            edge_stack.append(eid)
                        else:
                            stack.pop()
                            if edge_stack:
                                tour.append(edge_stack.pop())

            in_g1 = bytearray(total_edges_count)
            for idx, eid in enumerate(tour):
                if idx % 2 == 0:
                    in_g1[eid] = 1

            edges1 = []
            edges2 = []
            for u, v, eid in cur_edges:
                if in_g1[eid]:
                    edges1.append((u, v, eid))
                else:
                    edges2.append((u, v, eid))

            color_graph(edges1, d // 2, color_start)
            color_graph(edges2, d // 2, color_start + d // 2)

    color_graph(edges, Delta, 1)

    # Output results for the original m tests
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(ans[i]) for i in range(m)) + "\n")

if __name__ == '__main__':
    solve()
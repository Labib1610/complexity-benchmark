import sys

# Increase recursion depth for deep recursions
sys.setrecursionlimit(500000)

def solve():
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
    
    edges_u = [0] * m
    edges_v = [0] * m
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges_u[i] = u
        edges_v[i] = v
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    if Delta == 0:
        print("YES")
        print()
        return

    # Bin-pack left vertices into super-vertices
    super_L = [0] * (n_L + 1)
    cur_s = 0
    cur_deg = 0
    for u in range(1, n_L + 1):
        d = deg_L[u]
        if d == 0:
            continue
        if cur_deg + d > Delta:
            cur_s += 1
            cur_deg = 0
        super_L[u] = cur_s
        cur_deg += d
    num_s_L = cur_s + 1

    # Bin-pack right vertices into super-vertices
    super_R = [0] * (n_R + 1)
    cur_s = 0
    cur_deg = 0
    for v in range(1, n_R + 1):
        d = deg_R[v]
        if d == 0:
            continue
        if cur_deg + d > Delta:
            cur_s += 1
            cur_deg = 0
        super_R[v] = cur_s
        cur_deg += d
    num_s_R = cur_s + 1

    N_prime = max(num_s_L, num_s_R, 1)

    sdeg_L = [0] * N_prime
    sdeg_R = [0] * N_prime

    # Initial edge list: (u, v, orig_id)
    # u in [0, N_prime - 1], v in [0, N_prime - 1]
    edge_list = []
    for i in range(m):
        u = super_L[edges_u[i]]
        v = super_R[edges_v[i]]
        edge_list.append((u, v, i))
        sdeg_L[u] += 1
        sdeg_R[v] += 1

    defect_L = [Delta - sdeg_L[i] for i in range(N_prime)]
    defect_R = [Delta - sdeg_R[i] for i in range(N_prime)]

    pL = 0
    pR = 0
    while pL < N_prime and pR < N_prime:
        if defect_L[pL] == 0:
            pL += 1
            continue
        if defect_R[pR] == 0:
            pR += 1
            continue
        take = min(defect_L[pL], defect_R[pR])
        for _ in range(take):
            edge_list.append((pL, pR, -1))
        defect_L[pL] -= take
        defect_R[pR] -= take

    ans = [0] * m

    def hopcroft_karp(N, cur_edges):
        adj_L = [[] for _ in range(N)]
        for idx_e, (u, v, orig_id) in enumerate(cur_edges):
            adj_L[u].append((v, idx_e))
        
        pair_u = [-1] * N
        pair_v = [-1] * N
        dist = [-1] * N
        match_edge_idx = [-1] * N
        
        while True:
            queue = []
            for u in range(N):
                if pair_u[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = -1
            
            found = False
            head_q = 0
            while head_q < len(queue):
                u = queue[head_q]
                head_q += 1
                for v, idx_e in adj_L[u]:
                    pu = pair_v[v]
                    if pu != -1:
                        if dist[pu] == -1:
                            dist[pu] = dist[u] + 1
                            queue.append(pu)
                    else:
                        found = True
            
            if not found:
                break
                
            ptr = [0] * N
            def dfs(u):
                for i in range(ptr[u], len(adj_L[u])):
                    ptr[u] = i + 1
                    v, idx_e = adj_L[u][i]
                    pu = pair_v[v]
                    if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                        pair_u[u] = v
                        pair_v[v] = u
                        match_edge_idx[u] = idx_e
                        return True
                return False
                
            for u in range(N):
                if pair_u[u] == -1:
                    dfs(u)
                    
        matched_set = set(match_edge_idx)
        return matched_set

    def solve_rec(cur_edges, D, color_offset):
        if D == 0 or not cur_edges:
            return
        if D == 1:
            for u, v, orig_id in cur_edges:
                if orig_id != -1:
                    ans[orig_id] = color_offset + 1
            return
        
        if D % 2 == 1:
            matched_set = hopcroft_karp(N_prime, cur_edges)
            remaining_edges = []
            for idx_e, e in enumerate(cur_edges):
                if idx_e in matched_set:
                    if e[2] != -1:
                        ans[e[2]] = color_offset + D
                else:
                    remaining_edges.append(e)
            solve_rec(remaining_edges, D - 1, color_offset)
        else:
            total_V = 2 * N_prime
            adj = [[] for _ in range(total_V)]
            for idx_e, (u, v, orig_id) in enumerate(cur_edges):
                v_node = v + N_prime
                adj[u].append((v_node, idx_e))
                adj[v_node].append((u, idx_e))
            
            used = [False] * len(cur_edges)
            head = [0] * total_V
            
            tour = []
            for start_node in range(total_V):
                if head[start_node] < len(adj[start_node]):
                    curr_stack = [start_node]
                    edge_stack = []
                    while curr_stack:
                        u = curr_stack[-1]
                        while head[u] < len(adj[u]) and used[adj[u][head[u]][1]]:
                            head[u] += 1
                        if head[u] < len(adj[u]):
                            v, eid = adj[u][head[u]]
                            head[u] += 1
                            used[eid] = True
                            curr_stack.append(v)
                            edge_stack.append(eid)
                        else:
                            curr_stack.pop()
                            if edge_stack:
                                tour.append(edge_stack.pop())
            
            list1 = []
            list2 = []
            for i, eid in enumerate(tour):
                if i % 2 == 0:
                    list1.append(cur_edges[eid])
                else:
                    list2.append(cur_edges[eid])
            
            solve_rec(list1, D // 2, color_offset)
            solve_rec(list2, D // 2, color_offset + D // 2)

    solve_rec(edge_list, Delta, 0)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()
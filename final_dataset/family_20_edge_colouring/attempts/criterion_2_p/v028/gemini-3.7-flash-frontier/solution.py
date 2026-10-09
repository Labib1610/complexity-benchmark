import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nV = int(input_data[0])
    nD = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    deg_V = [0] * (nV + 1)
    deg_D = [0] * (nD + 1)
    
    edges_u = [0] * m
    edges_v = [0] * m
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges_u[i] = u
        edges_v[i] = v
        deg_V[u] += 1
        deg_D[v] += 1
        
    Delta = max(max(deg_V), max(deg_D))
    
    if Delta == 0:
        print("YES")
        print()
        return

    # Merge vertices in V
    L_map = [0] * (nV + 1)
    num_L = 0
    cur_deg = 0
    for u in range(1, nV + 1):
        if deg_V[u] == 0:
            continue
        if cur_deg + deg_V[u] > Delta:
            num_L += 1
            cur_deg = 0
        L_map[u] = num_L
        cur_deg += deg_V[u]
    num_L += 1

    # Merge vertices in D
    R_map = [0] * (nD + 1)
    num_R = 0
    cur_deg = 0
    for v in range(1, nD + 1):
        if deg_D[v] == 0:
            continue
        if cur_deg + deg_D[v] > Delta:
            num_R += 1
            cur_deg = 0
        R_map[v] = num_R
        cur_deg += deg_D[v]
    num_R += 1

    K = max(num_L, num_R)

    all_edge_u = [0] * m
    all_edge_v = [0] * m
    all_edge_id = list(range(m))

    cur_deg_L = [0] * K
    cur_deg_R = [0] * K

    for i in range(m):
        u = L_map[edges_u[i]]
        v = R_map[edges_v[i]]
        all_edge_u[i] = u
        all_edge_v[i] = v
        cur_deg_L[u] += 1
        cur_deg_R[v] += 1

    # Add dummy edges to make the graph Delta-regular
    pL = 0
    pR = 0
    dummy_count = 0
    while pL < K and pR < K:
        while pL < K and cur_deg_L[pL] == Delta:
            pL += 1
        while pR < K and cur_deg_R[pR] == Delta:
            pR += 1
        if pL < K and pR < K:
            add = min(Delta - cur_deg_L[pL], Delta - cur_deg_R[pR])
            for _ in range(add):
                all_edge_u.append(pL)
                all_edge_v.append(pR)
                all_edge_id.append(-1)
            cur_deg_L[pL] += add
            cur_deg_R[pR] += add

    ans = [0] * m
    total_edges = len(all_edge_u)
    
    # Hopcroft-Karp for finding 1-factor in d-regular bipartite graph
    def find_matching(edge_list):
        adj_L = [[] for _ in range(K)]
        for e in edge_list:
            u = all_edge_u[e]
            adj_L[u].append(e)

        pair_U = [-1] * K
        pair_V = [-1] * K
        
        # Greedy initialization
        for u in range(K):
            for e in adj_L[u]:
                v = all_edge_v[e]
                if pair_V[v] == -1:
                    pair_U[u] = e
                    pair_V[v] = e
                    break

        dist = [0] * K
        INF = 10**9

        while True:
            # BFS
            queue = []
            for u in range(K):
                if pair_U[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = INF
            
            dist_nil = INF
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                if dist[u] < dist_nil:
                    for e in adj_L[u]:
                        v = all_edge_v[e]
                        mv = pair_V[v]
                        if mv == -1:
                            dist_nil = dist[u] + 1
                        else:
                            nu = all_edge_u[mv]
                            if dist[nu] == INF:
                                dist[nu] = dist[u] + 1
                                queue.append(nu)

            if dist_nil == INF:
                break

            ptrs = [0] * K

            def dfs(u):
                while ptrs[u] < len(adj_L[u]):
                    e = adj_L[u][ptrs[u]]
                    ptrs[u] += 1
                    v = all_edge_v[e]
                    mv = pair_V[v]
                    if mv == -1 or (dist[all_edge_u[mv]] == dist[u] + 1 and dfs(all_edge_u[mv])):
                        pair_U[u] = e
                        pair_V[v] = e
                        return True
                dist[u] = INF
                return False

            for u in range(K):
                if pair_U[u] == -1:
                    dfs(u)

        matching = set()
        for u in range(K):
            if pair_U[u] != -1:
                matching.add(pair_U[u])
        return matching

    def decompose_euler(edge_list):
        adj = [[] for _ in range(2 * K)]
        for e in edge_list:
            u = all_edge_u[e]
            v = all_edge_v[e] + K
            adj[u].append((v, e))
            adj[v].append((u, e))

        used = [False] * len(all_edge_u)
        ptrs = [0] * (2 * K)
        set1 = []
        set2 = []

        for start_node in range(2 * K):
            if ptrs[start_node] >= len(adj[start_node]):
                continue

            stack = [(start_node, -1)]
            tour_edges = []

            while stack:
                curr, _ = stack[-1]
                while ptrs[curr] < len(adj[curr]) and used[adj[curr][ptrs[curr]][1]]:
                    ptrs[curr] += 1
                
                if ptrs[curr] < len(adj[curr]):
                    next_node, edge_idx = adj[curr][ptrs[curr]]
                    used[edge_idx] = True
                    ptrs[curr] += 1
                    stack.append((next_node, edge_idx))
                else:
                    _, edge_idx = stack.pop()
                    if edge_idx != -1:
                        tour_edges.append(edge_idx)

            for i, e in enumerate(tour_edges):
                if i % 2 == 0:
                    set1.append(e)
                else:
                    set2.append(e)

        return set1, set2

    def solve_rec(edge_list, d, color_offset):
        if d == 0 or not edge_list:
            return
        if d == 1:
            for e in edge_list:
                orig_id = all_edge_id[e]
                if orig_id != -1:
                    ans[orig_id] = color_offset
            return

        if d % 2 == 1:
            match_edges = find_matching(edge_list)
            rem_edges = []
            for e in edge_list:
                if e in match_edges:
                    orig_id = all_edge_id[e]
                    if orig_id != -1:
                        ans[orig_id] = color_offset
                else:
                    rem_edges.append(e)
            solve_rec(rem_edges, d - 1, color_offset + 1)
        else:
            set1, set2 = decompose_euler(edge_list)
            solve_rec(set1, d // 2, color_offset)
            solve_rec(set2, d // 2, color_offset + d // 2)

    solve_rec(list(range(total_edges)), Delta, 1)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()
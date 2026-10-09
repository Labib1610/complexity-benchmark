import sys

def main():
    sys.setrecursionlimit(500000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    orig_u = [0] * m
    orig_v = [0] * m
    deg_L = [0] * nL
    deg_R = [0] * nR
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        orig_u[i] = u
        orig_v[i] = v
        deg_L[u] += 1
        deg_R[v] += 1
        
    delta = max(max(deg_L), max(deg_R))
    if delta == 0:
        print("YES")
        print(" ".join(["1"] * m))
        return

    # Pack vertices into super-vertices of degree <= delta
    super_L = [-1] * nL
    num_super_L = 0
    cur_deg = 0
    for u in range(nL):
        if deg_L[u] == 0:
            continue
        if cur_deg + deg_L[u] > delta:
            num_super_L += 1
            cur_deg = 0
        super_L[u] = num_super_L
        cur_deg += deg_L[u]
    if cur_deg > 0:
        num_super_L += 1

    super_R = [-1] * nR
    num_super_R = 0
    cur_deg = 0
    for v in range(nR):
        if deg_R[v] == 0:
            continue
        if cur_deg + deg_R[v] > delta:
            num_super_R += 1
            cur_deg = 0
        super_R[v] = num_super_R
        cur_deg += deg_R[v]
    if cur_deg > 0:
        num_super_R += 1

    N = max(num_super_L, num_super_R, 1)

    # Compute degrees of super-vertices
    s_deg_L = [0] * N
    s_deg_R = [0] * N
    for i in range(m):
        s_deg_L[super_L[orig_u[i]]] += 1
        s_deg_R[super_R[orig_v[i]]] += 1

    edge_u = [0] * m
    edge_v = [0] * m
    for i in range(m):
        edge_u[i] = super_L[orig_u[i]]
        edge_v[i] = super_R[orig_v[i]]

    # Add dummy edges to make the bipartite graph delta-regular
    ptr_L = 0
    ptr_R = 0
    while ptr_L < N and ptr_R < N:
        rem_L = delta - s_deg_L[ptr_L]
        rem_R = delta - s_deg_R[ptr_R]
        if rem_L == 0:
            ptr_L += 1
            continue
        if rem_R == 0:
            ptr_R += 1
            continue
        add = min(rem_L, rem_R)
        for _ in range(add):
            edge_u.append(ptr_L)
            edge_v.append(ptr_R)
        s_deg_L[ptr_L] += add
        s_deg_R[ptr_R] += add

    total_edges = len(edge_u)
    ans = [0] * m

    in_M = [False] * total_edges
    used = [False] * total_edges

    def find_perfect_matching(edges_list):
        adj = [[] for _ in range(N)]
        for e in edges_list:
            adj[edge_u[e]].append((edge_v[e], e))

        match_L = [-1] * N
        match_R = [-1] * N
        edge_of_L = [-1] * N

        for u in range(N):
            for v, e in adj[u]:
                if match_R[v] == -1:
                    match_L[u] = v
                    match_R[v] = u
                    edge_of_L[u] = e
                    break

        dist = [-1] * N
        ptr = [0] * N

        def dfs(u):
            for i in range(ptr[u], len(adj[u])):
                ptr[u] = i + 1
                v, e = adj[u][i]
                next_u = match_R[v]
                if next_u == -1 or (dist[next_u] == dist[u] + 1 and dfs(next_u)):
                    match_L[u] = v
                    match_R[v] = u
                    edge_of_L[u] = e
                    return True
            return False

        while True:
            queue = []
            for u in range(N):
                if match_L[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = -1

            found = False
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v, e in adj[u]:
                    next_u = match_R[v]
                    if next_u == -1:
                        found = True
                    elif dist[next_u] == -1:
                        dist[next_u] = dist[u] + 1
                        queue.append(next_u)

            if not found:
                break

            for u in range(N):
                ptr[u] = 0
            for u in range(N):
                if match_L[u] == -1:
                    dfs(u)

        return [edge_of_L[u] for u in range(N)]

    def euler_split(edges_list):
        adj = [[] for _ in range(2 * N)]
        for e in edges_list:
            u = edge_u[e]
            v = edge_v[e] + N
            adj[u].append(e)
            adj[v].append(e)

        pos = [0] * (2 * N)
        E1 = []
        E2 = []

        for start_node in range(2 * N):
            if pos[start_node] >= len(adj[start_node]):
                continue

            stack_node = [start_node]
            stack_edge = []
            circuit = []

            while stack_node:
                u = stack_node[-1]
                while pos[u] < len(adj[u]) and used[adj[u][pos[u]]]:
                    pos[u] += 1
                if pos[u] < len(adj[u]):
                    e = adj[u][pos[u]]
                    used[e] = True
                    pos[u] += 1
                    u_orig = edge_u[e]
                    v_orig = edge_v[e] + N
                    next_node = v_orig if u == u_orig else u_orig
                    stack_node.append(next_node)
                    stack_edge.append(e)
                else:
                    stack_node.pop()
                    if stack_edge:
                        circuit.append(stack_edge.pop())

            for idx, e in enumerate(circuit):
                if idx % 2 == 0:
                    E1.append(e)
                else:
                    E2.append(e)

        return E1, E2

    def solve(edges_list, d, color_start):
        if d == 1:
            for e in edges_list:
                if e < m:
                    ans[e] = color_start
            return

        if d % 2 == 1:
            M = find_perfect_matching(edges_list)
            for e in M:
                in_M[e] = True
                if e < m:
                    ans[e] = color_start
            remaining = [e for e in edges_list if not in_M[e]]
            for e in M:
                in_M[e] = False
            solve(remaining, d - 1, color_start + 1)
        else:
            E1, E2 = euler_split(edges_list)
            solve(E1, d // 2, color_start)
            solve(E2, d // 2, color_start + d // 2)

    all_edges = list(range(total_edges))
    solve(all_edges, delta, 1)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    main()
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(k)]
    term_set = set(terminals)

    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w, i))

    # Identify connected components
    adj_full = [[] for _ in range(n)]
    for u, v, w, idx in edges:
        adj_full[u].append((v, w, idx))
        adj_full[v].append((u, w, idx))

    visited = [False] * n
    comp_list = []
    for i in range(n):
        if not visited[i]:
            comp = []
            q = [i]
            visited[i] = True
            for node in q:
                comp.append(node)
                for neighbor, _, _ in adj_full[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
            comp_list.append(comp)

    total_decoupled_edges = []
    total_cost = 0

    # Solve multiway cut for each component
    for comp in comp_list:
        comp_terms = [v for v in comp if v in term_set]
        if len(comp_terms) <= 1:
            continue

        comp_nodes = set(comp)
        node_map = {node: idx for idx, node in enumerate(comp)}
        inv_map = {idx: node for idx, node in enumerate(comp)}
        comp_n = len(comp)

        # Adjacency matrix for weights between nodes in this component
        # Also map edge indices
        comp_edges = []
        adj_matrix = [[0] * comp_n for _ in range(comp_n)]
        edge_orig = {}
        for u, v, w, idx in edges:
            if u in comp_nodes and v in comp_nodes:
                nu, nv = node_map[u], node_map[v]
                adj_matrix[nu][nv] += w
                adj_matrix[nv][nu] += w
                comp_edges.append((nu, nv, w, u, v))
                if (min(nu, nv), max(nu, nv)) not in edge_orig:
                    edge_orig[(min(nu, nv), max(nu, nv))] = []
                edge_orig[(min(nu, nv), max(nu, nv))].append((u, v, w))

        local_terms = [node_map[t] for t in comp_terms]
        local_k = len(local_terms)

        # Dinic's algorithm for min-cut
        def get_min_cut(source, sinks, n_v, cap_mat):
            # source is an int, sinks is a set/list
            # cap_mat is modified or we build flow network
            # build residual graph
            sink_set = set(sinks)
            # Source is source, sink is a virtual node n_v
            # total nodes: n_v + 1
            N_tot = n_v + 1
            virtual_sink = n_v

            head = [-1] * N_tot
            to = []
            nxt = []
            cap = []

            def add_edge(u, v, c):
                nxt.append(head[u])
                head[u] = len(to)
                to.append(v)
                cap.append(c)

                nxt.append(head[v])
                head[v] = len(to)
                to.append(u)
                cap.append(0)

            for i in range(n_v):
                for j in range(i + 1, n_v):
                    c = cap_mat[i][j]
                    if c > 0:
                        add_edge(i, j, c)
                        add_edge(j, i, c)

            for s in sink_set:
                add_edge(s, virtual_sink, float("inf"))

            # Dinic
            level = [-1] * N_tot

            def bfs():
                for i in range(N_tot):
                    level[i] = -1
                level[source] = 0
                q = [source]
                for u in q:
                    e = head[u]
                    while e != -1:
                        v = to[e]
                        if cap[e] > 0 and level[v] < 0:
                            level[v] = level[u] + 1
                            q.append(v)
                        e = nxt[e]
                return level[virtual_sink] >= 0

            cur = [0] * N_tot

            def dfs(u, flow):
                if u == virtual_sink or flow == 0:
                    return flow
                pushed = 0
                e = cur[u]
                while e != -1:
                    cur[u] = e
                    v = to[e]
                    if level[v] == level[u] + 1 and cap[e] > 0:
                        tr = dfs(v, min(flow, cap[e]))
                        if tr > 0:
                            cap[e] -= tr
                            cap[e ^ 1] += tr
                            pushed += tr
                            flow -= tr
                            if flow == 0:
                                break
                    e = nxt[e]
                return pushed

            max_flow = 0
            while bfs():
                for i in range(N_tot):
                    cur[i] = head[i]
                while True:
                    p = dfs(source, float("inf"))
                    if p == 0:
                        break
                    max_flow += p

            return max_flow

        # Lower bound function
        def compute_lb(assignment):
            # assignment is a list of length comp_n: terminal index (0..local_k-1) or -1
            # Contract nodes assigned to same terminal
            # Node indices for condensed graph: 0..local_k-1 for terminals, then other unassigned nodes
            # map each node to condensed index
            cond_map = [-1] * comp_n
            cond_n = local_k
            unassigned = []
            for i in range(comp_n):
                if assignment[i] != -1:
                    cond_map[i] = assignment[i]
                else:
                    cond_map[i] = cond_n
                    unassigned.append(cond_n)
                    cond_n += 1

            cond_cap = [[0] * cond_n for _ in range(cond_n)]
            for i in range(comp_n):
                for j in range(i + 1, comp_n):
                    c = adj_matrix[i][j]
                    if c > 0:
                        ci, cj = cond_map[i], cond_map[j]
                        if ci != cj:
                            cond_cap[ci][cj] += c
                            cond_cap[cj][ci] += c

            # Compute sum of mincuts for each terminal
            cut_sum = 0
            for t_idx in range(local_k):
                sinks = [j for j in range(local_k) if j != t_idx]
                mc = get_min_cut(t_idx, sinks, cond_n, cond_cap)
                cut_sum += mc

            return (cut_sum + 1) // 2

        # Branch and Bound
        # Initial assignment
        init_assignment = [-1] * comp_n
        for idx, t in enumerate(local_terms):
            init_assignment[t] = idx

        # Find an initial upper bound using isolation heuristic
        best_cost = float("inf")
        best_assignment = None

        # Isolation heuristic:
        # for each terminal, find min-cut to others, assign reachable nodes to that terminal
        # simple heuristic: assign each node to the terminal with maximum connectivity
        unassigned_nodes = [i for i in range(comp_n) if init_assignment[i] == -1]

        # Greedy initial solution
        greedy_assignment = list(init_assignment)
        for u in unassigned_nodes:
            # Pick terminal with max total weight to already assigned nodes of that terminal
            best_t = 0
            best_w = -1
            for t_idx in range(local_k):
                w_sum = sum(
                    adj_matrix[u][v]
                    for v in range(comp_n)
                    if greedy_assignment[v] == t_idx
                )
                if w_sum > best_w:
                    best_w = w_sum
                    best_t = t_idx
            greedy_assignment[u] = best_t

        def eval_cost(assignment):
            c = 0
            for i in range(comp_n):
                for j in range(i + 1, comp_n):
                    if assignment[i] != assignment[j]:
                        c += adj_matrix[i][j]
            return c

        best_cost = eval_cost(greedy_assignment)
        best_assignment = list(greedy_assignment)

        # Order unassigned nodes by degree / connectivity
        unassigned_nodes.sort(
            key=lambda u: sum(adj_matrix[u][v] for v in range(comp_n)),
            reverse=True,
        )

        def search(idx, current_assignment):
            nonlocal best_cost, best_assignment
            if idx == len(unassigned_nodes):
                c = eval_cost(current_assignment)
                if c < best_cost:
                    best_cost = c
                    best_assignment = list(current_assignment)
                return

            lb = compute_lb(current_assignment)
            if lb >= best_cost:
                return

            u = unassigned_nodes[idx]
            # Order choices for u by connection weight to terminals
            weights = []
            for t in range(local_k):
                w = sum(
                    adj_matrix[u][v]
                    for v in range(comp_n)
                    if current_assignment[v] == t
                )
                weights.append((w, t))
            weights.sort(reverse=True)

            for _, t in weights:
                current_assignment[u] = t
                search(idx + 1, current_assignment)
                current_assignment[u] = -1

        search(0, list(init_assignment))

        total_cost += best_cost
        # Collect cut edges
        for u, v, w, orig_u, orig_v in comp_edges:
            if best_assignment[u] != best_assignment[v]:
                total_decoupled_edges.append((orig_u + 1, orig_v + 1))

    if total_cost > B:
        print("NO")
    else:
        print("YES")
        print(len(total_decoupled_edges))
        for u, v in total_decoupled_edges:
            print(f"{u} {v}")


if __name__ == "__main__":
    solve()
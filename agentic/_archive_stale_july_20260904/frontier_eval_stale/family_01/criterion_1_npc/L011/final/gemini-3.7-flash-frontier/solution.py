import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve_2sat(n, var_map, clauses):
    # num_vars is len(var_map)
    # Literals: x_i is 2*i, ~x_i is 2*i + 1
    num_vars = len(var_map)
    num_nodes = 2 * num_vars
    adj = [[] for _ in range(num_nodes)]

    for u_lit, v_lit in clauses:
        # u_lit or v_lit  =>  ~u_lit -> v_lit and ~v_lit -> u_lit
        adj[u_lit ^ 1].append(v_lit)
        adj[v_lit ^ 1].append(u_lit)

    index = 0
    indices = [-1] * num_nodes
    lowlink = [-1] * num_nodes
    on_stack = [False] * num_nodes
    stack = []
    scc = [-1] * num_nodes
    scc_count = 0

    for i in range(num_nodes):
        if indices[i] == -1:
            # Iterative Tarjan to prevent recursion overhead
            call_stack = [(i, 0)]
            while call_stack:
                u, edge_idx = call_stack[-1]
                if edge_idx == 0:
                    indices[u] = lowlink[u] = index
                    index += 1
                    stack.append(u)
                    on_stack[u] = True

                advanced = False
                while edge_idx < len(adj[u]):
                    v = adj[u][edge_idx]
                    edge_idx += 1
                    call_stack[-1] = (u, edge_idx)
                    if indices[v] == -1:
                        call_stack.append((v, 0))
                        advanced = True
                        break
                    elif on_stack[v]:
                        if indices[v] < lowlink[u]:
                            lowlink[u] = indices[v]

                if advanced:
                    continue

                call_stack.pop()
                if call_stack:
                    p = call_stack[-1][0]
                    if lowlink[u] < lowlink[p]:
                        lowlink[p] = lowlink[u]

                if lowlink[u] == indices[u]:
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        scc[w] = scc_count
                        if w == u:
                            break
                    scc_count += 1

    for i in range(num_vars):
        if scc[2 * i] == scc[2 * i + 1]:
            return False
    return True


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)

    for i in range(n):
        adj[i] = list(set(adj[i]))

    def propagate(D):
        D = [set(d) for d in D]
        queue = [i for i in range(n) if len(D[i]) == 1]
        while queue:
            u = queue.pop()
            if len(D[u]) == 0:
                return None
            val = next(iter(D[u]))
            for v in adj[u]:
                if val in D[v]:
                    D[v].remove(val)
                    if len(D[v]) == 0:
                        return None
                    if len(D[v]) == 1:
                        queue.append(v)
        for d in D:
            if len(d) == 0:
                return None
        return D

    def is_satisfiable(D):
        D = propagate(D)
        if D is None:
            return False

        # Find vertex with |D[u]| == 3
        branch_u = -1
        max_deg = -1
        for i in range(n):
            if len(D[i]) == 3:
                if len(adj[i]) > max_deg:
                    max_deg = len(adj[i])
                    branch_u = i

        if branch_u != -1:
            for c in (1, 2, 3):
                D_next = [set(d) for d in D]
                D_next[branch_u] = {c}
                if is_satisfiable(D_next):
                    return True
            return False

        # All vertices have |D[i]| in {1, 2}
        var_map = {}
        var_domains = []
        for i in range(n):
            var_map[i] = len(var_map)
            var_domains.append(list(D[i]))

        clauses = []
        for i in range(n):
            dom = var_domains[i]
            if len(dom) == 1:
                # x_i is forced to be true (corresponds to dom[0])
                # Clause: (x_i or x_i) -> (2*var_map[i] or 2*var_map[i])
                lit = 2 * var_map[i]
                clauses.append((lit, lit))

        for u in range(n):
            for v in adj[u]:
                if u < v:
                    dom_u = var_domains[u]
                    dom_v = var_domains[v]
                    for cu_idx, cu in enumerate(dom_u):
                        for cv_idx, cv in enumerate(dom_v):
                            if cu == cv:
                                lit_u = 2 * var_map[u] + (1 if cu_idx == 0 else 0)
                                lit_v = 2 * var_map[v] + (1 if cv_idx == 0 else 0)
                                clauses.append((lit_u, lit_v))

        return solve_2sat(n, var_map, clauses)

    initial_D = [{1, 2, 3} for _ in range(n)]
    if not is_satisfiable(initial_D):
        print("NO")
        return

    current_D = initial_D
    result = []
    for i in range(n):
        for col in (1, 2, 3):
            if col in current_D[i]:
                temp_D = [set(d) for d in current_D]
                temp_D[i] = {col}
                if is_satisfiable(temp_D):
                    current_D = propagate(temp_D)
                    result.append(col)
                    break

    print("YES")
    print(*(result))


if __name__ == "__main__":
    solve()
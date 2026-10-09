import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

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
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    color_assignment = [0] * n  # 1, 2, 3 or 0 if unassigned

    def solve_2sat(curr_domains):
        # curr_domains: list of sets/lists of available colors for each vertex
        # unassigned vertices have domain size 1 or 2
        # We assign boolean variable x_i: True -> domain[i][0], False -> domain[i][1] (if size 2)
        # If size 1, x_i is fixed.
        
        # Variable mapping:
        # For each vertex v with len(curr_domains[v]) == 2:
        #   c0, c1 = curr_domains[v]
        #   x_v: True means c0, False means c1
        # For len == 1:
        #   c0 = curr_domains[v][0]
        #   x_v: True means c0, False is impossible
        
        num_vars = n
        # 2-SAT graph: 2 * n nodes (2*v for True, 2*v+1 for False)
        # Clause (A or B) => (~A -> B) and (~B -> A)
        two_sat_adj = [[] for _ in range(2 * num_vars)]
        
        def add_clause(lit1, lit2):
            # lit is signed: +v means True (2*v), -v means False (2*v+1)
            # lit1, lit2 are (v, bool_val)
            v1, val1 = lit1
            v2, val2 = lit2
            node1 = 2 * v1 if val1 else 2 * v1 + 1
            node2 = 2 * v2 if val2 else 2 * v2 + 1
            neg1 = 2 * v1 + 1 if val1 else 2 * v1
            neg2 = 2 * v2 + 1 if val2 else 2 * v2
            two_sat_adj[neg1].append(node2)
            two_sat_adj[neg2].append(node1)

        for v in range(n):
            dom = curr_domains[v]
            if len(dom) == 0:
                return False, None
            elif len(dom) == 1:
                # Must be True (representing dom[0])
                # Clause: (x_v or x_v)
                add_clause((v, True), (v, True))
            elif len(dom) == 2:
                pass  # Both are valid choices
            else:
                return False, None

        for u in range(n):
            for v in adj[u]:
                if u < v:
                    dom_u = curr_domains[u]
                    dom_v = curr_domains[v]
                    # Check all color collisions
                    for cu_idx, cu in enumerate(dom_u):
                        for cv_idx, cv in enumerate(dom_v):
                            if cu == cv:
                                # u cannot be cu AND v cannot be cv
                                # NOT (u == cu AND v == cv) <=> (u != cu OR v != cv)
                                val_u = (cu_idx == 0) # True means cu, False means not cu
                                val_v = (cv_idx == 0) # True means cv, False means not cv
                                add_clause((u, not val_u), (v, not val_v))

        # Tarjan's SCC
        n_nodes = 2 * num_vars
        dfn = [-1] * n_nodes
        low = [-1] * n_nodes
        scc = [-1] * n_nodes
        in_stack = [False] * n_nodes
        stack = []
        timer = 0
        scc_cnt = 0

        for i in range(n_nodes):
            if dfn[i] == -1:
                # Iterative Tarjan to avoid call stack issues
                call_stack = [(i, 0)]
                while call_stack:
                    u_node, edge_idx = call_stack[-1]
                    if edge_idx == 0:
                        timer += 1
                        dfn[u_node] = low[u_node] = timer
                        stack.append(u_node)
                        in_stack[u_node] = True
                    
                    advanced = False
                    while edge_idx < len(two_sat_adj[u_node]):
                        nxt = two_sat_adj[u_node][edge_idx]
                        edge_idx += 1
                        call_stack[-1] = (u_node, edge_idx)
                        if dfn[nxt] == -1:
                            call_stack.append((nxt, 0))
                            advanced = True
                            break
                        elif in_stack[nxt]:
                            low[u_node] = min(low[u_node], dfn[nxt])
                    
                    if advanced:
                        continue
                    
                    if low[u_node] == dfn[u_node]:
                        while True:
                            w = stack.pop()
                            in_stack[w] = False
                            scc[w] = scc_cnt
                            if w == u_node:
                                break
                        scc_cnt += 1
                    
                    call_stack.pop()
                    if call_stack:
                        parent, _ = call_stack[-1]
                        low[parent] = min(low[parent], low[u_node])

        res_colors = [0] * n
        for v in range(n):
            if scc[2 * v] == scc[2 * v + 1]:
                return False, None
            # In 2-SAT, x_v is True if scc[True] < scc[False]
            is_true = scc[2 * v] < scc[2 * v + 1]
            if is_true:
                res_colors[v] = curr_domains[v][0]
            else:
                res_colors[v] = curr_domains[v][1]

        return True, res_colors

    # Backtracking with domain propagation
    def search(domains):
        # Propagate size 1 domains
        domains = [list(d) for d in domains]
        changed = True
        while changed:
            changed = False
            for v in range(n):
                if len(domains[v]) == 0:
                    return False, None
                if len(domains[v]) == 1:
                    c = domains[v][0]
                    for neighbor in adj[v]:
                        if c in domains[neighbor]:
                            domains[neighbor].remove(c)
                            if len(domains[neighbor]) == 0:
                                return False, None
                            changed = True

        # Check if all domains have size <= 2
        all_le_2 = True
        for v in range(n):
            if len(domains[v]) > 2:
                all_le_2 = False
                break
        
        if all_le_2:
            return solve_2sat(domains)

        # Pick vertex with domain size 3 and maximum degree
        best_v = -1
        max_deg = -1
        for v in range(n):
            if len(domains[v]) == 3:
                deg = len(adj[v])
                if deg > max_deg:
                    max_deg = deg
                    best_v = v

        for c in [1, 2, 3]:
            new_domains = [list(d) for d in domains]
            new_domains[best_v] = [c]
            sat, res = search(new_domains)
            if sat:
                return True, res

        return False, None

    init_domains = [[1, 2, 3] for _ in range(n)]
    sat, res = search(init_domains)
    if sat:
        print("YES")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
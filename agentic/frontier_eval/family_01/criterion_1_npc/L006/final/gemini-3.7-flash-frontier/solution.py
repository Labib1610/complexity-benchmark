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
    
    # 2-SAT solver using Tarjan's SCC
    # Variables: 0 .. n-1
    # Literal x_i is 2*i, ~x_i is 2*i + 1
    def is_2sat_satisfiable(n_vars, clauses):
        num_literals = 2 * n_vars
        impl_graph = [[] for _ in range(num_literals)]
        for u, v in clauses:
            # u or v <=> ~u -> v and ~v -> u
            impl_graph[u ^ 1].append(v)
            impl_graph[v ^ 1].append(u)
        
        index = 0
        indices = [-1] * num_literals
        lowlink = [-1] * num_literals
        on_stack = [False] * num_literals
        stack = []
        scc_id = [-1] * num_literals
        current_scc = 0
        
        for i in range(num_literals):
            if indices[i] == -1:
                # Iterative Tarjan to avoid deep recursion overhead
                call_stack = [(i, 0)]
                while call_stack:
                    node, edge_idx = call_stack[-1]
                    if edge_idx == 0:
                        indices[node] = lowlink[node] = index
                        index += 1
                        stack.append(node)
                        on_stack[node] = True
                    
                    advanced = False
                    while edge_idx < len(impl_graph[node]):
                        nxt = impl_graph[node][edge_idx]
                        edge_idx += 1
                        call_stack[-1] = (node, edge_idx)
                        if indices[nxt] == -1:
                            call_stack.append((nxt, 0))
                            advanced = True
                            break
                        elif on_stack[nxt]:
                            lowlink[node] = min(lowlink[node], indices[nxt])
                    
                    if advanced:
                        continue
                    
                    if len(call_stack) > 1:
                        parent = call_stack[-2][0]
                        lowlink[parent] = min(lowlink[parent], lowlink[node])
                    
                    if lowlink[node] == indices[node]:
                        while True:
                            w = stack.pop()
                            on_stack[w] = False
                            scc_id[w] = current_scc
                            if w == node:
                                break
                        current_scc += 1
                    
                    call_stack.pop()

        for i in range(n_vars):
            if scc_id[2 * i] == scc_id[2 * i + 1] and scc_id[2 * i] != -1:
                return False
        return True

    def propagate(domains):
        # domains is a list of bitmasks: 1 for color 1, 2 for color 2, 4 for color 3
        # Returns updated domains, or None if contradiction
        domains = list(domains)
        q = [i for i in range(n) if bin(domains[i]).count('1') == 1]
        
        while q:
            u = q.pop()
            c = domains[u]
            for v in adj[u]:
                if domains[v] & c:
                    domains[v] &= ~c
                    if domains[v] == 0:
                        return None
                    if bin(domains[v]).count('1') == 1:
                        q.append(v)
        
        for i in range(n):
            if domains[i] == 0:
                return None
        return domains

    def check_3_colorable(domains):
        domains = propagate(domains)
        if domains is None:
            return False
        
        # Check if any vertex has 3 colors
        dom3 = [i for i in range(n) if bin(domains[i]).count('1') == 3]
        if not dom3:
            # All vertices have at most 2 colors. Formulate 2-SAT.
            clauses = []
            var_map = {}
            num_vars = 0
            for i in range(n):
                cnt = bin(domains[i]).count('1')
                if cnt == 2:
                    var_map[i] = num_vars
                    num_vars += 1
                elif cnt == 1:
                    pass
            
            for u in range(n):
                for v in adj[u]:
                    if u < v:
                        du, dv = domains[u], domains[v]
                        cnt_u, cnt_v = bin(du).count('1'), bin(dv).count('1')
                        
                        if cnt_u == 1 and cnt_v == 1:
                            if du == dv:
                                return False
                        elif cnt_u == 1 and cnt_v == 2:
                            cu = du
                            cols_v = [1 << k for k in range(3) if dv & (1 << k)]
                            var_v = var_map[v]
                            # if cols_v[0] == cu, v cannot be cols_v[0] (var_v must be True -> literal 2*var_v)
                            # if cols_v[1] == cu, v cannot be cols_v[1] (var_v must be False -> literal 2*var_v + 1)
                            if cols_v[0] == cu:
                                clauses.append((2 * var_v, 2 * var_v))
                            elif cols_v[1] == cu:
                                clauses.append((2 * var_v + 1, 2 * var_v + 1))
                        elif cnt_u == 2 and cnt_v == 1:
                            cv = dv
                            cols_u = [1 << k for k in range(3) if du & (1 << k)]
                            var_u = var_map[u]
                            if cols_u[0] == cv:
                                clauses.append((2 * var_u, 2 * var_u))
                            elif cols_u[1] == cv:
                                clauses.append((2 * var_u + 1, 2 * var_u + 1))
                        elif cnt_u == 2 and cnt_v == 2:
                            cols_u = [1 << k for k in range(3) if du & (1 << k)]
                            cols_v = [1 << k for k in range(3) if dv & (1 << k)]
                            var_u = var_map[u]
                            var_v = var_map[v]
                            # false means cols[0], true means cols[1]
                            for i_u, col_u in enumerate(cols_u):
                                for i_v, col_v in enumerate(cols_v):
                                    if col_u == col_v:
                                        lit_u = 2 * var_u + (1 if i_u == 0 else 0)
                                        lit_v = 2 * var_v + (1 if i_v == 0 else 0)
                                        clauses.append((lit_u, lit_v))
            
            return is_2sat_satisfiable(num_vars, clauses)

        # Pick vertex with domain size 3 having max neighbors with domain size 3
        best_u = max(dom3, key=lambda u: sum(1 for v in adj[u] if domains[v] == 7))
        
        for c in [1, 2, 4]:
            new_domains = list(domains)
            new_domains[best_u] = c
            if check_3_colorable(new_domains):
                return True
        return False

    initial_domains = [7] * n
    if not check_3_colorable(initial_domains):
        print("NO")
        return

    assignment = []
    current_domains = [7] * n

    for i in range(n):
        for c in [1, 2, 4]:
            if current_domains[i] & c:
                test_domains = list(current_domains)
                test_domains[i] = c
                if check_3_colorable(test_domains):
                    current_domains = propagate(test_domains)
                    assignment.append(1 if c == 1 else (2 if c == 2 else 3))
                    break

    print("YES")
    print(*(assignment))

solve()
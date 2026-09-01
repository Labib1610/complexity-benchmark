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
    adj_mask = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)

    # 2-SAT solver
    # Variable mapping: each vertex v has a domain D[v] (subset of {0, 1, 2})
    # If |D[v]| == 2, say D[v] = {c1, c2} with c1 < c2:
    # Boolean variable x_v: False -> c1, True -> c2.
    # If |D[v]| == 1, say D[v] = {c}: x_v is fixed.
    # If |D[v]| == 0: unsatisfiable.
    
    def solve_2sat(domains):
        # Build 2-SAT graph
        # 2*n nodes: 2*v is ~x_v, 2*v+1 is x_v
        # Let's map for each vertex:
        # dom[v] = list of allowed colors
        dom = [[] for _ in range(n)]
        for v in range(n):
            for c in range(3):
                if (domains[v] >> c) & 1:
                    dom[v].append(c)
            if len(dom[v]) == 0:
                return False
        
        # Build implication graph
        # For each vertex v:
        # If len(dom[v]) == 1:
        # x_v = False means choice 0. So x_v must be False: x_v -> ~x_v
        # If len(dom[v]) == 2:
        # False -> dom[v][0], True -> dom[v][1]
        
        # Total boolean variables: n
        # Literals: 2*v (negation of x_v), 2*v + 1 (x_v)
        num_vars = n
        adj_2sat = [[] for _ in range(2 * num_vars)]
        
        def add_clause(lit1, lit2):
            # (lit1 or lit2) <=> (~lit1 -> lit2) and (~lit2 -> lit1)
            adj_2sat[lit1 ^ 1].append(lit2)
            adj_2sat[lit2 ^ 1].append(lit1)

        for v in range(n):
            if len(dom[v]) == 1:
                # Must be dom[v][0], which corresponds to False (literal 2*v)
                # so (not x_v or not x_v)
                add_clause(2 * v, 2 * v)
            elif len(dom[v]) == 2:
                pass # variable can be False or True
            else:
                # Should not be called with domain size > 2
                pass

        for u in range(n):
            for v in adj[u]:
                if u < v:
                    # u and v cannot have the same color
                    for i_u, cu in enumerate(dom[u]):
                        for i_v, cv in enumerate(dom[v]):
                            if cu == cv:
                                # Not (var_u == i_u and var_v == i_v)
                                # i.e. (var_u != i_u or var_v != i_v)
                                lit_u = (2 * u + 1) if i_u == 0 else (2 * u) # not(var_u == i_u)
                                lit_v = (2 * v + 1) if i_v == 0 else (2 * v)
                                add_clause(lit_u, lit_v)

        # Kosaraju's algorithm or Tarjan's for SCC
        visited = [False] * (2 * num_vars)
        order = []
        for i in range(2 * num_vars):
            if not visited[i]:
                stack = [i]
                call_stack = [(i, 0)]
                visited[i] = True
                while call_stack:
                    curr, child_idx = call_stack.pop()
                    if child_idx < len(adj_2sat[curr]):
                        nxt = adj_2sat[curr][child_idx]
                        call_stack.append((curr, child_idx + 1))
                        if not visited[nxt]:
                            visited[nxt] = True
                            call_stack.append((nxt, 0))
                    else:
                        order.append(curr)

        # Transpose graph
        radj = [[] for _ in range(2 * num_vars)]
        for u_node in range(2 * num_vars):
            for v_node in adj_2sat[u_node]:
                radj[v_node].append(u_node)

        comp = [-1] * (2 * num_vars)
        c_id = 0
        for u_node in reversed(order):
            if comp[u_node] == -1:
                stack = [u_node]
                comp[u_node] = c_id
                while stack:
                    curr = stack.pop()
                    for nxt in radj[curr]:
                        if comp[nxt] == -1:
                            comp[nxt] = c_id
                            stack.append(nxt)
                c_id += 1

        for i in range(num_vars):
            if comp[2 * i] == comp[2 * i + 1]:
                return False
        return True

    def is_consistent(domains):
        # Forward check / 2-SAT / Branching
        # Find if any domain is empty
        for v in range(n):
            if domains[v] == 0:
                return False

        # Find vertex with domain size 3
        v_branch = -1
        max_deg = -1
        has_size_3 = False
        for v in range(n):
            size = bin(domains[v]).count('1')
            if size == 3:
                has_size_3 = True
                if len(adj[v]) > max_deg:
                    max_deg = len(adj[v])
                    v_branch = v

        if not has_size_3:
            return solve_2sat(domains)

        # Branch on v_branch
        for c in range(3):
            if (domains[v_branch] >> c) & 1:
                new_domains = list(domains)
                new_domains[v_branch] = 1 << c
                valid = True
                for neighbor in adj[v_branch]:
                    new_domains[neighbor] &= ~(1 << c)
                    if new_domains[neighbor] == 0:
                        valid = False
                        break
                if valid and is_consistent(new_domains):
                    return True
        return False

    # Check if a 3-coloring exists at all
    initial_domains = [7] * n
    # Quick self-loop check
    for i in range(n):
        if (adj_mask[i] >> i) & 1:
            print("NO")
            return

    if not is_consistent(initial_domains):
        print("NO")
        return

    # Find the lexicographically smallest assignment
    current_domains = [7] * n
    ans = [0] * n

    for v in range(n):
        for c in range(3):
            if (current_domains[v] >> c) & 1:
                test_domains = list(current_domains)
                test_domains[v] = 1 << c
                valid = True
                for neighbor in adj[v]:
                    test_domains[neighbor] &= ~(1 << c)
                    if test_domains[neighbor] == 0:
                        valid = False
                        break
                if valid and is_consistent(test_domains):
                    ans[v] = c + 1
                    current_domains = test_domains
                    break

    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()
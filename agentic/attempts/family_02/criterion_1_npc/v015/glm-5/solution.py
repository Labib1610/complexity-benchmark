import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT setup
    # Variables: 1..n, each can be True (1) or False (0)
    # Node indices: 2*x for x=True, 2*x+1 for x=False
    # x in 1..n -> nodes 2*x, 2*x+1
    # Total nodes: 2*(n+1)
    N = 2 * (n + 1)
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def var_node(var, is_true):
        return 2 * var + (0 if is_true else 1)
    
    def add_implication(u_var, u_val, v_var, v_val):
        u = var_node(u_var, u_val)
        v = var_node(v_var, v_val)
        adj[u].append(v)
        radj[v].append(u)
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        vars_req = []
        for lit in [l1, l2, l3]:
            var = abs(lit)
            val = lit > 0
            vars_req.append((var, val))
        
        # Interlock is satisfied if at least one requirement is met
        # (a OR b OR c) is equivalent to:
        # (!a -> b), (!a -> c), (!b -> a), (!b -> c), (!c -> a), (!c -> b)
        a, b, c = vars_req
        av, at = a
        bv, bt = b
        cv, ct = c
        
        add_implication(av, not at, bv, bt)
        add_implication(av, not at, cv, ct)
        add_implication(bv, not bt, av, at)
        add_implication(bv, not bt, cv, ct)
        add_implication(cv, not ct, av, at)
        add_implication(cv, not ct, bv, bt)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    current_comp = 0
    
    def dfs2(u, label):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = label
            for neighbor in radj[node]:
                if comp[neighbor] == -1:
                    stack.append(neighbor)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check satisfiability and assign values
    assignment = [False] * (n + 1)
    possible = True
    
    for var in range(1, n + 1):
        true_node = var_node(var, True)
        false_node = var_node(var, False)
        if comp[true_node] == comp[false_node]:
            possible = False
            break
        assignment[var] = comp[true_node] > comp[false_node]
    
    if not possible:
        print("NO")
    else:
        print("YES")
        result = [1 if assignment[i] else 0 for i in range(1, n + 1)]
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
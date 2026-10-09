import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # We'll have n original variables (1..n) and m auxiliary variables (n+1..n+m)
    # Each variable x_i is represented by two nodes: 2*i for False, 2*i+1 for True
    # For auxiliary variable y_j: 2*(n+j) for False, 2*(n+j)+1 for True
    
    num_vars = n + m
    N = 2 * num_vars
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]
    
    def add_imp(u, v):
        # u => v
        g[u].append(v)
        gr[v].append(u)
    
    def add_clause(lit1, lit2):
        # (lit1 OR lit2)
        # lit is (var_index, is_true)
        v1, t1 = lit1
        v2, t2 = lit2
        # ¬lit1 => lit2
        # ¬lit2 => lit1
        # node for (var, True) is 2*var+1, (var, False) is 2*var
        def node(var, val):
            return 2*var + (1 if val else 0)
        def neg_node(var, val):
            return 2*var + (0 if val else 1)
        add_imp(neg_node(v1, t1), node(v2, t2))
        add_imp(neg_node(v2, t2), node(v1, t1))
    
    # Read clauses
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        # Convert to literals: (var_index, is_true)
        def to_lit(l):
            var = abs(l) - 1  # 0-based
            val = l > 0
            return (var, val)
        a = to_lit(l1)
        b = to_lit(l2)
        c = to_lit(l3)
        clauses.append((a,b,c))
    
    # Add auxiliary variables and clauses
    for idx, (a,b,c) in enumerate(clauses):
        y = n + idx  # auxiliary variable index
        # (a OR y)
        add_clause(a, (y, True))
        # (b OR y)
        add_clause(b, (y, True))
        # (c OR ¬y)
        add_clause(c, (y, False))
    
    # Now solve 2-SAT using SCC (Kosaraju)
    visited = [False]*N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1]*N
    def dfs2(u, cid):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v, cid)
    
    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(num_vars):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [False]*num_vars
    for i in range(num_vars):
        # In Kosaraju, comp id order: if comp[2*i] > comp[2*i+1] then True
        assignment[i] = comp[2*i] > comp[2*i+1]
    
    # Output
    print("YES")
    print(" ".join('1' if assignment[i] else '0' for i in range(n)))

if __name__ == "__main__":
    solve()
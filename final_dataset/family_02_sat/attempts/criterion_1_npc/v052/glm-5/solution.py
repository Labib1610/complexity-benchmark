import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    interlocks = []
    for _ in range(m):
        deps = [int(next(it)) for _ in range(3)]
        interlocks.append(deps)
    
    # SAT problem with 3-SAT structure
    # Each interlock is a clause (x1 OR x2 OR x3) in terms of literals
    # Literal lookups
    # For variable i: i=True means engaged, i=False means isolated
    # Literal +x: x is True, Literal -x: x is False
    
    total_literals = 2 * n
    adj = [[] for _ in range(total_literals)]
    adj_rev = [[] for _ in range(total_literals)]
    
    # Helper: literal index for variable v (1-indexed)
    # Positive v (engaged): v-1 is var index, literal for True is 2*(v-1), False is 2*(v-1)+1
    # Literal representation:
    # For variable i (0-indexed): lit(2*i) = i is True, lit(2*i+1) = i is False
    
    def get_lit(var, is_true):
        # var is 1-indexed switch number
        idx = var - 1
        return 2 * idx if is_true else 2 * idx + 1
    
    # Build implication graph for 3-SAT
    # For each clause (a OR b OR c), it's equivalent to:
    # (not a => b) and (not a => c) and (not b => a) and (not b => c) and (not c => a) and (not c => b)
    # But standard reduction: for clause (a OR b OR c):
    # Add edges: not a -> b, not a -> c, not b -> a, not b -> c, not c -> a, not c -> b
    
    for inter in interlocks:
        lits = []
        for dep in inter:
            var = abs(dep)
            is_true = dep > 0
            lits.append(get_lit(var, is_true))
        
        a, b, c = lits
        
        # Implications: not a -> b, not a -> c
        adj[a ^ 1].append(b)
        adj[a ^ 1].append(c)
        # not b -> a, not b -> c
        adj[b ^ 1].append(a)
        adj[b ^ 1].append(c)
        # not c -> a, not c -> b
        adj[c ^ 1].append(a)
        adj[c ^ 1].append(b)
    
    # Build reverse graph
    for u in range(total_literals):
        for v in adj[u]:
            adj_rev[v].append(u)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * total_literals
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for u in range(total_literals):
        if not visited[u]:
            dfs1(u)
    
    comp = [-1] * total_literals
    current_comp = 0
    
    def dfs2(u, label):
        comp[u] = label
        for v in adj_rev[u]:
            if comp[v] == -1:
                dfs2(v, label)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check unsatisfiability: if x and not x are in same SCC
    for i in range(n):
        if comp[get_lit(i + 1, True)] == comp[get_lit(i + 1, False)]:
            print("NO")
            return
    
    # Assignment: use topological order of SCC (higher comp = earlier)
    assignment = [-1] * n  # -1: unassigned, 0: False (isolated), 1: True (engaged)
    
    for i in range(n):
        true_lit = get_lit(i + 1, True)
        false_lit = get_lit(i + 1, False)
        # SCC with higher topological order should be true
        if comp[true_lit] > comp[false_lit]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    # Verify the assignment
    for inter in interlocks:
        satisfied = False
        for dep in inter:
            var = abs(dep) - 1
            is_engaged = assignment[var] == 1
            if (dep > 0 and is_engaged) or (dep < 0 and not is_engaged):
                satisfied = True
                break
        if not satisfied:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
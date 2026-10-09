import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    # Variables: 0..n-1 are regulators, n..n+m-1 are auxiliary
    # Literal encoding: 2*var for positive, 2*var+1 for negative
    # Total variables: n + m
    
    total_vars = n + m
    adj = [[] for _ in range(2 * total_vars)]
    
    def neg(lit):
        return lit ^ 1
    
    def add_impl(u, v):
        adj[u].append(v)
    
    def add_clause_2(a, b):
        # (a or b)
        add_impl(neg(a), b)
        add_impl(neg(b), a)
    
    def add_clause_3(a, b, c):
        # (a or b or c) using auxiliary variable t
        t = 2 * (n + scenario_idx)
        add_clause_2(a, t)
        add_clause_2(b, neg(t))
        add_clause_2(t, c)
    
    scenario_idx = 0
    for _ in range(m):
        l1 = int(input_data[idx]); idx += 1
        l2 = int(input_data[idx]); idx += 1
        l3 = int(input_data[idx]); idx += 1
        
        def to_lit(x):
            var = abs(x) - 1
            if x > 0:
                return 2 * var  # positive
            else:
                return 2 * var + 1  # negative
        
        a = to_lit(l1)
        b = to_lit(l2)
        c = to_lit(l3)
        
        add_clause_3(a, b, c)
        scenario_idx += 1
    
    # Find SCCs using Tarjan's algorithm
    index_counter = [0]
    stack = []
    on_stack = [False] * (2 * total_vars)
    indices = [-1] * (2 * total_vars)
    lowlink = [0] * (2 * total_vars)
    scc_id = [-1] * (2 * total_vars)
    scc_count = [0]
    
    sys.setrecursionlimit(1000000)
    
    def strongconnect(v):
        indices[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in adj[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
        
        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc_id[w] = scc_count[0]
                if w == v:
                    break
            scc_count[0] += 1
    
    for v in range(2 * total_vars):
        if indices[v] == -1:
            strongconnect(v)
    
    # Check satisfiability
    for i in range(total_vars):
        if scc_id[2*i] == scc_id[2*i+1]:
            print("NO")
            return
    
    # Assign values
    result = [0] * n
    for i in range(n):
        # If positive literal has higher SCC (comes later in topological order), set to true
        if scc_id[2*i] > scc_id[2*i+1]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(' '.join(map(str, result)))

solve()
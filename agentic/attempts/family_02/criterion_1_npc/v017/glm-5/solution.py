import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph
    # Node indices: 0 to 2n-1
    # For variable i (1-indexed):
    #   i is true  -> node 2*(i-1)
    #   i is false -> node 2*(i-1) + 1
    # Implication: (a -> b) adds edge a -> b
    # Clause (a or b or c) is equivalent to:
    #   (not a -> b), (not a -> c)
    #   (not b -> a), (not b -> c)
    #   (not c -> a), (not c -> b)
    
    adj = [[] for _ in range(2 * n)]
    
    def get_node(var, is_true):
        # var is 1-indexed
        return 2 * (var - 1) + (0 if is_true else 1)
    
    def add_implication(u, v):
        adj[u].append(v)
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        # Parse literals
        vars_ = []
        signs = []
        for lit in [l1, l2, l3]:
            if lit > 0:
                vars_.append(lit)
                signs.append(True)
            else:
                vars_.append(-lit)
                signs.append(False)
        
        # Add implications for clause (a or b or c)
        # not a -> b, not a -> c
        # not b -> a, not b -> c
        # not c -> a, not c -> b
        a, b, c = 0, 1, 2
        for i in range(3):
            u = get_node(vars_[i], signs[i])  # literal i is true
            v1 = get_node(vars_[(i+1)%3], signs[(i+1)%3])
            v2 = get_node(vars_[(i+2)%3], signs[(i+2)%3])
            # not u -> v1 and not u -> v2
            add_implication(u ^ 1, v1)
            add_implication(u ^ 1, v2)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
            for i, v in enumerate(adj[node]):
                if i >= idx and not visited[v]:
                    stack.append((node, i + 1))
                    stack.append((v, 0))
                    break
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    # Reverse graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    visited = [False] * N
    comp = [-1] * N
    
    def dfs2(u, c):
        stack = [u]
        visited[u] = True
        comp[u] = c
        while stack:
            node = stack.pop()
            for v in radj[node]:
                if not visited[v]:
                    visited[v] = True
                    comp[v] = c
                    stack.append(v)
    
    cid = 0
    for u in reversed(order):
        if not visited[u]:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return
    
    # Construct assignment
    assignment = [0] * n
    for i in range(n):
        # If true node has higher component id, it's assigned true
        if comp[2*i] > comp[2*i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()
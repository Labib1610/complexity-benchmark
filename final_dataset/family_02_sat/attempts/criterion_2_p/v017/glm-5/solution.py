import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph
    # 2*n nodes: node 2*i is x_i = False (legacy), node 2*i+1 is x_i = True (upgraded)
    # For each policy (a, b), we need a OR b
    # Clause: (a OR b) => NOT a -> b and NOT b -> a
    # If a > 0: a means x_a = True (upgraded), NOT a means x_a = False (legacy)
    # If a < 0: a means x_{-a} = False (legacy), NOT a means x_{-a} = True (upgraded)
    
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        
        # Convert to node indices
        # For literal a: if a > 0, node is 2*(a-1)+1, else 2*(-a-1)
        def lit_to_node(lit):
            if lit > 0:
                return 2 * (lit - 1) + 1  # True
            else:
                return 2 * (-lit - 1)  # False
        
        def neg_node(node):
            return node ^ 1
        
        u = lit_to_node(a)
        v = lit_to_node(b)
        
        # NOT a -> b
        adj[neg_node(u)].append(v)
        radj[v].append(neg_node(u))
        
        # NOT b -> a
        adj[neg_node(v)].append(u)
        radj[u].append(neg_node(v))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(v):
        stack = [v]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            order.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    stack.append(nei)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    order.reverse()
    
    comp = [-1] * (2 * n)
    comp_id = 0
    
    def dfs2(v, cid):
        stack = [v]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = cid
            for nei in radj[node]:
                if comp[nei] == -1:
                    stack.append(nei)
    
    for v in order:
        if comp[v] == -1:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check if x_i and NOT x_i are in the same SCC
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: if comp[x_i] > comp[NOT x_i], then x_i = True
    # Because we want to assign True to the node that appears later in topological order
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i + 1] > comp[2 * i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
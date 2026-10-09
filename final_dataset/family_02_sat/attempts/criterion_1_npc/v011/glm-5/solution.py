import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Each clause is (a or b or c) where each literal is x or ~x
    # We use 1-indexed variables: positive = True, negative = False
    # Variable i corresponds to lens i being in focusing mode (1)
    
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # 2-SAT approach: convert 3-SAT to 2-SAT using implication graph
    # For clause (a or b or c), we add implications:
    # ~a -> b, ~a -> c
    # ~b -> a, ~b -> c
    # ~c -> a, ~c -> b
    
    # Variable encoding: 
    # For lens i, variable i is True if focusing (1), False if defocusing (0)
    # Literal encoding: positive literal l -> (|l|, True), negative -> (|l|, False)
    
    # We'll use 2n nodes: 2*i for False, 2*i+1 for True
    # Node 2*i represents x_i = False, 2*i+1 represents x_i = True
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def get_node(lit):
        idx = abs(lit) - 1  # 0-indexed
        if lit > 0:
            return 2 * idx + 1  # True
        else:
            return 2 * idx  # False
    
    def negate(node):
        return node ^ 1
    
    for l1, l2, l3 in clauses:
        a, b, c = get_node(l1), get_node(l2), get_node(l3)
        # ~a -> b, ~a -> c
        adj[negate(a)].append(b)
        adj[negate(a)].append(c)
        # ~b -> a, ~b -> c
        adj[negate(b)].append(a)
        adj[negate(b)].append(c)
        # ~c -> a, ~c -> b
        adj[negate(c)].append(a)
        adj[negate(c)].append(b)
        
        radj[b].append(negate(a))
        radj[c].append(negate(a))
        radj[a].append(negate(b))
        radj[c].append(negate(b))
        radj[a].append(negate(c))
        radj[b].append(negate(c))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, idx = stack[-1]
            if idx == 0:
                visited[node] = True
            if idx < len(adj[node]):
                nei = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nei]:
                    stack.append((nei, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * N
    comp = [-1] * N
    comp_id = 0
    
    def dfs2(v, cid):
        stack = [v]
        visited[v] = True
        comp[v] = cid
        while stack:
            node = stack.pop()
            for nei in radj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    comp[nei] = cid
                    stack.append(nei)
    
    for v in reversed(order):
        if not visited[v]:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check if x and ~x are in the same SCC
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * n
    for i in range(n):
        # If comp[True] > comp[False], then True is assigned
        if comp[2 * i + 1] > comp[2 * i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()
import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT: each dial i has two literals: i (true=1) and ~i (false=0)
    # Literal encoding: positive for i=1, negative for i=0
    # Variable i (1-indexed): literal i means dial i = 1, literal -i means dial i = 0
    
    # For each audit (a, b, c), at least one must be satisfied
    # Clause: (a OR b OR c)
    # Convert to 2-SAT: (a OR b OR c) = (a OR x) AND (NOT x OR b) AND (NOT x OR c) for some x
    # We'll use a helper variable for each audit
    
    # Total variables: n (dials) + m (helper variables)
    # Helper variable k (0-indexed) corresponds to variable n+1+k (1-indexed)
    
    clauses = []
    helper_base = n + 1  # 1-indexed variable number for first helper
    
    for k in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        # Audit: at least one of a, b, c must be satisfied
        # Introduce helper variable h = helper_base + k
        h = helper_base + k
        # (a OR b OR c) becomes:
        # (a OR h) AND (-h OR b) AND (-h OR c)
        clauses.append((a, h))
        clauses.append((-h, b))
        clauses.append((-h, c))
    
    total_vars = n + m
    
    # Build implication graph
    # For each clause (x OR y), add edges: ~x -> y and ~y -> x
    adj = [[] for _ in range(2 * total_vars + 1)]
    
    def lit_to_node(lit):
        # lit is signed integer, positive means true, negative means false
        # node index: 2*var for false, 2*var+1 for true (var is 1-indexed)
        var = abs(lit)
        if lit > 0:
            return 2 * var + 1
        else:
            return 2 * var
    
    for (x, y) in clauses:
        # ~x -> y
        adj[lit_to_node(-x)].append(lit_to_node(y))
        # ~y -> x
        adj[lit_to_node(-y)].append(lit_to_node(x))
    
    # Kosaraju's algorithm for SCC
    num_nodes = 2 * total_vars + 1
    visited = [False] * num_nodes
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                nei = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[nei]:
                    stack.append((nei, 0))
            else:
                stack.pop()
                order.append(node)
    
    for v in range(num_nodes):
        if v >= 2 and not visited[v]:
            dfs1(v)
    
    # Reverse graph
    radj = [[] for _ in range(num_nodes)]
    for v in range(num_nodes):
        for u in adj[v]:
            radj[u].append(v)
    
    visited = [False] * num_nodes
    comp = [-1] * num_nodes
    comp_id = 0
    
    def dfs2(v, cid):
        stack = [v]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                comp[node] = cid
                for nei in radj[node]:
                    if not visited[nei]:
                        stack.append(nei)
                        break
                else:
                    stack.pop()
            else:
                stack.pop()
    
    for v in reversed(order):
        if v >= 2 and not visited[v]:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check for contradiction: x and ~x in same component
    for i in range(1, total_vars + 1):
        if comp[2*i] == comp[2*i + 1]:
            print("NO")
            return
    
    # Assign values
    assignment = [False] * (total_vars + 1)
    # Process components in reverse topological order (higher comp_id first)
    for i in range(1, total_vars + 1):
        if comp[2*i] > comp[2*i + 1]:
            assignment[i] = False
        else:
            assignment[i] = True
    
    # Extract dial states
    result = []
    for i in range(1, n + 1):
        result.append(1 if assignment[i] else 0)
    
    print("YES")
    print(" ".join(map(str, result)))

solve()
import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT
    # Variable i: 2*i = True (activated), 2*i+1 = False (suppressed)
    # For gene i (1-indexed): node 2*(i-1) = activated, node 2*(i-1)+1 = suppressed
    # Total nodes: 2*n
    N = 2 * n
    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]
    
    def get_node(gene, state):
        # gene: 1-indexed
        # state: 1 for activated, 0 for suppressed
        return 2 * (gene - 1) + (1 - state)
    
    def negate(node):
        return node ^ 1
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        # Each clause is (a OR b OR c)
        # Convert to CNF: (a OR b OR c) = (a OR (b OR c))
        # = (!a -> (b OR c)) = (!a -> b) OR (!a -> c)
        # = (!a -> b) AND (!a -> c)
        # Similarly for b and c
        
        reqs = [l1, l2, l3]
        nodes = []
        for req in reqs:
            gene = abs(req)
            if req > 0:
                state = 1  # activated
            else:
                state = 0  # suppressed
            nodes.append(get_node(gene, state))
        
        a, b, c = nodes
        
        # (!a -> b) and (!a -> c)
        adj[negate(a)].append(b)
        adj_rev[b].append(negate(a))
        adj[negate(a)].append(c)
        adj_rev[c].append(negate(a))
        
        # (!b -> a) and (!b -> c)
        adj[negate(b)].append(a)
        adj_rev[a].append(negate(b))
        adj[negate(b)].append(c)
        adj_rev[c].append(negate(b))
        
        # (!c -> a) and (!c -> b)
        adj[negate(c)].append(a)
        adj_rev[a].append(negate(c))
        adj[negate(c)].append(b)
        adj_rev[b].append(negate(c))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
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
    
    visited = [False] * N
    comp = [-1] * N
    comp_id = 0
    
    def dfs2(v, cid):
        stack = [v]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                comp[node] = cid
                for neighbor in adj_rev[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    for v in reversed(order):
        if not visited[v]:
            dfs2(v, comp_id)
            comp_id += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * n
    for i in range(n):
        # If comp[2*i] > comp[2*i+1], then 2*i comes later in topological order
        # which means we should set it to True (activated)
        if comp[2*i] > comp[2*i+1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
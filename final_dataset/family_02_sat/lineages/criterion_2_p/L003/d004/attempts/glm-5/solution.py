import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Protocol triggers halt iff both probes generate deviation warning.
        # Probe v generates warning if:
        #   v > 0 and microservice |v| is in Secondary (0)
        #   v < 0 and microservice |v| is in Primary (1)
        # We need to prevent both warnings simultaneously.
        # So we add implication: if first probe warns, second must not warn.
        
        # Map: variable index i (1-based) -> node 2*(i-1) for Primary, 2*(i-1)+1 for Secondary
        # Node represents "microservice i is in Environment E"
        # Primary=1, Secondary=0.
        
        def get_node(var):
            idx = abs(var) - 1
            if var > 0:
                return 2 * idx + 1  # var>0 warns if Secondary, so this node is "Secondary"
            else:
                return 2 * idx      # var<0 warns if Primary, so this node is "Primary"
        
        u = get_node(l1)  # node representing "first probe warns"
        v = get_node(l2)  # node representing "second probe warns"
        
        # Implication: u -> !v
        # !v is the opposite environment for the same microservice
        adj[u].append(v ^ 1)
        # Implication: v -> !u
        adj[v].append(u ^ 1)
    
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
            for i in range(idx, len(adj[node])):
                v = adj[node][i]
                if not visited[v]:
                    stack.append((node, i + 1))
                    stack.append((v, 0))
                    break
            else:
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    # Build reverse graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    comp = [-1] * N
    cid = 0
    
    def dfs2(u, c):
        stack = [u]
        comp[u] = c
        while stack:
            node = stack.pop()
            for v in radj[node]:
                if comp[v] == -1:
                    comp[v] = c
                    stack.append(v)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check satisfiability
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Construct assignment
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] > comp[2 * i + 1]:
            assignment[i] = 1
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
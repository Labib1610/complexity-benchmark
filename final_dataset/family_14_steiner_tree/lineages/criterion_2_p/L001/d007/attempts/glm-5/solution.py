import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = [0] * (n + 1)
    for _ in range(t):
        node = int(next(it))
        critical[node] = 1
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for j in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, j))
        adj[v].append((u, w, j))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_edge_idx = [-1] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, idx in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_idx[v] = idx
                parent_edge_weight[v] = w
                stack.append(v)
    
    # Process in reverse order (bottom-up)
    # dp0[v]: min cost for subtree of v, v is active, no active ancestor
    # dp1[v]: min cost for subtree of v, v is active, has active ancestor
    # dp2[v]: min cost for subtree of v, v is inactive, no active ancestor
    # dp3[v]: min cost for subtree of v, v is inactive, has active ancestor
    
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    dp3 = [0] * (n + 1)
    
    INF = float('inf')
    
    for u in reversed(order):
        if critical[u]:
            dp2[u] = INF
            dp3[u] = INF
        else:
            dp0[u] = INF
            dp1[u] = INF
        
        # Accumulate children contributions
        for v, w, idx in adj[u]:
            if v == parent[u]:
                continue
            # dp0: u active, no active ancestor -> v must have no active ancestor
            # If v active: dp0[u] += dp0[v] + w (edge cost)
            # If v inactive: dp0[u] += dp2[v]
            # Take min
            if dp0[u] < INF:
                val_active = dp0[v] + w if dp0[v] < INF else INF
                val_inactive = dp2[v]
                dp0[u] += min(val_active, val_inactive)
            
            # dp1: u active, has active ancestor -> v can have or not have active ancestor
            # If v active: min(dp0[v], dp1[v]) + w
            # If v inactive: min(dp2[v], dp3[v])
            if dp1[u] < INF:
                val_active = min(dp0[v], dp1[v]) + w if min(dp0[v], dp1[v]) < INF else INF
                val_inactive = min(dp2[v], dp3[v])
                dp1[u] += min(val_active, val_inactive)
            
            # dp2: u inactive, no active ancestor -> v must have no active ancestor
            # v must be inactive (since u is inactive and no active ancestor)
            if dp2[u] < INF:
                dp2[u] += dp2[v]
            
            # dp3: u inactive, has active ancestor -> v can have active ancestor
            # If v active: dp1[v] + w
            # If v inactive: dp3[v]
            if dp3[u] < INF:
                val_active = dp1[v] + w if dp1[v] < INF else INF
                val_inactive = dp3[v]
                dp3[u] += min(val_active, val_inactive)
    
    # Root: no active ancestor
    # dp0[1]: root active, no active ancestor -> valid (I=1)
    # dp2[1]: root inactive, no active ancestor -> valid (I=1)
    result = min(dp0[1], dp2[1])
    print(result)

solve()
import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    is_primary = [False] * (n + 1)
    for i in range(t):
        p = int(input_data[idx]); idx += 1
        is_primary[p] = True
    
    adj = [[] for _ in range(n + 1)]
    total_weight = 0
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        total_weight += w
    
    # Iterative DFS
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for u, w in adj[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append(u)
    
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    
    for v in reversed(order):
        if is_primary[v]:
            dp0[v] = -float('inf')
        else:
            dp0[v] = 0
        dp1[v] = 0
        
        for u, w in adj[v]:
            if u != parent[v]:
                # u is child of v
                # If v is not activated: edge (v,u) is cut regardless of u
                # If v is activated: edge (v,u) is cut only if u is not activated
                if is_primary[v]:
                    dp0[v] = -float('inf')
                else:
                    dp0[v] += max(dp0[u], dp1[u]) + w
                
                dp1[v] += max(dp0[u] + w, dp1[u])
    
    result = total_weight - dp1[1]
    print(result)

solve()
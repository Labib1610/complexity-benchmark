import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    R = int(input[idx]); idx += 1
    S = int(input[idx]); idx += 1
    P = int(input[idx]); idx += 1
    
    mandated = [False] * (R + 1)
    for _ in range(P):
        v = int(input[idx]); idx += 1
        mandated[v] = True
    
    adj = [[] for _ in range(R + 1)]
    for _ in range(S):
        u = int(input[idx]); idx += 1
        v = int(input[idx]); idx += 1
        w = int(input[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    INF = float('inf')
    dp0 = [0] * (R + 1)
    dp1 = [0] * (R + 1)
    dp2 = [0] * (R + 1)
    dp3 = [0] * (R + 1)
    
    parent = [0] * (R + 1)
    order = []
    stack = [1]
    visited = [False] * (R + 1)
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)
    
    for u in reversed(order):
        if mandated[u]:
            dp0[u] = INF
            dp1[u] = INF
            dp2[u] = INF
            dp3[u] = INF
        else:
            dp0[u] = 0
            dp1[u] = INF
            dp2[u] = INF
            dp3[u] = INF
        
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            
            new_dp0 = dp0[u] + dp0[v]
            new_dp1 = min(dp0[u] + dp1[v], dp1[u] + dp0[v])
            new_dp2 = min(dp0[u] + dp2[v], dp2[u] + dp0[v], dp1[u] + dp1[v])
            new_dp3 = min(dp0[u] + dp3[v], dp3[u] + dp0[v], dp1[u] + dp2[v], dp2[u] + dp1[v])
            
            dp0[u] = new_dp0
            dp1[u] = new_dp1
            dp2[u] = new_dp2
            dp3[u] = new_dp3
        
        if mandated[u]:
            dp1[u] = min(dp1[u], dp0[u])
            dp2[u] = min(dp2[u], dp1[u])
            dp3[u] = min(dp3[u], dp2[u])
        else:
            dp1[u] = min(dp1[u], dp0[u] + w)
            dp2[u] = min(dp2[u], dp1[u] + w)
            dp3[u] = min(dp3[u], dp2[u] + w)
    
    print(dp1[1])

solve()
import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    critical = [False] * (n + 1)
    for _ in range(t):
        node = int(data[idx]); idx += 1
        critical[node] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    total_cost = 0
    visited = [False] * (n + 1)
    
    def dfs(u, p):
        nonlocal total_cost
        visited[u] = True
        cnt = 1 if critical[u] else 0
        for v, w in adj[u]:
            if v == p:
                continue
            if not visited[v]:
                sub = dfs(v, u)
                if sub > 0:
                    total_cost += w
                    cnt += sub
        return cnt
    
    # Start from any critical node (or any node if t=0, but t>=1)
    start = 1
    while start <= n and not critical[start]:
        start += 1
    
    dfs(start, 0)
    
    print(total_cost)

solve()
import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    is_T = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        is_T[v] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_T[i]:
            cnt[i] = 1
    
    for u in reversed(order):
        if parent[u] != 0:
            cnt[parent[u]] += cnt[u]
    
    total = 0
    for u in range(2, n + 1):
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_weight[u]
    
    print(total)

solve()
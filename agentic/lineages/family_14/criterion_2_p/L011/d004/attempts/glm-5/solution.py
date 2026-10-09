import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    required = [False] * (n + 1)
    for i in range(t):
        required[int(input_data[idx])] = True
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Find a required node as root
    root = 1
    for i in range(1, n + 1):
        if required[i]:
            root = i
            break
    
    # Iterative DFS
    parent = [0] * (n + 1)
    parent_edge = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    stack = [root]
    visited[root] = True
    parent[root] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        if required[i]:
            cnt[i] = 1
    
    # Process in reverse order (children before parents)
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            cnt[p] += cnt[u]
    
    ans = 0
    for u in range(1, n + 1):
        if u == root:
            continue
        if 0 < cnt[u] < t:
            ans += parent_edge[u]
    
    print(ans)

solve()
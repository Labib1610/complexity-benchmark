import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    critical = [False] * (n + 1)
    for i in range(t):
        c = int(input_data[idx]); idx += 1
        critical[c] = True
    
    adj = defaultdict(list)
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Iterative DFS
    parent = [0] * (n + 1)
    parent_edge = [0] * (n + 1)  # weight of edge to parent
    order = []
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = w
                stack.append(v)
    
    # cnt[u] = number of critical nodes in subtree rooted at u
    cnt = [0] * (n + 1)
    for u in reversed(order):
        cnt[u] = 1 if critical[u] else 0
        for v, w in adj[u]:
            if v != parent[u]:
                cnt[u] += cnt[v]
    
    # Edge (u, parent[u]) is included if cnt[u] > 0 and cnt[u] < t
    total = 0
    for u in range(2, n + 1):
        if 0 < cnt[u] < t:
            total += parent_edge[u]
    
    print(total)

solve()
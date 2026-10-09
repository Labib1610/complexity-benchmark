import sys
from sys import setrecursionlimit

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
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    # Find a critical node to root
    root = 1
    for i in range(1, n + 1):
        if critical[i]:
            root = i
            break
    
    parent_edge = [None] * (n + 1)  # (edge_index, weight)
    order = []
    stack = [root]
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    visited[root] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, e in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = (e, w)
                stack.append(v)
    
    # Count critical nodes in subtree
    cnt = [0] * (n + 1)
    for u in order:
        if critical[u]:
            cnt[u] = 1
    
    for u in reversed(order):
        if parent[u] != 0:
            cnt[parent[u]] += cnt[u]
    
    # Sum edges that are on path between critical nodes
    total = 0
    for u in range(1, n + 1):
        if u == root:
            continue
        if parent_edge[u] is not None:
            c = cnt[u]
            if c > 0 and c < t:
                total += parent_edge[u][1]
    
    print(total)

solve()
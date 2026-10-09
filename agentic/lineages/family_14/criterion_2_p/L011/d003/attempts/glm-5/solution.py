import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    is_terminal = [False] * (n + 1)
    for i in range(t):
        v = int(input_data[idx]); idx += 1
        is_terminal[v] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Iterative DFS to compute subtree terminal counts
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)  # edge index connecting to parent
    order = []
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w, ei in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = ei
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        if is_terminal[i]:
            cnt[i] = 1
    
    for u in reversed(order):
        if parent[u] != 0:
            cnt[parent[u]] += cnt[u]
    
    total = 0
    for i in range(1, n + 1):
        if parent[i] != 0:
            c = cnt[i]
            if 1 <= c <= t - 1:
                total += edges[parent_edge[i]][2]
    
    print(total)

solve()
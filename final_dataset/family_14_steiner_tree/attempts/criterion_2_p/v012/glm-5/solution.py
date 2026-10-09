import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    priority = [False] * (n + 1)
    for _ in range(t):
        p = int(input_data[idx]); idx += 1
        priority[p] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    setrecursionlimit(1 << 25)
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    
    stack = [(1, 0, 0, 0)]
    while stack:
        u, p, w, state = stack.pop()
        if state == 0:
            visited[u] = True
            parent[u] = p
            parent_weight[u] = w
            order.append(u)
            stack.append((u, p, w, 1))
            for v, vw in adj[u]:
                if not visited[v]:
                    stack.append((v, u, vw, 0))
        else:
            for v, vw in adj[u]:
                if v != p and parent[v] == u:
                    if priority[v]:
                        priority[u] = True
    
    total_cost = 0
    for u in order:
        if u != 1 and priority[u]:
            total_cost += parent_weight[u]
    
    print(total_cost)

solve()
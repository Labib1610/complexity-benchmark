import sys
from sys import setrecursionlimit

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    vital = [False] * (n + 1)
    for _ in range(t):
        v = int(data[idx]); idx += 1
        vital[v] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    
    for i in range(len(order)):
        u = order[i]
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                order.append(v)
    
    marked = [False] * (n + 1)
    for i in range(1, n + 1):
        if vital[i]:
            marked[i] = True
    
    for i in range(len(order) - 1, 0, -1):
        u = order[i]
        p = parent[u]
        if marked[u] and p != 0:
            marked[p] = True
    
    total = 0
    for i in range(len(order) - 1, 0, -1):
        u = order[i]
        if marked[u]:
            total += parent_weight[u]
    
    print(total)

solve()
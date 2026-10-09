import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = []
    is_target = [False] * (n + 1)
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        targets.append(x)
        is_target[x] = True
    
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
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [targets[0]]
    parent[targets[0]] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    marked = [False] * (n + 1)
    for x in targets:
        marked[x] = True
    
    for u in reversed(order):
        if marked[u] and parent[u] > 0:
            marked[parent[u]] = True
    
    total = 0
    for u in range(1, n + 1):
        if marked[u] and parent[u] > 0:
            total += parent_weight[u]
    
    print(total)

solve()
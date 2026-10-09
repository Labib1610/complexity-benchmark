import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    is_qc = [False] * (n + 1)
    for _ in range(t):
        v = int(input_data[idx]); idx += 1
        is_qc[v] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    setrecursionlimit(1 << 25)
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    qc_count = [0] * (n + 1)
    for i in range(n, 0, -1):
        u = order[i - 1]
        if is_qc[u]:
            qc_count[u] += 1
        p = parent[u]
        if p != -1:
            qc_count[p] += qc_count[u]
    
    total = 0
    for i in range(2, n + 1):
        if 0 < qc_count[i] < t:
            total += parent_weight[i]
    
    print(total)

solve()
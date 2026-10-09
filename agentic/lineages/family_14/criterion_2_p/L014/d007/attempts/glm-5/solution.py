import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    is_key = [False] * (n + 1)
    for _ in range(t):
        u = int(next(it))
        is_key[u] = True
        
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v, w))
        
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    depth = [0] * (n + 1)
    order = []
    
    stack = [(1, 0, -1, 0)]
    while stack:
        u, p, pe, d = stack.pop()
        parent[u] = p
        parent_edge[u] = pe
        depth[u] = d
        order.append(u)
        for v, eid in adj[u]:
            if v != p:
                stack.append((v, u, eid, d + 1))
                
    cnt = [1 if is_key[u] else 0 for u in range(n + 1)]
    for u in reversed(order):
        if parent[u] != 0:
            cnt[parent[u]] += cnt[u]
            
    ans = 0
    for u in range(2, n + 1):
        if 0 < cnt[u] < t:
            ans += edges[parent_edge[u]][2]
            
    print(ans)

setrecursionlimit(1 << 25)
solve()
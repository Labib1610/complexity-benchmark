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
    
    is_spore = [False] * (n + 1)
    for _ in range(t):
        u = int(next(it))
        is_spore[u] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    setrecursionlimit(max(300000, n + 100))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [(1, 0, 0)]
    
    while stack:
        u, p, pw = stack.pop()
        parent[u] = p
        parent_weight[u] = pw
        order.append(u)
        for v, w in adj[u]:
            if v != p:
                stack.append((v, u, w))
    
    cnt = [1 if is_spore[u] else 0 for u in range(n + 1)]
    
    for u in reversed(order):
        if u != 1:
            cnt[parent[u]] += cnt[u]
    
    ans = 0
    for u in range(2, n + 1):
        if 0 < cnt[u] < t:
            ans += parent_weight[u]
    
    print(ans)

solve()
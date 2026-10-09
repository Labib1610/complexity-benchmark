import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    required = [False] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    need = [False] * (n + 1)
    for i in range(1, n + 1):
        need[i] = required[i]
    
    for u in reversed(order):
        if u == 1:
            continue
        if need[u]:
            need[parent[u]] = True
    
    total_cost = 0
    for u in range(2, n + 1):
        if need[u]:
            total_cost += parent_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()
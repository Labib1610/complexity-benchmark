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
    
    contaminated = [False] * (n + 1)
    for _ in range(t):
        v = int(next(it))
        contaminated[v] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_edge_idx = [-1] * (n + 1)
    depth = [0] * (n + 1)
    
    stack = [1]
    parent[1] = 0
    order = [1]
    
    while stack:
        u = stack.pop()
        for v, w, idx in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_idx[v] = idx
                depth[v] = depth[u] + 1
                stack.append(v)
                order.append(v)
    
    count = [0] * (n + 1)
    for v in range(1, n + 1):
        if contaminated[v]:
            count[v] = 1
    
    for v in reversed(order):
        if v != 1:
            p = parent[v]
            count[p] += count[v]
    
    total_cost = 0
    for v in range(2, n + 1):
        if count[v] > 0 and count[v] < t:
            idx = parent_edge_idx[v]
            u, vx, w = edges[idx]
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()
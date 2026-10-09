import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    key_holders = [int(next(it)) for _ in range(t)]
    is_key = [False] * (n + 1)
    for k in key_holders:
        is_key[k] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    depth[1] = 0
    
    # BFS/DFS to build parent pointers and depth
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                order.append(v)
    
    # Process in reverse order (bottom-up)
    need = [False] * (n + 1)
    for k in key_holders:
        need[k] = True
    
    total_cost = 0
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        if need[u]:
            total_cost += parent_weight[u]
            need[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()
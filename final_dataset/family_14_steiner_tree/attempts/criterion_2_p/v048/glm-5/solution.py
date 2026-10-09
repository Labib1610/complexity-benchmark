import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    priority = [False] * (n + 1)
    for _ in range(t):
        priority[int(next(it))] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # BFS to find parent and depth for LCA
    parent = [0] * (n + 1)
    parent_edge = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    depth[1] = 0
    
    for u in order:
        for v, w, idx in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge[v] = idx
                depth[v] = depth[u] + 1
                order.append(v)
    
    # Process nodes from leaves to root
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        if priority[i]:
            cnt[i] = 1
    
    total_weight = 0
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        if cnt[u] >= 2:
            edge_idx = parent_edge[u]
            w = edges[edge_idx][2]
            total_weight += w
            cnt[u] = 0
        cnt[p] += cnt[u]
    
    print(total_weight)

if __name__ == "__main__":
    solve()
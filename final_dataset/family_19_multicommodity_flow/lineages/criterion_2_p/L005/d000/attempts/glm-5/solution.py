import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i + m))  # reverse edge index
    
    # Build flow network with scaled capacities
    # We need to check if max flow >= d
    # Use Dinic's algorithm with scaling
    
    # Create capacity array
    cap_arr = [0] * (2 * m)
    for i, (u, v, c) in enumerate(edges):
        cap_arr[i] = c
        cap_arr[i + m] = 0
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs(limit):
        for i in range(n + 1):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, idx in adj[u]:
                if level[v] == -1 and cap_arr[idx] >= limit:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1
    
    def dfs(u, flow, limit):
        if u == t:
            return flow
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            v, idx = adj[u][i]
            if level[v] == level[u] + 1 and cap_arr[idx] >= limit:
                pushed = dfs(v, min(flow, cap_arr[idx]), limit)
                if pushed > 0:
                    cap_arr[idx] -= pushed
                    cap_arr[idx ^ 1] += pushed
                    return pushed
        return 0
    
    flow = 0
    limit = 1
    while limit <= d:
        limit <<= 1
    limit >>= 1
    
    while limit > 0:
        while bfs(limit):
            ptr = [0] * (n + 1)
            while True:
                pushed = dfs(s, d - flow, limit)
                if pushed == 0:
                    break
                flow += pushed
                if flow >= d:
                    break
            if flow >= d:
                break
        limit >>= 1
        if flow >= d:
            break
    
    if flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i in range(m):
        # The flow on edge i is original_cap - cap_arr[i]
        # But we need to output the actual flow value
        # cap_arr[i] is remaining capacity, so flow = original_cap - cap_arr[i]
        # But we modified cap_arr during algorithm
        # Actually, flow on edge i = cap_arr[i ^ 1] (the reverse edge capacity)
        result.append(str(cap_arr[i + m]))
    print(" ".join(result))

solve()
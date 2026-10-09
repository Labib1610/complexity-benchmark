import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
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
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        edges.append((u, v, c))
    
    # Build graph for max flow
    # Node indices: 0 to n-1 (0-indexed)
    s0 = s - 1
    t0 = t - 1
    
    # Edge structure: to, rev, cap
    graph = [[] for _ in range(n)]
    edge_info = []  # (from, idx_in_graph)
    
    for u, v, c in edges:
        u0 = u - 1
        v0 = v - 1
        idx_u = len(graph[u0])
        idx_v = len(graph[v0])
        graph[u0].append([v0, idx_v, c])
        graph[v0].append([u0, idx_u, 0])
        edge_info.append((u0, idx_u))
    
    def bfs(level):
        level[:] = [-1] * n
        q = deque([s0])
        level[s0] = 0
        while q:
            u = q.popleft()
            for v, rev, cap in graph[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
    
    def dfs(u, f, level, ptr):
        if u == t0:
            return f
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            v, rev, cap = graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(f, cap), level, ptr)
                if pushed > 0:
                    graph[u][i][2] -= pushed
                    graph[v][rev][2] += pushed
                    return pushed
        return 0
    
    flow = 0
    level = [-1] * n
    while True:
        bfs(level)
        if level[t0] == -1:
            break
        ptr = [0] * n
        while True:
            pushed = dfs(s0, d - flow, level, ptr)
            if pushed == 0:
                break
            flow += pushed
            if flow == d:
                break
        if flow == d:
            break
    
    if flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for u0, idx in edge_info:
        original_cap = 0
        # Find original capacity from edges list
        # edges and edge_info are in same order
        edge_idx = len(result)
        u, v, c = edges[edge_idx]
        # Current capacity remaining is the residual capacity
        # Flow on edge = original_cap - residual_cap
        residual = graph[u0][idx][2]
        flow_on_edge = c - residual
        result.append(str(flow_on_edge))
    print(" ".join(result))

if __name__ == "__main__":
    solve()
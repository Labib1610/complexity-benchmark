import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = []
    target_set = set()
    for i in range(t):
        v = int(input_data[idx]); idx += 1
        targets.append(v)
        target_set.add(v)
    
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Build MST using Kruskal's
    edges.sort()
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    adj = [[] for _ in range(n + 1)]
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))
    
    # Binary lifting for LCA
    LOG = 20
    up = [[0] * (n + 1) for _ in range(LOG)]
    max_edge = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    
    # Iterative DFS
    visited = [False] * (n + 1)
    dfs_order = []
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, 0, 0, 0)]  # node, parent, weight_to_parent, state
        visited[start] = True
        up[0][start] = start
        max_edge[0][start] = 0
        depth[start] = 0
        while stack:
            node, par, w, state = stack.pop()
            if state == 0:
                dfs_order.append(node)
                stack.append((node, par, w, 1))
                for nb, nw in adj[node]:
                    if nb != par and not visited[nb]:
                        visited[nb] = True
                        up[0][nb] = node
                        max_edge[0][nb] = nw
                        depth[nb] = depth[node] + 1
                        stack.append((nb, node, nw, 0))
    
    for i in range(1, LOG):
        for j in range(1, n + 1):
            up[i][j] = up[i-1][up[i-1][j]]
            max_edge[i][j] = max(max_edge[i-1][j], max_edge[i-1][up[i-1][j]])
    
    def get_max_edge(u, v):
        if u == v:
            return 0
        result = 0
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if diff & (1 << i):
                result = max(result, max_edge[i][u])
                u = up[i][u]
        if u == v:
            return result
        for i in range(LOG - 1, -1, -1):
            if up[i][u] != up[i][v]:
                result = max(result, max_edge[i][u], max_edge[i][v])
                u = up[i][u]
                v = up[i][v]
        result = max(result, max_edge[0][u], max_edge[0][v])
        return result
    
    # Sort targets by DFS order
    pos = [0] * (n + 1)
    for i, node in enumerate(dfs_order):
        pos[node] = i
    
    sorted_targets = sorted(targets, key=lambda x: pos[x])
    
    total = 0
    for i in range(t):
        u = sorted_targets[i]
        v = sorted_targets[(i + 1) % t]
        total += get_max_edge(u, v)
    
    print(total // 2)

solve()
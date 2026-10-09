import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    critical = [False] * (n + 1)
    for _ in range(t):
        c = int(data[idx]); idx += 1
        critical[c] = True

    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    LOG = 0
    while (1 << LOG) < n:
        LOG += 1
    if LOG < 1:
        LOG = 1

    parent = [[0] * (n + 1) for _ in range(LOG)]
    max_edge = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)

    root = 1
    stack = [(root, 0, 0)]
    parent[0][root] = 0
    max_edge[0][root] = 0
    depth[root] = 0

    while stack:
        node, p, w = stack.pop()
        for v, wt in adj[node]:
            if v != p:
                parent[0][v] = node
                max_edge[0][v] = wt
                depth[v] = depth[node] + 1
                stack.append((v, node, wt))

    for i in range(1, LOG):
        for j in range(1, n + 1):
            p = parent[i-1][j]
            if p != 0:
                parent[i][j] = parent[i-1][p]
                max_edge[i][j] = max(max_edge[i-1][j], max_edge[i-1][p])
            else:
                parent[i][j] = 0
                max_edge[i][j] = max_edge[i-1][j]

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
                u = parent[i][u]
        if u == v:
            return result
        for i in range(LOG - 1, -1, -1):
            if parent[i][u] != parent[i][v]:
                result = max(result, max_edge[i][u], max_edge[i][v])
                u = parent[i][u]
                v = parent[i][v]
        result = max(result, max_edge[0][u], max_edge[0][v])
        return result

    # Kruskal-like: process edges in increasing weight, add if it connects two critical components
    edges.sort(key=lambda x: x[2])

    comp = list(range(n + 1))
    def find(x):
        while comp[x] != x:
            comp[x] = comp[comp[x]]
            x = comp[x]
        return x

    total = 0
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            comp[ru] = rv

    # Now find the minimal subtree connecting all critical nodes
    # This is the minimal Steiner tree on a tree, which is the union of paths
    # between consecutive critical nodes in DFS order
    # But we need to be careful: the minimal subtree is the union of paths
    # from each critical node to the LCA of all critical nodes

    # Find all critical nodes
    crit_nodes = [i for i in range(1, n + 1) if critical[i]]

    # The minimal subtree connecting all critical nodes is the union of paths
    # We can compute it by taking all critical nodes and finding the minimal
    # subtree that spans them. On a tree, this is equivalent to:
    # Sort critical nodes by DFS order, then for each consecutive pair,
    # add the path between them. But we need to avoid double counting.

    # Alternative: The minimal subtree is the union of paths from each critical
    # node to the "center" of all critical nodes. But a simpler approach:
    # The minimal subtree edges are exactly those edges that lie on some path
    # between two critical nodes.

    # We can use the property: an edge (u, v) where v is child of u is in the
    # minimal subtree iff the subtree rooted at v contains at least one but
    # not all critical nodes.

    # Let's compute for each node, the number of critical nodes in its subtree
    crit_count = [0] * (n + 1)
    for c in crit_nodes:
        crit_count[c] = 1

    # Process in reverse BFS/DFS order (post-order)
    # We can use the depth to process in decreasing order
    nodes_by_depth = sorted(range(1, n + 1), key=lambda x: -depth[x])
    for node in nodes_by_depth:
        p = parent[0][node]
        if p != 0:
            crit_count[p] += crit_count[node]

    total = 0
    for u, v, w in edges:
        # Determine which is parent and which is child
        if depth[u] > depth[v]:
            child = u
        else:
            child = v
        # Edge is in minimal subtree iff 0 < crit_count[child] < t
        if 0 < crit_count[child] < t:
            total += w

    print(total)

solve()
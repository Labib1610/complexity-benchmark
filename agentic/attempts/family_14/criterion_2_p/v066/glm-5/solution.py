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
    
    is_telemetry = [0] * (n + 1)
    for _ in range(t):
        u = int(next(it))
        is_telemetry[u] = 1
    
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
    parent_edge_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    # BFS to setup parent and depth
    q = [1]
    parent[1] = 0
    while q:
        u = q.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_weight[v] = w
                depth[v] = depth[u] + 1
                q.append(v)
    
    # DSU for LCA
    dsu = list(range(n + 1))
    
    def find(x):
        while dsu[x] != x:
            dsu[x] = dsu[dsu[x]]
            x = dsu[x]
        return x
    
    # Tarjan's LCA offline
    queries = [[] for _ in range(n + 1)]
    lca_result = [0] * (n + 1)
    # We need LCA for all pairs of telemetry nodes
    # But we only need sum of weights on paths
    # Using Tarjan's algorithm to compute LCA for all pairs
    
    # Collect all pairs
    tele_nodes = [i for i in range(1, n + 1) if is_telemetry[i]]
    k = len(tele_nodes)
    pair_count = 0
    # We'll process pairs in Tarjan's
    for i in range(k):
        for j in range(i + 1, k):
            u = tele_nodes[i]
            v = tele_nodes[j]
            queries[u].append((v, pair_count))
            queries[v].append((u, pair_count))
            pair_count += 1
    
    lca_answers = [0] * pair_count
    visited = [False] * (n + 1)
    ancestor = list(range(n + 1))
    
    # Tarjan's DFS
    stack = [(1, 0, 0)]  # node, state (0=enter, 1=exit), parent
    while stack:
        u, state, p = stack.pop()
        if state == 0:
            visited[u] = True
            ancestor[find(u)] = u
            stack.append((u, 1, p))
            # Push children
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, 0, u))
        else:
            # Process queries
            for v, idx in queries[u]:
                if visited[v]:
                    lca_answers[idx] = ancestor[find(v)]
            # Union with parent
            if p != 0:
                dsu[u] = p
                find(u)
    
    # Compute sum of weights on path between all pairs
    # We need prefix sums from root
    dist_from_root = [0] * (n + 1)
    q = [1]
    while q:
        u = q.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                dist_from_root[v] = dist_from_root[u] + w
                q.append(v)
    
    total_sum = 0
    for idx in range(pair_count):
        u = tele_nodes[0]  # dummy, need to get actual u, v
        # Actually we need to track which pair corresponds to which index
        pass
    
    # Better approach: compute sum of weights for each pair
    # We have lca_answers for each pair index
    # Let's map pair index to (u, v)
    pair_uv = []
    for i in range(k):
        for j in range(i + 1, k):
            pair_uv.append((tele_nodes[i], tele_nodes[j]))
    
    total_sum = 0
    for idx in range(pair_count):
        u, v = pair_uv[idx]
        lca = lca_answers[idx]
        path_weight = dist_from_root[u] + dist_from_root[v] - 2 * dist_from_root[lca]
        total_sum += path_weight
    
    # The answer is total_sum / (k-1) * 2 / 2 = total_sum / (k-1)
    # Wait, no. The sum of all pairwise distances = (k-1) * (sum of edge weights in Steiner tree)
    # So answer = total_sum / (k-1)
    if k <= 1:
        print(0)
    else:
        print(total_sum // (k - 1))

if __name__ == "__main__":
    solve()
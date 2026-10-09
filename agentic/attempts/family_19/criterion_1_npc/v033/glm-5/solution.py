import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    products = []
    for _ in range(k):
        s = int(data[idx]); idx += 1
        t = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        products.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))

    # Build a single commodity flow network:
    # Node 0: super source
    # Nodes 1..n: hubs
    # Node n+1: super sink
    # For each product i: super source -> s_i with capacity d_i
    # For each product i: t_i -> super sink with capacity d_i
    # For each lane: u -> v with capacity cap (shared)
    total_nodes = n + 2
    source = 0
    sink = n + 1

    graph = [[] for _ in range(total_nodes)]
    edge_list = []  # (to, cap, rev_index)

    def add_edge(fr, to, cap):
        graph[fr].append((to, cap, len(edge_list)))
        edge_list.append((to, cap, len(graph[to])))
        graph[to].append((fr, 0, len(edge_list)))
        edge_list.append((fr, 0, len(graph[fr]) - 1))

    for i, (s, t, d) in enumerate(products):
        add_edge(source, s, d)
        add_edge(t, sink, d)

    lane_edge_indices = []
    for u, v, cap in edges:
        idx_edge = len(edge_list)
        add_edge(u, v, cap)
        lane_edge_indices.append(idx_edge)

    # Dinic's max flow
    def bfs():
        level = [-1] * total_nodes
        level[source] = 0
        q = deque([source])
        while q:
            v = q.popleft()
            for to, cap, eid in graph[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level

    def dfs(v, f, level, it):
        if v == sink:
            return f
        while it[v] < len(graph[v]):
            to, cap, eid = graph[v][it[v]]
            if cap > 0 and level[v] < level[to]:
                ret = dfs(to, min(f, cap), level, it)
                if ret > 0:
                    # Update capacities
                    graph[v][it[v]] = (to, cap - ret, eid)
                    rev_idx = edge_list[eid][2]
                    rev_to, rev_cap, rev_eid = graph[to][rev_idx]
                    graph[to][rev_idx] = (rev_to, rev_cap + ret, rev_eid)
                    return ret
            it[v] += 1
        return 0

    total_demand = sum(d for _, _, d in products)
    flow = 0
    while True:
        level = bfs()
        if level[sink] < 0:
            break
        it = [0] * total_nodes
        while True:
            f = dfs(source, float('inf'), level, it)
            if f == 0:
                break
            flow += f

    if flow < total_demand:
        print("NO")
        return

    print("YES")
    # Extract per-product flows by decomposing the flow on each lane
    # For each lane, we have the total flow. We need to split it among products.
    # We do this by running a flow decomposition from each product's source to its sink
    # using the residual graph restricted to the product's source-sink pair.

    # Actually, we can extract per-product flows by sending flow along paths
    # for each product using the residual capacities of the original lane edges.
    # But the residual graph includes reverse edges too.

    # Simpler approach: For each product, find paths from s_i to t_i in the
    # current residual graph and push flow, recording how much of each lane is used.
    # But we need to be careful: the residual graph has reverse edges for lanes
    # and for the super source/sink edges.

    # Let's build a residual graph representation that we can query.
    # We already have `graph` and `edge_list` representing the residual graph.

    # For each product i, we want to route d_i units from s_i to t_i.
    # We can use the residual edges (including reverse lane edges) to find paths.
    # The flow on a lane for product i is the amount we push forward on that lane
    # minus the amount we push backward (on reverse edges).

    # Let's create a copy of the residual graph for decomposition.
    # Actually, we can decompose directly.

    # We'll track per-product per-lane flow.
    product_flows = [[0] * m for _ in range(k)]

    # Build adjacency for residual graph with mutable capacities
    # We need to be able to traverse and update.
    # Let's use the existing graph structure but we need to handle reverse edges properly.

    # For decomposition, we process each product:
    for i, (s, t, d) in enumerate(products):
        remaining = d
        while remaining > 0:
            # BFS/DFS to find a path from s to t in residual graph
            # We need to avoid using the super source/sink edges.
            # The residual graph includes:
            # - forward lane edges (capacity > 0)
            # - reverse lane edges (capacity > 0, meaning we can "undo" flow)
            # - super source -> s_i edges (but we start at s_i, so we don't use these)
            # - t_i -> super sink edges (but we end at t_i, so we don't use these)
            # - reverse edges of super source -> s_j (from s_j to super source, capacity = flow used)
            # - reverse edges of t_j -> super sink (from super sink to t_j, capacity = flow used)
            # We should avoid nodes 0 and n+1 (super source/sink) in our paths.

            parent = [-1] * total_nodes
            parent_edge = [-1] * total_nodes
            visited = [False] * total_nodes
            visited[s] = True
            q = deque([s])
            found = False
            while q and not found:
                v = q.popleft()
                for eid in range(len(graph[v])):
                    to, cap, _ = graph[v][eid]
                    if cap > 0 and not visited[to] and to != source and to != sink:
                        visited[to] = True
                        parent[to] = v
                        parent_edge[to] = eid
                        if to == t:
                            found = True
                            break
                        q.append(to)

            if not found:
                # Should not happen if total flow equals demand
                break

            # Find bottleneck
            path = []
            v = t
            bottleneck = remaining
            while v != s:
                p = parent[v]
                eid = parent_edge[v]
                cap = graph[p][eid][1]
                bottleneck = min(bottleneck, cap)
                path.append((p, eid, v))
                v = p
            path.reverse()

            # Update residual graph and record product flows
            for p, eid, v in path:
                to, cap, _ = graph[p][eid]
                graph[p][eid] = (to, cap - bottleneck, eid)
                # Reverse edge
                rev_idx = edge_list[eid][2]
                rev_to, rev_cap, rev_eid = graph[to][rev_idx]
                graph[to][rev_idx] = (rev_to, rev_cap + bottleneck, rev_eid)

                # Check if this edge corresponds to a lane
                # Lane edges have even indices in edge_list (since we add them in pairs)
                # and their index is stored in lane_edge_indices
                # The forward lane edge index is in lane_edge_indices
                # The reverse lane edge index is lane_edge_indices[j] + 1
                if eid in lane_edge_indices_set:
                    j = lane_edge_index_map[eid]
                    product_flows[i][j] += bottleneck
                elif eid in reverse_lane_edge_indices_set:
                    j = reverse_lane_edge_index_map[eid]
                    product_flows[i][j] -= bottleneck

            remaining -= bottleneck

    for i in range(k):
        print(' '.join(map(str, product_flows[i])))

# Precompute sets for fast lookup
lane_edge_indices_set = set()
lane_edge_index_map = {}
reverse_lane_edge_indices_set = set()
reverse_lane_edge_index_map = {}

# We need to set these after reading edges, so restructure
def solve2():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    products = []
    for _ in range(k):
        s = int(data[idx]); idx += 1
        t = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        products.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))

    total_nodes = n + 2
    source = 0
    sink = n + 1

    graph = [[] for _ in range(total_nodes)]
    edge_list = []

    def add_edge(fr, to, cap):
        graph[fr].append((to, cap, len(edge_list)))
        edge_list.append((to, cap, len(graph[to])))
        graph[to].append((fr, 0, len(edge_list)))
        edge_list.append((fr, 0, len(graph[fr]) - 1))

    for i, (s, t, d) in enumerate(products):
        add_edge(source, s, d)
        add_edge(t, sink, d)

    lane_edge_indices = []
    for u, v, cap in edges:
        idx_edge = len(edge_list)
        add_edge(u, v, cap)
        lane_edge_indices.append(idx_edge)

    lane_edge_indices_set = set(lane_edge_indices)
    lane_edge_index_map = {eid: j for j, eid in enumerate(lane_edge_indices)}
    reverse_lane_edge_indices_set = set(eid + 1 for eid in lane_edge_indices)
    reverse_lane_edge_index_map = {eid + 1: j for j, eid in enumerate(lane_edge_indices)}

    # Dinic's max flow
    def bfs():
        level = [-1] * total_nodes
        level[source] = 0
        q = deque([source])
        while q:
            v = q.popleft()
            for to, cap, eid in graph[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)
        return level

    def dfs(v, f, level, it):
        if v == sink:
            return f
        while it[v] < len(graph[v]):
            to, cap, eid = graph[v][it[v]]
            if cap > 0 and level[v] < level[to]:
                ret = dfs(to, min(f, cap), level, it)
                if ret > 0:
                    graph[v][it[v]] = (to, cap - ret, eid)
                    rev_idx = edge_list[eid][2]
                    rev_to, rev_cap, rev_eid = graph[to][rev_idx]
                    graph[to][rev_idx] = (rev_to, rev_cap + ret, rev_eid)
                    return ret
            it[v] += 1
        return 0

    total_demand = sum(d for _, _, d in products)
    flow = 0
    while True:
        level = bfs()
        if level[sink] < 0:
            break
        it = [0] * total_nodes
        while True:
            f = dfs(source, float('inf'), level, it)
            if f == 0:
                break
            flow += f

    if flow < total_demand:
        print("NO")
        return

    print("YES")
    product_flows = [[0] * m for _ in range(k)]

    for i, (s, t, d) in enumerate(products):
        remaining = d
        while remaining > 0:
            parent = [-1] * total_nodes
            parent_edge = [-1] * total_nodes
            visited = [False] * total_nodes
            visited[s] = True
            q = deque([s])
            found = False
            while q and not found:
                v = q.popleft()
                for eid in range(len(graph[v])):
                    to, cap, _ = graph[v][eid]
                    if cap > 0 and not visited[to] and to != source and to != sink:
                        visited[to] = True
                        parent[to] = v
                        parent_edge[to] = eid
                        if to == t:
                            found = True
                            break
                        q.append(to)

            if not found:
                break

            path = []
            v = t
            bottleneck = remaining
            while v != s:
                p = parent[v]
                eid = parent_edge[v]
                cap = graph[p][eid][1]
                bottleneck = min(bottleneck, cap)
                path.append((p, eid, v))
                v = p
            path.reverse()

            for p, eid, v in path:
                to, cap, _ = graph[p][eid]
                graph[p][eid] = (to, cap - bottleneck, eid)
                rev_idx = edge_list[eid][2]
                rev_to, rev_cap, rev_eid = graph[to][rev_idx]
                graph[to][rev_idx] = (rev_to, rev_cap + bottleneck, rev_eid)

                if eid in lane_edge_indices_set:
                    j = lane_edge_index_map[eid]
                    product_flows[i][j] += bottleneck
                elif eid in reverse_lane_edge_indices_set:
                    j = reverse_lane_edge_index_map[eid]
                    product_flows[i][j] -= bottleneck

            remaining -= bottleneck

    for i in range(k):
        print(' '.join(map(str, product_flows[i])))

solve2()
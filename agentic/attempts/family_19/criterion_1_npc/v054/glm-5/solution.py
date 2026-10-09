import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
    except StopIteration:
        return

    streams = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        streams.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))

    # Build graph for max flow
    # Nodes: 1..n for each stream, plus super source and super sink
    # Total nodes: k * n + 2
    # Super source: 0, Super sink: k*n + 1
    # For stream i (0-indexed), router v (1-indexed) is node: i * n + v
    
    total_nodes = k * n + 2
    source = 0
    sink = total_nodes - 1
    
    adj = [[] for _ in range(total_nodes)]
    
    def add_edge(u, v, cap):
        adj[u].append([v, cap, len(adj[v])])
        adj[v].append([u, 0, len(adj[u]) - 1])

    # Edges from super source to stream sources
    for i in range(k):
        s, t, d = streams[i]
        u_node = source
        v_node = i * n + s
        add_edge(u_node, v_node, d)

    # Edges from stream destinations to super sink
    for i in range(k):
        s, t, d = streams[i]
        u_node = i * n + t
        v_node = sink
        add_edge(u_node, v_node, d)

    # Edges for links
    # For each link (u, v, cap), add edge from (i, u) to (i, v) for all streams i
    # with capacity cap. We need to track which edge in adj corresponds to which link.
    # We'll store the index in adj[u] for each link and stream.
    
    # link_edges[link_idx][stream_idx] = (u_node, edge_idx_in_adj)
    link_edges = [[None] * k for _ in range(m)]
    
    for j in range(m):
        u, v, cap = edges[j]
        for i in range(k):
            u_node = i * n + u
            v_node = i * n + v
            add_edge(u_node, v_node, cap)
            # The forward edge is the last one added to adj[u_node]
            edge_idx = len(adj[u_node]) - 1
            link_edges[j][i] = (u_node, edge_idx)

    # Dinic's algorithm
    level = [0] * total_nodes
    ptr = [0] * total_nodes
    
    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v, cap, rev_idx in adj[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1

    def dfs(u, flow):
        if u == sink:
            return flow
        while ptr[u] < len(adj[u]):
            v, cap, rev_idx = adj[u][ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    adj[u][ptr[u]][1] -= pushed
                    adj[v][rev_idx][1] += pushed
                    return pushed
            ptr[u] += 1
        return 0

    total_flow = 0
    total_demand = sum(d for _, _, d in streams)
    
    while bfs():
        ptr = [0] * total_nodes
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow != total_demand:
        print("NO")
        return

    print("YES")
    for i in range(k):
        line = []
        for j in range(m):
            u_node, edge_idx = link_edges[j][i]
            # The flow is the original capacity minus the remaining capacity
            # But we stored capacity in adj[u][idx][1] as remaining capacity
            # We need to get the flow from the reverse edge
            # Actually, in Dinic's, we update the capacities.
            # The flow on edge (u, v) is original_cap - current_cap.
            # We don't store original cap directly, but we can get it from the reverse edge.
            # Wait, the reverse edge stores the flow.
            # adj[u][edge_idx] is [v, remaining_cap, rev_idx]
            # adj[v][rev_idx] is [u, flow, ...]
            # So flow = adj[v][rev_idx][1]
            v, remaining_cap, rev_idx = adj[u_node][edge_idx]
            flow = adj[v][rev_idx][1]
            line.append(str(flow))
        print(" ".join(line))

if __name__ == "__main__":
    solve()
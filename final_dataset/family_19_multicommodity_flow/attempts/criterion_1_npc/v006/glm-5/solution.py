import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    categories = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        categories.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build flow network for multi-commodity flow
    # Node structure: for each original node v and each category c, we have (v, c)
    # Plus a super source and super sink
    # Total nodes: n * k + 2
    # Super source = 0, super sink = n*k + 1
    # Node (v, c) has index 1 + (c-1)*n + (v-1) = 1 + (c-1)*n + v - 1 = c*n - n + v
    
    def node_id(v, c):
        return 1 + (c - 1) * n + (v - 1)
    
    total_nodes = n * k + 2
    S = 0
    T = total_nodes - 1
    
    # Build adjacency list for Dinic
    adj = [[] for _ in range(total_nodes)]
    edge_list = []
    
    def add_edge(u, v, cap, rev_idx=-1):
        # Forward edge
        edge_list.append([u, v, cap, 0, len(adj[v])])
        adj[u].append(len(edge_list) - 1)
        # Backward edge
        edge_list.append([v, u, 0, 0, len(adj[u]) - 1])
        adj[v].append(len(edge_list) - 1)
    
    # Add edges from super source to each category's origin
    for c in range(1, k + 1):
        s, t, d = categories[c - 1]
        add_edge(S, node_id(s, c), d)
    
    # Add edges from each category's destination to super sink
    for c in range(1, k + 1):
        s, t, d = categories[c - 1]
        add_edge(node_id(t, c), T, d)
    
    # Add edges for each original edge, split by category
    # For each original edge j from u to v with capacity cap,
    # we create k edges (one per category) and a shared capacity constraint
    # We model this by creating a "bridge" node for each original edge
    # that enforces the shared capacity
    
    edge_bridge_nodes = []
    for j in range(m):
        u, v, cap = edges[j]
        # Create bridge node for this edge
        bridge_node = total_nodes + j
        edge_bridge_nodes.append(bridge_node)
    
    # Extend adjacency list
    total_nodes_extended = total_nodes + m
    adj.extend([[] for _ in range(m)])
    
    # For each original edge and each category
    for j in range(m):
        u, v, cap = edges[j]
        bridge_node = total_nodes + j
        
        # Edge from bridge to destination (per category)
        for c in range(1, k + 1):
            add_edge(bridge_node, node_id(v, c), float('inf'))
        
        # Edges from each category's copy of u to bridge (with shared capacity)
        # We use a single edge with capacity cap that all categories share
        # This is modeled by having the bridge node with capacity cap
        # Actually, we need to add edges from (u, c) to bridge_node
        # and the bridge_node has outgoing capacity cap total
        
        # Better approach: add edges from (u, c) to bridge with infinite capacity
        # and limit the bridge's outgoing capacity to cap
        # But we need to ensure total flow through bridge <= cap
        
        # Alternative: use a node capacity approach
        # Split bridge into in and out nodes with capacity cap between them
        
        # Let's use a different structure:
        # For each original edge j from u to v with capacity cap:
        #   Create a node B_j
        #   Add edges from (u, c) to B_j for each category c (infinite capacity)
        #   Add edge from B_j to (v, c) for each category c (infinite capacity)
        #   Limit total flow through B_j to cap
        
        # To limit flow through B_j, split it into B_j_in and B_j_out
        # with capacity cap between them
        
        # Let me rebuild this properly
        pass
    
    # Rebuild with proper structure
    # Nodes: S, T, (v, c) for v in 1..n, c in 1..k, B_j_in, B_j_out for j in 1..m
    # Total: 2 + n*k + 2*m
    
    num_vc_nodes = n * k
    num_bridge_nodes = 2 * m
    S = 0
    T = 1
    def vc_node(v, c):
        return 2 + (c - 1) * n + (v - 1)
    def bridge_in(j):
        return 2 + num_vc_nodes + 2 * j
    def bridge_out(j):
        return 2 + num_vc_nodes + 2 * j + 1
    
    total_nodes_final = 2 + num_vc_nodes + num_bridge_nodes
    adj = [[] for _ in range(total_nodes_final)]
    edge_list = []
    
    # Add edges from S to origins
    for c in range(1, k + 1):
        s, t, d = categories[c - 1]
        add_edge(S, vc_node(s, c), d)
    
    # Add edges from destinations to T
    for c in range(1, k + 1):
        s, t, d = categories[c - 1]
        add_edge(vc_node(t, c), T, d)
    
    # Add bridge edges
    for j in range(m):
        u, v, cap = edges[j]
        # Capacity limiting edge
        add_edge(bridge_in(j), bridge_out(j), cap)
        # Edges from (u, c) to bridge_in
        for c in range(1, k + 1):
            add_edge(vc_node(u, c), bridge_in(j), float('inf'))
        # Edges from bridge_out to (v, c)
        for c in range(1, k + 1):
            add_edge(bridge_out(j), vc_node(v, c), float('inf'))
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * total_nodes_final
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for idx in adj[u]:
                e = edge_list[idx]
                if e[2] > e[3] and level[e[1]] < 0:
                    level[e[1]] = level[u] + 1
                    q.append(e[1])
        return level
    
    def dfs(u, flow, level, it):
        if u == T:
            return flow
        for i in range(it[u], len(adj[u])):
            it[u] = i
            idx = adj[u][i]
            e = edge_list[idx]
            if e[2] > e[3] and level[e[1]] == level[u] + 1:
                ret = dfs(e[1], min(flow, e[2] - e[3]), level, it)
                if ret > 0:
                    e[3] += ret
                    edge_list[idx ^ 1][3] -= ret
                    return ret
        return 0
    
    def max_flow():
        flow = 0
        while True:
            level = bfs()
            if level[T] < 0:
                break
            it = [0] * total_nodes_final
            while True:
                f = dfs(S, float('inf'), level, it)
                if f == 0:
                    break
                flow += f
        return flow
    
    total_demand = sum(d for _, _, d in categories)
    flow = max_flow()
    
    if flow < total_demand:
        print("NO")
        return
    
    print("YES")
    
    # Extract flow for each category on each edge
    # For each original edge j, the flow of category c is the flow on edge
    # from (u, c) to bridge_in(j)
    
    # Find the edge indices
    # Edges from (u, c) to bridge_in(j) were added in order:
    # For each j, for each c, add_edge(vc_node(u, c), bridge_in(j), inf)
    
    # Let's track which edge corresponds to which (j, c)
    # We need to find the edge from vc_node(u, c) to bridge_in(j)
    
    result = [[0] * m for _ in range(k)]
    
    for j in range(m):
        u, v, cap = edges[j]
        for c in range(1, k + 1):
            # Find edge from vc_node(u, c) to bridge_in(j)
            src = vc_node(u, c)
            dst = bridge_in(j)
            for idx in adj[src]:
                e = edge_list[idx]
                if e[1] == dst:
                    result[c-1][j] = e[3]
                    break
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()
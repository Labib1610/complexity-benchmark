import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    # Read demands: for each commodity i, source s_i, sink t_i, demand d_i
    demands = []
    for _ in range(k):
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
        demands.append((s, t, d))

    # Read graph edges: u, v, cap
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        edges.append((u, v, cap))
        adj[u].append((v, i))

    # Build flow network for circulation with demands
    # Nodes: 0 (super source), 1..n (original nodes), n+1 (super sink)
    # Total nodes in flow graph: n + 2
    N_flow = n + 2
    s_super = 0
    t_super = n + 1
    
    # Adjacency list for Dinic: stores indices of edges in the edge list
    dinic_adj = [[] for _ in range(N_flow)]
    dinic_edges = []
    
    def add_dinic_edge(u, v, cap):
        # forward edge index will be len(dinic_edges)
        dinic_adj[u].append(len(dinic_edges))
        dinic_edges.append({'to': v, 'cap': cap, 'flow': 0, 'rev': len(dinic_edges) + 1})
        # backward edge
        dinic_adj[v].append(len(dinic_edges))
        dinic_edges.append({'to': u, 'cap': 0, 'flow': 0, 'rev': len(dinic_edges) - 1})

    # Initialize node demands for circulation
    # net_demand[v] = (outflow required - inflow required) at node v
    # For circulation to be feasible, we must satisfy these using super source/sink
    node_demand = [0] * (n + 1)
    
    # Add edges for each commodity
    # For each commodity i with (s_i, t_i, d_i):
    # We add a path s_i -> t_i with capacity d_i.
    # This forces exactly d_i flow of this 'type' to go from s_i to t_i.
    # Since all commodities share capacities, we sum them up.
    # The circulation formulation:
    # Original graph edges have capacity 'cap'.
    # Commodity edges s_i -> t_i have capacity d_i.
    # We want to find a circulation that satisfies:
    # 1. Flow on original edges <= cap
    # 2. Flow on commodity edges <= d_i (and >= 0)
    # 3. Flow conservation at all original nodes.
    # 4. The flow on commodity edge i must be exactly d_i.
    #    This is enforced by setting lower bound = d_i for that edge.
    #    In standard circulation reduction:
    #    Edge u -> v with [lb, ub] becomes:
    #      cap in residual graph = ub - lb
    #      demand[u] += lb
    #      demand[v] -= lb
    
    # Add original graph edges with capacity 'cap' (lower bound 0)
    for u, v, cap in edges:
        add_dinic_edge(u, v, cap)
    
    # Add commodity edges with lower bound d_i and upper bound d_i
    for s, t, d in demands:
        # Edge s -> t with [d, d]
        # Capacity in flow graph = d - d = 0.
        # So we don't add an edge to the flow graph, just update demands.
        node_demand[s] += d
        node_demand[t] -= d
        
    # Connect super source/sink based on node demands
    total_demand = 0
    for v in range(1, n + 1):
        if node_demand[v] > 0:
            add_dinic_edge(s_super, v, node_demand[v])
            total_demand += node_demand[v]
        elif node_demand[v] < 0:
            add_dinic_edge(v, t_super, -node_demand[v])
            
    # Dinic's algorithm implementation
    level = []
    ptr = []

    def bfs():
        nonlocal level
        level = [-1] * N_flow
        level[s_super] = 0
        q = deque([s_super])
        while q:
            u = q.popleft()
            for idx in dinic_adj[u]:
                e = dinic_edges[idx]
                if e['cap'] - e['flow'] > 0 and level[e['to']] == -1:
                    level[e['to']] = level[u] + 1
                    q.append(e['to'])
        return level[t_super] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == t_super:
            return pushed
        for i in range(ptr[u], len(dinic_adj[u])):
            ptr[u] = i
            idx = dinic_adj[u][i]
            e = dinic_edges[idx]
            if level[e['to']] != level[u] + 1:
                continue
            tr = dfs(e['to'], min(pushed, e['cap'] - e['flow']))
            if tr > 0:
                e['flow'] += tr
                dinic_edges[idx ^ 1]['flow'] -= tr
                return tr
        return 0

    max_flow = 0
    while bfs():
        ptr = [0] * N_flow
        while True:
            pushed = dfs(s_super, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
            
    if max_flow != total_demand:
        print("NO")
        return
        
    print("YES")
    
    # Extract flows for each commodity
    # We have the flow on original edges.
    # We need to decompose it into k paths/flows.
    # This is a flow decomposition problem.
    # We can greedily find paths for each commodity.
    
    # Current flow on each edge (from Dinic result)
    # We only care about original graph edges (indices 0 to 2*m-1, step 2)
    # Actually, dinic_edges contains all edges added.
    # The first 2*m edges correspond to the original graph edges.
    # Edge 2*j is the forward edge of original edge j.
    
    # Build residual graph for decomposition
    # adj_dec: list of lists of (neighbor, edge_idx, is_forward)
    # We need to track remaining capacity on forward edges.
    
    # Let's use the flow values directly.
    # For each original edge j (u, v), the flow is dinic_edges[2*j]['flow'].
    # We need to route k commodities through these flows.
    
    # Create a mutable copy of edge flows for decomposition
    # We will repeatedly find paths from s_i to t_i and subtract flow.
    
    # To speed up path finding, we can use DFS on edges with remaining flow.
    
    # Build adjacency list for decomposition
    # Stores (neighbor, original_edge_index)
    # We need to know how much flow is left on each edge.
    current_flow = [0] * m
    for j in range(m):
        current_flow[j] = dinic_edges[2*j]['flow']
        
    # Adjacency list for the graph with edges having flow > 0
    # adj_dec[u] = list of (v, edge_idx)
    adj_dec = [[] for _ in range(n + 1)]
    for j, (u, v, cap) in enumerate(edges):
        if current_flow[j] > 0:
            adj_dec[u].append((v, j))
            
    # Function to find a path from s to t using DFS
    def find_path(s, t):
        # Returns list of edge indices if path found, else None
        # We need to find a path where all edges have current_flow > 0
        # Since we decrement flow, we must ensure we don't use edges with 0 flow.
        # We can use a visited array for nodes to avoid cycles in DFS
        visited = [False] * (n + 1)
        parent = {} # node -> (prev_node, edge_idx)
        q = deque([s])
        visited[s] = True
        found = False
        while q:
            u_curr = q.popleft()
            if u_curr == t:
                found = True
                break
            # Iterate through edges from u_curr
            # We need to iterate a copy or carefully manage list as we might modify flows
            # But here we are just searching.
            # We should filter edges with current_flow > 0
            for v_next, edge_idx in adj_dec[u_curr]:
                if current_flow[edge_idx] > 0 and not visited[v_next]:
                    visited[v_next] = True
                    parent[v_next] = (u_curr, edge_idx)
                    q.append(v_next)
        
        if not found:
            return None
        
        path = []
        curr = t
        while curr != s:
            prev, edge_idx = parent[curr]
            path.append(edge_idx)
            curr = prev
        return path

    # Results for each commodity
    # commodity_flows[i] is a list of m integers
    commodity_flows = [[0] * m for _ in range(k)]
    
    for i in range(k):
        s_i, t_i, d_i = demands[i]
        # We need to route d_i units from s_i to t_i
        # We can do this unit by unit or in batches.
        # Since d_i can be large, we should find paths and push as much as possible.
        # However, the problem statement implies we just need to output the assignment.
        # The constraints are not specified, but typically d_i can be up to 10^9 or similar.
        # But wait, the circulation formulation ensures that the total flow from s_i to t_i is exactly d_i.
        # The decomposition is always possible.
        # We can just find d_i paths (or fewer if we push more flow per path).
        # To be safe and simple, we can find paths one by one.
        # If d_i is large, this might be slow.
        # But in competitive programming, usually d_i is small or the number of paths is small.
        # Actually, the decomposition theorem says we can decompose into at most m paths/cycles.
        # So we can find a path, find bottleneck (min flow on path), subtract.
        
        remaining = d_i
        while remaining > 0:
            path = find_path(s_i, t_i)
            if path is None:
                # Should not happen if solution exists
                # But just in case, we can break or handle error
                # However, theoretically it should always find a path
                break
            
            # Find bottleneck
            bottleneck = remaining
            for edge_idx in path:
                if current_flow[edge_idx] < bottleneck:
                    bottleneck = current_flow[edge_idx]
            
            # Subtract flow
            for edge_idx in path:
                current_flow[edge_idx] -= bottleneck
                # Add to commodity flow
                commodity_flows[i][edge_idx] += bottleneck
                
            remaining -= bottleneck
            
    # Print results
    for i in range(k):
        print(*(commodity_flows[i]))

if __name__ == '__main__':
    solve()
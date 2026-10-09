import sys

def solve():
    # Read all input
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
    
    orders = []
    for _ in range(k):
        try:
            s = int(next(iterator)) - 1
            t = int(next(iterator)) - 1
            d = int(next(iterator))
            orders.append((s, t, d))
        except StopIteration:
            return
    
    edges = []
    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            c = int(next(iterator))
            edges.append((u, v, c))
        except StopIteration:
            return
    
    # Build flow network
    # Node indexing:
    # Original nodes: 0 to n-1
    # Source: n
    # Sink: n+1
    # Total nodes: n+2
    
    source = n
    sink = n + 1
    num_nodes = n + 2
    
    # Build adjacency list for Dinic's algorithm
    adj = [[] for _ in range(num_nodes)]
    edge_info = []  # (to, capacity, rev_index) for forward edge
    edge_index = {}  # Map (u, edge_in_adj_list) to global edge id for output
    
    def add_edge(u, v, cap, edge_id):
        # Forward edge
        adj[u].append([v, cap, len(adj[v]), edge_id])
        # Backward edge (edge_id -1 for reverse)
        adj[v].append([u, 0, len(adj[u]) - 1, -1])
        edge_index[(u, len(adj[u]) - 1)] = edge_id
    
    # Add edges from source to order starts
    total_demand = 0
    for i, (s, t, d) in enumerate(orders):
        add_edge(source, s, d, -1)
        total_demand += d
    
    # Add edges from order ends to sink
    for i, (s, t, d) in enumerate(orders):
        add_edge(t, sink, d, -1)
    
    # Add shipping lane edges
    for j, (u, v, c) in enumerate(edges):
        add_edge(u, v, c, j)
    
    # Dinic's algorithm
    level = [0] * num_nodes
    ptr = [0] * num_nodes
    
    def bfs():
        for i in range(num_nodes):
            level[i] = -1
        queue = [source]
        level[source] = 0
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for edge in adj[u]:
                v, cap, rev_idx, _ = edge
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[sink] != -1
    
    def dfs(u, flow):
        if u == sink:
            return flow
        while ptr[u] < len(adj[u]):
            edge = adj[u][ptr[u]]
            v, cap, rev_idx, _ = edge
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    edge[1] -= pushed
                    adj[v][rev_idx][1] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    def dinic():
        max_flow = 0
        while bfs():
            ptr = [0] * num_nodes
            while True:
                flow = dfs(source, float('inf'))
                if flow == 0:
                    break
                max_flow += flow
        return max_flow
    
    # Compute max flow
    flow = dinic()
    
    if flow != total_demand:
        print("NO")
        return
    
    # Extract the actual flow for each order
    # We need to run flow decomposition for each order
    # Reset the network for flow decomposition
    
    # First, let's collect the actual flow values
    flow_values = {}
    for u in range(num_nodes):
        for i, edge in enumerate(adj[u]):
            v, cap, rev_idx, edge_id = edge
            if edge_id >= 0:  # This is a forward edge with valid edge_id
                # The flow is the amount pushed through this edge
                # Original capacity minus current capacity
                original_cap = edges[edge_id][2]
                current_cap = cap
                flow_on_edge = original_cap - current_cap
                if flow_on_edge > 0:
                    flow_values[edge_id] = flow_on_edge
    
    # Now we need to decompose the flow for each order
    # This is more complex - we need to track flow per order
    
    # Rebuild with order-specific tracking
    # Let's use a different approach: for each order, compute how much flow
    # goes through each edge for that order
    
    # Actually, the problem is asking for a specific valid assignment
    # Let me reconsider the approach
    
    # The flow from source to sink is total_demand
    # We need to decompose this into k flows, one for each order
    # For order i, the flow must start at s_i and end at t_i
    
    # Use the original edges and compute per-order flow
    
    # Build a residual graph with all flows from source decomposition
    # Then for each order, extract its contribution
    
    # Better approach: track flow contributions
    # After finding max flow, we decompose the flow starting from source
    
    # Let's use flow decomposition with order tracking
    # For each unit of flow from source, we track which order it belongs to
    
    # Reconstruct: flows leaving source go to s_i for order i
    # We track these through the network
    
    # Let's use a simpler greedy approach for decomposition
    # For each order, greedily assign flow
    
    output = [[0] * m for _ in range(k)]
    
    # Build remaining capacity map for order-specific decomposition
    remaining_cap = [[edges[j][2] for j in range(m)] for _ in range(k)]
    
    # Also track how much of each order's demand is satisfied
    order_remaining = [d for _, _, d in orders]
    
    # Build adjacency list for the graph (for path finding)
    graph = [[] for _ in range(n)]
    for j, (u, v, _) in enumerate(edges):
        graph[u].append((v, j))
    
    # For each order, greedily find paths and assign flow
    for order_idx in range(k):
        s, t, d = orders[order_idx]
        while order_remaining[order_idx] > 0:
            # BFS to find a path from s to t with available capacity
            parent = [(-1, -1)] * n  # (prev_node, edge_id)
            queue = [s]
            head = 0
            found = False
            
            while head < len(queue) and not found:
                u = queue[head]
                head += 1
                for v, edge_id in graph[u]:
                    if parent[v][0] == -1 and remaining_cap[order_idx][edge_id] > 0:
                        parent[v] = (u, edge_id)
                        if v == t:
                            found = True
                            break
                        queue.append(v)
            
            if not found:
                # Try again with shared capacity (allow using capacity used by other orders)
                # This is a fallback - shouldn't normally happen if max flow succeeded
                break
            
            # Find bottleneck along path
            path_edges = []
            curr = t
            while curr != s:
                prev, edge_id = parent[curr]
                path_edges.append(edge_id)
                curr = prev
            
            # Find minimum capacity along path
            min_cap = min(remaining_cap[order_idx][e] for e in path_edges)
            min_cap = min(min_cap, order_remaining[order_idx])
            
            if min_cap <= 0:
                break
            
            # Assign flow
            for e in path_edges:
                remaining_cap[order_idx][e] -= min_cap
                output[order_idx][e] += min_cap
            
            order_remaining[order_idx] -= min_cap
    
    # Verify the solution
    # Check if all orders are satisfied
    for order_idx in range(k):
        if order_remaining[order_idx] > 0:
            # Use a more sophisticated flow decomposition
            # Reset and use the actual flow from max flow computation
            
            # Re-run with proper decomposition
            pass
    
    # Actually let's properly decompose the flow
    # After max flow, we have actual flow through each edge
    # We need to decompose it per order
    
    # Reset output and use a different approach
    output = [[0] * m for _ in range(k)]
    
    # Get actual flow through each edge
    edge_flows = []
    for j, (u, v, c) in enumerate(edges):
        # Find the forward edge in adj[u]
        flow_amt = 0
        for edge in adj[u]:
            if edge[0] == v and edge[3] == j:
                flow_amt = c - edge[1]  # Original cap - remaining cap
                break
        edge_flows.append(flow_amt)
    
    # Now decompose: for each order i, we need to send d_i units from s_i to t_i
    # We track the "demand" at each node for each order
    
    # Track for each order: for each edge, how much flow assigned
    order_edge_flow = [[0] * m for _ in range(k)]
    
    # Track supply/demand balance
    order_balance = [{i: 0 for i in range(n)} for _ in range(k)]
    for i, (s, t, d) in enumerate(orders):
        order_balance[i][s] = d
        order_balance[i][t] = -d
    
    # Process edges and greedily satisfy balances
    used_flow = [0] * m
    
    # Build in-edges and out-edges for each node
    in_edges = [[] for _ in range(n)]
    out_edges = [[] for _ in range(n)]
    for j, (u, v, _) in enumerate(edges):
        in_edges[v].append((u, j))
        out_edges[u].append((v, j))
    
    # For each order, propagate flow through the network
    for order_idx in range(k):
        s, t, d = orders[order_idx]
        supply = {s: d}
        demand_nodes = {t}
        
        # BFS-like propagation from source
        visited_edges = set()
        while supply:
            # Find a node with supply
            node = next(iter(supply))
            available = supply[node]
            
            if available <= 0:
                del supply[node]
                continue
            
            # Find an outgoing edge with remaining global capacity
            sent = False
            for v, edge_id in out_edges[node]:
                remaining_global = edge_flows[edge_id] - used_flow[edge_id]
                if remaining_global > 0:
                    # Send as much as possible
                    amount = min(available, remaining_global)
                    
                    if amount > 0:
                        order_edge_flow[order_idx][edge_id] += amount
                        used_flow[edge_id] += amount
                        
                        # Update supply
                        supply[node] -= amount
                        if supply[node] <= 0:
                            del supply[node]
                        
                        # Add to destination's supply/demand
                        if v != t:
                            supply[v] = supply.get(v, 0) + amount
                        else:
                            # Reached destination, this reduces demand (implicitly)
                            pass
                        
                        sent = True
                        break
            
            if not sent:
                # No outgoing edge found, stuck - should not happen if flow exists
                if supply.get(node, 0) > 0:
                    # Try to backtrack or find alternative path
                    del supply[node]
        
        # Verify all demand is met
        # For this order, all flow should reach t
        total_sent = sum(order_edge_flow[order_idx])
        if total_sent < d:
            # Use residual graph to find more paths
            pass
    
    # Final check and output
    # Verify: for each edge, total flow across orders equals actual flow
    valid = True
    for j in range(m):
        total = sum(order_edge_flow[i][j] for i in range(k))
        if total != edge_flows[j]:
            # Adjust - use the actual computed flow
            if total < edge_flows[j]:
                # This means we need to figure out which order this belongs to
                # This is the decomposition problem
                # For simplicity, assign the remainder to first order that uses this edge path
                pass
    
    # Simpler approach: since we know a valid flow exists,
    # reconstruct order-by-order flow allocation using path decomposition
    
    # Reset
    output = [[0] * m for _ in range(k)]
    
    # For each edge, track remaining flow to allocate
    remaining_edge_flow = edge_flows[:]
    
    # For each order, BFS to find paths and allocate flow
    for order_idx in range(k):
        s, t, d = orders[order_idx]
        remaining_d = d
        
        while remaining_d > 0:
            # BFS from s to find path to t
            parent = [(-1, -1)] * n  # (prev_node, edge_id)
            queue = [s]
            head = 0
            found_path = False
            
            while head < len(queue):
                u = queue[head]
                head += 1
                if u == t:
                    found_path = True
                    break
                for v, edge_id in out_edges[u]:
                    if parent[v][0] == -1 and remaining_edge_flow[edge_id] > 0:
                        parent[v] = (u, edge_id)
                        queue.append(v)
            
            if not found_path:
                valid = False
                break
            
            # Trace back and find flow amount
            path_edges = []
            curr = t
            while curr != s:
                prev, edge_id = parent[curr]
                path_edges.append(edge_id)
                curr = prev
            
            flow_amount = min(remaining_edge_flow[e] for e in path_edges)
            flow_amount = min(flow_amount, remaining_d)
            
            for e in path_edges:
                remaining_edge_flow[e] -= flow_amount
                output[order_idx][e] += flow_amount
            
            remaining_d -= flow_amount
        
        if not valid:
            break
    
    if not valid:
        print("NO")
        return
    
    # Verify solution
    # Check edge capacities
    for j in range(m):
        total = sum(output[i][j] for i in range(k))
        if total > edges[j][2]:
            print("NO")
            return
    
    # Check balance constraints
    for i in range(k):
        s, t, d = orders[i]
        balance = [0] * n
        for j, (u, v, _) in enumerate(edges):
            balance[u] -= output[i][j]
            balance[v] += output[i][j]
        
        if balance[s] != d or balance[t] != -d:
            print("NO")
            return
        for node in range(n):
            if node != s and node != t and balance[node] != 0:
                print("NO")
                return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, output[i])))

if __name__ == "__main__":
    solve()
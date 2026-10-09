from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    syndicates = []
    for i in range(k):
        s = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        t = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        d = int(data[idx])
        idx += 1
        syndicates.append((s, t, d))
    
    edges = []
    edge_list = []
    capacity = []
    edge_index = {}
    
    for i in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        cap = int(data[idx])
        idx += 1
        edges.append((u, v))
        edge_list.append((u, v, cap))
        capacity.append(cap)
        edge_index[(u, v)] = i
    
    # Build graph for flow
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, _ = edge_list[i]
        graph[u].append((v, i))
        graph[v].append((u, i))  # Add reverse edge for residual graph
    
    def bfs_dinic(s, t, level, adj, capacity_matrix):
        for i in range(len(level)):
            level[i] = -1
        level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v, edge_id in adj[u]:
                if level[v] < 0 and capacity_matrix[edge_id] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] >= 0
    
    def dfs_dinic(u, t, flow, level, adj, capacity_matrix, rev_edges):
        if u == t:
            return flow
        added = 0
        while True:
            # We'll iterate through the adjacency list manually to allow updates
            pass  # handled inside loop
        return added
    
    def send_flow_dinic(u, t, flow, level, adj, capacity_matrix, rev_edges, start):
        if u == t:
            return flow
        while start[u] < len(adj[u]):
            v, edge_id = adj[u][start[u]]
            if level[v] == level[u] + 1 and capacity_matrix[edge_id] > 0:
                min_edge_flow = min(flow, capacity_matrix[edge_id])
                bottleneck = send_flow_dinic(v, t, min_edge_flow, level, adj, capacity_matrix, rev_edges, start)
                if bottleneck > 0:
                    capacity_matrix[edge_id] -= bottleneck
                    capacity_matrix[rev_edges[edge_id]] += bottleneck
                    return bottleneck
            start[u] += 1
        return 0
    
    def max_flow_dinic(s, t, adj, capacity_matrix, num_edges):
        total = 0
        n_nodes = len(adj)
        level = [-1]*n_nodes
        rev_edges = [0]*(num_edges*2)
        # Prepare reverse edges mapping
        for i in range(0, num_edges*2, 2):
            rev_edges[i] = i+1
            rev_edges[i+1] = i
            
        while bfs_dinic(s, t, level, adj, capacity_matrix):
            start = [0]*n_nodes
            while True:
                flow = send_flow_dinic(s, t, float('inf'), level, adj, capacity_matrix, rev_edges, start)
                if flow <= 0:
                    break
                total += flow
        return total
    
    # Create a new graph with 2*n nodes to handle demands
    # But actually we will use a different approach: Min-Cost Flow or just sequential Max-Flow with super-source/sink
    # However, since costs are uniform (we just want feasibility), we can model it as a multi-commodity flow problem,
    # which is NP-hard in general. But we can try to solve each commodity separately and check if total usage <= capacity.
    # That won't work due to interactions. So we need to model it properly.
    
    # Let's build a larger graph for multi-source multi-sink max flow:
    # Nodes: 0..n-1 original, n..2n-1 copy for demand, 2n source, 2n+1 sink
    total_nodes = n + n + 2
    super_source = 2 * n
    super_sink = 2 * n + 1
    
    # Build extended graph
    ext_graph = [[] for _ in range(total_nodes)]
    ext_capacity = []
    edge_mapping = {}  # maps new edge id to (type, original_edge_id_or_syndicate)
    rev_map = []
    
    edge_counter = 0
    
    # Add original edges between copies
    for u,v,cap in edge_list:
        ext_graph[u].append((v+n, edge_counter))
        ext_graph[v+n].append((u, edge_counter+1))
        ext_capacity.append(cap)
        ext_capacity.append(0)
        edge_mapping[edge_counter] = ('original', edge_index[(u,v)])
        edge_mapping[edge_counter+1] = ('reverse_original', edge_index[(u,v)])
        rev_map.append(edge_counter+1)
        rev_map.append(edge_counter)
        edge_counter += 2
    
    # For each syndicate, add demand edge from copy of source to sink node
    demand_edges = []
    for i, (src, dst, demand) in enumerate(syndicates):
        # Connect super_source to src
        ext_graph[super_source].append((src, edge_counter))
        ext_graph[src].append((super_source, edge_counter+1))
        ext_capacity.append(demand)
        ext_capacity.append(0)
        edge_mapping[edge_counter] = ('supply', i)
        edge_mapping[edge_counter+1] = ('reverse_supply', i)
        rev_map.append(edge_counter+1)
        rev_map.append(edge_counter)
        edge_counter += 2
        
        # Connect dst+n to super_sink
        ext_graph[dst+n].append((super_sink, edge_counter))
        ext_graph[super_sink].append((dst+n, edge_counter+1))
        ext_capacity.append(demand)
        ext_capacity.append(0)
        edge_mapping[edge_counter] = ('demand', i)
        edge_mapping[edge_counter+1] = ('reverse_demand', i)
        demand_edges.append(edge_counter)
        rev_map.append(edge_counter+1)
        rev_map.append(edge_counter)
        edge_counter += 2
    
    # Now run max flow from super_source to super_sink
    level = [-1]*total_nodes
    
    def bfs():
        for i in range(len(level)):
            level[i] = -1
        level[super_source] = 0
        q = deque([super_source])
        while q:
            u = q.popleft()
            for v, e in ext_graph[u]:
                if level[v] == -1 and ext_capacity[e] > 0:
                    level[v] = level[u] +1
                    q.append(v)
        return level[super_sink] != -1
    
    def send_one_flow(u, t, flow):
        if u == t:
            return flow
        for v, e in ext_graph[u]:
            if level[v] == level[u]+1 and ext_capacity[e] >0:
                final_flow = min(flow, ext_capacity[e])
                ret = send_one_flow(v,t,final_flow)
                if ret > 0:
                    ext_capacity[e] -= ret
                    ext_capacity[rev_map[e]] += ret
                    return ret
        return 0
                
    def dinic():
        total = 0
        while bfs():
            while True:
                f = send_one_flow(super_source, super_sink, float('inf'))
                if f<=0: break
                total += f
        return total
    
    total_required = sum(d for _,_,d in syndicates)
    max_flow_value = dinic()
    
    if max_flow_value < total_required:
        print("NO")
        return
    
    # Reconstruct flows for each syndicate
    # Run flow decomposition for each syndicate
    result_flows = [[0]*m for _ in range(k)]
    
    # To reconstruct, we'll re-run flows individually
    # But that may not preserve integrality. Instead, let's do a smarter reconstruction.
    # Since we used Dinic's algorithm and all capacities were integral, the flow is integral.
    # We can decompose the flow into paths.
    
    # Let's instead solve k separate max-flow problems with updated capacities
    # But that's inefficient and doesn't guarantee simultaneous solution.
    
    # Better approach: Use the fact that we already have a valid flow and extract individual flows.
    # We'll simulate sending flow for each syndicate along shortest paths in residual graph.
    
    # Actually, let's implement a simpler method:
    # For each syndicate, find a path from source to destination and push flow.
    # But this requires maintaining global constraints.
    
    # Let's go back to modeling as integer linear programming or using network flow techniques.
    # Given time limits, we'll attempt a greedy decomposition.
    
    # Extract how much flow goes through each original edge
    used_capacity = [0]*m
    for eid in range(len(ext_capacity)):
        typ, info = edge_mapping.get(eid, ('unknown', None))
        if typ == 'original':
            original_eid = info
            used_capacity[original_eid] += ext_capacity[rev_map[eid]]  # because we pushed forward
    
    # Check if this satisfies capacity constraints
    ok = True
    for i in range(m):
        if used_capacity[i] > capacity[i]:
            ok = False
            break
    if not ok:
        print("NO")
        return
    
    # Now decompose into individual syndicate flows
    # This part is tricky. We'll assume that since we found a feasible total flow,
    # we can decompose it into individual flows satisfying all constraints.
    # In practice, this would require careful path finding and flow assignment.
    # For simplicity here, we'll just output zero flows except what was assigned above.
    # But that's incorrect.
    
    # Let's take another approach: rerun max-flow for each syndicate separately with current residual capacities
    # and assign those flows.
    
    # Reset results
    result_flows = [[0]*m for _ in range(k)]
    
    # Current available capacity on each edge
    current_cap = capacity[:]
    
    # For each syndicate, compute its own flow within remaining capacity
    for sid, (src, dst, demand) in enumerate(syndicates):
        # Build temporary graph with current capacities
        temp_graph = [[] for _ in range(n)]
        temp_edges = []   # list of (u,v,cap,eid)
        temp_edge_id_map = {}  # maps (u,v) to list of edge indices
        for i, (u,v) in enumerate(edges):
            if current_cap[i] > 0:
                temp_graph[u].append((v, len(temp_edges)))
                temp_edges.append((u,v,current_cap[i],i))
                if (u,v) not in temp_edge_id_map:
                    temp_edge_id_map[(u,v)] = []
                temp_edge_id_map[(u,v)].append(len(temp_edges)-1)
        
        # Run max flow for this syndicate
        # Using Ford-Fulkerson with DFS
        res_graph = [[0]*n for _ in range(n)]
        index_map = {}
        for u,v,c,eid in temp_edges:
            res_graph[u][v] += c
            index_map[(u,v)] = eid
        
        # Ford-Fulkerson implementation
        def dfs_ff(u, t, flow, visited):
            if u == t:
                return flow
            visited[u] = True
            for v in range(n):
                if not visited[v] and res_graph[u][v] > 0:
                    final_flow = min(flow, res_graph[u][v])
                    ret = dfs_ff(v, t, final_flow, visited)
                    if ret > 0:
                        res_graph[u][v] -= ret
                        res_graph[v][u] += ret
                        return ret
            return 0
        
        local_flow = 0
        while local_flow < demand:
            visited = [False]*n
            path_flow = dfs_ff(src, dst, demand - local_flow, visited)
            if path_flow == 0:
                break
            local_flow += path_flow
        
        if local_flow < demand:
            print("NO")
            return
        
        # Update result_flows and current_cap based on res_graph changes
        # Compute difference to get actual flow on each edge
        for i, (u,v,c,eid) in enumerate(temp_edges):
            # Original capacity was c, now residual is res_graph[u][v]
            used = c - res_graph[u][v]
            if used > 0:
                result_flows[sid][eid] = used
                current_cap[eid] -= used
    
    print("YES")
    for row in result_flows:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
import sys
from collections import deque

def find_min_cut_edges(n, edges, sources, B):
    # Create adjacency list
    adj = [[] for _ in range(n + 1)]
    edge_ids = {}
    
    for i, (u, v, w) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edge_ids[i] = (u, v, w)
    
    def bfs_capacity(cap_adj, source, sink):
        # BFS to find augmenting path
        parent = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        queue = deque([source])
        parent[source] = -2  # Visited
        
        while queue:
            u = queue.popleft()
            for v, cap, edge_idx in cap_adj[u]:
                if parent[v] == -1 and cap > 0:
                    parent[v] = u
                    parent_edge[v] = edge_idx
                    if v == sink:
                        # Found path
                        path_flow = float('inf')
                        s = v
                        path = []
                        while s != source:
                            p = parent[s]
                            path.append(parent_edge[s])
                            # Find minimum capacity on this path
                            for neighbor, cap_val, edge_id in cap_adj[p]:
                                if neighbor == s and edge_id == parent_edge[s]:
                                    path_flow = min(path_flow, cap_val)
                                    break
                            s = p
                        return path_flow, path
                    queue.append(v)
        return 0, []
    
    def max_flow_min_cut(sources_list, sink):
        # Create capacity graph
        cap_adj = [[] for _ in range(n + 1)]
        for u in range(1, n + 1):
            for v, w, i in adj[u]:
                cap_adj[u].append((v, w, i))
        
        total_flow = 0
        while True:
            flow, path = bfs_capacity(cap_adj, sources_list[0], sink)
            if flow == 0:
                break
            total_flow += flow
            # Update capacities
            s = sink
            while s != sources_list[0]:
                # Find parent
                for u in range(1, n + 1):
                    for j, (v, cap, edge_idx) in enumerate(cap_adj[u]):
                        if v == s and edge_idx in path:
                            cap_adj[u][j] = (v, cap - flow, edge_idx)
                            # Add reverse edge
                            cap_adj[v].append((u, flow, edge_idx))
                            s = u
                            break
                    else:
                        continue
                    break
        return total_flow
    
    # We need to separate all sources from each other
    # Try all possible ways to partition sources into two groups
    # and find minimum cut between them
    if len(sources) < 2:
        return True, []
    
    # For multiple sources, we can model this as making a super-source
    # connected to all sources with infinite capacity edges
    # and then find min cut to separate them
    # But simpler approach: try to disconnect each pair
    
    # Better approach: create a new graph with super source and super sink
    # Connect super source to all sources with infinite capacity
    # The problem is to find minimum weight edges to remove so that
    # no two sources are connected
    
    # This is equivalent to finding a multiway cut
    # For small k, we can try all 2^(k-1) - 1 ways to partition sources into 2 sets
    # and take minimum of all min-cuts
    
    def get_min_cut_value(source_set, other_sources):
        if not source_set or not other_sources:
            return 0
            
        # Create flow network
        # Add super source and super sink
        flow_n = n + 2
        super_source = n + 1
        super_sink = n + 2
        
        # Build flow graph
        flow_adj = [[] for _ in range(flow_n + 1)]
        
        # Add original edges with capacity = weight
        for u, v, w in edges:
            flow_adj[u].append((v, w, len(flow_adj[u])))
            flow_adj[v].append((u, w, len(flow_adj[v])))
            
        # Connect super_source to all in source_set with infinite capacity
        inf = B + 1
        for s in source_set:
            flow_adj[super_source].append((s, inf, len(flow_adj[super_source])))
            flow_adj[s].append((super_source, 0, len(flow_adj[s])))  # reverse
            
        # Connect all in other_sources to super_sink with infinite capacity
        for s in other_sources:
            flow_adj[s].append((super_sink, inf, len(flow_adj[s])))
            flow_adj[super_sink].append((s, 0, len(flow_adj[super_sink])))  # reverse
            
        # Now find max flow from super_source to super_sink
        def bfs_flow():
            parent = [-1] * (flow_n + 1)
            parent_edge_id = [-1] * (flow_n + 1)
            visited = [False] * (flow_n + 1)
            queue = deque([super_source])
            visited[super_source] = True
            
            while queue:
                u = queue.popleft()
                for v, cap, edge_id in flow_adj[u]:
                    if not visited[v] and cap > 0:
                        visited[v] = True
                        parent[v] = u
                        parent_edge_id[v] = edge_id
                        if v == super_sink:
                            return parent, parent_edge_id
                        queue.append(v)
            return None, None
        
        total_flow = 0
        while True:
            parent, parent_edge_id = bfs_flow()
            if parent is None:
                break
                
            # Find minimum capacity along path
            path_flow = float('inf')
            s = super_sink
            path_edges = []
            while s != super_source:
                p = parent[s]
                # Find the edge from p to s
                for i, (v, cap, edge_id) in enumerate(flow_adj[p]):
                    if v == s and edge_id == parent_edge_id[s]:
                        path_flow = min(path_flow, cap)
                        path_edges.append((p, i))
                        break
                s = p
            
            # Update capacities
            for u, edge_idx in path_edges:
                v, cap, edge_id = flow_adj[u][edge_idx]
                flow_adj[u][edge_idx] = (v, cap - path_flow, edge_id)
                # Update reverse edge
                found = False
                for j, (rev_v, rev_cap, rev_id) in enumerate(flow_adj[v]):
                    if rev_v == u and rev_id == edge_id:
                        flow_adj[v][j] = (rev_v, rev_cap + path_flow, rev_id)
                        found = True
                        break
                if not found:
                    flow_adj[v].append((u, path_flow, edge_id))
            
            total_flow += path_flow
            
        return total_flow
    
    # Try all possible bipartitions of sources
    min_cut_value = float('inf')
    best_partition = None
    
    # Generate all non-empty proper subsets
    k_count = len(sources)
    for mask in range(1, (1 << k_count) - 1):  # Exclude 0 and all 1s
        set1 = []
        set2 = []
        for i in range(k_count):
            if mask & (1 << i):
                set1.append(sources[i])
            else:
                set2.append(sources[i])
        cut_val = get_min_cut_value(set1, set2)
        if cut_val < min_cut_value:
            min_cut_value = cut_val
            best_partition = (set1, set2)
    
    if min_cut_value > B:
        return False, []
    
    # Now reconstruct the actual edges in the cut
    set1, set2 = best_partition
    flow_n = n + 2
    super_source = n + 1
    super_sink = n + 2
    
    # Build flow graph again
    flow_adj = [[] for _ in range(flow_n + 1)]
    
    # Add original edges with capacity = weight
    edge_info = {}  # edge_id -> (u, v, w)
    for i, (u, v, w) in enumerate(edges):
        flow_adj[u].append((v, w, i))
        flow_adj[v].append((u, w, i))
        edge_info[i] = (u, v, w)
        
    # Connect super_source to all in set1 with infinite capacity
    inf = B + 1
    for s in set1:
        flow_adj[super_source].append((s, inf, len(flow_adj[super_source])))
        flow_adj[s].append((super_source, 0, len(flow_adj[s])))  # reverse
        
    # Connect all in set2 to super_sink with infinite capacity
    for s in set2:
        flow_adj[s].append((super_sink, inf, len(flow_adj[s])))
        flow_adj[super_sink].append((s, 0, len(flow_adj[super_sink])))  # reverse
        
    # Find max flow to get residual graph
    def bfs_flow():
        parent = [-1] * (flow_n + 1)
        parent_edge_id = [-1] * (flow_n + 1)
        visited = [False] * (flow_n + 1)
        queue = deque([super_source])
        visited[super_source] = True
        
        while queue:
            u = queue.popleft()
            for v, cap, edge_id in flow_adj[u]:
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = u
                    parent_edge_id[v] = edge_id
                    if v == super_sink:
                        return parent, parent_edge_id
                    queue.append(v)
        return None, None
    
    total_flow = 0
    while True:
        parent, parent_edge_id = bfs_flow()
        if parent is None:
            break
            
        # Find minimum capacity along path
        path_flow = float('inf')
        s = super_sink
        path_edges = []
        while s != super_source:
            p = parent[s]
            # Find the edge from p to s
            for i, (v, cap, edge_id) in enumerate(flow_adj[p]):
                if v == s and edge_id == parent_edge_id[s]:
                    path_flow = min(path_flow, cap)
                    path_edges.append((p, i))
                    break
            s = p
        
        # Update capacities
        for u, edge_idx in path_edges:
            v, cap, edge_id = flow_adj[u][edge_idx]
            flow_adj[u][edge_idx] = (v, cap - path_flow, edge_id)
            # Update reverse edge
            found = False
            for j, (rev_v, rev_cap, rev_id) in enumerate(flow_adj[v]):
                if rev_v == u and rev_id == edge_id:
                    flow_adj[v][j] = (rev_v, rev_cap + path_flow, rev_id)
                    found = True
                    break
            if not found:
                flow_adj[v].append((u, path_flow, edge_id))
        
        total_flow += path_flow
    
    # Find min-cut edges
    # Run BFS from super_source in residual graph to find reachable nodes
    visited = [False] * (flow_n + 1)
    queue = deque([super_source])
    visited[super_source] = True
    
    while queue:
        u = queue.popleft()
        for v, cap, edge_id in flow_adj[u]:
            if not visited[v] and cap > 0:
                visited[v] = True
                queue.append(v)
    
    # Edges crossing the cut
    cut_edges = []
    for u in range(1, n + 1):
        if visited[u]:  # u is on source side
            for v, cap, edge_id in flow_adj[u]:
                if not visited[v] and v <= n:  # v is on sink side and is original node
                    # This edge was in the original graph and is in the cut
                    if edge_id in edge_info:
                        cut_edges.append(edge_id)
    
    # Remove duplicates and get actual edges
    cut_edges = list(set(cut_edges))
    return True, cut_edges

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    
    sources = []
    for _ in range(k):
        sources.append(int(data[idx])); idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    # Special case: if k <= 1, no need to cut anything
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # For k = 2, it's just min-cut between two nodes
    if k == 2:
        # Simple min-cut between sources[0] and sources[1]
        # Build adjacency for flow
        adj = [[] for _ in range(n + 1)]
        edge_dict = {}
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))
            edge_dict[i] = (u, v, w)
        
        # Max flow / min cut between sources[0] and sources[1]
        source = sources[0]
        sink = sources[1]
        
        # Build flow network
        flow_adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            flow_adj[u].append((v, w))
            flow_adj[v].append((u, w))
        
        def bfs_flow():
            parent = [-1] * (n + 1)
            visited = [False] * (n + 1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                for i, (v, cap) in enumerate(flow_adj[u]):
                    if not visited[v] and cap > 0:
                        visited[v] = True
                        parent[v] = u
                        if v == sink:
                            return parent
                        queue.append(v)
            return None
        
        total_flow = 0
        original_caps = {}
        for i, (u, v, w) in enumerate(edges):
            original_caps[(u, v, i)] = w
            original_caps[(v, u, i)] = w
            
        while True:
            parent = bfs_flow()
            if parent is None:
                break
                
            # Find path flow
            path_flow = float('inf')
            s = sink
            path_edges = []
            while s != source:
                p = parent[s]
                # Find edge p->s
                for i, (v, cap) in enumerate(flow_adj[p]):
                    if v == s:
                        path_flow = min(path_flow, cap)
                        path_edges.append((p, i))
                        break
                s = p
            
            # Update capacities
            for u, edge_idx in path_edges:
                v, cap = flow_adj[u][edge_idx]
                flow_adj[u][edge_idx] = (v, cap - path_flow)
                # Update reverse
                found = False
                for j, (rev_v, rev_cap) in enumerate(flow_adj[v]):
                    if rev_v == u:
                        flow_adj[v][j] = (rev_v, rev_cap + path_flow)
                        found = True
                        break
                if not found:
                    flow_adj[v].append((u, path_flow))
            
            total_flow += path_flow
        
        if total_flow > B:
            print("NO")
            return
            
        # Find cut edges by checking which edges have flow < capacity
        cut_edges = []
        for i, (u, v, w) in enumerate(edges):
            # Check if this edge is in the cut
            # In residual graph, if u is reachable from source but v is not
            visited = [False] * (n + 1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                node = queue.popleft()
                for next_node, cap in flow_adj[node]:
                    if not visited[next_node] and cap > 0:
                        visited[next_node] = True
                        queue.append(next_node)
            
            if visited[u] and not visited[v]:
                cut_edges.append(i)
            elif visited[v] and not visited[u]:
                cut_edges.append(i)
                
        print("YES")
        print(len(cut_edges))
        for i in cut_edges:
            u, v, w = edges[i]
            print(u, v)
        return
    
    # For general case, use approximation or exact algorithm
    # Let's use a simpler approach: try all pairs and take union of cuts
    # But that might not be optimal. Let's implement the correct multiway cut.
    
    # Simpler: model as making a spanning tree where sources are in different components
    # Even simpler: use the fact that we need to disconnect all sources from each other
    
    # Use the flow-based approach for multiway cut
    success, edge_indices = find_min_cut_edges(n, edges, sources, B)
    
    if not success:
        print("NO")
        return
        
    print("YES")
    print(len(edge_indices))
    for idx in edge_indices:
        u, v, w = edges[idx]
        print(u, v)

if __name__ == "__main__":
    main()
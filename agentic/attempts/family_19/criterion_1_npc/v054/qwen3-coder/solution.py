from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    streams = []
    for i in range(k):
        s, t, d = map(int, input().split())
        streams.append((s, t, d))
    
    edges = []
    edge_index = {}
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        edge_index[(u, v)] = i
        graph[u].append((v, i))
        capacity.append(cap)
    
    # Build flow network: nodes 0 to n+1
    # 0 is super source, n+1 is super sink
    # Routers are 1 to n
    # For each stream i: node n+2+i is stream source
    # For each stream i: node n+2+k+i is stream sink
    
    total_nodes = n + 2 + 2 * k
    source = 0
    sink = n + 1
    
    # Edge list for the new graph
    new_edges = []
    new_capacity = []
    new_graph = defaultdict(list)
    
    edge_mapping = {}  # maps (u,v) in original graph to indices in new_edges
    
    # Add edges from original network with infinite capacity initially
    for i in range(m):
        u, v = edges[i]
        idx = len(new_edges)
        new_edges.append((u, v))
        new_capacity.append(capacity[i])
        new_graph[u].append((v, idx))
        edge_mapping[(u, v)] = idx
    
    # Connect super source to each stream's source router
    for i in range(k):
        s, t, d = streams[i]
        idx = len(new_edges)
        new_edges.append((source, s))
        new_capacity.append(d)
        new_graph[source].append((s, idx))
    
    # Connect each stream's destination router to super sink
    for i in range(k):
        s, t, d = streams[i]
        idx = len(new_edges)
        new_edges.append((t, sink))
        new_capacity.append(d)
        new_graph[t].append((sink, idx))
    
    # Connect each router to corresponding stream nodes
    for i in range(k):
        s, t, d = streams[i]
        # Source router to stream source
        idx = len(new_edges)
        new_edges.append((s, n+2+i))
        new_capacity.append(d)
        new_graph[s].append((n+2+i, idx))
        
        # Stream sink to destination router
        idx = len(new_edges)
        new_edges.append((n+2+k+i, t))
        new_capacity.append(d)
        new_graph[n+2+k+i].append((t, idx))
        
        # Stream source to stream sink
        idx = len(new_edges)
        new_edges.append((n+2+i, n+2+k+i))
        new_capacity.append(d)
        new_graph[n+2+i].append((n+2+k+i, idx))
    
    def bfs(cap):
        parent = [-1] * len(new_edges)
        visited = [False] * total_nodes
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx in new_graph[u]:
                if not visited[v] and new_capacity[edge_idx] > cap[edge_idx]:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    def find_path_flow(parent, cap):
        if parent[sink] == -1:
            return 0, []
        
        path = []
        current = sink
        min_flow = float('inf')
        
        while current != source:
            prev, edge_idx = parent[current]
            path.append(edge_idx)
            min_flow = min(min_flow, new_capacity[edge_idx] - cap[edge_idx])
            current = prev
            
        return min_flow, path[::-1]
    
    # Initialize flow
    flow = [0] * len(new_edges)
    
    # Max flow algorithm
    while True:
        parent = bfs(flow)
        if parent is None:
            break
            
        min_flow, path = find_path_flow(parent, flow)
        if min_flow == 0:
            break
            
        for edge_idx in path:
            flow[edge_idx] += min_flow
    
    # Check if all demands are satisfied
    satisfied = True
    for i in range(k):
        s, t, d = streams[i]
        # Check flow from super source to stream source
        found_flow = 0
        for v, edge_idx in new_graph[source]:
            if v == s:
                found_flow = flow[edge_idx]
                break
        if found_flow != d:
            satisfied = False
            break
            
        # Check flow from stream destination to super sink
        found_flow = 0
        for v, edge_idx in new_graph[t]:
            if v == sink:
                found_flow = flow[edge_idx]
                break
        if found_flow != d:
            satisfied = False
            break
    
    if not satisfied:
        print("NO")
        return
    
    # Now we need to extract the flow on original edges
    result = []
    for i in range(k):
        stream_flow = [0] * m
        s, t, d = streams[i]
        
        # We'll do a flow decomposition for this stream
        # Build residual graph for this stream
        stream_edges = []
        stream_cap = []
        stream_graph = defaultdict(list)
        
        # Add original network edges with remaining capacity
        for j in range(m):
            u, v = edges[j]
            # Flow used by previous streams
            used = flow[edge_mapping[(u, v)]] if (u, v) in edge_mapping else 0
            stream_edges.append((u, v))
            stream_cap.append(capacity[j] - used)
            if capacity[j] - used > 0:
                idx = len(stream_edges) - 1
                stream_graph[u].append((v, idx))
        
        # Add demand constraint: s -> (n+2+i) -> (n+2+k+i) -> t
        demand_edges_start = len(stream_edges)
        stream_edges.append((s, n+2+i))  # source to stream source
        stream_cap.append(d)
        stream_graph[s].append((n+2+i, len(stream_edges)-1))
        
        stream_edges.append((n+2+k+i, t))  # stream sink to dest
        stream_cap.append(d)
        stream_graph[n+2+k+i].append((t, len(stream_edges)-1))
        
        stream_edges.append((n+2+i, n+2+k+i))  # stream source to sink
        stream_cap.append(d)
        stream_graph[n+2+i].append((n+2+k+i, len(stream_edges)-1))
        
        # Find path from s to t in this subgraph
        def dfs_path(node, target, visited, path_edges, current_flow):
            if node == target:
                return current_flow, path_edges[:]
            
            for neighbor, edge_idx in stream_graph[node]:
                if neighbor not in visited and stream_cap[edge_idx] > 0:
                    visited.add(neighbor)
                    path_edges.append(edge_idx)
                    min_edge_flow = min(current_flow, stream_cap[edge_idx])
                    result_dfs = dfs_path(neighbor, target, visited, path_edges, min_edge_flow)
                    if result_dfs[0] > 0:
                        return result_dfs
                    path_edges.pop()
                    visited.remove(neighbor)
            return 0, []
        
        remaining_demand = d
        while remaining_demand > 0:
            visited = set([n+2+i])
            flow_val, path = dfs_path(n+2+i, n+2+k+i, visited, [], remaining_demand)
            if flow_val == 0:
                print("NO")
                return
                
            # Update capacities and record flows on original edges
            for edge_idx in path:
                if edge_idx < m:  # Original edge
                    stream_flow[edge_idx] += flow_val
                stream_cap[edge_idx] -= flow_val
                
            remaining_demand -= flow_val
        
        result.append(stream_flow)
    
    print("YES")
    for flows in result:
        print(' '.join(map(str, flows)))

solve()
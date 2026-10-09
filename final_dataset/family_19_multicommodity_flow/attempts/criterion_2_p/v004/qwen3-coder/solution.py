from collections import defaultdict, deque
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index+1])
    index += 3  # skip the '1'
    
    s = int(data[index]) - 1  # Convert to 0-based indexing
    t = int(data[index+1]) - 1
    d = int(data[index+2])
    index += 3
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        cap = int(data[index+2])
        index += 3
        
        edges.append((u, v))
        graph[u].append(len(capacity))
        capacity.append(cap)
        graph[v].append(len(capacity))
        capacity.append(0)  # Reverse edge with 0 capacity initially
    
    # Add reverse edges for residual graph
    rev_edges = []
    for i in range(m):
        u, v = edges[i]
        rev_edges.append((v, u))
    
    # Total nodes including super source and sink
    super_source = n
    super_sink = n + 1
    total_nodes = n + 2
    
    # Extend graph for super source/sink
    graph[super_source] = []
    graph[super_sink] = []
    
    # Connect super_source to s with demand d
    graph[super_source].append(len(capacity))
    capacity.append(d)
    graph[s].append(len(capacity))
    capacity.append(0)
    
    # Connect t to super_sink with demand d
    graph[t].append(len(capacity))
    capacity.append(d)
    graph[super_sink].append(len(capacity))
    capacity.append(0)
    
    def bfs():
        parent = [-1] * total_nodes
        visited = [False] * total_nodes
        queue = deque([super_source])
        visited[super_source] = True
        
        while queue:
            u = queue.popleft()
            for i in graph[u]:
                v = edges_list[i][1] if i < len(edges_list) else rev_edges_list[i - len(edges_list)][1]
                if not visited[v] and capacity[i] > 0:
                    visited[v] = True
                    parent[v] = i
                    queue.append(v)
                    if v == super_sink:
                        return parent
        return None
    
    # Build edge list with indices
    edges_list = [(u,v) for u,v in edges]
    rev_edges_list = [(v,u) for u,v in edges]
    
    # Combine original edges and reverse edges
    all_edges = edges_list + rev_edges
    all_capacity = capacity[:]
    
    def edmonds_karp():
        max_flow = 0
        flows = [0] * m
        
        while True:
            parent = [-1] * total_nodes
            visited = [False] * total_nodes
            queue = deque([super_source])
            visited[super_source] = True
            
            while queue:
                u = queue.popleft()
                for idx in range(len(all_edges)):
                    v_node = all_edges[idx][1]
                    if not visited[v_node] and all_capacity[idx] > 0:
                        visited[v_node] = True
                        parent[v_node] = idx
                        queue.append(v_node)
                        if v_node == super_sink:
                            break
                if visited[super_sink]:
                    break
            
            if not visited[super_sink]:
                break
                
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_idx = super_sink
            path = []
            while s_idx != super_source:
                edge_idx = parent[s_idx]
                path.append(edge_idx)
                path_flow = min(path_flow, all_capacity[edge_idx])
                prev_node = all_edges[edge_idx][0]
                s_idx = prev_node
            
            # Update capacities and flows
            for edge_idx in path:
                all_capacity[edge_idx] -= path_flow
                # Find reverse edge index
                u, v = all_edges[edge_idx]
                for j in range(len(all_edges)):
                    if all_edges[j] == (v, u):
                        all_capacity[j] += path_flow
                        break
                        
                # Update flow for original edges
                if edge_idx < m:
                    flows[edge_idx] += path_flow
                elif edge_idx >= m and edge_idx < 2*m:
                    # This is a reverse edge, subtract from original
                    orig_idx = edge_idx - m
                    flows[orig_idx] -= path_flow
                    
            max_flow += path_flow
            
        return max_flow, flows
    
    # Since we're dealing with a complex graph, let's use a simpler approach:
    # Use Ford-Fulkerson with DFS
    
    def dfs(u, target, flow, visited, adj, cap):
        if u == target:
            return flow
        visited[u] = True
        for i in range(len(adj[u])):
            v_idx = adj[u][i]
            v = edges_list[v_idx][1] if v_idx < m else rev_edges_list[v_idx - m][1]
            if not visited[v] and cap[v_idx] > 0:
                bottleneck = dfs(v, target, min(flow, cap[v_idx]), visited, adj, cap)
                if bottleneck > 0:
                    cap[v_idx] -= bottleneck
                    # Find reverse edge
                    for j in range(len(edges_list)):
                        if edges_list[j] == (v, u):
                            cap[j] += bottleneck
                            break
                    return bottleneck
        return 0
    
    def max_flow_ford_fulkerson(source, sink, n_nodes):
        # Create adjacency list
        adj = [[] for _ in range(n_nodes)]
        cap = capacity[:]
        
        # Populate adjacency list
        for i in range(m):
            u, v = edges[i]
            adj[u].append(i)
            # Add reverse edge
            adj[v].append(i + m)
            
        total_flow = 0
        while True:
            visited = [False] * n_nodes
            flow = dfs(source, sink, float('inf'), visited, adj, cap)
            if flow == 0:
                break
            total_flow += flow
            
        return total_flow
    
    # Check if maximum flow meets demand
    result_flow = max_flow_ford_fulkerson(super_source, super_sink, total_nodes)
    
    if result_flow < d:
        print("NO")
        return
        
    # Reconstruct the actual flows by running a flow algorithm that tracks flows
    # Let's implement a cleaner version using network flow
    
    def solve_flow():
        # Build residual graph
        res_graph = [[0]*n for _ in range(n)]
        orig_cap = [0] * m
        
        for i in range(m):
            u, v = edges[i]
            res_graph[u][v] += capacity[i]
            orig_cap[i] = capacity[i]
            
        # Now create a new graph with super source and sink
        extended_n = n + 2
        extended_graph = [[0]*extended_n for _ in range(extended_n)]
        
        # Copy existing edges
        for i in range(n):
            for j in range(n):
                extended_graph[i][j] = res_graph[i][j]
                
        # Connect super source (n) to s
        extended_graph[n][s] = d
        # Connect t to super sink (n+1)
        extended_graph[t][n+1] = d
        
        # Run max flow from super_source to super_sink
        def bfs_extended(parent):
            visited = [False] * extended_n
            queue = deque([n])  # super source
            visited[n] = True
            
            while queue:
                u = queue.popleft()
                for v in range(extended_n):
                    if not visited[v] and extended_graph[u][v] > 0:
                        visited[v] = True
                        parent[v] = u
                        queue.append(v)
                        if v == n+1:  # super sink
                            return True
            return False
        
        def ford_fulkerson():
            parent = [-1] * extended_n
            max_flow = 0
            
            while bfs_extended(parent):
                path_flow = float('Inf')
                s_idx = n+1
                while s_idx != n:
                    path_flow = min(path_flow, extended_graph[parent[s_idx]][s_idx])
                    s_idx = parent[s_idx]
                    
                # update residual capacities
                v = n+1
                while v != n:
                    u = parent[v]
                    extended_graph[u][v] -= path_flow
                    extended_graph[v][u] += path_flow
                    v = parent[v]
                    
                max_flow += path_flow
                
            return max_flow
            
        max_flow = ford_fulkerson()
        if max_flow < d:
            return None, False
            
        # Extract flows on original edges
        flows = [0] * m
        for i in range(m):
            u, v = edges[i]
            # Flow is original capacity minus residual capacity
            flows[i] = orig_cap[i] - extended_graph[u][v]
            
        return flows, True
    
    flows, success = solve_flow()
    if not success:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, flows)))

if __name__ == "__main__":
    main()
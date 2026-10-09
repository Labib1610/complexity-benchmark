from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    s, t, d = map(int, input().split())
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))  # For residual graph
        capacity.append(cap)
    
    # Build a super source and super sink
    # Source connects to s with capacity d
    # t connects to sink with capacity d
    super_source = 0
    super_sink = n + 1
    
    # Add edges from super_source to s and t to super_sink
    new_edges_start = m
    graph[super_source].append((s, m))
    graph[s].append((super_source, m))
    capacity.append(d)
    
    graph[t].append((super_sink, m+1))
    graph[super_sink].append((t, m+1))
    capacity.append(d)
    
    # Add reverse edges for all original edges
    for i in range(m):
        u, v = edges[i]
        graph[v].append((u, m+2+i))
        graph[u].append((v, m+2+i))
        capacity.append(0)  # Reverse edge has 0 initial capacity
    
    total_nodes = n + 2
    total_edges = len(capacity)
    
    def bfs(source, sink, res):
        parent = [-1] * total_edges
        visited = [False] * (total_nodes + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor, edge_idx in graph[node]:
                if not visited[neighbor] and res[edge_idx] > 0:
                    visited[neighbor] = True
                    parent[edge_idx] = node
                    queue.append(neighbor)
                    if neighbor == sink:
                        return True, parent
        return False, parent
    
    def edmonds_karp(source, sink):
        # Initialize residual capacities
        res = capacity[:]
        max_flow = 0
        
        while True:
            found, parent = bfs(source, sink, res)
            if not found:
                break
                
            # Find minimum residual capacity along the path
            path_flow = float('inf')
            current = sink
            path_edges = []
            
            # Reconstruct path
            while current != source:
                # Find the edge that led to current
                found_edge = False
                for neighbor, edge_idx in graph[current]:
                    if neighbor == parent[edge_idx] and res[edge_idx] > 0:
                        path_flow = min(path_flow, res[edge_idx])
                        path_edges.append(edge_idx)
                        current = parent[edge_idx]
                        found_edge = True
                        break
                if not found_edge:
                    break
            
            # Update residual capacities
            for edge_idx in path_edges:
                res[edge_idx] -= path_flow
                # Find the reverse edge
                u, v = None, None
                if edge_idx < m:
                    u, v = edges[edge_idx]
                elif edge_idx == m:
                    u, v = super_source, s
                elif edge_idx == m+1:
                    u, v = t, super_sink
                else:
                    orig_idx = edge_idx - m - 2
                    v, u = edges[orig_idx]  # Reverse direction
                
                # Find reverse edge index
                reverse_edge_idx = -1
                for neighbor, idx in graph[v]:
                    if neighbor == u:
                        reverse_edge_idx = idx
                        break
                if reverse_edge_idx != -1:
                    res[reverse_edge_idx] += path_flow
            
            max_flow += path_flow
        
        return max_flow, res
    
    max_flow, residual = edmonds_karp(super_source, super_sink)
    
    if max_flow < d:
        print("NO")
        return
    
    # Extract flow on original edges
    flow = [0] * m
    for i in range(m):
        # Original forward edge capacity was capacity[i]
        # Residual now contains remaining capacity
        # Flow = original capacity - residual capacity
        flow[i] = capacity[i] - residual[i]
    
    print("YES")
    print(" ".join(map(str, flow)))

solve()
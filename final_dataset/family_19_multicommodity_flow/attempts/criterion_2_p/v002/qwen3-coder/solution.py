from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 3  # skip the '1'
    
    s = int(data[idx]) - 1  # Convert to 0-based indexing
    t = int(data[idx+1]) - 1
    d = int(data[idx+2])
    idx += 3
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        cap = int(data[idx+2])
        idx += 3
        
        edges.append((u, v))
        graph[u].append(len(capacity))
        graph[v].append(len(capacity))  # For residual graph
        capacity.append(cap)
    
    # Build residual graph
    adj = [[] for _ in range(n)]
    edge_ids = []  # To track original edge index for each edge in adj
    
    for i in range(m):
        u, v = edges[i]
        adj[u].append(v)  # Forward edge
        adj[v].append(u)  # Backward edge
        edge_ids.append(i)
        edge_ids.append(i)
        
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs(source, sink, parent_edge, parent_node):
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        parent_node[source] = -1
        
        while queue:
            u = queue.popleft()
            
            for i, v in enumerate(adj[u]):
                edge_idx = edge_ids.index(edge_ids[i]) if u < len(adj) else 0
                # This approach is getting complex. Let me restart with a cleaner implementation.
                pass
                
    # Let me restructure this properly
    
    # Rebuild with proper residual graph representation
    # Each edge in the original graph gets a forward and backward edge
    
    # Create edge mapping
    forward_edges = []
    backward_edges = []
    edge_index_map = {}  # Maps (u,v,i) to edge index in residual graph
    
    res_graph = [[] for _ in range(n)]
    res_capacity = []
    res_edge_info = []  # (original_edge_id, is_forward)
    
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        
        # Forward edge
        res_graph[u].append(len(res_capacity))
        res_capacity.append(cap)
        res_edge_info.append((i, True))
        
        # Backward edge
        res_graph[v].append(len(res_capacity))
        res_capacity.append(0)
        res_edge_info.append((i, False))
        
        forward_edges.append(len(res_capacity)-2)
        backward_edges.append(len(res_capacity)-1)
    
    def bfs_flow(source, sink, parent_edge):
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for edge_idx in res_graph[u]:
                to_node = -1
                # Determine the 'to' node based on edge direction
                # This is getting messy. Let me use adjacency with explicit storage.
                
                # Actually, let's rebuild the data structure cleanly:
                # For each original edge (u,v,cap), we create:
                # - Forward edge u->v with capacity cap
                # - Backward edge v->u with capacity 0
                
                # But we need to know the reverse mapping. Let me start over once more.
    
    # Clean restart with better data structures
    class FlowNetwork:
        def __init__(self, n):
            self.n = n
            self.graph = [[] for _ in range(n)]
            self.capacity = []
            self.edge_map = {}  # Maps (u,v,id) to edge indices
            
        def add_edge(self, u, v, cap, orig_id):
            # Add forward edge
            self.graph[u].append(len(self.capacity))
            self.capacity.append(cap)
            
            # Add backward edge
            self.graph[v].append(len(self.capacity))
            self.capacity.append(0)
            
        def bfs(self, source, sink, parent):
            visited = [False] * self.n
            queue = deque([source])
            visited[source] = True
            parent[source] = -1
            
            while queue:
                u = queue.popleft()
                
                for edge_idx in self.graph[u]:
                    # Determine where this edge goes
                    # We need to store destinations explicitly
                    pass
                    
            # This design isn't working well either. Let me do a textbook Edmonds-Karp.
            
    # Final clean attempt:
    INF = float('inf')
    
    # Residual graph representation
    res_graph_adj = [[] for _ in range(n)]  # Adjacency list storing (node, edge_id)
    res_edges = []  # (from, to, capacity, original_id, is_forward)
    
    # Build residual graph
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        
        # Forward edge
        res_graph_adj[u].append((v, len(res_edges)))
        res_edges.append((u, v, cap, i, True))
        
        # Backward edge
        res_graph_adj[v].append((u, len(res_edges)))
        res_edges.append((v, u, 0, i, False))
    
    flow_values = [0] * m  # Track flow on original edges
    
    def edmonds_karp(source, sink):
        total_flow = 0
        
        while True:
            # BFS to find augmenting path
            parent_edge = [-1] * n
            parent_node = [-1] * n
            visited = [False] * n
            queue = deque([source])
            visited[source] = True
            
            found = False
            
            while queue and not found:
                u = queue.popleft()
                
                for v, edge_id in res_graph_adj[u]:
                    if not visited[v] and res_edges[edge_id][2] > 0:  # capacity > 0
                        visited[v] = True
                        parent_edge[v] = edge_id
                        parent_node[v] = u
                        queue.append(v)
                        
                        if v == sink:
                            found = True
                            break
            
            if not found:
                break
                
            # Find minimum capacity along the path
            path_flow = INF
            cur = sink
            while cur != source:
                edge_id = parent_edge[cur]
                path_flow = min(path_flow, res_edges[edge_id][2])
                cur = parent_node[cur]
                
            # Update residual capacities and track flows
            cur = sink
            while cur != source:
                edge_id = parent_edge[cur]
                u, v, cap, orig_id, is_forward = res_edges[edge_id]
                
                # Update residual capacity
                res_edges[edge_id] = (u, v, cap - path_flow, orig_id, is_forward)
                
                # Update reverse edge
                reverse_edge_id = edge_id ^ 1  # XOR flips last bit
                ru, rv, rcap, rorig_id, ris_forward = res_edges[reverse_edge_id]
                res_edges[reverse_edge_id] = (ru, rv, rcap + path_flow, rorig_id, ris_forward)
                
                # Update flow values for original edges
                if is_forward:
                    flow_values[orig_id] += path_flow
                else:
                    flow_values[orig_id] -= path_flow
                    
                cur = parent_node[cur]
                
            total_flow += path_flow
            
        return total_flow
    
    max_flow = edmonds_karp(s, t)
    
    if max_flow >= d:
        print("YES")
        result = []
        for f in flow_values:
            result.append(str(f))
        print(" ".join(result))
    else:
        print("NO")

solve()
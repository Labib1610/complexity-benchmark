from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    cargo_types = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    capacities = []
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        limit = int(data[idx])
        idx += 1
        
        edges.append((u, v, limit))
        graph[u].append((v, i))
        reverse_graph[v].append((u, i))
        capacities.append(limit)
    
    # We model this as a max flow problem
    # Create a super source SS and super sink TT
    # SS -> s with capacity d
    # t -> TT with capacity d
    # For each node except s,t, we enforce flow conservation (inflow = outflow)
    # This is a circulation problem with demands
    
    # Actually, let's think of it as a max flow from s to t with value d
    # And each edge has capacity limits
    
    # Nodes: 1 to n
    # Source: s, Sink: t
    # Demand: d
    
    # Use Ford-Fulkerson or Edmonds-Karp algorithm
    
    # Let's build the residual graph
    # We'll use adjacency list with edge indices
    
    # But we need to be careful about multiple edges etc.
    # Let's just implement a clean Ford-Fulkerson
    
    # Actually, since we want EXACTLY d flow, we can model it as max flow = d
    
    def bfs_find_path(residual_graph, source, sink, parent_edge, parent_node):
        visited = [False] * (n+1)
        queue = deque([source])
        visited[source] = True
        parent_node[source] = -1
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx, forward in residual_graph[u]:
                if not visited[v] and forward:
                    visited[v] = True
                    parent_node[v] = u
                    parent_edge[v] = edge_idx
                    if v == sink:
                        return True
                    queue.append(v)
        return False
    
    # Build initial residual graph
    # For each edge (u,v,cap), we add (u,v,cap) forward and (v,u,0) backward
    residual_edges = []
    adj = [[] for _ in range(n+1)]
    
    # Add original edges
    for i in range(m):
        u, v, cap = edges[i]
        # Forward edge
        residual_edges.append((u, v, cap, True))   # (from, to, capacity, is_forward)
        # Backward edge
        residual_edges.append((v, u, 0, False))
        
        idx_forward = len(residual_edges) - 2
        idx_backward = len(residual_edges) - 1
        
        adj[u].append((v, idx_forward, True))
        adj[v].append((u, idx_backward, True))
    
    def edmonds_karp(source, sink, demand):
        # residual_edges contains all edges
        # adj[u] contains list of (v, edge_index, is_adj_list_entry)
        flow = 0
        parent_edge = [-1] * (n+1)
        parent_node = [-1] * (n+1)
        
        while flow < demand:
            # BFS to find augmenting path
            visited = [False] * (n+1)
            queue = deque([source])
            visited[source] = True
            
            found = False
            while queue:
                u = queue.popleft()
                
                for v, edge_idx, _ in adj[u]:
                    # Check if there's remaining capacity
                    if not visited[v] and residual_edges[edge_idx][2] > 0:
                        visited[v] = True
                        parent_edge[v] = edge_idx
                        parent_node[v] = u
                        if v == sink:
                            found = True
                            break
                        queue.append(v)
                if found:
                    break
            
            if not found:
                break
                
            # Find minimum capacity along the path
            path_flow = demand - flow
            current = sink
            while current != source:
                edge_idx = parent_edge[current]
                path_flow = min(path_flow, residual_edges[edge_idx][2])
                current = parent_node[current]
            
            if path_flow <= 0:
                break
                
            # Update residual capacities
            current = sink
            while current != source:
                edge_idx = parent_edge[current]
                residual_edges[edge_idx] = (
                    residual_edges[edge_idx][0],
                    residual_edges[edge_idx][1],
                    residual_edges[edge_idx][2] - path_flow,
                    residual_edges[edge_idx][3]
                )
                
                # Find the backward edge
                u = parent_node[current]
                v = current
                # Look for the reverse edge in adj[v] that goes to u
                for next_v, rev_edge_idx, _ in adj[v]:
                    if next_v == u and residual_edges[rev_edge_idx][3] == False:
                        residual_edges[rev_edge_idx] = (
                            residual_edges[rev_edge_idx][0],
                            residual_edges[rev_edge_idx][1],
                            residual_edges[rev_edge_idx][2] + path_flow,
                            residual_edges[rev_edge_idx][3]
                        )
                        break
                        
                current = parent_node[current]
            
            flow += path_flow
        
        return flow == demand, parent_edge, parent_node, residual_edges
    
    # But actually, let's simplify and re-implement cleanly
    # Let's create a proper residual graph representation
    
    class FlowNetwork:
        def __init__(self, n):
            self.n = n
            self.adj = [[] for _ in range(n+1)]  # adjacency list
            self.edge_list = []  # store all edges
        
        def add_edge(self, u, v, cap):
            # Add forward edge
            forward_idx = len(self.edge_list)
            self.edge_list.append([u, v, cap, 0])  # [from, to, cap, flow]
            self.adj[u].append(forward_idx)
            
            # Add backward edge
            backward_idx = len(self.edge_list)
            self.edge_list.append([v, u, 0, 0])
            self.adj[v].append(backward_idx)
            
            return forward_idx
        
        def bfs(self, source, sink, parent, parent_edge):
            visited = [False] * (self.n + 1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                
                for edge_idx in self.adj[u]:
                    edge = self.edge_list[edge_idx]
                    v = edge[1]
                    residual_capacity = edge[2] - edge[3]
                    
                    if not visited[v] and residual_capacity > 0:
                        visited[v] = True
                        parent[v] = u
                        parent_edge[v] = edge_idx
                        if v == sink:
                            return True
                        queue.append(v)
            return False
        
        def edmonds_karp(self, source, sink):
            parent = [-1] * (self.n + 1)
            parent_edge = [-1] * (self.n + 1)
            max_flow = 0
            
            while self.bfs(source, sink, parent, parent_edge):
                # Find minimum residual capacity along the path
                path_flow = float('inf')
                s = sink
                while s != source:
                    edge_idx = parent_edge[s]
                    edge = self.edge_list[edge_idx]
                    residual = edge[2] - edge[3]
                    path_flow = min(path_flow, residual)
                    s = parent[s]
                
                # Update residual capacities
                v = sink
                while v != source:
                    edge_idx = parent_edge[v]
                    self.edge_list[edge_idx][3] += path_flow  # update flow
                    # The backward edge is the paired edge
                    # Since we added forward then backward consecutively
                    backward_edge_idx = edge_idx ^ 1
                    self.edge_list[backward_edge_idx][3] -= path_flow
                    v = parent[v]
                
                max_flow += path_flow
                parent = [-1] * (self.n + 1)
                parent_edge = [-1] * (self.n + 1)
            
            return max_flow
    
    # Now build the network
    network = FlowNetwork(n)
    edge_indices = []
    
    for u, v, cap in edges:
        idx = network.add_edge(u, v, cap)
        edge_indices.append(idx)
    
    max_flow = network.edmonds_karp(s, t)
    
    if max_flow < d:
        print("NO")
        return
    
    # Extract the flow values
    result = []
    for i in range(m):
        edge_idx = edge_indices[i]
        flow = network.edge_list[edge_idx][3]
        result.append(str(flow))
    
    print("YES")
    print(" ".join(result))

solve()
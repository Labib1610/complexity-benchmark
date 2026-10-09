from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 3  # skip the '1'
    
    s = int(data[idx])
    t = int(data[idx+1])
    d = int(data[idx+2])
    idx += 3
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        cap = int(data[idx+2])
        idx += 3
        edges.append((u, v))
        graph[u].append((v, len(capacity)))
        graph[v].append((u, len(capacity)))  # reverse edge for residual graph
        capacity.append(cap)
    
    # Add reverse edges with 0 capacity
    for i in range(m):
        u, v = edges[i]
        graph[v].append((u, len(capacity)))
        capacity.append(0)
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v, edge_idx in graph[u]:
                if not visited[v] and capacity[edge_idx] > 0:
                    visited[v] = True
                    parent[v] = (u, edge_idx)
                    if v == t:
                        return parent
                    queue.append(v)
        return None
    
    max_flow = 0
    while True:
        parent = bfs()
        if parent is None:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        v = t
        while v != s:
            u, edge_idx = parent[v]
            path_flow = min(path_flow, capacity[edge_idx])
            v = u
            
        # Update capacities
        v = t
        while v != s:
            u, edge_idx = parent[v]
            capacity[edge_idx] -= path_flow
            # The reverse edge index is edge_idx ^ 1 if we added them consecutively
            # But since we're using indices, we need to be more careful
            # Actually, our construction adds forward edges first, then reverse edges
            # So for original edge i, reverse edge is at position i+m
            # But we've constructed the graph differently - let's track edge indices properly
            v = u
            
        max_flow += path_flow
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    # Now we need to find a feasible flow of exactly d
    # We can run a max flow algorithm again but with demand d
    # Or we can scale down if we have more than d
    # But since we just need to find any valid flow of value d, let's reconstruct
    
    # Reconstruct the flow values for original edges
    result = []
    for i in range(m):
        # The flow on edge i is the original capacity minus the current capacity
        # But we need to be more precise about how we track flows
        # Let's rebuild with proper flow tracking
        
        # Actually, let's restart with a cleaner implementation
        pass
    
    # Restart with a cleaner max-flow implementation
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 3  
    
    s = int(data[idx])
    t = int(data[idx+1])
    d = int(data[idx+2])
    idx += 3
    
    # Build graph for max flow
    edges_info = []
    graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        cap = int(data[idx+2])
        idx += 3
        edges_info.append((u, v, cap))
    
    # Use Ford-Fulkerson with proper edge indexing
    class FlowNetwork:
        def __init__(self, n):
            self.n = n
            self.adj = defaultdict(list)
            self.edges = []
            
        def add_edge(self, u, v, cap):
            self.edges.append([u, v, cap, 0])  # from, to, cap, flow
            self.edges.append([v, u, 0, 0])    # reverse edge
            idx = len(self.edges)
            self.adj[u].append(idx - 2)
            self.adj[v].append(idx - 1)
            
        def bfs(self, source, sink, parent):
            visited = [False] * (self.n + 1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                
                for edge_idx in self.adj[u]:
                    edge = self.edges[edge_idx]
                    v = edge[1]
                    residual_capacity = edge[2] - edge[3]
                    
                    if not visited[v] and residual_capacity > 0:
                        visited[v] = True
                        parent[v] = edge_idx
                        if v == sink:
                            return True
                        queue.append(v)
            return False
        
        def max_flow(self, source, sink):
            parent = [-1] * (self.n + 1)
            total_flow = 0
            
            while self.bfs(source, sink, parent):
                path_flow = float('inf')
                s_temp = sink
                
                # Find minimum capacity in the path
                while s_temp != source:
                    edge_idx = parent[s_temp]
                    edge = self.edges[edge_idx]
                    path_flow = min(path_flow, edge[2] - edge[3])
                    s_temp = edge[0]
                
                # Update residual capacities
                v = sink
                while v != source:
                    edge_idx = parent[v]
                    self.edges[edge_idx][3] += path_flow  # forward flow
                    self.edges[edge_idx ^ 1][3] -= path_flow  # backward flow
                    v = self.edges[edge_idx][0]
                
                total_flow += path_flow
                parent = [-1] * (self.n + 1)
                
            return total_flow
    
    # Create network
    fn = FlowNetwork(n)
    edge_indices = []
    
    for u, v, cap in edges_info:
        fn.add_edge(u, v, cap)
        edge_indices.append(len(fn.edges) - 2)
    
    max_f = fn.max_flow(s, t)
    
    if max_f < d:
        print("NO")
        return
    
    # Extract flows on original edges
    flows = []
    for edge_idx in edge_indices:
        flows.append(str(fn.edges[edge_idx][3]))
    
    print("YES")
    print(" ".join(flows))

if __name__ == "__main__":
    main()
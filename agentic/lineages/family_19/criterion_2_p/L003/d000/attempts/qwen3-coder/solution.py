from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    _ = int(data[index])
    index += 1
    
    s = int(data[index])
    index += 1
    t = int(data[index])
    index += 1
    d = int(data[index])
    index += 1
    
    edges = []
    capacities = []
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        cap = int(data[index])
        index += 1
        edges.append((u, v))
        capacities.append(cap)
        graph[u].append(i)
        reverse_graph[v].append(i)
    
    # Binary search on flow value
    # We'll use a max flow approach with a fixed flow value
    
    # Let's model this as a flow network and try to push exactly 'd' flow
    # We'll build the residual graph and check if we can push exactly 'd'
    
    def bfs_flow(flow_edges):
        # Build current graph with flow values
        in_flow = defaultdict(int)
        out_flow = defaultdict(int)
        
        for i in range(m):
            f = flow_edges[i]
            u, v = edges[i]
            in_flow[v] += f
            out_flow[u] += f
            
        # Check conservation laws
        for node in range(1, n+1):
            if node != s and node != t:
                if in_flow[node] != out_flow[node]:
                    return False
        if out_flow[s] - in_flow[s] != d:
            return False
        if in_flow[t] - out_flow[t] != d:
            return False
        return True
    
    # Try to find a feasible flow using circulation method
    # Add a temporary edge from t to s with capacity d
    # Then check if there exists a circulation that satisfies all constraints
    
    # But let's instead formulate it as a linear programming feasibility problem
    # And solve it using a max flow approach with lower bounds set to zero
    
    # We'll use the Ford-Fulkerson method with a twist to handle exact flow
    
    # Actually, let's reduce this to a max flow problem:
    # Create super source SS and super sink TT
    # Connect SS to s with capacity d
    # Connect t to TT with capacity d
    # All original edges have capacity = min(flow, capacity)
    # Find max flow from SS to TT, and check if it equals d
    
    # But since we want exactly d flow, we can do the following:
    # Set up a flow network and try to find a feasible flow of value d
    
    # Let's use the method of converting to circulation:
    # Add edge (t,s) with demand d and capacity d
    # For each edge, subtract flow and check if we can satisfy demands
    
    # Simpler approach: Use linear programming or network simplex
    # But since this is competitive programming, let's try to construct manually
    
    # Let's model this as a system of linear equations and inequalities:
    # Variables: f_i (flow on edge i)
    # Constraints:
    # 1. 0 <= f_i <= capacities[i]
    # 2. Flow conservation at each node except s,t
    # 3. Net flow out of s is d
    # 4. Net flow into t is d
    
    # This is essentially a min-cost max-flow problem with all costs 0
    # But we just want any feasible solution with flow value d
    
    # Let's implement a simple max-flow algorithm and modify it
    
    # Actually, let's think differently. 
    # We can model this as a circulation problem with demands.
    # Each edge has capacity capacities[i] and minimum flow 0
    # We add an edge from t to s with demand d (flow must be exactly d)
    
    # But let's stick to standard max-flow with a modification
    
    # Create adjacency list for flow network
    adj = [[] for _ in range(n+2)]  # nodes 1..n, plus SS=n+1, TT=n+2
    SS = n + 1
    TT = n + 2
    
    edge_list = []  # To store forward and backward edges
    
    # Add original edges
    for i in range(m):
        u, v = edges[i]
        cap = capacities[i]
        # Forward edge: idx = 2*i
        # Backward edge: idx = 2*i + 1
        adj[u].append(len(edge_list))
        edge_list.append([v, cap, 0])  # [to, capacity, flow]
        adj[v].append(len(edge_list))
        edge_list.append([u, 0, 0])
    
    # Add SS -> s with capacity d
    adj[SS].append(len(edge_list))
    edge_list.append([s, d, 0])
    adj[s].append(len(edge_list))
    edge_list.append([SS, 0, 0])
    
    # Add t -> TT with capacity d
    adj[t].append(len(edge_list))
    edge_list.append([TT, d, 0])
    adj[TT].append(len(edge_list))
    edge_list.append([t, 0, 0])
    
    # Now run max flow from SS to TT
    def max_flow(source, sink):
        def bfs():
            parent = [-1] * len(adj)
            visited = [False] * len(adj)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                for edge_idx in adj[u]:
                    edge = edge_list[edge_idx]
                    v = edge[0]
                    residual_capacity = edge[1] - edge[2]
                    if not visited[v] and residual_capacity > 0:
                        parent[v] = edge_idx
                        visited[v] = True
                        queue.append(v)
                        if v == sink:
                            return parent
            return None
        
        max_flow_value = 0
        while True:
            parent = bfs()
            if parent is None:
                break
                
            # Find minimum residual capacity along the path
            path_flow = float('inf')
            s = sink
            while s != source:
                edge_idx = parent[s]
                edge = edge_list[edge_idx]
                residual_capacity = edge[1] - edge[2]
                path_flow = min(path_flow, residual_capacity)
                # Find the previous node in the path
                prev_edge_idx = edge_idx ^ 1
                prev_node = edge_list[prev_edge_idx][0]
                s = prev_node
            
            # Update residual capacities
            v = sink
            while v != source:
                edge_idx = parent[v]
                edge_list[edge_idx][2] += path_flow  # Increase flow
                # Backward edge
                backward_edge_idx = edge_idx ^ 1
                edge_list[backward_edge_idx][2] -= path_flow
                # Find previous node
                prev_edge_idx = edge_idx ^ 1
                prev_node = edge_list[prev_edge_idx][0]
                v = prev_node
                
            max_flow_value += path_flow
            
        return max_flow_value
    
    flow_val = max_flow(SS, TT)
    
    if flow_val != d:
        print("NO")
        return
    
    # Extract flows on original edges
    result = []
    for i in range(m):
        forward_edge_idx = 2 * i
        flow_on_edge = edge_list[forward_edge_idx][2]
        result.append(str(flow_on_edge))
    
    print("YES")
    print(" ".join(result))

solve()
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
    _ = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    graph = defaultdict(list)
    capacity = {}
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        cap = int(data[idx])
        idx += 1
        
        edges.append((u, v, cap))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity[i] = cap
    
    # We model this as a min-cost max-flow problem by setting cost=1 for all edges
    # But actually, we just need to find a feasible flow of value d from s to t
    # This is equivalent to finding a circulation with demands
    
    # Let's use the standard approach:
    # Create a super-source and super-sink
    # Connect super-source to s with capacity d
    # Connect t to super-sink with capacity d
    # All other nodes have demand 0
    # All edges have lower bound 0 and upper bound capacity
    
    # But since we don't have lower bounds on nodes, we can directly model this as:
    # Find a flow of value d from s to t respecting edge capacities
    # And ensure flow conservation at intermediate nodes
    
    # Let's build the residual graph and use Ford-Fulkerson/Edmonds-Karp
    
    # Node IDs: 1 to n are original nodes
    # We'll run max-flow to see if we can get flow value d
    
    def bfs_flow(residual_graph, source, sink, parent_edge, parent_node):
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent_node[source] = -1
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx, forward in residual_graph[u]:
                if v not in visited and residual_graph[u][residual_graph[u].index((v, edge_idx, forward))][2] > 0:
                    visited.add(v)
                    parent_node[v] = u
                    parent_edge[v] = edge_idx if forward else -edge_idx - 1
                    if v == sink:
                        return True
                    queue.append(v)
        
        return False
    
    # Build initial residual graph
    # For each edge (u,v,cap), we add (u,v,cap) and (v,u,0)
    residual = defaultdict(list)
    
    for i, (u, v, cap) in enumerate(edges):
        # Forward edge
        residual[u].append((v, i, cap))
        # Backward edge
        residual[v].append((u, i, 0))
    
    # Now run Edmonds-Karp to find max flow
    flow_value = 0
    flow_on_edge = [0] * m
    
    while flow_value < d:
        parent_edge = {}
        parent_node = {}
        
        if not bfs_flow(residual, s, t, parent_edge, parent_node):
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        current = t
        path_edges = []
        
        while current != s:
            prev = parent_node[current]
            edge_idx = abs(parent_edge[current])
            forward = parent_edge[current] >= 0
            
            # Find the edge in residual graph
            for next_node, idx, res_cap in residual[prev]:
                if next_node == current and idx == edge_idx:
                    path_flow = min(path_flow, res_cap)
                    path_edges.append((prev, current, edge_idx, forward))
                    break
                    
            current = prev
        
        # Update residual capacities and flow
        current = t
        while current != s:
            prev = parent_node[current]
            edge_idx = abs(parent_edge[current])
            forward = parent_edge[current] >= 0
            
            # Update residual graph
            for i in range(len(residual[prev])):
                if residual[prev][i][1] == edge_idx and residual[prev][i][0] == current:
                    residual[prev][i] = (residual[prev][i][0], residual[prev][i][1], residual[prev][i][2] - path_flow)
                    break
            
            for i in range(len(residual[current])):
                if residual[current][i][1] == edge_idx and residual[current][i][0] == prev:
                    residual[current][i] = (residual[current][i][0], residual[current][i][1], residual[current][i][2] + path_flow)
                    break
            
            if forward:
                flow_on_edge[edge_idx] += path_flow
            else:
                flow_on_edge[edge_idx] -= path_flow
                
            current = prev
            
        flow_value += path_flow
    
    if flow_value < d:
        print("NO")
        return
    
    # Check flow conservation at intermediate nodes
    # And that all flows are non-negative and within capacity
    
    inflow = defaultdict(int)
    outflow = defaultdict(int)
    
    for i in range(m):
        u, v, _ = edges[i]
        f = flow_on_edge[i]
        if f < 0:
            print("NO")
            return
        outflow[u] += f
        inflow[v] += f
    
    for node in range(1, n+1):
        if node != s and node != t:
            if inflow[node] != outflow[node]:
                print("NO")
                return
    
    if outflow[s] - inflow[s] != d:
        print("NO")
        return
        
    if inflow[t] - outflow[t] != d:
        print("NO")
        return
    
    # Verify capacities
    for i in range(m):
        if flow_on_edge[i] > edges[i][2]:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, flow_on_edge)))

solve()
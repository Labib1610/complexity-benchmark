from collections import defaultdict, deque
import sys

def solve():
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
    
    frequencies = []
    for _ in range(k):
        s = int(data[idx])
        idx += 1
        t = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        frequencies.append((s, t, d))
    
    conduits = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        conduits.append((u, v, c))
    
    # Build graph
    graph = [[] for _ in range(n+1)]
    edge_id = {}
    for i, (u, v, c) in enumerate(conduits):
        graph[u].append((v, i))
        graph[v].append((u, i))  # For residual graph
        edge_id[(u, v)] = i
    
    def max_flow(source, sink, capacity, flow_req):
        # Edmonds-Karp implementation
        from collections import deque
        
        def bfs():
            parent = [-1] * (n + 1)
            edge_used = [-1] * (n + 1)
            q = deque()
            q.append(source)
            parent[source] = source
            
            while q:
                u = q.popleft()
                if u == sink:
                    break
                for v, eid in graph[u]:
                    if parent[v] == -1 and capacity[eid] > 0:
                        parent[v] = u
                        edge_used[v] = eid
                        q.append(v)
            return parent, edge_used
        
        total_flow = 0
        flows = [0] * m
        
        while total_flow < flow_req:
            parent, edge_used = bfs()
            if parent[sink] == -1:
                break
            
            # Find minimum capacity along path
            path_flow = flow_req - total_flow
            s = sink
            path_edges = []
            while s != source:
                eid = edge_used[s]
                path_flow = min(path_flow, capacity[eid])
                path_edges.append(eid)
                s = parent[s]
            
            if path_flow == 0:
                break
                
            # Update capacities and flows
            for eid in path_edges:
                capacity[eid] -= path_flow
                # Assuming reverse edges are handled properly
                # We'll handle residual graph separately if needed
                flows[eid] += path_flow
                
            total_flow += path_flow
            
        return total_flow == flow_req, flows
    
    # For each frequency, compute the flow
    all_flows = []
    total_usage = [0] * m
    
    for freq_idx, (s, t, d) in enumerate(frequencies):
        # Create a flow network for this frequency
        # We need to find a circulation that sends 'd' units from s to t
        # This is equivalent to finding a flow of value d from s to t
        
        # Capacity is current available capacity = cap - total_usage
        capacity = [conduits[i][2] - total_usage[i] for i in range(m)]
        
        # Run max flow
        success, flow_vals = max_flow(s, t, capacity.copy(), d)
        
        if not success:
            print("NO")
            return
            
        # Update total usage
        for i in range(m):
            total_usage[i] += flow_vals[i]
            
        all_flows.append(flow_vals)
    
    # Check if total usage exceeds capacity
    for i in range(m):
        if total_usage[i] > conduits[i][2]:
            print("NO")
            return
    
    print("YES")
    for flow_list in all_flows:
        print(' '.join(map(str, flow_list)))

solve()
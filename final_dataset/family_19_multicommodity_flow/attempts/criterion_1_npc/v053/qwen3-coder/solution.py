from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    compounds = []
    for i in range(k):
        s, t, d = map(int, input().split())
        compounds.append((s, t, d))
    
    edges = []
    edge_index = {}
    adj = defaultdict(list)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_index[(u, v)] = i
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # For each compound, find a flow from s to t with value d
    # This is a multi-commodity flow problem with integer constraints
    
    # We'll solve this by modeling it as a circulation problem with demands
    # and then using a max flow approach for each commodity separately,
    # checking if the total flow on each edge doesn't exceed capacity
    
    # But since we need integer flows and edge capacities are shared,
    # we'll try to find flows one by one and check capacity constraints
    
    # Let's use a different approach: for each compound, find a path or flow
    # and then check if the total usage of edges is within capacity
    
    # Actually, let's model this properly:
    # For each compound i, we need to find a flow of value d_i from s_i to t_i
    # The sum of all flows on each edge must not exceed its capacity
    
    # This is a multi-commodity flow problem. We'll try to solve it greedily
    # by finding flows one by one and checking capacity constraints
    
    def bfs_flow(s, t, d, capacities):
        # Find a flow of value d from s to t using BFS
        # Returns the flow on each edge, or None if not possible
        # This is a simplified version - we'll find a path and push flow
        
        # Build residual graph
        res_graph = defaultdict(lambda: defaultdict(int))
        edge_ids = defaultdict(dict)
        
        for i, (u, v, cap) in enumerate(edges):
            res_graph[u][v] += capacities[i]
            edge_ids[u][v] = i
        
        # Try to find a path and push flow
        flow_edges = [0] * m
        
        for _ in range(d):
            # BFS to find a path from s to t
            parent = {}
            queue = deque([s])
            parent[s] = None
            
            found = False
            while queue:
                node = queue.popleft()
                if node == t:
                    found = True
                    break
                    
                for next_node, edge_id in adj[node]:
                    if next_node not in parent and res_graph[node][next_node] > 0:
                        parent[next_node] = (node, edge_id)
                        queue.append(next_node)
            
            if not found:
                return None  # Cannot push more flow
                
            # Push 1 unit of flow along the path
            curr = t
            while parent[curr] is not None:
                prev_node, edge_id = parent[curr]
                flow_edges[edge_id] += 1
                res_graph[prev_node][curr] -= 1
                res_graph[curr][prev_node] += 1
                curr = prev_node
        
        return flow_edges
    
    # Try to find flows for all compounds
    all_flows = []
    total_usage = [0] * m
    
    for s, t, d in compounds:
        # For each compound, find a flow considering current total usage
        remaining_capacity = [edges[i][2] - total_usage[i] for i in range(m)]
        
        flow = bfs_flow(s, t, d, remaining_capacity)
        if flow is None:
            print("NO")
            return
            
        all_flows.append(flow)
        for i in range(m):
            total_usage[i] += flow[i]
    
    # Check if all flows are valid
    for i in range(m):
        if total_usage[i] > edges[i][2]:
            print("NO")
            return
    
    print("YES")
    for flow in all_flows:
        print(' '.join(map(str, flow)))

solve()
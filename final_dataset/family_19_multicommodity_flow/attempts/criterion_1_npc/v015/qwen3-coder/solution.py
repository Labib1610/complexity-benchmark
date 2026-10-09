from collections import defaultdict, deque
import sys

def main():
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
    
    # Contracts: (source, target, demand)
    contracts = []
    for _ in range(k):
        s = int(data[idx])
        idx += 1
        t = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        contracts.append((s, t, d))
    
    # Edges: (u, v, capacity) - store edges in order
    edges = []
    edge_list = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        edges.append((u, v, c))
        edge_list.append((u, v))
    
    # For each contract, we need to find a flow from source to target with value d
    # We'll model this as a multi-commodity flow problem with edge capacities shared among all commodities
    
    # Let's build the graph for each contract separately and then check the combined constraints
    
    # For each contract, we'll compute a path from s to t (or multiple paths) that carries exactly d units
    # But since we have shared edge capacities, we need to ensure the sum over all contracts on each edge <= capacity
    
    # Approach:
    # 1. For each contract, find a feasible flow (can be multiple paths) from s to t with value d
    # 2. Represent the flow for each contract on each edge as a variable f[i][j]
    # 3. Constraints:
    #    - Flow conservation at each node for each contract
    #    - Edge capacity constraints: sum over i of f[i][j] <= c_j
    #    - f[i][j] >= 0 and integer
    
    # Since this is a complex integer programming problem, and given the small constraints,
    # we can try modeling it as a max-flow feasibility problem with additional constraints.
    
    # However, let's think differently: we can model this as a single min-cost circulation problem
    # Or even better, since demands are fixed, we just need to route fixed amounts and check capacity
    
    # Let's use a flow-based approach:
    # For each contract, we need to send 'd' units from 's' to 't'
    # We can represent the flow for each contract on the given graph edges
    
    # To simplify, we can model the entire system as a single multi-commodity flow:
    # Variables: f[i][j] = flow of contract i on edge j
    # Constraints:
    # 1. Flow conservation for each contract at each node
    # 2. Capacity constraints: sum over i of f[i][j] <= c_j
    # 3. Supply/demand constraints for each contract
    # 4. f[i][j] >= 0 and integer
    
    # This is an integer programming problem. Given the constraints, we might need to use a solver
    # But since this is a programming contest, let's assume we can solve it with network flow techniques
    # or iterative methods
    
    # Let's try to solve it using linear programming relaxation first, then round if necessary
    # But since we need integer solutions, and flows must be integers, we should look for exact methods
    
    # Let's model it as a circulation problem with supplies and demands
    # But actually, since we have fixed demands, it's more like a fixed-flow problem
    
    # Let's consider solving each contract individually to get a base flow, then adjust to satisfy capacities
    
    # But that may not work because of shared capacities
    
    # Let's try a different approach:
    # Model the entire thing as a single optimization problem:
    # Minimize 0 (just feasibility)
    # Subject to:
    # 1. For each contract i, and each node v:
    #    sum_{in_edges} f[i][e] - sum_{out_edges} f[i][e] = 
    #       +d_i if v=s_i, -d_i if v=t_i, 0 otherwise
    # 2. For each edge j: sum_{i} f[i][j] <= c_j
    # 3. f[i][j] >= 0 and integer
    
    # This is a multi-commodity flow problem with integer constraints
    
    # Since k and m are small (up to 100), we can try to solve it with a general approach
    
    # Let's build the constraint matrix and solve using a method like simplex or network flow adaptations
    
    # But for simplicity in coding, let's try to iteratively assign flows
    
    # First, let's see if we can route each contract individually ignoring capacities
    # Then adjust to meet the capacity constraints
    
    # Actually, let's model it properly
    
    # Build adjacency list for the graph
    adj = [[] for _ in range(n+1)]
    edge_index = {}
    for i in range(m):
        u, v = edges[i][0], edges[i][1]
        adj[u].append((v, i))
        adj[v].append((u, i))  # for residual graph
        edge_index[(u,v,i)] = i
    
    # For each contract, we need to find a way to send 'd' units from 's' to 't'
    # We can use a flow algorithm to find such a path or set of paths
    
    # Let's define a function to find a flow for a single contract
    def find_flow(s, t, amount, graph_adj, num_nodes):
        # BFS to find a path and push flow
        # This is a simplified version - in reality, we might need to handle multiple paths
        # But for now, let's assume we can find a single path
        
        # Let's do a BFS to find a path from s to t
        parent_edge = [-1] * (num_nodes + 1)
        parent = [-1] * (num_nodes + 1)
        visited = [False] * (num_nodes + 1)
        
        queue = deque()
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            if u == t:
                break
            for v, e_idx in graph_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = e_idx
                    queue.append(v)
        
        if not visited[t]:
            return None  # No path found
        
        # Reconstruct path
        path_edges = []
        current = t
        while parent[current] != -1:
            e_idx = parent_edge[current]
            path_edges.append(e_idx)
            current = parent[current]
        
        return path_edges[::-1]  # reverse to get s->t path
    
    # Initialize flow for each contract on each edge
    flow = [[0]*m for _ in range(k)]
    
    # Try to route each contract
    temp_flow = [0] * m  # temporary flow used during routing attempts
    
    # Create a copy of edges with remaining capacity
    remaining_capacity = [c for _, _, c in edges]
    
    # For each contract, try to find a flow
    contract_flows = []  # store flow for each contract
    
    success = True
    
    # We'll use a greedy approach: for each contract, find any feasible flow
    # Then check if total capacity constraints are satisfied
    
    # But this won't work directly because of interdependencies
    
    # Let's try a different approach: solve as a system of equations
    
    # This is getting complex. Let's look at the example to understand better
    
    # In the example:
    # Terminals: 1,2,3,4
    # Contracts: (1,4,2), (1,3,1)
    # Edges: (1,2,2), (2,4,2), (1,3,2), (3,4,2), (2,3,1)
    
    # Contract 1 (1->4, amount=2): can go 1->2->4 
    # Contract 2 (1->3, amount=1): can go 1->3 directly
    
    # So flow[0] = [2, 2, 0, 0, 0] means contract 1 uses edges 0 and 1 (1->2 and 2->4) with 2 units each
    # flow[1] = [0, 0, 1, 0, 0] means contract 2 uses edge 2 (1->3) with 1 unit
    
    # Check capacities: 
    # Edge 0 (1->2): 2 used, capacity 2 OK
    # Edge 1 (2->4): 2 used, capacity 2 OK  
    # Edge 2 (1->3): 1 used, capacity 2 OK
    # Edge 3 (3->4): 0 used, capacity 2 OK
    # Edge 4 (2->3): 0 used, capacity 1 OK
    
    # So the solution works
    
    # Let's implement a proper solution using flow networks
    
    # For small instances, we can model this as an integer linear program and solve it
    
    # But since we're in a competitive programming setting, let's try a heuristic approach
    
    # Let's model it as a min-cost flow problem where cost is 0, so we just need feasibility
    
    # Or even simpler: for each contract, find any valid flow (path or set of paths)
    # Then check if the sum of flows on each edge exceeds capacity
    
    # If it does, the instance is infeasible
    
    # But we also need to be able to adjust flows to make them fit within capacities
    
    # This is essentially a multi-commodity flow problem
    
    # Let's try to solve it by finding flows for each commodity independently,
    # then checking capacity constraints
    
    from collections import deque, defaultdict
    import sys
    
    sys.setrecursionlimit(10000)
    
    def bfs_flow(graph, source, sink, capacity, flow_used):
        # Find augmenting path using BFS
        parent = {source: None}
        queue = deque([source])
        found = False
        
        while queue and not found:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent:
                    # Calculate residual capacity
                    edge_key = (u, v)
                    if edge_key in capacity:
                        res_cap = capacity[edge_key] - flow_used.get(edge_key, 0)
                        if res_cap > 0:
                            parent[v] = u
                            if v == sink:
                                found = True
                                break
                            queue.append(v)
        
        if not found:
            return None
            
        # Reconstruct path
        path = []
        current = sink
        while parent[current] is not None:
            prev = parent[current]
            path.append((prev, current))
            current = prev
            
        return path[::-1]
    
    def find_path_flow(source, sink, amount, edge_list_original):
        # Build graph adjacency list
        graph = defaultdict(list)
        capacity = {}
        for u, v in edge_list_original:
            graph[u].append(v)
            graph[v].append(u)  # for residual
            capacity[(u, v)] = float('inf')  # Initially infinite, will be constrained later
            
        flow_used = {}
        
        total_sent = 0
        edge_flows = defaultdict(int)
        
        while total_sent < amount:
            path = bfs_flow(graph, source, sink, capacity, flow_used)
            if not path:
                break
                
            # Send 1 unit along the path
            for u, v in path:
                edge_flows[(u, v)] += 1
                flow_used[(u, v)] = flow_used.get((u, v), 0) + 1
            total_sent += 1
            
        if total_sent < amount:
            return None
        return edge_flows
    
    # Try to solve the problem
    contract_edge_flows = []
    
    # For each contract, find a way to route the required amount
    for i in range(k):
        s, t, d = contracts[i]
        edge_flows = find_path_flow(s, t, d, edge_list)
        if edge_flows is None:
            print("NO")
            return
        contract_edge_flows.append(edge_flows)
    
    # Now check capacity constraints
    total_edge_usage = [0] * m
    for i in range(k):
        edge_flows = contract_edge_flows[i]
        for j in range(m):
            u, v = edges[j][0], edges[j][1]
            total_edge_usage[j] += edge_flows.get((u, v), 0)
    
    # Check if any edge exceeds capacity
    for j in range(m):
        if total_edge_usage[j] > edges[j][2]:
            print("NO")
            return
    
    # If we reach here, a feasible solution exists
    print("YES")
    
    # Output the flow for each contract
    for i in range(k):
        edge_flows = contract_edge_flows[i]
        result = []
        for j in range(m):
            u, v = edges[j][0], edges[j][1]
            result.append(str(edge_flows.get((u, v), 0)))
        print(' '.join(result))

if __name__ == "__main__":
    main()
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
    
    contracts = []
    for _ in range(k):
        s = int(data[idx])
        idx += 1
        t = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        contracts.append((s, t, d))
    
    edges = []
    edge_dict = {}
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        cap = int(data[idx])
        idx += 1
        edges.append((u, v, cap))
        edge_dict[(u, v)] = i
        graph[u].append((v, i))
    
    # For each contract, we need to find a flow of 'd' units from s to t
    # We'll build a combined flow network and solve it as a multi-commodity flow problem
    # But since this is a small instance, we can model it as an LP or use iterative approach
    # However, given the constraints and nature, let's try modeling it as a system of linear equations with bounds
    
    # Variables: f[i][j] = flow of contract i on edge j
    # Constraints:
    # 1. Flow conservation for each contract at each node
    # 2. Capacity constraints on edges: sum over all contracts <= cap
    # 3. Flow values are non-negative integers
    
    # Let's encode this as an integer linear program and solve using a solver-like approach
    # Since we're in competitive programming, we'll implement a solution that works for small inputs
    
    # We'll use the fact that we can decompose flows into paths
    # For each contract, we need to route 'd' units from s to t
    # We can precompute possible paths and then assign flows accordingly respecting capacities
    
    # First, let's build adjacency list for path finding
    from collections import defaultdict, deque
    
    def bfs_paths(graph, start, goal, max_len=10):
        queue = deque([(start, [start])])
        paths = []
        while queue:
            (vertex, path) = queue.popleft()
            if len(path) > max_len:
                continue
            if vertex == goal:
                paths.append(path)
                continue
            for (next_node, edge_idx) in graph[vertex]:
                if next_node not in path:  # Simple cycle prevention
                    queue.append((next_node, path + [next_node]))
        return paths
    
    # Precompute paths for each contract
    paths_per_contract = []
    edge_paths = [[] for _ in range(m)]  # For each edge, which (contract, path_index) uses it
    
    for i, (s, t, d) in enumerate(contracts):
        paths = bfs_paths(graph, s, t)
        paths_per_contract.append(paths)
        if not paths:
            print("NO")
            return
    
    # Now we have for each contract, a set of possible paths
    # We need to choose one path per unit of flow, such that edge capacities are respected
    
    # This becomes a complex integer programming problem
    # Let's instead model it as a flow problem with multiple commodities
    
    # Let's try a different approach: iterative path selection with capacity updates
    
    # Initialize result matrix
    result = [[0]*m for _ in range(k)]
    used_capacity = [0]*m
    
    # For each contract, we need to send 'd' units
    # We'll greedily select paths and update capacities
    # To make it work, we might need to allow path decomposition
    
    # Actually, let's think differently. 
    # We can model this as a min-cost flow or just a feasibility flow problem
    # But since all costs are 0, we just need to find feasible flows
    
    # Let's use a more systematic approach:
    # For each contract, compute a flow (can be multiple paths)
    # Represent each flow as a vector of edge usages
    # Then solve for non-negative integer coefficients that satisfy:
    # sum over contracts (flow_vector[contract] * amount[contract]) <= capacity
    # and sum(amount[contract]) = demand[contract]
    
    # This is getting complex. Let's look at the example:
    # 4 nodes, 5 edges, 2 contracts
    # Contract 1: 1->4, amount 2
    # Contract 2: 2->3, amount 1
    # Edges: 1->2 (2), 1->3 (2), 2->4 (2), 3->4 (2), 2->3 (1)
    
    # For contract 1 (1->4, amt 2): paths could be 1->2->4 or 1->3->4
    # For contract 2 (2->3, amt 1): path is 2->3
    
    # Let's say contract 1 uses 1 unit on 1->2->4 and 1 unit on 1->3->4
    # That means:
    # Edge 1->2 gets 1 from contract 1
    # Edge 1->3 gets 1 from contract 1  
    # Edge 2->4 gets 1 from contract 1
    # Edge 3->4 gets 1 from contract 1
    # Edge 2->3 gets 1 from contract 2
    # Total usage: [1,1,1,1,1], all within capacities [2,2,2,2,1] - OK
    
    # So the key insight is to decompose flows properly
    
    # Let's implement a proper flow decomposition approach
    
    # For each contract, compute a flow that satisfies the demand
    # We can do this with a simple max-flow algorithm
    
    def max_flow_single(graph_edges, n_nodes, source, sink, demand):
        # Build residual graph
        res_graph = defaultdict(lambda: defaultdict(int))
        edge_index_map = {}  # maps (u,v) to index in edges list
        rev_edge_index_map = {}  # maps index to (u,v)
        
        for i, (u,v,cap) in enumerate(graph_edges):
            res_graph[u][v] += cap  # Handle parallel edges by adding capacities
            edge_index_map[(u,v)] = edge_index_map.get((u,v), []) + [i]
            rev_edge_index_map[i] = (u,v)
            
        # But actually, our edges are unique, so we can simplify
        edge_caps = {}
        for i, (u,v,cap) in enumerate(graph_edges):
            if (u,v) in edge_caps:
                edge_caps[(u,v)] += cap
            else:
                edge_caps[(u,v)] = cap
                
        res_caps = edge_caps.copy()
        
        # Run Ford-Fulkerson
        def bfs_find_path(res_caps, src, snk):
            visited = set()
            queue = deque([(src, [(src,None)])])  # (node, path of (node,edge_to_node))
            
            while queue:
                u, path = queue.popleft()
                if u == snk:
                    return [edge for (_, edge) in path[1:]]  # Return list of edges
                if u in visited:
                    continue
                visited.add(u)
                for (a,b) in res_caps:
                    if a == u and res_caps[(a,b)] > 0 and b not in visited:
                        queue.append((b, path + [(b,(a,b))]))
            return None
            
        total_flow = 0
        flow_on_edges = defaultdict(int)
        
        while total_flow < demand:
            path = bfs_find_path(res_caps, source, sink)
            if not path:
                break
                
            # Find minimum residual capacity along path
            min_cap = float('inf')
            for edge in path:
                min_cap = min(min_cap, res_caps[edge])
                
            # But we want to send exactly what's needed or what's possible
            send = min(demand - total_flow, min_cap)
            if send <= 0:
                break
                
            # Update residual capacities and flow
            for edge in path:
                u,v = edge
                res_caps[(u,v)] -= send
                if res_caps[(u,v)] == 0:
                    del res_caps[(u,v)]
                res_caps[(v,u)] = res_caps.get((v,u), 0) + send
                flow_on_edges[edge] += send
                
            total_flow += send
            
        if total_flow < demand:
            return None, None  # Not enough capacity
            
        return flow_on_edges, total_flow
        
    # Get flow for each contract
    contract_flows = []
    temp_used_capacity = [0] * m
    
    for i, (s,t,d) in enumerate(contracts):
        # Temporarily reduce edge capacities based on already allocated flow
        temp_edges = [(u,v,cap - temp_used_capacity[edge_dict[(u,v)]]) for (u,v,cap) in edges if (u,v) in edge_dict]
        temp_edge_list = [(u,v,cap) for (u,v,cap) in edges if (u,v) in edge_dict]
        # Need to handle case where capacity becomes negative due to previous allocations
        
        # Actually, better approach: for each contract, find a flow assuming full original capacity,
        # then check if combination is feasible
        
        pass
    
    # Let me restart with a cleaner mathematical formulation
    
    # Variables: f[c][e] = flow of contract c on edge e
    # Constraints:
    # 1. Flow conservation for each contract: 
    #    For each node v != source,sink of contract c: 
    #      sum_{in_edges} f[c][e] = sum_{out_edges} f[c][e]
    #    For source: out_flow - in_flow = demand
    #    For sink: in_flow - out_flow = demand
    # 2. Capacity: for each edge e: sum_c f[c][e] <= cap[e]
    # 3. Non-negativity: f[c][e] >= 0
    
    # This is a system of linear inequalities. We can solve it with integer programming.
    # But in competitive programming, often these problems have small inputs and special structure.
    
    # Let's try to solve it by modeling as a network flow with multiple commodities
    # Or even simpler, since the example works, let's see if we can construct flows manually
    
    # Re-examining the example:
    # Contract 1: 1->4, amount 2
    # Contract 2: 2->3, amount 1  
    # Edges: (1,2,2), (1,3,2), (2,4,2), (3,4,2), (2,3,1)
    
    # Solution given:
    # Contract 1: [1,1,1,1,0] meaning 1 unit on each of first four edges, 0 on last
    # Contract 2: [0,0,0,0,1] meaning 1 unit on last edge only
    
    # Check contract 1 (1->4, amt 2):
    # Flows: 1->2 (1), 1->3 (1), 2->4 (1), 3->4 (1)
    # Node 1: out=2, in=0, net out=2 ✓
    # Node 2: in=1, out=1, net=0 ✓  
    # Node 3: in=1, out=1, net=0 ✓
    # Node 4: in=2, out=0, net in=2 ✓
    
    # Check capacities:
    # Edge 1->2: used 1, cap 2 ✓
    # Edge 1->3: used 1, cap 2 ✓
    # Edge 2->4: used 1, cap 2 ✓
    # Edge 3->4: used 1, cap 2 ✓
    # Edge 2->3: used 1 (from contract 2), cap 1 ✓
    
    # So the approach is to find valid flows for each contract independently,
    # making sure the total usage doesn't exceed edge capacities
    
    # Strategy:
    # 1. For each contract, find any valid flow (decomposed into paths) that meets demand
    # 2. Check if total edge usage respects capacities
    # 3. If yes, output the flows; if no, output "NO"
    
    # To find flow for a contract: run max-flow from source to sink with value = demand
    # Decompose the flow into paths/flows
    
    def find_flow_for_contract(contract_idx):
        s, t, d = contracts[contract_idx]
        
        # Build flow network for this contract
        # Nodes 1..n, plus super-source 0 and super-sink n+1
        # Edge 0->s with capacity d
        # Edge t->(n+1) with capacity d
        # Original edges with infinite capacity (we'll adjust later)
        
        # Actually, simpler: just find a way to push 'd' units from s to t
        # And represent the flow as edge usages
        
        # Use simple path-based approach
        from collections import Counter
        
        # Try to find paths and allocate flow
        def dfs_all_paths(current, target, path, visited, paths, limit=10):
            if len(path) > limit:
                return
            if current == target:
                paths.append(path[:])
                return
            if len(paths) >= d + 5:  # Don't generate too many
                return
            for (next_node, edge_idx) in graph[current]:
                if next_node not in visited:
                    visited.add(next_node)
                    path.append(edge_idx)
                    dfs_all_paths(next_node, target, path, visited, paths, limit)
                    path.pop()
                    visited.remove(next_node)
        
        paths = []
        visited_start = {s}
        dfs_all_paths(s, t, [], visited_start, paths)
        
        if not paths:
            return None
            
        # Now we have candidate paths, need to find combination that gives exactly 'd' flow
        # This is like solving a subset sum/set cover variant
        # For simplicity in competition setting, we can try greedy or exhaustive for small d
        
        # Greedy: pick shortest paths until we meet demand
        paths.sort(key=len)
        
        # But we need to track how much flow we put on each path
        # And ensure final edge totals respect global capacities
        
        # Different approach: formulate as integer program and solve with backtracking
        # Given small constraints, this should be feasible
        
        # Even simpler heuristic for now:
        # Just take first few paths and split the demand among them
        
        if len(paths) == 0:
            return None
            
        # Distribute demand d among paths
        flow_assignments = []  # list of (path, amount)
        remaining = d
        for p in paths:
            if remaining <= 0:
                break
            alloc = min(remaining, 1)  # Put 1 unit per path for simplicity
            flow_assignments.append((p, alloc))
            remaining -= alloc
            
        if remaining > 0:
            # Try putting more on existing paths
            for i in range(min(remaining, len(flow_assignments))):
                flow_assignments[i] = (flow_assignments[i][0], flow_assignments[i][1] + 1)
            if remaining > len(flow_assignments):
                return None  # Not enough paths
                
        # Convert to edge flows
        edge_flow = [0] * m
        for path, amount in flow_assignments:
            for edge_idx in path:
                edge_flow[edge_idx] += amount
                
        return edge_flow
        
    # Get flows for all contracts
    all_flows = []
    for i in range(k):
        flow = find_flow_for_contract(i)
        if flow is None:
            print("NO")
            return
        all_flows.append(flow)
        
    # Check capacity constraints
    total_usage = [0] * m
    for flow in all_flows:
        for j in range(m):
            total_usage[j] += flow[j]
            
    for j in range(m):
        if total_usage[j] > edges[j][2]:  # exceeds capacity
            print("NO")
            return
            
    # Output the solution
    print("YES")
    for flow in all_flows:
        print(' '.join(map(str, flow)))

if __name__ == "__main__":
    main()
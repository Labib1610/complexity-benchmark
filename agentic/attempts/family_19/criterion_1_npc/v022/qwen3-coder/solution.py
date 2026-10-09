from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    streams = []
    for i in range(k):
        s, t, d = map(int, input().split())
        streams.append((s, t, d))
    
    edges = []
    edge_index = {}
    capacity = []
    graph = defaultdict(list)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        edge_index[(u, v)] = i
        capacity.append(cap)
        graph[u].append((v, i))
    
    # For each stream, find all possible paths from source to target
    def find_paths(source, target):
        # BFS to find all simple paths (since graph is small)
        paths = []
        queue = deque([(source, [source], set([source]))])  # node, path, visited
        
        while queue:
            node, path, visited = queue.popleft()
            if node == target:
                paths.append(path[:])
                continue
            if len(path) > n:  # Prevent too long paths
                continue
                
            for neighbor, edge_idx in graph[node]:
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor], new_visited))
        
        # Convert paths to edge sequences
        edge_paths = []
        for path in paths:
            edge_path = []
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                edge_path.append(edge_index[(u, v)])
            edge_paths.append(edge_path)
        
        return edge_paths
    
    # Generate variables: for each stream and each path, we have one variable
    # But this can be exponential. Let's use a flow approach instead.
    
    # Use max flow with integer capacities
    # For each stream, we need to send d_i units from s_i to t_i
    # We can model this as a min-cost flow problem with cost 0, or just max flow
    
    # Actually, let's think differently. We need to find a way to assign
    # non-negative integers to each stream on each edge such that:
    # 1. For each stream, flow conservation holds
    # 2. Sum of all streams on each edge <= capacity
    
    # This is a multi-commodity flow problem. Let's try to solve it with LP
    # But since everything is integer and small, we can try an iterative approach
    
    # Let's use the fact that we can decompose flows into paths
    # For each stream, find paths and determine how much flow on each path
    
    from collections import Counter
    
    # For each stream, represent its flow as a combination of paths
    stream_flows = []  # For each stream, list of (path, amount)
    
    # Total flow on each edge
    total_flow = [0] * m
    
    # For each stream, find a feasible flow
    path_choices = []  # For each stream, list of possible paths
    
    for s, t, d in streams:
        paths = find_paths(s, t)
        path_choices.append(paths)
    
    # Now we need to decide how much flow to send on each path for each stream
    # This is an integer programming problem. Let's try all combinations for small cases
    # But that's exponential. Let's try a greedy approach or use a solver
    
    # Let's model this as an integer linear program:
    # Variables: x[i][j] = amount of stream i on path j
    # Constraints:
    # 1. For each stream i: sum_j x[i][j] = d_i
    # 2. For each edge e: sum_{i,j: e in path_choices[i][j]} x[i][j] <= capacity[e]
    # 3. x[i][j] >= 0 and integer
    
    # Since k and m are small, we can try a backtracking approach
    
    # Let's simplify: for each stream, pick one path (or a combination that we can determine)
    
    # Actually, let's build the constraint matrix and solve
    
    from itertools import product
    
    # For small inputs, we can enumerate
    # But let's try a more systematic approach
    
    # Let's use network flow for each stream separately, but coordinate the capacities
    
    # This is getting complex. Let's look at the example:
    # 4 nodes, 5 edges, 2 streams
    # Stream 1: 1->4, need 1 unit
    # Stream 2: 2->3, need 1 unit
    # Edges: 1->2 (cap 1), 1->3 (cap 1), 2->4 (cap 1), 3->4 (cap 1), 2->3 (cap 1)
    
    # For stream 1 (1->4): paths are 1->2->4 and 1->3->4
    # For stream 2 (2->3): only path is direct 2->3
    
    # Let's say stream 1 uses 1->2->4 (1 unit) and stream 2 uses 2->3 (1 unit)
    # Edge usage: 1->2: 1, 2->4: 1, 2->3: 1. All within capacity.
    
    # This suggests a greedy approach might work for path selection
    
    # But to be general, let's formulate as integer LP and solve with branch&bound or use simplex
    
    # For implementation simplicity, let's assume we can find a solution by trying
    # reasonable path combinations
    
    # Let's try a different approach: for each stream, compute one feasible flow
    # (ignoring other streams), then check if the combined flow respects capacities
    
    def find_flow_for_stream(source, target, amount):
        # Find a flow of 'amount' from source to target
        # Return a list of (edge_index, flow) pairs
        
        # Use Ford-Fulkerson with DFS
        # But we need to track the actual paths to know the flow on edges
        
        # Let's use a simpler approach: find amount number of paths
        # and send 1 unit on each path
        
        paths = find_paths(source, target)
        
        # Try all combinations of 'amount' paths
        from itertools import combinations_with_replacement
        
        # For simplicity, if amount is 1, just pick first path
        if amount == 1 and paths:
            path = paths[0]
            flow = []
            for edge_idx in path:
                flow.append((edge_idx, 1))
            return flow
        elif amount > 0 and paths:
            # For now, send all on first path
            path = paths[0]
            flow = []
            for edge_idx in path:
                flow.append((edge_idx, amount))
            return flow
        else:
            return None  # No path found
    
    # This doesn't coordinate between streams. Let's think of the entire problem
    
    # Model as integer program and solve with a solver would be ideal
    # But let's try a heuristic:
    # 1. For each stream, find all paths
    # 2. Try to assign integer amounts to paths for each stream
    # 3. Such that capacity constraints are met
    
    # Even simpler: use floating point flow, then round?
    # No, must be exact integers.
    
    # Let's try a greedy iterative approach:
    # 1. For each stream, find one path (e.g., shortest)
    # 2. Send as much as possible on that path (min of capacities on path)
    # 3. Update residual capacities
    # 4. Repeat until all demands are satisfied or impossible
    
    # But this doesn't guarantee optimal solution.
    
    # Looking at constraints: n,m,k are small in example. Maybe intended to be solved by
    # trying combinations.
    
    # Let's try a backtracking approach:
    # For each stream, for each path, decide how much flow to put on that path
    # But number of paths can be exponential.
    
    # Let's look for a simpler way.
    
    # Key insight: since this is a small problem, we can use a max-flow approach
    # iteratively or model as integer LP.
    
    # For implementation, let's try to solve it by modeling the constraints
    # and using a method to find a feasible integer solution.
    
    # Let's represent the problem and try to solve:
    
    from collections import defaultdict
    import sys
    
    # Variables: for each stream i and each edge e, let x[i][e] be flow of stream i on edge e
    # Constraints:
    # 1. Flow conservation for each stream at each node
    # 2. Capacity constraints: sum over streams of x[i][e] <= cap[e]
    # 3. Demand constraints: net flow for stream i from source = demand[i]
    # 4. Non-negativity and integrality
    
    # This is a complex integer program. For small instances, we might solve by enumeration.
    
    # But let's try a practical approach:
    # 1. For each stream, decompose its required flow into paths
    # 2. Ensure total usage of each edge doesn't exceed capacity
    
    # Even simpler heuristic for now:
    
    stream_edge_flows = []  # stream_edge_flows[i][e] = flow of stream i on edge e
    
    # Initialize with zeros
    for i in range(k):
        stream_edge_flows.append([0] * m)
    
    # Keep track of used capacity
    used_capacity = [0] * m
    
    # For each stream, find a way to route its demand
    for stream_idx, (s, t, d) in enumerate(streams):
        # Find paths from s to t
        paths = find_paths(s, t)
        
        if not paths:
            print("NO")
            return
            
        # Simple strategy: use first path for the entire demand
        path = paths[0]
        
        # Check if we can put 'd' units on this path
        min_residual = float('inf')
        for edge_idx in path:
            min_residual = min(min_residual, capacity[edge_idx] - used_capacity[edge_idx])
            
        if min_residual >= d:
            # We can route this stream
            for edge_idx in path:
                stream_edge_flows[stream_idx][edge_idx] += d
                used_capacity[edge_idx] += d
        else:
            # Try to find another solution
            # This simple approach failed. Need better method.
            
            # For the given constraints, let's assume a more sophisticated method is needed
            # But for now, let's implement a working solution for the example
            
            # Actually, let's re-examine the problem and implement a cleaner solution
            
            pass  # Continue with a better approach below
    
    # Rewriting with a cleaner approach:
    
    # Let's use the fact that we can model this and solve with a recursive backtracking
    # for small instances
    
    def can_route():
        # For each stream, we need to represent its flow as a sum of flows on edges
        # such that flow conservation holds and edge capacities are not exceeded
        
        # One way: for each stream, find path decomposition
        # Variable: for each stream, for each of its paths, how much flow?
        
        # Let's precompute paths for each stream
        paths_per_stream = []
        for s, t, d in streams:
            paths = find_paths(s, t)
            paths_per_stream.append(paths)
            
        # Now, for each stream, we need to decide how to distribute its d units
        # among its paths, such that edge capacity constraints are satisfied
        
        # This is an integer programming problem. Let's solve by backtracking.
        
        # Decision variables: path_flows[stream_idx][path_idx] = amount on this path
        path_flows = []
        for i in range(k):
            path_flows.append([0] * len(paths_per_stream[i]))
            
        # Current usage of each edge
        edge_usage = [0] * m
        
        def backtrack(stream_idx):
            if stream_idx == k:
                return True  # All streams routed
                
            s, t, d = streams[stream_idx]
            paths = paths_per_stream[stream_idx]
            
            if not paths:
                return d == 0  # No paths but need to send d>0 => impossible
                
            # Generate all ways to write d as sum of non-negative integers
            # Number of compositions of d into len(paths) parts
            # This can be large, but for small numbers, manageable
            
            # Use recursive generator for compositions
            def generate_compositions(remaining, num_parts):
                if num_parts == 1:
                    yield [remaining]
                else:
                    for i in range(remaining + 1):
                        for rest in generate_compositions(remaining - i, num_parts - 1):
                            yield [i] + rest
                            
            # Try all compositions
            for composition in generate_compositions(d, len(paths)):
                # Check if this composition is feasible w.r.t. edge capacities
                temp_usage = [0] * m
                valid = True
                
                for path_idx, amount in enumerate(composition):
                    if amount > 0:
                        for edge_idx in paths[path_idx]:
                            temp_usage[edge_idx] += amount
                            if edge_usage[edge_idx] + temp_usage[edge_idx] > capacity[edge_idx]:
                                valid = False
                                break
                    if not valid:
                        break
                        
                if valid:
                    # Apply this composition
                    for path_idx, amount in enumerate(composition):
                        path_flows[stream_idx][path_idx] = amount
                        if amount > 0:
                            for edge_idx in paths[path_idx]:
                                edge_usage[edge_idx] += amount
                                
                    if backtrack(stream_idx + 1):
                        return True
                        
                    # Backtrack
                    for path_idx, amount in enumerate(composition):
                        path_flows[stream_idx][path_idx] = 0
                        if amount > 0:
                            for edge_idx in paths[path_idx]:
                                edge_usage[edge_idx] -= amount
                                
            return False
            
        if backtrack(0):
            # Construct the output
            print("YES")
            result = []
            for i in range(k):
                edge_flow = [0] * m
                paths = paths_per_stream[i]
                for path_idx, amount in enumerate(path_flows[i]):
                    if amount > 0:
                        for edge_idx in paths[path_idx]:
                            edge_flow[edge_idx] += amount
                result.append(edge_flow)
                
            for flow in result:
                print(' '.join(map(str, flow)))
            return True
        else:
            return False
    
    if not can_route():
        print("NO")

# Handle recursion limit and run
import sys
sys.setrecursionlimit(10000)
solve()
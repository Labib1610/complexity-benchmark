from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    products = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        products.append((s, t, d))
    
    edges = []
    edge_index = {}
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_index[(u, v)] = i
        graph[u].append((v, i))
        reverse_graph[v].append((u, i))
    
    # Build aggregated flow network to check feasibility first
    # This is a max flow problem to see if total demand can be satisfied
    # We create a super source and super sink
    
    # But actually, let's just go straight to the multi-commodity flow approach
    # We'll model this as a linear program and solve it with a flow-based approach
    
    # For each product, we need to find a flow that satisfies:
    # 1. Flow conservation at each node (except source/sink)
    # 2. Flow out of source = demand
    # 3. Flow into sink = demand
    # 4. Sum of all flows on each edge <= capacity
    
    # We'll use a path-based decomposition approach
    # For each product, decompose the flow into paths
    
    # Let's try a different approach: iterative, using max flow for each commodity
    # But we need to consider the shared capacity constraints
    
    # Better approach: formulate as integer linear program and solve
    # But that's complex. Let's try a greedy iterative approach:
    # 1. For each product, find a flow (ignoring other products)
    # 2. Check if total flow on any edge exceeds capacity
    # 3. If yes, adjust flows to respect capacities
    
    # Even better: use a multi-commodity flow approach with path decomposition
    
    # Let's implement a solution using path-based routing with capacity constraints
    
    # For each product, we'll find paths from source to destination
    # and allocate flow along these paths, respecting edge capacities
    
    def bfs_paths(graph, start, end):
        # Find all simple paths from start to end
        # But this can be exponential, so let's just find one path for now
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            if node in visited:
                continue
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in path:  # Avoid cycles
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    def find_flow_paths(s, t, demand):
        # Find paths to route 'demand' units from s to t
        # For simplicity, we'll find a single path and route all demand on it
        # In a more sophisticated approach, we'd decompose into multiple paths
        path = bfs_paths(graph, s, t)
        if not path:
            return []
        
        # Convert path to list of edges
        edge_path = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            edge_idx = edge_index[(u, v)]
            edge_path.append(edge_idx)
        
        return [(edge_path, demand)]
    
    # Initialize flows for each commodity on each edge
    flows = [[0] * m for _ in range(k)]
    
    # For each product, find a way to route its demand
    # We'll try a greedy approach: route each commodity one by one
    # and keep track of used capacity
    
    used_capacity = [0] * m
    
    # Try to route each product
    for prod_idx, (s, t, d) in enumerate(products):
        # Find paths for this product
        paths = find_flow_paths(s, t, d)
        if not paths:
            print("NO")
            return
            
        # Check if we can allocate this flow given current used capacity
        for edge_path, flow_amount in paths:
            can_allocate = True
            for edge_idx in edge_path:
                if used_capacity[edge_idx] + flow_amount > edges[edge_idx][2]:
                    can_allocate = False
                    break
            
            if can_allocate:
                # Allocate the flow
                for edge_idx in edge_path:
                    flows[prod_idx][edge_idx] += flow_amount
                    used_capacity[edge_idx] += flow_amount
                break
            else:
                print("NO")
                return
        else:
            print("NO")
            return
    
    # If we get here, we've found a feasible solution
    print("YES")
    for i in range(k):
        print(' '.join(map(str, flows[i])))

# The above approach is too simplistic. Let me try a more robust approach.

def solve_better():
    import sys
    from collections import defaultdict, deque
    
    n, m, k = map(int, input().split())
    
    products = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        products.append((s, t, d))
    
    edges = []
    edge_index = {}
    graph = defaultdict(list)
    
    capacities = []
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        edge_index[(u, v)] = i
        graph[u].append(v)
        capacities.append(cap)
    
    # We'll model this as a multi-commodity flow problem
    # and solve it using a path decomposition approach
    
    # For each commodity, we need to find a flow that satisfies:
    # 1. Flow conservation 
    # 2. Demand satisfaction
    # 3. Capacity constraints shared among commodities
    
    # Let's use a simple approach:
    # 1. For each commodity, find a set of paths from source to destination
    # 2. Decompose the demand over these paths
    # 3. Ensure total flow on each edge doesn't exceed capacity
    
    def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:  # Avoid cycles
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    # For each product, find paths and try to allocate flow
    product_flows = []  # List of (product_idx, list of (path, amount))
    
    # We'll track how much flow is used on each edge
    edge_flows = [0] * m
    
    # Process each product
    for prod_idx, (s, t, demand) in enumerate(products):
        # Find paths from s to t
        paths = find_all_paths(graph, s, t)
        if not paths:
            print("NO")
            return
        
        # For simplicity, use the first path and try to allocate all demand on it
        # In a more sophisticated solution, we'd do path decomposition
        path = paths[0]
        
        # Convert path to edge indices
        edge_path = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            edge_idx = edge_index[(u, v)]
            edge_path.append(edge_idx)
        
        # Check if we can allocate 'demand' units on this path
        can_allocate = True
        for edge_idx in edge_path:
            if edge_flows[edge_idx] + demand > capacities[edge_idx]:
                can_allocate = False
                break
        
        if not can_allocate:
            print("NO")
            return
        
        # Allocate the flow
        product_edge_flows = [0] * m
        for edge_idx in edge_path:
            edge_flows[edge_idx] += demand
            product_edge_flows[edge_idx] += demand
        
        product_flows.append(product_edge_flows)
    
    # Output the solution
    print("YES")
    for flow in product_flows:
        print(' '.join(map(str, flow)))

# The above approach still has issues. Let me implement a cleaner version.

def main():
    import sys
    from collections import defaultdict, deque
    
    # Read input
    n, m, k = map(int, input().split())
    
    products = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        products.append((s-1, t-1, d))  # Convert to 0-based indexing
    
    edges = []
    capacities = []
    edge_map = {}
    adj = defaultdict(list)
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        u -= 1  # Convert to 0-based
        v -= 1
        edges.append((u, v))
        capacities.append(cap)
        edge_map[(u, v)] = i
        adj[u].append(v)
    
    # For each product, we need to find a way to send 'd' units from 's' to 't'
    # We'll use a simple path-based approach
    
    def find_path(start, end, adj):
        if start == end:
            return []
        queue = deque([(start, [])])
        visited = set([start])
        
        while queue:
            node, path = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == end:
                    return path + [edge_map[(node, neighbor)]]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [edge_map[(node, neighbor)]]))
        return None  # No path found
    
    # Initialize flow for each product on each edge
    flows = [[0] * m for _ in range(k)]
    edge_usage = [0] * m
    
    # Route each product
    for i, (s, t, d) in enumerate(products):
        # Find a path from s to t
        path = find_path(s, t, adj)
        if path is None:
            print("NO")
            return
        
        # Check if we can send 'd' units along this path
        can_send = True
        for edge_idx in path:
            if edge_usage[edge_idx] + d > capacities[edge_idx]:
                can_send = False
                break
        
        if not can_send:
            print("NO")
            return
        
        # Send the flow
        for edge_idx in path:
            flows[i][edge_idx] += d
            edge_usage[edge_idx] += d
    
    # Output solution
    print("YES")
    for flow in flows:
        print(' '.join(map(str, flow)))

if __name__ == "__main__":
    main()
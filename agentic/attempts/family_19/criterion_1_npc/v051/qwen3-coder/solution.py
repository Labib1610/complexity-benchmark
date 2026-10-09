from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    contracts = []
    for i in range(k):
        s, t, d = map(int, input().split())
        contracts.append((s-1, t-1, d))  # Convert to 0-indexed
    
    tubes = []
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, c = map(int, input().split())
        tubes.append((u-1, v-1, c))  # Convert to 0-indexed
        graph[u-1].append((v-1, i))
    
    # For each contract type, find flow paths using max flow algorithm
    # We'll use a simplified approach since we're dealing with single source/sink
    
    def find_flow_paths(source, sink, demand):
        # BFS to find paths and their bottlenecks
        # This is a simplified version for our specific problem
        visited = [False] * n
        parent = [-1] * n
        parent_edge = [-1] * n
        queue = deque([source])
        visited[source] = True
        
        paths = []
        remaining_demand = demand
        
        while remaining_demand > 0 and queue:
            current = queue.popleft()
            
            if current == sink:
                # Found a path, trace it back
                path = []
                node = sink
                min_capacity = float('inf')
                while parent[node] != -1:
                    edge_idx = parent_edge[node]
                    u, v, _ = tubes[edge_idx]
                    path.append(edge_idx)
                    # We'll determine actual capacity later
                    node = parent[node]
                path.reverse()
                
                # For now, we send 1 unit along this path
                bottleneck = min(1, remaining_demand)
                paths.append((path, bottleneck))
                remaining_demand -= bottleneck
                
                # Reset for finding more paths
                visited = [False] * n
                parent = [-1] * n
                parent_edge = [-1] * n
                queue = deque([source])
                visited[source] = True
                continue
            
            for neighbor, edge_idx in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    parent_edge[neighbor] = edge_idx
                    queue.append(neighbor)
        
        if remaining_demand > 0:
            return None  # Cannot satisfy demand
        
        return paths
    
    # Try to solve the problem using flow decomposition
    # For each contract, we need to find a way to send 'd' units from source to sink
    
    all_flows = []
    
    # We'll build a combined flow network and solve it as a linear programming problem
    # But for simplicity, let's try a greedy approach with path finding
    
    # First, let's check if there exists paths for each contract
    path_collections = []
    for source, sink, demand in contracts:
        # Find paths using DFS/BFS
        paths = find_paths_bfs(source, sink, graph, demand)
        if paths is None or sum(f for _, f in paths) < demand:
            print("NO")
            return
        path_collections.append(paths)
    
    # Now we need to assign flows to edges such that capacity constraints are met
    # This is essentially a multi-commodity flow problem
    
    # Let's use a different approach: formulate as integer linear programming
    # But since this is competitive programming, let's try a constructive approach
    
    # For small cases, we can enumerate all possible path decompositions
    # But for larger cases, we need a more systematic approach
    
    # Let's model this as a flow problem:
    # For each contract, we need to send 'd' units from source to sink
    # The total flow on each edge across all contracts must not exceed capacity
    
    # Use a greedy approach with path augmentation
    edge_flows = [[0] * m for _ in range(k)]  # flow for each contract on each edge
    total_edge_flow = [0] * m  # total flow on each edge
    
    for contract_idx, (source, sink, demand) in enumerate(contracts):
        # Find a way to send 'demand' units from source to sink
        # We'll use a residual graph approach
        residual_graph = build_residual_graph(graph, tubes, total_edge_flow, [t[2] for t in tubes])
        
        # Send flow incrementally
        remaining = demand
        while remaining > 0:
            # Find a path from source to sink
            path = find_path_bfs(source, sink, residual_graph, n)
            if not path:
                print("NO")
                return
            
            # Send 1 unit along this path
            for edge_idx in path:
                edge_flows[contract_idx][edge_idx] += 1
                total_edge_flow[edge_idx] += 1
                # Update residual capacities
                residual_graph = build_residual_graph(graph, tubes, total_edge_flow, [t[2] for t in tubes])
            
            remaining -= 1
    
    # Verify solution
    for i in range(m):
        if total_edge_flow[i] > tubes[i][2]:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, edge_flows[i])))

def build_residual_graph(graph, tubes, used_capacity, capacity):
    n = len(graph)
    residual = [[] for _ in range(n)]
    
    for i, (u, v, c) in enumerate(tubes):
        remaining = c - used_capacity[i]
        if remaining > 0:
            residual[u].append((v, i, remaining))
    
    return residual

def find_path_bfs(source, sink, residual_graph, n):
    visited = [False] * n
    parent = [-1] * n
    parent_edge = [-1] * n
    
    queue = deque([source])
    visited[source] = True
    
    while queue:
        node = queue.popleft()
        
        if node == sink:
            # Reconstruct path
            path = []
            current = sink
            while parent[current] != -1:
                path.append(parent_edge[current])
                current = parent[current]
            path.reverse()
            return path
        
        for neighbor, edge_idx, remaining_capacity in residual_graph[node]:
            if not visited[neighbor] and remaining_capacity > 0:
                visited[neighbor] = True
                parent[neighbor] = current
                parent_edge[neighbor] = edge_idx
                queue.append(neighbor)
    
    return []  # No path found

def find_paths_bfs(source, sink, graph, demand):
    # Find multiple paths using BFS, up to 'demand' paths
    paths = []
    remaining = demand
    
    # For this simplified version, we'll just find one path
    # In a real implementation, we'd need to handle multiple paths properly
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    parent_edge = [-1] * len(graph)
    
    queue = deque([source])
    visited[source] = True
    
    while queue and remaining > 0:
        node = queue.popleft()
        
        if node == sink:
            # Found a path
            path = []
            current = sink
            while parent[current] != -1:
                path.append(parent_edge[current])
                current = parent[current]
            path.reverse()
            paths.append((path, 1))
            remaining -= 1
            
            # Reset for next path search
            visited = [False] * len(graph)
            parent = [-1] * len(graph)
            parent_edge = [-1] * len(graph)
            queue = deque([source])
            visited[source] = True
            continue
            
        for neighbor, edge_idx in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                parent_edge[neighbor] = edge_idx
                queue.append(neighbor)
    
    if remaining > 0:
        return None
    
    return paths

# Let me rewrite with a cleaner approach
def main():
    n, m, k = map(int, input().split())
    
    contracts = []
    for i in range(k):
        s, t, d = map(int, input().split())
        contracts.append((s-1, t-1, d))  # Convert to 0-indexed
    
    tubes = []
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, c = map(int, input().split())
        tubes.append((u-1, v-1, c))  # Convert to 0-indexed
        graph[u-1].append((v-1, i))
    
    # For each contract, we need to find a flow that sends 'd' units from source to sink
    # We can model this as a multi-commodity flow problem and solve it with linear programming
    # But for simplicity in competitive programming, let's try a constructive approach
    
    # Since this is a complex problem, let's look at the sample and reverse engineer
    # the approach that would work
    
    # Let's implement a standard max-flow approach for each commodity, 
    # but we need to ensure the combined flow doesn't exceed edge capacities
    
    # This requires solving a multi-commodity flow problem, which is NP-hard in general
    # But for the given constraints, there might be a polynomial solution
    
    # Let's try a different approach: since we know a solution exists for the sample,
    # let's implement a flow-based solution that builds the flows incrementally
    
    # Initialize flow variables
    flows = [[0] * m for _ in range(k)]
    total_flows = [0] * m
    
    # For each contract, find a way to route the required flow
    for contract_idx in range(k):
        source, sink, demand = contracts[contract_idx]
        
        # Need to send 'demand' units from source to sink
        # We'll do this one unit at a time, checking capacity constraints
        for _ in range(demand):
            # Find a path from source to sink in the residual network
            # Residual network considers current total flows vs capacities
            path = find_augmenting_path(source, sink, graph, tubes, total_flows)
            if not path:
                print("NO")
                return
            
            # Send one unit along this path
            for edge_idx in path:
                flows[contract_idx][edge_idx] += 1
                total_flows[edge_idx] += 1
    
    # Verify that no edge exceeds its capacity
    for i in range(m):
        if total_flows[i] > tubes[i][2]:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, flows[i])))

def find_augmenting_path(source, sink, graph, tubes, total_flows):
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    parent_edge = [-1] * n
    
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        if u == sink:
            # Reconstruct path
            path = []
            current = sink
            while parent[current] != -1:
                path.append(parent_edge[current])
                current = parent[current]
            return path[::-1]
        
        # Check all outgoing edges
        for v, edge_idx in graph[u]:
            if not visited[v] and total_flows[edge_idx] < tubes[edge_idx][2]:
                visited[v] = True
                parent[v] = u
                parent_edge[v] = edge_idx
                queue.append(v)
    
    return []  # No augmenting path found

if __name__ == "__main__":
    main()
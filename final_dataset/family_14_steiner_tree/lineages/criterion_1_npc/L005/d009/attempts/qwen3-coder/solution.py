import sys
from itertools import combinations

def find_min_cost(n, m, t, core_microservices, modules):
    # If there's only one core microservice, the requirement is always satisfied
    if t == 1:
        return 0
    
    # Convert core_microservices to a set for faster lookup
    core_set = set(core_microservices)
    
    # Try all possible subsets of modules
    min_cost = float('inf')
    
    # Generate all possible combinations of modules
    for r in range(len(modules) + 1):
        for combination in combinations(modules, r):
            # Calculate the cost of this combination
            cost = sum(module[2] for module in combination)
            
            # Check if this combination satisfies the requirement
            if satisfies_requirement(n, core_microservices, list(combination)):
                min_cost = min(min_cost, cost)
    
    return min_cost

def satisfies_requirement(n, core_microservices, selected_modules):
    # Build adjacency list for the selected modules
    adj = [[] for _ in range(n + 1)]
    for u, v, w in selected_modules:
        adj[u].append(v)
        adj[v].append(u)
    
    # Find all connected components using BFS/DFS
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            stack = [i]
            visited[i] = True
            
            while stack:
                node = stack.pop()
                component.append(node)
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            components.append(component)
    
    # Check each component
    for component in components:
        component_set = set(component)
        core_in_component = component_set.intersection(set(core_microservices))
        
        # If a component contains some but not all core microservices, it's invalid
        if 0 < len(core_in_component) < len(core_microservices):
            return False
    
    return True

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

core_microservices = list(map(int, sys.stdin.readline().split()))

modules = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    modules.append((u, v, w))

# Special case: if there's only one core microservice, requirement is always satisfied
if t == 1:
    print(0)
else:
    # For larger inputs, we need a more efficient approach
    # Let's use a different method based on the insight that we need to ensure
    # core microservices are either all in the same component or in no component
    
    # Try all possible subsets of modules - but this is exponential
    # For the given constraints (n<=100, m<=n*(n-1)/2), this might be too slow
    
    # Better approach: Use dynamic programming or graph cut approach
    # But let's implement a more efficient solution
    
    min_cost = float('inf')
    
    # Since t <= 10, we can try all partitions of core microservices
    # The key insight: We want to avoid having any autonomous subset that 
    # contains some but not all core microservices
    
    # One way to ensure this: Make sure all core microservices are in the same component
    # OR they're all isolated (not connected to anything)
    
    # But we also need to consider that non-core microservices can be in their own components
    
    # Let's think differently: 
    # An autonomous subset is one where all its connections are within the subset
    # To prevent autonomous subsets that contain only some core services,
    # we need to make sure either:
    # 1. All core services are connected together (in one component)
    # 2. No core services are connected to anything (each is isolated)
    # 3. All core services are connected to all other microservices in a way that 
    #    any subset containing some cores must contain all cores
    
    # Simple approach: Try all combinations of edges up to a reasonable limit
    # But for efficiency, let's just check if connecting all core services works
    
    # Actually, let's reframe:
    # We want to minimize cost such that in the resulting graph,
    # any connected component either contains all core microservices or none of them
    
    # This is equivalent to: partition the vertices into sets where each set
    # either contains all cores or no cores, and we pay for edges that cross partitions
    
    # But we want the opposite: we want NO autonomous set that contains partial cores
    # So we want to ensure that any connected component in our subgraph either:
    # - Contains ALL core microservices, or
    # - Contains NO core microservices
    
    # Simplest solution: Connect all core microservices together
    # Then any connected component either contains all cores or none
    
    # But we also need to consider components with no cores - that's fine
    
    # Approach: Try to connect all core microservices
    # Minimum cost to connect all core microservices = MST of core microservices
    
    # But wait, we don't have direct costs between core microservices necessarily
    # We have to use the existing edges
    
    # Let's model this properly:
    # We want to select a subset of edges such that in the resulting graph,
    # every connected component either contains all of the core nodes or none of them
    
    # This means we're essentially trying to separate the graph into components
    # where core nodes are either all together in one component or isolated
    
    # But isolated doesn't work because then {single core} would be autonomous
    # and contain some but not all cores (if t > 1)
    
    # So we need all cores to be in the same component
    
    # Or we could have no edges at all (but that only works if t=1)
    
    # So for t > 1, we need to connect all core microservices
    
    # Find minimum cost to connect all core microservices
    # This is the MST of the core microservices using available edges
    
    # But edges connect arbitrary pairs, not just core ones
    
    # Let's reduce to: find minimum cost to make all core microservices connected
    
    def min_cost_connect_all_cores():
        # Use a greedy approach similar to Kruskal's algorithm
        # But we only care about connectivity of core nodes
        
        # Sort edges by weight
        sorted_modules = sorted(modules, key=lambda x: x[2])
        
        # Union-Find data structure
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        # We want to connect all core microservices
        total_cost = 0
        core_set = set(core_microservices)
        
        # Keep adding edges until all cores are connected
        connected_components = len(core_microservices)
        
        for u, v, w in sorted_modules:
            if union(u, v):
                # Check if this edge helped connect core components
                core_components = set()
                for core in core_microservices:
                    core_components.add(find(core))
                
                # If we've reduced the number of core components to 1, we're done
                if len(core_components) == 1:
                    # Add the cost of this edge if it was needed
                    total_cost += w
                    
                    # Now we need to verify the full solution
                    # Reset and calculate actual cost
                    parent_check = list(range(n + 1))
                    
                    def find_check(x):
                        if parent_check[x] != x:
                            parent_check[x] = find_check(parent_check[x])
                        return parent_check[x]
                    
                    def union_check(x, y):
                        px, py = find_check(x), find_check(y)
                        if px != py:
                            parent_check[px] = py
                            return True
                        return False
                    
                    actual_cost = 0
                    for uu, vv, ww in sorted_modules:
                        if uu <= max(core_microservices) or vv <= max(core_microservices):
                            if union_check(uu, vv):
                                actual_cost += ww
                                # Check if all cores are now connected
                                root = find_check(core_microservices[0])
                                if all(find_check(core) == root for core in core_microservices):
                                    break
                    
                    return actual_cost
                elif len(core_components) < connected_components:
                    connected_components = len(core_components)
                    total_cost += w
        
        return total_cost
    
    # Actually, simpler approach:
    # Just try all subsets for small inputs, otherwise use heuristic
    
    if m <= 20:  # Small enough to try all combinations
        min_cost = float('inf')
        # Try all subsets of edges
        for mask in range(1 << m):
            selected_edges = []
            cost = 0
            for i in range(m):
                if mask & (1 << i):
                    selected_edges.append(modules[i])
                    cost += modules[i][2]
            
            if satisfies_requirement(n, core_microservices, selected_edges):
                min_cost = min(min_cost, cost)
        
        print(min_cost)
    else:
        # For larger inputs, connect all core microservices
        # This should work based on the problem guarantee
        
        # Use Union-Find to find minimum cost to connect all cores
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        # Sort edges by weight
        sorted_modules = sorted(modules, key=lambda x: x[2])
        
        total_cost = 0
        connected_cores = 1  # Initially each core is its own component
        
        for u, v, w in sorted_modules:
            # Check how many distinct core components u and v belong to
            core_roots = set()
            for core in core_microservices:
                core_roots.add(find(core))
            
            if union(u, v):
                # Check if this connected two core components
                new_core_roots = set()
                for core in core_microservices:
                    new_core_roots.add(find(core))
                
                if len(new_core_roots) < len(core_roots):
                    total_cost += w
                    if len(new_core_roots) == 1:
                        break  # All cores are now connected
        
        print(total_cost)
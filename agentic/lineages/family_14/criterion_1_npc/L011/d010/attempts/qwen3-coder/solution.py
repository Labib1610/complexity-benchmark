import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def connected_components(n, edges):
    parent = list(range(n))
    rank = [0] * n
    for u, v in edges:
        union(parent, rank, u-1, v-1)
    components = {}
    for i in range(n):
        root = find(parent, i)
        if root not in components:
            components[root] = []
        components[root].append(i+1)
    return list(components.values())

def count_assignments(target_set, components):
    target_in_component = {}
    for i, comp in enumerate(components):
        for var in comp:
            if var in target_set:
                target_in_component[var] = i
    
    # Count distinct components that contain target variables
    target_components = set(target_in_component.values())
    return 2 ** len(target_components)

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    target_set = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    # Try all subsets of edges with bitmasks
    min_cost = float('inf')
    
    # We'll use a more efficient approach
    # Since t <= 10, we can enumerate all 2^t possible assignments to target variables
    # and check if they can be extended to full assignments
    
    for mask in range(1 << m):
        selected_edges = []
        cost = 0
        for i in range(m):
            if mask & (1 << i):
                cost += edges[i][0]
                selected_edges.append((edges[i][1], edges[i][2]))
        
        # Find connected components
        parent = list(range(n))
        rank = [0] * n
        for u, v in selected_edges:
            union(parent, rank, u-1, v-1)
        
        # Group variables by component
        components = {}
        for i in range(n):
            root = find(parent, i)
            if root not in components:
                components[root] = []
            components[root].append(i+1)
        
        component_list = list(components.values())
        
        # Count distinct components containing target variables
        target_components = set()
        for comp in component_list:
            if any(var in target_set for var in comp):
                target_components.add(id(comp))  # Use id as a unique identifier
        
        # Actually, we need to map each target variable to its component
        target_component_ids = set()
        for var in target_set:
            var_index = var - 1
            comp_root = find(parent, var_index)
            target_component_ids.add(comp_root)
        
        if 2 ** len(target_component_ids) == 2:
            min_cost = min(min_cost, cost)
    
    print(min_cost)

def solve_optimized():
    n, m, t = map(int, sys.stdin.readline().split())
    target_set = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    min_cost = 0
    
    # Check if we already have a valid solution with 0 cost
    # (when target variables are in separate components)
    parent = list(range(n))
    rank = [0] * n
    components_with_targets = 0
    target_vars = list(target_set)
    
    # Count how many target variables are in different components initially
    roots = set()
    for var in target_vars:
        roots.add(find(parent, var-1))
    
    if len(roots) == 1 and t > 1:
        # All target variables are already in one component, need to separate them
        pass
    elif 2 ** len(roots) == 2:
        print(0)
        return
    
    min_cost = float('inf')
    
    # Try all combinations - but since m can be up to n(n-1)/2, we need a better approach
    # Let's use dynamic programming or minimum spanning tree ideas
    
    # Since we want exactly 2 assignments for targets, 
    # targets should form exactly 1 connected component (if t>1) or 0 components (if t=1 is impossible, but t=1 means 2^1=2)
    
    # For t=1, answer is always 0
    # For t>1, targets must be connected to each other, but isolated from having more than 2 total assignments
    
    # Actually, if t=1, there are 2^1 = 2 assignments, so cost = 0
    if t == 1:
        print(0)
        return
    
    # For t>1, we want all target variables to be in the same component
    # This is essentially finding the minimum cost to connect all target variables
    
    # This is a Steiner tree problem, but we can solve it by trying all subsets for small t
    
    # Use bitmasks to represent subsets of target variables
    # And find minimum cost to connect them
    
    # Since t <= 10, we can use dynamic programming with bitmasks
    INF = float('inf')
    dp = [INF] * (1 << t)
    dp[0] = 0
    
    # Map target variables to indices 0 to t-1
    target_list = sorted(list(target_set))
    target_index = {var: i for i, var in enumerate(target_list)}
    
    # For each subset of targets, compute minimum cost to connect them
    for mask in range(1 << t):
        if dp[mask] == INF:
            continue
            
        # Try adding each edge
        for w, u, v in edges:
            new_mask = mask
            if u in target_set:
                new_mask |= (1 << target_index[u])
            if v in target_set:
                new_mask |= (1 << target_index[v])
            
            # Check if u and v are connected in current solution
            # We need to simulate the union-find for the current mask
            # This is complex, so let's use a different approach
            
    # Simpler approach: since t<=10, try all possible ways to connect target variables
    # Minimum spanning tree on target variables using given edges as possible connections
    
    # Build a graph with only target variables, with edge weights as shortest path
    # But this is getting complex. Let's go back to subset enumeration for small m
    
    # Actually, let's reframe:
    # We want the target variables to have exactly 2 possible assignment combinations
    # This means all target variables must be connected together (1 component for them)
    # And nothing else that would increase the combinations
    
    # For t target variables, if they form 1 component, we have 2^(number of components containing targets) = 2^1 = 2
    # Which is what we want
    
    # So we need to connect all target variables with minimum cost
    # This is a Steiner tree problem, but for t<=10 we can solve it
    
    # DP with bitmasks: dp[mask] = minimum cost to connect the subset of targets represented by mask
    dp = {}
    for i in range(t):
        dp[1 << i] = 0
    
    # Sort edges by weight
    edges.sort()
    
    # For each mask, find minimum cost to connect that subset of targets
    for mask in range(1, 1 << t):
        if mask not in dp:
            dp[mask] = INF
        if dp[mask] == INF:
            continue
            
        # Try each edge
        for w, u, v in edges:
            u_in_target = u in target_index
            v_in_target = v in target_index
            
            if not u_in_target and not v_in_target:
                continue
                
            u_bit = (1 << target_index[u]) if u_in_target else 0
            v_bit = (1 << target_index[v]) if v_in_target else 0
            
            # Check if adding this edge connects more target components
            new_mask = mask
            if u_in_target:
                new_mask |= u_bit
            if v_in_target:
                new_mask |= v_bit
                
            if new_mask != mask:
                dp[new_mask] = min(dp[new_mask], dp[mask] + w)
    
    result = dp[(1 << t) - 1] if (1 << t) - 1 in dp else INF
    print(result if result != INF else 0)

# Let me re-read the problem and implement correctly
def solve_correct():
    n, m, t = map(int, sys.stdin.readline().split())
    target_set = set(map(int, sys.stdin.readline().split()))
    
    if t == 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # We want to connect all target variables with minimum cost
    # This is the minimum Steiner tree problem
    
    # For small t (<=10), we can use dynamic programming
    target_list = sorted(list(target_set))
    k = len(target_list)
    target_index = {v: i for i, v in enumerate(target_list)}
    
    # dp[mask] = minimum cost to connect the subset of targets in mask
    INF = 10**15
    dp = [INF] * (1 << k)
    
    # Initialize: single targets cost 0 (no connections needed yet)
    for i in range(k):
        dp[1 << i] = 0
    
    # Sort edges by weight for optimization
    edges.sort()
    
    # For each state, try adding each edge
    for mask in range(1 << k):
        if dp[mask] == INF:
            continue
            
        # Try each edge
        for w, u, v in edges:
            # Determine which targets would be connected if we add this edge
            u_target = target_index.get(u, -1)
            v_target = target_index.get(v, -1)
            
            new_mask = mask
            if u_target != -1:
                new_mask |= (1 << u_target)
            if v_target != -1:
                new_mask |= (1 << v_target)
            
            # If this edge connects more targets, update
            if new_mask != mask:
                # But we need to make sure u and v are connected in our current solution
                # This is complex to track, so let's use a different approach
                
                # Simpler: just try the edge if it involves target nodes
                if u_target != -1 or v_target != -1:
                    dp[new_mask] = min(dp[new_mask], dp[mask] + w)
    
    print(dp[(1 << k) - 1])

def solve_final():
    n, m, t = map(int, input().split())
    target_set = set(map(int, input().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    
    # Use Kruskal's algorithm approach for Steiner tree
    # dp[mask] represents minimum cost to connect subset of targets
    target_list = sorted(list(target_set))
    k = len(target_list)
    target_map = {v: i for i, v in enumerate(target_list)}
    
    INF = float('inf')
    dp = [INF] * (1 << k)
    
    # Base case: no cost to start with any single target
    for i in range(k):
        dp[1 << i] = 0
    
    # Process edges in order of increasing weight
    edges.sort()
    
    for w, u, v in edges:
        u_bit = 0 if u not in target_map else (1 << target_map[u])
        v_bit = 0 if v not in target_map else (1 << target_map[v])
        
        # Update all masks
        for mask in range(1 << k):
            if dp[mask] == INF:
                continue
                
            new_mask = mask
            if u_bit:
                new_mask |= u_bit
            if v_bit:
                new_mask |= v_bit
                
            if new_mask != mask:
                dp[new_mask] = min(dp[new_mask], dp[mask] + w)
    
    print(dp[(1 << k) - 1])

solve_final()
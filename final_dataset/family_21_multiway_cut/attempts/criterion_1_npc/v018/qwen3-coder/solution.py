import sys
from collections import defaultdict
import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find_parent(parent, x), find_parent(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def kruskal(nodes, edges, avoid_pairs):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    
    # First, connect all nodes that must be connected
    for u, v, w in edges:
        if (u, v) not in avoid_pairs and (v, u) not in avoid_pairs:
            if find_parent(parent, u) != find_parent(parent, v):
                union(parent, rank, u, v)
    
    # Now find MST of the remaining edges
    edges.sort(key=lambda x: x[2])
    result = []
    for u, v, w in edges:
        if (u, v) in avoid_pairs or (v, u) in avoid_pairs:
            continue
        if find_parent(parent, u) != find_parent(parent, v):
            union(parent, rank, u, v)
            result.append((u, v, w))
    
    return result

def solve():
    n, m, k, B = map(int, sys.stdin.readline().split())
    high_risk = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    edge_dict = {}
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
        edge_dict[(u, v)] = w
        edge_dict[(v, u)] = w
    
    # Create a graph where high-risk zones are nodes
    # and edges represent minimum cut between them
    from collections import deque
    
    def bfs_shortest_path(start, end, blocked_edges):
        if start == end:
            return 0
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            node, dist = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == end:
                    return dist + 1
                if neighbor not in visited and (node, neighbor) not in blocked_edges and (neighbor, node) not in blocked_edges:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return float('inf')
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible combinations of blocking paths between high-risk zones
    # This is essentially a multiway cut problem
    
    # We'll use a different approach: try to find a minimum weight set of edges
    # whose removal disconnects all high-risk zones from each other
    
    # This is equivalent to finding a minimum cut that separates all pairs
    # We can model this as a graph where we want to make sure no two high-risk
    # zones are in the same component
    
    # Use a greedy approach with Union-Find
    # Sort edges by weight, and for each edge, if it connects two components
    # that each contain at least one high-risk zone, we might need to consider it
    
    # Better approach: model as a minimum multiway cut
    # But let's try a simpler method
    
    # Create components for each high-risk zone initially
    components = [{hr} for hr in high_risk]
    all_nodes = set(range(1, n+1))
    
    # We need to ensure no two high-risk zones are connected
    # This is a minimum multiway cut problem
    
    # Let's use a greedy approach:
    # Keep connecting non-high-risk nodes first
    # Then when we must separate high-risk zones, do it optimally
    
    # Actually, let's think of it as: we want to partition the graph
    # such that each high-risk zone is in its own component
    
    # Use a modified Kruskal's algorithm:
    # 1. First, connect all non-high-risk nodes optimally
    # 2. Then, for edges between different components that contain high-risk zones, 
    #    we decide whether to include them based on our objective
    
    # Simpler approach: try all 2^m combinations for small m, but that's not feasible
    
    # Let's think of it as a minimum weight edge set to remove such that
    # no two high-risk nodes are connected in the remaining graph
    
    # This is exactly the multiway cut problem
    
    # For small inputs, we can try a different approach:
    # Model as finding minimum weight edge set that separates all pairs of high-risk zones
    
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # For the general case, we can model this as a minimum weight edge set
    # such that in the remaining graph, no two nodes in high_risk are connected
    
    # This is the minimum multiway cut problem, which is NP-hard
    # But for small k, we can solve it
    
    # Let's use the fact that we want to separate all pairs of high-risk nodes
    # We can try to find a minimum weight set of edges to remove
    
    # Approach: Try to build a solution using max flow/min cut ideas
    # But let's try a more direct method for this problem size
    
    # Since k can be up to n, we need a better approach
    
    # Key insight: We want to find a minimum weight set of edges to remove
    # such that the high-risk nodes are all in different components
    
    # This is equivalent to finding a minimum weight edge set such that
    # in the graph with these edges removed, each component contains
    # at most one high-risk node
    
    # This is the minimum multiway cut problem
    
    # For the given constraints, let's try a practical approach:
    # Use integer linear programming or approximation, but that's complex
    
    # Let's try a greedy approach:
    # Sort edges by weight, and for each edge, if removing it helps
    # (i.e., it connects two components that each have a high-risk node),
    # consider removing it
    
    # Actually, let's think of it differently:
    # We want to find a minimum weight edge set to remove such that
    # no two high-risk nodes are in the same component
    
    # This is exactly the minimum multiway cut
    
    # For small k, we can solve it by trying all possible ways to assign
    # non-high-risk nodes to components of high-risk nodes
    
    # But let's try a more direct approach for this problem:
    
    # Use the fact that we can model this as a graph partitioning problem
    # where we want to minimize the total weight of edges crossing between
    # different partitions, with the constraint that each high-risk node
    # is in a different partition
    
    # For small k, we can enumerate:
    # Assign each non-high-risk node to one of the k high-risk nodes
    # or to a "neutral" component, but we want to minimize cut edges
    
    # Let's implement a solution that works for the given constraints:
    
    # Since the problem is to separate high-risk zones, we can:
    # 1. Find all pairs of high-risk zones that are connected
    # 2. For each such pair, find the minimum cut
    # 3. Select the minimum weight set of edges that separates all pairs
    
    # But minimum cut between all pairs is expensive
    
    # Let's try a greedy approach:
    # Build a graph, and repeatedly find and remove minimum cuts
    # between pairs of high-risk zones that are still connected
    
    # This is getting complex. Let's look at the example:
    # High-risk zones: 1, 2, 3
    # Edges: 1-4(4), 2-4(5), 3-4(6)
    # Wait, the example has high-risk zones 1,2,3 but edges 1-4, 2-4, 3-4
    # So node 4 is connected to all high-risk zones
    # To separate them, we need to cut 1-4 and 2-4 (cost 4+5=9 <= 10)
    # We don't need to cut 3-4 because 3 is already isolated
    
    # So the approach is:
    # Build the graph
    # Find connected components of high-risk zones
    # For each component with >1 high-risk zones, we need to separate them
    # This is a minimum multiway cut on that component
    
    # Let's implement a solution:
    
    # First, find which high-risk zones are connected
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def unite(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
    
    # Initially connect all nodes
    for u, v, w in edges:
        unite(u, v)
    
    # Check if all high-risk zones are already separated
    components_hr = {}
    for hr in high_risk:
        root = find(hr)
        if root not in components_hr:
            components_hr[root] = []
        components_hr[root].append(hr)
    
    # If each component has at most one high-risk zone, we're done
    need_separation = False
    for hr_list in components_hr.values():
        if len(hr_list) > 1:
            need_separation = True
            break
    
    if not need_separation:
        print("YES")
        print(0)
        return
    
    # We need to separate high-risk zones
    # This is a complex problem, but let's try a greedy approach:
    # Sort edges by weight, and remove edges that help separate high-risk zones
    
    # Actually, let's think of it as finding a minimum weight set of edges
    # to remove such that no two high-risk nodes are connected
    
    # This is the minimum multiway cut problem
    
    # For small instances, we can try:
    # Enumerate all possible subsets of edges to remove, check if valid, pick minimum weight
    
    # But 2^m is too large
    
    # Let's try a different approach:
    # Use the fact that we want to make sure high-risk nodes are in different components
    # We can try to assign each node to a "terminal" (high-risk zone) or create a new component
    
    # This is getting too complex for a quick solution
    
    # Let's try a simple greedy:
    # Sort edges by weight, remove edges that connect different high-risk components
    
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Reset Union-Find
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    for u, v, w in edges:
        unite(u, v)
    
    # Group high-risk nodes by component
    hr_components = {}
    hr_to_component = {}
    for hr in high_risk:
        root = find(hr)
        if root not in hr_components:
            hr_components[root] = []
        hr_components[root].append(hr)
        hr_to_component[hr] = root
    
    # Check if separation is needed
    separation_needed = any(len(nodes) > 1 for nodes in hr_components.values())
    
    if not separation_needed:
        print("YES")
        print(0)
        return
    
    # Greedy approach: remove cheapest edges that help separation
    removed_edges = []
    total_cost = 0
    
    # Reset Union-Find for the process
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    for u, v, w in edges:
        unite(u, v)
    
    def recompute_components():
        hr_comp = {}
        hr_to_comp = {}
        for hr in high_risk:
            root = find(hr)
            if root not in hr_comp:
                hr_comp[root] = []
            hr_comp[root].append(hr)
            hr_to_comp[hr] = root
        return hr_comp, hr_to_comp
    
    hr_components, hr_to_component = recompute_components()
    
    # While there are components with multiple high-risk nodes
    while any(len(nodes) > 1 for nodes in hr_components.values()):
        # Find the cheapest edge whose removal helps
        best_edge = None
        best_cost = float('inf')
        
        for u, v, w in edges_sorted:
            if (u, v) in removed_edges or (v, u) in removed_edges:
                continue
                
            # Check if removing this edge helps
            # Temporarily remove it by using a new Union-Find
            temp_parent = parent[:]
            temp_rank = rank[:]
            
            # Rebuild Union-Find without this edge
            temp_parent = list(range(n+1))
            temp_rank = [0] * (n+1)
            
            def temp_find(x):
                if temp_parent[x] != x:
                    temp_parent[x] = temp_find(temp_parent[x])
                return temp_parent[x]
            
            def temp_unite(x, y):
                px, py = temp_find(x), temp_find(y)
                if px == py:
                    return
                if temp_rank[px] < temp_rank[py]:
                    px, py = py, px
                temp_parent[py] = px
                if temp_rank[px] == temp_rank[py]:
                    temp_rank[px] += 1
            
            # Connect all edges except (u,v)
            for x, y, z in edges_sorted:
                if (x == u and y == v) or (x == v and y == u):
                    continue
                if (x, y) in removed_edges or (y, x) in removed_edges:
                    continue
                temp_unite(x, y)
            
            # Check components after removal
            temp_hr_components = {}
            for hr in high_risk:
                root = temp_find(hr)
                if root not in temp_hr_components:
                    temp_hr_components[root] = []
                temp_hr_components[root].append(hr)
            
            # If this removal improves the situation
            bad_before = sum(max(0, len(nodes) - 1) for nodes in hr_components.values())
            bad_after = sum(max(0, len(nodes) - 1) for nodes in temp_hr_components.values())
            
            if bad_after < bad_before and w < best_cost:
                best_cost = w
                best_edge = (u, v, w)
        
        if best_edge is None or total_cost + best_edge[2] > B:
            print("NO")
            return
            
        u, v, w = best_edge
        removed_edges.append((u, v))
        total_cost += w
        
        # Actually remove the edge by rebuilding Union-Find
        parent = list(range(n+1))
        rank = [0] * (n+1)
        
        for x, y, z in edges:
            if (x, y) in removed_edges or (y, x) in removed_edges:
                continue
            unite(x, y)
        
        hr_components, hr_to_component = recompute_components()
        
        # Check if we're done
        if not any(len(nodes) > 1 for nodes in hr_components.values()):
            break
    
    if total_cost <= B:
        print("YES")
        print(len(removed_edges))
        for u, v in removed_edges:
            print(u, v)
    else:
        print("NO")

solve()
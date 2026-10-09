import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = set()
    for _ in range(t):
        critical.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Find the node with minimum degree among critical nodes
    min_deg = n + 1
    start_node = -1
    for node in critical:
        deg = len(adj[node])
        if deg < min_deg:
            min_deg = deg
            start_node = node
    
    # Dijkstra from start_node
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    total_cost = 0
    critical_remaining = t
    
    for u, v, w in edges:
        # Check if this edge is useful
        # It's useful if it connects two different components
        # and at least one component has a critical node
        # and adding it reduces the total cost
        # The cost of adding this edge is w
        # The benefit is dist[u] + dist[v] - w (if positive)
        # But we need to track which components have critical nodes
        
        # Actually, let's use a different approach:
        # For each edge, we check if it connects two components
        # and if at least one component has critical nodes
        # and if adding it is beneficial
        
        # We need to track for each component:
        # - Whether it has critical nodes
        # - The minimum distance from start_node to any node in the component
        # - The second minimum distance (if applicable)
        
        # Let's use a simpler approach:
        # For each component, track:
        # - has_critical: bool
        # - min_dist: minimum dist among nodes in component
        # - second_min_dist: second minimum dist (or INF if not applicable)
        
        # Actually, let's just track:
        # - has_critical: bool
        # - min_dist: minimum dist among critical nodes in component (or INF if none)
        # - min_dist_non_critical: minimum dist among non-critical nodes in component (or INF if none)
        
        # Hmm, this is getting complicated. Let me think again.
        
        # The key insight is:
        # An edge (u, v, w) is useful if:
        # 1. It connects two different components
        # 2. At least one component has critical nodes
        # 3. The cost of connecting them via this edge (w) is less than the cost via the start_node (dist[u] + dist[v])
        
        # So for each component, we need to track:
        # - Whether it has critical nodes
        # - The minimum dist[u] for u in the component
        
        # But wait, we also need to handle the case where both components have critical nodes
        # In that case, we must connect them, and we should use the minimum cost edge
        
        # Let me re-read the problem...
        
        # OK so the problem is: we have a tree, and we want to find the minimum cost subtree
        # that connects all critical nodes.
        
        # The approach is:
        # 1. Compute dist[v] = shortest path from start_node to v (which is just the unique path in the tree)
        # 2. For each edge (u, v, w), the cost of using this edge to connect two components is w
        #    The cost of connecting them via the start_node is dist[u] + dist[v]
        #    So we should use this edge if w < dist[u] + dist[v]
        # 3. Use Kruskal's algorithm with the modified cost
        
        # But we need to be careful: we can only use an edge if at least one of the components has critical nodes
        
        # Let me implement this properly
        
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        
        # Check if at least one component has critical nodes
        # We need to track this for each component
        # Let's use a separate array
        
        # Actually, let's just check if we should add this edge
        # We should add it if:
        # 1. At least one component has critical nodes
        # 2. w < dist[u] + dist[v]
        
        # But we also need to handle the case where both components have critical nodes
        # In that case, we must connect them eventually
        
        # Let me think about this differently:
        # The final answer is the sum of:
        # - For each critical node v (except start_node), the minimum of:
        #   - dist[v] (cost to connect via start_node)
        #   - The cost of the edge that connects v's component to another component with critical nodes
        
        # Hmm, this is still complicated. Let me just implement the straightforward approach:
        # For each edge, check if it's useful and add it if so
        
        # We need to track for each component whether it has critical nodes
        # Let's use a separate array for this
        
        pass
    
    # Let me restart with a cleaner implementation
    
    # Re-initialize Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    has_critical = [False] * (n + 1)
    for node in critical:
        has_critical[node] = True
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
            has_critical[ry] = has_critical[ry] or has_critical[rx]
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
            has_critical[rx] = has_critical[rx] or has_critical[ry]
        else:
            parent[ry] = rx
            rank[rx] += 1
            has_critical[rx] = has_critical[rx] or has_critical[ry]
        return True
    
    total_cost = 0
    critical_components = t  # Initially, each critical node is in its own component
    
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        
        # Check if this edge is useful
        # It's useful if at least one component has critical nodes
        # and w < dist[u] + dist[v]
        
        if (has_critical[ru] or has_critical[rv]) and w < dist[u] + dist[v]:
            # This edge is useful
            if has_critical[ru] and has_critical[rv]:
                critical_components -= 1
            total_cost += w
            union(u, v)
    
    # Now we need to connect remaining critical components
    # For each critical node v that is not connected to start_node's component,
    # we need to add dist[v] to the total cost
    
    # Actually, let me reconsider the approach
    # The issue is that we might have multiple critical components that need to be connected
    # We should connect them using the minimum cost edges
    
    # Let me use a different approach:
    # 1. For each critical node v, compute dist[v] = shortest path from start_node to v
    # 2. Sort critical nodes by dist[v] (ascending)
    # 3. For each critical node v (in sorted order), if v is not in the same component as start_node,
    #    add dist[v] to the total cost and merge v's component with start_node's component
    
    # Wait, this doesn't work either because we might have already added some edges
    
    # Let me think about this more carefully...
    
    # OK I think the correct approach is:
    # 1. Compute dist[v] for all v
    # 2. For each edge (u, v, w), the effective cost is min(w, dist[u] + dist[v])
    # 3. Use Kruskal's algorithm with the effective cost, but only consider edges where
    #    at least one endpoint is in a component with critical nodes
    
    # Actually, I realize the issue: the effective cost should be computed differently
    # If we use edge (u, v, w), the cost is w
    # If we don't use this edge, the cost to connect u and v is dist[u] + dist[v]
    # So we should use this edge if w < dist[u] + dist[v]
    
    # But the total cost is not just the sum of edge costs
    # We also need to account for the cost of connecting to the start_node
    
    # Let me re-read the problem statement...
    
    # OK so the problem is asking for the minimum cost to connect all critical nodes
    # The cost is the sum of the weights of the edges we choose
    
    # The approach should be:
    # 1. Compute dist[v] = shortest path from start_node to v
    # 2. For each edge (u, v, w), the cost of using this edge is w
    #    The cost of not using this edge (and connecting via start_node) is dist[u] + dist[v]
    # 3. We should use this edge if w < dist[u] + dist[v] and at least one component has critical nodes
    
    # But we also need to ensure that all critical nodes are connected
    # So we need to track which components have critical nodes
    
    # Let me implement this properly
    
    # Re-initialize
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    has_critical = [False] * (n + 1)
    min_dist_in_comp = [INF] * (n + 1)  # Minimum dist among critical nodes in the component
    for node in critical:
        has_critical[node] = True
        min_dist_in_comp[node] = dist[node]
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
            has_critical[ry] = has_critical[ry] or has_critical[rx]
            if has_critical[rx]:
                min_dist_in_comp[ry] = min(min_dist_in_comp[ry], min_dist_in_comp[rx])
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
            has_critical[rx] = has_critical[rx] or has_critical[ry]
            if has_critical[ry]:
                min_dist_in_comp[rx] = min(min_dist_in_comp[rx], min_dist_in_comp[ry])
        else:
            parent[ry] = rx
            rank[rx] += 1
            has_critical[rx] = has_critical[rx] or has_critical[ry]
            if has_critical[ry]:
                min_dist_in_comp[rx] = min(min_dist_in_comp[rx], min_dist_in_comp[ry])
        return True
    
    total_cost = 0
    critical_components = t
    
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        
        # Check if this edge is useful
        # It's useful if at least one component has critical nodes
        # and w < dist[u] + dist[v]
        
        if has_critical[ru] or has_critical[rv]:
            # This edge connects at least one component with critical nodes
            # Check if it's cheaper to use this edge than to connect via start_node
            if w < dist[u] + dist[v]:
                # Use this edge
                if has_critical[ru] and has_critical[rv]:
                    critical_components -= 1
                total_cost += w
                union(u, v)
    
    # Now we need to connect remaining critical components to the start_node
    # For each critical component, we need to add the minimum dist among its critical nodes
    
    # Actually, we need to be more careful here
    # The remaining critical components need to be connected to the start_node's component
    # The cost is the minimum dist among the critical nodes in each component
    
    # But wait, we might have already connected some critical components to the start_node's component
    # So we need to find the component containing the start_node and check if it has critical nodes
    
    # Let me reconsider...
    
    # The issue is that the start_node might not be in a component with any critical nodes
    # (if we haven't added any edges yet)
    
    # Actually, the start_node is a critical node, so it's always in a component with critical nodes
    
    # Let me re-think the algorithm:
    # 1. We start with each node in its own component
    # 2. We process edges in order of increasing weight
    # 3. For each edge (u, v, w):
    #    a. If u and v are in the same component, skip
    #    b. If neither component has critical nodes, skip
    #    c. If w < dist[u] + dist[v], add this edge and merge the components
    # 4. After processing all edges, we need to connect remaining critical components
    #    For each critical component that is not connected to the start_node's component,
    #    we need to add the minimum dist among its critical nodes
    
    # But this is still not quite right...
    
    # Let me think about it differently:
    # The total cost is the sum of:
    # - The cost of edges we added
    # - The cost of connecting remaining critical components to the start_node
    
    # For the second part, we need to find the minimum dist among critical nodes in each component
    # that is not connected to the start_node's component
    
    # But we also need to ensure that we don't double-count
    
    # Actually, I think the correct approach is:
    # 1. Compute dist[v] for all v
    # 2. For each edge (u, v, w), the effective cost is min(w, dist[u] + dist[v])
    # 3. Use Kruskal's algorithm with the effective cost, but only consider edges where
    #    at least one endpoint is in a component with critical nodes
    # 4. The total cost is the sum of effective costs of edges we added
    
    # Wait, but this doesn't account for the cost of connecting to the start_node
    
    # Let me re-read the problem statement again...
    
    # OK I think I understand now. The problem is asking for the minimum cost subtree
    # that connects all critical nodes. This is the Steiner tree problem on a tree.
    
    # For a tree, the Steiner tree can be computed as follows:
    # 1. Find the minimum spanning tree of the critical nodes
    # 2. The Steiner tree is the union of all paths in the original tree that connect the critical nodes
    
    # But computing the MST of critical nodes requires knowing the distance between each pair,
    # which is O(t^2) and might be too slow for large t.
    
    # Let me think of a different approach...
    
    # Actually, for a tree, there's a simpler approach:
    # 1. Root the tree at an arbitrary critical node
    # 2. For each critical node, mark all edges on the path from it to the root
    # 3. The Steiner tree is the set of marked edges
    
    # But this doesn't give the minimum cost Steiner tree...
    
    # Let me think about this more carefully...
    
    # For a tree, the minimum Steiner tree connecting a set of terminals is:
    # - The union of all edges that lie on some path between two terminals
    
    # So the approach is:
    # 1. For each edge, check if it lies on some path between two critical nodes
    # 2. If so, include it in the Steiner tree
    
    # To check if an edge lies on some path between two critical nodes:
    # - Remove the edge, splitting the tree into two components
    # - If both components have at least one critical node, the edge is in the Steiner tree
    
    # This can be done efficiently using a DFS to count critical nodes in each subtree.
    
    # Let me implement this approach.
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n + 1)]
    for i, (u, v, w) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # DFS to count critical nodes in each subtree
    critical_count = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        count = 1 if node in critical else 0
        for neighbor, edge_idx in adj[node]:
            if not visited[neighbor]:
                child_count = dfs(neighbor)
                count += child_count
        critical_count[node] = count
        return count
    
    # Start DFS from node 1
    dfs(1)
    
    # For each edge, check if it's in the Steiner tree
    total_cost = 0
    for i, (u, v, w) in enumerate(edges):
        # Determine which node is the child (the one with smaller critical_count)
        if critical_count[u] < critical_count[v]:
            child = u
        else:
            child = v
        
        # The edge is in the Steiner tree if:
        # - The subtree rooted at 'child' has at least one critical node
        # - The rest of the tree has at least one critical node
        # i.e., 0 < critical_count[child] < t
        
        if 0 < critical_count[child] < t:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()
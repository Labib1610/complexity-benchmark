import sys
from collections import defaultdict
import heapq

def find_mst_with_targets(n, edges, targets):
    if len(targets) <= 1:
        return 0
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Since the graph is a tree (n-1 edges and connected), we can use Prim's algorithm
    # to find the minimum spanning tree that connects all target nodes
    
    # We'll run a modified Prim's algorithm starting from all target nodes simultaneously
    target_set = set(targets)
    in_tree = set()
    heap = []
    
    # Add all target nodes to the heap with cost 0
    for node in targets:
        heapq.heappush(heap, (0, node, -1))  # (cost, node, parent)
    
    total_cost = 0
    edges_in_mst = 0
    
    while heap and edges_in_mst < len(targets) - 1:
        cost, node, parent = heapq.heappop(heap)
        
        if node in in_tree:
            continue
            
        in_tree.add(node)
        if parent != -1 and node in target_set or parent in target_set:
            total_cost += cost
            edges_in_mst += 1
        elif parent != -1:
            total_cost += cost
            edges_in_mst += 1
            
        # Add neighbors to heap
        for neighbor, weight in adj[node]:
            if neighbor not in in_tree:
                heapq.heappush(heap, (weight, neighbor, node))
                
    # Actually, let me think differently. 
    # Since we have a tree and we want to connect all target nodes,
    # we need to find the minimal subtree that connects all targets.
    # This is the Steiner tree problem on a tree, which can be solved optimally.
    
    # For a tree, the optimal solution is:
    # 1. Find the subtree that spans all target nodes
    # 2. This is equivalent to finding all edges in the paths between target nodes
    
    # Better approach: since it's a tree, we can find the minimal connected subgraph
    # containing all targets by running BFS/DFS from one target to find others
    
    # Even simpler: find the union of paths between all pairs of targets
    # But that might overcount. The right way is to find the minimal subtree.
    
    # Optimal approach for tree:
    # Root the tree at any node, then find the minimal subtree containing all targets
    # This is done by finding the union of paths from each target to a fixed root
    # Or better yet, find the "Steiner tree" for the targets in the tree
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. For each target, mark its path to root
    # 3. The union of these paths forms the minimal subtree connecting all targets
    # 4. Sum the weights of edges in this subtree
    
    # Let's implement this properly:
    
    # First, let's build the actual tree structure
    tree = defaultdict(list)
    for u, v, w in edges:
        tree[u].append((v, w))
        tree[v].append((u, w))
    
    # Root the tree at node 1 (or any node)
    root = 1
    
    # DFS to compute parent and depth for each node
    parent = {}
    depth = {}
    weight_to_parent = {}
    
    def dfs(node, par, dep, wt):
        parent[node] = par
        depth[node] = dep
        if par != -1:
            weight_to_parent[node] = wt
        for nei, w in tree[node]:
            if nei != par:
                dfs(nei, node, dep + 1, w)
    
    dfs(root, -1, 0, 0)
    
    # Now find the minimal subtree that connects all targets
    # An edge is in the minimal subtree if removing it disconnects two targets
    
    # Better approach: find the union of paths between all targets
    # In a tree, the minimal subtree connecting a set of nodes is unique
    
    # Algorithm:
    # 1. Take any target as root of our subtree search
    # 2. Do BFS/DFS to find distances to all other targets
    # 3. The edges needed are those in the paths between targets
    
    # Even simpler approach for trees:
    # Find the "Steiner tree" by marking all nodes that lie on paths between targets
    
    # Mark all nodes that are on some path between two targets
    marked = set()
    
    # For each pair of targets, mark the path between them
    target_list = list(targets)
    
    # Function to get path between two nodes in tree
    def get_path(a, b):
        path_a = []
        curr = a
        while curr != -1:
            path_a.append(curr)
            curr = parent[curr]
            
        path_b = []
        curr = b
        while curr != -1:
            path_b.append(curr)
            curr = parent[curr]
            
        # Find LCA by making depths equal
        idx_a, idx_b = 0, 0
        
        # Convert to sets for quick lookup
        ancestors_a = set(path_a)
        ancestors_b = set(path_b)
        
        # Find path from a to LCA
        visited_a = set()
        curr = a
        while curr != -1 and curr not in ancestors_b:
            visited_a.add(curr)
            curr = parent[curr]
            
        lca = curr  # This is the LCA
        
        # Find path from b to LCA
        visited_b = set()
        curr = b
        while curr != -1 and curr != lca:
            visited_b.add(curr)
            curr = parent[curr]
            
        # Union of both paths plus LCA
        return visited_a.union(visited_b).union({lca})
    
    # Simpler: just mark all nodes that are ancestors of targets in some consistent way
    # Most direct approach: do BFS from all targets together until we've processed enough
    
    # Actually, let's use the standard algorithm for Steiner tree in trees:
    # 1. Root tree arbitrarily
    # 2. For each node, compute if it's a terminal, or has a terminal descendant
    # 3. The minimal subtree includes exactly those nodes where both conditions are true
    
    # But we also need to compute the cost...
    
    # Let me restart with a cleaner approach:
    
    # In a tree, the minimal cost to connect all targets is found by:
    # 1. Finding the subtree that spans all targets
    # 2. This can be done by rooting the tree and including an edge if it separates targets
    
    # Simple greedy approach:
    # Run Prim's or Kruskal's but only consider edges needed to keep targets connected
    
    # Since it's already a tree, we just need to find the minimal subtree connecting targets
    
    # Here's the cleanest approach:
    # Use Union-Find but on the original tree structure to find the MST that connects targets
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n + 1))
            self.rank = [0] * (n + 1)
            
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
            
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            return True
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    cost = 0
    targets_in_component = defaultdict(int)
    
    # Initialize count of targets in each component
    for t in targets:
        targets_in_component[t] = 1
    
    # Kruskal's algorithm variant
    for u, v, w in edges:
        pu, pv = uf.find(u), uf.find(v)
        if pu != pv:
            # Check if this edge connects components with targets
            if targets_in_component[pu] > 0 and targets_in_component[pv] > 0:
                cost += w
            # Union the components
            if uf.rank[pu] < uf.rank[pv]:
                pu, pv = pv, pu
            uf.parent[pv] = pu
            if uf.rank[pu] == uf.rank[pv]:
                uf.rank[pu] += 1
            targets_in_component[pu] += targets_in_component[pv]
            targets_in_component[pv] = 0
    
    return cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

targets = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Since m = n-1 and the graph is connected (as per problem statement),
# we can apply the Steiner tree algorithm on a tree

# For a tree, the Steiner tree problem has a polynomial solution
# Root the tree and find the minimal subtree containing all terminals

if t <= 1:
    print(0)
else:
    # Build adjacency list representation of the tree
    from collections import defaultdict, deque
    
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Function to find the minimal subtree connecting all targets
    # Using the fact that in a tree, we can do BFS from all targets
    # and find the union of paths
    
    # More direct approach:
    # Since it's a tree, we can use the following property:
    # The minimum cost to connect k terminals is the sum of edge weights
    # in the minimal subtree containing all terminals
    
    # Algorithm:
    # 1. Root tree at some node
    # 2. Compute for each node whether its subtree contains any terminal
    # 3. An edge should be included if it separates terminals
    
    # Let's root at node 1
    def dfs_mark(node, parent_node):
        # Returns set of terminals in subtree rooted at node
        terminals_here = set()
        if node in target_set:
            terminals_here.add(node)
            
        for nei, _ in adj[node]:
            if nei != parent_node:
                child_terminals = dfs_mark(nei, node)
                terminals_here.update(child_terminals)
                
        return terminals_here
    
    # But we want to compute the cost directly
    def dfs_cost(node, parent_node):
        cost = 0
        terminals_count = 0
        
        if node in target_set:
            terminals_count += 1
            
        for nei, weight in adj[node]:
            if nei != parent_node:
                child_cost, child_count = dfs_cost(nei, node)
                cost += child_cost
                terminals_count += child_count
                
                # If this child subtree has some targets but not all,
                # then this edge must be included
                if child_count > 0 and child_count < t:
                    cost += weight
                    
        return cost, terminals_count
    
    target_set = set(targets)
    
    # Try rooting at first target
    root = targets[0]
    
    # Need a different DFS that computes correctly
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        total_cost = 0
        terminals_in_subtree = 1 if node in target_set else 0
        
        for nei, weight in adj[node]:
            if not visited[nei]:
                cost, count = dfs(nei)
                total_cost += cost
                terminals_in_subtree += count
                
                # If the child subtree has some but not all targets,
                # we must include this edge
                if count > 0 and count < t:
                    total_cost += weight
                    
        return total_cost, terminals_in_subtree
    
    # Reset visited
    visited = [False] * (n + 1)
    
    # Root at first target
    result_cost, _ = dfs(root)
    print(result_cost)
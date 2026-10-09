import sys
from collections import defaultdict
import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x == root_y:
        return False
    
    if rank[root_x] < rank[root_y]:
        root_x, root_y = root_y, root_x
        
    parent[root_y] = root_x
    if rank[root_x] == rank[root_y]:
        rank[root_x] += 1
    return True

def kruskal(n, edges, critical_nodes):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # First, connect all critical nodes
    critical_parent = None
    total_cost = 0
    
    # Find MST that connects all critical nodes
    critical_set = set(critical_nodes)
    connected_critical = set()
    
    # We need to connect all critical nodes with minimum cost
    # This is essentially finding the minimum spanning tree of the subgraph induced by critical nodes
    # But we can use a different approach: build a complete graph of critical nodes where edge weights
    # are the shortest path distances between them, then find MST of that graph.
    
    # However, there's a simpler way for this problem:
    # Since we want all critical nodes to be in the same component,
    # we can just run Kruskal until all critical nodes are connected.
    
    # But let's think differently - since m = n-1 and all edges form a tree,
    # we're looking for the minimum cost subtree that connects all critical nodes.
    # This is the Steiner tree problem on a tree, which has a greedy solution:
    # 1. Take all edges in the unique paths between pairs of critical nodes
    # 2. Find the minimum spanning tree of this edge set
    
    # Even simpler approach for trees:
    # The optimal solution is to take the edges on the paths between consecutive critical nodes
    # when the critical nodes are ordered according to their position in the tree.
    
    # But let's implement a more general approach:
    # Run Kruskal's algorithm but stop when all critical nodes are in the same component
    
    parent_uf = list(range(n + 1))
    rank_uf = [0] * (n + 1)
    
    # Count how many separate critical components we have
    critical_components = len(critical_nodes)
    
    # If there's only one critical node, cost is 0
    if critical_components <= 1:
        return 0
    
    # Process edges in order of increasing weight
    for u, v, w in edges:
        root_u = find(parent_uf, u)
        root_v = find(parent_uf, v)
        
        if root_u != root_v:
            # Check if this edge connects two components that both contain critical nodes
            # Actually, let's just do normal union-find and count components
            
            # Union the sets
            if rank_uf[root_u] < rank_uf[root_v]:
                parent_uf[root_u] = root_v
            elif rank_uf[root_u] > rank_uf[root_v]:
                parent_uf[root_v] = root_u
            else:
                parent_uf[root_v] = root_u
                rank_uf[root_u] += 1
                
            total_cost += w
            
            # Count how many critical nodes are now in the same component
            # This is inefficient, so let's track it properly
            # Let's restart with a cleaner approach
            
    # Cleaner approach:
    # Since the input graph is a tree (m=n-1 and connected), 
    # we need to find the minimum cost subtree that spans all critical nodes.
    # For a tree, this is equivalent to taking the union of all paths between pairs of critical nodes
    # and then finding the minimum spanning tree of that union.
    
    # Even simpler: In a tree, the Steiner tree is unique and consists of all edges on paths
    # between pairs of terminals (critical nodes). The cost is the sum of weights of these edges.
    
    # Efficient algorithm for trees:
    # 1. Root the tree at any node
    # 2. For each critical node, compute path to root
    # 3. Take union of all such paths
    # 4. The result is exactly what we need
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root the tree at node 1 (arbitrary choice)
    root = 1
    
    # BFS to compute parent and distance from root for all nodes
    from collections import deque
    parent_tree = [-1] * (n + 1)
    depth = [0] * (n + 1)
    dist_from_root = [0] * (n + 1)
    
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True
    
    while queue:
        node = queue.popleft()
        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent_tree[neighbor] = node
                depth[neighbor] = depth[node] + 1
                dist_from_root[neighbor] = dist_from_root[node] + weight
                queue.append(neighbor)
    
    # Function to find path between two nodes in a tree
    def get_path_edges(u, v):
        path_edges = []
        # Bring u and v to the same depth
        while depth[u] > depth[v]:
            # Find parent edge of u
            for neighbor, weight in adj[u]:
                if neighbor == parent_tree[u]:
                    path_edges.append(weight)
                    break
            u = parent_tree[u]
            
        while depth[v] > depth[u]:
            # Find parent edge of v
            for neighbor, weight in adj[v]:
                if neighbor == parent_tree[v]:
                    path_edges.append(weight)
                    break
            v = parent_tree[v]
            
        # Now u and v are at the same depth, move up until they meet
        while u != v:
            # Move u up
            for neighbor, weight in adj[u]:
                if neighbor == parent_tree[u]:
                    path_edges.append(weight)
                    break
            u = parent_tree[u]
            
            # Move v up
            for neighbor, weight in adj[v]:
                if neighbor == parent_tree[v]:
                    path_edges.append(weight)
                    break
            v = parent_tree[v]
            
        return path_edges
    
    # Get all edges on paths between critical nodes
    required_edges = set()
    critical_list = list(critical_nodes)
    
    # For efficiency in trees, we can just pick one critical node as "center"
    # and connect all others to it. But to get the true minimum, we should consider
    # that we only need the edges that appear in the union of paths between all pairs.
    
    # Simpler correct approach:
    # In a tree, to connect k critical nodes, we need exactly k-1 paths.
    # The minimum way is to create a "Steiner tree" which is the union of paths
    # that connects all critical nodes with minimal total edge weight.
    
    # For trees, there's a greedy approach:
    # 1. Root tree at arbitrary node
    # 2. Mark all nodes that are critical or are ancestors of critical nodes
    # 3. The minimal subtree includes all edges from marked nodes to their parents
    
    # Mark all critical nodes
    is_critical = [False] * (n + 1)
    for node in critical_nodes:
        is_critical[node] = True
    
    # Mark ancestors of critical nodes using parent_tree
    marked = [False] * (n + 1)
    for node in critical_nodes:
        current = node
        while current != -1 and not marked[current]:
            marked[current] = True
            current = parent_tree[current]
    
    # Collect all edges in the minimal subtree
    total_cost = 0
    for u, v, w in edges:
        # Check if this edge is in our subtree
        # An edge (u,v) is in subtree if one is parent of the other and the child is marked
        if parent_tree[u] == v and marked[u]:
            total_cost += w
        elif parent_tree[v] == u and marked[v]:
            total_cost += w
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

critical_nodes = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and print result
result = kruskal(n, edges, critical_nodes)
print(result)
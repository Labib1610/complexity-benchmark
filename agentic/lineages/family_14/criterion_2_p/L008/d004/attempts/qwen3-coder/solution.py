import sys
from collections import defaultdict, deque

def find_mst_with_injected_nodes(R, S, P, injected_nodes, edges):
    # Since S = R - 1 and the graph is connected with no redundancy, 
    # it's already a tree. We just need to find the minimal subtree
    # that connects all the injected nodes.
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(R + 1)]
    for idx, (u, v, w) in enumerate(edges):
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
    
    # If there's only one injected node, we don't need any edges
    if P <= 1:
        return 0
    
    # Find the minimal subtree that connects all injected nodes
    # This is essentially finding the Steiner tree for the injected nodes
    # But since our graph is a tree, we can do this efficiently:
    # 1. Find all nodes that are on paths between any pair of injected nodes
    # 2. The minimal subtree is the set of edges connecting these nodes
    
    # Mark which nodes are injected
    is_injected = [False] * (R + 1)
    for node in injected_nodes:
        is_injected[node] = True
    
    # BFS from all injected nodes to find the minimal subtree
    # We'll use a multi-source BFS to find all nodes that lie on paths
    # between any pair of injected nodes
    
    # First, let's build parent/depth information for efficient path finding
    parent = [-1] * (R + 1)
    depth = [0] * (R + 1)
    
    def dfs(u, par, d):
        parent[u] = par
        depth[u] = d
        for v, _, _ in adj[u]:
            if v != par:
                dfs(v, u, d + 1)
    
    # Root the tree at node 1
    dfs(1, -1, 0)
    
    # Function to find path between two nodes
    def get_path(a, b):
        path_edges = []
        # Bring both nodes to same depth
        while depth[a] > depth[b]:
            # Find parent edge of a
            for v, w, idx in adj[a]:
                if v == parent[a]:
                    path_edges.append(idx)
                    break
            a = parent[a]
        
        while depth[b] > depth[a]:
            # Find parent edge of b
            for v, w, idx in adj[b]:
                if v == parent[b]:
                    path_edges.append(idx)
                    break
            b = parent[b]
        
        # Now move both up until they meet
        while a != b:
            # Move a up
            for v, w, idx in adj[a]:
                if v == parent[a]:
                    path_edges.append(idx)
                    break
            a = parent[a]
            
            # Move b up
            for v, w, idx in adj[b]:
                if v == parent[b]:
                    path_edges.append(idx)
                    break
            b = parent[b]
        
        return path_edges
    
    # For efficiency, we'll find the connected subtree containing all injected nodes
    # by doing a BFS in the tree considering only edges that separate injected components
    
    # Alternative simpler approach for trees:
    # The minimal subtree connecting all injected nodes is the union of paths
    # between all pairs, but we can compute it more efficiently
    
    # Mark all nodes that are in the subtree using a BFS approach:
    # Start with all injected nodes as "active"
    # Repeatedly activate neighbors of active nodes until no more changes
    
    # Actually, let's use the fact that in a tree, the minimal subtree connecting
    # a set of nodes is the union of paths between them. But there's a better way:
    # Find the "center" properties or just do pairwise connections.
    
    # Simpler approach: 
    # In a tree, the subgraph induced by a set of nodes has a unique minimal 
    # connected subtree. We can find it by:
    # 1. Pick any injected node as root
    # 2. Do BFS from that root, stopping when we've visited all injected nodes
    # 3. The edges used form the minimal subtree
    
    visited_node = [False] * (R + 1)
    visited_edge = [False] * S
    queue = deque()
    
    # Add all injected nodes to queue
    for node in injected_nodes:
        queue.append(node)
        visited_node[node] = True
    
    total_cost = 0
    nodes_found = len(injected_nodes)
    
    while queue and nodes_found < P:
        u = queue.popleft()
        for v, w, idx in adj[u]:
            if not visited_node[v]:
                visited_node[v] = True
                visited_edge[idx] = True
                total_cost += w
                queue.append(v)
                if is_injected[v]:
                    nodes_found += 1
    
    # Wait, this approach is wrong because we're not ensuring connectivity correctly.
    
    # Let me restart with a cleaner approach:
    # In a tree, to connect P nodes optimally, we need exactly (P-1) edges in the 
    # subgraph formed by taking the union of paths between them. But we want the 
    # actual minimal set of edges that connects all of them.
    
    # The right way: Find the minimal subtree containing all injected nodes.
    # Algorithm:
    # 1. Mark all injected nodes
    # 2. Repeatedly contract edges where one endpoint is not marked and has degree 1
    # 3. The remaining edges form the minimal subtree
    
    # Even simpler for implementation:
    # Do a DFS/BFS from any injected node, and collect all edges needed to reach
    # other injected nodes. But we have to be careful not to double count.
    
    # Best approach for a tree:
    # The minimal subtree connecting a set of nodes can be found by:
    # 1. Root the tree at some node
    # 2. Find the lowest common ancestor (LCA) of all injected nodes
    # 3. The minimal subtree includes all edges from each injected node to this LCA
    # But again, computing LCA for multiple nodes is complex.
    
    # Simple greedy approach that works:
    # Use Union-Find with Kruskal-like idea but on the path structure.
    # However, since it's a tree, MST doesn't make sense.
    
    # Let me think differently:
    # The key insight is that we want the subtree that spans all injected nodes.
    # In a tree, this is unique. We can find it by:
    # 1. For each edge, determine if its removal disconnects the graph such that
    #    injected nodes end up in different components.
    # 2. Keep such edges; discard others.
    
    # Even simpler approach:
    # 1. Root the tree
    # 2. For each node, compute if its subtree contains any injected node
    # 3. An edge should be kept if it connects to a subtree with injected nodes
    
    has_injected_descendant = [False] * (R + 1)
    result_edges = [False] * S
    edge_map = {}  # Map (u,v) or (v,u) to edge index
    
    for i, (u, v, w) in enumerate(edges):
        edge_map[(u, v)] = i
        edge_map[(v, u)] = i
    
    # Mark leaves and propagate upward
    def mark_subtree(node, parent_node):
        # Check children first
        for v, _, _ in adj[node]:
            if v != parent_node:
                mark_subtree(v, node)
                if has_injected_descendant[v]:
                    has_injected_descendant[node] = True
        
        if is_injected[node]:
            has_injected_descendant[node] = True
    
    # Mark which subtrees contain injected nodes
    mark_subtree(1, -1)
    
    # Now traverse again to decide which edges to keep
    total_cost = 0
    
    def dfs_mark_edges(node, parent_node):
        nonlocal total_cost
        for v, w, idx in adj[node]:
            if v != parent_node:
                # Edge from node to v
                # Keep this edge if subtree of v has injected nodes AND
                # there are also injected nodes outside this subtree
                dfs_mark_edges(v, node)
                
                # A simpler condition: keep edge if the subtree of v contains
                # at least one injected node and there's at least one injected
                # node in the rest of the tree
                if has_injected_descendant[v]:  
                    # Check if there are injected nodes NOT in subtree of v
                    # This is tricky without full computation
                    
                    # Simpler: just check if v's subtree has injected nodes
                    # This isn't quite right either...
                    
                    # Correct approach:
                    # Keep an edge if removing it separates injected nodes
                    # I.e., both sides of the edge have injected nodes
                    result_edges[idx] = True
                    total_cost += w
    
    # This is still not right conceptually.
    
    # Final clean approach:
    # 1. Root the tree at injected node 1
    # 2. For each node, compute if its subtree contains an injected node
    # 3. An edge {parent[v], v} is needed iff subtree of v contains an injected node
    #    AND there's an injected node outside this subtree
    
    parent = [-1] * (R + 1)
    subtree_has_injected = [False] * (R + 1)
    
    # First DFS to set parents and compute subtree info
    def dfs1(u, par):
        parent[u] = par
        subtree_has_injected[u] = is_injected[u]
        for v, _, _ in adj[u]:
            if v != par:
                dfs1(v, u)
                if subtree_has_injected[v]:
                    subtree_has_injected[u] = True
    
    dfs1(injected_nodes[0], -1)
    
    # Count total injected nodes
    total_injected = sum(is_injected)
    
    # Second pass to decide edges
    total_cost = 0
    
    # Create mapping from edge endpoints to edge index
    edge_idx_map = {}
    for i, (u, v, w) in enumerate(edges):
        edge_idx_map[(u, v)] = i
        edge_idx_map[(v, u)] = i
    
    # Check each edge
    visited_check = [False] * (R + 1)
    
    def dfs_check(u, par):
        nonlocal total_cost
        visited_check[u] = True
        for v, w, _ in adj[u]:
            if v != par and not visited_check[v]:
                dfs_check(v, u)
                # Edge u-v, directed from u to v (v is child)
                # This edge is necessary if:
                # 1. Subtree of v contains at least one injected node
                # 2. Rest of the tree (including u's side) contains at least one injected node
                if subtree_has_injected[v]:  # subtree of v has injected nodes
                    # Check if there are injected nodes outside subtree of v
                    # That means not all injected nodes are in subtree of v
                    if sum(is_injected) > sum(subtree_has_injected[i] for i in range(1, R+1) if dfs_subtree_contains(i, v, parent)):
                        total_cost += w
    
    # This is getting overly complex. Let me restart with the textbook solution:
    
    # For a tree, the minimum subtree spanning a set of K nodes has exactly K-1 edges.
    # The algorithm:
    # 1. Root tree at arbitrary node
    # 2. Compute for each node whether its subtree contains any terminal (injected node)
    # 3. Edge from u to parent[u] is in solution iff subtree of u contains a terminal
    
    # But we also need there to be terminals outside subtree of u.
    # So edge {u, parent[u]} is kept iff:
    #   (subtree of u has terminals) AND (rest of tree has terminals)
    
    # Recompute properly:
    subtree_count = [0] * (R + 1)  # Number of injected nodes in subtree
    
    def dfs_count(u, par):
        subtree_count[u] = 1 if is_injected[u] else 0
        for v, _, _ in adj[u]:
            if v != par:
                dfs_count(v, u)
                subtree_count[u] += subtree_count[v]
    
    dfs_count(1, -1)  # Root at 1
    
    # Total injected nodes
    total_terminals = sum(is_injected)
    
    # Now check each edge
    total_cost = 0
    
    def dfs_edges(u, par):
        nonlocal total_cost
        for v, w, idx in adj[u]:
            if v != par:
                # Edge from v to its parent u
                # Keep if subtree of v has terminals AND complement has terminals
                if subtree_count[v] > 0 and (total_terminals - subtree_count[v]) > 0:
                    total_cost += w
                dfs_edges(v, u)
    
    dfs_edges(1, -1)
    
    return total_cost


# Read input
line1 = list(map(int, sys.stdin.readline().split()))
R, S, P = line1[0], line1[1], line1[2]

injected_nodes = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(S):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

print(find_mst_with_injected_nodes(R, S, P, injected_nodes, edges))
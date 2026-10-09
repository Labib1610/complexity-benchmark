import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    required = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one required site, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find the spanning tree that connects all required nodes
    # We can do this by finding the minimal subtree that spans all required nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # First, find all nodes that are required
    required_nodes = set(required)
    
    # If we have a tree structure, we can find the minimal connected subtree
    # that contains all required nodes by:
    # 1. Finding the paths between all pairs of required nodes
    # 2. Taking the union of all these paths
    # But there's a more efficient way:
    # In a tree, the minimal connected subtree containing a set of nodes
    # is the union of all paths between consecutive nodes in any ordering
    # that includes all required nodes.
    # Even better: we can find the "Steiner tree" by:
    # - Rooting the tree at any node
    # - Finding the minimal subtree containing all required nodes
    # - This is equivalent to finding the edges that must be included
    
    # Efficient approach:
    # The minimal cost to connect all required nodes in a tree
    # is the sum of edge weights in the minimal subtree spanning all required nodes.
    # This can be computed by:
    # 1. Rooting the tree at an arbitrary node
    # 2. For each node, compute whether its subtree contains any required node
    # 3. An edge is included if it connects two subtrees that both contain required nodes,
    #    or if it's on the path between required nodes
    
    # Let's root the tree at node 1
    root = 1
    
    # Build parent pointers and depths via BFS
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    edge_to_parent = [0] * (n + 1)  # weight of edge to parent
    
    queue = deque([root])
    depth[root] = 0
    parent[root] = -1
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if depth[v] == -1:  # not visited
                depth[v] = depth[u] + 1
                parent[v] = u
                edge_to_parent[v] = w
                queue.append(v)
    
    # Now, for each node, determine if its subtree contains a required node
    # We'll do a post-order traversal (DFS)
    visited = [False] * (n + 1)
    contains_required = [False] * (n + 1)
    
    # Get all nodes in post-order
    post_order = []
    stack = [root]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            post_order.append(u)
            for v, w in adj[u]:
                if not visited[v] and v != parent[u]:
                    stack.append(v)
    
    # Process in reverse post-order (which is post-order)
    # Mark which nodes contain required nodes in their subtree
    for u in reversed(post_order):
        contains_required[u] = (u in required_nodes)
        for v, w in adj[u]:
            if v != parent[u] and depth[v] > depth[u]:  # child of u
                contains_required[u] = contains_required[u] or contains_required[v]
    
    # Now, count the edges that must be included
    # An edge (parent[v], v) is included if v's subtree contains at least one required node
    # AND the rest of the tree (including parent[v]) contains at least one required node
    # But there's a simpler way:
    # An edge (u, v) where depth[u] < depth[v] is included if:
    # v's subtree contains a required node AND
    # the rest of the tree (removing v's subtree) also contains a required node
    
    # Even simpler: 
    # In the rooted tree, edge (parent[v], v) is in the Steiner tree if
    # v's subtree contains at least one required node and
    # v's subtree doesn't contain ALL required nodes
    
    total_required = len(required_nodes)
    total_cost = 0
    
    # For each node v (except root), check if edge (parent[v], v) should be included
    for v in range(1, n + 1):
        if parent[v] != -1 and contains_required[v]:  # v has a parent and its subtree has required nodes
            # Check if v's subtree contains ALL required nodes
            # If not, then the edge from parent to v must be included
            # But to do that efficiently, we need to count how many required nodes are in v's subtree
            # Let's recompute this properly
            
            # Let's do a proper count
            count_in_subtree = [0] * (n + 1)
            
            # Recompute in post-order
            for u in reversed(post_order):
                count_in_subtree[u] = (1 if u in required_nodes else 0)
                for v_child, w in adj[u]:
                    if v_child != parent[u] and depth[v_child] > depth[u]:  # child
                        count_in_subtree[u] += count_in_subtree[v_child]
            
            # Now for each edge (parent[v], v), it's included if:
            # count_in_subtree[v] > 0 and count_in_subtree[v] < total_required
            if count_in_subtree[v] > 0 and count_in_subtree[v] < total_required:
                total_cost += edge_to_parent[v]
    
    print(total_cost)

if __name__ == "__main__":
    main()
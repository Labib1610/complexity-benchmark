import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one critical module, cost is 0
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
    
    # Find the subtree that spans all critical nodes
    # We need to find all edges in the subtree that connects all critical nodes
    
    # First, find all nodes in the subtree spanning the critical nodes
    # This is equivalent to finding the minimal subtree containing all critical nodes
    
    # We can do this by:
    # 1. Starting from one critical node
    # 2. Doing BFS/DFS to find paths to all other critical nodes
    # 3. The union of all these paths gives us the minimal subtree
    
    # But there's a simpler approach for a tree:
    # The minimal subtree connecting all critical nodes is the union of paths between all pairs
    # However, we can do better: it's the subtree induced by the critical nodes
    
    # In a tree, the minimal connected subgraph containing a set of nodes
    # is the union of paths between them. But actually, it's simpler:
    # it's the subtree formed by taking all paths between consecutive nodes
    # in some ordering. Even simpler: we can find the "Steiner tree" for the critical nodes.
    
    # For a tree, the minimal subtree containing all critical nodes can be found by:
    # 1. Root the tree at some node
    # 2. Find the lowest common ancestors of all critical nodes
    # 3. The minimal subtree consists of all paths from each critical node to the root,
    #    but that's not quite right either.
    
    # Let me think differently:
    # In a tree, to connect k critical nodes, we need exactly k-1 edges in the final tree.
    # But which edges? We need the edges of the minimal subtree containing all critical nodes.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. For each node, compute if its subtree contains any critical node
    # 3. An edge is in the minimal subtree if it connects two subtrees that both contain critical nodes
    
    # Let's implement this
    
    # Root the tree at node 1
    root = 1
    
    # Build parent relationships and depths via BFS
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    children = defaultdict(list)
    
    queue = deque([root])
    depth[root] = 0
    parent[root] = -1
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if depth[v] == -1:  # Not visited
                depth[v] = depth[u] + 1
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # For each node, compute if its subtree contains any critical node
    contains_critical = [False] * (n + 1)
    
    # Post-order traversal to compute contains_critical
    def dfs(u):
        # Check if u itself is critical
        if u in critical:
            contains_critical[u] = True
        
        # Check children
        for v, w in children[u]:
            dfs(v)
            if contains_critical[v]:
                contains_critical[u] = True
    
    dfs(root)
    
    # Now, collect all edges in the minimal subtree
    # An edge (u, v) where u is parent of v is in the minimal subtree
    # if v's subtree contains at least one critical node AND
    # there exists a critical node outside v's subtree
    
    # But actually, in the minimal subtree connecting all critical nodes,
    # an edge is included if it separates the set of critical nodes into two non-empty parts.
    
    # Simpler approach:
    # In the rooted tree, for each edge from parent to child,
    # include it in the solution if the child's subtree contains at least one critical node
    # and there is at least one critical node outside the child's subtree.
    
    # But we need to be more careful. Let's think of it this way:
    # The minimal subtree connecting all critical nodes has the property that
    # every edge in it separates the critical nodes into two non-empty sets.
    
    # In a tree, the minimal subtree containing all critical nodes can be found by:
    # 1. For each edge, check if removing it separates the critical nodes
    # 2. This happens iff both components after removal contain critical nodes
    
    # But there's an even simpler linear-time approach:
    # Do a post-order traversal. For each node, count critical nodes in its subtree.
    # For each edge to a child, if child's subtree has at least 1 critical node
    # and < t critical nodes, then this edge is in the minimal subtree.
    
    # Count critical nodes in each subtree
    crit_count = [0] * (n + 1)
    
    # Another post-order DFS
    def dfs2(u):
        if u in critical:
            crit_count[u] = 1
        for v, w in children[u]:
            dfs2(v)
            crit_count[u] += crit_count[v]
    
    dfs2(root)
    
    # Now collect the edges
    total_cost = 0
    def dfs3(u):
        nonlocal total_cost
        for v, w in children[u]:
            # If v's subtree has at least one critical node and not all critical nodes
            # then edge (u,v) is in the minimal subtree
            if crit_count[v] > 0 and crit_count[v] < t:
                total_cost += w
            dfs3(v)
    
    dfs3(root)
    
    print(total_cost)

if __name__ == "__main__":
    main()
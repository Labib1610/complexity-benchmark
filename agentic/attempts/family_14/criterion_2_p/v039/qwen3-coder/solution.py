import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one or zero critical facilities, cost is 0
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
    
    # Find the minimal subtree that connects all critical nodes
    # We can do this by finding the Steiner tree on the tree graph
    
    # First, we find the union of paths between all pairs of critical nodes
    # But since it's a tree, we can find the minimal connected subgraph containing all critical nodes
    # by finding the minimal subtree that spans all critical nodes
    
    # A simpler approach: since it's a tree, the minimal connecting subgraph 
    # is the subgraph induced by all edges on paths between critical nodes
    
    # Let's use the fact that in a tree, the minimal connected subgraph containing 
    # a set of vertices is the union of paths between them
    
    # Better approach: 
    # 1. Root the tree at any node
    # 2. Find the minimal subtree containing all critical nodes
    
    # Even simpler: 
    # Since it's a tree, we can find the "Steiner tree" by:
    # - Finding all nodes that are on paths between critical nodes
    # - The cost is the sum of edge weights in this subtree
    
    # Efficient way:
    # Use the fact that in a tree, the minimal subtree spanning a set of nodes
    # can be found by:
    # 1. Taking all paths between pairs of critical nodes
    # 2. Union of these paths gives us the required edges
    
    # But even better: 
    # In a tree, the minimal connected subgraph containing S is the 
    # union of paths P(u,v) for all u,v in S.
    # However, we can compute it more efficiently:
    # Root the tree, compute LCA, then the minimal subtree weight 
    # equals sum_{e in E} w(e) * |paths using e|
    
    # Let's implement a clean solution:
    # 1. Root the tree at node 1
    # 2. Compute parent, depth, and for each edge count how many critical pairs use it
    # 3. Sum up the costs
    
    # Actually, let's think differently:
    # The minimal cost to connect all critical nodes in a tree is 
    # the cost of the subtree that includes all critical nodes and has no unnecessary branches
    
    # Algorithm:
    # 1. Mark all critical nodes
    # 2. Do a DFS to determine for each node if its subtree contains any critical node
    # 3. Count an edge only if both its endpoints have critical nodes in their subtrees (in opposite directions)
    
    # Let's root at node 1
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}
    
    # Build rooted tree with edge weights
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                children[u].append(v)
                edge_weight[(u, v)] = w
                edge_weight[(v, u)] = w
                queue.append(v)
    
    # For each node, compute if its subtree contains any critical node
    contains_critical = [False] * (n + 1)
    
    def dfs(node):
        # Leaf nodes
        has_critical = node in critical
        for child in children[node]:
            has_critical |= dfs(child)
        contains_critical[node] = has_critical
        return has_critical
    
    dfs(1)
    
    # Now count the cost: include an edge if it separates parts of the tree that both contain critical nodes
    total_cost = 0
    for u in range(1, n + 1):
        for v in children[u]:
            # Edge from u to v
            # If both u's subtree (including u) and v's subtree contain critical nodes,
            # then this edge must be included
            # But we need to be careful about what "contains"
            # contains_critical[v] tells if subtree of v has critical node
            # We also need to check if the rest (including u but excluding v's subtree) has critical node
            if contains_critical[v]:  # v's subtree has critical node
                # Check if the rest of the tree from u's perspective has critical node
                # This is true if u itself or any other child of u has critical, or u's parent side has critical
                # Simpler: if the whole tree has > 1 critical nodes and v's subtree has some,
                # and the complement also has some, then we count the edge
                # Actually, let's reframe:
                # An edge {u,v} where u is parent of v should be counted if:
                # 1. v's subtree contains at least one critical node
                # 2. The rest of the tree (V \ subtree of v) also contains at least one critical node
                
                # Total critical nodes
                total_critical = len(critical)
                # Critical nodes in subtree of v
                crit_in_subtree_v = count_critical_in_subtree(v)
                # Critical nodes outside subtree of v
                crit_outside_v = total_critical - crit_in_subtree_v
                
                if crit_in_subtree_v > 0 and crit_outside_v > 0:
                    total_cost += edge_weight[(u, v)]
    
    # Helper function to count critical nodes in subtree
    critical_count = [0] * (n + 1)
    
    def count_critical_in_subtree(node):
        if critical_count[node] != 0:
            return critical_count[node]
        count = 1 if node in critical else 0
        for child in children[node]:
            count += count_critical_in_subtree(child)
        critical_count[node] = count
        return count
    
    # Recompute with helper
    total_cost = 0
    for u in range(1, n + 1):
        for v in children[u]:
            crit_in_subtree_v = count_critical_in_subtree(v)
            crit_outside_v = len(critical) - crit_in_subtree_v
            
            if crit_in_subtree_v > 0 and crit_outside_v > 0:
                total_cost += edge_weight[(u, v)]
                
    print(total_cost)

if __name__ == "__main__":
    main()
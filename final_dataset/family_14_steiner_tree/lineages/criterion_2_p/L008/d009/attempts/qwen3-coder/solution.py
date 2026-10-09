import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    R, S, P = map(int, sys.stdin.readline().split())
    mandated = set(map(int, sys.stdin.readline().split()))
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(S):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one mandated node, no corridors are needed
    if P == 1:
        print(0)
        return
    
    # Find the minimal subtree that connects all mandated nodes
    # We'll do this by finding the Steiner tree approximation:
    # 1. Build a virtual tree (also called auxiliary tree) on the mandated nodes
    # 2. The nodes of this tree are the mandated nodes plus their pairwise LCA's
    # However, we can simplify using the fact that we're on a tree:
    # The minimal connected subtree containing all mandated nodes is unique.
    # We can find it by:
    # - Rooting the tree at some node
    # - Finding the minimal subtree that includes all mandated nodes
    
    # Let's root the tree at node 1
    root = 1
    # But make sure root exists; if not, use the first node in adjacency list
    if root not in adj:
        root = next(iter(adj))
    
    # DFS to build parent/depth info
    parent = {root: -1}
    depth = {root: 0}
    dfs_tree = defaultdict(list)
    
    stack = [root]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                dfs_tree[u].append((v, w))
                dfs_tree[v].append((u, w))
                stack.append(v)
    
    # Function to compute LCA of two nodes
    def lift(node, k):
        while k > 0:
            node = parent[node]
            k -= 1
        return node
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        u = lift(u, depth[u] - depth[v])
        if u == v:
            return u
        # Now they are at same depth, move both up until they meet
        while parent[u] != parent[v]:
            u = parent[u]
            v = parent[v]
        return parent[u]
    
    # Compute all pairwise LCA's of mandated nodes to get the set of all necessary nodes
    # But that might be too many. Instead, let's do a more direct approach:
    # Find the minimal connected subtree containing all mandated nodes.
    
    # Alternative simpler method:
    # Since it's a tree, we can do the following:
    # Mark all mandated nodes as "must include"
    # Then, for each node, determine if it's needed in the subtree
    # A node is needed if it's mandated OR if it's an ancestor of a mandated node
    # OR if it's on the path between two mandated nodes.
    
    # Even simpler: since we want the minimal connected subgraph containing all mandated nodes,
    # we can do a BFS/DFS from all mandated nodes simultaneously until we've covered all
    # nodes that are on paths between mandated nodes.
    
    # Actually, let's think differently:
    # The minimal subtree connecting all mandated nodes is the union of paths between
    # all pairs of mandated nodes. But we don't need all pairs.
    # We can take any spanning tree of the mandated nodes (in the metric closure),
    # but since we're already on a tree, the metric closure is just the original tree.
    
    # So the optimal solution is to take the minimal subtree that connects all mandated nodes.
    # This is equivalent to finding the "Steiner tree" on a tree, which has a known algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute whether the subtree rooted at that node contains any mandated node
    # 3. The edges in our final tree are those where both endpoints are in the minimal subtree
    
    # Let's implement this properly:
    
    # First, let's do a post-order traversal to mark which subtrees contain mandated nodes
    contains_mandated = {}
    
    def dfs_mark(u, par):
        has_mandated = u in mandated
        for v, w in dfs_tree[u]:
            if v != par:
                child_has = dfs_mark(v, u)
                has_mandated |= child_has
        contains_mandated[u] = has_mandated
        return has_mandated
    
    dfs_mark(root, -1)
    
    # Now, traverse again to collect the edges in the minimal subtree
    total_cost = 0
    
    def dfs_collect(u, par):
        nonlocal total_cost
        for v, w in dfs_tree[u]:
            if v != par:
                # If both u and v are part of the minimal subtree, add the edge
                # In the rooted view, if the edge (u,v) is such that the subtree of v
                # contains a mandated node, and the rest of the tree also contains a mandated node,
                # then this edge is in the minimal subtree.
                # But actually, in the minimal subtree connecting all mandated nodes,
                # an edge is included if removing it would disconnect the graph into two parts,
                # each containing at least one mandated node.
                
                # Simpler logic:
                # An edge (u,v) is in the minimal subtree if:
                # 1. The subtree of v (when removing edge u-v) contains at least one mandated node
                # 2. The rest of the tree (including u) contains at least one mandated node
                
                # But since we're dealing with a tree, we can simplify:
                # Do a DFS from all mandated nodes, and include an edge if it's on a path
                # between two mandated nodes.
                
                # Let's try yet another approach:
                # The minimal subtree is the union of paths between all pairs of mandated nodes.
                # But that's O(P^2).
                
                # Best approach:
                # Root the tree. For each node, count how many mandated nodes are in its subtree.
                # An edge (parent[v], v) is in the minimal subtree iff:
                # count[v] > 0 and count[v] < P
                # That is, the subtree of v contains some but not all mandated nodes.
                
                # We already have 'contains_mandated' which tells us if subtree contains >=1 mandated node.
                # We also need to know how many.
                
                # Let's recompute with counts:
                def dfs_count(u, par):
                    count = 1 if u in mandated else 0
                    for v, w in dfs_tree[u]:
                        if v != par:
                            c = dfs_count(v, u)
                            count += c
                    counts[u] = count
                    return count
                
                # But we already did one DFS. Let's restart with proper counting.
                # Actually, let's fix the existing approach.
                
                # contains_mandated tells us if subtree contains at least one mandated node.
                # We also need to know if the complement (rest of the tree) contains at least one.
                # That's true if total > count in subtree.
                
                # Let's re-initialize properly:
    counts = {}
    
    def dfs_count(u, par):
        count = 1 if u in mandated else 0
        for v, w in dfs_tree[u]:
            if v != par:
                c = dfs_count(v, u)
                count += c
        counts[u] = count
        return count
    
    dfs_count(root, -1)
    total_mandated = counts[root]
    
    # Now traverse edges and decide which ones to include
    def dfs_edges(u, par):
        nonlocal total_cost
        for v, w in dfs_tree[u]:
            if v != par:
                # Edge u-v
                # It's in minimal subtree if:
                # counts[v] > 0 and counts[v] < total_mandated
                if counts[v] > 0 and counts[v] < total_mandated:
                    total_cost += w
                dfs_edges(v, u)
    
    dfs_edges(root, -1)
    print(total_cost)

if __name__ == "__main__":
    main()
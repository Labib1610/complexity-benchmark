import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    patent_holders = set(map(int, sys.stdin.readline().split()))
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Convert patent_holders to a list for indexing
    ph_list = list(patent_holders)
    
    # For each node, we need to be able to find paths between any two patent holders
    # But since it's a tree, the path between any two nodes is unique
    # So we need to find the union of all paths between all pairs of patent holders
    
    # To do this efficiently, we can find the minimal subtree that contains all patent holders
    # This is the Steiner tree for the set of patent holders
    
    # One approach: find the "center" or use subtree approach
    # But simpler: since it's a tree, we can do the following:
    # 1. Pick any patent holder as root
    # 2. Do DFS to find all nodes needed
    
    # Let's build a subtree that contains all patent holders with minimal edges
    # This is essentially finding the minimal connected subtree containing all patent holders
    
    # Approach:
    # 1. Root the tree at one of the patent holders
    # 2. For each node, compute if it's an ancestor of any patent holder
    # 3. An edge is needed if it's on the path between two patent holders
    
    # More efficient approach:
    # Use the fact that in a tree, the union of paths between all pairs of a subset
    # is the same as the minimal subtree containing that subset
    
    # Algorithm:
    # 1. Root the tree at any node
    # 2. For each node, compute if its subtree contains any patent holder
    # 3. An edge is needed if it connects two parts that each contain at least one patent holder
    
    root = ph_list[0]
    
    # Build parent relationships and depths via BFS
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    children = defaultdict(list)
    
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                children[u].append((v, w))
                queue.append(v)
    
    # For each node, compute if its subtree contains any patent holder
    contains_patent = [False] * (n + 1)
    
    # Mark leaves
    for ph in patent_holders:
        contains_patent[ph] = True
    
    # Propagate up
    # Process nodes in reverse topological order (by decreasing depth)
    nodes_by_depth = [(depth[i], i) for i in range(1, n + 1)]
    nodes_by_depth.sort(reverse=True)
    
    for _, u in nodes_by_depth:
        for v, w in children[u]:
            if contains_patent[v]:
                contains_patent[u] = True
    
    # Now, count edges where both endpoints have contains_patent = True
    # But we need edges that are on paths between patent holders
    # An edge (u,v) where v is child of u is needed if:
    # 1. v's subtree contains at least one patent holder, AND
    # 2. There exists a patent holder outside v's subtree
    
    total_cost = 0
    
    # Check all edges
    for u in range(1, n + 1):
        for v, w in children[u]:
            # Edge from u to v
            # v's subtree contains some patent holders
            if contains_patent[v]:
                # We need to check if there are patent holders outside v's subtree
                # This is true if the total number of patent holders in the tree
                # is more than those in v's subtree
                # But actually, since we're looking at the minimal subtree containing ALL patent holders,
                # an edge is needed if v's subtree contains at least one patent holder
                # and the rest of the tree contains at least one patent holder
                # This is equivalent to: v's subtree contains some but not all patent holders
                # OR v's subtree contains all patent holders but u is not in subtree (which is impossible in this traversal)
                
                # Let's count patent holders in v's subtree
                # We need to do a separate DFS to count
                def count_patents_in_subtree(node, par):
                    count = 1 if node in patent_holders else 0
                    for child, _ in children[node]:
                        if child != par:
                            count += count_patents_in_subtree(child, node)
                    return count
                
                patents_in_v_subtree = count_patents_in_subtree(v, u)
                
                # If v's subtree has at least one patent holder and not all of them,
                # then this edge is needed
                if patents_in_v_subtree > 0 and patents_in_v_subtree < t:
                    total_cost += w
                elif patents_in_v_subtree == t:
                    # All patent holders are in v's subtree, so edge (u,v) is not needed
                    # unless u is also part of the minimal subtree, but since we're going down from root,
                    # and root is a patent holder, this case is handled correctly
                    pass
    
    # Wait, there's a simpler way
    # The minimal subtree containing all patent holders has exactly (number of patent holders - 1) edges
    # But that's not right either, because we're looking for edges in the original tree that must be included
    
    # Let me re-think:
    # We need all edges that lie on paths between any pair of patent holders
    # In a tree, this is equivalent to the minimal connected subtree containing all patent holders
    
    # Let's use a different approach:
    # 1. Find all pairwise paths between patent holders
    # 2. Take union of all edges in these paths
    # But this is inefficient
    
    # Better approach:
    # 1. Root tree at arbitrary node
    # 2. Find for each node whether its subtree contains any patent holder
    # 3. An edge from parent to child is needed iff child's subtree contains at least one patent holder
    #    AND there exists a patent holder outside child's subtree
    
    # Since the root can be any node, let's root it at node 1 for simplicity
    root = 1
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # Count patent holders in each subtree
    patent_count = [0] * (n + 1)
    
    # Initialize leaves
    for i in range(1, n + 1):
        if i in patent_holders:
            patent_count[i] = 1
    
    # Propagate up
    nodes_by_depth = [(depth[i] if 'depth' in locals() else 0, i) for i in range(1, n + 1)]
    if 'depth' not in locals():
        # Recompute depth
        depth = [0] * (n + 1)
        queue = deque([root])
        depths_computed = [False] * (n + 1)
        depths_computed[root] = True
        while queue:
            u = queue.popleft()
            for v, w in children[u]:
                if not depths_computed[v]:
                    depths_computed[v] = True
                    depth[v] = depth[u] + 1
                    queue.append(v)
        nodes_by_depth = [(depth[i], i) for i in range(1, n + 1)]
        
    nodes_by_depth.sort(reverse=True)
    
    for _, u in nodes_by_depth:
        for v, w in children[u]:
            patent_count[u] += patent_count[v]
    
    # Now, an edge from u to v (where v is child of u) is needed if:
    # patent_count[v] > 0 and patent_count[v] < t
    total_cost = 0
    for u in range(1, n + 1):
        for v, w in children[u]:
            if 0 < patent_count[v] < t:
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()
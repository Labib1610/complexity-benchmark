import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    # If there's only one target, no pipes needed
    if t <= 1:
        print(0)
        return
    
    target_set = set(targets)
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find the spanning tree that connects all target nodes with minimal cost
    # This is essentially finding the Steiner tree, but we'll use the fact that 
    # we can build the minimal subtree that spans all targets
    
    # First, we find the induced subgraph that contains all paths between target nodes
    # We can do this by finding the union of all paths between pairs of targets
    # But more efficiently, we can find the minimal subtree containing all targets
    
    # Approach:
    # 1. Do a BFS/DFS from one target node to find distances to all other nodes
    # 2. Among all targets, find the one with minimum distance to the current set
    # 3. Add it to the set and update distances
    # This is Prim's algorithm for the Steiner tree
    
    # Actually, let's think differently:
    # We want the minimum cost to connect all targets
    # This is the minimum Steiner tree problem which is NP-hard in general
    # But on a tree, it's solvable in polynomial time
    
    # On a tree, the Steiner tree is the subgraph obtained by taking the union of 
    # all paths between pairs of terminals, then removing unnecessary leaves
    
    # Simpler approach:
    # Since the graph is a tree, the minimal way to connect all targets
    # is to take the subtree that contains all of them
    # This can be found by:
    # 1. Marking all target nodes
    # 2. Doing a traversal to find all nodes that are on paths between targets
    # 3. The edges in this subtree form the solution
    
    # Even simpler:
    # Root the tree at some node, compute for each node whether its subtree contains
    # any target. Then, an edge should be included if it connects two components
    # each containing at least one target.
    
    # Best approach:
    # Use the fact that in a tree, the minimal subtree containing all targets
    # has exactly (number of targets - 1) edges if we minimize properly.
    # But actually, we need to include ALL edges on paths between targets.
    
    # Let's use the standard algorithm for Steiner tree on trees:
    # 1. Root the tree at an arbitrary node
    # 2. For each node, compute if its subtree contains any target
    # 3. An edge is in the Steiner tree if both its endpoints' subtrees contain targets
    
    # Pick root as first target
    root = targets[0]
    
    # Build parent relationships and depths via BFS
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    children = defaultdict(list)
    
    queue = deque([root])
    depth[root] = 0
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if depth[v] == -1:  # Not visited
                depth[v] = depth[u] + 1
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # Compute for each node if its subtree contains any target
    contains_target = [False] * (n + 1)
    
    # Mark leaf targets
    for target in targets:
        contains_target[target] = True
    
    # Propagate up the tree
    # Process nodes in reverse topological order (bottom-up)
    # We can do BFS from leaves and move upward
    
    # Count children for each node to simulate topological processing
    child_count = [0] * (n + 1)
    for u in range(1, n+1):
        child_count[u] = len(children[u])
        
    # Start with leaves
    leaf_queue = deque()
    for u in range(1, n+1):
        if child_count[u] == 0 and u != root:
            leaf_queue.append(u)
            
    # Process leaves bottom-up
    processed = [False] * (n + 1)
    topo_order = []
    
    temp_child_count = child_count[:]
    temp_queue = deque([node for node in range(1, n+1) if temp_child_count[node] == 0 and node != root])
    
    while temp_queue:
        u = temp_queue.popleft()
        topo_order.append(u)
        if parent[u] != -1:
            temp_child_count[parent[u]] -= 1
            if temp_child_count[parent[u]] == 0 and parent[u] != root:
                temp_queue.append(parent[u])
                
    # Don't forget the root
    topo_order.append(root)
    
    # Now process in reverse order (bottom-up)
    for u in reversed(topo_order):
        if u == root:
            continue
        p = parent[u]
        if contains_target[u]:
            contains_target[p] = True
    
    # Now traverse down and count edges
    total_cost = 0
    
    # Traverse the tree top-down to check edges
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v, w in children[u]:
            # Edge from u to v
            # Include this edge if both u's component and v's subtree contain targets
            # But we defined contains_target[v] as whether v's subtree contains targets
            # So if contains_target[v] is True, we should include the edge u-v
            # But also u must be part of the solution, which means u's subtree contains targets
            # Wait, contains_target[u] means u's subtree contains targets
            # So if contains_target[v] is True, then this edge should be included
            # But we also need to make sure that by including this edge, we're connecting parts
            # Actually, in the rooted view, if contains_target[v] is True, then we must include
            # the edge from parent[v] to v, which is u to v
            
            if contains_target[v]:  # Subtree of v contains targets, so edge u-v is needed
                total_cost += w
            queue.append(v)
                
    print(total_cost)

if __name__ == "__main__":
    main()
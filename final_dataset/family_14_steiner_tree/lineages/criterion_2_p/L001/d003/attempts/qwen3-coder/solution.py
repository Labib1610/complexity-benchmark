import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    core = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n - 1 and the graph is connected with unique paths,
    # it's a tree.
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one core node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimal subtree (Steiner tree) that connects all core nodes.
    # For a tree, the Steiner tree is the union of all paths between core nodes.
    # This is equivalent to finding the minimal connected subgraph containing all core nodes.
    
    # Approach:
    # 1. Mark all core nodes.
    # 2. Do a BFS/DFS from all core nodes simultaneously to find the minimal subtree.
    # 3. The edges in this subtree are those needed.
    
    # Multi-source BFS to find the minimal subtree containing all core nodes
    visited = [False] * (n + 1)
    queue = deque()
    parent = [-1] * (n + 1)  # To reconstruct the subtree
    
    # Initialize queue with all core nodes
    for c in core:
        queue.append(c)
        visited[c] = True
    
    edge_used = set()
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    # Now, for each node, trace back to a core node to mark edges in the subtree
    visited_edges = [False] * (n + 1)
    queue = deque(core)
    
    for c in core:
        visited_edges[c] = True
        
    total_cost = 0
    edge_dict = {}
    for u, v, w in edges:
        edge_dict[(u, v)] = w
        edge_dict[(v, u)] = w
    
    marked = [False] * (n + 1)
    queue = deque()
    
    # Start from all core nodes
    for c in core:
        queue.append(c)
        marked[c] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not marked[v]:
                marked[v] = True
                total_cost += w
                queue.append(v)
                
    # Wait, this approach counts all edges in the induced subtree.
    # Let me think differently.
    
    # Correct approach:
    # Build a virtual tree (also called a Steiner tree for a subset of nodes in a tree)
    # The cost is the sum of weights of edges in the minimal subtree connecting all core nodes.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node.
    # 2. Compute for each node whether its subtree contains any core node.
    # 3. An edge is in the minimal subtree if both its endpoints' subtrees contain core nodes.
    
    root = 1
    # Build parent relationships via DFS
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    
    def dfs(u, par):
        parent[u] = par
        for v, w in adj[u]:
            if v != par:
                children[u].append((v, w))
                dfs(v, u)
                
    dfs(root, -1)
    
    # For each node, compute if its subtree contains any core node
    contains_core = [False] * (n + 1)
    
    # Leaf to root DP
    def mark_cores(u):
        if u in core:
            contains_core[u] = True
        for v, w in children[u]:
            mark_cores(v)
            if contains_core[v]:
                contains_core[u] = True
                
    mark_cores(root)
    
    # Now traverse edges and count those where both sides have core descendants
    total = 0
    edge_map = {}
    for u, v, w in edges:
        edge_map[(u, v)] = w
        edge_map[(v, u)] = w
    
    def dfs_count(u):
        nonlocal total
        for v, w in children[u]:
            dfs_count(v)
            # If both u's subtree and v's subtree contain cores, we need this edge
            # But actually, if v's subtree contains a core, then the edge (u,v) is needed
            # iff u also needs to be in the final tree, which means u's subtree contains a core
            # and v's subtree contains a core.
            # Actually, simpler: an edge {u,v} is in the Steiner tree if 
            # the removal of the edge splits the tree into two components, each containing at least one core.
            # In a rooted tree, for an edge from parent u to child v:
            # The edge is needed if v's subtree contains at least one core AND 
            # the rest of the tree (including u's other subtrees and u's ancestors) contains at least one core.
            
            # Simpler characterization for trees:
            # Edge {u,v} is in Steiner tree iff 
            # (subtree of v contains a core) AND (rest of tree contains a core).
            # Since the whole tree contains >= 2 cores (unless t=1), 
            # an edge (u,v) where v is child of u is in Steiner tree iff
            # (v's subtree has a core) AND (not all cores are in v's subtree).
            
            if contains_core[v]:  # v's subtree has a core
                # Check if there's a core outside v's subtree
                # It's easier to check if ALL cores are inside v's subtree
                # If not all cores are in v's subtree, then we need this edge
                # But how many cores are in v's subtree?
                # We don't track the count, just presence.
                
                # Actually, since the total number of cores is t > 1,
                # if v's subtree contains some but not all cores, we need the edge.
                # If v's subtree contains all cores, we don't need the edge to u.
                # But we don't know the count.
                
                # Let's recompute: for each subtree, count cores
                total += w
                
    # Recompute with counts
    core_count = [0] * (n + 1)
    
    def count_cores(u):
        if u in core:
            core_count[u] = 1
        for v, w in children[u]:
            count_cores(v)
            core_count[u] += core_count[v]
            
    count_cores(root)
    
    total = 0
    def accumulate_edges(u):
        nonlocal total
        for v, w in children[u]:
            accumulate_edges(v)
            # Edge from u to v is needed if v's subtree has at least 1 core
            # and also has less than t cores (i.e., there exist cores outside)
            if core_count[v] > 0 and core_count[v] < t:
                total += w
                
    accumulate_edges(root)
    
    print(total)

if __name__ == "__main__":
    main()
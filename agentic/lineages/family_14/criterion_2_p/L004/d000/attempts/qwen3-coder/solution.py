import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    flagged = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one flagged node, we need 0 energy
    if t == 1:
        print(0)
        return
    
    # Build the tree
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((w, u, v))
    
    # We need to find the minimal subtree that connects all flagged nodes.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # Approach:
    # 1. Root the tree at some node (e.g., node 1)
    # 2. Do a post-order DFS: for each node, compute whether the subtree contains any flagged node
    # 3. An edge is needed in the solution if both sides of the edge contain at least one flagged node
    
    # Let's root the tree at node 1
    parent = [-1] * (n + 1)
    parent_weight = [-1] * (n + 1)  # weight from node to its parent
    
    # BFS to build parent relationships
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                queue.append(v)
    
    # Now we do a post-order traversal to determine which edges to include
    # We'll use a DFS to mark which subtrees contain flagged nodes
    
    # contains_flagged[i] will be True if subtree rooted at i contains at least one flagged node
    contains_flagged = [False] * (n + 1)
    
    # Get all nodes in post-order (leaves first)
    post_order = []
    visited_dfs = [False] * (n + 1)
    
    def dfs(u):
        visited_dfs[u] = True
        for v, w in adj[u]:
            if not visited_dfs[v]:
                dfs(v)
        post_order.append(u)
    
    dfs(1)
    
    # Now process in post-order to compute contains_flagged
    for u in post_order:
        if u in flagged:
            contains_flagged[u] = True
        for v, w in adj[u]:
            if parent[v] == u:  # v is child of u
                if contains_flagged[v]:
                    contains_flagged[u] = True
    
    # Now count the total cost of edges where both endpoints have contains_flagged = True
    # But we need to be more careful: we want edges that separate flagged components
    # In a tree, an edge is in the minimal Steiner tree if removing it disconnects 
    # the flagged nodes into two non-empty sets.
    
    # So for each edge (u,v), check if the subtree "hanging" from that edge contains flagged nodes,
    # and the rest of the tree also contains flagged nodes.
    
    # Let's recompute this properly:
    # For each node u (except root), consider the edge from u to its parent.
    # The subtree rooted at u is one side, the rest is the other side.
    # Edge (parent[u], u) is needed if both sides contain at least one flagged node.
    
    total_energy = 0
    for u in range(2, n + 1):  # Skip root (node 1)
        p = parent[u]
        w = parent_weight[u]
        
        # Does subtree of u contain flagged?
        subtree_has_flagged = contains_flagged[u]
        
        # Does the complement (rest of tree) contain flagged?
        # We need to check if there's a flagged node NOT in subtree of u
        # Since we're in a tree, if subtree of u has some but not all flagged nodes,
        # then the complement has the rest.
        
        # Total number of flagged nodes in entire tree
        # Number of flagged nodes in subtree of u
        # If both > 0 and < total, then edge is needed
        
        # To make this work, let's count how many flagged nodes are in each subtree
        # We already computed contains_flagged, but we need actual counts
        
        # Let's do another DP: count flagged nodes in each subtree
        count_flagged = [0] * (n + 1)
        visited_count = [False] * (n + 1)
        
        # Collect all nodes in post-order again for counting
        order_for_counting = []
        
        def dfs_count(node):
            visited_count[node] = True
            order_for_counting.append(node)
            for nei, _ in adj[node]:
                if not visited_count[nei] and parent[nei] == node:
                    dfs_count(nei)
                    
        # Rebuild parent structure visitation
        visited_count2 = [False] * (n + 1)
        post_order_count = []
        
        def get_post_order_count(r):
            stack = [r]
            while stack:
                x = stack.pop()
                if not visited_count2[x]:
                    visited_count2[x] = True
                    post_order_count.append(x)
                    for nei, _ in adj[x]:
                        if not visited_count2[nei] and parent[nei] == x:
                            stack.append(nei)
                            
        get_post_order_count(1)
        post_order_count.reverse()  # Now it's actually post-order
                
        # Count flagged nodes in each subtree
        for node in post_order_count:
            if node in flagged:
                count_flagged[node] += 1
            for nei, _ in adj[node]:
                if parent[nei] == node:  # nei is child
                    count_flagged[node] += count_flagged[nei]
        
        total_flagged = count_flagged[1]
        subtree_count = count_flagged[u]
        
        if subtree_count > 0 and (total_flagged - subtree_count) > 0:
            total_energy += w
            
    print(total_energy)

if __name__ == "__main__":
    main()
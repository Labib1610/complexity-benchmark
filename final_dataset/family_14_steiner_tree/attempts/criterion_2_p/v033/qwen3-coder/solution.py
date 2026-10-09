import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    required = list(map(int, sys.stdin.readline().split()))
    
    # If only one required site, cost is 0
    if t <= 1:
        print(0)
        return
    
    required_set = set(required)
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Since the graph is a tree, we can find the minimal subtree that connects all required nodes.
    # This is called the Steiner tree problem on trees, which can be solved efficiently.
    
    # Step 1: Pick any required node as root and do DFS to compute subtree information
    root = required[0]
    
    # We'll do a DFS to mark which nodes are needed in the subtree connecting all required nodes
    # A node is needed if it is required or if it is an ancestor of at least two required nodes
    
    # First, build parent relationships via BFS/DFS from root
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    stack = [root]
    parent[root] = -1
    visited = [False] * (n + 1)
    visited[root] = True
    dfs_order = []
    
    # BFS to establish parent and depth
    queue = deque([root])
    while queue:
        u = queue.popleft()
        dfs_order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Now, for each node, determine if it's required or if it lies on a path between required nodes
    # We can do this by marking all nodes that are on paths between required nodes
    
    # Mark required nodes
    is_required = [False] * (n + 1)
    for r in required:
        is_required[r] = True
    
    # To find the minimal subtree, we can find the union of paths between all pairs,
    # but since it's a tree, we just need the smallest connected subtree containing all required nodes.
    # An efficient way is to find the "meet-in-the-middle" points.
    
    # Better approach:
    # Root the tree at a required node.
    # For each node, count how many required nodes are in its subtree.
    # A node should be included if it has >= 1 required node in its subtree AND is not a required node,
    # OR if it has >= 2 required node subtrees passing through it.
    
    # Let's use a better method:
    # Compute for each node, whether the subtree rooted at that node contains any required node.
    # Then, the minimal connected subtree includes all nodes such that there are at least two
    # required-node-containing branches meeting at that node, or the node itself is required.
    
    # However, there's a simpler linear-time algorithm:
    # 1. Root the tree at any node.
    # 2. Do post-order traversal to compute for each node, the number of required nodes in its subtree.
    # 3. A node is in the minimal subtree if:
    #    - It is required, OR
    #    - It has at least two children whose subtrees contain required nodes.
    
    # Re-root at node 1 for simplicity
    root = 1
    parent = [-1] * (n + 1)
    children = [[] for _ in range(n + 1)]
    
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append((v, w))
                queue.append(v)
    
    # Post-order traversal to compute required count in subtrees
    req_count = [0] * (n + 1)
    # Mark required nodes
    for r in required:
        req_count[r] = 1
    
    # Process in reverse order (post-order)
    for u in reversed(order):
        for v, w in children[u]:
            req_count[u] += req_count[v]
    
    # Now, identify which edges are in the minimal subtree
    # An edge (u,v) where v is child of u is included if req_count[v] > 0 and 
    # either v is required or there are multiple required nodes below v or passing through
    
    # Actually, let's think differently:
    # The minimal subtree connecting all required nodes is the union of paths between all pairs.
    # But in a tree, it's equivalent to finding the smallest connected subgraph containing all required nodes.
    # This is the subtree induced by the required nodes.
    
    # Efficient algorithm:
    # 1. Root the tree at any node.
    # 2. For each node, compute if its subtree contains any required node.
    # 3. Include an edge (parent[v], v) in the solution if v's subtree contains at least one required node
    #    and the rest of the tree (through parent) also contains at least one required node,
    #    OR if v is required and its subtree contains others.
    
    # Simpler and correct approach:
    # Run a DFS from any required node, and find the minimal connected subtree.
    # The cost is the sum of weights of edges in that subtree.
    
    # Even simpler:
    # Since it's a tree, the minimal subtree connecting all required nodes
    # is the union of paths from one required node to all others.
    # But we don't know the topology.
    
    # Best approach:
    # Use the fact that in a tree, the minimal subtree connecting a set of nodes
    # can be found by rooting the tree, computing for each node whether its subtree
    # contains any required node, and including an edge if both endpoints have required nodes
    # in their respective components when the edge is removed.
    
    # Let's implement correctly:
    # 1. Root the tree at node 1.
    # 2. Compute for each node, whether its subtree contains any required node.
    # 3. For each edge, check if removing it separates required nodes.
    
    # But we already did step 1 and 2.
    # Now, for each edge (u,v), with v being child of u,
    # include the edge if:
    # - req_count[v] > 0 (subtree of v contains required nodes) AND
    # - req_count[u] > req_count[v] (the rest of the tree also contains required nodes)
    # OR equivalently, the edge is a bridge between two components each having required nodes.
    
    # Wait, let's re-think.
    # Root at node 1.
    # req_count[v] = number of required nodes in subtree of v.
    # Total required nodes = t.
    # Edge (u,v) where v is child of u is in the minimal subtree iff:
    # req_count[v] > 0 and (t - req_count[v]) > 0
    # i.e., both sides of the edge contain at least one required node.
    
    total_cost = 0
    for u in order:
        for v, w in children[u]:
            # This edge connects subtree of v to the rest of the tree
            if req_count[v] > 0 and (t - req_count[v]) > 0:
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()
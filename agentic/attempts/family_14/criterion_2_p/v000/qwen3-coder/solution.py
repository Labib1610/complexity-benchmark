import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    required = set()
    for _ in range(t):
        required.add(int(data[idx]))
        idx += 1
    
    # If there's only one or zero required node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # We need to find the minimum subtree that connects all required nodes.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # Approach:
    # 1. Root the tree at any node (e.g., node 1)
    # 2. For each node, compute:
    #    - is_required[u]: whether u is required
    #    - has_required_descendant[u]: whether subtree of u contains any required node
    # 3. The minimal connecting edges are those where both endpoints have required descendants,
    #    but removing the edge separates the tree into two components each containing at least one required node.
    
    # Let's do a post-order traversal to mark which nodes have required descendants
    parent = [-1] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # DFS to build parent relationships and determine required descendants
    def dfs(u, par, weight_from_parent):
        parent[u] = par
        parent_edge_weight[u] = weight_from_parent
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                dfs(v, u, w)
    
    dfs(1, -1, 0)
    
    # Now we perform a BFS from all required nodes to find which edges are needed
    # Actually, better approach:
    # Since it's a tree, the minimal subtree connecting all required nodes is unique.
    # It consists of all paths between required nodes.
    # But since it's a tree, we can think of it as keeping only edges that lie on paths between required nodes.
    
    # Efficient way:
    # 1. Mark all required nodes
    # 2. Do a post-order traversal to mark for each node whether its subtree contains a required node
    # 3. An edge should be included if it connects two components each having at least one required node
    
    # Let's reroot and compute for each node if its subtree contains a required node
    has_req = [False] * (n + 1)
    
    # Get all nodes in post-order
    post_order = []
    visited2 = [False] * (n + 1)
    
    def post_dfs(u):
        visited2[u] = True
        for v, w in adj[u]:
            if not visited2[v]:
                post_dfs(v)
        post_order.append(u)
    
    post_dfs(1)
    
    # Mark which nodes are required
    is_req_node = [False] * (n + 1)
    for x in required:
        is_req_node[x] = True
    
    # Propagate required status up the tree
    for u in reversed(post_order):
        has_req[u] = is_req_node[u]
        for v, w in adj[u]:
            if parent[v] == u:  # v is child of u
                has_req[u] = has_req[u] or has_req[v]
    
    # Now count the edges that must be included
    total_cost = 0
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if parent[v] == u:  # Only consider each edge once
                # Edge from u to v (v is child)
                # Include this edge if both u's subtree (including u) and v's subtree have required nodes
                # But we need to be careful about the direction
                # Actually, in the rooted view:
                # Include edge (u,v) if v's subtree has a required node AND there exists a required node outside v's subtree
                if has_req[v] and (has_req[1] and not has_req[v]) != has_req[1]:
                    # Wait, let's reframe:
                    # Include edge (parent[v], v) if both sides of the edge contain at least one required node
                    # Since it's a tree, removing edge (u,v) splits the tree into two components:
                    # One containing v (v's subtree), and one containing the rest
                    # Include the edge if both components have at least one required node
                    p = parent[v]
                    if p != -1:  # Not root
                        # Component with v: has_req[v]
                        # Component without v: has_req[1] XOR has_req[v] ? No, that's not right
                        # Total required = has_req[1] (root has all info)
                        # Component without v's subtree = total - component with v
                        # So check if has_req[v] > 0 and (total_req - has_req[v]) > 0
                        total_req_count = sum(is_req_node)
                        comp_with_v = 0
                        comp_without_v = 0
                        
                        # Recompute counts properly
                        req_count = [0] * (n + 1)
                        
                        # Re-propagate counts
                        for u2 in reversed(post_order):
                            req_count[u2] = 1 if is_req_node[u2] else 0
                            for v2, w2 in adj[u2]:
                                if parent[v2] == u2:
                                    req_count[u2] += req_count[v2]
                        
                        # Now for each edge (parent[v], v), check
                        total_required = req_count[1]
                        if req_count[v] > 0 and (total_required - req_count[v]) > 0:
                            total_cost += w

    # Simpler and correct approach:
    # Rerooting is complex. Let's just do one DFS from an arbitrary node (say 1)
    # and compute for each edge whether it's part of the minimal subtree connecting all required nodes.
    
    req_count = [0] * (n + 1)
    
    # First DFS to compute req_count
    def dfs_count(u, parent_u):
        req_count[u] = 1 if u in required else 0
        for v, w in adj[u]:
            if v != parent_u:
                req_count[u] += dfs_count(v, u)
        return req_count[u]
    
    dfs_count(1, -1)
    
    total_required = req_count[1]
    total_cost = 0
    
    # Second DFS to accumulate edge weights
    def dfs_edges(u, parent_u):
        nonlocal total_cost
        for v, w in adj[u]:
            if v != parent_u:
                # Edge (u, v) with weight w
                # Count of required nodes in v's subtree: req_count[v]
                # Count of required nodes outside v's subtree: total_required - req_count[v]
                if req_count[v] > 0 and (total_required - req_count[v]) > 0:
                    total_cost += w
                dfs_edges(v, u)
    
    dfs_edges(1, -1)
    
    print(total_cost)

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    mandatory = set()
    for _ in range(t):
        mandatory.add(int(data[idx]))
        idx += 1
    
    edges = []
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Since m = n-1 and the whole graph is market-linked (i.e., connected),
    # the graph is a tree.
    
    # We need to find the minimal connected subgraph containing all mandatory nodes.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # Strategy:
    # 1. Root the tree at any node.
    # 2. Find the minimal subtree that contains all mandatory nodes.
    # 3. The cost is the sum of edge weights in this subtree.
    
    # However, there's a simpler way for trees:
    # The minimal connected subgraph containing all mandatory nodes
    # is equivalent to the union of paths between all pairs of mandatory nodes,
    # but more precisely, it's the subtree induced by the mandatory nodes and their connectors.
    
    # Efficient approach for trees:
    # 1. Root the tree at an arbitrary node.
    # 2. Compute the subtree that includes all mandatory nodes.
    # 3. The minimal cost is the sum of all edge weights in this subtree.
    
    # But we don't have to build the actual tree structure.
    # Instead, since it's a tree, we can use the fact that the minimal connected subgraph
    # that spans all mandatory nodes is unique and its total edge weight can be computed
    # by including all edges in the subtree formed by these nodes.
    
    # Even simpler observation:
    # In a tree, the minimal connected subgraph containing all mandatory nodes
    # is the same as the subtree formed by contracting non-mandatory nodes appropriately.
    # But the easiest way is to realize that we want the minimum spanning tree (which is the tree itself)
    # that connects all mandatory nodes. Since the original graph is already a tree,
    # we just need to find the minimal subtree connecting all mandatory nodes.
    
    # For a tree, the minimal subtree containing a set of nodes is called the Steiner tree.
    # On trees, this can be found by:
    # 1. Rooting the tree.
    # 2. Finding the lowest common ancestors and building the minimal subtree.
    
    # But there's an even easier approach here:
    # Since the graph is a tree and we want the minimal connected subgraph containing all mandatory nodes,
    # we can do the following:
    # - Root the tree at some node.
    # - Mark all mandatory nodes as "needed".
    # - Perform a post-order traversal: a node is needed if it is mandatory or if at least one of its children is needed.
    # - Count an edge if it leads to a needed node.
    
    # Let's implement this approach.
    
    # First, let's build adjacency list with edge weights
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If there's only one mandatory node, cost is 0
    if len(mandatory) == 1:
        print(0)
        return
    
    # Root the tree at node 1 (arbitrary)
    root = 1
    parent = {root: None}
    visited = set()
    stack = [root]
    order = []
    
    # DFS to establish parent relationships and traversal order
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nei, w in adj[node]:
            if nei not in visited:
                parent[nei] = node
                stack.append(nei)
    
    # Reverse the order for post-processing
    order.reverse()
    
    # Now, mark which nodes are needed
    # A node is needed if it's mandatory or if any of its descendants are needed
    needed = set(mandatory)
    marked = [False] * (n + 1)  # To avoid re-marking
    
    total_cost = 0
    # Process nodes in reverse order (leaves to root)
    for node in order:
        if node in needed:
            continue
        # Check if any child is needed
        is_needed = False
        for nei, w in adj[node]:
            if parent[nei] == node and marked[nei]:  # nei is a child and is needed
                is_needed = True
                break
        if is_needed:
            needed.add(node)
            marked[node] = True
            # Add the edge from parent to this node if parent exists
            par = parent[node]
            if par is not None:
                # Find the edge weight between par and node
                for nei, w in adj[node]:
                    if nei == par:
                        total_cost += w
                        break
        else:
            marked[node] = False
    
    # Alternatively, let's try a cleaner implementation:
    # Use a different approach: build the subtree by starting from mandatory nodes and going up to root,
    # then take the edges in the resulting subtree.
    
    # Simpler and correct approach:
    # In a tree, the minimal connected subgraph containing mandatory nodes is obtained by:
    # 1. Starting with all mandatory nodes.
    # 2. Adding their parents until reaching a common ancestor or root.
    # 3. The result is a subtree; sum its edge weights.
    
    # But the most straightforward way for trees is:
    # - Root the tree.
    # - Do BFS/DFS to compute parent and depth for each node.
    # - For each mandatory node, mark the path from it to root.
    # - The union of all such paths forms the minimal subtree.
    # - Sum the weights of edges in this subtree.
    
    # Let's implement this correctly.
    
    # Rebuild parent and depth using BFS
    from collections import deque
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
    
    # Now, for each mandatory node, mark the path to root
    marked_edges = set()
    for node in mandatory:
        current = node
        while parent[current] != -1:
            par = parent[current]
            # Add edge (current, par) to marked_edges
            # Normalize edge representation: min, max
            edge_key = tuple(sorted((current, par)))
            marked_edges.add(edge_key)
            current = par
    
    # Now sum the weights of marked edges
    edge_dict = {}
    for w, u, v in edges:
        key = tuple(sorted((u, v)))
        edge_dict[key] = w
    
    total = 0
    for key in marked_edges:
        total += edge_dict[key]
    
    print(total)

if __name__ == "__main__":
    main()
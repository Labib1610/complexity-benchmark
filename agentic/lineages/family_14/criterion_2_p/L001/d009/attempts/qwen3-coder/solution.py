import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n - 1 and the graph is connected, it's a tree
    adj = defaultdict(list)
    edges = []
    edge_weight = {}
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        edge_weight[(u,v)] = w
        edge_weight[(v,u)] = w
    
    # If t == 1, we can just activate that single critical node
    if t == 1:
        print(0)
        return
    
    # We must activate all critical nodes.
    # In a tree, the subgraph induced by the critical nodes and the paths between them
    # forms a subtree. We must activate all nodes on the paths between critical nodes.
    
    # Find the minimal subtree that contains all critical nodes.
    # This is the union of all paths between pairs of critical nodes.
    # But since it's a tree, we can find the "Steiner tree" by taking the union of paths
    # from one critical node to all others.
    
    # Alternatively, we can do a BFS from all critical nodes to find the minimal subtree.
    # The minimal connected subtree containing all critical nodes is the union of all
    # edges on paths between critical nodes.
    
    # A simpler way: find the spanning tree of the critical nodes.
    # In a tree, the minimal connected subgraph containing a set of nodes
    # is the union of the paths between them. The number of edges in this subgraph
    # is (number of nodes in the subgraph) - 1.
    
    # But we need to compute the cost correctly.
    
    # Let's build the "skeleton" tree that connects all critical nodes.
    # We can do BFS/DFS from one critical node to find distances and parents,
    # then for each critical node, we can trace back to find the path to the root.
    # The union of all such paths gives us the minimal subtree.
    
    # But there's a simpler observation:
    # The total net stability is 2.
    # Each activated node contributes 2 and each edge between activated nodes consumes 2 (1 from each end).
    # So total_net = 2 * k - 2 * e, where k is number of activated nodes and e is number of edges between them.
    # We want 2*k - 2*e = 2, so k - e = 1.
    # In a tree, if we have k nodes, the number of edges is k-1.
    # So k - (k-1) = 1. This means any connected subtree satisfies the stability condition.
    
    # Therefore, we just need to find the minimum cost to connect all critical nodes.
    # This is the Minimum Spanning Tree (MST) of the subgraph induced by critical nodes and the paths between them.
    # But since the original graph is a tree, the MST of any subset of nodes is unique and is the 
    # subtree that connects them with minimal total edge weight.
    
    # The minimal cost to connect all critical nodes in a tree is the sum of weights of edges
    # in the minimal subtree containing all critical nodes.
    
    # To find this, we can:
    # 1. Do a BFS from all critical nodes to find which nodes and edges are needed.
    # 2. The required nodes are those on paths between critical nodes.
    # 3. The required edges are those connecting these nodes.
    
    # But there's an even simpler way:
    # In a tree, to connect k nodes, we need exactly k-1 edges.
    # The minimal way to do this is to find the "Steiner tree" which is the union of paths.
    # The cost is the sum of weights of edges in this Steiner tree.
    
    # We can find this by:
    # 1. Rooting the tree at one critical node.
    # 2. For each critical node, find the path to the root.
    # 3. Union all these paths.
    
    # Let's implement this.
    
    # Root the tree at the first critical node
    root = next(iter(critical))
    
    # BFS to compute parent and depth for each node
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    depth[root] = 0
    queue = deque([root])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if depth[v] == -1:  # not visited
                depth[v] = depth[u] + 1
                parent[v] = u
                queue.append(v)
    
    # For each critical node (except root), trace path to root and mark edges
    # We'll store edges in a set to avoid duplicates
    required_edges = set()
    
    for node in critical:
        if node == root:
            continue
        # Trace path from node to root
        current = node
        while current != root:
            p = parent[current]
            # Add edge (current, p) to required_edges
            # Normalize edge representation to avoid duplicates
            edge = tuple(sorted((current, p)))
            required_edges.add(edge)
            current = p
    
    # Calculate total cost
    total_cost = 0
    for u, v in required_edges:
        total_cost += edge_weight[(u, v)]
    
    print(total_cost)

if __name__ == "__main__":
    main()
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
    
    qc_stations = set()
    for _ in range(t):
        qc_stations.add(int(data[idx]))
        idx += 1
    
    # If there's only one QC station, no belts needed
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
    
    # Find the minimum spanning tree that connects all QC stations
    # This is essentially finding the Steiner tree, but since the graph is a tree,
    # we can find the minimal subtree that connects all QC stations.
    
    # Approach:
    # 1. Find all nodes that are on paths between any two QC stations
    # 2. The optimal hub will be a node in this subtree
    # 3. We can compute for each edge, how many QC station pairs use this edge
    # 4. But since it's a tree, there's a unique path between any two nodes
    
    # Better approach:
    # Since the graph is a tree, the minimal subtree connecting all QC stations is unique.
    # We can find all edges that are part of the paths between QC stations.
    # The total cost is the sum of weights of these edges.
    
    # Even better: 
    # Find the "Steiner tree" for the QC stations in a tree.
    # In a tree, the minimal connected subtree containing a set of vertices
    # can be found by taking all vertices on paths between pairs of the terminal vertices.
    
    # Efficient way:
    # 1. Root the tree at any node
    # 2. Find the lowest common ancestors (LCA) to help count edges
    # 3. But there's a simpler way for trees:
    #    - Find the minimal subtree that contains all QC stations
    #    - This can be done by finding all edges that lie on paths between QC stations
    
    # Let's use the fact that in a tree, to connect a set of terminals,
    # we need to include all edges on paths between them.
    # But we don't need to double count.
    
    # Simpler approach:
    # Since it's a tree, we can:
    # 1. Pick any QC station as root
    # 2. Do BFS/DFS to find parent and depth for each node
    # 3. Find the farthest pair of QC stations (diameter of the QC subtree)
    # 4. The optimal hub lies on the path between them
    
    # Even simpler for implementation:
    # The cost is the sum of edge weights in the minimal subtree connecting all QC stations.
    # In a tree, this is equivalent to finding the union of paths between all pairs,
    # but more efficiently.
    
    # Key insight: In a tree, the minimum cost to connect a set of terminals
    # is the total weight of edges in their "Steiner tree".
    # For a tree, the Steiner tree of a set of vertices is the union of paths
    # between them, which can be computed by finding the minimal subtree containing them.
    
    # Algorithm:
    # 1. Root the tree at an arbitrary node
    # 2. Compute parent and depth for each node
    # 3. For each edge, count how many times it's used in paths between QC stations
    # 4. But that's complex. Simpler:
    #    - Find the minimal subtree containing all QC stations
    #    - Its total edge weight is the answer
    
    # Let's implement a clean solution:
    # 1. Root the tree
    # 2. Find for each node its parent and children
    # 3. Mark all nodes that are QC stations
    # 4. Compute for each node if its subtree contains any QC station
    # 5. An edge from parent to child is in the Steiner tree iff the child's subtree
    #    contains at least one QC station and is not all of them
    
    # Root the tree at node 1
    root = 1
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    weight_to_child = {}
    
    # BFS to build rooted tree
    visited = [False] * (n + 1)
    queue = deque([root])
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                weight_to_child[(u, v)] = w
                queue.append(v)
    
    # Count how many QC stations are in each subtree
    qc_count = [0] * (n + 1)
    
    # Post-order traversal to compute qc_count
    def dfs_count(u):
        if u in qc_stations:
            qc_count[u] = 1
        for v in children[u]:
            dfs_count(v)
            qc_count[u] += qc_count[v]
    
    dfs_count(root)
    
    # Now, sum up the weights of edges in the Steiner tree
    total_cost = 0
    # For each node (except root), check if edge to parent is needed
    for u in range(1, n + 1):
        if u != root:
            p = parent[u]
            # Edge from p to u is in Steiner tree if:
            # - u's subtree has at least one QC station, AND
            # - u's subtree doesn't have ALL QC stations
            if qc_count[u] > 0 and qc_count[u] < t:
                total_cost += weight_to_child[(p, u)]
    
    print(total_cost)

if __name__ == "__main__":
    main()
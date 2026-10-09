import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    if t <= 1:
        print(0)
        return
    
    rented = list(map(int, data[3:3+t]))
    rented_set = set(rented)
    
    # Build graph
    graph = defaultdict(list)
    index = 3 + t
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        w = int(data[index+2])
        edges.append((w, u, v))
        graph[u].append((v, w))
        graph[v].append((u, w))
        index += 3
    
    # Sort edges by weight for Kruskal's algorithm
    edges.sort()
    
    # Union-Find data structure for Kruskal's algorithm
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # We need to find the minimal subtree that connects all rented nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Since the graph is a tree, we can find the minimal connected subgraph containing all rented nodes
    # by finding the minimal subtree that spans all rented nodes
    
    # First, we build the tree
    # Then we find the minimal connected subtree containing all rented nodes
    
    # In a tree, the minimal connected subtree spanning a set of nodes
    # is the union of paths between consecutive nodes in some ordering
    # But since it's a tree, we can do better:
    # The solution is to find the minimal subtree that contains all rented nodes
    # This is equivalent to finding the "Steiner tree" in a tree, which can be computed as:
    # Take all nodes that are on paths between any two rented nodes
    
    # Efficient approach:
    # 1. Root the tree at any node
    # 2. Compute DFS to get depths and parents
    # 3. Find the minimal connected subtree containing all rented nodes
    
    # Let's root the tree at node 1
    root = 1
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Compute parent, depth, and subtree information via BFS/DFS
    parent_node = [-1] * (n+1)
    depth = [0] * (n+1)
    visited = [False] * (n+1)
    queue = deque([root])
    visited[root] = True
    parent_node[root] = -1
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent_node[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Function to compute LCA (Lowest Common Ancestor) using binary lifting
    # Preprocessing for LCA
    max_log = 19  # Since n <= 200000
    up = [[-1] * max_log for _ in range(n+1)]
    # Initialize up[v][0] = parent[v]
    for v in range(1, n+1):
        up[v][0] = parent_node[v]
    
    # Fill up table
    for j in range(1, max_log):
        for v in range(1, n+1):
            if up[v][j-1] != -1:
                up[v][j] = up[up[v][j-1]][j-1]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u to the same level as v
        k = depth[u] - depth[v]
        for i in range(max_log):
            if k & (1 << i):
                u = up[u][i]
        if u == v:
            return u
        # Move both up until they meet
        for i in range(max_log-1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]
    
    # Function to compute distance between two nodes
    def distance(u, v):
        l = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[l]
    
    # Now we need to find the minimal connected subtree containing all rented nodes
    # In a tree, this is equivalent to taking the union of paths between all pairs
    # But more efficiently, we can take the union of paths from the first rented node to all others
    
    # However, even simpler: we can use the fact that in a tree, the minimal subtree connecting 
    # a set of nodes is obtained by taking all edges on paths between consecutive nodes in 
    # the sorted order according to their position in a DFS traversal
    
    # Even simpler approach:
    # The cost is the sum of weights of edges in the minimal subtree connecting all rented nodes
    # This is a classic problem solvable by:
    # 1. Rooting the tree
    # 2. Marking all nodes that are ancestors of rented nodes
    # 3. Counting edges in the induced subtree
    
    # Let's implement a clean version:
    # We will use the fact that in a tree, the minimal connected subgraph containing 
    # a set of nodes S is the union of paths between nodes in S.
    # The total weight is the sum of weights of edges in this subgraph.
    
    # Efficient way:
    # 1. Root the tree at any node
    # 2. For each rented node, mark its path to the root
    # 3. The minimal subtree is the union of these paths
    # 4. Its total weight is what we want
    
    # But actually, since it's a tree, we can compute the Steiner tree cost directly:
    # We can sort the rented nodes in the order they appear in a DFS traversal
    # Then connect them consecutively in this order
    
    # Even simpler: 
    # The cost is the sum over all edges of (weight of edge) * (number of rented node pairs 
    # for which this edge lies on the path between them)
    
    # So we compute for each edge how many rented node pairs use it
    
    # To do this efficiently:
    # 1. Root the tree
    # 2. For each node, count how many rented nodes are in its subtree
    # 3. For each edge (u,v) where u is parent of v, the number of rented pairs using this edge 
    #    is count[v] * (t - count[v]) where count[v] is number of rented nodes in subtree of v
    
    # Re-root at node 1 and compute subtree counts
    subtree_count = [0] * (n+1)
    visited = [False] * (n+1)
    
    # Convert rented to a set for fast lookup
    rented_set = set(rented)
    
    # DFS to compute subtree counts
    def dfs_subtree(u, parent):
        count = 1 if u in rented_set else 0
        for v, w in adj[u]:
            if v != parent:
                count += dfs_subtree(v, u)
        subtree_count[u] = count
        return count
    
    dfs_subtree(root, -1)
    
    # Now compute the total cost
    total_cost = 0
    visited_edges = [False] * (n+1)
    
    # Another DFS to accumulate edge contributions
    def dfs_edges(u, parent):
        nonlocal total_cost
        for v, w in adj[u]:
            if v != parent:
                # Edge u-v contributes w * (subtree_count[v]) * (t - subtree_count[v]) to the total cost
                # But wait, this counts each edge in the path between rented nodes
                # Actually, the contribution of an edge to the total cost of connecting all rented nodes
                # is w * (number of rented node pairs that use this edge)
                # Which is w * (nodes_in_one_side) * (nodes_in_other_side)
                # If we direct the edge from u to v (where u is closer to root), then
                # nodes_in_subtree_v and t - nodes_in_subtree_v
                total_cost += w * subtree_count[v] * (t - subtree_count[v])
                dfs_edges(v, u)
    
    dfs_edges(root, -1)
    print(total_cost)

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    R, S, P = map(int, sys.stdin.readline().split())
    mandated = set(map(int, sys.stdin.readline().split()))
    
    # Since S = R - 1 and the graph is connected, it's a tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(S):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one mandated node, cost is 0
    if P == 1:
        print(0)
        return
    
    # Find the minimal subtree that connects all mandated nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Approach:
    # 1. Build a virtual tree (also called auxiliary tree) that contains:
    #    - All mandated nodes
    #    - All their pairwise LCA (Lowest Common Ancestors)
    # 2. The minimal cost is the sum of edge weights in this virtual tree
    
    # But since it's a tree and we want the minimal connected subgraph containing all mandated nodes,
    # we can do the following:
    # - Root the tree at any node
    # - Find the minimal subtree that contains all mandated nodes
    # - This can be done by finding the union of paths between all pairs of mandated nodes
    # - Or more efficiently: find the minimal connected subtree containing all mandated nodes
    
    # Efficient approach:
    # 1. Root the tree at an arbitrary node (e.g., 1)
    # 2. Compute parent and depth for each node using BFS/DFS
    # 3. Implement LCA (Lowest Common Ancestor) algorithm
    # 4. The solution is the sum of distances from each mandated node to the root minus 
    #    twice the sum of distances from each node in the subtree (after contraction) to their parent
    
    # Even simpler approach for a tree:
    # The minimal cost equals the total weight of the edges in the minimal connected subtree
    # that spans all mandated vertices.
    
    # Algorithm:
    # 1. Root the tree arbitrarily
    # 2. For each node, compute if its subtree contains any mandated node
    # 3. An edge from parent to child is included in the solution if the child's subtree 
    #    contains at least one mandated node and is not the entire set of mandated nodes
    
    # Let's implement this
    
    # Root the tree at node 1
    root = 1
    parent = [-1] * (R + 1)
    depth = [-1] * (R + 1)
    children = defaultdict(list)
    edge_weight_to_child = {}
    
    # BFS to build rooted tree
    queue = deque([root])
    depth[root] = 0
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if depth[v] == -1:  # Not visited
                depth[v] = depth[u] + 1
                parent[v] = u
                children[u].append(v)
                edge_weight_to_child[(u, v)] = w
                queue.append(v)
    
    # For each node, compute if its subtree contains any mandated node
    # Also count how many mandated nodes are in each subtree
    contains_mandated = [False] * (R + 1)
    count_mandated = [0] * (R + 1)
    
    # Post-order traversal to compute counts
    def dfs_count(u):
        if u in mandated:
            count_mandated[u] = 1
            contains_mandated[u] = True
        for v in children[u]:
            dfs_count(v)
            count_mandated[u] += count_mandated[v]
            if count_mandated[v] > 0:
                contains_mandated[u] = True
    
    dfs_count(root)
    
    # Now traverse the tree and sum up the weights of edges that connect to subtrees
    # containing at least one but not all mandated nodes
    total_cost = 0
    for u in range(1, R + 1):
        for v in children[u]:
            # Edge from u to v
            # Include this edge in the cost if v's subtree contains some but not all mandated nodes
            c = count_mandated[v]
            if c > 0 and c < P:
                total_cost += edge_weight_to_child[(u, v)]
    
    print(total_cost)

if __name__ == "__main__":
    main()
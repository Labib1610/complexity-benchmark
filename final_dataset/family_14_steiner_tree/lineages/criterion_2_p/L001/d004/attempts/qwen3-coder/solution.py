import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    core = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n - 1 and there's exactly one simple path between any two nodes,
    # the graph is a tree.
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # We need to find a subset of nodes S such that:
    # 1. All core nodes are in S
    # 2. The number of edges in the induced subgraph of S is |S| - 1
    # This means that S must induce a connected subgraph (a subtree)
    
    # The minimum cost subtree that contains all core nodes is what we want.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # For a tree, the minimum Steiner tree can be found by:
    # 1. Start with all core nodes
    # 2. For each core node, mark it
    # 3. Do a BFS/DFS from all core nodes simultaneously to find the minimal subtree
    #    that connects all of them
    
    # But there's a simpler way for trees:
    # The cost of the minimal Steiner tree is the sum of weights of edges
    # in the subtree formed by the core nodes and their connecting paths.
    
    # Another approach:
    # Root the tree at any node. For each node, compute:
    # - whether the subtree rooted at this node contains any core node
    # - the minimum cost to connect all core nodes in this subtree
    
    # Let's root the tree at node 1
    root = 1
    
    # First, build the tree structure with parent relationships
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}
    
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
                edge_weight[(u, v)] = w
                edge_weight[(v, u)] = w
                queue.append(v)
    
    # Now, for each node, determine if its subtree contains any core node
    contains_core = [False] * (n + 1)
    
    # Initialize leaves
    for i in range(1, n + 1):
        if i in core:
            contains_core[i] = True
    
    # Post-order traversal to compute contains_core
    def post_order(node):
        for child in children[node]:
            post_order(child)
            if contains_core[child]:
                contains_core[node] = True
    
    post_order(root)
    
    # Now, traverse the tree and sum up the weights of edges that connect
    # parts of the tree that contain core nodes
    
    total_cost = 0
    
    def dfs(node):
        nonlocal total_cost
        cost = 0
        for child in children[node]:
            dfs(child)
            # If both node and child's subtree contain core nodes,
            # we must include the edge between them
            if contains_core[node] and contains_core[child]:
                total_cost += edge_weight[(node, child)]
    
    dfs(root)
    
    print(total_cost)

if __name__ == "__main__":
    main()
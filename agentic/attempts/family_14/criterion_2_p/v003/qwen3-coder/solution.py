import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, t = map(int, sys.stdin.readline().split())
    required = list(map(int, sys.stdin.readline().split()))
    
    # If there's only one required site, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the tree
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Convert required list to a set for fast lookup
    required_set = set(required)
    
    # Find the shortest paths between all pairs of required nodes
    # We'll do this by running BFS/DFS from each required node and tracking distances
    
    # But since it's a tree, we can find the minimal subtree that connects all required nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Approach:
    # 1. Find all leaves that are not required and remove them iteratively
    # 2. The remaining tree will be the minimal subtree connecting all required nodes
    
    # Actually, better approach:
    # Since it's a tree, the minimal subtree connecting all required nodes is unique
    # We can find it by:
    # 1. Starting from all required nodes
    # 2. Doing a multi-source BFS to find the minimal subtree
    # 3. The edges in this subtree are exactly what we need
    
    # Even simpler approach:
    # Find the "Steiner tree" in a tree:
    # 1. Root the tree at any node
    # 2. For each node, compute if its subtree contains any required node
    # 3. An edge is in the minimal subtree if it connects two subtrees that both contain required nodes
    
    # Let's root the tree at node 1
    root = 1
    
    # Build parent relationships and children lists via DFS
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_cost = {}  # edge_cost[(u,v)] = cost where u is parent of v
    
    def dfs(u, par):
        parent[u] = par
        for v, w in adj[u]:
            if v != par:
                children[u].append(v)
                edge_cost[(u, v)] = w
                edge_cost[(v, u)] = w
                dfs(v, u)
    
    dfs(root, -1)
    
    # For each node, determine if its subtree contains any required node
    contains_required = [False] * (n + 1)
    
    # Mark leaves and propagate up
    def mark_required(u):
        if u in required_set:
            contains_required[u] = True
        for v in children[u]:
            mark_required(v)
            if contains_required[v]:
                contains_required[u] = True
    
    mark_required(root)
    
    # Now collect all edges that must be included
    # An edge (parent[v], v) is needed if v's subtree contains at least one required node
    # and there's another required node outside v's subtree
    total_cost = 0
    
    def calculate_cost(u):
        nonlocal total_cost
        for v in children[u]:
            if contains_required[v]:
                total_cost += edge_cost[(u, v)]
                calculate_cost(v)
    
    calculate_cost(root)
    
    print(total_cost)

if __name__ == "__main__":
    main()
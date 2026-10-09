import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    primary = list(map(int, sys.stdin.readline().split()))
    
    # Build adjacency list with weights
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Convert primary list to a set for fast lookup
    primary_set = set(primary)
    
    # BFS from all primary nodes to compute distances
    # We'll do multi-source BFS
    dist = [float('inf')] * (n + 1)
    queue = deque()
    for p in primary:
        dist[p] = 0
        queue.append(p)
    
    while queue:
        u = queue.popleft()
        d = dist[u]
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                queue.append(v)
    
    # Now, for each edge, check if both endpoints are within distance from primary
    # But actually, we want to find the minimal subtree that includes all primary nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # In a tree, the minimal connected subgraph containing all primary nodes
    # can be found by taking all nodes that lie on paths between primary nodes
    
    # An easier approach: since it's a tree, we can find the "subtree" that connects all primary nodes
    # by marking all nodes that are on some path between two primary nodes
    
    # But even simpler: we can use the fact that in the optimal solution,
    # the set of activated nodes forms a connected subtree containing all primary nodes
    
    # The cost is sum of weights of edges in this subtree
    
    # To find this, we can do the following:
    # 1. Root the tree at some node
    # 2. For each node, compute if its subtree contains any primary node
    # 3. An edge is included if both its endpoints' subtrees contain primary nodes
    
    # Let's root the tree at node 1
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    edge_weight = {}
    
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    
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
    
    # Now compute for each node if its subtree contains a primary node
    contains_primary = [False] * (n + 1)
    
    # Leaf to root pass
    # Get all nodes in post-order
    post_order = []
    visited = [False] * (n + 1)
    stack = [1]
    
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            post_order.append(u)
            for v in children[u]:
                if not visited[v]:
                    stack.append(v)
    
    # Process in reverse order (leaf to root)
    for u in reversed(post_order):
        if u in primary_set:
            contains_primary[u] = True
        for v in children[u]:
            if contains_primary[v]:
                contains_primary[u] = True
    
    # Now count the cost: include an edge if both endpoints' subtrees contain primary
    total_cost = 0
    for u in range(1, n + 1):
        for v in children[u]:
            # Edge u-v is included if both u's and v's "downward" subtrees contain primary
            # But we computed contains_primary as subtree including descendants
            # So if both u and v have contains_primary True, and the edge connects them,
            # then this edge is on the path between some primary nodes
            if contains_primary[u] and contains_primary[v]:
                total_cost += edge_weight[(u, v)]
    
    print(total_cost)

if __name__ == "__main__":
    main()
import sys
from itertools import combinations

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find_root(parent, x)
    root_y = find_root(parent, y)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

def kruskal(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst_weight = 0
    for w, u, v in sorted(edges):
        if union(parent, rank, u, v):
            mst_weight += w
    return mst_weight

def connected_components(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    for w, u, v in edges:
        union(parent, rank, u, v)
    
    components = {}
    for i in range(1, n + 1):
        root = find_root(parent, i)
        if root not in components:
            components[root] = []
        components[root].append(i)
    
    return list(components.values())

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    constraints = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        constraints.append((w, u, v))
    
    # If we have only one target, the projection is always 1-dimensional
    if t <= 1:
        print(0)
        return
    
    # Try all possible ways to make the target variables connected
    min_cost = float('inf')
    
    # Generate all possible subsets of constraints
    # But we use a more efficient approach:
    # We want the target variables to be in the same connected component
    # So we try to connect them with minimal cost
    
    # For each possible way of connecting target nodes,
    # we find the minimum spanning tree that includes these connections
    
    # Actually, let's think differently:
    # We want the projection onto target axes to be 1-dimensional
    # This means all target variables must be equal in the solution space
    # So they must be in the same connected component
    
    # We can try all possible partitions of target nodes and find the minimum cost
    # to make each group connected, but that's complex
    
    # Better approach:
    # The projection has dimension 1 iff all target variables are forced to be equal
    # This happens when all target variables are in the same connected component
    # in the constraint graph
    
    # So we need to find the minimum cost to connect all target vertices
    
    # This is the Steiner tree problem, which is NP-hard
    # But since t <= 10, we can try all possible ways to connect the targets
    
    # Actually, it's simpler - we just need to make the target variables connected
    # Minimum cost to make a set of vertices connected is the MST cost of 
    # the subgraph induced by these vertices plus possibly some connecting edges
    
    # But there's an easier way:
    # Try all 2^(m) subsets of constraints? No, too large.
    
    # Let's think of it as: we want to make all targets in one component
    # Minimum way to do this is to find the minimum cost to connect them
    
    # Use dynamic programming on subsets?
    # dp[mask] = minimum cost to connect targets in mask
    
    # Or even simpler: since t <= 10, we can try all possible graphs on targets
    # and see what's the minimum cost to achieve connectivity
    
    # Even simpler approach:
    # Try all possible ways to make targets connected using Union-Find
    # and find the minimum cost subset of edges
    
    # Brute force approach for small t:
    # Enumerate all subsets of constraints and check if targets are connected
    # But m can be up to n*(n-1)/2 = 4950, so 2^m is too large
    
    # Key insight: we only care about connecting the target vertices
    # So we can build a complete graph on target vertices where edge weights
    # are the shortest path distances in the original graph
    
    # First, compute all-pairs shortest paths in the constraint graph
    # Then find the MST of the target vertices with these distances
    
    # Floyd-Warshall for all pairs shortest paths
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    edges_list = []
    for w, u, v in constraints:
        if dist[u][v] > w:
            dist[u][v] = w
            dist[v][u] = w
        edges_list.append((w, u, v))
    
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now we have shortest distances between all pairs
    # We want to connect all targets with minimum cost
    # This is MST on the complete graph formed by targets
    
    target_edges = []
    for i in range(len(targets)):
        for j in range(i + 1, len(targets)):
            u, v = targets[i], targets[j]
            target_edges.append((dist[u][v], u, v))
    
    # Find MST of target vertices
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst_cost = 0
    edge_count = 0
    
    target_edges.sort()
    for w, u, v in target_edges:
        if w == INF:
            continue
        if union(parent, rank, u, v):
            mst_cost += w
            edge_count += 1
            if edge_count == len(targets) - 1:
                break
    
    print(mst_cost)

solve()
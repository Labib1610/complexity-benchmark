import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def kruskal(n, edges, nodes):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    core = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # For each subset of core nodes, compute the MST cost to connect them
    # We use a bitmask approach for subsets of core nodes
    INF = float('inf')
    dp = {}
    
    # Precompute pairwise distances between core nodes using Dijkstra/Floyd or MST
    # But since we want to connect all core nodes optimally, we'll use a different approach
    
    # Generate all possible spanning trees for core nodes and find minimum
    # Actually, better approach: Steiner tree approximation or enumeration for small t
    
    # Since t <= 10, we can enumerate all possible subsets of core nodes
    # and compute the minimum cost to connect each subset
    
    # But even simpler for this constraint: try all 2^t subsets and compute MST
    # However, that's still complex. Let's think differently.
    
    # Best approach: since t is small (<=10), we can:
    # 1. Find the complete graph on core nodes with shortest path weights
    # 2. Find the minimum spanning tree of this complete graph
    
    # First, compute all-pairs shortest paths between core nodes
    # Initialize distance matrix
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall to get all-pairs shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now create a complete graph on core nodes with shortest path weights
    core_list = list(core)
    core_edges = []
    
    for i in range(len(core_list)):
        for j in range(i + 1, len(core_list)):
            u, v = core_list[i], core_list[j]
            core_edges.append((u, v, dist[u][v]))
    
    # Now find the MST of this complete graph on core nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    core_edges.sort(key=lambda x: x[2])
    
    for u, v, w in core_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
    
    print(cost)

solve()
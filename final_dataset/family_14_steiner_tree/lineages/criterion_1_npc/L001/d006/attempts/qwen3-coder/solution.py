import sys
import heapq
from collections import defaultdict

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

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # We need to connect all target nodes with minimum cost
    # This is essentially a Steiner tree problem, but since t is small (<= 10),
    # we can use dynamic programming with bitmasks
    
    # First, let's build a graph with all nodes and edges
    adj = [[] for _ in range(n + 1)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Compute shortest paths between all pairs of nodes using Dijkstra
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
        pq = [(0, i)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                if dist[i][v] > dist[i][u] + w:
                    dist[i][v] = dist[i][u] + w
                    heapq.heappush(pq, (dist[i][v], v))
    
    # Now we have the shortest distances between any two nodes
    # We need to find the minimum cost to connect all target nodes
    # Since t <= 10, we can use bitmask DP
    
    # Create a complete graph on target nodes with edge weights as shortest paths
    target_indices = {targets[i]: i for i in range(len(targets))}
    k = len(targets)
    
    # dp[mask] = minimum cost to connect nodes in the mask
    dp = [float('inf')] * (1 << k)
    dp[0] = 0
    
    # Initialize: for each pair of targets, we can connect them directly
    for i in range(k):
        for j in range(i + 1, k):
            u, v = targets[i], targets[j]
            dp[(1 << i) | (1 << j)] = min(dp[(1 << i) | (1 << j)], dist[u][v])
    
    # For each subset of targets, try to merge smaller subsets
    for mask in range(1 << k):
        if dp[mask] == float('inf'):
            continue
        for i in range(k):
            if not (mask & (1 << i)):  # i is not in current mask
                new_mask = mask | (1 << i)
                # Try connecting i to any node already in mask
                for j in range(k):
                    if mask & (1 << j):  # j is in current mask
                        u, v = targets[i], targets[j]
                        dp[new_mask] = min(dp[new_mask], dp[mask] + dist[u][v])
        
        # Also try combining two disjoint subsets
        submask = mask
        while submask > 0:
            if dp[submask] != float('inf') and dp[mask ^ submask] != float('inf'):
                dp[mask] = min(dp[mask], dp[submask] + dp[mask ^ submask])
            submask = (submask - 1) & mask
    
    print(dp[(1 << k) - 1])

solve()
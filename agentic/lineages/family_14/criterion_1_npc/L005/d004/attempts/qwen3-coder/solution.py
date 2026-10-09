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

def kruskal(n, edges, must_connect):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    
    # First, connect all required nodes
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            must_connect.discard(find(parent, u))
            must_connect.discard(find(parent, v))
            if len(must_connect) <= 1:
                break
                
    # Then add remaining edges for MST
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    key_assets = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        return 0
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    # Try all possible ways to connect the key assets
    min_cost = float('inf')
    
    # We use a different approach: bitmask DP
    # But since t <= 10, we can try all possible ways to connect them
    
    # Actually, let's think differently:
    # Since we want to connect all key assets, we can treat this as finding 
    # the minimum cost to make all key assets connected.
    # This is essentially a Steiner tree problem, but we can solve it with enumeration
    # since t <= 10.
    
    # Let's use a simpler approach:
    # Try all 2^t subsets of key assets and compute minimum spanning tree cost
    # to connect each subset. Then use dynamic programming.
    
    # But even simpler - since t is small, we can check all possible partitions
    # of the key assets and find the minimum cost to connect them.
    
    # Even simpler approach: 
    # Use the fact that we just need to connect all key assets.
    # So we can run Kruskal's algorithm but prioritize connecting key assets.
    
    # Best approach: bitmask DP
    INF = float('inf')
    dp = [INF] * (1 << t)
    dp[0] = 0
    
    # Precompute cost for connecting any subset of key assets
    # But this is complex. Let's use another approach.
    
    # Simplest working approach:
    # Since t <= 10, we can enumerate all possible ways to connect the key assets.
    # But let's think of it as: we want to find minimum cost to make all key assets
    # belong to the same component.
    
    # We'll use the following approach:
    # Try all possible "roots" among key assets.
    # For each root, compute minimum cost to connect all other key assets to it.
    # This becomes a shortest path problem.
    
    # Actually, let's model this properly:
    # We want to find minimum cost to make all key assets connected.
    # This is minimum spanning tree on the key assets (and possibly some others).
    
    # Let's use the following algorithm:
    # 1. Create a complete graph on key assets where edge weights are shortest path distances
    # 2. Find MST of this complete graph
    # 3. The total cost is the sum of these shortest paths
    
    # But we don't need the complete graph. We can do better.
    
    # Simpler and correct approach:
    # Use subset DP with bitmasks.
    
    # State: dp[mask] = minimum cost to connect key assets indicated by mask
    # Transition: for each subset S of mask, dp[mask] = min(dp[S] + dp[mask\S] + cost to connect)
    
    # Even simpler working solution:
    # Since we're looking for minimum cost to make all key assets connected,
    # we can use the fact that this is equivalent to finding the minimum cost
    # to make all key assets in the same connected component.
    
    # Let's reduce to: find minimum cost so that all key assets are connected.
    # This is a Steiner tree problem but with small t.
    
    # Approach: 
    # 1. For each pair of key assets, compute shortest path distance between them
    # 2. Create a complete graph on key assets with these distances
    # 3. Find MST of this graph
    
    from heapq import heappush, heappop
    from collections import defaultdict
    
    # Build adjacency list
    adj = defaultdict(list)
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Function to compute shortest distance between two nodes
    def dijkstra(start, end):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heappop(pq)
            if u == end:
                return d
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        return dist[end]
    
    # Compute all-pairs shortest paths among key assets
    # But we only need pairwise distances between key assets
    k = len(key_assets)
    if k <= 1:
        return 0
        
    # Create complete graph on key assets
    key_edges = []
    for i in range(k):
        for j in range(i + 1, k):
            u, v = key_assets[i], key_assets[j]
            dist = dijkstra(u, v)
            if dist < float('inf'):
                key_edges.append((dist, i, j))
    
    # Now find MST of key_edges
    key_edges.sort()
    parent = list(range(k))
    rank = [0] * k
    cost = 0
    edges_used = 0
    
    for w, u, v in key_edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            cost += w
            edges_used += 1
            # Union
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            if edges_used == k - 1:
                break
    
    return cost

print(solve())
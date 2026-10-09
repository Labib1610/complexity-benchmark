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

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    edges.sort()
    cost = 0
    for w, u, v in edges:
        if union(parent, rank, u, v):
            cost += w
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))  # Convert to 0-indexed
    
    # For each subset of priority nodes, find the minimum spanning tree cost
    # We use bitmask to represent subsets
    INF = float('inf')
    dp = [INF] * (1 << t)
    dp[0] = 0
    
    # Precompute cost for each subset of priorities
    subset_cost = {}
    for mask in range(1 << t):
        if bin(mask).count('1') <= 1:
            subset_cost[mask] = 0
            continue
            
        # Collect nodes in this subset
        nodes = set()
        for i in range(t):
            if mask & (1 << i):
                nodes.add(priorities[i] - 1)  # Convert to 0-indexed
                
        # Find MST cost for this subset
        parent = list(range(n))
        rank = [0] * n
        edges_sorted = sorted(edges)
        cost = 0
        connected_components = len(nodes)
        
        for w, u, v in edges_sorted:
            if (u in nodes or v in nodes) and union(parent, rank, u, v):
                cost += w
                connected_components -= 1
                if connected_components == 1:
                    break
                    
        subset_cost[mask] = cost if connected_components == 1 else INF
    
    # DP to find minimum cost to connect all priorities
    for mask in range(1 << t):
        if dp[mask] == INF:
            continue
        # Try adding each subset
        for submask in range(1 << t):
            if submask & mask != 0:  # Not disjoint
                continue
            new_mask = mask | submask
            dp[new_mask] = min(dp[new_mask], dp[mask] + subset_cost[submask])
    
    print(dp[(1 << t) - 1])

solve()
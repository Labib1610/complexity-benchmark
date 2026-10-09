import sys
import heapq
from collections import defaultdict

def find_mst_cost(n, edges, mandatory_hubs):
    # If there's only one mandatory hub, no connections needed
    if len(mandatory_hubs) <= 1:
        return 0
    
    # Create a graph with only mandatory hubs as nodes
    # We need to find shortest paths between all pairs of mandatory hubs
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize distances
    for i in range(n):
        dist[i][i] = 0
    
    # Fill in direct edge weights
    for u, v, w in edges:
        dist[u-1][v-1] = min(dist[u-1][v-1], w)
        dist[v-1][u-1] = min(dist[v-1][u-1], w)
    
    # Floyd-Warshall to find all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Create a complete graph of mandatory hubs with shortest path weights
    mandatory_indices = [hub - 1 for hub in mandatory_hubs]
    hub_count = len(mandatory_indices)
    
    # Create edges between all pairs of mandatory hubs with their shortest path costs
    hub_edges = []
    for i in range(hub_count):
        for j in range(i + 1, hub_count):
            u_idx = mandatory_indices[i]
            v_idx = mandatory_indices[j]
            weight = dist[u_idx][v_idx]
            if weight < float('inf'):
                hub_edges.append((i, j, weight))
    
    # Now find MST of this complete graph of mandatory hubs
    # Using Kruskal's algorithm
    hub_edges.sort(key=lambda x: x[2])
    
    # Union-Find data structure
    parent = list(range(hub_count))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Kruskal's algorithm
    total_cost = 0
    edges_used = 0
    
    for u, v, w in hub_edges:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == hub_count - 1:
                break
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

mandatory_hubs = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and output
result = find_mst_cost(n, edges, mandatory_hubs)
print(result)
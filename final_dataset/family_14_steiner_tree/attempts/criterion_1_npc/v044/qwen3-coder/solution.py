import sys
import heapq
from itertools import combinations

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    core_stations = list(map(int, data[idx:idx + t]))
    idx += t
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # If there's 0 or 1 core station, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Precompute shortest distances from each core station to all other stations
    dist_from_core = {}
    for core in core_stations:
        dist_from_core[core] = dijkstra(graph, core, n)
    
    # Also compute shortest distances from each station to all core stations
    # This will help us when we consider auxiliary stations as intermediate points
    all_distances = {}
    for i in range(1, n + 1):
        all_distances[i] = dijkstra(graph, i, n)
    
    # For t <= 10, we can try all subsets of stations as intermediate points
    # But a better approach is to use the fact that the optimal solution 
    # is a Steiner tree, which is a tree connecting all core stations with
    # possible auxiliary stations as internal nodes.
    
    # We'll use a dynamic programming approach with bitmasks
    # dp[mask][i] = minimum cost to connect the core stations in 'mask' with root at core station 'i'
    
    # But since t <= 10, we can also consider all possible combinations
    
    # Let's use a different approach:
    # Since t is small (<=10), we can consider all possible subsets of stations
    # and find the minimum spanning tree that connects all core stations
    
    # Actually, let's think differently:
    # Build a complete graph where the weight between two core stations 
    # is the shortest path distance between them in the original graph
    # Then find the MST of this complete graph
    
    # Number of core stations
    k = t
    if k <= 1:
        print(0)
        return
    
    # Create a complete graph on core stations with shortest path weights
    # edges will be stored as (weight, u, v)
    edges = []
    
    for i in range(k):
        for j in range(i + 1, k):
            u = core_stations[i]
            v = core_stations[j]
            # Shortest path distance between u and v
            dist = dist_from_core[u][v]
            edges.append((dist, i, j))
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find for Kruskal's algorithm
    parent = list(range(k))
    
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
    
    # Kruskal's algorithm to find MST
    total_cost = 0
    edge_count = 0
    
    for weight, u, v in edges:
        if union(u, v):
            total_cost += weight
            edge_count += 1
            if edge_count == k - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
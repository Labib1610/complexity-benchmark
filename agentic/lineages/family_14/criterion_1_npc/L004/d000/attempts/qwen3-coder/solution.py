import sys
import heapq
from collections import defaultdict

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
    n, m, t = map(int, sys.stdin.readline().split())
    core_sites = list(map(int, sys.stdin.readline().split()))
    
    # If there's only one core site, no connection is needed
    if t <= 1:
        print(0)
        return
    
    # Build the graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths between all pairs of core sites
    # We'll create a complete graph on core sites with edge weights as shortest paths
    core_graph = []
    
    for i in range(t):
        dist = dijkstra(graph, core_sites[i], n)
        for j in range(i + 1, t):
            core_graph.append((core_sites[i], core_sites[j], dist[core_sites[j]]))
    
    # Now we need to find MST of this complete graph on core sites
    # Sort edges by weight
    core_graph.sort(key=lambda x: x[2])
    
    # Union-Find for Kruskal's algorithm
    parent = list(range(n + 1))
    
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
    
    for u, v, w in core_graph:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
                
    print(total_cost)

if __name__ == "__main__":
    main()
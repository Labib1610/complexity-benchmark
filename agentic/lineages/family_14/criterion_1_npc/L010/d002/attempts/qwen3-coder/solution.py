import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, nodes):
    dist = {node: float('inf') for node in nodes}
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
    priorities = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    # Compute shortest paths between all pairs of priority nodes
    # We'll use a modified approach: run Dijkstra from each priority node
    distances = {}
    all_nodes = set(range(1, n+1))
    
    for p in priorities:
        distances[p] = dijkstra(graph, p, all_nodes)
    
    # Create a complete graph of priority nodes with edge weights as shortest paths
    priority_graph = []
    for i in range(t):
        for j in range(i+1, t):
            u, v = priorities[i], priorities[j]
            weight = distances[u][v]
            priority_graph.append((weight, u, v))
    
    # Apply Kruskal's algorithm to find MST of priority nodes
    priority_graph.sort()
    
    parent = {p: p for p in priorities}
    
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
    
    total_cost = 0
    edges_used = 0
    
    for weight, u, v in priority_graph:
        if union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == t - 1:
                break
                
    print(total_cost)

if __name__ == "__main__":
    main()
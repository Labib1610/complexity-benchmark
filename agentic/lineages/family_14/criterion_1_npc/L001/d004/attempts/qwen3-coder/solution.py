import sys
from itertools import combinations
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == end:
            return current_distance
            
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances[end]

def find_mst_cost(graph, nodes):
    if len(nodes) <= 1:
        return 0
        
    # Create a complete graph with shortest paths between critical nodes
    n = len(nodes)
    edges = []
    
    # Calculate shortest paths between all pairs of critical nodes
    for i in range(n):
        for j in range(i+1, n):
            u, v = nodes[i], nodes[j]
            cost = dijkstra(graph, u, v)
            edges.append((cost, i, j))
    
    # Kruskal's algorithm for MST
    edges.sort()
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        parent[px] = py
    
    total_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost
            
    return total_cost

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    # Build graph
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Find minimum cost to connect all critical nodes
    result = find_mst_cost(graph, critical)
    print(result)

if __name__ == "__main__":
    main()
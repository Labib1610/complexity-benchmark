import sys
import heapq
from collections import defaultdict

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

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    anchors = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph of anchor nodes with shortest paths as edge weights
    anchor_graph = []
    for i in range(t):
        for j in range(i+1, t):
            anchor1, anchor2 = anchors[i], anchors[j]
            distance = dijkstra(graph, anchor1, anchor2)
            anchor_graph.append((distance, anchor1, anchor2))
    
    # Kruskal's algorithm to find MST of anchor graph
    anchor_graph.sort()
    
    parent = {anchor: anchor for anchor in anchors}
    
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
    
    for weight, u, v in anchor_graph:
        if union(u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
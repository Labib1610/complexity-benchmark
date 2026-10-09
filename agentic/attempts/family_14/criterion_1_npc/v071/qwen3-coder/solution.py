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

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    core_nodes = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Create a complete graph of core nodes with shortest path distances
    core_graph = []
    node_set = set(range(1, n+1))
    
    for i, core_u in enumerate(core_nodes):
        distances = dijkstra(graph, core_u, node_set)
        for j in range(i+1, len(core_nodes)):
            core_v = core_nodes[j]
            core_graph.append((distances[core_v], core_u, core_v))
    
    # Kruskal's algorithm for MST
    core_graph.sort()
    
    parent = {node: node for node in core_nodes}
    
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
    
    for cost, u, v in core_graph:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()
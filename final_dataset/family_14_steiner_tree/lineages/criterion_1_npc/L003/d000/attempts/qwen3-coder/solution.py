import sys
from collections import defaultdict
import heapq

def dijkstra(graph, start, nodes):
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > distances[u]:
            continue
            
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
                
    return distances

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    core_components = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths from each core component to all other nodes
    distances = {}
    all_nodes = set(range(1, n+1))
    
    for core in core_components:
        distances[core] = dijkstra(graph, core, all_nodes)
    
    # Build a complete graph among core components with shortest path weights
    core_graph = []
    for i in range(t):
        for j in range(i+1, t):
            u = core_components[i]
            v = core_components[j]
            # Find shortest path between u and v
            weight = distances[u][v]
            core_graph.append((weight, u, v))
    
    # Now we need to find MST of this complete graph on core components
    # Using Kruskal's algorithm
    
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
    
    # Sort edges by weight
    core_graph.sort()
    
    parent = {c: c for c in core_components}
    rank = {c: 0 for c in core_components}
    
    total_cost = 0
    edges_used = 0
    
    for weight, u, v in core_graph:
        if union(parent, rank, u, v):
            total_cost += weight
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()
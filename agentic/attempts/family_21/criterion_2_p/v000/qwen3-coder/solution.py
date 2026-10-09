import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    prev = {}
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == end:
            break
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    if dist[end] == float('inf'):
        return None, float('inf')
    
    path = []
    curr = end
    while curr in prev:
        path.append(curr)
        curr = prev[curr]
    path.append(start)
    path.reverse()
    
    return path, dist[end]

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # Find shortest path between s and t
    path, min_cost = dijkstra(graph, s, t)
    
    if min_cost > B:
        print("NO")
        return
    
    # Reconstruct the path edges
    path_edges = set()
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        path_edges.add((min(u, v), max(u, v)))
    
    # Find the minimum cost edge on the path
    min_edge_cost = float('inf')
    min_edge = None
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        for neighbor, weight in graph[u]:
            if neighbor == v:
                if weight < min_edge_cost:
                    min_edge_cost = weight
                    min_edge = (u, v)
                break
    
    # Check if we can remove just this one edge
    if min_edge_cost <= B:
        print("YES")
        print(1)
        print(min_edge[0], min_edge[1])
        return
    
    print("NO")

if __name__ == "__main__":
    main()
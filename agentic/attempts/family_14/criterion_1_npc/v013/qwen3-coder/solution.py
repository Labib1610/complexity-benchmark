import sys
from itertools import combinations
from collections import defaultdict
import heapq

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
    
    required = list(map(int, data[idx:idx+t]))
    idx += t
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Compute shortest paths between all pairs of required nodes
    # We only need distances between required nodes
    distances = {}
    for req in required:
        dist = dijkstra(graph, req, n)
        distances[req] = dist
    
    # Create a complete graph of required nodes with edge weights as shortest path distances
    # Then find the minimum spanning tree of this complete graph
    
    # For small t (<= 10), we can use brute force or Prim's algorithm
    # Let's implement Prim's algorithm for the complete graph on required nodes
    
    # First, compute all pairwise distances
    req_dist = {}
    for i in range(t):
        for j in range(i+1, t):
            u, v = required[i], required[j]
            d = distances[u][v]
            req_dist[(u, v)] = d
            req_dist[(v, u)] = d
    
    # Now solve MST on required nodes
    # Prim's algorithm
    if t == 0:
        print(0)
        return
        
    visited = set()
    visited.add(required[0])
    edges = []
    
    # Initialize with edges from first node
    for i in range(1, t):
        u = required[0]
        v = required[i]
        heapq.heappush(edges, (req_dist[(u, v)], u, v))
    
    total_cost = 0
    while len(visited) < t:
        # Find minimum edge that connects visited to unvisited
        while edges:
            cost, u, v = heapq.heappop(edges)
            if (u in visited) != (v in visited):  # Exactly one is visited
                break
        else:
            # This shouldn't happen given the problem constraints
            break
            
        # Add the unvisited node
        new_node = v if u in visited else u
        visited.add(new_node)
        total_cost += cost
        
        # Add new edges from this node to the heap
        for node in required:
            if node not in visited:
                heapq.heappush(edges, (req_dist[(new_node, node)], new_node, node))
    
    print(total_cost)

if __name__ == "__main__":
    main()
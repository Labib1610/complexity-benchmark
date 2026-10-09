import sys
import heapq
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    priority = set()
    for _ in range(t):
        priority.add(int(data[idx]))
        idx += 1
    
    # If there's only one or zero priority facility, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the graph
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
    
    # Function to compute shortest paths from a source using Dijkstra
    def dijkstra(src):
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    # Compute all-pairs shortest paths among priority nodes
    # We'll create a complete graph on priority nodes with edge weights as shortest paths
    priority_list = list(priority)
    k = len(priority_list)
    
    # Create a new graph with only priority nodes
    new_graph = [[0]*k for _ in range(k)]
    
    # For each priority node, run Dijkstra to get distances to all other nodes
    dists = {}
    for i in range(k):
        src = priority_list[i]
        dists[src] = dijkstra(src)
    
    # Build the complete graph of priority nodes with shortest path weights
    for i in range(k):
        for j in range(i+1, k):
            u = priority_list[i]
            v = priority_list[j]
            new_graph[i][j] = dists[u][v]
            new_graph[j][i] = dists[u][v]
    
    # Now we need to find the minimum spanning tree of this complete graph
    # Using Prim's algorithm
    in_mst = [False] * k
    min_edge = [float('inf')] * k
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(k):
        # Find the vertex with minimum edge weight not yet in MST
        u = -1
        for v in range(k):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        in_mst[u] = True
        total_cost += min_edge[u]
        
        # Update the minimum edge weights to vertices adjacent to u
        for v in range(k):
            if not in_mst[v] and new_graph[u][v] < min_edge[v]:
                min_edge[v] = new_graph[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    main()
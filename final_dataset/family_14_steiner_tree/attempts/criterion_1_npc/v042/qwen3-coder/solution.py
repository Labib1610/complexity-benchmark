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
    
    deposit = set()
    for _ in range(t):
        deposit.add(int(data[idx]) - 1)  # Convert to 0-based indexing
        idx += 1
    
    # If there's only one or zero deposit chamber, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Build the graph
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Function to compute shortest paths from a source node using Dijkstra
    def dijkstra(src):
        dist = [float('inf')] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    # Compute shortest paths from each deposit chamber to all other nodes
    # Only store distances to other deposit chambers
    deposit_list = list(deposit)
    k = len(deposit_list)
    # Create a complete graph among deposit chambers with shortest path weights
    cost_matrix = [[0]*k for _ in range(k)]
    dists = []
    for i in range(k):
        dist = dijkstra(deposit_list[i])
        dists.append(dist)
        for j in range(k):
            if i != j:
                cost_matrix[i][j] = dist[deposit_list[j]]
    
    # Now we need to find the minimum spanning tree of this complete graph
    # Using Prim's algorithm
    if k == 0:
        print(0)
        return
        
    in_mst = [False] * k
    min_edge = [float('inf')] * k
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(k):
        # Find the vertex with minimum edge weight not yet in MST
        u = -1
        for v in range(k):
            if not in_mst[v]:
                if u == -1 or min_edge[v] < min_edge[u]:
                    u = v
        in_mst[u] = True
        total_cost += min_edge[u]
        
        # Update min_edge for vertices adjacent to u
        for v in range(k):
            if not in_mst[v]:
                if cost_matrix[u][v] < min_edge[v]:
                    min_edge[v] = cost_matrix[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    main()
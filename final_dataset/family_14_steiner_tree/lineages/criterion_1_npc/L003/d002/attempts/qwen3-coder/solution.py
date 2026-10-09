import sys
import heapq
from collections import defaultdict
import itertools

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index+1])
    t = int(data[index+2])
    index += 3
    
    priority = list(map(int, data[index:index+t]))
    index += t
    
    # Build graph
    graph = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        w = int(data[index+2])
        index += 3
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # If only one priority node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Function to compute shortest paths from a source
    def dijkstra(src):
        dist = [float('inf')] * (n+1)
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
    # We only care about distances between priority nodes
    k = len(priority)
    # Create a complete graph on priority nodes with edge weights as shortest paths
    dist_matrix = [[0]*k for _ in range(k)]
    dists = {}
    for i in range(k):
        dist_from_i = dijkstra(priority[i])
        dists[priority[i]] = dist_from_i
        for j in range(k):
            dist_matrix[i][j] = dist_from_i[priority[j]]
    
    # Now we have a complete graph on priority nodes with metric distances
    # Find MST of this complete graph using Prim's algorithm
    # But since k<=10, we can use brute-force enumeration of all spanning trees for small k
    # Actually, better to just run MST on the complete graph
    
    # Use Prim's algorithm on the complete graph of priority nodes
    def prim_mst(cost_matrix, nodes):
        if len(nodes) <= 1:
            return 0
        # Nodes are indices in cost_matrix
        in_tree = [False] * len(nodes)
        min_edge = [float('inf')] * len(nodes)
        min_edge[0] = 0
        total_cost = 0
        for _ in range(len(nodes)):
            u = -1
            for v in range(len(nodes)):
                if not in_tree[v] and (u == -1 or min_edge[v] < min_edge[u]):
                    u = v
            in_tree[u] = True
            total_cost += min_edge[u]
            for v in range(len(nodes)):
                if not in_tree[v]:
                    if cost_matrix[u][v] < min_edge[v]:
                        min_edge[v] = cost_matrix[u][v]
        return total_cost
    
    print(prim_mst(dist_matrix, priority))

if __name__ == "__main__":
    main()
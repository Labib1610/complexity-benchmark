import sys
import heapq
from collections import defaultdict
import itertools

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
    
    vital = list(map(int, data[idx:idx+t]))
    idx += t
    vital_set = set(vital)
    
    # If there's only one vital compound, no reactions needed
    if t <= 1:
        print(0)
        return
    
    # Build graph
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
    
    # Precompute shortest paths between all pairs using Dijkstra
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
        pq = [(0, i)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in graph[u]:
                if dist[i][v] > d + w:
                    dist[i][v] = d + w
                    heapq.heappush(pq, (dist[i][v], v))
    
    # Create a complete graph on vital nodes with shortest path weights
    # Then find MST of this graph
    # We'll use Prim's algorithm on the complete graph induced by vital nodes
    # But we compute edge weights on-the-fly using precomputed distances
    
    # Generate all pairs of vital compounds
    vital_pairs = list(itertools.combinations(vital, 2))
    
    # For small t (<=10), we can compute the complete graph and find MST directly
    # Build a graph with only vital nodes, edge weights are shortest paths
    vital_graph = []
    for u, v in vital_pairs:
        w = dist[u][v]
        if w < float('inf'):
            vital_graph.append((w, u, v))
    
    # Sort edges by weight for Kruskal's algorithm
    vital_graph.sort()
    
    # Union-Find for Kruskal's
    parent = {v: v for v in vital}
    rank = {v: 0 for v in vital}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Kruskal's algorithm
    total_burden = 0
    edges_used = 0
    for w, u, v in vital_graph:
        if union(u, v):
            total_burden += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_burden)

if __name__ == "__main__":
    main()
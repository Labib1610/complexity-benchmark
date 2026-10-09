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
    
    if t <= 1:
        print(0)
        return
    
    cameras = list(map(int, data[idx:idx+t]))
    idx += t
    camera_set = set(cameras)
    
    # Build graph
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
    
    # Compute shortest paths from each camera node
    # We'll use Dijkstra's algorithm for each camera
    dist = {}
    for c in cameras:
        dist[c] = {}
        visited = {}
        pq = [(0, c)]
        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited[u] = True
            dist[c][u] = d
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(pq, (d + w, v))
    
    # Create a complete graph among cameras using shortest paths
    # Then find MST of this complete graph
    # But since t<=10, we can compute all pairwise distances and then find MST
    
    # Build complete graph with edge weights as shortest path distances
    edges = []
    for i in range(t):
        for j in range(i+1, t):
            u = cameras[i]
            v = cameras[j]
            # Find shortest path between u and v
            min_dist = float('inf')
            for node in dist[u]:
                if node in dist[v]:
                    min_dist = min(min_dist, dist[u][node] + dist[v][node])
            edges.append((min_dist, u, v))
    
    # Now run Kruskal's algorithm to find MST
    parent = {c: c for c in cameras}
    
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
    
    edges.sort()
    total_cost = 0
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()
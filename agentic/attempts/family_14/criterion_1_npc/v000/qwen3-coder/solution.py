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
    
    required = list(map(int, data[idx:idx+t]))
    idx += t
    required_set = set(required)
    
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
    
    # If there's only one required site, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Compute shortest paths between all pairs of required nodes
    # Using Dijkstra for each required node
    dist = {}
    
    def dijkstra(start):
        d = [float('inf')] * (n + 1)
        d[start] = 0
        pq = [(0, start)]
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > d[u]:
                continue
            for v, w in graph[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(pq, (d[v], v))
        return d
    
    # Build a complete graph on required nodes with shortest path weights
    req_graph = []
    for i in range(t):
        u = required[i]
        d = dijkstra(u)
        for j in range(i+1, t):
            v = required[j]
            req_graph.append((d[v], u, v))
    
    # Sort edges for Kruskal's algorithm
    req_graph.sort()
    
    # Union-Find for Kruskal's
    parent = list(range(n + 1))
    
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
    
    # Kruskal's algorithm to find MST of required nodes
    total_cost = 0
    edges_used = 0
    
    for w, u, v in req_graph:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
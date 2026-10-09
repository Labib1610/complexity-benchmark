import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    primary = [int(next(it)) for _ in range(t)]
    primary_set = set(primary)
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If t <= 1, no edges needed
    if t <= 1:
        print(0)
        return
    
    # Compute all-pairs shortest paths using Dijkstra from each primary node
    INF = float('inf')
    dist = {}
    
    for s in primary:
        d = [INF] * (n + 1)
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                if d[v] > du + w:
                    d[v] = du + w
                    heapq.heappush(pq, (d[v], v))
        dist[s] = d
    
    # Build complete graph on primary nodes with edge weights = shortest path
    # Then find MST of this complete graph
    edges = []
    primary_list = list(primary)
    for i in range(len(primary_list)):
        u = primary_list[i]
        for j in range(i + 1, len(primary_list)):
            v = primary_list[j]
            w = dist[u][v]
            edges.append((w, i, j))
    
    # Kruskal's algorithm
    edges.sort()
    parent = list(range(len(primary_list)))
    rank = [0] * len(primary_list)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    total = 0
    for w, i, j in edges:
        if union(i, j):
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()
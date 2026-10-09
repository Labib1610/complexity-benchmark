import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = [int(next(it)) - 1 for _ in range(t)]
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each critical node
    INF = 10**18
    dist_matrix = []
    for src in critical:
        dist = [INF] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist_matrix.append(dist)
    
    # Build complete graph among critical nodes
    edges = []
    for i in range(t):
        for j in range(i+1, t):
            w = dist_matrix[i][critical[j]]
            edges.append((w, i, j))
    
    # Kruskal MST
    edges.sort()
    parent = list(range(t))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True
    
    total = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()
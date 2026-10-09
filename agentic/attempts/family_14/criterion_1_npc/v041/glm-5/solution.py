import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
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
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each primary node
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i in range(t):
        start = primary[i]
        dist[i][start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[i][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[i][v]:
                    dist[i][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Prim's algorithm on primary nodes
    INF = float('inf')
    min_edge = [INF] * t
    in_mst = [False] * t
    
    # Initialize with node 0
    min_edge[0] = 0
    result = 0
    
    for _ in range(t):
        # Find minimum edge node
        u = -1
        for j in range(t):
            if not in_mst[j] and (u == -1 or min_edge[j] < min_edge[u]):
                u = j
        
        in_mst[u] = True
        result += min_edge[u]
        
        # Update edges
        for v in range(t):
            if not in_mst[v]:
                # Find minimum distance between primary u and v through any node
                d = INF
                for node in range(1, n + 1):
                    d = min(d, dist[u][node] + dist[v][node])
                min_edge[v] = min(min_edge[v], d)
    
    print(result)

if __name__ == "__main__":
    solve()
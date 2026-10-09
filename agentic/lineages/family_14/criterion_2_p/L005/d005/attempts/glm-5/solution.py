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
    
    critical = [False] * (n + 1)
    for _ in range(t):
        critical[int(next(it))] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find centroid of critical nodes using multi-source BFS
    dist = [float('inf')] * (n + 1)
    pq = []
    for v in range(1, n + 1):
        if critical[v]:
            dist[v] = 0
            heapq.heappush(pq, (0, v))
    
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    
    # Find centroid (node with minimum maximum distance to critical nodes)
    centroid = 1
    max_dist = dist[1]
    for v in range(2, n + 1):
        if dist[v] < max_dist:
            max_dist = dist[v]
            centroid = v
    
    # Compute MST cost from centroid to all critical nodes
    mst_dist = [float('inf')] * (n + 1)
    mst_dist[centroid] = 0
    pq = [(0, centroid)]
    total_cost = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        if d != mst_dist[u]:
            continue
        if critical[u]:
            total_cost += d
        for v, w in adj[u]:
            if mst_dist[v] > d + w:
                mst_dist[v] = d + w
                heapq.heappush(pq, (mst_dist[v], v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()
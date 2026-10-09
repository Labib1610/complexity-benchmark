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
    
    targets = set()
    for _ in range(t):
        targets.add(int(next(it)))
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    INF = 10**18
    dist = [INF] * (n + 1)
    pq = []
    
    for node in targets:
        dist[node] = 0
        heapq.heappush(pq, (0, node))
    
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    
    total_price = 0
    for node in targets:
        total_price += dist[node]
    
    print(total_price)

if __name__ == "__main__":
    solve()
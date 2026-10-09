import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        E = int(next(iterator))
        F = int(next(iterator))
    except StopIteration:
        return

    critical = set()
    for _ in range(F):
        critical.add(int(next(iterator))
)
    adj = [[] for _ in range(N + 1)]
    for _ in range(E):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if F <= 1:
        print(0)
        return

    INF = float('inf')
    dist = [INF] * (N + 1)
    pq = []
    
    for node in critical:
        dist[node] = 0
        heapq.heappush(pq, (0, node))
    
    total_cost = 0
    edges_used = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        total_cost += d
        edges_used += 1
        
        if edges_used == F:
            break
            
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    
    print(total_cost)

if __name__ == '__main__':
    solve()
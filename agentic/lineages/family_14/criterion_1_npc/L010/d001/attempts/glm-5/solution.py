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
    
    required = set()
    for _ in range(t):
        required.add(int(next(it)))
    
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
    
    # Prim's algorithm starting from any required node
    start = next(iter(required))
    in_mst = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    min_edge[start] = 0
    pq = [(0, start)]
    
    total_cost = 0
    required_in_mst = 0
    
    while pq and required_in_mst < t:
        cost, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += cost
        if u in required:
            required_in_mst += 1
        
        for v, w in adj[u]:
            if not in_mst[v] and w < min_edge[v]:
                min_edge[v] = w
                heapq.heappush(pq, (w, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()
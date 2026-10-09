import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    target = [int(next(it)) for _ in range(t)]
    
    # Build adjacency list for Prim's algorithm
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
    
    # Prim's algorithm starting from first target variable
    import heapq
    INF = 10**18
    min_edge = [INF] * (n + 1)
    in_mst = [False] * (n + 1)
    
    start = target[0]
    min_edge[start] = 0
    pq = [(0, start)]
    
    total_cost = 0
    mst_size = 0
    
    while pq and mst_size < n:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total_cost += w
        mst_size += 1
        
        for v, weight in adj[u]:
            if not in_mst[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heapq.heappush(pq, (weight, v))
    
    print(total_cost)

if __name__ == "__main__":
    solve()
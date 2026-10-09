import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    target_indices = [int(next(it)) for _ in range(t)]
    
    # Build graph for MST
    # Nodes are 1..n
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
    
    # Prim's algorithm starting from first target index
    start = target_indices[0]
    in_mst = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    min_edge[start] = 0
    pq = [(0, start)]
    mst_cost = 0
    
    while pq:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        mst_cost += w
        for v, weight in adj[u]:
            if not in_mst[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heapq.heappush(pq, (weight, v))
    
    print(mst_cost)

if __name__ == "__main__":
    solve()
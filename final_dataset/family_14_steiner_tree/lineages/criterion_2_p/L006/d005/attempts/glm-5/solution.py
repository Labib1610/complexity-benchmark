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
    
    priority = set()
    for _ in range(t):
        priority.add(int(next(it)))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Special case: t <= 1, no equations needed
    if t <= 1:
        print(0)
        return
    
    # Find the minimum spanning tree using Prim's algorithm
    # Start from node 1
    in_mst = [False] * (n + 1)
    min_edge = [float('inf')] * (n + 1)
    min_edge[1] = 0
    heap = [(0, 1)]
    mst_cost = 0
    
    while heap:
        w, u = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        mst_cost += w
        for v, weight in adj[u]:
            if not in_mst[v] and weight < min_edge[v]:
                min_edge[v] = weight
                heapq.heappush(heap, (weight, v))
    
    print(mst_cost)

if __name__ == "__main__":
    solve()
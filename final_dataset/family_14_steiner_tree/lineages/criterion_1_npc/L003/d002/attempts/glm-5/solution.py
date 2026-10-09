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
    
    priority = set()
    for _ in range(t):
        priority.add(int(next(it)))
    
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
    
    # Compute all-pairs shortest paths among priority nodes
    priority_list = list(priority)
    dist = {}
    
    for start in priority_list:
        d = [float('inf')] * (n + 1)
        d[start] = 0
        pq = [(0, start)]
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d > d[u]:
                continue
            for v, w in adj[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heapq.heappush(pq, (d[v], v))
        dist[start] = d
    
    # Prim's algorithm on priority nodes using virtual edges
    # Virtual edge weight between priority nodes i and j is shortest path from i to j
    first = priority_list[0]
    in_mst = set()
    min_edge = {}
    for p in priority_list:
        min_edge[p] = float('inf')
    min_edge[first] = 0
    total = 0
    
    for _ in range(t):
        # Find minimum edge to add
        best = None
        best_val = float('inf')
        for p in priority_list:
            if p not in in_mst and min_edge[p] < best_val:
                best_val = min_edge[p]
                best = p
        if best is None:
            break
        in_mst.add(best)
        total += best_val
        # Update min_edge for remaining nodes
        for p in priority_list:
            if p not in in_mst:
                d = dist[best][p]
                if d < min_edge[p]:
                    min_edge[p] = d
    
    print(total)

solve()
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
    
    targets = set()
    for _ in range(t):
        targets.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If t <= 1, no edges needed
    if t <= 1:
        print(0)
        return
    
    # Compute pairwise shortest distances between targets
    target_list = list(targets)
    T = len(target_list)
    dist_matrix = [[float('inf')] * T for _ in range(T)]
    
    for i, src in enumerate(target_list):
        # Dijkstra from src
        dist = [float('inf')] * (n + 1)
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
        
        for j, dst in enumerate(target_list):
            dist_matrix[i][j] = dist[dst]
    
    # MST on target nodes using Prim's algorithm
    total_cost = 0
    in_mst = [False] * T
    min_edge = [float('inf')] * T
    min_edge[0] = 0
    
    for _ in range(T):
        # Find minimum edge to add
        u = -1
        for v in range(T):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        in_mst[u] = True
        total_cost += min_edge[u]
        
        # Update edges
        for v in range(T):
            if not in_mst[v] and dist_matrix[u][v] < min_edge[v]:
                min_edge[v] = dist_matrix[u][v]
    
    print(total_cost)

if __name__ == "__main__":
    solve()
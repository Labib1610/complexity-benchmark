import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = set()
    for _ in range(t):
        critical.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each critical node
    dist = {}
    for s in critical:
        d = [float('inf')] * (n + 1)
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                if d[v] > du + w:
                    d[v] = du + w
                    heappush(pq, (d[v], v))
        dist[s] = d
    
    # Prim's algorithm on critical nodes
    # Edge weight between critical nodes i and j is dist[i][j]
    critical_list = list(critical)
    k = len(critical_list)
    
    in_mst = [False] * k
    min_edge = [float('inf')] * k
    min_edge[0] = 0
    total = 0
    
    for _ in range(k):
        # Find minimum edge to add
        u = -1
        for i in range(k):
            if not in_mst[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i
        in_mst[u] = True
        total += min_edge[u]
        
        # Update minimum edges
        node_u = critical_list[u]
        for v in range(k):
            if not in_mst[v]:
                node_v = critical_list[v]
                w = dist[node_u][node_v]
                if w < min_edge[v]:
                    min_edge[v] = w
    
    print(total)

if __name__ == "__main__":
    solve()
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
    
    if t <= 1:
        print(0)
        return
    
    # Compute all-pairs shortest paths between critical nodes
    # Using Dijkstra from each critical node
    INF = 10**18
    # Map critical node to index
    crit_list = list(critical)
    crit_index = {node: i for i, node in enumerate(crit_list)}
    k = len(crit_list)
    
    # dist[i][j] = shortest path from crit_list[i] to crit_list[j]
    dist = [[INF] * k for _ in range(k)]
    
    for i, start in enumerate(crit_list):
        # Dijkstra from start
        d = [INF] * (n + 1)
        d[start] = 0
        pq = [(0, start)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        # Fill distances to other critical nodes
        for j, node in enumerate(crit_list):
            dist[i][j] = d[node]
    
    # Now find MST on the complete graph of critical nodes
    # with edge weights = shortest path distances
    # Prim's algorithm
    in_mst = [False] * k
    min_edge = [INF] * k
    min_edge[0] = 0
    total = 0
    
    for _ in range(k):
        # Find minimum edge to add
        u = -1
        for v in range(k):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        in_mst[u] = True
        total += min_edge[u]
        # Update min_edge
        for v in range(k):
            if not in_mst[v] and dist[u][v] < min_edge[v]:
                min_edge[v] = dist[u][v]
    
    print(total)

if __name__ == "__main__":
    solve()
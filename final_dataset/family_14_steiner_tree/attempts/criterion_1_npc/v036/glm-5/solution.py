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
    
    # Compute pairwise shortest distances between critical languages
    critical_list = list(critical)
    dist_matrix = {}
    
    for start in critical_list:
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist_matrix[start] = dist
    
    # Build graph for Steiner tree: nodes are critical languages
    # Edge weight between critical i and j is shortest path distance
    crit_to_idx = {lang: i for i, lang in enumerate(critical_list)}
    num_crit = len(critical_list)
    
    # Prim's algorithm for MST
    total_cost = 0
    in_mst = [False] * num_crit
    min_edge = [float('inf')] * num_crit
    min_edge[0] = 0
    
    for _ in range(num_crit):
        # Find minimum edge not in MST
        u = -1
        for i in range(num_crit):
            if not in_mst[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i
        
        in_mst[u] = True
        total_cost += min_edge[u]
        
        # Update edges
        lang_u = critical_list[u]
        for v in range(num_crit):
            if not in_mst[v]:
                lang_v = critical_list[v]
                w = dist_matrix[lang_u][lang_v]
                if w < min_edge[v]:
                    min_edge[v] = w
    
    print(total_cost)

if __name__ == "__main__":
    solve()
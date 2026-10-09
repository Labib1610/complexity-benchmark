import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    anchors = set()
    for _ in range(k):
        anchors.add(int(next(it)))
    
    adj = defaultdict(list)
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))
    
    # Multi-source Dijkstra from all anchors
    INF = float('inf')
    dist = [INF] * (n + 1)
    source_edge = [-1] * (n + 1)  # which edge index led to this node
    pq = []
    
    for a in anchors:
        dist[a] = 0
        pq.append((0, a, -1))
    
    # Heap operations
    import heapq
    heapq.heapify(pq)
    
    visited = [False] * (n + 1)
    
    while pq:
        d, u, e_idx = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        source_edge[u] = e_idx
        
        for v, w, idx in adj[u]:
            if not visited[v] and dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v, idx))
    
    # Build virtual tree
    virtual_edges = defaultdict(list)
    for u, v, w in edges:
        if source_edge[u] != -1 and source_edge[u] == source_edge[v]:
            continue
        virtual_edges[u].append((v, w))
        virtual_edges[v].append((u, w))
    
    # Prim's MST on virtual tree
    in_mst = [False] * (n + 1)
    min_edge = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    
    # Start from first anchor
    start = next(iter(anchors))
    min_edge[start] = 0
    
    total_cost = 0
    mst_edges = []
    
    for _ in range(n):
        # Find minimum edge
        u = -1
        for i in range(1, n + 1):
            if not in_mst[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i
        
        if u == -1 or min_edge[u] == INF:
            break
        
        in_mst[u] = True
        total_cost += min_edge[u]
        
        if parent[u] != -1:
            mst_edges.append((parent[u], u))
        
        for v, w in virtual_edges[u]:
            if not in_mst[v] and w < min_edge[v]:
                min_edge[v] = w
                parent[v] = u
    
    if total_cost > B:
        print("NO")
        return
    
    print("YES")
    print(len(mst_edges))
    for u, v in mst_edges:
        print(u, v)

if __name__ == "__main__":
    solve()
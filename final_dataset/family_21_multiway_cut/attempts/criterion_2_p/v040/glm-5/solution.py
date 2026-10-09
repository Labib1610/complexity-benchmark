import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    t = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w, len(edges) - 1))
        adj[v].append((u, w, len(edges) - 1))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    parent = [(-1, -1)] * (n + 1)
    visited = [False] * (n + 1)
    import heapq
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u == t:
            break
        for v, w, idx in adj[u]:
            if not visited[v] and d + w < dist[v]:
                dist[v] = d + w
                parent[v] = (u, idx)
                heapq.heappush(pq, (dist[v], v))

    if dist[t] > B:
        print("NO")
        return

    path_edges = []
    cur = t
    while cur != s:
        p, idx = parent[cur]
        path_edges.append(idx)
        cur = p

    print("YES")
    print(len(path_edges))
    for idx in path_edges:
        u, v, w = edges[idx]
        print(u, v)

solve()
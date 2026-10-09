import sys
from heapq import heappush, heappop

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

    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
        edges.append((u, v, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    parent_edge = [-1] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        if u == t:
            break
        for v, w, idx in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent_edge[v] = idx
                heappush(pq, (nd, v))

    if dist[t] > B:
        print("NO")
        return

    chosen = []
    node = t
    while node != s:
        idx = parent_edge[node]
        u, v, w = edges[idx]
        chosen.append((u, v))
        node = v if u == node else u

    print("YES")
    print(len(chosen))
    sys.stdout.write("\n".join(f"{u} {v}" for u, v in chosen) + ("\n" if chosen else ""))

solve()
import sys
from collections import defaultdict
import heapq

def solve():
    data = sys.stdin.read().split()
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
    idx = 0
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
        edges.append((u, v, w))
        idx += 1

    if s == t:
        print("YES")
        print(0)
        return

    INF = float('inf')
    dist1 = [INF] * (n + 1)
    dist2 = [INF] * (n + 1)
    dist1[s] = 0
    dist2[t] = 0

    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist1[u]:
            continue
        for v, w, _ in adj[u]:
            if dist1[u] + w < dist1[v]:
                dist1[v] = dist1[u] + w
                heapq.heappush(pq, (dist1[v], v))

    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist2[u]:
            continue
        for v, w, _ in adj[u]:
            if dist2[u] + w < dist2[v]:
                dist2[v] = dist2[u] + w
                heapq.heappush(pq, (dist2[v], v))

    min_cut = INF
    for u, v, w in edges:
        cand = dist1[u] + w + dist2[v]
        cand2 = dist1[v] + w + dist2[u]
        if cand < min_cut:
            min_cut = cand
        if cand2 < min_cut:
            min_cut = cand2

    min_cut = min(min_cut, dist1[t])

    if min_cut > B:
        print("NO")
        return

    ds_parent = [None] * (n + 1)
    dt_parent = [None] * (n + 1)

    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist1[u]:
            continue
        for v, w, e_idx in adj[u]:
            if dist1[u] + w == dist1[v] and ds_parent[v] is None and v != s:
                ds_parent[v] = (u, e_idx)
                heapq.heappush(pq, (dist1[v], v))

    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist2[u]:
            continue
        for v, w, e_idx in adj[u]:
            if dist2[u] + w == dist2[v] and dt_parent[v] is None and v != t:
                dt_parent[v] = (u, e_idx)
                heapq.heappush(pq, (dist2[v], v))

    cut_edges_idx = set()
    for i, (u, v, w) in enumerate(edges):
        if (dist1[u] + w + dist2[v] == min_cut) or (dist1[v] + w + dist2[u] == min_cut):
            cut_edges_idx.add(i)

    cut_edges = []
    for i in cut_edges_idx:
        u, v, w = edges[i]
        cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

if __name__ == "__main__":
    solve()
import sys
import heapq

INF = 10 ** 18

def dijkstra(dist, adj):
    """multi‑source Dijkstra, updates dist in place"""
    n = len(dist)
    heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
    heapq.heapify(heap)
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(t)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    FULL = (1 << t) - 1
    dp = [[INF] * n for _ in range(FULL + 1)]

    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # process all masks
    for mask in range(1, FULL + 1):
        # combine two proper sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # both sub and other are non‑empty
            for v in range(n):
                cand = dp[sub][v] + dp[other][v]
                if cand < dp[mask][v]:
                    dp[mask][v] = cand
            sub = (sub - 1) & mask

        # shortest‑path relaxation
        dijkstra(dp[mask], adj)

    ans = min(dp[FULL])
    print(ans)

if __name__ == "__main__":
    solve()
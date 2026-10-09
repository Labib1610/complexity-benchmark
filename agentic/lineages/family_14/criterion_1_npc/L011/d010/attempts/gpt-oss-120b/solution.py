import sys
import heapq

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
    # keep the smallest edge between two vertices (optional optimisation)
    min_edge = {}
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if u > v:
            u, v = v, u
        key = (u, v)
        if key in min_edge:
            if w < min_edge[key]:
                min_edge[key] = w
        else:
            min_edge[key] = w
    for (u, v), w in min_edge.items():
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t == 1:
        print(0)
        return

    FULL = (1 << t) - 1
    INF = 10 ** 18
    dp = [[INF] * (1 << t) for _ in range(n)]

    # initialise singletons
    for i, v in enumerate(terminals):
        dp[v][1 << i] = 0

    # helper: Dijkstra for a given mask
    def dijkstra(mask: int) -> None:
        dist = [dp[v][mask] for v in range(n)]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)
        while heap:
            d, x = heapq.heappop(heap)
            if d != dist[x]:
                continue
            for y, w in adj[x]:
                nd = d + w
                if nd < dist[y]:
                    dist[y] = nd
                    heapq.heappush(heap, (nd, y))
        for v in range(n):
            dp[v][mask] = dist[v]

    # DP over subsets
    for mask in range(1, FULL + 1):
        # combine smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # to avoid doing both (sub, other) and (other, sub) we could enforce sub < other,
            # but the cost is still tiny, so we skip that optimisation.
            for v in range(n):
                nd = dp[v][sub] + dp[v][other]
                if nd < dp[v][mask]:
                    dp[v][mask] = nd
            sub = (sub - 1) & mask
        # propagate through edges
        dijkstra(mask)

    ans = min(dp[v][FULL] for v in range(n))
    print(ans)


if __name__ == "__main__":
    solve()
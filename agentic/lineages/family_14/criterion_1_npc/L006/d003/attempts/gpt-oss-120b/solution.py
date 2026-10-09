import sys
import heapq

INF = 10**18

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

    if t == 1:
        print(0)
        return

    FULL = (1 << t) - 1
    dp = [[INF] * n for _ in range(FULL + 1)]

    # initialise singletons
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # helper: run multi-source Dijkstra for a given mask
    def dijkstra(mask: int):
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    # DP over masks
    for mask in range(1, FULL + 1):
        # skip singletons for merging, but still need Dijkstra
        if mask & (mask - 1):          # more than one bit set
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # to avoid doing both (sub, other) and (other, sub) we could enforce sub < other,
                # but the min operation is cheap; we just process all.
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                sub = (sub - 1) & mask
        # after merging, spread through the graph
        dijkstra(mask)

    ans = min(dp[FULL])
    print(ans)


if __name__ == "__main__":
    solve()
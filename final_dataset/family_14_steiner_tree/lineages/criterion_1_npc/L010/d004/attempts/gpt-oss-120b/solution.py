import sys
import heapq

INF = 10 ** 18

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]          # 0‑based
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(full + 1)]

    # singletons
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # main DP over masks
    for mask in range(1, full + 1):
        # merge two smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # both sub and other are non‑empty
            for v in range(n):
                cand = dp[sub][v] + dp[other][v]
                if cand < dp[mask][v]:
                    dp[mask][v] = cand
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, v = heapq.heappop(pq)
            if d != dp[mask][v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dp[mask][to]:
                    dp[mask][to] = nd
                    heapq.heappush(pq, (nd, to))

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
import sys
import heapq

INF = 10 ** 18

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

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # iterate masks in increasing order
    for mask in range(1, full + 1):
        # combine two already computed sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                # to avoid doing the same partition twice, enforce sub < other
                if sub < other:
                    dps = dp[sub]
                    dpo = dp[other]
                    dpm = dp[mask]
                    for v in range(n):
                        val = dps[v] + dpo[v]
                        if val < dpm[v]:
                            dpm[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        heap = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(heap)
        while heap:
            d, v = heapq.heappop(heap)
            if d != dp[mask][v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dp[mask][to]:
                    dp[mask][to] = nd
                    heapq.heappush(heap, (nd, to))

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
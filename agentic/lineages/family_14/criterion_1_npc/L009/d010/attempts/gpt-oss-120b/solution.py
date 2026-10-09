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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t == 1:
        print(0)
        return

    INF = 10**18
    FULL = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process masks in increasing order
    for mask in range(1, FULL + 1):
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need to consider each unordered pair once; both sub and other will appear
            for v in range(n):
                cand = dp[sub][v] + dp[other][v]
                if cand < dp[mask][v]:
                    dp[mask][v] = cand
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        heap = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(heap)
        while heap:
            d, u = heapq.heappop(heap)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(heap, (nd, v))

    answer = min(dp[FULL])
    print(answer)


if __name__ == "__main__":
    solve()
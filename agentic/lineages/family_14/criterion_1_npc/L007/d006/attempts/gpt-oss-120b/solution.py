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
    targets = [int(next(it)) - 1 for _ in range(t)]

    # graph
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

    K = t
    ALL = (1 << K) - 1
    dp = [[INF] * n for _ in range(1 << K)]

    # init singletons
    for i, v in enumerate(targets):
        dp[1 << i][v] = 0

    # process masks in increasing order of bits
    for mask in range(1, ALL + 1):
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need to consider each unordered pair once
            if other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for w, wcost in adj[u]:
                nd = d + wcost
                if nd < dp[mask][w]:
                    dp[mask][w] = nd
                    heapq.heappush(pq, (nd, w))

    ans = min(dp[ALL])
    print(ans)


if __name__ == "__main__":
    solve()
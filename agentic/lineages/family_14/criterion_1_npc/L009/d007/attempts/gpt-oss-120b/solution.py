import sys, heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    targets = [int(next(it)) - 1 for _ in range(t)]
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
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(targets):
        dp[1 << i][node] = 0

    # Precompute masks order by increasing bits
    masks = list(range(1, full + 1))
    masks.sort(key=lambda x: (x.bit_count(), x))

    for mask in masks:
        # combine smaller submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need to consider each partition once
            if other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
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
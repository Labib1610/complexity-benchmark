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
    cores = [int(next(it)) - 1 for _ in range(t)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = 10**18
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(cores):
        dp[1 << i][node] = 0

    # iterate masks
    for mask in range(1, full + 1):
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need to consider each partition once
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # multi-source Dijkstra for this mask
        heap = []
        for v in range(n):
            if dp[mask][v] < INF:
                heap.append((dp[mask][v], v))
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
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

    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        g[u].append((v, w))
        g[v].append((u, w))

    if t == 1:
        print(0)
        return

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialise singletons
    for i, node in enumerate(terminals):
        mask = 1 << i
        dp[mask][node] = 0

    # Dijkstra helper
    def dijkstra(mask: int):
        dist = dp[mask]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

    # run Dijkstra for singletons first
    for i in range(t):
        dijkstra(1 << i)

    # process all other masks
    for mask in range(1, full + 1):
        if mask & (mask - 1) == 0:   # power of two, already done
            continue
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # to avoid duplicate work we can enforce sub < other, but not needed
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub - 1) & mask
        # shortest path relaxation
        dijkstra(mask)

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()
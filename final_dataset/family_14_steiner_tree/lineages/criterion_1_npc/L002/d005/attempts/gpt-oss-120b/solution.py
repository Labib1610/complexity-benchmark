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

    INF = 10**18
    T = 1 << t
    dp = [[INF] * n for _ in range(T)]

    # initialise single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # helper: run multi-source Dijkstra for a given mask
    def dijkstra(mask: int):
        dist = dp[mask]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

    # DP over masks
    for mask in range(1, T):
        # skip singletons (already optimal)
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # combine two already computed masks
            # only need to consider sub where sub < other to avoid duplicate work,
            # but simplicity: process all
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub - 1) & mask
        # after merging, propagate through edges
        dijkstra(mask)

    full = T - 1
    ans = min(dp[full])
    print(ans)

if __name__ == "__main__":
    solve()
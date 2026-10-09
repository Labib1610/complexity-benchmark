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

    terminals = [next(it) - 1 for _ in range(t)]          # zero based
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialise single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process masks in increasing order
    for mask in range(1, full_mask + 1):
        # combine two smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                # try to improve dp[mask][v] via dp[sub][v] + dp[other][v]
                dps = dp[sub]
                dpo = dp[other]
                dpm = dp[mask]
                for v in range(n):
                    val = dps[v] + dpo[v]
                    if val < dpm[v]:
                        dpm[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph edges
        dist = dp[mask]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        while pq:
            d, v = heapq.heappop(pq)
            if d != dist[v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(pq, (nd, to))

    answer = min(dp[full_mask])
    print(answer)


if __name__ == "__main__":
    solve()
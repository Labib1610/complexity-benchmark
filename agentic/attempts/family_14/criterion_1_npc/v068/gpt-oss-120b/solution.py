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
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process masks in increasing order
    for mask in range(1, full + 1):
        # merge smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dps = dp[sub]
                dpo = dp[other]
                dpm = dp[mask]
                for v in range(n):
                    nd = dps[v] + dpo[v]
                    if nd < dpm[v]:
                        dpm[v] = nd
            sub = (sub - 1) & mask

        # Dijkstra (multi‑source)
        heap = []
        dist = dp[mask]
        for v in range(n):
            if dist[v] < INF:
                heap.append((dist[v], v))
        heapq.heapify(heap)

        while heap:
            d, v = heapq.heappop(heap)
            if d != dist[v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(heap, (nd, to))

    ans = min(dp[full])
    print(ans)

if __name__ == "__main__":
    solve()
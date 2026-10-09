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

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialization
    for i, v in enumerate(targets):
        dp[1 << i][v] = 0

    # process masks in increasing order
    for mask in range(1, full + 1):
        # skip singletons (already optimal)
        if mask & (mask - 1):
            # merge submasks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # both non‑empty
                if other:
                    dps = dp[sub]
                    dpo = dp[other]
                    dp_mask = dp[mask]
                    for v in range(n):
                        val = dps[v] + dpo[v]
                        if val < dp_mask[v]:
                            dp_mask[v] = val
                sub = (sub - 1) & mask

        # multi‑source Dijkstra for this mask
        dist = dp[mask]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
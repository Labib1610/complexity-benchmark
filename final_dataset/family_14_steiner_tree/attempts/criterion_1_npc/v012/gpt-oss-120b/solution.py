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

    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialise single terminals
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # iterate masks
    for mask in range(1, full_mask + 1):
        # combine two smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need each unordered partition once (optional optimization)
            if sub < other:   # ensures each pair processed once
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # multi‑source Dijkstra to propagate through edges
        dist = dp[mask][:]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)

        while heap:
            d, v = heapq.heappop(heap)
            if d != dist[v]:
                continue
            nd = d
            for to, w in adj[v]:
                nd2 = nd + w
                if nd2 < dist[to]:
                    dist[to] = nd2
                    heapq.heappush(heap, (nd2, to))
        dp[mask] = dist

    ans = min(dp[full_mask])
    print(ans)


if __name__ == "__main__":
    solve()
import sys
import heapq

INF = 10 ** 15

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))                     # number of terminals (t)
    terminals = [int(next(it)) - 1 for _ in range(k)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    full_mask = (1 << k) - 1
    dp = [[INF] * n for _ in range(1 << k)]

    # initialization for single terminals
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # iterate over all masks
    for mask in range(1, full_mask + 1):
        # combine two proper non‑empty sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    cand = dp_sub[v] + dp_other[v]
                    if cand < dp_mask[v]:
                        dp_mask[v] = cand
            sub = (sub - 1) & mask

        # Dijkstra to propagate through ordinary edges
        dist = dp[mask][:]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        dp[mask] = dist

    answer = min(dp[full_mask])
    print(answer)


if __name__ == "__main__":
    solve()
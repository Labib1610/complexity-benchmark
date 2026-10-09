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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialise single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process all masks
    for mask in range(1, full + 1):
        # merge two proper sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through the graph
        dist = dp[mask]
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

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
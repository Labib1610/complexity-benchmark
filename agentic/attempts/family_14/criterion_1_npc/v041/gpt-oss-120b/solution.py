import sys
import heapq

INF = 10**18

def solve() -> None:
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
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

    if t <= 1:
        print(0)
        return

    full = 1 << t
    dp = [[INF] * n for _ in range(full)]

    # initialization for single terminals
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # process all masks
    for mask in range(1, full):
        # merging submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # combine only if both parts have been computed (they are,
            # because sub < mask)
            dsub = dp[sub]
            doth = dp[other]
            dcur = dp[mask]
            for v in range(n):
                val = dsub[v] + doth[v]
                if val < dcur[v]:
                    dcur[v] = val
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

    answer = min(dp[full - 1])
    print(answer)


if __name__ == "__main__":
    solve()
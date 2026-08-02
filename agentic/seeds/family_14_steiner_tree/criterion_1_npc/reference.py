import sys
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); t = int(data[idx + 2]); idx += 3
    terminals = [int(data[idx + i]) - 1 for i in range(t)]; idx += t

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; w = int(data[idx + 2]); idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float("inf")
    # dp[mask][v] = min cost of a subtree connecting the terminals in `mask` and
    # containing vertex v. (Dreyfus-Wagner / Erickson bitmask DP.)
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0

    for mask in range(1, 1 << t):
        row = dp[mask]
        # Combine two subtrees sharing root v.
        for v in range(n):
            sub = (mask - 1) & mask
            while sub > 0:
                other = mask ^ sub
                val = dp[sub][v] + dp[other][v]
                if val < row[v]:
                    row[v] = val
                sub = (sub - 1) & mask
        # Dijkstra relaxation: extend the subtree along edges.
        pq = [(row[v], v) for v in range(n) if row[v] < INF]
        heapq.heapify(pq)
        while pq:
            d, v = heapq.heappop(pq)
            if d > row[v]:
                continue
            for (nx, w) in adj[v]:
                nd = d + w
                if nd < row[nx]:
                    row[nx] = nd
                    heapq.heappush(pq, (nd, nx))

    print(min(dp[full][v] for v in range(n)))


main()

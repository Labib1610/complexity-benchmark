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

    FULL = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # process masks in increasing order
    for mask in range(1, FULL + 1):
        # combine two smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # we only need to consider each partition once,
            # but it is fine to process all sub masks.
            row_sub = dp[sub]
            row_other = dp[other]
            row_mask = dp[mask]
            for v in range(n):
                cand = row_sub[v] + row_other[v]
                if cand < row_mask[v]:
                    row_mask[v] = cand
            sub = (sub - 1) & mask

        # multi‑source Dijkstra for this mask
        heap = []
        row = dp[mask]
        for v in range(n):
            if row[v] < INF:
                heap.append((row[v], v))
        heapq.heapify(heap)

        while heap:
            d, u = heapq.heappop(heap)
            if d != row[u]:
                continue
            for to, w in adj[u]:
                nd = d + w
                if nd < row[to]:
                    row[to] = nd
                    heapq.heappush(heap, (nd, to))

    ans = min(dp[FULL])
    print(ans)


if __name__ == "__main__":
    solve()
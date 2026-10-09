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

    required = [int(next(it)) - 1 for _ in range(t)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialise single‑terminal masks
    for i, v in enumerate(required):
        dp[1 << i][v] = 0

    # process masks increasingly
    for mask in range(1, full + 1):
        # combine two smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                row_sub = dp[sub]
                row_oth = dp[other]
                row_mask = dp[mask]
                for v in range(n):
                    val = row_sub[v] + row_oth[v]
                    if val < row_mask[v]:
                        row_mask[v] = val
            sub = (sub - 1) & mask

        # multi‑source Dijkstra for this mask
        heap = []
        row = dp[mask]
        for v in range(n):
            if row[v] < INF:
                heap.append((row[v], v))
        heapq.heapify(heap)

        while heap:
            d, v = heapq.heappop(heap)
            if d != row[v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < row[to]:
                    row[to] = nd
                    heapq.heappush(heap, (nd, to))

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
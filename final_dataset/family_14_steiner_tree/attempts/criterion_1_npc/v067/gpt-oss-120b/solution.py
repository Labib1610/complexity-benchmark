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

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(full + 1)]

    # initialise single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process all masks
    for mask in range(1, full + 1):
        # combine two proper sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other and sub < other:          # each unordered pair once
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    cand = dp_sub[v] + dp_other[v]
                    if cand < dp_mask[v]:
                        dp_mask[v] = cand
            sub = (sub - 1) & mask

        # multi‑source Dijkstra to spread through edges
        heap = []
        for v in range(n):
            if dp[mask][v] < INF:
                heap.append((dp[mask][v], v))
        heapq.heapify(heap)

        while heap:
            dist, u = heapq.heappop(heap)
            if dist != dp[mask][u]:
                continue
            for to, w in adj[u]:
                nd = dist + w
                if nd < dp[mask][to]:
                    dp[mask][to] = nd
                    heapq.heappush(heap, (nd, to))

    answer = min(dp[full])
    print(answer)


if __name__ == "__main__":
    solve()
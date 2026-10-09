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
    crit = [int(next(it)) - 1 for _ in range(t)]
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

    for i, node in enumerate(crit):
        dp[1 << i][node] = 0

    # precompute list of masks in increasing order of bits
    masks = list(range(1, full + 1))

    for mask in masks:
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need each unordered pair once; enforce sub < other to reduce work
            if sub < other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        heap = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(heap)
        visited = [False] * n
        while heap:
            d, v = heapq.heappop(heap)
            if visited[v]:
                continue
            visited[v] = True
            if d != dp[mask][v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dp[mask][to]:
                    dp[mask][to] = nd
                    heapq.heappush(heap, (nd, to))

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()
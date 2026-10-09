import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
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

    # Dijkstra from each terminal to initialize singletons
    def dijkstra(start):
        dist = [INF] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

    for i, term in enumerate(terminals):
        dist = dijkstra(term)
        mask = 1 << i
        dp[mask] = dist[:]   # copy

    # DP over subsets
    for mask in range(1, full + 1):
        # combine smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # only need to consider each partition once
            if sub < other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # multi-source Dijkstra to propagate through graph
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()
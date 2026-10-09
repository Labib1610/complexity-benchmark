import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    targets = [int(next(it)) - 1 for _ in range(t)]
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

    T = t
    full = (1 << T) - 1
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << T)]

    # initialize single terminals
    for i, node in enumerate(targets):
        mask = 1 << i
        dp[mask][node] = 0

    # for each mask, improve by combining submasks
    for mask in range(1, full + 1):
        # skip singletons (already init)
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # combine only once per partition (avoid duplicate work)
            if sub < other:
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask

        # run Dijkstra to propagate through edges
        dist = dp[mask][:]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        dp[mask] = dist

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()
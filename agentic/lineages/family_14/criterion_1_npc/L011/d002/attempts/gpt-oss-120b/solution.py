import sys
import heapq

INF = 10 ** 18

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]   # 0‑based
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialisation: single terminal sets
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process all masks
    for mask in range(1, full + 1):
        # merging sub‑masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:   # both non‑empty
                dsub = dp[sub]
                dother = dp[other]
                dcur = dp[mask]
                for v in range(n):
                    val = dsub[v] + dother[v]
                    if val < dcur[v]:
                        dcur[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to spread through the graph
        dist = dp[mask]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for to, w in adj[u]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(pq, (nd, to))

    answer = min(dp[full])
    print(answer)


if __name__ == "__main__":
    solve()
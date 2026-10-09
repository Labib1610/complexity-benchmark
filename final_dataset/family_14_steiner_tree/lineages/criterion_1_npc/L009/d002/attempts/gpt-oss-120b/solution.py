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
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initial masks: single terminal, distance = shortest paths from that terminal
    for i, term in enumerate(terminals):
        mask = 1 << i
        # Dijkstra from term
        dist = [INF] * n
        dist[term] = 0
        pq = [(0, term)]
        while pq:
            d, v = heapq.heappop(pq)
            if d != dist[v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(pq, (nd, to))
        dp[mask] = dist

    # DP over masks
    for mask in range(1, full_mask + 1):
        # skip singletons (already processed)
        if mask & (mask - 1):
            # combine submasks
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                # to avoid duplicate work, ensure sub < other (optional)
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                sub = (sub - 1) & mask

        # run multi-source Dijkstra to propagate through edges
        # initialise heap with current dp[mask][v]
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
            if d != dp[mask][v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dp[mask][to]:
                    dp[mask][to] = nd
                    heapq.heappush(pq, (nd, to))

    answer = min(dp[full_mask])
    print(answer)

if __name__ == "__main__":
    solve()
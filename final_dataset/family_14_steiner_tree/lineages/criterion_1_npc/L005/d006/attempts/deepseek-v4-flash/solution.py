import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    focal = list(map(int, input().split()))
    focal = [x - 1 for x in focal]  # 0-based

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # If t == 1, no edges needed
    if t == 1:
        print(0)
        return

    INF = 10**18
    # dp[mask][v] = min cost to connect terminals in mask, ending at node v
    dp = [[INF] * n for _ in range(1 << t)]
    for i, node in enumerate(focal):
        dp[1 << i][node] = 0

    # Dijkstra for each mask
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask

        # Run Dijkstra from current dp[mask]
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
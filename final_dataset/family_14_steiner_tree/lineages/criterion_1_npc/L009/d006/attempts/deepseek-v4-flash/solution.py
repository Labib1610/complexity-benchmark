import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x-1 for x in targets]  # 0-index

    INF = 10**18
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # dp[mask][v]
    dp = [[INF]*n for _ in range(1<<t)]
    for i, term in enumerate(targets):
        dp[1<<i][term] = 0

    # Dijkstra for each mask
    for mask in range(1<<t):
        # Dijkstra from current dp[mask]
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

        # Combine submasks
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub-1) & mask

    ans = min(dp[(1<<t)-1])
    print(ans)

if __name__ == "__main__":
    solve()
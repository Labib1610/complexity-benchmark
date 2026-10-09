import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x - 1 for x in terminals]  # 0-based

    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    # If only one terminal, cost is 0
    if t == 1:
        print(0)
        return

    INF = 10**18
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    dp = [[INF] * n for _ in range(1 << t)]
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0

    # Dijkstra for each mask
    for mask in range(1 << t):
        # First, combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask

        # Then run Dijkstra from all nodes in this mask
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for w, cost in graph[u]:
                nd = d + cost
                if nd < dp[mask][w]:
                    dp[mask][w] = nd
                    heapq.heappush(pq, (nd, w))

    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
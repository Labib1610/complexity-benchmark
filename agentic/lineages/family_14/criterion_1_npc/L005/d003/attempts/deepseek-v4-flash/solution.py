import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x - 1 for x in terminals]  # 0-based

    # Build adjacency list for undirected graph (since reverse is free)
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

    # Precompute shortest paths between all pairs using Dijkstra from each node
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for s in range(n):
        dist[s][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[s][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[s][v]:
                    dist[s][v] = nd
                    heapq.heappush(pq, (nd, v))

    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at node v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]

    # Initialize: single terminal
    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    # For each mask, try to combine two submasks
    for mask in range(1, full_mask):
        # Try splitting mask into two non-empty submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other < sub:  # avoid duplicate work
                sub = (sub - 1) & mask
                continue
            for u in range(n):
                if dp[sub][u] < INF and dp[other][u] < INF:
                    dp[mask][u] = min(dp[mask][u], dp[sub][u] + dp[other][u])
            sub = (sub - 1) & mask

        # Relax using shortest paths
        for u in range(n):
            if dp[mask][u] < INF:
                for v in range(n):
                    if dist[u][v] < INF:
                        nd = dp[mask][u] + dist[u][v]
                        if nd < dp[mask][v]:
                            dp[mask][v] = nd

    # Answer is min over all nodes for full mask
    ans = min(dp[full_mask - 1])
    print(ans)

if __name__ == "__main__":
    solve()
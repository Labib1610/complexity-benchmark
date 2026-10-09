import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    centers = list(map(int, input().split()))
    centers = [c - 1 for c in centers]  # 0-index

    INF = 10**18
    # adjacency list
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    # If t == 1, no need to connect anything
    if t == 1:
        print(0)
        return

    # Step 1: Compute all-pairs shortest paths (Floyd-Warshall or Dijkstra from each node)
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in range(n):
        for v, w in graph[u]:
            if w < dist[u][v]:
                dist[u][v] = w

    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    # Step 2: DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    full_mask = 1 << t
    dp = [[INF] * n for _ in range(full_mask)]

    # Initialize: single terminal
    for i in range(t):
        c = centers[i]
        for v in range(n):
            dp[1 << i][v] = dist[c][v]

    # Combine subsets
    for mask in range(1, full_mask):
        # Try splitting mask into two non-empty subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask

        # Run Dijkstra-like relaxation for this mask
        # Since n <= 100, we can just do a simple relaxation loop
        # Use priority queue for efficiency
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    # Answer: min over all nodes of dp[full_mask-1][v]
    ans = min(dp[full_mask - 1])
    print(ans)

if __name__ == "__main__":
    solve()
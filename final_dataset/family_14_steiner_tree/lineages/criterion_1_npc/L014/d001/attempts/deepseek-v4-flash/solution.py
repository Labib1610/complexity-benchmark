import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]  # 0-based

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

    # Dijkstra from every node
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
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
    full_mask = 1 << t
    dp = [[INF]*n for _ in range(full_mask)]

    # Initialize: single terminal
    for i in range(t):
        for v in range(n):
            dp[1 << i][v] = dist[terminals[i]][v]

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

        # Relax via Dijkstra-like step for this mask
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))

    ans = min(dp[full_mask-1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
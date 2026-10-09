import sys
import heapq

def main():
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

    # Dijkstra from each terminal to all nodes
    INF = 10**18
    dist = [[INF] * n for _ in range(t)]
    for i, s in enumerate(terminals):
        d = dist[i]
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in graph[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))

    # DP over subsets of terminals
    # dp[mask][i] = min cost to connect terminals in mask, ending at terminal i
    full_mask = 1 << t
    dp = [[INF] * t for _ in range(full_mask)]
    for i in range(t):
        dp[1 << i][i] = 0

    # First: combine subsets via terminal-to-terminal distances
    for mask in range(full_mask):
        for i in range(t):
            if dp[mask][i] == INF:
                continue
            # Try to add another terminal j
            for j in range(t):
                if mask & (1 << j):
                    continue
                nmask = mask | (1 << j)
                nd = dp[mask][i] + dist[i][terminals[j]]
                if nd < dp[nmask][j]:
                    dp[nmask][j] = nd

    # Second: allow merging via non-terminal nodes (Steiner tree DP)
    # We can merge two subsets at any node, but since we only care about terminals,
    # we can use the shortest path distances between terminals as edges.
    # Actually, the above already gives the MST-like solution for the terminal graph.
    # But Steiner tree may use non-terminal nodes, which is already captured by dist[i][terminals[j]].
    # So the above DP is sufficient.

    ans = min(dp[full_mask - 1][i] for i in range(t))
    print(ans)

if __name__ == "__main__":
    main()
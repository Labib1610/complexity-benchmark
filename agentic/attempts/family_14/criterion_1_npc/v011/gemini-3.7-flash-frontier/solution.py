import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    idx = 3
    terminals = [int(x) - 1 for x in input_data[idx:idx + t]]
    idx += t

    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        if u != v:
            adj[u].append((v, w))
            adj[v].append((u, w))

    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        # Submask combination
        # To iterate over submasks:
        submask = (mask - 1) & mask
        while submask > 0:
            if submask <= (mask ^ submask):
                other = mask ^ submask
                for u in range(n):
                    val = dp[submask][u] + dp[other][u]
                    if val < dp[mask][u]:
                        dp[mask][u] = val
            submask = (submask - 1) & mask

        # Dijkstra relaxation for this mask
        pq = []
        for u in range(n):
            if dp[mask][u] < INF:
                heapq.heappush(pq, (dp[mask][u], u))

        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                if dp[mask][u] + w < dp[mask][v]:
                    dp[mask][v] = dp[mask][u] + w
                    heapq.heappush(pq, (dp[mask][v], v))

    full_mask = num_masks - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == '__main__':
    solve()
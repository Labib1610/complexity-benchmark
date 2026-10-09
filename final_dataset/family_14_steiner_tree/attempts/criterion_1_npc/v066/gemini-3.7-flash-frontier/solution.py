import heapq
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    if t <= 1:
        print(0)
        return

    idx = 3
    terminals = []
    for _ in range(t):
        terminals.append(int(input_data[idx]))
        idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float("inf")
    num_masks = 1 << t
    dp = [[INF] * (n + 1) for _ in range(num_masks)]

    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        dp_mask = dp[mask]
        low = mask & -mask

        if mask & (mask - 1):
            sub = (mask - 1) & mask
            while sub > 0:
                if sub & low:
                    other = mask ^ sub
                    dp_sub = dp[sub]
                    dp_other = dp[other]
                    for u in range(1, n + 1):
                        val = dp_sub[u] + dp_other[u]
                        if val < dp_mask[u]:
                            dp_mask[u] = val
                sub = (sub - 1) & mask

        pq = []
        for u in range(1, n + 1):
            if dp_mask[u] < INF:
                heapq.heappush(pq, (dp_mask[u], u))

        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if d + w < dp_mask[v]:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))

    ans = min(dp[num_masks - 1][1:])
    print(ans)


if __name__ == "__main__":
    solve()
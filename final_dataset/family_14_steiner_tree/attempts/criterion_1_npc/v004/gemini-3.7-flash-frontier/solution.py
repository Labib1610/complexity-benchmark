import heapq
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    idx = 3
    terminals = []
    for _ in range(t):
        terminals.append(int(input_data[idx]) - 1)
        idx += 1

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    INF = float("inf")
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            dp_sub = dp[submask]
            dp_other = dp[other]
            dp_mask = dp[mask]
            for u in range(n):
                val = dp_sub[u] + dp_other[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            submask = (submask - 1) & mask

        dp_mask = dp[mask]
        pq = [(dp_mask[u], u) for u in range(n) if dp_mask[u] < INF]
        heapq.heapify(pq)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if d + w < dp_mask[v]:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))

    ans = min(dp[(1 << t) - 1])
    print(ans)


if __name__ == "__main__":
    solve()
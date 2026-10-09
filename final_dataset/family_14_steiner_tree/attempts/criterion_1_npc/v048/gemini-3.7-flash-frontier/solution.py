import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    t = int(data[2])

    idx = 3
    terminals = [int(data[idx + i]) - 1 for i in range(t)]
    idx += t

    if t <= 1:
        print(0)
        return

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            dist_i = dist[i]
            dik = dist_i[k]
            if dik == INF:
                continue
            for j in range(n):
                if dik + dist_k[j] < dist_i[j]:
                    dist_i[j] = dik + dist_k[j]

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        term = terminals[i]
        mask = 1 << i
        for u in range(n):
            dp[mask][u] = dist[term][u]

    for mask in range(1, num_masks):
        # If mask is a power of 2, already initialized
        if (mask & (mask - 1)) != 0:
            first_bit = mask & (-mask)
            dp_mask = dp[mask]
            sub = (mask - 1) & mask
            while sub > 0:
                if sub & first_bit:
                    other = mask ^ sub
                    dp_sub = dp[sub]
                    dp_other = dp[other]
                    for u in range(n):
                        val = dp_sub[u] + dp_other[u]
                        if val < dp_mask[u]:
                            dp_mask[u] = val
                sub = (sub - 1) & mask

            # Update with shortest paths
            temp = list(dp_mask)
            for v in range(n):
                min_val = INF
                dist_v = dist[v]
                for u in range(n):
                    val = temp[u] + dist_v[u]
                    if val < min_val:
                        min_val = val
                dp_mask[v] = min_val

    ans = dp[num_masks - 1][terminals[0]]
    print(ans)


if __name__ == "__main__":
    solve()
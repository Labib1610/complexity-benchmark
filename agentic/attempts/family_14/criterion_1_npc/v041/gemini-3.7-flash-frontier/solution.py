import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))

    terminals = [int(next(iterator)) - 1 for _ in range(t)]

    if t <= 1:
        print(0)
        return

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        if u != v:
            if w < dist[u][v]:
                dist[u][v] = w
                dist[v][u] = w

    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            dist_i = dist[i]
            d_ik = dist_i[k]
            if d_ik == INF:
                continue
            for j in range(n):
                if d_ik + dist_k[j] < dist_i[j]:
                    dist_i[j] = d_ik + dist_k[j]

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        mask = 1 << i
        u = terminals[i]
        dp_mask = dp[mask]
        dist_u = dist[u]
        for v in range(n):
            dp_mask[v] = dist_u[v]

    for mask in range(1, num_masks):
        if (mask & (mask - 1)) == 0:
            continue

        dp_mask = dp[mask]
        sub = (mask - 1) & mask
        while sub > (mask ^ sub):
            other = mask ^ sub
            dp_sub = dp[sub]
            dp_other = dp[other]
            for u in range(n):
                val = dp_sub[u] + dp_other[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            sub = (sub - 1) & mask

        # Update via all-pairs shortest path
        # dp_mask[u] = min_v (dp_mask[v] + dist[v][u])
        dp_mask_copy = dp_mask[:]
        for u in range(n):
            min_val = dp_mask[u]
            for v in range(n):
                val = dp_mask_copy[v] + dist[v][u]
                if val < min_val:
                    min_val = val
            dp_mask[u] = min_val

    ans = min(dp[(1 << t) - 1])
    print(ans)


if __name__ == "__main__":
    solve()
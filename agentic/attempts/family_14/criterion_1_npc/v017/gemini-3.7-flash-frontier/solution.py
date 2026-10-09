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
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(n):
                if di[j] > dik + dk[j]:
                    di[j] = dik + dk[j]

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        mask = 1 << i
        term = terminals[i]
        for u in range(n):
            dp[mask][u] = dist[term][u]

    for mask in range(1, num_masks):
        if (mask & (mask - 1)) == 0:
            continue

        dp_mask = dp[mask]
        low_bit = mask & -mask
        sub = (mask - 1) & mask
        while sub:
            if sub & low_bit:
                comp = mask ^ sub
                dp_sub = dp[sub]
                dp_comp = dp[comp]
                for u in range(n):
                    val = dp_sub[u] + dp_comp[u]
                    if val < dp_mask[u]:
                        dp_mask[u] = val
            sub = (sub - 1) & mask

        # Shortest path update
        new_dp_mask = [INF] * n
        for v in range(n):
            min_val = INF
            for u in range(n):
                val = dp_mask[u] + dist[u][v]
                if val < min_val:
                    min_val = val
            new_dp_mask[v] = min_val
        dp[mask] = new_dp_mask

    ans = min(dp[num_masks - 1])
    print(ans)


if __name__ == "__main__":
    solve()
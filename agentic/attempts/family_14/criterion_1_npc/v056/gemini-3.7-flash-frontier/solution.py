import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    idx = 3
    terminals = [int(input_data[idx + i]) - 1 for i in range(t)]
    idx += t

    INF = 10**15
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik >= INF:
                continue
            for j in range(n):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        dp_mask = dp[mask]
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub <= other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                for u in range(n):
                    val = dp_sub[u] + dp_other[u]
                    if val < dp_mask[u]:
                        dp_mask[u] = val
            sub = (sub - 1) & mask

        new_dp = [INF] * n
        for v in range(n):
            val_v = dp_mask[v]
            if val_v >= INF:
                continue
            dv = dist[v]
            for u in range(n):
                if val_v + dv[u] < new_dp[u]:
                    new_dp[u] = val_v + dv[u]
        dp[mask] = new_dp

    ans = min(dp[num_masks - 1])
    print(ans)


if __name__ == "__main__":
    solve()
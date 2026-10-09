import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    t = int(data[2])

    ptr = 3
    terminals = []
    for _ in range(t):
        terminals.append(int(data[ptr]) - 1)
        ptr += 1

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(data[ptr]) - 1
        v = int(data[ptr + 1]) - 1
        w = int(data[ptr + 2])
        ptr += 3
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
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        # Step 1: Combine submasks
        first_bit = mask & -mask
        sub = (mask - 1) & mask
        while sub >= first_bit:
            if sub & first_bit:
                comp = mask ^ sub
                dp_sub = dp[sub]
                dp_comp = dp[comp]
                dp_mask = dp[mask]
                for u in range(n):
                    val = dp_sub[u] + dp_comp[u]
                    if val < dp_mask[u]:
                        dp_mask[u] = val
            sub = (sub - 1) & mask

        # Step 2: Relax using shortest paths
        dp_mask = dp[mask]
        new_dp = [INF] * n
        for u in range(n):
            min_val = INF
            for v in range(n):
                if dp_mask[v] != INF:
                    val = dp_mask[v] + dist[v][u]
                    if val < min_val:
                        min_val = val
            new_dp[u] = min_val
        dp[mask] = new_dp

    ans = min(dp[num_masks - 1])
    print(ans)


if __name__ == "__main__":
    solve()
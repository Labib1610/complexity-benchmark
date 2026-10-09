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
    terminals = []
    for _ in range(t):
        terminals.append(int(data[idx]) - 1)
        idx += 1

    if t <= 1:
        print(0)
        return

    INF = float('inf')
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
        term = terminals[i]
        mask = 1 << i
        for v in range(n):
            dp[mask][v] = dist[term][v]

    for mask in range(1, num_masks):
        if (mask & (mask - 1)) == 0:
            continue

        lowbit = mask & -mask
        submask = (mask - 1) & mask
        while submask > 0:
            if submask & lowbit:
                comp = mask ^ submask
                dp_sub = dp[submask]
                dp_comp = dp[comp]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_comp[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            submask = (submask - 1) & mask

        dp_mask = dp[mask]
        new_dp = [INF] * n
        for u in range(n):
            du = dist[u]
            min_val = INF
            for v in range(n):
                val = dp_mask[v] + du[v]
                if val < min_val:
                    min_val = val
            new_dp[u] = min_val
        dp[mask] = new_dp

    ans = min(dp[(1 << t) - 1])
    print(ans)

if __name__ == '__main__':
    solve()
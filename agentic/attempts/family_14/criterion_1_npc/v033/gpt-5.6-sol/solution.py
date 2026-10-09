import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]
    INF = 10**30

    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
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
                value = dik + dk[j]
                if value < di[j]:
                    di[j] = value

    size = 1 << t
    dp = [None] * size

    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            bit = mask.bit_length() - 1
            dp[mask] = dist[terminals[bit]][:]
            continue

        merged = [INF] * n
        low_bit = mask & -mask
        remaining = mask ^ low_bit
        subset = (remaining - 1) & remaining

        while True:
            left = low_bit | subset
            right = remaining ^ subset
            dl = dp[left]
            dr = dp[right]

            for v in range(n):
                value = dl[v] + dr[v]
                if value < merged[v]:
                    merged[v] = value

            if subset == 0:
                break
            subset = (subset - 1) & remaining

        result = [INF] * n
        for u in range(n):
            base = merged[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < result[v]:
                    result[v] = value

        dp[mask] = result

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
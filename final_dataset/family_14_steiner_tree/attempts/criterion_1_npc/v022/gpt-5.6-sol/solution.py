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
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                value = dik + dk[j]
                if value < di[j]:
                    di[j] = value

    size = 1 << t
    dp = [None] * size

    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            terminal_index = mask.bit_length() - 1
            dp[mask] = dist[terminals[terminal_index]][:]
            continue

        merged = [INF] * n
        lowest_bit = mask & -mask
        submask = (mask - 1) & mask

        while submask:
            if submask & lowest_bit:
                other = mask ^ submask
                if other:
                    left = dp[submask]
                    right = dp[other]
                    for v in range(n):
                        value = left[v] + right[v]
                        if value < merged[v]:
                            merged[v] = value
            submask = (submask - 1) & mask

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
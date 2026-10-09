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
            terminal_index = mask.bit_length() - 1
            dp[mask] = dist[terminals[terminal_index]][:]
            continue

        merged = [INF] * n
        lowbit = mask & -mask
        sub = (mask - 1) & mask

        while sub:
            other = mask ^ sub
            if other and (sub & lowbit):
                a = dp[sub]
                b = dp[other]
                for v in range(n):
                    value = a[v] + b[v]
                    if value < merged[v]:
                        merged[v] = value
            sub = (sub - 1) & mask

        relaxed = [INF] * n
        for u in range(n):
            base = merged[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < relaxed[v]:
                    relaxed[v] = value

        dp[mask] = relaxed

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
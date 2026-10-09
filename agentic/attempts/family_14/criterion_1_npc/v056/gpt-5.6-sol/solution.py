import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]

    INF = 10**18
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

    if t == 1:
        print(0)
        return

    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    size = 1 << t
    dp = [None] * size

    for i, terminal in enumerate(terminals):
        dp[1 << i] = dist[terminal][:]

    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            continue

        merged = [INF] * n
        lowest_bit = mask & -mask
        sub = (mask - 1) & mask

        while sub:
            if sub & lowest_bit:
                other = mask ^ sub
                a = dp[sub]
                b = dp[other]
                for v in range(n):
                    value = a[v] + b[v]
                    if value < merged[v]:
                        merged[v] = value
            sub = (sub - 1) & mask

        closed = [INF] * n
        for u in range(n):
            base = merged[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < closed[v]:
                    closed[v] = value

        dp[mask] = closed

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
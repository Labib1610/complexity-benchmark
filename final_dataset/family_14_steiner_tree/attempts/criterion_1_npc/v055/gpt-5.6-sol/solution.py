import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]

    if t == 1:
        print(0)
        return

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

    # All-pairs shortest paths.
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

    full = (1 << t) - 1
    dp = [None] * (full + 1)

    for mask in range(1, full + 1):
        if mask & (mask - 1) == 0:
            terminal_index = mask.bit_length() - 1
            dp[mask] = dist[terminals[terminal_index]][:]
            continue

        cur = [INF] * n

        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                a = dp[sub]
                b = dp[other]
                for v in range(n):
                    value = a[v] + b[v]
                    if value < cur[v]:
                        cur[v] = value
            sub = (sub - 1) & mask

        relaxed = [INF] * n
        for u in range(n):
            base = cur[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < relaxed[v]:
                    relaxed[v] = value

        dp[mask] = relaxed

    print(min(dp[full]))

if __name__ == "__main__":
    main()
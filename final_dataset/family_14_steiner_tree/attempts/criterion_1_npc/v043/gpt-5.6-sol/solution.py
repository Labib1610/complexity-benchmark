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
    dp = [[INF] * n for _ in range(size)]

    for i, terminal in enumerate(terminals):
        dp[1 << i] = dist[terminal][:]

    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            continue

        merged = [INF] * n
        sub = (mask - 1) & mask

        while sub:
            other = mask ^ sub
            if sub < other:
                left = dp[sub]
                right = dp[other]
                for v in range(n):
                    value = left[v] + right[v]
                    if value < merged[v]:
                        merged[v] = value
            sub = (sub - 1) & mask

        closed = [INF] * n
        for v in range(n):
            dv = dist[v]
            best = INF
            for u in range(n):
                value = merged[u] + dv[u]
                if value < best:
                    best = value
            closed[v] = best

        dp[mask] = closed

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
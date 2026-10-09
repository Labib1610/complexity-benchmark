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
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    total_masks = 1 << t
    dp = [None] * total_masks

    for mask in range(1, total_masks):
        current = [INF] * n

        if mask & (mask - 1) == 0:
            terminal_index = mask.bit_length() - 1
            current[terminals[terminal_index]] = 0
        else:
            lowbit = mask & -mask
            sub = (mask - 1) & mask
            while sub:
                if sub & lowbit:
                    other = mask ^ sub
                    if other:
                        left = dp[sub]
                        right = dp[other]
                        for v in range(n):
                            value = left[v] + right[v]
                            if value < current[v]:
                                current[v] = value
                sub = (sub - 1) & mask

        closed = [INF] * n
        for u in range(n):
            base = current[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < closed[v]:
                    closed[v] = value

        dp[mask] = closed

    print(min(dp[total_masks - 1]))

if __name__ == "__main__":
    main()
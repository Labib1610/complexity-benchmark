import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    n, m, t = data[idx], data[idx + 1], data[idx + 2]
    idx += 3

    terminals = [x - 1 for x in data[idx:idx + t]]
    idx += t

    if t == 1:
        print(0)
        return

    INF = 10**30
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = data[idx] - 1, data[idx + 1] - 1, data[idx + 2]
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # All-pairs shortest paths.
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            via = di[k]
            if via == INF:
                continue
            for j in range(n):
                value = via + dk[j]
                if value < di[j]:
                    di[j] = value

    size = 1 << t
    dp = [[INF] * n for _ in range(size)]

    for i, terminal in enumerate(terminals):
        dp[1 << i] = dist[terminal][:]

    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            continue

        merged = [INF] * n
        lowest_bit = mask & -mask
        sub = (mask - 1) & mask

        # Only consider one orientation of each partition.
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

        # Move the common connection point through shortest paths.
        current = [INF] * n
        for u in range(n):
            base = merged[u]
            if base == INF:
                continue
            du = dist[u]
            for v in range(n):
                value = base + du[v]
                if value < current[v]:
                    current[v] = value

        dp[mask] = current

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
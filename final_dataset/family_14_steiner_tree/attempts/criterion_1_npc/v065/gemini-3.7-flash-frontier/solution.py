import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))

    terminals = [int(next(iterator)) - 1 for _ in range(t)]

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            dist_i = dist[i]
            dik = dist_i[k]
            if dik == INF:
                continue
            for j in range(n):
                if dist_i[j] > dik + dist_k[j]:
                    dist_i[j] = dik + dist_k[j]

    if t == 1:
        print(0)
        return

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]

    for i, term in enumerate(terminals):
        for v in range(n):
            dp[1 << i][v] = dist[term][v]

    for mask in range(1, num_masks):
        # If mask is a power of 2, it's already initialized and updated with dist
        if (mask & (mask - 1)) != 0:
            dp_mask = dp[mask]
            # Submask iteration: s goes through proper submasks
            sub = (mask - 1) & mask
            while sub > (mask ^ sub):
                sub_comp = mask ^ sub
                dp_sub = dp[sub]
                dp_comp = dp[sub_comp]
                for v in range(n):
                    val = dp_sub[v] + dp_comp[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
                sub = (sub - 1) & mask

            # Update with shortest paths
            for v in range(n):
                min_val = dp_mask[v]
                for u in range(n):
                    val = dp_mask[u] + dist[u][v]
                    if val < min_val:
                        min_val = val
                dp_mask[v] = min_val

    ans = min(dp[num_masks - 1])
    print(ans)


if __name__ == "__main__":
    solve()
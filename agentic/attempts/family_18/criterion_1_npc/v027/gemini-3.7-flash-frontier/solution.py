import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])

    if n == 1:
        if B >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    adj = [0] * n
    deg = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            deg[u] += 1
            deg[v] += 1

    size = 1 << n
    INF = 10**15
    dp = [INF] * size
    prev = [0] * size
    cut = [0] * size

    dp[0] = 0

    full_mask = size - 1
    for mask in range(size - 1):
        cur_dp = dp[mask]
        if cur_dp > B:
            continue
        cur_cut = cut[mask]

        for v in range(n):
            bit = 1 << v
            if not (mask & bit):
                nxt = mask | bit
                # Compute cut of nxt set
                # neighbor count in mask:
                in_neighbors = (adj[v] & mask).bit_count()
                nxt_cut = cur_cut + deg[v] - 2 * in_neighbors
                cut[nxt] = nxt_cut

                add_cost = nxt_cut if nxt != full_mask else 0
                cost = cur_dp + add_cost

                if cost < dp[nxt]:
                    dp[nxt] = cost
                    prev[nxt] = v

    if dp[full_mask] <= B:
        print("YES")
        order = [0] * n
        curr = full_mask
        for minute in range(n, 0, -1):
            v = prev[curr]
            order[v] = minute
            curr ^= 1 << v
        print(*(order[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()
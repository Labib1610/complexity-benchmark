import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])

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

    num_masks = 1 << n
    cut = [0] * num_masks

    for mask in range(1, num_masks):
        lsb = mask & -mask
        v = (lsb).bit_length() - 1
        prev_mask = mask ^ lsb
        # cut[mask] = cut[prev_mask] + deg[v] - 2 * popcount(adj[v] & prev_mask)
        cut[mask] = (
            cut[prev_mask] + deg[v] - 2 * (adj[v] & prev_mask).bit_count()
        )

    INF = 10**18
    dp = [INF] * num_masks
    parent_lsb = [0] * num_masks
    dp[0] = 0

    all_mask = num_masks - 1
    for mask in range(num_masks - 1):
        c = dp[mask] + cut[mask]
        rem = all_mask ^ mask
        while rem:
            lsb = rem & -rem
            nxt = mask | lsb
            if c < dp[nxt]:
                dp[nxt] = c
                parent_lsb[nxt] = lsb
            rem ^= lsb

    min_cost = dp[all_mask]
    if min_cost > B:
        print("NO")
        return

    # Reconstruct order of vertices
    order = []
    curr = all_mask
    while curr > 0:
        lsb = parent_lsb[curr]
        v = (lsb).bit_length() - 1
        order.append(v)
        curr ^= lsb

    order.reverse()

    pos = [0] * n
    for p, v in enumerate(order):
        pos[v] = p + 1

    print("YES")
    print(*(pos[i] for i in range(n)))


if __name__ == "__main__":
    solve()
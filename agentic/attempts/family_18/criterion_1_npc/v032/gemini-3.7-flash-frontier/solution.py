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
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        deg[u] += 1
        deg[v] += 1

    size = 1 << n
    INF = 10**9
    dp = [INF] * size
    cut = [0] * size
    dp[0] = 0

    full_mask = size - 1
    for mask in range(1, size):
        lsb = mask & -mask
        u = lsb.bit_length() - 1
        prev = mask ^ lsb
        cut[mask] = cut[prev] + deg[u] - 2 * (adj[u] & prev).bit_count()

        min_prev = INF
        temp = mask
        while temp:
            b = temp & -temp
            val = dp[mask ^ b]
            if val < min_prev:
                min_prev = val
            temp ^= b

        if mask == full_mask:
            dp[mask] = min_prev
        else:
            dp[mask] = min_prev + cut[mask]

    min_cost = dp[full_mask]
    if min_cost > B:
        print("NO")
        return

    print("YES")

    # Reconstruct the permutation
    order = []
    curr = full_mask
    while curr > 0:
        temp = curr
        best_b = -1
        best_val = INF
        while temp:
            b = temp & -temp
            val = dp[curr ^ b]
            if val < best_val:
                best_val = val
                best_b = b
            temp ^= b

        u = best_b.bit_length() - 1
        order.append(u)
        curr ^= best_b

    order.reverse()

    ans = [0] * n
    for slot_idx, u in enumerate(order, 1):
        ans[u] = slot_idx

    print(*(ans[i] for i in range(n)))


if __name__ == "__main__":
    solve()
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

    num_states = 1 << n
    dp = [float("inf")] * num_states
    cut = [0] * num_states
    dp[0] = 0

    for mask in range(1, num_states):
        lsb = mask & -mask
        u = lsb.bit_length() - 1
        prev = mask ^ lsb
        cut[mask] = cut[prev] + deg[u] - 2 * (adj[u] & prev).bit_count()

        min_prev = float("inf")
        m_temp = mask
        while m_temp:
            b = m_temp & -m_temp
            val = dp[mask ^ b]
            if val < min_prev:
                min_prev = val
            m_temp ^= b

        if mask == num_states - 1:
            dp[mask] = min_prev
        else:
            dp[mask] = min_prev + cut[mask]

    min_cost = dp[num_states - 1]
    if min_cost > B:
        print("NO")
        return

    print("YES")
    order = []
    curr = num_states - 1
    while curr > 0:
        target = dp[curr]
        expected_prev_dp = target if curr == num_states - 1 else target - cut[curr]
        m_temp = curr
        chosen_v = -1
        while m_temp:
            b = m_temp & -m_temp
            v = b.bit_length() - 1
            if dp[curr ^ b] == expected_prev_dp:
                chosen_v = v
                break
            m_temp ^= b
        order.append(chosen_v)
        curr ^= 1 << chosen_v

    order.reverse()
    ans = [0] * n
    for zone_idx, v in enumerate(order):
        ans[v] = zone_idx + 1

    print(*ans)


if __name__ == "__main__":
    solve()
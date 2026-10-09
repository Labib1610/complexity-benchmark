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
    dp = [float("inf")] * size
    dp[0] = 0
    cut = [0] * size

    for mask in range(1, size):
        low_bit = mask & -mask
        b = low_bit.bit_length() - 1
        prev = mask ^ low_bit
        cut[mask] = cut[prev] + deg[b] - 2 * (adj[b] & prev).bit_count()

        m_temp = mask
        min_prev = float("inf")
        while m_temp:
            v_bit = m_temp & -m_temp
            val = dp[mask ^ v_bit]
            if val < min_prev:
                min_prev = val
            m_temp ^= v_bit
        dp[mask] = min_prev + cut[mask]

    min_cost = dp[size - 1]
    if min_cost <= B:
        print("YES")
        ans = [0] * n
        curr = size - 1
        for k in range(n, 0, -1):
            c = cut[curr]
            m_temp = curr
            chosen_v = -1
            while m_temp:
                v_bit = m_temp & -m_temp
                v = v_bit.bit_length() - 1
                if dp[curr ^ v_bit] + c == dp[curr]:
                    chosen_v = v
                    break
                m_temp ^= v_bit
            ans[chosen_v] = k
            curr ^= 1 << chosen_v
        print(*(ans[i] for i in range(n)))
    else:
        print("NO")


solve()
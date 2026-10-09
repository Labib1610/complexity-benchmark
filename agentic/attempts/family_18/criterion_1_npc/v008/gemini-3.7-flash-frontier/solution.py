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
    c = [0] * num_states
    for mask in range(1, num_states):
        lsb = mask & -mask
        u = lsb.bit_length() - 1
        prev = mask ^ lsb
        c[mask] = c[prev] + deg[u] - 2 * (prev & adj[u]).bit_count()

    dp = [float("inf")] * num_states
    parent = [0] * num_states
    dp[0] = 0

    all_mask = num_states - 1
    for mask in range(num_states - 1):
        cur_d = dp[mask]
        avail = all_mask ^ mask
        while avail:
            lsb = avail & -avail
            avail ^= lsb
            nxt = mask | lsb
            cost = cur_d + c[nxt]
            if cost < dp[nxt]:
                dp[nxt] = cost
                parent[nxt] = lsb

    if dp[all_mask] <= B:
        print("YES")
        pos = [0] * n
        curr = all_mask
        for p in range(n, 0, -1):
            lsb = parent[curr]
            u = lsb.bit_length() - 1
            pos[u] = p
            curr ^= lsb
        print(*(pos[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()
import sys


def main():
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

    num_states = 1 << n
    cut = [0] * num_states
    for i in range(n):
        bit = 1 << i
        mask_adj = adj[i]
        d = deg[i]
        for s in range(bit):
            cut[s | bit] = cut[s] + d - 2 * (s & mask_adj).bit_count()

    INF = 10**18
    dp = [INF] * num_states
    parent = [0] * num_states
    dp[0] = 0

    for mask in range(num_states - 1):
        c = dp[mask]
        if c > B:
            continue
        for u in range(n):
            if not (mask & (1 << u)):
                nmask = mask | (1 << u)
                val = c + cut[nmask]
                if val < dp[nmask]:
                    dp[nmask] = val
                    parent[nmask] = u

    total_cost = dp[num_states - 1]
    if total_cost <= B:
        pos = [0] * n
        mask = num_states - 1
        for step in range(n, 0, -1):
            u = parent[mask]
            pos[u] = step
            mask ^= 1 << u
        print("YES")
        print(*(pos[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    main()
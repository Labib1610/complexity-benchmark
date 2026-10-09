import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    B = int(data[2])

    adj = [0] * n
    deg = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        if u != v:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            deg[u] += 1
            deg[v] += 1

    num_states = 1 << n
    cut = [0] * num_states
    
    for mask in range(1, num_states):
        low_bit = mask & -mask
        v = low_bit.bit_length() - 1
        prev = mask ^ low_bit
        cut[mask] = cut[prev] + deg[v] - 2 * (adj[v] & prev).bit_count()

    INF = float('inf')
    dp = [INF] * num_states
    parent = [0] * num_states
    dp[0] = 0

    all_mask = num_states - 1
    for mask in range(num_states - 1):
        cur_d = dp[mask] + cut[mask]
        rem = all_mask ^ mask
        while rem:
            low_bit = rem & -rem
            v = low_bit.bit_length() - 1
            nmask = mask | low_bit
            if cur_d < dp[nmask]:
                dp[nmask] = cur_d
                parent[nmask] = v
            rem ^= low_bit

    if dp[all_mask] <= B:
        print("YES")
        pos = [0] * n
        curr = all_mask
        for slot in range(n, 0, -1):
            v = parent[curr]
            pos[v] = slot
            curr ^= (1 << v)
        print(*(pos[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    main()
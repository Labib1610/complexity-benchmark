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
            print("1")
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
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        deg[u] += 1
        deg[v] += 1

    size = 1 << n
    INF = 10**15

    cut = [0] * size
    dp = [INF] * size
    dp[0] = 0
    parent = bytearray(size)

    for mask in range(1, size):
        lowbit = mask & -mask
        v = lowbit.bit_length() - 1
        prev = mask ^ lowbit
        cut[mask] = cut[prev] + deg[v] - 2 * (prev & adj[v]).bit_count()

    for mask in range(1, size):
        temp_mask = mask
        best_val = INF
        best_v = 0
        c = cut[mask]
        while temp_mask:
            lowbit = temp_mask & -temp_mask
            v = lowbit.bit_length() - 1
            temp_mask ^= lowbit
            val = dp[mask ^ lowbit] + c
            if val < best_val:
                best_val = val
                best_v = v
        dp[mask] = best_val
        parent[mask] = best_v

    if dp[size - 1] <= B:
        print("YES")
        ans = [0] * n
        curr = size - 1
        for step in range(n, 0, -1):
            v = parent[curr]
            ans[v] = step
            curr ^= (1 << v)
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
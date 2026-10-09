import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])

    if n <= 1:
        print("YES")
        print("1")
        return

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
    INF = 10**9

    cut = [0] * num_states
    for mask in range(1, num_states):
        lsb = mask & -mask
        u = (lsb).bit_length() - 1
        prev = mask ^ lsb
        cut[mask] = cut[prev] + deg[u] - 2 * (adj[u] & prev).bit_count()

    dp = [INF] * num_states
    dp[0] = 0

    for mask in range(num_states - 1):
        d = dp[mask]
        if d > B:
            continue
        c = cut[mask] if mask > 0 else 0
        rem = (~mask) & (num_states - 1)
        while rem > 0:
            lsb = rem & -rem
            u = lsb.bit_length() - 1
            nmask = mask | lsb
            cost = d + cut[nmask]
            if nmask == num_states - 1:
                cost = d
            if cost < dp[nmask]:
                dp[nmask] = cost
            rem ^= lsb

    if dp[num_states - 1] > B:
        print("NO")
        return

    print("YES")

    curr = num_states - 1
    order = []
    for step in range(n, 0, -1):
        if step == n:
            target = dp[curr]
            for u in range(n):
                if (curr & (1 << u)) and dp[curr ^ (1 << u)] == target:
                    order.append(u)
                    curr ^= 1 << u
                    break
        else:
            for u in range(n):
                if curr & (1 << u):
                    prev = curr ^ (1 << u)
                    if dp[prev] + cut[curr] == dp[curr]:
                        order.append(u)
                        curr = prev
                        break

    order.reverse()
    pos = [0] * n
    for bay, u in enumerate(order, 1):
        pos[u] = bay

    print(*(pos[i] for i in range(n)))


if __name__ == "__main__":
    solve()
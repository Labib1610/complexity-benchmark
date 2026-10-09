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

    adj_mask = [0] * n
    deg = [0] * n

    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        deg[u] += 1
        deg[v] += 1

    num_states = 1 << n
    cut = [0] * num_states

    for mask in range(1, num_states):
        lsb = mask & -mask
        v = lsb.bit_length() - 1
        prev = mask ^ lsb
        cut[mask] = cut[prev] + deg[v] - 2 * (prev & adj_mask[v]).bit_count()

    INF = 10**18
    dp = [INF] * num_states
    parent = [-1] * num_states
    dp[0] = 0

    full_mask = num_states - 1

    for mask in range(num_states - 1):
        d = dp[mask]
        if d > B:
            continue
        
        avail = full_mask ^ mask
        while avail:
            lsb = avail & -avail
            v = lsb.bit_length() - 1
            next_mask = mask | lsb
            cost = d + cut[next_mask]
            if cost < dp[next_mask]:
                dp[next_mask] = cost
                parent[next_mask] = v
            avail ^= lsb

    if dp[full_mask] <= B:
        print("YES")
        order = []
        curr = full_mask
        while curr > 0:
            v = parent[curr]
            order.append(v)
            curr ^= (1 << v)
        order.reverse()

        pos = [0] * n
        for slot, u in enumerate(order, start=1):
            pos[u] = slot

        print(*(pos[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
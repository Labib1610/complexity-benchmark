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

    for i in range(n):
        deg[i] = adj[i].bit_count()

    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    # If N is small enough for DP (e.g. N <= 20)
    # Total cost of linear arrangement = sum_{S_i} cut(S_i) for i = 1 to n-1
    size = 1 << n
    dp = [10**9] * size
    parent = [-1] * size
    cut = [0] * size

    dp[0] = 0

    # Group masks by popcount
    by_popcount = [[] for _ in range(n + 1)]
    for mask in range(size):
        by_popcount[mask.bit_count()].append(mask)

    # Compute cut values
    for mask in range(1, size):
        v = (mask & -mask).bit_length() - 1
        prev_mask = mask & (mask - 1)
        neighbors_in_prev = (prev_mask & adj[v]).bit_count()
        cut[mask] = cut[prev_mask] + deg[v] - 2 * neighbors_in_prev

    for k in range(n):
        for mask in by_popcount[k]:
            current_cost = dp[mask]
            if current_cost > B:
                continue
            add_cut = cut[mask]
            # Try adding each unused vertex
            unused = ((1 << n) - 1) ^ mask
            while unused:
                lsb = unused & -unused
                v = lsb.bit_length() - 1
                unused ^= lsb
                next_mask = mask | (1 << v)
                next_cost = current_cost + cut[next_mask]
                if next_cost < dp[next_mask]:
                    dp[next_mask] = next_cost
                    parent[next_mask] = v

    full_mask = (1 << n) - 1
    # Note: cut[full_mask] is 0, so dp[full_mask] is the exact total cost
    min_cost = dp[full_mask]

    if min_cost <= B:
        print("YES")
        order = []
        curr = full_mask
        while curr > 0:
            v = parent[curr]
            order.append(v)
            curr ^= 1 << v
        order.reverse()

        pos = [0] * n
        for bay_idx, v in enumerate(order):
            pos[v] = bay_idx + 1

        print(*(pos[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()
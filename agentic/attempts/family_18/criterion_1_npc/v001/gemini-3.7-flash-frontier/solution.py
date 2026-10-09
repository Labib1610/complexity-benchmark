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
            deg[u] += 1
            deg[v] += 1

    if n == 0:
        print("YES")
        print()
        return

    if n == 1:
        if B >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return

    # For n <= 20, exact DP
    if n <= 20:
        size = 1 << n
        dp = [float("inf")] * size
        parent = [-1] * size
        cut = [0] * size

        for mask in range(1, size):
            # Find the lowest set bit
            u = (mask & -mask).bit_length() - 1
            prev_mask = mask ^ (1 << u)
            # cut[mask] = cut[prev_mask] + deg[u] - 2 * (edges between u and prev_mask)
            edges_to_prev = (adj[u] & prev_mask).bit_count()
            cut[mask] = cut[prev_mask] + deg[u] - 2 * edges_to_prev

        dp[0] = 0

        for mask in range(size - 1):
            cur_cost = dp[mask]
            if cur_cost > B:
                continue
            # Try adding each unused vertex
            unused = ((size - 1) ^ mask)
            while unused:
                u = (unused & -unused).bit_length() - 1
                unused &= unused - 1
                nxt_mask = mask | (1 << u)
                nxt_cost = cur_cost + cut[nxt_mask]
                if nxt_cost < dp[nxt_mask]:
                    dp[nxt_mask] = nxt_cost
                    parent[nxt_mask] = u

        total_cost = dp[size - 1]
        if total_cost <= B:
            print("YES")
            ans = [0] * n
            curr = size - 1
            for pos in range(n, 0, -1):
                u = parent[curr]
                ans[u] = pos
                curr ^= 1 << u
            print(*(ans[i] for i in range(n)))
        else:
            print("NO")
    else:
        # Fallback for larger n (e.g. simulated annealing or greedy)
        import random

        best_perm = list(range(n))
        best_cost = float("inf")

        def calc_cost(p):
            pos = [0] * n
            for i, v in enumerate(p):
                pos[v] = i + 1
            cost = 0
            for u in range(n):
                for v in range(u + 1, n):
                    if (adj[u] >> v) & 1:
                        cost += abs(pos[u] - pos[v])
            return cost

        # Degree-based initial greedy
        perm = sorted(range(n), key=lambda x: -deg[x])
        c = calc_cost(perm)
        if c < best_cost:
            best_cost = c
            best_perm = list(perm)

        # Quick simulated annealing
        import time

        start_time = time.time()
        while time.time() - start_time < 4.0 and best_cost > B:
            perm = list(best_perm)
            for _ in range(500):
                i, j = random.sample(range(n), 2)
                perm[i], perm[j] = perm[j], perm[i]
                cost = calc_cost(perm)
                if cost < best_cost:
                    best_cost = cost
                    best_perm = list(perm)
                    if best_cost <= B:
                        break
                else:
                    perm[i], perm[j] = perm[j], perm[i]

        if best_cost <= B:
            print("YES")
            ans = [0] * n
            for i, v in enumerate(best_perm):
                ans[v] = i + 1
            print(*(ans[i] for i in range(n)))
        else:
            print("NO")


if __name__ == "__main__":
    solve()
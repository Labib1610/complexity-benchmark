import sys
from array import array

def output_order(order):
    n = len(order)
    pos = [0] * n
    for i, v in enumerate(order, 1):
        pos[v] = i
    print("YES")
    print(*pos)

def arrangement_cost(order, edges):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(abs(pos[u] - pos[v]) for u, v in edges)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj_list = [[] for _ in range(n)]
    edges = []

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        adj_list[u].append(v)
        adj_list[v].append(u)

    if n == 1:
        print("YES")
        print(1)
        return

    if budget < n - 1:
        print("NO")
        return

    # Paths attain the absolute lower bound n - 1.
    if max(map(len, adj_list)) <= 2:
        start = next(v for v in range(n) if len(adj_list[v]) == 1)
        order = []
        prev = -1
        cur = start
        while cur != -1:
            order.append(cur)
            nxt = -1
            for v in adj_list[cur]:
                if v != prev:
                    nxt = v
                    break
            prev, cur = cur, nxt
        output_order(order)
        return

    # Try a few inexpensive arrangements first.
    candidates = [list(range(n))]

    roots = {0, max(range(n), key=lambda x: len(adj_list[x]))}
    for root in roots:
        for reverse_degree in (False, True):
            order = []
            stack = [(root, -1)]
            while stack:
                u, parent = stack.pop()
                order.append(u)
                children = [v for v in adj_list[u] if v != parent]
                children.sort(key=lambda x: len(adj_list[x]),
                              reverse=not reverse_degree)
                for v in reversed(children):
                    stack.append((v, u))
            candidates.append(order)

    for order in candidates:
        if arrangement_cost(order, edges) <= budget:
            output_order(order)
            return

    # Exact subset dynamic programming:
    # Every edge contributes once for each prefix cut separating its endpoints.
    if n > 23:
        print("NO")
        return

    size = 1 << n
    full = size - 1
    adj_mask = [0] * n
    degree = [0] * n
    for u, v in edges:
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        degree[u] += 1
        degree[v] += 1

    inf = budget + 1
    dp = array('I', [inf]) * size
    cut = array('B' if n <= 256 else 'H', [0]) * size
    parent = array('B', [0]) * size
    dp[0] = 0

    dp_local = dp
    cut_local = cut
    parent_local = parent
    adj_local = adj_mask
    degree_local = degree
    inf_local = inf

    for mask in range(1, size):
        low = mask & -mask
        v0 = low.bit_length() - 1
        rest = mask ^ low
        c = cut_local[rest] + degree_local[v0] - 2 * (
            adj_local[v0] & rest
        ).bit_count()
        cut_local[mask] = c

        x = mask
        best = inf_local
        best_v = v0
        while x:
            bit = x & -x
            val = dp_local[mask ^ bit]
            if val < best:
                best = val
                best_v = bit.bit_length() - 1
            x ^= bit

        value = best + c
        if value > inf_local:
            value = inf_local
        dp_local[mask] = value
        parent_local[mask] = best_v

    if dp_local[full] > budget:
        print("NO")
        return

    order = [0] * n
    mask = full
    for i in range(n - 1, -1, -1):
        v = parent_local[mask]
        order[i] = v
        mask ^= 1 << v

    output_order(order)

if __name__ == "__main__":
    main()
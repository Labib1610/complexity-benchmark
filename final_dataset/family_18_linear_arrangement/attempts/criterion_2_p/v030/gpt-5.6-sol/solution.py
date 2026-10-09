import sys
from array import array
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    budget = next(it)

    adj_mask = [0] * n
    graph = [[] for _ in range(n)]
    degree = [0] * n
    edges = []

    identity_cost = 0
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        identity_cost += abs(u - v)

    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    # A valid lower bound obtained independently at every vertex.
    lower_twice = 0
    for d in degree:
        lower_twice += ((d + 1) * (d + 1)) // 4
    lower_bound = (lower_twice + 1) // 2

    if budget < lower_bound:
        print("NO")
        return

    # Quickly try a center-out arrangement. This is especially effective for
    # high-degree trees and can avoid the exponential DP for generous budgets.
    if n > 0:
        root = max(range(n), key=degree.__getitem__)
        bfs = []
        seen = [False] * n
        seen[root] = True
        q = deque([root])

        while q:
            v = q.popleft()
            bfs.append(v)
            for to in graph[v]:
                if not seen[to]:
                    seen[to] = True
                    q.append(to)

        slots = []
        mid = n // 2
        slots.append(mid)
        distance = 1
        while len(slots) < n:
            left = mid - distance
            right = mid + distance
            if left >= 0:
                slots.append(left)
            if right < n and len(slots) < n:
                slots.append(right)
            distance += 1

        heuristic_pos = [0] * n
        for v, slot in zip(bfs, slots):
            heuristic_pos[v] = slot

        heuristic_cost = 0
        for u, v in edges:
            heuristic_cost += abs(heuristic_pos[u] - heuristic_pos[v])

        if heuristic_cost <= budget:
            print("YES")
            print(*(p + 1 for p in heuristic_pos))
            return

    # Subset DP:
    # cut[S] is the number of edges crossing between S and V \ S.
    # dp[S] is the minimum sum of cut sizes over all prefixes ending at S.
    # Thus dp[S] = cut[S] + min(dp[S \ {v}]).
    size = 1 << n
    max_value = 0xFFFFFFFF
    limit = min(budget, max_value - 1)

    cut_type = 'B' if m <= 255 else ('H' if m <= 65535 else 'I')
    cut = array(cut_type, [0]) * size
    dp = array('I', [max_value]) * size
    parent_type = 'B' if n <= 255 else 'H'
    parent = array(parent_type, [0]) * size
    dp[0] = 0

    dp_local = dp
    cut_local = cut
    parent_local = parent
    masks_local = adj_mask
    degrees_local = degree
    inf = max_value

    for mask in range(1, size):
        first_bit = mask & -mask
        first_vertex = first_bit.bit_length() - 1
        previous = mask ^ first_bit

        crossing = (
            cut_local[previous]
            + degrees_local[first_vertex]
            - 2 * ((masks_local[first_vertex] & previous).bit_count())
        )
        cut_local[mask] = crossing

        bits = mask
        best = inf
        best_vertex = 0

        while bits:
            bit = bits & -bits
            predecessor_value = dp_local[mask ^ bit]
            if predecessor_value < best:
                best = predecessor_value
                best_vertex = bit.bit_length() - 1
            bits ^= bit

        if best != inf:
            value = best + crossing
            if value <= limit:
                dp_local[mask] = value
                parent_local[mask] = best_vertex

    full = size - 1
    if dp[full] == max_value:
        print("NO")
        return

    positions = [0] * n
    mask = full
    position = n

    while mask:
        vertex = parent[mask]
        positions[vertex] = position
        position -= 1
        mask ^= 1 << vertex

    print("YES")
    print(*positions)

if __name__ == "__main__":
    main()
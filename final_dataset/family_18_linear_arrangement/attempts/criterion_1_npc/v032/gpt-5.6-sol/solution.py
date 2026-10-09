import sys
from array import array
from collections import deque

INF = (1 << 63) - 1
DENSE_LIMIT = 21


def arrangement_cost(order, edges):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)


def cuthill_mckee_order(n, adj):
    seen = bytearray(n)
    result = []

    starts = sorted(range(n), key=lambda v: (len(adj[v]), v))
    for start in starts:
        if seen[start]:
            continue
        seen[start] = 1
        q = deque([start])
        while q:
            v = q.popleft()
            result.append(v)
            neighbors = [u for u in adj[v] if not seen[u]]
            neighbors.sort(key=lambda u: (len(adj[u]), u))
            for u in neighbors:
                if not seen[u]:
                    seen[u] = 1
                    q.append(u)
    return result


def solve_component(vertices, adj, cap):
    k = len(vertices)
    if k == 1:
        return [vertices[0]], 0

    index = {v: i for i, v in enumerate(vertices)}
    local_neighbors = [[] for _ in range(k)]
    degrees = [0] * k
    edge_weight = 0
    simple = True

    for i, v in enumerate(vertices):
        for u, w in adj[v].items():
            j = index.get(u)
            if j is not None:
                local_neighbors[i].append((j, w))
                degrees[i] += w
                if w != 1:
                    simple = False
                if i < j:
                    edge_weight += w

    if edge_weight > cap:
        return None, None

    adj_masks = None
    if simple:
        adj_masks = [0] * k
        for i in range(k):
            mask = 0
            for j, _ in local_neighbors[i]:
                mask |= 1 << j
            adj_masks[i] = mask

    if k <= DENSE_LIMIT:
        size = 1 << k
        full = size - 1

        dp = array('q', [INF]) * size
        cuts = array('q', [0]) * size
        remaining_edges = array('q', [0]) * size
        parent = bytearray(size)

        dp[0] = 0
        remaining_edges[0] = edge_weight

        for mask in range(1, size):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit

            if simple:
                connected_to_prefix = (adj_masks[i] & prev).bit_count()
            else:
                connected_to_prefix = 0
                for j, w in local_neighbors[i]:
                    if prev & (1 << j):
                        connected_to_prefix += w

            cut_value = cuts[prev] + degrees[i] - 2 * connected_to_prefix
            rem_value = remaining_edges[prev] - (degrees[i] - connected_to_prefix)
            cuts[mask] = cut_value
            remaining_edges[mask] = rem_value

            best = INF
            best_vertex = 0
            bits = mask
            while bits:
                b = bits & -bits
                j = b.bit_length() - 1
                val = dp[mask ^ b]
                if val < best:
                    best = val
                    best_vertex = j
                bits ^= b

            if best != INF:
                value = best + cut_value
                if value <= cap and value + rem_value <= cap:
                    dp[mask] = value
                    parent[mask] = best_vertex

        if dp[full] == INF:
            return None, None

        reverse_order = []
        mask = full
        while mask:
            i = parent[mask]
            reverse_order.append(vertices[i])
            mask ^= 1 << i
        reverse_order.reverse()
        return reverse_order, dp[full]

    full = (1 << k) - 1
    current = {0: (0, 0, edge_weight)}
    parent = {}

    for _ in range(k):
        nxt = {}
        for mask, (cost, cut_value, rem_value) in current.items():
            available = full ^ mask
            bits = available
            while bits:
                bit = bits & -bits
                i = bit.bit_length() - 1
                new_mask = mask | bit

                if simple:
                    connected_to_prefix = (adj_masks[i] & mask).bit_count()
                else:
                    connected_to_prefix = 0
                    for j, w in local_neighbors[i]:
                        if mask & (1 << j):
                            connected_to_prefix += w

                new_cut = cut_value + degrees[i] - 2 * connected_to_prefix
                new_rem = rem_value - (degrees[i] - connected_to_prefix)
                new_cost = cost + new_cut

                if new_cost <= cap and new_cost + new_rem <= cap:
                    old = nxt.get(new_mask)
                    if old is None or new_cost < old[0]:
                        nxt[new_mask] = (new_cost, new_cut, new_rem)
                        parent[new_mask] = i

                bits ^= bit

        current = nxt
        if not current:
            return None, None

    final_state = current.get(full)
    if final_state is None:
        return None, None

    reverse_order = []
    mask = full
    while mask:
        i = parent[mask]
        reverse_order.append(vertices[i])
        mask ^= 1 << i
    reverse_order.reverse()
    return reverse_order, final_state[0]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]
    edges = []

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        adj[u][v] = adj[u].get(v, 0) + 1
        adj[v][u] = adj[v].get(u, 0) + 1

    for u in range(n):
        for v, w in adj[u].items():
            if u < v:
                edges.append((u, v, w))

    lower_bound = sum(w for _, _, w in edges)
    if budget < lower_bound:
        print("NO")
        return

    identity = list(range(n))
    if arrangement_cost(identity, edges) <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    heuristic = cuthill_mckee_order(n, adj)
    if arrangement_cost(heuristic, edges) <= budget:
        positions = [0] * n
        for slot, v in enumerate(heuristic, 1):
            positions[v] = slot
        print("YES")
        print(*positions)
        return

    seen = bytearray(n)
    components = []

    for start in range(n):
        if seen[start]:
            continue
        seen[start] = 1
        stack = [start]
        vertices = []
        edge_sum_twice = 0

        while stack:
            v = stack.pop()
            vertices.append(v)
            edge_sum_twice += sum(adj[v].values())
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = 1
                    stack.append(u)

        components.append((vertices, edge_sum_twice // 2))

    components.sort(key=lambda x: (-len(x[0]), -x[1]))

    remaining_lower = sum(weight for _, weight in components)
    total_cost = 0
    final_order = []

    for vertices, component_lower in components:
        remaining_lower -= component_lower
        cap = budget - total_cost - remaining_lower
        if cap < component_lower:
            print("NO")
            return

        order, cost = solve_component(vertices, adj, cap)
        if order is None:
            print("NO")
            return

        final_order.extend(order)
        total_cost += cost

    if total_cost > budget:
        print("NO")
        return

    positions = [0] * n
    for slot, v in enumerate(final_order, 1):
        positions[v] = slot

    print("YES")
    print(*positions)


if __name__ == "__main__":
    main()
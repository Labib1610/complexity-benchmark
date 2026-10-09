import sys
from array import array

def arrangement_cost(order, edges):
    pos = {v: i for i, v in enumerate(order)}
    return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)

def solve_component(vertices, edges, allowed):
    k = len(vertices)
    if k <= 1:
        return 0, vertices[:]

    index = {v: i for i, v in enumerate(vertices)}
    neighbors = [[] for _ in range(k)]
    degree_top = [0] * k
    degree_weight = [0] * k
    total_weight = 0
    all_unit = True

    local_edges = []
    for u, v, w in edges:
        a = index[u]
        b = index[v]
        local_edges.append((a, b, w))
        neighbors[a].append((b, w))
        neighbors[b].append((a, w))
        degree_top[a] += 1
        degree_top[b] += 1
        degree_weight[a] += w
        degree_weight[b] += w
        total_weight += w
        if w != 1:
            all_unit = False

    if total_weight > allowed:
        return None

    # Path
    if max(degree_top) <= 2 and sum(d == 1 for d in degree_top) == 2:
        start = next(i for i, d in enumerate(degree_top) if d == 1)
        order_idx = []
        prev = -1
        cur = start
        while cur != -1:
            order_idx.append(cur)
            nxt = -1
            for x, _ in neighbors[cur]:
                if x != prev:
                    nxt = x
                    break
            prev, cur = cur, nxt
        return total_weight, [vertices[i] for i in order_idx]

    # Cycle
    if all(d == 2 for d in degree_top):
        a, b, min_w = min(local_edges, key=lambda e: e[2])
        order_idx = [a]
        prev = b
        cur = a
        while True:
            nxt = -1
            for x, _ in neighbors[cur]:
                if x != prev:
                    nxt = x
                    break
            if nxt == b:
                break
            order_idx.append(nxt)
            prev, cur = cur, nxt
        order_idx.append(b)
        cost = total_weight + min_w * (k - 2)
        if cost > allowed:
            return None
        return cost, [vertices[i] for i in order_idx]

    # Star
    center = -1
    for i, d in enumerate(degree_top):
        if d == k - 1:
            center = i
            break
    if center != -1 and all(i == center or degree_top[i] == 1 for i in range(k)):
        center_pos = (k - 1) // 2
        available = [p for p in range(k) if p != center_pos]
        available.sort(key=lambda p: (abs(p - center_pos), p))
        leaves = [(w, x) for x, w in neighbors[center]]
        leaves.sort(reverse=True)

        order_idx = [-1] * k
        order_idx[center_pos] = center
        cost = 0
        for (w, leaf), p in zip(leaves, available):
            order_idx[p] = leaf
            cost += w * abs(p - center_pos)

        if cost > allowed:
            return None
        return cost, [vertices[i] for i in order_idx]

    # Unweighted complete graph
    if all_unit and len(local_edges) == k * (k - 1) // 2:
        cost = k * (k * k - 1) // 6
        if cost > allowed:
            return None
        return cost, vertices[:]

    # Exact subset DP.
    size = 1 << k
    if allowed < 0:
        return None

    max_cut = total_weight
    cut_type = 'I' if max_cut <= 0xFFFFFFFF else 'Q'
    dp_type = 'I' if allowed + 1 <= 0xFFFFFFFF else 'Q'
    inf = allowed + 1

    cuts = array(cut_type, [0]) * size
    dp = array(dp_type, [inf]) * size
    dp[0] = 0

    simple = all_unit
    adjacency_masks = [0] * k
    if simple:
        for i in range(k):
            mask = 0
            for j, _ in neighbors[i]:
                mask |= 1 << j
            adjacency_masks[i] = mask

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit

        if simple:
            crossing_to_rest = (adjacency_masks[v] & rest).bit_count()
        else:
            crossing_to_rest = 0
            for u, w in neighbors[v]:
                if rest & (1 << u):
                    crossing_to_rest += w

        cuts[mask] = cuts[rest] + degree_weight[v] - 2 * crossing_to_rest

        best = inf
        bits = mask
        while bits:
            last_bit = bits & -bits
            prev = mask ^ last_bit
            base = dp[prev]
            if base < inf:
                value = base + cuts[prev]
                if value < best:
                    best = value
            bits ^= last_bit
        if best < inf:
            dp[mask] = best

    full = size - 1
    optimum = dp[full]
    if optimum > allowed:
        return None

    reversed_order = []
    mask = full
    while mask:
        target = dp[mask]
        bits = mask
        found = False
        while bits:
            bit = bits & -bits
            v = bit.bit_length() - 1
            prev = mask ^ bit
            if dp[prev] < inf and dp[prev] + cuts[prev] == target:
                reversed_order.append(v)
                mask = prev
                found = True
                break
            bits ^= bit
        if not found:
            return None

    reversed_order.reverse()
    return optimum, [vertices[i] for i in reversed_order]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    edge_weights = {}
    identity_cost = 0
    p = 3

    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        identity_cost += abs(u - v)
        if u == v:
            continue
        if u > v:
            u, v = v, u
        edge_weights[(u, v)] = edge_weights.get((u, v), 0) + 1

    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    graph = [[] for _ in range(n)]
    weighted_edges = []
    total_weight = 0

    for (u, v), w in edge_weights.items():
        graph[u].append(v)
        graph[v].append(u)
        weighted_edges.append((u, v, w))
        total_weight += w

    if total_weight > budget:
        print("NO")
        return

    visited = bytearray(n)
    components = []
    isolated = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = 1
        if not graph[start]:
            isolated.append(start)
            continue

        stack = [start]
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = 1
                    stack.append(u)
        components.append(vertices)

    component_id = [-1] * n
    for cid, vertices in enumerate(components):
        for v in vertices:
            component_id[v] = cid

    component_edges = [[] for _ in components]
    component_baseline = [0] * len(components)
    for u, v, w in weighted_edges:
        cid = component_id[u]
        component_edges[cid].append((u, v, w))
        component_baseline[cid] += w

    remaining_baseline = total_weight
    total_cost = 0
    final_order = []

    # Smaller components first usually reduces peak memory sooner on impossible cases.
    order_of_components = sorted(range(len(components)), key=lambda i: len(components[i]))

    solved_orders = [None] * len(components)
    for cid in order_of_components:
        base = component_baseline[cid]
        remaining_baseline -= base
        allowed = budget - total_cost - remaining_baseline

        result = solve_component(
            components[cid],
            component_edges[cid],
            allowed
        )
        if result is None:
            print("NO")
            return

        cost, order = result
        total_cost += cost
        solved_orders[cid] = order

    if total_cost > budget:
        print("NO")
        return

    for cid in range(len(components)):
        final_order.extend(solved_orders[cid])
    final_order.extend(isolated)

    positions = [0] * n
    for pos, vertex in enumerate(final_order, 1):
        positions[vertex] = pos

    print("YES")
    print(*positions)


if __name__ == "__main__":
    main()
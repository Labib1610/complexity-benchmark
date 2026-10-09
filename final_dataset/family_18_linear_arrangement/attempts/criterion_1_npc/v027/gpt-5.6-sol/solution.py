import sys
from array import array
from collections import deque


def score_order(order, adjacency):
    pos = {v: i for i, v in enumerate(order)}
    total = 0
    for u in order:
        pu = pos[u]
        for v, w in adjacency[u].items():
            if u < v:
                total += w * abs(pu - pos[v])
    return total


def heuristic_order(component, adjacency):
    if len(component) <= 1:
        return component[:]

    degrees = {v: len(adjacency[v]) for v in component}
    candidates = [component[:]]
    starts = sorted(component, key=lambda v: (degrees[v], v))
    selected_starts = starts[:3]
    if starts[-1] not in selected_starts:
        selected_starts.append(starts[-1])

    for start in selected_starts:
        seen = {start}
        q = deque([start])
        bfs = []
        while q:
            u = q.popleft()
            bfs.append(u)
            neighbors = sorted(
                (v for v in adjacency[u] if v not in seen),
                key=lambda v: (degrees[v], v)
            )
            for v in neighbors:
                seen.add(v)
                q.append(v)
        candidates.append(bfs)

        seen = {start}
        stack = [start]
        dfs = []
        while stack:
            u = stack.pop()
            dfs.append(u)
            neighbors = sorted(
                (v for v in adjacency[u] if v not in seen),
                key=lambda v: (degrees[v], v),
                reverse=True
            )
            for v in neighbors:
                seen.add(v)
                stack.append(v)
        candidates.append(dfs)

    return min(candidates, key=lambda order: score_order(order, adjacency))


def exact_special_order(component, adjacency):
    k = len(component)
    if k <= 1:
        return component[:], 0

    unique_edges = sum(len(adjacency[v]) for v in component) // 2
    weighted_edges = sum(sum(adjacency[v].values()) for v in component) // 2

    # A connected graph of maximum degree at most two is a path unless it is a cycle.
    if unique_edges == k - 1 and all(len(adjacency[v]) <= 2 for v in component):
        start = next(v for v in component if len(adjacency[v]) == 1)
        order = []
        prev = -1
        cur = start
        while True:
            order.append(cur)
            nxt = [v for v in adjacency[cur] if v != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
        return order, weighted_edges

    # Every ordering of an unweighted clique has the same cost.
    if unique_edges == k * (k - 1) // 2:
        all_unweighted = all(
            w == 1 for v in component for w in adjacency[v].values()
        )
        if all_unweighted:
            return component[:], k * (k * k - 1) // 6

    return None


def array_type(max_value):
    if max_value <= 255:
        return 'B'
    if max_value <= 65535:
        return 'H'
    if max_value <= 4294967295:
        return 'I'
    return 'Q'


def exact_component_order(component, adjacency, cap):
    special = exact_special_order(component, adjacency)
    if special is not None:
        order, cost = special
        return (order, cost) if cost <= cap else None

    k = len(component)
    index = {v: i for i, v in enumerate(component)}
    adj_masks = [0] * k
    weighted_neighbors = [[] for _ in range(k)]
    weighted_degree = [0] * k
    simple = True
    component_weight = 0

    for i, u in enumerate(component):
        mask = 0
        for v, w in adjacency[u].items():
            j = index[v]
            mask |= 1 << j
            weighted_neighbors[i].append((1 << j, w))
            weighted_degree[i] += w
            if w != 1:
                simple = False
            if i < j:
                component_weight += w
        adj_masks[i] = mask

    if component_weight > cap:
        return None

    size = 1 << k
    inf = cap + 1
    cut_type = array_type(component_weight)
    dp_type = array_type(inf)

    cuts = array(cut_type, [0]) * size
    dp = array(dp_type, [inf]) * size
    dp[0] = 0

    for mask in range(1, size):
        bit = mask & -mask
        i = bit.bit_length() - 1
        previous = mask ^ bit

        if simple:
            internal = (adj_masks[i] & previous).bit_count()
        else:
            internal = 0
            for neighbor_bit, weight in weighted_neighbors[i]:
                if previous & neighbor_bit:
                    internal += weight

        cut = cuts[previous] + weighted_degree[i] - 2 * internal
        cuts[mask] = cut

        best = inf
        remaining = mask
        while remaining:
            b = remaining & -remaining
            value = dp[mask ^ b]
            if value < best:
                best = value
            remaining ^= b

        value = best + cut
        if value <= cap:
            dp[mask] = value

    full = size - 1
    if dp[full] == inf:
        return None

    reverse_order = []
    mask = full
    while mask:
        target = dp[mask] - cuts[mask]
        remaining = mask
        chosen = 0
        while remaining:
            bit = remaining & -remaining
            if dp[mask ^ bit] == target:
                chosen = bit
                break
            remaining ^= bit
        reverse_order.append(component[chosen.bit_length() - 1])
        mask ^= chosen

    reverse_order.reverse()
    return reverse_order, dp[full]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adjacency = [dict() for _ in range(n)]
    effective_edges = 0

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        adjacency[u][v] = adjacency[u].get(v, 0) + 1
        adjacency[v][u] = adjacency[v].get(u, 0) + 1
        effective_edges += 1

    if effective_edges > budget:
        print("NO")
        return

    visited = [False] * n
    components = []
    isolates = []

    for start in range(n):
        if visited[start]:
            continue
        if not adjacency[start]:
            visited[start] = True
            isolates.append(start)
            continue

        visited[start] = True
        stack = [start]
        component = []
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adjacency[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        components.append(component)

    # First try inexpensive constructions, which also handle large easy instances.
    heuristic_orders = []
    heuristic_cost = 0
    for component in components:
        special = exact_special_order(component, adjacency)
        if special is not None:
            order, cost = special
        else:
            order = heuristic_order(component, adjacency)
            cost = score_order(order, adjacency)
        heuristic_orders.append(order)
        heuristic_cost += cost

    if heuristic_cost <= budget:
        final_order = []
        for order in heuristic_orders:
            final_order.extend(order)
        final_order.extend(isolates)

        answer = [0] * n
        for position, vertex in enumerate(final_order, 1):
            answer[vertex] = position
        print("YES")
        print(*answer)
        return

    exact_orders = []
    exact_total = 0

    for component in components:
        component_weight = (
            sum(sum(adjacency[v].values()) for v in component) // 2
        )
        cap = budget - (effective_edges - component_weight)
        if cap < component_weight:
            print("NO")
            return

        result = exact_component_order(component, adjacency, cap)
        if result is None:
            print("NO")
            return

        order, cost = result
        exact_orders.append(order)
        exact_total += cost
        if exact_total > budget:
            print("NO")
            return

    if exact_total > budget:
        print("NO")
        return

    final_order = []
    for order in exact_orders:
        final_order.extend(order)
    final_order.extend(isolates)

    answer = [0] * n
    for position, vertex in enumerate(final_order, 1):
        answer[vertex] = position

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()
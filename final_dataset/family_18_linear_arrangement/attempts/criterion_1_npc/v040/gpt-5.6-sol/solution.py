import sys
from array import array
from collections import deque

def exact_order(vertices, adjacency, budget):
    k = len(vertices)
    if k <= 1:
        return vertices[:], 0

    index = {v: i for i, v in enumerate(vertices)}
    masks = [0] * k
    for i, v in enumerate(vertices):
        mask = 0
        for u in adjacency[v]:
            j = index.get(u)
            if j is not None:
                mask |= 1 << j
        masks[i] = mask

    size = 1 << k
    cuts = array('i', [0]) * size
    inf = budget + 1
    dp = array('q', [inf]) * size
    dp[0] = 0

    for s in range(1, size):
        low = s & -s
        i = low.bit_length() - 1
        prev = s ^ low
        cut = cuts[prev] + masks[i].bit_count() - 2 * (masks[i] & prev).bit_count()
        cuts[s] = cut

        t = s
        best = inf
        while t:
            bit = t & -t
            value = dp[s ^ bit]
            if value < best:
                best = value
            t ^= bit

        value = best + cut
        if value < inf:
            dp[s] = value

    full = size - 1
    optimum = dp[full]
    if optimum > budget:
        return None, optimum

    reverse_order = []
    s = full
    while s:
        target = dp[s] - cuts[s]
        t = s
        chosen = 0
        while t:
            bit = t & -t
            if dp[s ^ bit] == target:
                chosen = bit
                break
            t ^= bit
        if chosen == 0:
            return None, inf
        reverse_order.append(vertices[chosen.bit_length() - 1])
        s ^= chosen

    reverse_order.reverse()
    return reverse_order, optimum


def path_or_cycle_order(vertices, adjacency, is_cycle):
    if len(vertices) <= 1:
        return vertices[:]

    if is_cycle:
        start = vertices[0]
    else:
        start = next(v for v in vertices if len(adjacency[v]) <= 1)

    order = []
    previous = -1
    current = start

    while True:
        order.append(current)
        next_vertex = -1
        for u in adjacency[current]:
            if u != previous and (not is_cycle or len(order) == 1 or u != start):
                next_vertex = u
                break

        if next_vertex == -1 or len(order) == len(vertices):
            break
        previous, current = current, next_vertex

    return order


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adjacency = [set() for _ in range(n)]
    edges = []
    p = 3

    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        if v not in adjacency[u]:
            adjacency[u].add(v)
            adjacency[v].add(u)
            edges.append((u, v))

    identity_cost = sum(abs(u - v) for u, v in edges)
    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    edge_count = len(edges)
    if edge_count > budget:
        print("NO")
        return

    visited = [False] * n
    components = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        queue = [start]
        component = []
        while queue:
            v = queue.pop()
            component.append(v)
            for u in adjacency[v]:
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
        components.append(component)

    result_orders = [None] * len(components)
    unresolved = []
    total_cost = 0
    unresolved_edge_lower_bound = 0

    for ci, component in enumerate(components):
        k = len(component)
        component_edges = sum(len(adjacency[v]) for v in component) // 2

        if k == 1:
            result_orders[ci] = component[:]
            continue

        degrees = [len(adjacency[v]) for v in component]
        max_degree = max(degrees)

        if component_edges == k - 1 and max_degree <= 2:
            order = path_or_cycle_order(component, adjacency, False)
            result_orders[ci] = order
            total_cost += k - 1
        elif component_edges == k and all(d == 2 for d in degrees):
            order = path_or_cycle_order(component, adjacency, True)
            result_orders[ci] = order
            total_cost += 2 * (k - 1)
        elif component_edges == k * (k - 1) // 2:
            result_orders[ci] = component[:]
            total_cost += k * (k * k - 1) // 6
        elif component_edges == k - 1 and max_degree == k - 1:
            center = next(v for v in component if len(adjacency[v]) == k - 1)
            leaves = [v for v in component if v != center]
            left_count = (k - 1) // 2
            result_orders[ci] = leaves[:left_count] + [center] + leaves[left_count:]
            total_cost += (k * k) // 4
        else:
            unresolved.append((ci, component, component_edges))
            unresolved_edge_lower_bound += component_edges

    if total_cost + unresolved_edge_lower_bound > budget:
        print("NO")
        return

    unresolved.sort(key=lambda item: len(item[1]), reverse=True)

    for ci, component, component_edges in unresolved:
        unresolved_edge_lower_bound -= component_edges
        component_budget = budget - total_cost - unresolved_edge_lower_bound

        order, cost = exact_order(component, adjacency, component_budget)
        if order is None:
            print("NO")
            return

        result_orders[ci] = order
        total_cost += cost

    if total_cost > budget:
        print("NO")
        return

    sequence = []
    for order in result_orders:
        sequence.extend(order)

    positions = [0] * n
    for bay, vertex in enumerate(sequence, 1):
        positions[vertex] = bay

    actual_cost = sum(abs(positions[u] - positions[v]) for u, v in edges)
    if actual_cost > budget:
        print("NO")
        return

    print("YES")
    print(*positions)


if __name__ == "__main__":
    solve()
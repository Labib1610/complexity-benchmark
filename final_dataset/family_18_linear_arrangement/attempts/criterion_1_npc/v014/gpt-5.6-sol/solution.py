import sys
from array import array
from collections import deque


def positions_from_order(order, n):
    pos = [0] * n
    for i, v in enumerate(order, 1):
        pos[v] = i
    return pos


def arrangement_cost(pos, graph):
    total = 0
    for u, neighbors in enumerate(graph):
        pu = pos[u]
        for v in neighbors:
            total += abs(pu - pos[v])
    return total // 2


def solve_component(component, graph):
    k = len(component)
    if k == 1:
        return component, 0

    # Low-degree vertices receive low local indices, which also makes the
    # weighted cut computation cheaper when parallel edges are present.
    vertices = sorted(component, key=lambda x: len(graph[x]))
    local_index = {v: i for i, v in enumerate(vertices)}

    local_adj = [[] for _ in range(k)]
    simple = True

    for i, v in enumerate(vertices):
        row = [local_index[to] for to in graph[v]]
        local_adj[i] = row
        if len(row) != len(set(row)):
            simple = False

    degrees = [len(row) for row in local_adj]

    if simple:
        masks = [0] * k
        for i, row in enumerate(local_adj):
            mask = 0
            for j in row:
                mask |= 1 << j
            masks[i] = mask

    size = 1 << k
    cuts = array('q', [0]) * size
    dp = array('q', [0]) * size

    edge_count = sum(degrees) // 2
    infinity = edge_count * max(1, k - 1) + 1

    if simple:
        for subset in range(1, size):
            bit = subset & -subset
            v = bit.bit_length() - 1
            previous = subset ^ bit
            cut = cuts[previous] + degrees[v] - 2 * (
                masks[v] & previous
            ).bit_count()
            cuts[subset] = cut

            best = infinity
            remaining = subset
            while remaining:
                b = remaining & -remaining
                value = dp[subset ^ b]
                if value < best:
                    best = value
                remaining ^= b
            dp[subset] = best + cut
    else:
        for subset in range(1, size):
            bit = subset & -subset
            v = bit.bit_length() - 1
            previous = subset ^ bit

            inside = 0
            for neighbor in local_adj[v]:
                inside += (previous >> neighbor) & 1

            cut = cuts[previous] + degrees[v] - 2 * inside
            cuts[subset] = cut

            best = infinity
            remaining = subset
            while remaining:
                b = remaining & -remaining
                value = dp[subset ^ b]
                if value < best:
                    best = value
                remaining ^= b
            dp[subset] = best + cut

    minimum_cost = dp[size - 1]

    subset = size - 1
    reversed_order = []
    while subset:
        best_bit = 0
        best_value = infinity
        remaining = subset
        while remaining:
            bit = remaining & -remaining
            value = dp[subset ^ bit]
            if value < best_value:
                best_value = value
                best_bit = bit
            remaining ^= bit

        local_vertex = best_bit.bit_length() - 1
        reversed_order.append(vertices[local_vertex])
        subset ^= best_bit

    reversed_order.reverse()
    return reversed_order, minimum_cost


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]

    identity_cost = 0
    non_loop_edges = 0
    index = 3

    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2

        if u == v:
            continue

        graph[u].append(v)
        graph[v].append(u)
        identity_cost += abs(u - v)
        non_loop_edges += 1

    if non_loop_edges > budget:
        print("NO")
        return

    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    visited = bytearray(n)
    components = []

    for start in range(n):
        if visited[start]:
            continue

        visited[start] = 1
        stack = [start]
        component = []

        while stack:
            v = stack.pop()
            component.append(v)
            for to in graph[v]:
                if not visited[to]:
                    visited[to] = 1
                    stack.append(to)

        components.append(component)

    # Try a Cuthill-McKee-style ordering first. It can avoid exponential
    # optimization when the budget is permissive.
    heuristic_order = []
    for component in components:
        if len(component) == 1:
            heuristic_order.append(component[0])
            continue

        start = min(component, key=lambda x: len(graph[x]))
        seen = {start}
        queue = deque([start])

        while queue:
            v = queue.popleft()
            heuristic_order.append(v)
            candidates = [to for to in graph[v] if to not in seen]
            candidates.sort(key=lambda x: len(graph[x]))
            for to in candidates:
                if to not in seen:
                    seen.add(to)
                    queue.append(to)

    heuristic_pos = positions_from_order(heuristic_order, n)
    if arrangement_cost(heuristic_pos, graph) <= budget:
        print("YES")
        print(*(x + 1 for x in heuristic_pos))
        return

    optimal_order = []
    total_cost = 0

    for component in components:
        component_order, component_cost = solve_component(component, graph)
        total_cost += component_cost

        if total_cost > budget:
            print("NO")
            return

        optimal_order.extend(component_order)

    positions = positions_from_order(optimal_order, n)

    print("YES")
    print(*(x + 1 for x in positions))


if __name__ == "__main__":
    main()
import sys
from array import array


def solve_component(vertices, graph, budget):
    k = len(vertices)
    if k == 1:
        return vertices, 0

    index = {v: i for i, v in enumerate(vertices)}
    degree = [0] * k
    masks = [0] * k
    weighted_neighbors = [[] for _ in range(k)]
    simple = True
    edge_weight = 0

    for i, v in enumerate(vertices):
        for u, w in graph[v].items():
            j = index[u]
            degree[i] += w
            masks[i] |= 1 << j
            weighted_neighbors[i].append((j, w))
            if w != 1:
                simple = False
            if i < j:
                edge_weight += w

    if edge_weight > budget:
        return None, None

    size = 1 << k
    cap = budget + 1

    cuts = array('q', [0]) * size
    dp = array('q', [cap]) * size
    parent_type = 'B' if k <= 255 else 'H'
    parent = array(parent_type, [0]) * size
    dp[0] = 0

    cuts_local = cuts
    dp_local = dp
    parent_local = parent
    degree_local = degree
    masks_local = masks
    weighted_local = weighted_neighbors
    bit_count = int.bit_count

    for s in range(1, size):
        low = s & -s
        v = low.bit_length() - 1
        t = s ^ low

        if simple:
            internal = bit_count(masks_local[v] & t)
        else:
            internal = 0
            for u, w in weighted_local[v]:
                if t & (1 << u):
                    internal += w

        cut_value = cuts_local[t] + degree_local[v] - (internal << 1)
        cuts_local[s] = cut_value

        best = cap
        best_v = 0
        bits = s
        while bits:
            b = bits & -bits
            prev = dp_local[s ^ b]
            if prev < best:
                best = prev
                best_v = b.bit_length() - 1
            bits ^= b

        value = best + cut_value
        if value > budget:
            value = cap
        dp_local[s] = value
        parent_local[s] = best_v

    full = size - 1
    minimum = dp_local[full]
    if minimum > budget:
        return None, None

    reverse_order = []
    s = full
    while s:
        v = parent_local[s]
        reverse_order.append(vertices[v])
        s ^= 1 << v
    reverse_order.reverse()

    return reverse_order, minimum


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [dict() for _ in range(n)]

    total_weight = 0
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2

        if u == v:
            continue

        graph[u][v] = graph[u].get(v, 0) + 1
        graph[v][u] = graph[v].get(u, 0) + 1
        total_weight += 1

    if budget < 0 or total_weight > budget:
        print("NO")
        return

    visited = bytearray(n)
    components = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = 1
        if not graph[start]:
            components.append([start])
            continue

        stack = [start]
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = 1
                    stack.append(u)
        components.append(component)

    components.sort(key=len, reverse=True)

    remaining = budget
    full_order = []

    for component in components:
        order, cost = solve_component(component, graph, remaining)
        if order is None:
            print("NO")
            return
        full_order.extend(order)
        remaining -= cost

    positions = [0] * n
    for position, artifact in enumerate(full_order, 1):
        positions[artifact] = position

    print("YES")
    print(*positions)


if __name__ == "__main__":
    main()
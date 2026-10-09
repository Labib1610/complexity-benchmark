import sys
from array import array


def unsigned_type(max_value):
    if max_value <= 0xFF:
        return 'B'
    if max_value <= 0xFFFF:
        return 'H'
    if max_value <= 0xFFFFFFFF:
        return 'I'
    return 'Q'


def solve_component(vertices, graph, edge_count, limit):
    k = len(vertices)
    if k == 1:
        return 0, vertices

    if limit < edge_count:
        return None

    index = {v: i for i, v in enumerate(vertices)}
    masks = [0] * k
    neighbors = [[] for _ in range(k)]
    multigraph = False

    for i, v in enumerate(vertices):
        current = neighbors[i]
        mask = 0
        for u in graph[v]:
            j = index[u]
            current.append(j)
            mask |= 1 << j
        masks[i] = mask
        if len(current) != mask.bit_count():
            multigraph = True

    size = 1 << k
    cut_type = unsigned_type(edge_count)
    cuts = array(cut_type, [0]) * size

    inf = limit + 1
    dp_type = unsigned_type(inf)
    dp = array(dp_type, [inf]) * size
    parent = array('B', [0]) * size
    dp[0] = 0

    cuts_local = cuts
    dp_local = dp
    parent_local = parent
    masks_local = masks
    neighbors_local = neighbors

    for s in range(1, size):
        bit = s & -s
        v = bit.bit_length() - 1
        t = s ^ bit

        if multigraph:
            inside = 0
            for u in neighbors_local[v]:
                inside += (t >> u) & 1
            crossing = cuts_local[t] + len(neighbors_local[v]) - (inside << 1)
        else:
            crossing = (
                cuts_local[t]
                + masks_local[v].bit_count()
                - ((masks_local[v] & t).bit_count() << 1)
            )
        cuts_local[s] = crossing

        best = inf
        best_v = 0
        x = s
        while x:
            b = x & -x
            candidate = dp_local[s ^ b]
            if candidate < best:
                best = candidate
                best_v = b.bit_length() - 1
            x ^= b

        if best <= limit - crossing:
            dp_local[s] = best + crossing
            parent_local[s] = best_v

    full = size - 1
    minimum = dp_local[full]
    if minimum > limit:
        return None

    reverse_order = []
    s = full
    while s:
        v = parent_local[s]
        reverse_order.append(vertices[v])
        s ^= 1 << v
    reverse_order.reverse()

    return minimum, reverse_order


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    identity_cost = 0
    nonloop_edges = 0

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        graph[u].append(v)
        graph[v].append(u)
        identity_cost += abs(u - v)
        nonloop_edges += 1

    if budget < 0 or budget < nonloop_edges:
        print("NO")
        return

    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    visited = [False] * n
    components = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        stack = [start]
        vertices = []
        degree_sum = 0

        while stack:
            v = stack.pop()
            vertices.append(v)
            degree_sum += len(graph[v])
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        components.append((vertices, degree_sum // 2))

    components.sort(key=lambda item: len(item[0]), reverse=True)

    remaining_lower_bound = sum(edge_count for _, edge_count in components)
    total_cost = 0
    global_order = []

    for vertices, edge_count in components:
        remaining_lower_bound -= edge_count
        component_limit = budget - total_cost - remaining_lower_bound
        result = solve_component(vertices, graph, edge_count, component_limit)
        if result is None:
            print("NO")
            return

        component_cost, component_order = result
        total_cost += component_cost
        global_order.extend(component_order)

    positions = [0] * n
    for pos, vertex in enumerate(global_order, 1):
        positions[vertex] = pos

    print("YES")
    print(*positions)


if __name__ == "__main__":
    main()
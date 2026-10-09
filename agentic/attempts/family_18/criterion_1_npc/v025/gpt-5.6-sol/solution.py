import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    edges = []
    active = bytearray(n)
    identity_cost = 0
    nonloop_edges = 0

    idx = 3
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        if u == v:
            continue
        edges.append((u, v))
        active[u] = 1
        active[v] = 1
        union(u, v)
        identity_cost += abs(u - v)
        nonloop_edges += 1

    if budget < 0 or nonloop_edges > budget:
        print("NO")
        return

    if identity_cost <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    component_vertices = {}
    for v in range(n):
        if active[v]:
            r = find(v)
            component_vertices.setdefault(r, []).append(v)

    component_edges = {r: [] for r in component_vertices}
    for u, v in edges:
        component_edges[find(u)].append((u, v))

    components = []
    heuristic_order = []
    heuristic_cost = 0

    for r, vertices in component_vertices.items():
        vertices.sort()
        local_index = {v: i for i, v in enumerate(vertices)}
        comp_edges = component_edges[r]

        for u, v in comp_edges:
            heuristic_cost += abs(local_index[u] - local_index[v])

        heuristic_order.extend(vertices)
        components.append((vertices, comp_edges))

    isolated = [v for v in range(n) if not active[v]]
    heuristic_order.extend(isolated)

    if heuristic_cost <= budget:
        answer = [0] * n
        for pos, v in enumerate(heuristic_order, 1):
            answer[v] = pos
        print("YES")
        print(*answer)
        return

    components.sort(key=lambda x: len(x[0]))
    total_optimum = 0
    final_order = []

    for vertices, comp_edges in components:
        k = len(vertices)
        if k <= 1:
            final_order.extend(vertices)
            continue

        local_index = {v: i for i, v in enumerate(vertices)}
        weights = [[0] * k for _ in range(k)]
        degree = [0] * k

        for u, v in comp_edges:
            a = local_index[u]
            b = local_index[v]
            weights[a][b] += 1
            weights[b][a] += 1
            degree[a] += 1
            degree[b] += 1

        total_weight = len(comp_edges)
        states = 1 << k

        if total_weight <= 0xFFFF:
            cut_type = 'H'
        elif total_weight <= 0xFFFFFFFF:
            cut_type = 'I'
        else:
            cut_type = 'Q'

        max_component_cost = total_weight * (k - 1)
        if max_component_cost <= 0xFFFFFFFF:
            dp_type = 'I'
        else:
            dp_type = 'Q'

        try:
            cuts = array(cut_type, [0]) * states
            dp = array(dp_type, [0]) * states
        except (MemoryError, OverflowError):
            print("NO")
            return

        for mask in range(1, states):
            low = mask & -mask
            v = low.bit_length() - 1
            prev = mask ^ low

            connected_inside = 0
            x = prev
            row = weights[v]
            while x:
                bit = x & -x
                connected_inside += row[bit.bit_length() - 1]
                x ^= bit

            cut_value = cuts[prev] + degree[v] - 2 * connected_inside
            cuts[mask] = cut_value

            x = mask
            first = x & -x
            best = dp[mask ^ first]
            x ^= first
            while x:
                bit = x & -x
                value = dp[mask ^ bit]
                if value < best:
                    best = value
                x ^= bit
            dp[mask] = cut_value + best

        full = states - 1
        optimum = dp[full]
        total_optimum += optimum

        if total_optimum > budget:
            print("NO")
            return

        reversed_order = []
        mask = full
        while mask:
            target = dp[mask] - cuts[mask]
            x = mask
            chosen = -1
            while x:
                bit = x & -x
                if dp[mask ^ bit] == target:
                    chosen = bit.bit_length() - 1
                    break
                x ^= bit
            reversed_order.append(vertices[chosen])
            mask ^= 1 << chosen

        reversed_order.reverse()
        final_order.extend(reversed_order)

        del cuts
        del dp

    if total_optimum > budget:
        print("NO")
        return

    final_order.extend(isolated)
    answer = [0] * n
    for pos, v in enumerate(final_order, 1):
        answer[v] = pos

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()
import sys
from array import array


def main():
    input = sys.stdin.buffer.readline
    n, m, B = map(int, input().split())

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    weights = {}
    identity_cost = 0
    nonloop_edges = 0

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u == v:
            continue
        identity_cost += abs(u - v)
        nonloop_edges += 1
        if u > v:
            u, v = v, u
        key = (u, v)
        weights[key] = weights.get(key, 0) + 1
        union(u, v)

    if B < nonloop_edges:
        print("NO")
        return

    if identity_cost <= B:
        print("YES")
        print(*range(1, n + 1))
        return

    adjacency = [[] for _ in range(n)]
    degree = [0] * n
    for (u, v), w in weights.items():
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))
        degree[u] += w
        degree[v] += w

    components_map = {}
    for v in range(n):
        r = find(v)
        components_map.setdefault(r, []).append(v)
    components = list(components_map.values())

    def evaluate_positions(pos):
        total = 0
        for (u, v), w in weights.items():
            total += w * abs(pos[u] - pos[v])
            if total > B:
                return total
        return total

    # Try concatenating components and placing high-degree vertices centrally.
    candidate_positions = [0] * n
    offset = 0
    for comp in components:
        k = len(comp)
        ordered = sorted(comp, key=lambda x: (degree[x], x))
        slots = []
        left, right = 0, k - 1
        take_left = True
        while left <= right:
            if take_left:
                slots.append(left)
                left += 1
            else:
                slots.append(right)
                right -= 1
            take_left = not take_left

        local_order = [0] * k
        for vertex, slot in zip(ordered, slots):
            local_order[slot] = vertex
        for i, vertex in enumerate(local_order):
            candidate_positions[vertex] = offset + i + 1
        offset += k

    if evaluate_positions(candidate_positions) <= B:
        print("YES")
        print(*candidate_positions)
        return

    result_positions = [0] * n
    offset = 0
    optimum_so_far = 0

    for comp in components:
        k = len(comp)

        if k == 1:
            result_positions[comp[0]] = offset + 1
            offset += 1
            continue

        local_index = {v: i for i, v in enumerate(comp)}
        adj_mask = [0] * k
        weighted_degree = [0] * k
        extras = [[] for _ in range(k)]
        component_edge_weight = 0

        for i, u in enumerate(comp):
            for v, w in adjacency[u]:
                j = local_index[v]
                adj_mask[i] |= 1 << j
                weighted_degree[i] += w
                if w > 1:
                    extras[i].append((1 << j, w - 1))
                if u < v:
                    component_edge_weight += w

        remaining_budget = B - optimum_so_far
        if remaining_budget < component_edge_weight:
            print("NO")
            return

        states = 1 << k
        maximum_cost = component_edge_weight * (k - 1)
        cap = min(remaining_budget, maximum_cost)
        INF = cap + 1

        cuts = array('q', [0]) * states
        dp = array('q', [INF]) * states
        dp[0] = 0

        for mask in range(1, states):
            previous = mask & (mask - 1)
            added_bit = mask ^ previous
            v = added_bit.bit_length() - 1

            neighbours_inside = (adj_mask[v] & previous).bit_count()
            if extras[v]:
                for bit, extra_weight in extras[v]:
                    if previous & bit:
                        neighbours_inside += extra_weight

            cut_value = (
                cuts[previous]
                + weighted_degree[v]
                - 2 * neighbours_inside
            )
            cuts[mask] = cut_value

            best = INF
            bits = mask
            while bits:
                bit = bits & -bits
                value = dp[mask ^ bit] + cut_value
                if value < best:
                    best = value
                bits ^= bit

            if best < INF:
                dp[mask] = best

        full = states - 1
        component_optimum = dp[full]
        if component_optimum >= INF:
            print("NO")
            return

        optimum_so_far += component_optimum
        if optimum_so_far > B:
            print("NO")
            return

        mask = full
        while mask:
            position = mask.bit_count()
            cut_value = cuts[mask]
            bits = mask
            chosen = 0

            while bits:
                bit = bits & -bits
                if dp[mask ^ bit] + cut_value == dp[mask]:
                    chosen = bit
                    break
                bits ^= bit

            local_vertex = chosen.bit_length() - 1
            global_vertex = comp[local_vertex]
            result_positions[global_vertex] = offset + position
            mask ^= chosen

        offset += k

    print("YES")
    print(*result_positions)


if __name__ == "__main__":
    main()
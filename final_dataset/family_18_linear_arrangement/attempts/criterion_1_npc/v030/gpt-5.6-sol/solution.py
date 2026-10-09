import sys
from array import array


def arrangement_cost(order, adj):
    pos = {v: i for i, v in enumerate(order)}
    total = 0
    for u in order:
        pu = pos[u]
        for v, w in adj[u].items():
            if u < v:
                total += w * abs(pu - pos[v])
    return total


def path_order(vertices, adj):
    start = next(v for v in vertices if len(adj[v]) <= 1)
    order = []
    prev = -1
    cur = start
    while True:
        order.append(cur)
        nxt = -1
        for v in adj[cur]:
            if v != prev:
                nxt = v
                break
        if nxt == -1:
            break
        prev, cur = cur, nxt
    return order


def star_order(vertices, adj, center):
    s = len(vertices)
    center_pos = (s - 1) // 2
    slots = [i for i in range(s) if i != center_pos]
    slots.sort(key=lambda x: (abs(x - center_pos), x))

    leaves = [(w, v) for v, w in adj[center].items()]
    leaves.sort(key=lambda x: (-x[0], x[1]))

    order = [-1] * s
    order[center_pos] = center
    for slot, (_, v) in zip(slots, leaves):
        order[slot] = v
    return order


def exact_component(vertices, adj, upper_bound):
    s = len(vertices)
    if s <= 1:
        return vertices[:], 0

    index = {v: i for i, v in enumerate(vertices)}
    local_adj = [[] for _ in range(s)]
    degree = [0] * s
    neighbor_masks = [0] * s
    simple = True
    edge_weight_sum = 0

    for i, u in enumerate(vertices):
        for v, w in adj[u].items():
            j = index[v]
            local_adj[i].append((j, w))
            degree[i] += w
            neighbor_masks[i] |= 1 << j
            if w != 1:
                simple = False
            if i < j:
                edge_weight_sum += w

    size = 1 << s
    inf = upper_bound + 1
    max_value = max(inf, edge_weight_sum)

    if max_value <= 0xFFFFFFFF:
        typecode = 'I'
    elif max_value <= 0xFFFFFFFFFFFFFFFF:
        typecode = 'Q'
    else:
        typecode = None

    if typecode is None:
        cuts = [0] * size
        dp = [inf] * size
    else:
        cuts = array(typecode, [0]) * size
        dp = array(typecode, [inf]) * size

    dp[0] = 0
    bit_a = 1
    bit_b = 2

    if simple:
        masks = neighbor_masks
        deg = degree
        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit
            cuts[mask] = cuts[rest] + deg[v] - 2 * ((masks[v] & rest).bit_count())

            if (mask & bit_b) and not (mask & bit_a):
                continue

            best = inf
            bits = mask
            while bits:
                b = bits & -bits
                prev = mask ^ b
                value = dp[prev] + cuts[prev]
                if value < best:
                    best = value
                bits ^= b
            dp[mask] = best if best < inf else inf
    else:
        ladj = local_adj
        deg = degree
        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit
            inside = 0
            for j, w in ladj[v]:
                if rest & (1 << j):
                    inside += w
            cuts[mask] = cuts[rest] + deg[v] - 2 * inside

            if (mask & bit_b) and not (mask & bit_a):
                continue

            best = inf
            bits = mask
            while bits:
                b = bits & -bits
                prev = mask ^ b
                value = dp[prev] + cuts[prev]
                if value < best:
                    best = value
                bits ^= b
            dp[mask] = best if best < inf else inf

    full = size - 1
    optimum = dp[full]
    reversed_order = []
    mask = full

    while mask:
        bits = mask
        found = False
        while bits:
            bit = bits & -bits
            prev = mask ^ bit
            if dp[mask] == dp[prev] + cuts[prev]:
                reversed_order.append(bit.bit_length() - 1)
                mask = prev
                found = True
                break
            bits ^= bit
        if not found:
            raise RuntimeError("Failed to reconstruct arrangement")

    reversed_order.reverse()
    order = [vertices[i] for i in reversed_order]
    return order, optimum


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]
    total_edge_weight = 0

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        adj[u][v] = adj[u].get(v, 0) + 1
        adj[v][u] = adj[v].get(u, 0) + 1
        total_edge_weight += 1

    if total_edge_weight > budget:
        print("NO")
        return

    visited = bytearray(n)
    isolated = []
    records = []

    for start in range(n):
        if visited[start]:
            continue
        if not adj[start]:
            visited[start] = 1
            isolated.append(start)
            continue

        visited[start] = 1
        stack = [start]
        vertices = []

        while stack:
            u = stack.pop()
            vertices.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    stack.append(v)

        s = len(vertices)
        exact = False

        if all(len(adj[v]) <= 2 for v in vertices):
            order = path_order(vertices, adj)
            cost = arrangement_cost(order, adj)
            exact = True
        else:
            center = -1
            for v in vertices:
                if len(adj[v]) == s - 1:
                    is_star = True
                    for u in vertices:
                        if u != v and len(adj[u]) != 1:
                            is_star = False
                            break
                    if is_star:
                        center = v
                        break

            if center != -1:
                order = star_order(vertices, adj, center)
                cost = arrangement_cost(order, adj)
                exact = True
            else:
                complete_simple = True
                for v in vertices:
                    if len(adj[v]) != s - 1:
                        complete_simple = False
                        break
                    for w in adj[v].values():
                        if w != 1:
                            complete_simple = False
                            break
                    if not complete_simple:
                        break

                order = vertices[:]
                cost = arrangement_cost(order, adj)
                exact = complete_simple

        records.append([vertices, order, cost, exact])

    current_cost = sum(record[2] for record in records)

    if current_cost > budget:
        unresolved = sorted(
            (i for i, record in enumerate(records) if not record[3]),
            key=lambda i: len(records[i][0])
        )

        for i in unresolved:
            vertices, old_order, old_cost, _ = records[i]
            new_order, optimum = exact_component(vertices, adj, old_cost)
            records[i] = [vertices, new_order, optimum, True]
            current_cost += optimum - old_cost
            if current_cost <= budget:
                break

    if current_cost > budget:
        print("NO")
        return

    final_order = []
    for _, order, _, _ in records:
        final_order.extend(order)
    final_order.extend(isolated)

    position = [0] * n
    for slot, vertex in enumerate(final_order, 1):
        position[vertex] = slot

    print("YES")
    print(*position)


if __name__ == "__main__":
    main()
import sys
from array import array
from collections import deque

def make_positions(order, n):
    pos = [0] * n
    for i, v in enumerate(order, 1):
        pos[v] = i
    return pos

def arrangement_cost(order, edges, n, limit=None):
    pos = make_positions(order, n)
    total = 0
    for u, v, w in edges:
        total += w * abs(pos[u] - pos[v])
        if limit is not None and total > limit:
            return total
    return total

def local_cost(order, edges):
    pos = {v: i for i, v in enumerate(order)}
    return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)

def special_component_order(vertices, edges, adj):
    c = len(vertices)
    if c <= 1:
        return vertices[:], 0

    degrees = {v: len(adj[v]) for v in vertices}

    # A path is optimally placed in path order, making every edge length one.
    if max(degrees.values()) <= 2 and any(degrees[v] == 1 for v in vertices):
        start = next(v for v in vertices if degrees[v] == 1)
        order = []
        prev = -1
        cur = start
        while True:
            order.append(cur)
            nxt = -1
            for to, _ in adj[cur]:
                if to != prev:
                    nxt = to
                    break
            if nxt == -1:
                break
            prev, cur = cur, nxt
        if len(order) == c:
            return order, sum(w for _, _, w in edges)

    # A cycle: break the lightest edge and place the resulting path consecutively.
    if all(degrees[v] == 2 for v in vertices) and len(edges) == c:
        bu, bv, _ = min(edges, key=lambda e: e[2])
        order = [bu]
        prev = bv
        cur = bu
        while len(order) < c:
            nxt = -1
            for to, _ in adj[cur]:
                if to != prev:
                    nxt = to
                    break
            if nxt == -1 or (cur == bu and nxt == bv):
                return None
            order.append(nxt)
            prev, cur = cur, nxt
        return order, local_cost(order, edges)

    # A weighted star: put the center in the middle and heavier leaves closer.
    center = None
    for v in vertices:
        if degrees[v] == c - 1:
            center = v
            break
    if center is not None and all(v == center or degrees[v] == 1 for v in vertices):
        center_pos = c // 2
        slots = [i for i in range(c) if i != center_pos]
        slots.sort(key=lambda x: (abs(x - center_pos), x))
        leaves = [(w, to) for to, w in adj[center]]
        leaves.sort(reverse=True)

        order = [-1] * c
        order[center_pos] = center
        for slot, (_, leaf) in zip(slots, leaves):
            order[slot] = leaf
        return order, local_cost(order, edges)

    # An equal-weight clique has the same cost under every ordering.
    if len(edges) == c * (c - 1) // 2:
        first_weight = edges[0][2]
        if all(w == first_weight for _, _, w in edges):
            cost = first_weight * (c * c * c - c) // 6
            return vertices[:], cost

    return None

def solve_component_dp(vertices, edges, adj, allowance):
    c = len(vertices)
    if c == 1:
        return vertices[:], 0

    # High-degree vertices receive larger local indices, reducing weighted-cut work.
    vertices = sorted(vertices, key=lambda v: len(adj[v]))
    index = {v: i for i, v in enumerate(vertices)}

    local_adj = [[] for _ in range(c)]
    all_unit = True
    comp_weight = 0
    for u, v, w in edges:
        a, b = index[u], index[v]
        local_adj[a].append((b, w))
        local_adj[b].append((a, w))
        comp_weight += w
        if w != 1:
            all_unit = False

    size = 1 << c
    cut_type = 'I' if comp_weight <= 0xFFFFFFFF else 'Q'
    cuts = array(cut_type, [0]) * size

    if all_unit:
        neighbor_masks = [0] * c
        degrees = [0] * c
        for i in range(c):
            mask = 0
            for j, _ in local_adj[i]:
                mask |= 1 << j
            neighbor_masks[i] = mask
            degrees[i] = len(local_adj[i])

        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            prev = mask ^ bit
            cuts[mask] = cuts[prev] + degrees[v] - 2 * (
                neighbor_masks[v] & prev
            ).bit_count()
    else:
        degrees = [sum(w for _, w in local_adj[i]) for i in range(c)]
        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            prev = mask ^ bit
            inside_weight = 0
            for to, w in local_adj[v]:
                if prev & (1 << to):
                    inside_weight += w
            cuts[mask] = cuts[prev] + degrees[v] - 2 * inside_weight

    inf = allowance + 1
    dp_type = 'I' if inf <= 0xFFFFFFFF else 'Q'
    dp = array(dp_type, [inf]) * size
    dp[0] = 0
    parent = bytearray(size)

    for mask in range(1, size):
        best = inf
        best_v = 0
        bits = mask
        while bits:
            bit = bits & -bits
            prev = mask ^ bit
            value = dp[prev]
            if value < best:
                best = value
                best_v = bit.bit_length() - 1
            bits ^= bit

        value = best + cuts[mask]
        if value > allowance:
            value = inf
        dp[mask] = value
        parent[mask] = best_v

    full = size - 1
    optimum = dp[full]
    if optimum == inf:
        return None

    reverse_order = []
    mask = full
    while mask:
        v = parent[mask]
        reverse_order.append(vertices[v])
        mask ^= 1 << v
    reverse_order.reverse()
    return reverse_order, optimum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    if budget < 0:
        print("NO")
        return

    weights = {}
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        if u > v:
            u, v = v, u
        key = (u, v)
        weights[key] = weights.get(key, 0) + 1

    edges = [(u, v, w) for (u, v), w in weights.items()]
    total_edge_weight = sum(w for _, _, w in edges)

    if total_edge_weight > budget:
        print("NO")
        return

    identity = list(range(n))
    if arrangement_cost(identity, edges, n, budget) <= budget:
        print("YES")
        print(*range(1, n + 1))
        return

    adj = [[] for _ in range(n)]
    active = bytearray(n)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        active[u] = 1
        active[v] = 1

    components = []
    seen = bytearray(n)
    for start in range(n):
        if not active[start] or seen[start]:
            continue
        stack = [start]
        seen[start] = 1
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for to, _ in adj[v]:
                if not seen[to]:
                    seen[to] = 1
                    stack.append(to)
        components.append(vertices)

    edge_component = [-1] * n
    for ci, vertices in enumerate(components):
        for v in vertices:
            edge_component[v] = ci

    component_edges = [[] for _ in components]
    component_weight = [0] * len(components)
    for u, v, w in edges:
        ci = edge_component[u]
        component_edges[ci].append((u, v, w))
        component_weight[ci] += w

    isolates = [v for v in range(n) if not active[v]]

    # Cuthill-McKee-like constructive attempt, useful for large easy YES cases.
    heuristic_order = []
    for vertices in components:
        remaining = set(vertices)
        while remaining:
            start = min(remaining, key=lambda v: (len(adj[v]), v))
            q = deque([start])
            remaining.remove(start)
            while q:
                v = q.popleft()
                heuristic_order.append(v)
                nxt = [to for to, _ in adj[v] if to in remaining]
                nxt.sort(key=lambda x: (len(adj[x]), x))
                for to in nxt:
                    remaining.remove(to)
                    q.append(to)
    heuristic_order.extend(isolates)

    if arrangement_cost(heuristic_order, edges, n, budget) <= budget:
        pos = make_positions(heuristic_order, n)
        print("YES")
        print(*(x + 1 for x in pos))
        return

    result_order = []
    spent = 0
    remaining_lower_bound = total_edge_weight

    # Smaller components first generally reduces peak memory.
    order_of_components = sorted(
        range(len(components)), key=lambda i: len(components[i])
    )

    for ci in order_of_components:
        vertices = components[ci]
        comp_edges = component_edges[ci]
        comp_weight = component_weight[ci]
        remaining_lower_bound -= comp_weight

        special = special_component_order(vertices, comp_edges, adj)
        if special is not None:
            order, cost = special
        else:
            allowance = budget - spent - remaining_lower_bound
            if allowance < comp_weight:
                print("NO")
                return
            solved = solve_component_dp(vertices, comp_edges, adj, allowance)
            if solved is None:
                print("NO")
                return
            order, cost = solved

        spent += cost
        if spent + remaining_lower_bound > budget:
            print("NO")
            return
        result_order.extend(order)

    result_order.extend(isolates)

    if spent > budget:
        print("NO")
        return

    pos = make_positions(result_order, n)
    print("YES")
    print(*(x + 1 for x in pos))

if __name__ == "__main__":
    main()
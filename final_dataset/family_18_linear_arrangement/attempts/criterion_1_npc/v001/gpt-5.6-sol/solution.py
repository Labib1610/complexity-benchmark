import sys
from array import array
from collections import deque

def component_cost(order, edges):
    pos = {v: i for i, v in enumerate(order)}
    return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)

def improve_order(order, adj, max_passes=8):
    order = order[:]
    pos = {v: i for i, v in enumerate(order)}
    k = len(order)

    for _ in range(max_passes):
        changed = False
        i = 0
        while i + 1 < k:
            a, b = order[i], order[i + 1]
            delta = 0

            for y, w in adj[a].items():
                if y == b:
                    continue
                delta += w if pos[y] < i else -w

            for y, w in adj[b].items():
                if y == a:
                    continue
                delta += -w if pos[y] < i else w

            if delta < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True
                if i:
                    i -= 1
                    continue
            i += 1

        if not changed:
            break

    return order

def heuristic_order(vertices, edges, adj):
    if len(vertices) <= 1:
        return vertices[:]

    degree = {v: sum(adj[v].values()) for v in vertices}
    candidates = [
        vertices[:],
        sorted(vertices, key=lambda v: (degree[v], v)),
        sorted(vertices, key=lambda v: (-degree[v], v))
    ]

    start = min(vertices, key=lambda v: (degree[v], v))
    q = deque([start])
    seen = {start}
    bfs = []
    while q:
        v = q.popleft()
        bfs.append(v)
        ns = [u for u in adj[v] if u not in seen]
        ns.sort(key=lambda u: (degree[u], u))
        for u in ns:
            seen.add(u)
            q.append(u)
    candidates.append(bfs)
    candidates.append(bfs[::-1])

    best = None
    best_cost = None

    for initial in candidates:
        order = initial[:]
        for _ in range(8):
            pos = {v: i for i, v in enumerate(order)}
            scored = []
            for v in order:
                d = degree[v]
                if d:
                    s = sum(w * pos[u] for u, w in adj[v].items()) / d
                else:
                    s = pos[v]
                scored.append((s, pos[v], v))
            new_order = [v for _, _, v in sorted(scored)]
            if new_order == order:
                break
            order = new_order

        order = improve_order(order, adj)
        cost = component_cost(order, edges)
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best = order

    return best

def exact_dense(vertices, edges, cap):
    k = len(vertices)
    if k <= 1:
        return vertices[:], 0

    index = {v: i for i, v in enumerate(vertices)}
    deg = [0] * k
    nbr_mask = [0] * k
    weights = [dict() for _ in range(k)]
    simple = True

    for u, v, w in edges:
        a, b = index[u], index[v]
        deg[a] += w
        deg[b] += w
        nbr_mask[a] |= 1 << b
        nbr_mask[b] |= 1 << a
        weights[a][b] = w
        weights[b][a] = w
        if w != 1:
            simple = False

    size = 1 << k
    inf = cap + 1
    cuts = array('q', [0]) * size
    dp = array('q', [inf]) * size
    parent = bytearray(size)
    dp[0] = 0

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit

        if simple:
            conn = (nbr_mask[v] & rest).bit_count()
        else:
            x = nbr_mask[v] & rest
            conn = 0
            wv = weights[v]
            while x:
                b = x & -x
                j = b.bit_length() - 1
                conn += wv[j]
                x ^= b

        cut_value = cuts[rest] + deg[v] - 2 * conn
        cuts[mask] = cut_value

        x = mask
        best = inf
        best_v = 0
        while x:
            b = x & -x
            j = b.bit_length() - 1
            value = dp[mask ^ b]
            if value < best:
                best = value
                best_v = j
            x ^= b

        value = best + cut_value
        if value <= cap:
            dp[mask] = value
            parent[mask] = best_v

    full = size - 1
    if dp[full] > cap:
        return None, None

    rev = []
    mask = full
    while mask:
        v = parent[mask]
        rev.append(vertices[v])
        mask ^= 1 << v
    rev.reverse()
    return rev, int(dp[full])

def exact_sparse(vertices, edges, cap):
    k = len(vertices)
    if k <= 1:
        return vertices[:], 0

    index = {v: i for i, v in enumerate(vertices)}
    deg = [0] * k
    neighbors = [[] for _ in range(k)]

    for u, v, w in edges:
        a, b = index[u], index[v]
        deg[a] += w
        deg[b] += w
        neighbors[a].append((b, w))
        neighbors[b].append((a, w))

    costs = {0: 0}
    cuts = {0: 0}
    parent = {}

    for new_size in range(1, k + 1):
        next_costs = {}
        next_cuts = {}
        remaining_lb = k - 1 - new_size

        for mask, base_cost in costs.items():
            missing = ((1 << k) - 1) ^ mask
            cut_mask = cuts[mask]

            while missing:
                bit = missing & -missing
                v = bit.bit_length() - 1
                new_mask = mask | bit

                if new_mask in next_cuts:
                    new_cut = next_cuts[new_mask]
                else:
                    conn = 0
                    for u, w in neighbors[v]:
                        if mask & (1 << u):
                            conn += w
                    new_cut = cut_mask + deg[v] - 2 * conn
                    next_cuts[new_mask] = new_cut

                value = base_cost + new_cut
                if value + remaining_lb <= cap:
                    old = next_costs.get(new_mask)
                    if old is None or value < old:
                        next_costs[new_mask] = value
                        parent[new_mask] = v

                missing ^= bit

        if not next_costs:
            return None, None
        costs, cuts = next_costs, next_cuts

    full = (1 << k) - 1
    if full not in costs:
        return None, None

    rev = []
    mask = full
    while mask:
        v = parent[mask]
        rev.append(vertices[v])
        mask ^= 1 << v
    rev.reverse()
    return rev, costs[full]

def exact_order(vertices, edges, cap):
    if len(vertices) <= 21:
        return exact_dense(vertices, edges, cap)
    return exact_sparse(vertices, edges, cap)

def output_order(n, order):
    position = [0] * (n + 1)
    for i, v in enumerate(order, 1):
        position[v] = i
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, position[1:])) + "\n")

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    edge_weights = {}
    p = 3

    for _ in range(m):
        u, v = data[p], data[p + 1]
        p += 2
        if u == v:
            continue
        if u > v:
            u, v = v, u
        edge_weights[(u, v)] = edge_weights.get((u, v), 0) + 1

    total_edge_weight = sum(edge_weights.values())
    if total_edge_weight > budget:
        print("NO")
        return

    adj = [dict() for _ in range(n + 1)]
    all_edges = []
    for (u, v), w in edge_weights.items():
        adj[u][v] = w
        adj[v][u] = w
        all_edges.append((u, v, w))

    visited = [False] * (n + 1)
    components = []
    isolated = []

    for start in range(1, n + 1):
        if visited[start]:
            continue
        visited[start] = True
        if not adj[start]:
            isolated.append(start)
            continue

        stack = [start]
        vertices = []
        vertex_set = set()
        while stack:
            v = stack.pop()
            vertices.append(v)
            vertex_set.add(v)
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        edges = []
        lower_bound = 0
        for u in vertices:
            for v, w in adj[u].items():
                if u < v:
                    edges.append((u, v, w))
                    lower_bound += w

        components.append({
            "vertices": vertices,
            "edges": edges,
            "lb": lower_bound
        })

    heuristic_total = 0
    for comp in components:
        order = heuristic_order(comp["vertices"], comp["edges"], adj)
        cost = component_cost(order, comp["edges"])
        comp["heuristic_order"] = order
        comp["heuristic_cost"] = cost
        heuristic_total += cost

    if heuristic_total <= budget:
        final_order = []
        for comp in components:
            final_order.extend(comp["heuristic_order"])
        final_order.extend(isolated)
        output_order(n, final_order)
        return

    components.sort(key=lambda c: len(c["vertices"]), reverse=True)
    remaining_lb = sum(c["lb"] for c in components)
    exact_total = 0
    final_order = []

    for comp in components:
        remaining_lb -= comp["lb"]
        cap = budget - exact_total - remaining_lb
        if cap < comp["lb"]:
            print("NO")
            return

        order, cost = exact_order(comp["vertices"], comp["edges"], cap)
        if order is None:
            print("NO")
            return

        final_order.extend(order)
        exact_total += cost

    if exact_total > budget:
        print("NO")
        return

    final_order.extend(isolated)
    output_order(n, final_order)

if __name__ == "__main__":
    main()
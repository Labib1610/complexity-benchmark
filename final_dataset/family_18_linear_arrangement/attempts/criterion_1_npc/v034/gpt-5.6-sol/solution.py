import sys
from collections import deque

def arrangement_cost(order, edges):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)

def improve_adjacent(order, nbrs):
    order = order[:]
    n = len(order)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    for _ in range(8):
        changed = False
        i = 0
        while i + 1 < n:
            a, b = order[i], order[i + 1]
            delta = 0

            for x, w in nbrs[a]:
                if x == b:
                    continue
                px = pos[x]
                delta += w if px < i else -w

            for x, w in nbrs[b]:
                if x == a:
                    continue
                px = pos[x]
                delta += -w if px < i else w

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

def heuristic_order(n, edges, nbrs, degrees):
    if n <= 1:
        return list(range(n)), 0

    candidates = []

    degree_order = sorted(range(n), key=lambda x: (degrees[x], x))
    candidates.append(degree_order)
    candidates.append(degree_order[::-1])

    roots = []
    roots.extend(degree_order[:min(6, n)])
    roots.extend(degree_order[-min(6, n):])
    roots.extend(sorted(range(n), key=lambda x: (-degrees[x], x))[:min(6, n)])
    roots = list(dict.fromkeys(roots))

    for root in roots:
        seen = [False] * n
        seen[root] = True
        q = deque([root])
        bfs = []
        while q:
            v = q.popleft()
            bfs.append(v)
            nxt = [u for u, _ in nbrs[v] if not seen[u]]
            nxt.sort(key=lambda x: (degrees[x], x))
            for u in nxt:
                if not seen[u]:
                    seen[u] = True
                    q.append(u)
        candidates.append(bfs)
        candidates.append(bfs[::-1])

        mask = 0
        cut = 0
        greedy = []
        unused = (1 << n) - 1
        first = root
        while unused:
            if not greedy:
                v = first
            else:
                best_key = None
                v = -1
                bits = unused
                while bits:
                    bit = bits & -bits
                    x = bit.bit_length() - 1
                    internal = 0
                    for y, w in nbrs[x]:
                        if (mask >> y) & 1:
                            internal += w
                    nc = cut + degrees[x] - 2 * internal
                    key = (nc, -internal, degrees[x], x)
                    if best_key is None or key < best_key:
                        best_key = key
                        v = x
                    bits -= bit
            greedy.append(v)
            internal = 0
            for y, w in nbrs[v]:
                if (mask >> y) & 1:
                    internal += w
            cut += degrees[v] - 2 * internal
            mask |= 1 << v
            unused ^= 1 << v
        candidates.append(greedy)
        candidates.append(greedy[::-1])

    best_order = None
    best_cost = 10**100
    seen_orders = set()

    for order in candidates:
        key = tuple(order)
        if key in seen_orders:
            continue
        seen_orders.add(key)
        improved = improve_adjacent(order, nbrs)
        cost = arrangement_cost(improved, edges)
        if cost < best_cost:
            best_cost = cost
            best_order = improved

    return best_order, best_cost

def stoer_wagner_min_cut(n, edges):
    if n <= 1:
        return 0
    if n > 150:
        return 1

    g = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        g[u][v] += w
        g[v][u] += w

    vertices = list(range(n))
    best = 10**100

    while len(vertices) > 1:
        used = [False] * n
        weights = [0] * n
        prev = -1

        for step in range(len(vertices)):
            sel = -1
            for v in vertices:
                if not used[v] and (sel == -1 or weights[v] > weights[sel]):
                    sel = v

            if step == len(vertices) - 1:
                best = min(best, weights[sel])
                if prev != -1:
                    for v in vertices:
                        if v != sel and v != prev:
                            g[prev][v] += g[sel][v]
                            g[v][prev] = g[prev][v]
                    vertices.remove(sel)
                break

            used[sel] = True
            prev = sel
            for v in vertices:
                if not used[v]:
                    weights[v] += g[sel][v]

    return best

def component_lower_bound(n, edges, nbrs, degrees):
    total_weight = sum(w for _, _, w in edges)
    min_cut = stoer_wagner_min_cut(n, edges)
    lb = max(total_weight, min_cut * (n - 1))

    incident_bound_sum = 0
    for v in range(n):
        ws = sorted((w for _, w in nbrs[v]), reverse=True)
        incident_bound_sum += sum(w * (i // 2 + 1) for i, w in enumerate(ws))
    lb = max(lb, (incident_bound_sum + 1) // 2)

    return lb, max(1, min_cut)

def exact_order(n, edges, nbrs, degrees, cap, min_cut):
    if n == 1:
        return [0], 0
    if cap < 0:
        return None, None

    total_weight = sum(w for _, _, w in edges)
    shift = max(1, total_weight.bit_length())
    cut_mask = (1 << shift) - 1
    all_mask = (1 << n) - 1

    simple = all(w == 1 for _, _, w in edges)
    adj_masks = [0] * n
    if simple:
        for u, v, _ in edges:
            adj_masks[u] |= 1 << v
            adj_masks[v] |= 1 << u

    levels = [{0: 0}]

    for size in range(n):
        current = levels[-1]
        nxt = {}
        remaining_after = n - (size + 1) - 1

        for mask, encoded in current.items():
            dp = encoded >> shift
            cut = encoded & cut_mask
            bits = all_mask ^ mask

            while bits:
                bit = bits & -bits
                v = bit.bit_length() - 1

                if simple:
                    internal = (adj_masks[v] & mask).bit_count()
                else:
                    internal = 0
                    for u, w in nbrs[v]:
                        if (mask >> u) & 1:
                            internal += w

                new_cut = cut + degrees[v] - 2 * internal
                new_dp = dp + new_cut

                if new_dp + max(0, remaining_after) * min_cut <= cap:
                    new_mask = mask | bit
                    old = nxt.get(new_mask)
                    if old is None or new_dp < (old >> shift):
                        nxt[new_mask] = (new_dp << shift) | new_cut

                bits -= bit

        if not nxt:
            return None, None
        levels.append(nxt)

    final_encoded = levels[n].get(all_mask)
    if final_encoded is None:
        return None, None

    optimum = final_encoded >> shift
    order_rev = []
    mask = all_mask

    for size in range(n, 0, -1):
        encoded = levels[size][mask]
        dp = encoded >> shift
        cut = encoded & cut_mask
        bits = mask
        found = False

        while bits:
            bit = bits & -bits
            v = bit.bit_length() - 1
            prev_mask = mask ^ bit
            prev_encoded = levels[size - 1].get(prev_mask)
            if prev_encoded is not None:
                prev_dp = prev_encoded >> shift
                if prev_dp + cut == dp:
                    order_rev.append(v)
                    mask = prev_mask
                    found = True
                    break
            bits -= bit

        if not found:
            return None, None

    return order_rev[::-1], optimum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, limit = data[0], data[1], data[2]
    if limit < 0:
        print("NO")
        return

    edge_weights = {}
    idx = 3
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        if u == v:
            continue
        if u > v:
            u, v = v, u
        edge_weights[(u, v)] = edge_weights.get((u, v), 0) + 1

    global_edges = [(u, v, w) for (u, v), w in edge_weights.items()]
    total_edge_weight = sum(w for _, _, w in global_edges)

    if total_edge_weight > limit:
        print("NO")
        return

    graph = [[] for _ in range(n)]
    active = [False] * n
    for u, v, w in global_edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        active[u] = active[v] = True

    visited = [False] * n
    components = []

    for start in range(n):
        if not active[start] or visited[start]:
            continue
        visited[start] = True
        q = [start]
        vertices = []
        while q:
            v = q.pop()
            vertices.append(v)
            for u, _ in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        components.append(vertices)

    comp_infos = []
    heuristic_total = 0
    lower_total = 0

    for vertices in components:
        local_id = {v: i for i, v in enumerate(vertices)}
        s = len(vertices)
        local_edges = []
        nbrs = [[] for _ in range(s)]
        degrees = [0] * s

        for gv in vertices:
            a = local_id[gv]
            for gu, w in graph[gv]:
                if gv < gu and gu in local_id:
                    b = local_id[gu]
                    local_edges.append((a, b, w))
                    nbrs[a].append((b, w))
                    nbrs[b].append((a, w))
                    degrees[a] += w
                    degrees[b] += w

        h_order, h_cost = heuristic_order(s, local_edges, nbrs, degrees)
        lb, min_cut = component_lower_bound(s, local_edges, nbrs, degrees)

        comp_infos.append({
            "vertices": vertices,
            "edges": local_edges,
            "nbrs": nbrs,
            "degrees": degrees,
            "h_order": h_order,
            "h_cost": h_cost,
            "lb": lb,
            "min_cut": min_cut,
        })
        heuristic_total += h_cost
        lower_total += lb

    if lower_total > limit:
        print("NO")
        return

    if heuristic_total <= limit:
        final_station_order = []
        for info in comp_infos:
            final_station_order.extend(info["vertices"][v] for v in info["h_order"])
        final_station_order.extend(v for v in range(n) if not active[v])

        positions = [0] * n
        for pos, v in enumerate(final_station_order, 1):
            positions[v] = pos
        print("YES")
        print(*positions)
        return

    exact_sum = 0
    remaining_lb = lower_total
    chosen_orders = []

    comp_infos.sort(key=lambda info: (
        -(info["h_cost"] - info["lb"]),
        -len(info["vertices"])
    ))

    for info in comp_infos:
        remaining_lb -= info["lb"]
        cap = limit - exact_sum - remaining_lb

        if info["h_cost"] == info["lb"]:
            order = info["h_order"]
            cost = info["h_cost"]
        else:
            order, cost = exact_order(
                len(info["vertices"]),
                info["edges"],
                info["nbrs"],
                info["degrees"],
                cap,
                info["min_cut"]
            )
            if order is None:
                print("NO")
                return

        exact_sum += cost
        chosen_orders.append((info, order))

        if exact_sum + remaining_lb > limit:
            print("NO")
            return

    if exact_sum > limit:
        print("NO")
        return

    final_station_order = []
    for info, order in chosen_orders:
        final_station_order.extend(info["vertices"][v] for v in order)
    final_station_order.extend(v for v in range(n) if not active[v])

    positions = [0] * n
    for pos, v in enumerate(final_station_order, 1):
        positions[v] = pos

    print("YES")
    print(*positions)

if __name__ == "__main__":
    main()
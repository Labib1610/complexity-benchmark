import sys
from array import array
from collections import deque

def arrangement_cost(order, adj):
    pos = [0] * len(adj)
    for i, v in enumerate(order):
        pos[v] = i
    total = 0
    for u in range(len(adj)):
        pu = pos[u]
        for v, w in adj[u].items():
            if u < v:
                total += w * abs(pu - pos[v])
    return total

def component_cost(order, adj):
    pos = {v: i for i, v in enumerate(order)}
    total = 0
    for u in order:
        pu = pos[u]
        for v, w in adj[u].items():
            if u < v:
                total += w * abs(pu - pos[v])
    return total

def bfs_order(component, root, adj, reverse_neighbors=False):
    comp_set = set(component)
    seen = {root}
    q = deque([root])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        neighbors = [v for v in adj[u] if v in comp_set and v not in seen]
        neighbors.sort(
            key=lambda x: (len(adj[x]), x),
            reverse=reverse_neighbors
        )
        for v in neighbors:
            seen.add(v)
            q.append(v)
    return order

def dfs_order(component, root, adj):
    comp_set = set(component)
    seen = {root}
    stack = [root]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        neighbors = [v for v in adj[u] if v in comp_set and v not in seen]
        neighbors.sort(key=lambda x: (len(adj[x]), x), reverse=True)
        for v in neighbors:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return order

def heuristic_component(component, adj):
    if len(component) <= 1:
        return component[:]

    by_degree = sorted(component, key=lambda v: (len(adj[v]), v))
    roots = []
    for v in (by_degree[0], by_degree[-1], min(component), max(component)):
        if v not in roots:
            roots.append(v)

    candidates = [
        sorted(component),
        by_degree,
        list(reversed(by_degree)),
    ]

    for root in roots:
        b1 = bfs_order(component, root, adj, False)
        b2 = bfs_order(component, root, adj, True)
        d = dfs_order(component, root, adj)
        candidates.extend((b1, list(reversed(b1)), b2, d, list(reversed(d))))

    best = candidates[0]
    best_cost = component_cost(best, adj)
    for candidate in candidates[1:]:
        value = component_cost(candidate, adj)
        if value < best_cost:
            best_cost = value
            best = candidate
    return best

def exact_component(component, adj, limit):
    k = len(component)
    if k <= 1:
        return component[:], 0

    index = {v: i for i, v in enumerate(component)}
    degree = [0] * k
    neighbor_mask = [0] * k
    extras = [[] for _ in range(k)]

    for i, u in enumerate(component):
        mask = 0
        for v, w in adj[u].items():
            j = index.get(v)
            if j is None:
                continue
            degree[i] += w
            mask |= 1 << j
            if w > 1:
                extras[i].append((1 << j, w - 1))
        neighbor_mask[i] = mask

    size = 1 << k
    cuts = array('i', [0]) * size

    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        rest = mask ^ bit
        inside_weight = (neighbor_mask[v] & rest).bit_count()
        for nb_bit, extra in extras[v]:
            if rest & nb_bit:
                inside_weight += extra
        cuts[mask] = cuts[rest] + degree[v] - 2 * inside_weight

    MAXQ = 9_000_000_000_000_000_000
    inf = min(MAXQ, max(0, limit) + 1)
    dp = array('q', [inf]) * size
    dp[0] = 0

    for mask in range(1, size):
        best = inf
        bits = mask
        while bits:
            bit = bits & -bits
            value = dp[mask ^ bit]
            if value < best:
                best = value
            bits ^= bit

        value = best + cuts[mask]
        if value < inf:
            dp[mask] = value

    optimum = dp[size - 1]
    if optimum > limit:
        return None, optimum

    reversed_order = []
    mask = size - 1
    while mask:
        target = dp[mask] - cuts[mask]
        bits = mask
        chosen = 0
        while bits:
            bit = bits & -bits
            if dp[mask ^ bit] == target:
                chosen = bit
                break
            bits ^= bit
        if chosen == 0:
            return None, optimum
        reversed_order.append(component[chosen.bit_length() - 1])
        mask ^= chosen

    reversed_order.reverse()
    return reversed_order, optimum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        adj[u][v] = adj[u].get(v, 0) + 1
        adj[v][u] = adj[v].get(u, 0) + 1

    if budget < 0:
        print("NO")
        return

    components = []
    seen = [False] * n
    for start in range(n):
        if seen[start]:
            continue
        seen[start] = True
        stack = [start]
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        components.append(comp)

    edge_lower_bound = 0
    local_sum = 0
    for u in range(n):
        weights = sorted(adj[u].values(), reverse=True)
        local_sum += sum(w * (i // 2 + 1) for i, w in enumerate(weights))
        for v, w in adj[u].items():
            if u < v:
                edge_lower_bound += w

    lower_bound = max(edge_lower_bound, (local_sum + 1) // 2)
    if lower_bound > budget:
        print("NO")
        return

    heuristic_order = []
    for comp in components:
        heuristic_order.extend(heuristic_component(comp, adj))

    if arrangement_cost(heuristic_order, adj) <= budget:
        positions = [0] * n
        for i, v in enumerate(heuristic_order, 1):
            positions[v] = i
        print("YES")
        print(*positions)
        return

    components.sort(key=len, reverse=True)
    final_order = []
    total = 0

    for comp in components:
        remaining = budget - total
        order, value = exact_component(comp, adj, remaining)
        if order is None:
            print("NO")
            return
        final_order.extend(order)
        total += value

    positions = [0] * n
    for i, v in enumerate(final_order, 1):
        positions[v] = i

    print("YES")
    print(*positions)

if __name__ == "__main__":
    main()
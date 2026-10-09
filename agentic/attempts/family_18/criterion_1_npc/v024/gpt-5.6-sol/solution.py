import sys
from collections import deque
from array import array

def arrangement_cost(order, adj):
    pos = {v: i for i, v in enumerate(order)}
    total = 0
    for u in order:
        pu = pos[u]
        for v in adj[u]:
            if u < v:
                total += abs(pu - pos[v])
    return total

def improve_order(order, adj):
    order = order[:]
    k = len(order)
    pos = {v: i for i, v in enumerate(order)}

    changed = True
    passes = 0
    while changed and passes < 2 * k:
        changed = False
        passes += 1
        for i in range(k - 1):
            a, b = order[i], order[i + 1]
            delta = 0

            for x in adj[a]:
                if x == b:
                    continue
                px = pos[x]
                if px < i:
                    delta += 1
                elif px > i + 1:
                    delta -= 1

            for x in adj[b]:
                if x == a:
                    continue
                px = pos[x]
                if px < i:
                    delta -= 1
                elif px > i + 1:
                    delta += 1

            if delta < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True

    return order

def heuristic_order(component, adj):
    comp_set = set(component)
    candidates = [
        sorted(component),
        sorted(component, key=lambda v: (len(adj[v]), v)),
        sorted(component, key=lambda v: (-len(adj[v]), v)),
    ]

    starts = [
        min(component, key=lambda v: (len(adj[v]), v)),
        max(component, key=lambda v: (len(adj[v]), -v)),
    ]

    for start in starts:
        seen = {start}
        q = deque([start])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            neighbors = sorted(
                (v for v in adj[u] if v in comp_set and v not in seen),
                key=lambda v: (len(adj[v]), v)
            )
            for v in neighbors:
                seen.add(v)
                q.append(v)
        candidates.append(order)

    best_order = None
    best_cost = None
    for order in candidates:
        order = improve_order(order, adj)
        cost = arrangement_cost(order, adj)
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_order = order

    return best_order, best_cost

def exact_component(component, adj, cap):
    k = len(component)
    if k <= 1:
        return component[:], 0

    index = {v: i for i, v in enumerate(component)}
    adj_masks = [0] * k
    degrees = [0] * k

    for i, u in enumerate(component):
        mask = 0
        for v in adj[u]:
            j = index.get(v)
            if j is not None:
                mask |= 1 << j
        adj_masks[i] = mask
        degrees[i] = mask.bit_count()

    size = 1 << k
    full = size - 1

    cuts = array('i', [0]) * size
    for mask in range(1, size):
        bit = mask & -mask
        v = bit.bit_length() - 1
        prev = mask ^ bit
        cuts[mask] = cuts[prev] + degrees[v] - 2 * (adj_masks[v] & prev).bit_count()

    inf = cap + 1
    dp = array('q', [inf]) * size
    parent = bytearray(size)
    dp[0] = 0

    for mask in range(1, size):
        best = inf
        best_v = 0
        bits = mask
        while bits:
            bit = bits & -bits
            v = bit.bit_length() - 1
            prev_value = dp[mask ^ bit]
            if prev_value < best:
                best = prev_value
                best_v = v
            bits ^= bit

        if best >= inf:
            continue

        value = best + cuts[mask]
        if mask != full:
            remaining_cuts = k - mask.bit_count() - 1
            if value + remaining_cuts > cap:
                continue

        if value <= cap:
            dp[mask] = value
            parent[mask] = best_v + 1

    if dp[full] > cap:
        return None, None

    reversed_order = []
    mask = full
    while mask:
        v = parent[mask] - 1
        reversed_order.append(component[v])
        mask ^= 1 << v

    order = reversed_order[::-1]
    return order, dp[full]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m_input, budget = data[0], data[1], data[2]
    adj = [set() for _ in range(n)]
    p = 3

    for _ in range(m_input):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u != v:
            adj[u].add(v)
            adj[v].add(u)

    if budget < 0:
        print("NO")
        return

    components = []
    seen = [False] * n

    for start in range(n):
        if seen[start] or not adj[start]:
            continue
        stack = [start]
        seen[start] = True
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        components.append(comp)

    isolated = [v for v in range(n) if not adj[v]]

    heuristic_orders = []
    heuristic_total = 0
    for comp in components:
        order, cost = heuristic_order(comp, adj)
        heuristic_orders.append(order)
        heuristic_total += cost

    if heuristic_total <= budget:
        zone_order = []
        for order in heuristic_orders:
            zone_order.extend(order)
        zone_order.extend(isolated)

        answer = [0] * n
        for zone, crop in enumerate(zone_order, 1):
            answer[crop] = zone

        print("YES")
        print(*answer)
        return

    component_info = []
    total_lower_bound = 0

    for comp in components:
        edge_count = sum(len(adj[v]) for v in comp) // 2
        lower_bound = max(len(comp) - 1, edge_count)
        component_info.append((comp, lower_bound))
        total_lower_bound += lower_bound

    if total_lower_bound > budget:
        print("NO")
        return

    component_info.sort(key=lambda x: -len(x[0]))

    exact_orders = []
    exact_total = 0
    remaining_lower_bound = total_lower_bound

    for comp, lower_bound in component_info:
        remaining_lower_bound -= lower_bound
        cap = budget - exact_total - remaining_lower_bound

        order, cost = exact_component(comp, adj, cap)
        if order is None:
            print("NO")
            return

        exact_orders.append(order)
        exact_total += cost

    if exact_total > budget:
        print("NO")
        return

    zone_order = []
    for order in exact_orders:
        zone_order.extend(order)
    zone_order.extend(isolated)

    answer = [0] * n
    for zone, crop in enumerate(zone_order, 1):
        answer[crop] = zone

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()
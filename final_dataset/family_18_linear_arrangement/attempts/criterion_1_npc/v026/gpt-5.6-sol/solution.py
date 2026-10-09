import sys
from array import array
from collections import deque

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]
    edge_weights = {}

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
        edge_weights[key] = edge_weights.get(key, 0) + 1

    edges = []
    total_weight = 0
    for (u, v), w in edge_weights.items():
        edges.append((u, v, w))
        adj[u][v] = w
        adj[v][u] = w
        total_weight += w

    if budget < total_weight:
        print("NO")
        return

    def order_cost(order):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        return sum(w * abs(pos[u] - pos[v]) for u, v, w in edges)

    identity = list(range(n))
    if order_cost(identity) <= budget:
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
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        components.append(comp)

    components.sort(key=min)

    def cuthill_order(comp):
        comp_set = set(comp)
        seen = set()
        result = []
        while len(seen) < len(comp):
            root = min((v for v in comp if v not in seen),
                       key=lambda x: (len(adj[x]), x))
            seen.add(root)
            q = deque([root])
            while q:
                v = q.popleft()
                result.append(v)
                neighbors = [u for u in adj[v] if u in comp_set and u not in seen]
                neighbors.sort(key=lambda x: (len(adj[x]), x))
                for u in neighbors:
                    seen.add(u)
                    q.append(u)
        return result

    heuristic = []
    for comp in components:
        heuristic.extend(cuthill_order(comp))

    if order_cost(heuristic) <= budget:
        assignment = [0] * n
        for i, v in enumerate(heuristic, 1):
            assignment[v] = i
        print("YES")
        print(*assignment)
        return

    degree_order = []
    for comp in components:
        degree_order.extend(sorted(comp, key=lambda v: (sum(adj[v].values()), v)))

    if order_cost(degree_order) <= budget:
        assignment = [0] * n
        for i, v in enumerate(degree_order, 1):
            assignment[v] = i
        print("YES")
        print(*assignment)
        return

    def exact_component(comp, limit):
        k = len(comp)
        if k <= 1:
            return comp[:], 0

        local_index = {v: i for i, v in enumerate(comp)}
        local_adj = [[] for _ in range(k)]
        degree = [0] * k
        simple = True

        for i, v in enumerate(comp):
            for u, w in adj[v].items():
                j = local_index[u]
                local_adj[i].append((j, w))
                degree[i] += w
                if w != 1:
                    simple = False

        size = 1 << k
        full = size - 1
        inf = limit + 1

        if k <= 22:
            cuts = array('q', [0]) * size
            dp = array('q', [inf]) * size
            parent = bytearray(size)
            dp[0] = 0

            if simple:
                masks = [0] * k
                for i in range(k):
                    mask = 0
                    for j, _ in local_adj[i]:
                        mask |= 1 << j
                    masks[i] = mask

                for mask in range(1, size):
                    bit = mask & -mask
                    v = bit.bit_length() - 1
                    prev = mask ^ bit
                    inside = (masks[v] & prev).bit_count()
                    cuts[mask] = cuts[prev] + degree[v] - 2 * inside
            else:
                for mask in range(1, size):
                    bit = mask & -mask
                    v = bit.bit_length() - 1
                    prev = mask ^ bit
                    inside = 0
                    for u, w in local_adj[v]:
                        if prev & (1 << u):
                            inside += w
                    cuts[mask] = cuts[prev] + degree[v] - 2 * inside

            for mask in range(size - 1):
                cur = dp[mask]
                if cur > limit:
                    continue
                base = cur + cuts[mask]
                if base > limit:
                    continue
                remaining = full ^ mask
                while remaining:
                    bit = remaining & -remaining
                    new_mask = mask | bit
                    if base < dp[new_mask]:
                        dp[new_mask] = base
                        parent[new_mask] = bit.bit_length()
                    remaining ^= bit

            optimum = dp[full]
            if optimum > limit:
                return None, optimum

            reversed_order = []
            mask = full
            while mask:
                v = parent[mask] - 1
                if v < 0:
                    return None, inf
                reversed_order.append(comp[v])
                mask ^= 1 << v
            reversed_order.reverse()
            return reversed_order, optimum

        cut_cache = {0: 0}

        if simple:
            neighbor_masks = [0] * k
            for i in range(k):
                mask = 0
                for j, _ in local_adj[i]:
                    mask |= 1 << j
                neighbor_masks[i] = mask

            def get_cut(mask):
                if mask in cut_cache:
                    return cut_cache[mask]
                chain = []
                cur = mask
                while cur not in cut_cache:
                    bit = cur & -cur
                    chain.append((cur, bit))
                    cur ^= bit
                value = cut_cache[cur]
                while chain:
                    current, bit = chain.pop()
                    v = bit.bit_length() - 1
                    prev = current ^ bit
                    value += degree[v] - 2 * (neighbor_masks[v] & prev).bit_count()
                    cut_cache[current] = value
                return cut_cache[mask]
        else:
            def get_cut(mask):
                if mask in cut_cache:
                    return cut_cache[mask]
                chain = []
                cur = mask
                while cur not in cut_cache:
                    bit = cur & -cur
                    chain.append((cur, bit))
                    cur ^= bit
                value = cut_cache[cur]
                while chain:
                    current, bit = chain.pop()
                    v = bit.bit_length() - 1
                    prev = current ^ bit
                    inside = 0
                    for u, w in local_adj[v]:
                        if prev & (1 << u):
                            inside += w
                    value += degree[v] - 2 * inside
                    cut_cache[current] = value
                return cut_cache[mask]

        current = {0: 0}
        parent = {}

        for _ in range(k):
            nxt = {}
            for mask, cost in current.items():
                base = cost + get_cut(mask)
                if base > limit:
                    continue
                remaining = full ^ mask
                while remaining:
                    bit = remaining & -remaining
                    new_mask = mask | bit
                    old = nxt.get(new_mask)
                    if old is None or base < old:
                        nxt[new_mask] = base
                        parent[new_mask] = bit
                    remaining ^= bit
            current = nxt
            if not current:
                return None, inf

        optimum = current.get(full, inf)
        if optimum > limit:
            return None, optimum

        reversed_order = []
        mask = full
        while mask:
            bit = parent[mask]
            reversed_order.append(comp[bit.bit_length() - 1])
            mask ^= bit
        reversed_order.reverse()
        return reversed_order, optimum

    final_order = []
    used_cost = 0

    for comp in components:
        remaining_budget = budget - used_cost
        order, cost = exact_component(comp, remaining_budget)
        if order is None or cost > remaining_budget:
            print("NO")
            return
        final_order.extend(order)
        used_cost += cost

    assignment = [0] * n
    for position, vertex in enumerate(final_order, 1):
        assignment[vertex] = position

    print("YES")
    print(*assignment)

if __name__ == "__main__":
    solve()
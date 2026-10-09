import sys
from array import array
from collections import deque

def placement_cost(order, edges):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    return sum(abs(pos[u] - pos[v]) for u, v in edges)

def exact_component(nodes, adj):
    k = len(nodes)
    if k <= 1:
        return nodes[:], 0

    index = {v: i for i, v in enumerate(nodes)}
    degrees = [0] * k
    neighbor_masks = [0] * k
    neighbors = [[] for _ in range(k)]
    local_edges = []
    simple = True

    for i, u in enumerate(nodes):
        for v, w in adj[u].items():
            j = index[v]
            degrees[i] += w
            neighbor_masks[i] |= 1 << j
            neighbors[i].append((j, w))
            if w != 1:
                simple = False
            if i < j:
                local_edges.append((i, j, w))

    size = 1 << k
    dp = array('q', [0]) * size

    if simple:
        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit
            inside = (neighbor_masks[v] & rest).bit_count()
            dp[mask] = dp[rest] + degrees[v] - 2 * inside
    else:
        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            rest = mask ^ bit
            inside = 0
            for u, w in neighbors[v]:
                if rest & (1 << u):
                    inside += w
            dp[mask] = dp[rest] + degrees[v] - 2 * inside

    for mask in range(1, size):
        cut = dp[mask]
        bits = mask
        best = None
        while bits:
            bit = bits & -bits
            value = dp[mask ^ bit]
            if best is None or value < best:
                best = value
            bits ^= bit
        dp[mask] = cut + best

    optimum = dp[size - 1]
    mask = size - 1
    reverse_order = []

    while mask:
        cut = 0
        for u, v, w in local_edges:
            if bool(mask & (1 << u)) != bool(mask & (1 << v)):
                cut += w

        target = dp[mask] - cut
        bits = mask
        chosen = 0
        while bits:
            bit = bits & -bits
            if dp[mask ^ bit] == target:
                chosen = bit
                break
            bits ^= bit

        v = chosen.bit_length() - 1
        reverse_order.append(nodes[v])
        mask ^= chosen

    reverse_order.reverse()
    return reverse_order, optimum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, budget = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]
    edges = []
    effective_edges = 0

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            continue
        edges.append((u, v))
        effective_edges += 1
        adj[u][v] = adj[u].get(v, 0) + 1
        adj[v][u] = adj[v].get(u, 0) + 1

    if effective_edges > budget:
        print("NO")
        return

    identity = list(range(n))
    if placement_cost(identity, edges) <= budget:
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
        component = []
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        components.append(component)

    # A fast Cuthill-McKee-style candidate can avoid exponential work
    # when the budget is generous.
    heuristic_order = []
    for component in components:
        if len(component) <= 1:
            heuristic_order.extend(component)
            continue

        remaining = set(component)
        while remaining:
            start = min(remaining, key=lambda x: (len(adj[x]), x))
            remaining.remove(start)
            queue = deque([start])
            while queue:
                u = queue.popleft()
                heuristic_order.append(u)
                nxt = [v for v in adj[u] if v in remaining]
                nxt.sort(key=lambda x: (len(adj[x]), x))
                for v in nxt:
                    remaining.remove(v)
                    queue.append(v)

    if placement_cost(heuristic_order, edges) <= budget:
        positions = [0] * n
        for i, v in enumerate(heuristic_order, 1):
            positions[v] = i
        print("YES")
        print(*positions)
        return

    final_order = []
    minimum_cost = 0

    for component in components:
        order, cost = exact_component(component, adj)
        minimum_cost += cost
        if minimum_cost > budget:
            print("NO")
            return
        final_order.extend(order)

    positions = [0] * n
    for i, v in enumerate(final_order, 1):
        positions[v] = i

    print("YES")
    print(*positions)

if __name__ == "__main__":
    main()
import sys
import heapq
from array import array


def order_cost(order, adj):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    total = 0
    for u in range(len(adj)):
        pu = pos[u]
        for v, w in adj[u]:
            if u < v:
                total += w * abs(pu - pos[v])
    return total


def adjacent_improve(order, adj, rounds=10):
    k = len(order)
    order = order[:]
    pos = [0] * k
    for i, v in enumerate(order):
        pos[v] = i

    for _ in range(rounds):
        changed = False
        for i in range(k - 1):
            a = order[i]
            b = order[i + 1]
            delta = 0

            for x, w in adj[a]:
                if x == b:
                    continue
                if pos[x] < i:
                    delta += w
                else:
                    delta -= w

            for x, w in adj[b]:
                if x == a:
                    continue
                if pos[x] < i:
                    delta -= w
                else:
                    delta += w

            if delta < 0:
                order[i], order[i + 1] = b, a
                pos[a], pos[b] = i + 1, i
                changed = True

        if not changed:
            break

    return order


def barycentric_improve(initial, adj, iterations=12):
    k = len(initial)
    order = initial[:]
    best = adjacent_improve(order, adj)
    best_cost = order_cost(best, adj)

    for _ in range(iterations):
        pos = [0] * k
        for i, v in enumerate(order):
            pos[v] = i

        def key(v):
            if not adj[v]:
                return (pos[v], pos[v])
            weighted_sum = 0
            weight = 0
            for x, w in adj[v]:
                weighted_sum += w * pos[x]
                weight += w
            return (weighted_sum / weight, pos[v])

        new_order = sorted(order, key=key)
        if new_order == order:
            break
        order = new_order

        candidate = adjacent_improve(order, adj, 4)
        c = order_cost(candidate, adj)
        if c < best_cost:
            best = candidate
            best_cost = c

    return best


def heuristic_order(adj):
    k = len(adj)
    degree = [sum(w for _, w in adj[v]) for v in range(k)]
    delta = degree[:]
    selected = [False] * k
    heap = [(delta[v], degree[v], v) for v in range(k)]
    heapq.heapify(heap)
    order = []

    while heap:
        d, _, v = heapq.heappop(heap)
        if selected[v] or d != delta[v]:
            continue
        selected[v] = True
        order.append(v)
        for u, w in adj[v]:
            if not selected[u]:
                delta[u] -= 2 * w
                heapq.heappush(heap, (delta[u], degree[u], u))

    candidates = [
        adjacent_improve(order, adj),
        barycentric_improve(order, adj),
        barycentric_improve(list(range(k)), adj),
        barycentric_improve(sorted(range(k), key=lambda v: (degree[v], v)), adj),
    ]

    best = candidates[0]
    best_cost = order_cost(best, adj)
    for candidate in candidates[1:]:
        c = order_cost(candidate, adj)
        if c < best_cost:
            best = candidate
            best_cost = c
    return best, best_cost


def exact_order(adj):
    k = len(adj)
    size = 1 << k

    degree = [0] * k
    masks = [0] * k
    simple = True

    for v in range(k):
        seen = 0
        for u, w in adj[v]:
            degree[v] += w
            bit = 1 << u
            if seen & bit or w != 1:
                simple = False
            seen |= bit
        masks[v] = seen

    cuts = array('q', [0]) * size

    if simple:
        for s in range(1, size):
            lb = s & -s
            v = lb.bit_length() - 1
            t = s ^ lb
            cuts[s] = cuts[t] + degree[v] - 2 * ((masks[v] & t).bit_count())
    else:
        for s in range(1, size):
            lb = s & -s
            v = lb.bit_length() - 1
            t = s ^ lb
            inside = 0
            for u, w in adj[v]:
                if t & (1 << u):
                    inside += w
            cuts[s] = cuts[t] + degree[v] - 2 * inside

    inf = (1 << 62)
    dp = array('q', [inf]) * size
    parent = array('b', [-1]) * size
    dp[0] = 0

    for s in range(1, size):
        x = s
        best = inf
        best_v = -1
        while x:
            lb = x & -x
            v = lb.bit_length() - 1
            value = dp[s ^ lb]
            if value < best:
                best = value
                best_v = v
            x ^= lb
        dp[s] = best + cuts[s]
        parent[s] = best_v

    order_rev = []
    s = size - 1
    while s:
        v = parent[s]
        order_rev.append(v)
        s ^= 1 << v
    order_rev.reverse()
    return order_rev, dp[size - 1]


def main():
    input_stream = sys.stdin.buffer
    first = input_stream.readline().split()
    if not first:
        return

    n, m, budget = map(int, first)

    edge_weights = {}
    for _ in range(m):
        u, v = map(int, input_stream.readline().split())
        u -= 1
        v -= 1
        if u > v:
            u, v = v, u
        key = u * n + v
        edge_weights[key] = edge_weights.get(key, 0) + 1

    total_links = sum(edge_weights.values())
    if total_links > budget:
        print("NO")
        return

    global_adj = [[] for _ in range(n)]
    for key, w in edge_weights.items():
        u, v = divmod(key, n)
        global_adj[u].append((v, w))
        global_adj[v].append((u, w))
    del edge_weights

    visited = [False] * n
    components = []
    isolated = []

    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        if not global_adj[start]:
            isolated.append(start)
            continue

        stack = [start]
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for u, _ in global_adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)
        components.append(component)

    component_data = []
    heuristic_total = 0

    for vertices in components:
        index = {v: i for i, v in enumerate(vertices)}
        local_adj = [[] for _ in vertices]
        for i, v in enumerate(vertices):
            for u, w in global_adj[v]:
                local_adj[i].append((index[u], w))

        local_order, local_cost = heuristic_order(local_adj)
        heuristic_total += local_cost
        component_data.append((vertices, local_adj, local_order, local_cost))

    if heuristic_total <= budget:
        final_order = []
        for vertices, _, local_order, _ in component_data:
            final_order.extend(vertices[i] for i in local_order)
        final_order.extend(isolated)

        assignment = [0] * n
        for position, module in enumerate(final_order, 1):
            assignment[module] = position

        print("YES")
        print(*assignment)
        return

    operation_estimate = 0
    exact_possible = True
    for vertices, _, _, _ in component_data:
        k = len(vertices)
        if k > 21:
            exact_possible = False
            break
        operation_estimate += k * (1 << max(0, k - 1))
        if operation_estimate > 30_000_000:
            exact_possible = False
            break

    if not exact_possible:
        print("NO")
        return

    exact_total = 0
    exact_orders = []

    for vertices, local_adj, _, _ in component_data:
        local_order, local_cost = exact_order(local_adj)
        exact_total += local_cost
        exact_orders.append((vertices, local_order))
        if exact_total > budget:
            print("NO")
            return

    final_order = []
    for vertices, local_order in exact_orders:
        final_order.extend(vertices[i] for i in local_order)
    final_order.extend(isolated)

    assignment = [0] * n
    for position, module in enumerate(final_order, 1):
        assignment[module] = position

    print("YES")
    print(*assignment)


if __name__ == "__main__":
    main()
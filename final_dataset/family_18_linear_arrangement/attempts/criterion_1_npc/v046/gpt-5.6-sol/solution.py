import sys
from array import array
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, B = data[0], data[1], data[2]
    adj = [dict() for _ in range(n)]
    edges = []
    effective_edges = 0

    p = 3
    for _ in range(m):
        x = data[p] - 1
        y = data[p + 1] - 1
        p += 2
        if x == y:
            continue
        edges.append((x, y))
        effective_edges += 1
        adj[x][y] = adj[x].get(y, 0) + 1
        adj[y][x] = adj[y].get(x, 0) + 1

    if B < 0 or effective_edges > B:
        print("NO")
        return

    def output_order(order):
        pos = [0] * n
        for i, v in enumerate(order, 1):
            pos[v] = i
        print("YES")
        print(*pos)

    identity_cost = sum(abs(x - y) for x, y in edges)
    if identity_cost <= B:
        output_order(list(range(n)))
        return

    seen = [False] * n
    components = []

    for start in range(n):
        if seen[start]:
            continue
        seen[start] = True
        stack = [start]
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = True
                    stack.append(u)
        components.append(comp)

    components.sort(key=len, reverse=True)

    def order_cost(order):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        return sum(abs(pos[x] - pos[y]) for x, y in edges)

    grouped_order = []
    for comp in components:
        grouped_order.extend(sorted(comp))
    if order_cost(grouped_order) <= B:
        output_order(grouped_order)
        return

    rcm_order = []
    for comp in components:
        if len(comp) <= 1:
            rcm_order.extend(comp)
            continue

        degrees = {v: sum(adj[v].values()) for v in comp}
        unused = set(comp)
        local_order = []

        while unused:
            start = min(unused, key=lambda v: (degrees[v], v))
            unused.remove(start)
            q = deque([start])

            while q:
                v = q.popleft()
                local_order.append(v)
                neighbors = [u for u in adj[v] if u in unused]
                neighbors.sort(key=lambda u: (degrees[u], u))
                for u in neighbors:
                    unused.remove(u)
                    q.append(u)

        local_order.reverse()
        rcm_order.extend(local_order)

    if order_cost(rcm_order) <= B:
        output_order(rcm_order)
        return

    def solve_component(comp, limit):
        k = len(comp)
        if k <= 1:
            return comp, 0

        index = {v: i for i, v in enumerate(comp)}
        masks = [0] * k
        degrees = [0] * k
        extras = [[] for _ in range(k)]
        edge_weight = 0

        for i, v in enumerate(comp):
            for u, w in adj[v].items():
                j = index[u]
                masks[i] |= 1 << j
                degrees[i] += w
                if w > 1:
                    extras[i].append((j, w - 1))
                if i < j:
                    edge_weight += w

        theoretical = edge_weight * (k - 1)
        cap = min(limit, theoretical)
        inf = cap + 1
        size = 1 << k

        typecode = 'i' if inf <= 2147483647 and edge_weight <= 2147483647 else 'q'
        cuts = array(typecode, [0]) * size
        dp = array(typecode, [inf]) * size
        dp[0] = 0

        masks_l = masks
        degrees_l = degrees
        extras_l = extras
        cuts_l = cuts
        dp_l = dp
        inf_l = inf

        for s in range(1, size):
            bit = s & -s
            v = bit.bit_length() - 1
            rest = s ^ bit

            inside = (masks_l[v] & rest).bit_count()
            for j, extra in extras_l[v]:
                if rest & (1 << j):
                    inside += extra

            cut = cuts_l[rest] + degrees_l[v] - (inside << 1)
            cuts_l[s] = cut

            best = inf_l
            t = s
            while t:
                b = t & -t
                prev = dp_l[s ^ b]
                value = prev + cut
                if value < best:
                    best = value
                t ^= b

            if best > inf_l:
                best = inf_l
            dp_l[s] = best

        full = size - 1
        minimum = dp_l[full]
        if minimum > limit or minimum >= inf_l:
            return None, minimum

        reversed_order = []
        s = full
        while s:
            cut = cuts_l[s]
            target = dp_l[s]
            t = s
            chosen = 0

            while t:
                b = t & -t
                if dp_l[s ^ b] + cut == target:
                    chosen = b
                    break
                t ^= b

            if chosen == 0:
                return None, inf_l

            reversed_order.append(comp[chosen.bit_length() - 1])
            s ^= chosen

        reversed_order.reverse()
        return reversed_order, minimum

    final_order = []
    remaining = B

    for comp in components:
        if len(comp) == 1:
            final_order.append(comp[0])
            continue

        comp_order, minimum = solve_component(comp, remaining)
        if comp_order is None:
            print("NO")
            return

        remaining -= minimum
        final_order.extend(comp_order)

    output_order(final_order)

if __name__ == "__main__":
    main()
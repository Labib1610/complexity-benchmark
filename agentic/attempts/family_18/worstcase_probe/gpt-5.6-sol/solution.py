import sys
from array import array
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    n, m, B = data[0], data[1], data[2]
    parent = list(range(n))
    size = [1] * n
    adj = [dict() for _ in range(n)]
    nonloop_edges = 0

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    idx = 3
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        if u == v:
            continue
        nonloop_edges += 1
        adj[u][v] = adj[u].get(v, 0) + 1
        adj[v][u] = adj[v].get(u, 0) + 1
        union(u, v)

    if B < 0 or nonloop_edges > B:
        print("NO")
        return

    groups = {}
    for v in range(n):
        r = find(v)
        groups.setdefault(r, []).append(v)

    components = list(groups.values())

    def positions_from_order(order):
        pos = [0] * n
        for i, v in enumerate(order, 1):
            pos[v] = i
        return pos

    def arrangement_cost(order):
        pos = positions_from_order(order)
        total = 0
        for u in range(n):
            pu = pos[u]
            for v, w in adj[u].items():
                if u < v:
                    total += w * abs(pu - pos[v])
                    if total > B:
                        return total
        return total

    natural_order = []
    for comp in components:
        natural_order.extend(comp)

    if arrangement_cost(natural_order) <= B:
        pos = positions_from_order(natural_order)
        print("YES")
        print(*pos)
        return

    rcm_order = []
    for comp in components:
        if len(comp) <= 1:
            rcm_order.extend(comp)
            continue
        start = min(comp, key=lambda x: (len(adj[x]), x))
        seen = {start}
        q = deque([start])
        part = []
        while q:
            u = q.popleft()
            part.append(u)
            nxt = [v for v in adj[u] if v not in seen]
            nxt.sort(key=lambda x: (len(adj[x]), x))
            for v in nxt:
                seen.add(v)
                q.append(v)
        rcm_order.extend(part)

    if arrangement_cost(rcm_order) <= B:
        pos = positions_from_order(rcm_order)
        print("YES")
        print(*pos)
        return

    def solve_component(comp, cap):
        k = len(comp)
        if k <= 1:
            return comp[:], 0

        local = {v: i for i, v in enumerate(comp)}
        local_adj = [[] for _ in range(k)]
        unique_degree = [0] * k
        weighted_degree = [0] * k
        masks = [0] * k
        all_unit = True
        edge_weight_sum = 0
        unique_edges = 0

        for i, u in enumerate(comp):
            for v, w in adj[u].items():
                j = local.get(v)
                if j is None:
                    continue
                local_adj[i].append((j, w))
                unique_degree[i] += 1
                weighted_degree[i] += w
                masks[i] |= 1 << j
                if w != 1:
                    all_unit = False
                if i < j:
                    edge_weight_sum += w
                    unique_edges += 1

        # A path can place every edge at distance one, attaining the universal lower bound.
        if max(unique_degree) <= 2:
            endpoint = next((i for i in range(k) if unique_degree[i] <= 1), 0)
            order_local = []
            prev = -1
            cur = endpoint
            while cur != -1:
                order_local.append(cur)
                nxt = -1
                for v, _ in local_adj[cur]:
                    if v != prev:
                        nxt = v
                        break
                prev, cur = cur, nxt
            if edge_weight_sum > cap:
                return None, edge_weight_sum
            return [comp[i] for i in order_local], edge_weight_sum

        # In a complete graph with equal multiplicity, every ordering has the same cost.
        if unique_edges == k * (k - 1) // 2:
            first_weight = local_adj[0][0][1]
            uniform = all(w == first_weight for row in local_adj for _, w in row)
            if uniform:
                cost = first_weight * k * (k * k - 1) // 6
                if cost > cap:
                    return None, cost
                return comp[:], cost

        total_states = 1 << k
        cut = array('I', [0]) * total_states

        if all_unit:
            for s in range(1, total_states):
                bit = s & -s
                i = bit.bit_length() - 1
                p = s ^ bit
                cut[s] = cut[p] + weighted_degree[i] - 2 * ((masks[i] & p).bit_count())
        else:
            for s in range(1, total_states):
                bit = s & -s
                i = bit.bit_length() - 1
                p = s ^ bit
                inside = 0
                for j, w in local_adj[i]:
                    if p & (1 << j):
                        inside += w
                cut[s] = cut[p] + weighted_degree[i] - 2 * inside

        inf = cap + 1
        dp = array('Q', [inf]) * total_states
        dp[0] = 0

        for s in range(1, total_states):
            bits = s
            best = inf
            while bits:
                bit = bits & -bits
                p = s ^ bit
                value = dp[p] + cut[p]
                if value < best:
                    best = value
                bits ^= bit
            if best <= cap:
                dp[s] = best

        full = total_states - 1
        if dp[full] == inf:
            return None, inf

        reversed_order = []
        s = full
        while s:
            bits = s
            chosen = -1
            while bits:
                bit = bits & -bits
                p = s ^ bit
                if dp[p] != inf and dp[s] == dp[p] + cut[p]:
                    chosen = bit.bit_length() - 1
                    s = p
                    break
                bits ^= bit
            if chosen < 0:
                return None, inf
            reversed_order.append(chosen)

        reversed_order.reverse()
        return [comp[i] for i in reversed_order], dp[full]

    final_order = []
    total_cost = 0

    components.sort(key=lambda c: (len(c) == 1, -len(c)))

    for comp in components:
        remaining = B - total_cost
        order, cost = solve_component(comp, remaining)
        if order is None or total_cost + cost > B:
            print("NO")
            return
        final_order.extend(order)
        total_cost += cost

    pos = positions_from_order(final_order)
    print("YES")
    print(*pos)

if __name__ == "__main__":
    main()
import sys
import random

sys.setrecursionlimit(1_000_000)


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        f = [v, len(self.g[v]), cap]
        r = [u, len(self.g[u]), 0]
        self.g[u].append(f)
        self.g[v].append(r)
        return f

    def max_flow(self, s, t, limit):
        if s == t:
            return limit
        flow = 0
        n = self.n
        g = self.g

        while flow < limit:
            level = [-1] * n
            level[s] = 0
            q = [s]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for e in g[u]:
                    if e[2] > 0 and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1
                        q.append(e[0])

            if level[t] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(g[u]):
                    e = g[u][it[u]]
                    if e[2] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[2]))
                        if got:
                            e[2] -= got
                            g[e[0]][e[1]][2] += got
                            return got
                    it[u] += 1
                return 0

            while flow < limit:
                pushed = dfs(s, limit - flow)
                if not pushed:
                    break
                flow += pushed

        return flow


def route_flow(n, edges, capacities, s, t, demand, need_usage=False):
    if demand == 0 or s == t:
        return (True, [0] * len(edges)) if need_usage else True

    dinic = Dinic(n)
    refs = []
    for (u, v, _), cap in zip(edges, capacities):
        refs.append(dinic.add_edge(u, v, cap))

    got = dinic.max_flow(s, t, demand)
    if got != demand:
        return (False, None) if need_usage else False

    if not need_usage:
        return True

    usage = [capacities[i] - refs[i][2] for i in range(len(edges))]
    return True, usage


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    orders = []
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        orders.append((s, t, d))

    edges = []
    adjacency = [[] for _ in range(n)]
    capacities = []
    for eid in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v, c))
        capacities.append(c)
        if c > 0 and u != v:
            adjacency[u].append((v, eid))

    answer = [[0] * m for _ in range(k)]
    active = [i for i, (s, t, d) in enumerate(orders) if d > 0 and s != t]

    for i in active:
        s, t, d = orders[i]
        if not route_flow(n, edges, capacities, s, t, d):
            print("NO")
            return

    def greedy(order):
        residual = capacities[:]
        result = [[0] * m for _ in range(k)]
        for idx in order:
            s, t, d = orders[idx]
            ok, usage = route_flow(n, edges, residual, s, t, d, True)
            if not ok:
                return None
            result[idx] = usage
            for e in range(m):
                residual[e] -= usage[e]
        return result

    base_orders = []
    if active:
        base_orders.append(active[:])
        base_orders.append(list(reversed(active)))
        base_orders.append(sorted(active, key=lambda i: -orders[i][2]))
        base_orders.append(sorted(active, key=lambda i: orders[i][2]))

        rng = random.Random(712367821)
        for _ in range(12):
            cur = active[:]
            rng.shuffle(cur)
            base_orders.append(cur)

    seen_orders = set()
    for order in base_orders:
        key = tuple(order)
        if key in seen_orders:
            continue
        seen_orders.add(key)
        got = greedy(order)
        if got is not None:
            print("YES")
            out = [" ".join(map(str, row)) for row in got]
            sys.stdout.write("\n".join(out))
            return

    paths_by_commodity = {}

    def enumerate_paths(s, t):
        paths = []
        visited = [False] * n
        visited[s] = True
        current = []

        def dfs(u):
            if u == t:
                paths.append(tuple(current))
                return
            for v, eid in adjacency[u]:
                if not visited[v]:
                    visited[v] = True
                    current.append(eid)
                    dfs(v)
                    current.pop()
                    visited[v] = False

        dfs(s)

        unique = {}
        for p in paths:
            mask = 0
            for eid in p:
                mask |= 1 << eid
            if mask not in unique:
                unique[mask] = p

        items = sorted(unique.items(), key=lambda z: (z[0].bit_count(), len(z[1])))
        kept = []
        kept_masks = []
        for mask, p in items:
            dominated = False
            for km in kept_masks:
                if km & mask == km:
                    dominated = True
                    break
            if not dominated:
                kept_masks.append(mask)
                kept.append(p)

        kept.sort(key=lambda p: (-min(capacities[e] for e in p), len(p)))
        return kept

    for idx in active:
        s, t, _ = orders[idx]
        plist = enumerate_paths(s, t)
        if not plist:
            print("NO")
            return
        paths_by_commodity[idx] = plist

    exact_order = sorted(
        active,
        key=lambda i: (len(paths_by_commodity[i]), -orders[i][2])
    )

    residual = capacities[:]
    failed_boundary = set()

    def future_possible(pos):
        for q in range(pos, len(exact_order)):
            idx = exact_order[q]
            s, t, d = orders[idx]
            if not route_flow(n, edges, residual, s, t, d):
                return False
        return True

    def solve_commodity(pos):
        if pos == len(exact_order):
            return True

        state = (pos, tuple(residual))
        if state in failed_boundary:
            return False

        if not future_possible(pos):
            failed_boundary.add(state)
            return False

        idx = exact_order[pos]
        demand = orders[idx][2]
        plist = paths_by_commodity[idx]
        plen = len(plist)

        def assign(start, rem):
            if rem == 0:
                return solve_commodity(pos + 1)
            if start >= plen:
                return False

            bottlenecks = [0] * plen
            total_bound = 0
            for j in range(start, plen):
                b = rem
                for eid in plist[j]:
                    if residual[eid] < b:
                        b = residual[eid]
                    if b == 0:
                        break
                bottlenecks[j] = b
                total_bound += b

            if total_bound < rem:
                return False

            suffix = [0] * (plen + 1)
            for j in range(plen - 1, start - 1, -1):
                suffix[j] = suffix[j + 1] + bottlenecks[j]

            for j in range(start, plen):
                upper = min(rem, bottlenecks[j])
                if upper <= 0:
                    continue
                lower = max(1, rem - suffix[j + 1])
                if lower > upper:
                    continue

                path = plist[j]
                for amount in range(upper, lower - 1, -1):
                    for eid in path:
                        residual[eid] -= amount
                        answer[idx][eid] += amount

                    if assign(j + 1, rem - amount):
                        return True

                    for eid in path:
                        residual[eid] += amount
                        answer[idx][eid] -= amount

            return False

        if assign(0, demand):
            return True

        failed_boundary.add(state)
        return False

    if solve_commodity(0):
        print("YES")
        sys.stdout.write("\n".join(" ".join(map(str, row)) for row in answer))
    else:
        print("NO")


if __name__ == "__main__":
    main()
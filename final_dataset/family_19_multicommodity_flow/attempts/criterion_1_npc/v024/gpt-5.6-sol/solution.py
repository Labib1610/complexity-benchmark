import sys
import random
import time

sys.setrecursionlimit(1_000_000)


class Dinic:
    __slots__ = ("n", "g", "level", "it")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        gu = self.g[u]
        gv = self.g[v]
        ui = len(gu)
        vi = len(gv)
        gu.append([v, vi, cap])
        gv.append([u, ui, 0])
        return ui

    def max_flow(self, s, t, limit):
        if s == t or limit <= 0:
            return limit

        total = 0
        n = self.n
        g = self.g
        level = self.level
        it = self.it

        while total < limit:
            for i in range(n):
                level[i] = -1
            level[s] = 0
            q = [s]
            head = 0

            while head < len(q):
                u = q[head]
                head += 1
                nl = level[u] + 1
                for e in g[u]:
                    if e[2] > 0 and level[e[0]] < 0:
                        level[e[0]] = nl
                        q.append(e[0])

            if level[t] < 0:
                break

            for i in range(n):
                it[i] = 0

            def dfs(u, pushed):
                if u == t:
                    return pushed
                edges = g[u]
                while it[u] < len(edges):
                    idx = it[u]
                    e = edges[idx]
                    if e[2] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[2]))
                        if got:
                            e[2] -= got
                            g[e[0]][e[1]][2] += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(s, limit - total)
                if not pushed:
                    break
                total += pushed

        return total


def route_one(n, edges, capacities, s, t, demand, randomized):
    m = len(edges)
    if demand == 0 or s == t:
        return [0] * m

    order = list(range(m))
    if randomized:
        random.shuffle(order)

    dinic = Dinic(n)
    refs = [None] * m

    for eid in order:
        cap = capacities[eid]
        if cap <= 0:
            continue
        u, v = edges[eid]
        pos = dinic.add_edge(u, v, cap)
        refs[eid] = (u, pos)

    if dinic.max_flow(s, t, demand) != demand:
        return None

    result = [0] * m
    for eid, ref in enumerate(refs):
        if ref is not None:
            u, pos = ref
            result[eid] = capacities[eid] - dinic.g[u][pos][2]
    return result


def attempt(n, edges, caps, requests, order, randomized, deadline):
    m = len(edges)
    remaining = caps[:]
    answer = [[0] * m for _ in requests]

    for idx in order:
        if time.monotonic() >= deadline:
            return None, idx, True

        s, t, demand = requests[idx]
        flow = route_one(n, edges, remaining, s, t, demand, randomized)
        if flow is None:
            return None, idx, False

        answer[idx] = flow
        for e, value in enumerate(flow):
            remaining[e] -= value

    return answer, -1, False


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    p = 0
    n, m, k = data[p], data[p + 1], data[p + 2]
    p += 3

    requests = []
    for _ in range(k):
        s, t, d = data[p], data[p + 1], data[p + 2]
        p += 3
        requests.append((s - 1, t - 1, d))

    edges = []
    caps = []
    for _ in range(m):
        u, v, cap = data[p], data[p + 1], data[p + 2]
        p += 3
        edges.append((u - 1, v - 1))
        caps.append(cap)

    if k == 0:
        sys.stdout.write("YES\n")
        return

    start = time.monotonic()
    deadline = start + 4.55
    rng_seed = 1469598103934665603
    for x in data[:min(len(data), 10000)]:
        rng_seed ^= x
        rng_seed = (rng_seed * 1099511628211) & ((1 << 64) - 1)
    random.seed(rng_seed)

    base_orders = [
        list(range(k)),
        sorted(range(k), key=lambda i: requests[i][2], reverse=True),
        sorted(range(k), key=lambda i: requests[i][2]),
    ]

    last_failed = -1
    trial = 0
    answer = None

    while trial < 5000 and time.monotonic() < deadline:
        if trial < len(base_orders):
            order = base_orders[trial][:]
            randomized = trial != 0
        else:
            order = list(range(k))
            random.shuffle(order)
            if last_failed >= 0 and trial % 3 != 0:
                pos = order.index(last_failed)
                order[0], order[pos] = order[pos], order[0]
            randomized = True

        answer, failed, timed_out = attempt(
            n, edges, caps, requests, order, randomized, deadline
        )
        if answer is not None:
            break
        if timed_out:
            break
        last_failed = failed
        trial += 1

    if answer is None:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    for row in answer:
        out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
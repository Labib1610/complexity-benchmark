import sys
import time
import random
from collections import deque

sys.setrecursionlimit(1_000_000)


class Edge:
    __slots__ = ("to", "rev", "cap", "initial")

    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.initial = cap


class Dinic:
    __slots__ = ("n", "g", "level", "it")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        forward = Edge(v, len(self.g[v]), cap)
        backward = Edge(u, len(self.g[u]), 0)
        self.g[u].append(forward)
        self.g[v].append(backward)
        return forward

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            nl = level[u] + 1
            for e in self.g[u]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = nl
                    if e.to == t:
                        return True
                    q.append(e.to)
        return level[t] >= 0

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        g = self.g
        level = self.level
        i = self.it[u]
        while i < len(g[u]):
            self.it[u] = i
            e = g[u][i]
            if e.cap > 0 and level[e.to] == level[u] + 1:
                got = self.dfs(e.to, t, min(pushed, e.cap))
                if got:
                    e.cap -= got
                    g[e.to][e.rev].cap += got
                    return got
            i += 1
            self.it[u] = i
        return 0

    def max_flow(self, s, t, limit):
        flow = 0
        inf = 10**30
        while flow < limit and self.bfs(s, t):
            self.it = [0] * self.n
            while flow < limit:
                pushed = self.dfs(s, t, min(inf, limit - flow))
                if not pushed:
                    break
                flow += pushed
        return flow


def aggregate_solution(n, m, batches, edges, common_source):
    total = sum(d for _, _, d in batches)
    extra = n
    dinic = Dinic(n + 1)
    refs = [None] * m

    for j, (u, v, cap) in enumerate(edges):
        if cap > 0 and u != v:
            refs[j] = dinic.add_edge(u, v, cap)

    if common_source:
        source = batches[0][0] if batches else 0
        sink = extra
        for _, t, d in batches:
            if d:
                dinic.add_edge(t, sink, d)
    else:
        source = extra
        sink = batches[0][1] if batches else 0
        for s, _, d in batches:
            if d:
                dinic.add_edge(source, s, d)

    if dinic.max_flow(source, sink, total) != total:
        return None

    remaining = [0] * m
    outgoing = [[] for _ in range(n)]
    for j, (u, v, _) in enumerate(edges):
        ref = refs[j]
        if ref is not None:
            used = ref.initial - ref.cap
            remaining[j] = used
            if used:
                outgoing[u].append(j)

    result = [[0] * m for _ in batches]

    for idx, (s, t, demand) in enumerate(batches):
        need = demand
        while need > 0:
            parent_node = [-1] * n
            parent_edge = [-1] * n
            parent_node[s] = s
            q = deque([s])

            while q and parent_node[t] == -1:
                u = q.popleft()
                for eid in outgoing[u]:
                    if remaining[eid] <= 0:
                        continue
                    v = edges[eid][1]
                    if parent_node[v] == -1:
                        parent_node[v] = u
                        parent_edge[v] = eid
                        q.append(v)
                        if v == t:
                            break

            if parent_node[t] == -1:
                return None

            amount = need
            v = t
            while v != s:
                eid = parent_edge[v]
                amount = min(amount, remaining[eid])
                v = parent_node[v]

            v = t
            while v != s:
                eid = parent_edge[v]
                remaining[eid] -= amount
                result[idx][eid] += amount
                v = parent_node[v]

            need -= amount

    return result


def sequential_attempt(n, m, batches, edges, order, edge_order):
    remaining = [cap for _, _, cap in edges]
    result = [[0] * m for _ in batches]

    for idx in order:
        s, t, demand = batches[idx]
        if demand == 0:
            continue

        dinic = Dinic(n)
        refs = [None] * m

        for eid in edge_order:
            u, v, _ = edges[eid]
            cap = remaining[eid]
            if cap > 0 and u != v:
                refs[eid] = dinic.add_edge(u, v, cap)

        if dinic.max_flow(s, t, demand) != demand:
            return None

        row = result[idx]
        for eid, ref in enumerate(refs):
            if ref is not None:
                used = ref.initial - ref.cap
                if used:
                    row[eid] = used
                    remaining[eid] -= used

    return result


def main():
    start_time = time.monotonic()
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    batches = []
    invalid = False
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        if d < 0 or (s == t and d > 0):
            invalid = True
        batches.append((s, t, d))

    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        if cap < 0:
            invalid = True
        edges.append((u, v, cap))

    if invalid:
        print("NO")
        return

    active = [i for i, (_, _, d) in enumerate(batches) if d > 0]
    if not active:
        print("YES")
        zero_line = " ".join(["0"] * m)
        for _ in range(k):
            print(zero_line)
        return

    same_source = all(batches[i][0] == batches[active[0]][0] for i in active)
    same_target = all(batches[i][1] == batches[active[0]][1] for i in active)

    answer = None
    if same_source:
        answer = aggregate_solution(n, m, batches, edges, True)
        if answer is None:
            print("NO")
            return
    elif same_target:
        answer = aggregate_solution(n, m, batches, edges, False)
        if answer is None:
            print("NO")
            return
    else:
        base_edges = list(range(m))
        by_desc = sorted(active, key=lambda i: (-batches[i][2], i))
        by_asc = sorted(active, key=lambda i: (batches[i][2], i))
        reverse_active = list(reversed(active))

        plans = [
            (active, base_edges),
            (by_desc, base_edges),
            (by_asc, base_edges),
            (reverse_active, base_edges),
            (active, list(reversed(base_edges))),
            (by_desc, list(reversed(base_edges))),
        ]

        deadline = start_time + 4.75
        for order, edge_order in plans:
            answer = sequential_attempt(n, m, batches, edges, order, edge_order)
            if answer is not None:
                break
            if time.monotonic() >= deadline:
                break

        rng = random.Random(0x5EEDC0DE)
        attempts = 0
        while answer is None and time.monotonic() < deadline and attempts < 200:
            order = active[:]
            edge_order = base_edges[:]
            rng.shuffle(order)
            rng.shuffle(edge_order)
            answer = sequential_attempt(n, m, batches, edges, order, edge_order)
            attempts += 1

        if answer is None:
            print("NO")
            return

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
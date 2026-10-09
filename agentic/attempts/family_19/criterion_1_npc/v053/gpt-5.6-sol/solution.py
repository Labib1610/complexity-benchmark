import sys
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
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        forward = Edge(v, len(self.g[v]), cap)
        backward = Edge(u, len(self.g[u]), 0)
        self.g[u].append(forward)
        self.g[v].append(backward)
        return forward

    def max_flow(self, source, sink, limit=None):
        if source == sink:
            return 0
        if limit is None:
            limit = 10**100

        total = 0
        n = self.n
        while total < limit:
            level = [-1] * n
            level[source] = 0
            q = deque([source])

            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[u] + 1
                        q.append(e.to)

            if level[sink] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == sink:
                    return pushed
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    if e.cap > 0 and level[e.to] == level[u] + 1:
                        got = dfs(e.to, min(pushed, e.cap))
                        if got:
                            e.cap -= got
                            self.g[e.to][e.rev].cap += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(source, limit - total)
                if not pushed:
                    break
                total += pushed

        return total


def build_and_maxflow(n, edges, source, sink, limit=None):
    dinic = Dinic(n)
    refs = []
    for u, v, cap in edges:
        refs.append(dinic.add_edge(u, v, cap))
    value = dinic.max_flow(source, sink, limit)
    return value, refs


def solve_common_source(n, m, commodities, edges):
    source = commodities[0][0]
    terminal = n
    dinic = Dinic(n + 1)

    refs = []
    for u, v, cap in edges:
        refs.append(dinic.add_edge(u, v, cap))

    total = 0
    for _, t, d in commodities:
        dinic.add_edge(t, terminal, d)
        total += d

    if dinic.max_flow(source, terminal, total) != total:
        return None

    remaining_flow = [ref.initial - ref.cap for ref in refs]
    incoming = [[] for _ in range(n)]
    for eid, (u, v, _) in enumerate(edges):
        incoming[v].append((u, eid))

    answer = [[0] * m for _ in commodities]

    for i, (_, target, demand) in enumerate(commodities):
        rem = demand
        if target == source:
            continue

        while rem > 0:
            parent_node = [-1] * n
            parent_edge = [-1] * n
            parent_node[target] = target
            q = deque([target])

            while q and parent_node[source] == -1:
                v = q.popleft()
                for u, eid in incoming[v]:
                    if remaining_flow[eid] > 0 and parent_node[u] == -1:
                        parent_node[u] = v
                        parent_edge[u] = eid
                        q.append(u)

            if parent_node[source] == -1:
                return None

            path = []
            u = source
            amount = rem
            while u != target:
                eid = parent_edge[u]
                path.append(eid)
                amount = min(amount, remaining_flow[eid])
                u = parent_node[u]

            for eid in path:
                remaining_flow[eid] -= amount
                answer[i][eid] += amount
            rem -= amount

    return answer


def solve_common_sink(n, m, commodities, edges):
    source = n
    sink = commodities[0][1]
    dinic = Dinic(n + 1)

    refs = []
    for u, v, cap in edges:
        refs.append(dinic.add_edge(u, v, cap))

    total = 0
    for s, _, d in commodities:
        dinic.add_edge(source, s, d)
        total += d

    if dinic.max_flow(source, sink, total) != total:
        return None

    remaining_flow = [ref.initial - ref.cap for ref in refs]
    outgoing = [[] for _ in range(n)]
    for eid, (u, v, _) in enumerate(edges):
        outgoing[u].append((v, eid))

    answer = [[0] * m for _ in commodities]

    for i, (start, _, demand) in enumerate(commodities):
        rem = demand
        if start == sink:
            continue

        while rem > 0:
            parent_node = [-1] * n
            parent_edge = [-1] * n
            parent_node[start] = start
            q = deque([start])

            while q and parent_node[sink] == -1:
                u = q.popleft()
                for v, eid in outgoing[u]:
                    if remaining_flow[eid] > 0 and parent_node[v] == -1:
                        parent_node[v] = u
                        parent_edge[v] = eid
                        q.append(v)

            if parent_node[sink] == -1:
                return None

            path = []
            v = sink
            amount = rem
            while v != start:
                eid = parent_edge[v]
                path.append(eid)
                amount = min(amount, remaining_flow[eid])
                v = parent_node[v]

            for eid in path:
                remaining_flow[eid] -= amount
                answer[i][eid] += amount
            rem -= amount

    return answer


def maxflow_with_capacities(n, edges, capacities, source, sink, limit):
    if limit <= 0 or source == sink:
        return limit

    dinic = Dinic(n)
    for eid, (u, v, _) in enumerate(edges):
        cap = capacities[eid]
        if cap > 0:
            dinic.add_edge(u, v, cap)
    return dinic.max_flow(source, sink, limit)


def aggregate_necessary_check(n, commodities, edges):
    source = n
    sink = n + 1
    dinic = Dinic(n + 2)
    for u, v, cap in edges:
        if cap > 0:
            dinic.add_edge(u, v, cap)

    total = 0
    for s, t, d in commodities:
        if d > 0:
            dinic.add_edge(source, s, d)
            dinic.add_edge(t, sink, d)
            total += d

    return dinic.max_flow(source, sink, total) == total


def enumerate_simple_paths(n, edges, outgoing, source, sink):
    if source == sink:
        return [()]

    paths = []
    visited = [False] * n
    visited[source] = True
    current = []

    def dfs(u):
        if u == sink:
            paths.append(tuple(current))
            return

        for eid in outgoing[u]:
            v = edges[eid][1]
            if not visited[v]:
                visited[v] = True
                current.append(eid)
                dfs(v)
                current.pop()
                visited[v] = False

    dfs(source)
    paths.sort(key=lambda p: (len(p), p))
    return paths


def solve_general_exact(n, m, commodities, edges):
    capacities = [cap for _, _, cap in edges]

    if not aggregate_necessary_check(n, commodities, edges):
        return None

    for s, t, d in commodities:
        if d > 0 and s != t:
            if maxflow_with_capacities(n, edges, capacities, s, t, d) < d:
                return None

    outgoing = [[] for _ in range(n)]
    for eid, (u, _, cap) in enumerate(edges):
        if cap > 0:
            outgoing[u].append(eid)

    cache = {}
    commodity_paths = []
    for s, t, d in commodities:
        if d == 0 or s == t:
            commodity_paths.append([()])
            continue
        key = (s, t)
        if key not in cache:
            cache[key] = enumerate_simple_paths(n, edges, outgoing, s, t)
        commodity_paths.append(cache[key])
        if not cache[key]:
            return None

    order = list(range(len(commodities)))
    order.sort(key=lambda i: (
        0 if commodities[i][2] == 0 or commodities[i][0] == commodities[i][1] else 1,
        len(commodity_paths[i]),
        -commodities[i][2]
    ))

    residual = capacities[:]
    answer = [[0] * m for _ in commodities]

    def solve_position(pos):
        if pos == len(order):
            return True

        ci = order[pos]
        s, t, demand = commodities[ci]
        if demand == 0 or s == t:
            return solve_position(pos + 1)

        if maxflow_with_capacities(n, edges, residual, s, t, demand) < demand:
            return False

        paths = commodity_paths[ci]

        def choose_paths(start_index, rem):
            if rem == 0:
                return solve_position(pos + 1)

            for pi in range(start_index, len(paths)):
                path = paths[pi]
                bottleneck = rem
                for eid in path:
                    if residual[eid] < bottleneck:
                        bottleneck = residual[eid]
                        if bottleneck == 0:
                            break

                if bottleneck == 0:
                    continue

                for amount in range(bottleneck, 0, -1):
                    for eid in path:
                        residual[eid] -= amount
                        answer[ci][eid] += amount

                    feasible = True
                    if rem > amount:
                        feasible = (
                            maxflow_with_capacities(
                                n, edges, residual, s, t, rem - amount
                            ) >= rem - amount
                        )

                    if feasible and choose_paths(pi + 1, rem - amount):
                        return True

                    for eid in path:
                        residual[eid] += amount
                        answer[ci][eid] -= amount

            return False

        return choose_paths(0, demand)

    if solve_position(0):
        return answer
    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    commodities = []
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        commodities.append((s, t, d))

    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges.append((u, v, cap))

    if k == 0:
        print("YES")
        return

    same_source = all(s == commodities[0][0] for s, _, _ in commodities)
    same_sink = all(t == commodities[0][1] for _, t, _ in commodities)

    if same_source:
        answer = solve_common_source(n, m, commodities, edges)
    elif same_sink:
        answer = solve_common_sink(n, m, commodities, edges)
    else:
        answer = solve_general_exact(n, m, commodities, edges)

    if answer is None:
        print("NO")
        return

    out = ["YES"]
    for row in answer:
        out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
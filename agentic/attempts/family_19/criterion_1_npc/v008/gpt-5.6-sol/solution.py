import sys
from collections import deque

sys.setrecursionlimit(200000)


class Edge:
    __slots__ = ("to", "rev", "cap")

    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


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

    def max_flow(self, s, t, limit):
        if s == t:
            return limit

        total = 0
        n = self.n
        g = self.g

        while total < limit:
            level = [-1] * n
            level[s] = 0
            q = deque([s])

            while q:
                u = q.popleft()
                for e in g[u]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[u] + 1
                        q.append(e.to)

            if level[t] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(g[u]):
                    e = g[u][it[u]]
                    if e.cap > 0 and level[e.to] == level[u] + 1:
                        got = dfs(e.to, min(pushed, e.cap))
                        if got:
                            e.cap -= got
                            g[e.to][e.rev].cap += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(s, limit - total)
                if not pushed:
                    break
                total += pushed

        return total


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    p = 0
    n, m, k = data[p], data[p + 1], data[p + 2]
    p += 3

    commodities = []
    for _ in range(k):
        s, t, d = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        commodities.append((s, t, d))

    edges = []
    adjacency = [[] for _ in range(n)]
    initial_caps = []

    for eid in range(m):
        u, v, cap = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        edges.append((u, v))
        initial_caps.append(cap)
        adjacency[u].append(eid)

    answer = [[0] * m for _ in range(k)]
    active = tuple(
        i for i, (s, t, d) in enumerate(commodities)
        if d > 0 and s != t
    )

    def one_commodity_flow(cid, caps, reverse_order=False):
        s, t, demand = commodities[cid]
        dinic = Dinic(n)
        refs = [None] * m

        order = range(m - 1, -1, -1) if reverse_order else range(m)
        for eid in order:
            cap = caps[eid]
            if cap > 0:
                u, v = edges[eid]
                refs[eid] = dinic.add_edge(u, v, cap)

        value = dinic.max_flow(s, t, demand)
        if value < demand:
            return None

        flow = [0] * m
        for eid, ref in enumerate(refs):
            if ref is not None:
                flow[eid] = caps[eid] - ref.cap
        return flow

    failed = set()

    def solve(remaining, caps):
        if not remaining:
            return True

        key = (remaining, tuple(caps))
        if key in failed:
            return False

        feasible_flows = {}
        selected = -1
        best_slack = None

        for cid in remaining:
            flow = one_commodity_flow(cid, caps)
            if flow is None:
                failed.add(key)
                return False

            feasible_flows[cid] = flow
            used_capacity = sum(flow)
            demand = commodities[cid][2]
            slack_score = used_capacity - demand

            if best_slack is None or slack_score < best_slack:
                best_slack = slack_score
                selected = cid

        rest = tuple(x for x in remaining if x != selected)

        candidates = [feasible_flows[selected]]
        reverse_flow = one_commodity_flow(selected, caps, True)
        if reverse_flow is not None and reverse_flow != candidates[0]:
            candidates.append(reverse_flow)

        for flow in candidates:
            new_caps = caps[:]
            valid = True
            for eid, x in enumerate(flow):
                if x:
                    if x > new_caps[eid]:
                        valid = False
                        break
                    new_caps[eid] -= x
            if valid:
                answer[selected] = flow
                if solve(rest, new_caps):
                    return True

        s, t, demand = commodities[selected]

        paths = []
        visited = [False] * n
        visited[s] = True
        current_path = []

        def enumerate_paths(u):
            if u == t:
                bottleneck = demand
                for eid in current_path:
                    if caps[eid] < bottleneck:
                        bottleneck = caps[eid]
                if bottleneck > 0:
                    paths.append((tuple(current_path), bottleneck))
                return

            for eid in adjacency[u]:
                if caps[eid] <= 0:
                    continue
                v = edges[eid][1]
                if visited[v]:
                    continue
                visited[v] = True
                current_path.append(eid)
                enumerate_paths(v)
                current_path.pop()
                visited[v] = False

        enumerate_paths(s)

        paths.sort(key=lambda item: (-item[1], len(item[0]), item[0]))
        path_count = len(paths)

        suffix_upper = [0] * (path_count + 1)
        for i in range(path_count - 1, -1, -1):
            suffix_upper[i] = suffix_upper[i + 1] + paths[i][1]

        working_caps = caps[:]
        working_flow = [0] * m

        def allocate(idx, left):
            if left == 0:
                answer[selected] = working_flow[:]
                return solve(rest, working_caps)

            if idx == path_count or suffix_upper[idx] < left:
                return False

            path, original_bound = paths[idx]
            qmax = min(left, original_bound)
            for eid in path:
                if working_caps[eid] < qmax:
                    qmax = working_caps[eid]

            for quantity in range(qmax, -1, -1):
                if quantity:
                    for eid in path:
                        working_caps[eid] -= quantity
                        working_flow[eid] += quantity

                if allocate(idx + 1, left - quantity):
                    return True

                if quantity:
                    for eid in path:
                        working_caps[eid] += quantity
                        working_flow[eid] -= quantity

            return False

        if allocate(0, demand):
            return True

        failed.add(key)
        if len(failed) > 100000:
            failed.clear()
            failed.add(key)
        return False

    possible = solve(active, initial_caps[:])

    if not possible:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
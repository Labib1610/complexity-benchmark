import sys
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

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = [s]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            nl = level[u] + 1
            for v, _, cap in self.g[u]:
                if cap and level[v] < 0:
                    level[v] = nl
                    if v == t:
                        return True
                    q.append(v)
        return level[t] >= 0

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        g = self.g
        level = self.level
        it = self.it
        while it[u] < len(g[u]):
            e = g[u][it[u]]
            v, rev, cap = e
            if cap and level[v] == level[u] + 1:
                got = self.dfs(v, t, min(pushed, cap))
                if got:
                    e[2] -= got
                    g[v][rev][2] += got
                    return got
            it[u] += 1
        return 0

    def max_flow(self, s, t, limit):
        if s == t:
            return limit
        total = 0
        inf = 10**30
        while total < limit and self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = 0
            while total < limit:
                got = self.dfs(s, t, min(inf, limit - total))
                if not got:
                    break
                total += got
        return total


def edge_maxflow(n, edges, capacities, s, t, limit, need_flows=True):
    if limit <= 0 or s == t:
        return limit, [0] * len(edges) if need_flows else None

    din = Dinic(n)
    refs = []
    for j, (u, v) in enumerate(edges):
        c = capacities[j]
        idx = din.add_edge(u, v, c)
        if need_flows:
            refs.append((u, idx, c))

    value = din.max_flow(s, t, limit)
    if not need_flows:
        return value, None

    flows = [0] * len(edges)
    for j, (u, idx, initial) in enumerate(refs):
        flows[j] = initial - din.g[u][idx][2]
    return value, flows


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    contracts = []
    for idx in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        contracts.append((s, t, d, idx))

    edges = []
    original_caps = []
    outgoing = [[] for _ in range(n)]
    for j in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v))
        original_caps.append(c)
        outgoing[u].append(j)

    groups_map = {}
    for s, t, d, idx in contracts:
        key = (s, t)
        if key not in groups_map:
            groups_map[key] = [0, []]
        groups_map[key][0] += d
        groups_map[key][1].append((idx, d))

    groups = []
    for (s, t), (demand, members) in groups_map.items():
        if demand == 0 or s == t:
            slack = 10**30
        else:
            value, _ = edge_maxflow(
                n, edges, original_caps, s, t, demand, False
            )
            if value < demand:
                print("NO")
                return
            full_value, _ = edge_maxflow(
                n, edges, original_caps, s, t, sum(original_caps), False
            )
            slack = full_value - demand
        groups.append([s, t, demand, members, slack])

    groups.sort(key=lambda x: (x[4], -x[2]))
    gcount = len(groups)
    residual = original_caps[:]
    group_flows = [[0] * m for _ in range(gcount)]
    failed_states = set()

    def aggregate_possible(start):
        total = 0
        active = []
        for q in range(start, gcount):
            s, t, d = groups[q][0], groups[q][1], groups[q][2]
            if d > 0 and s != t:
                active.append((s, t, d))
                total += d
        if total == 0:
            return True

        ss = n
        tt = n + 1
        din = Dinic(n + 2)
        for j, (u, v) in enumerate(edges):
            if residual[j]:
                din.add_edge(u, v, residual[j])
        for s, t, d in active:
            din.add_edge(ss, s, d)
            din.add_edge(t, tt, d)
        return din.max_flow(ss, tt, total) == total

    def path_generator(s, t, minimum_key):
        used = [False] * n
        used[s] = True
        path = []

        def dfs(u):
            if u == t:
                key = tuple(path)
                if key > minimum_key:
                    yield key
                return
            for eidx in outgoing[u]:
                if residual[eidx] <= 0:
                    continue
                v = edges[eidx][1]
                if used[v]:
                    continue
                used[v] = True
                path.append(eidx)
                yield from dfs(v)
                path.pop()
                used[v] = False

        yield from dfs(s)

    def solve_group(idx):
        while idx < gcount and (groups[idx][2] == 0 or groups[idx][0] == groups[idx][1]):
            idx += 1
        if idx == gcount:
            return True

        state = (idx, tuple(residual))
        if state in failed_states:
            return False

        if not aggregate_possible(idx):
            if len(failed_states) >= 20000:
                failed_states.clear()
            failed_states.add(state)
            return False

        s, t, demand = groups[idx][0], groups[idx][1], groups[idx][2]

        if idx == gcount - 1:
            value, flow = edge_maxflow(n, edges, residual, s, t, demand, True)
            if value < demand:
                return False
            group_flows[idx] = flow
            return True

        if route_partial(idx, demand, ()):
            return True

        if len(failed_states) >= 20000:
            failed_states.clear()
        failed_states.add(state)
        return False

    def route_partial(idx, remaining, minimum_key):
        if remaining == 0:
            return solve_group(idx + 1)

        s, t = groups[idx][0], groups[idx][1]

        value, completion = edge_maxflow(
            n, edges, residual, s, t, remaining, True
        )
        if value < remaining:
            return False

        changed = []
        for eidx, amount in enumerate(completion):
            if amount:
                residual[eidx] -= amount
                group_flows[idx][eidx] += amount
                changed.append((eidx, amount))

        if solve_group(idx + 1):
            return True

        for eidx, amount in changed:
            residual[eidx] += amount
            group_flows[idx][eidx] -= amount

        for path in path_generator(s, t, minimum_key):
            bottleneck = remaining
            for eidx in path:
                if residual[eidx] < bottleneck:
                    bottleneck = residual[eidx]
            for amount in range(bottleneck, 0, -1):
                for eidx in path:
                    residual[eidx] -= amount
                    group_flows[idx][eidx] += amount

                if route_partial(idx, remaining - amount, path):
                    return True

                for eidx in path:
                    residual[eidx] += amount
                    group_flows[idx][eidx] -= amount

        return False

    if not solve_group(0):
        print("NO")
        return

    answer = [[0] * m for _ in range(k)]

    for gi, group in enumerate(groups):
        s, t, demand, members = group[0], group[1], group[2], group[3]
        if demand == 0 or s == t:
            continue

        remaining_flow = group_flows[gi][:]
        member_pos = 0
        member_left = members[0][1] if members else 0

        while member_pos < len(members) and member_left == 0:
            member_pos += 1
            if member_pos < len(members):
                member_left = members[member_pos][1]

        delivered = 0
        while delivered < demand:
            parent_edge = [-1] * n
            parent_edge[s] = -2
            q = [s]
            head = 0

            while head < len(q) and parent_edge[t] == -1:
                u = q[head]
                head += 1
                for eidx in outgoing[u]:
                    if remaining_flow[eidx] <= 0:
                        continue
                    v = edges[eidx][1]
                    if parent_edge[v] == -1:
                        parent_edge[v] = eidx
                        q.append(v)
                        if v == t:
                            break

            if parent_edge[t] == -1:
                print("NO")
                return

            path = []
            v = t
            amount = 10**30
            while v != s:
                eidx = parent_edge[v]
                path.append(eidx)
                if remaining_flow[eidx] < amount:
                    amount = remaining_flow[eidx]
                v = edges[eidx][0]
            path.reverse()

            for eidx in path:
                remaining_flow[eidx] -= amount

            left = amount
            while left:
                while member_pos < len(members) and member_left == 0:
                    member_pos += 1
                    if member_pos < len(members):
                        member_left = members[member_pos][1]

                if member_pos >= len(members):
                    print("NO")
                    return

                take = min(left, member_left)
                contract_idx = members[member_pos][0]
                row = answer[contract_idx]
                for eidx in path:
                    row[eidx] += take

                left -= take
                member_left -= take
                delivered += take

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
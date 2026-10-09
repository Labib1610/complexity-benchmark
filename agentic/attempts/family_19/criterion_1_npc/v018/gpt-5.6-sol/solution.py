import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


class Dinic:
    def __init__(self, n, edges, capacities):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to = []
        self.cap = []
        self.initial = []
        self.forward_arc = [-1] * len(edges)

        for eid, ((u, v), c) in enumerate(zip(edges, capacities)):
            idx = len(self.to)
            self.forward_arc[eid] = idx

            self.to.append(v)
            self.cap.append(c)
            self.initial.append(c)
            self.adj[u].append(idx)

            self.to.append(u)
            self.cap.append(0)
            self.initial.append(0)
            self.adj[v].append(idx ^ 1)

    def max_flow(self, source, sink, limit):
        if source == sink:
            return limit
        if limit <= 0:
            return 0

        n = self.n
        total = 0
        adj = self.adj
        to = self.to
        cap = self.cap

        while total < limit:
            level = [-1] * n
            level[source] = 0
            q = deque([source])

            while q:
                u = q.popleft()
                nl = level[u] + 1
                for a in adj[u]:
                    if cap[a] > 0 and level[to[a]] < 0:
                        level[to[a]] = nl
                        q.append(to[a])

            if level[sink] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == sink:
                    return pushed
                au = adj[u]
                while it[u] < len(au):
                    a = au[it[u]]
                    v = to[a]
                    if cap[a] > 0 and level[v] == level[u] + 1:
                        got = dfs(v, min(pushed, cap[a]))
                        if got:
                            cap[a] -= got
                            cap[a ^ 1] += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(source, limit - total)
                if not pushed:
                    break
                total += pushed

        return total

    def edge_flows(self):
        result = [0] * len(self.forward_arc)
        for eid, a in enumerate(self.forward_arc):
            result[eid] = self.initial[a] - self.cap[a]
        return result


def get_flow(n, edges, capacities, source, sink, demand, need_edges=False):
    if demand == 0:
        return 0, ([0] * len(edges) if need_edges else None)
    dinic = Dinic(n, edges, capacities)
    value = dinic.max_flow(source, sink, demand)
    if need_edges:
        return value, dinic.edge_flows()
    return value, None


def print_answer(answer):
    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    commodities = []
    impossible = False
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        if s == t and d > 0:
            impossible = True
        commodities.append((s, t, d))

    edges = []
    original_cap = []
    outgoing = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    for eid in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v))
        original_cap.append(c)
        if c > 0 and u != v:
            outgoing[u].append(eid)
            reverse_graph[v].append(u)

    if impossible:
        print("NO")
        return

    if k == 0:
        print("YES")
        return

    if all(d == 0 for _, _, d in commodities):
        print_answer([[0] * m for _ in range(k)])
        return

    active = [i for i, (_, _, d) in enumerate(commodities) if d > 0]

    # A single source-destination pair can be solved as one ordinary flow,
    # then decomposed and assigned to the individual commodities.
    if active:
        s0, t0, _ = commodities[active[0]]
        same_pair = all(
            commodities[i][0] == s0 and commodities[i][1] == t0
            for i in active
        )
    else:
        same_pair = True

    if same_pair:
        total_demand = sum(commodities[i][2] for i in active)
        value, aggregate = get_flow(
            n, edges, original_cap, s0, t0, total_demand, True
        )
        if value < total_demand:
            print("NO")
            return

        answer = [[0] * m for _ in range(k)]
        positive = aggregate[:]
        current_pos = 0
        current_id = active[0] if active else -1
        current_need = commodities[current_id][2] if active else 0

        while total_demand > 0:
            parent_edge = [-1] * n
            parent_edge[s0] = -2
            q = deque([s0])

            while q and parent_edge[t0] == -1:
                u = q.popleft()
                for eid in outgoing[u]:
                    if positive[eid] <= 0:
                        continue
                    v = edges[eid][1]
                    if parent_edge[v] == -1:
                        parent_edge[v] = eid
                        q.append(v)
                        if v == t0:
                            break

            if parent_edge[t0] == -1:
                print("NO")
                return

            path = []
            v = t0
            amount = 10**30
            while v != s0:
                eid = parent_edge[v]
                path.append(eid)
                amount = min(amount, positive[eid])
                v = edges[eid][0]

            while amount > 0:
                take = min(amount, current_need)
                for eid in path:
                    answer[current_id][eid] += take
                    positive[eid] -= take

                amount -= take
                current_need -= take
                total_demand -= take

                if current_need == 0 and total_demand > 0:
                    current_pos += 1
                    current_id = active[current_pos]
                    current_need = commodities[current_id][2]

        print_answer(answer)
        return

    # First try several sequential max-flow orders. This quickly handles
    # most feasible instances.
    base_orders = [
        active[:],
        sorted(active, key=lambda x: -commodities[x][2]),
        sorted(active, key=lambda x: commodities[x][2]),
    ]

    seed = 712367821
    for _ in range(min(12, max(1, len(active) * 2))):
        order = active[:]
        for p in range(len(order) - 1, 0, -1):
            seed = (seed * 1103515245 + 12345) & 0x7fffffff
            q = seed % (p + 1)
            order[p], order[q] = order[q], order[p]
        base_orders.append(order)

    seen_orders = set()
    for order in base_orders:
        key = tuple(order)
        if key in seen_orders:
            continue
        seen_orders.add(key)

        residual = original_cap[:]
        answer = [[0] * m for _ in range(k)]
        ok = True

        for cid in order:
            s, t, d = commodities[cid]
            value, flow = get_flow(n, edges, residual, s, t, d, True)
            if value < d:
                ok = False
                break
            answer[cid] = flow
            for eid, x in enumerate(flow):
                residual[eid] -= x

        if ok:
            print_answer(answer)
            return

    # Enumerate all simple paths for exact backtracking.
    paths_by_commodity = {}

    for cid in active:
        s, t, d = commodities[cid]

        reachable = [False] * n
        reachable[t] = True
        q = deque([t])
        while q:
            v = q.popleft()
            for u in reverse_graph[v]:
                if not reachable[u]:
                    reachable[u] = True
                    q.append(u)

        if not reachable[s]:
            print("NO")
            return

        paths = []
        visited = [False] * n
        visited[s] = True
        current = []

        def enumerate_paths(u):
            if u == t:
                paths.append(tuple(current))
                return
            for eid in outgoing[u]:
                v = edges[eid][1]
                if not visited[v] and reachable[v]:
                    visited[v] = True
                    current.append(eid)
                    enumerate_paths(v)
                    current.pop()
                    visited[v] = False

        enumerate_paths(s)

        if not paths:
            print("NO")
            return

        paths.sort(
            key=lambda p: (
                len(p),
                -min(original_cap[e] for e in p),
                p
            )
        )
        paths_by_commodity[cid] = paths

    order = sorted(
        active,
        key=lambda cid: (
            len(paths_by_commodity[cid]),
            -commodities[cid][2]
        )
    )

    residual = original_cap[:]
    answer = [[0] * m for _ in range(k)]

    def individually_feasible(start_index):
        for pos in range(start_index, len(order)):
            cid = order[pos]
            s, t, d = commodities[cid]
            value, _ = get_flow(n, edges, residual, s, t, d, False)
            if value < d:
                return False
        return True

    def solve_commodity(pos):
        if pos == len(order):
            return True

        if not individually_feasible(pos):
            return False

        cid = order[pos]
        s, t, demand = commodities[cid]
        paths = paths_by_commodity[cid]

        def allocate(start_path, remaining):
            if remaining == 0:
                return solve_commodity(pos + 1)

            for pidx in range(start_path, len(paths)):
                path = paths[pidx]
                bottleneck = remaining
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
                        answer[cid][eid] += amount

                    left = remaining - amount
                    possible = True
                    if left > 0:
                        value, _ = get_flow(
                            n, edges, residual, s, t, left, False
                        )
                        possible = value >= left

                    if possible and allocate(pidx + 1, left):
                        return True

                    for eid in path:
                        residual[eid] += amount
                        answer[cid][eid] -= amount

            return False

        return allocate(0, demand)

    if solve_commodity(0):
        print_answer(answer)
    else:
        print("NO")


if __name__ == "__main__":
    main()
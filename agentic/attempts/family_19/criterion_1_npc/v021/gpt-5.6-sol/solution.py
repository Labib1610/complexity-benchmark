import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


class Dinic:
    __slots__ = ("n", "g", "level", "it")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        forward = [v, cap, None]
        backward = [u, 0, forward]
        forward[2] = backward
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
                nl = level[u] + 1
                for e in g[u]:
                    if e[1] > 0 and level[e[0]] < 0:
                        level[e[0]] = nl
                        q.append(e[0])

            if level[t] < 0:
                break

            self.level = level
            self.it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                i = self.it[u]
                while i < len(g[u]):
                    self.it[u] = i
                    e = g[u][i]
                    if e[1] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[1]))
                        if got:
                            e[1] -= got
                            e[2][1] += got
                            return got
                    i += 1
                    self.it[u] = i
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

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    commodities = []
    for idx in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        commodities.append((s, t, d, idx))

    edges = []
    adjacency = [[] for _ in range(n)]
    capacities = [0] * m

    for eid in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges.append((u, v))
        capacities[eid] = cap
        if cap > 0:
            adjacency[u].append(eid)

    for a in adjacency:
        a.sort()

    answer = [[0] * m for _ in range(k)]
    active = [c for c in commodities if c[2] > 0 and c[0] != c[1]]

    if not active:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
        return

    def build_and_flow(caps, s, t, limit, retain=False):
        dinic = Dinic(n)
        refs = [None] * m if retain else None
        for eid, (u, v) in enumerate(edges):
            cap = caps[eid]
            ref = dinic.add_edge(u, v, cap)
            if retain:
                refs[eid] = ref
        value = dinic.max_flow(s, t, limit)
        if retain:
            flows = [caps[eid] - refs[eid][1] for eid in range(m)]
            return value, flows
        return value

    # If every commodity has the same terminals, the problem is one max-flow.
    first_s, first_t = active[0][0], active[0][1]
    if all(s == first_s and t == first_t for s, t, _, _ in active):
        required = sum(d for _, _, d, _ in active)
        value, positive_flow = build_and_flow(
            capacities, first_s, first_t, required, True
        )

        if value < required:
            sys.stdout.write("NO")
            return

        pos_adj = [[] for _ in range(n)]
        for eid, (u, _) in enumerate(edges):
            if positive_flow[eid] > 0:
                pos_adj[u].append(eid)

        commodity_pos = 0
        commodity_remaining = active[0][2]

        while commodity_pos < len(active):
            visited = [False] * n
            path = []

            def find_path(u):
                if u == first_t:
                    return True
                visited[u] = True
                for eid in pos_adj[u]:
                    if positive_flow[eid] <= 0:
                        continue
                    v = edges[eid][1]
                    if not visited[v]:
                        path.append(eid)
                        if find_path(v):
                            return True
                        path.pop()
                return False

            if not find_path(first_s):
                sys.stdout.write("NO")
                return

            bottleneck = min(positive_flow[eid] for eid in path)

            while bottleneck > 0 and commodity_pos < len(active):
                take = min(bottleneck, commodity_remaining)
                original_idx = active[commodity_pos][3]
                for eid in path:
                    answer[original_idx][eid] += take
                    positive_flow[eid] -= take

                bottleneck -= take
                commodity_remaining -= take

                if commodity_remaining == 0:
                    commodity_pos += 1
                    if commodity_pos < len(active):
                        commodity_remaining = active[commodity_pos][2]

        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
        return

    # Exact branch-and-bound for the general integral multicommodity case.
    initial_info = []
    for c in active:
        s, t, d, idx = c
        full = build_and_flow(capacities, s, t, sum(capacities))
        if full < d:
            sys.stdout.write("NO")
            return
        initial_info.append((full - d, full, -d, s, t, d, idx))

    initial_info.sort()
    ordered = [(s, t, d, idx) for _, _, _, s, t, d, idx in initial_info]

    caps = capacities[:]
    failed = set()
    flow_cache = {}

    def can_send(s, t, demand):
        if demand <= 0:
            return True
        state_caps = tuple(caps)
        key = (s, t, demand, state_caps)
        cached = flow_cache.get(key)
        if cached is not None:
            return cached

        result = build_and_flow(caps, s, t, demand) >= demand
        if len(flow_cache) >= 100000:
            flow_cache.clear()
        flow_cache[key] = result
        return result

    def available_paths(s, t, lower_bound):
        visited = [False] * n
        path = []
        visited[s] = True

        def dfs(u):
            if u == t:
                candidate = tuple(path)
                if lower_bound is None or candidate > lower_bound:
                    yield candidate
                return

            for eid in adjacency[u]:
                if caps[eid] <= 0:
                    continue
                v = edges[eid][1]
                if visited[v]:
                    continue
                visited[v] = True
                path.append(eid)
                yield from dfs(v)
                path.pop()
                visited[v] = False

        yield from dfs(s)

    def search(stage, remaining, previous_path):
        if stage == len(ordered):
            return True

        s, t, total_demand, original_idx = ordered[stage]

        if remaining == 0:
            return search(stage + 1, ordered[stage + 1][2], None) \
                if stage + 1 < len(ordered) else True

        state = (stage, remaining, previous_path, tuple(caps))
        if state in failed:
            return False

        if not can_send(s, t, remaining):
            failed.add(state)
            return False

        # Every unprocessed commodity must still be feasible on its own.
        for future in range(stage + 1, len(ordered)):
            fs, ft, fd, _ = ordered[future]
            if not can_send(fs, ft, fd):
                failed.add(state)
                return False

        for path in available_paths(s, t, previous_path):
            maximum = remaining
            for eid in path:
                if caps[eid] < maximum:
                    maximum = caps[eid]

            for amount in range(maximum, 0, -1):
                for eid in path:
                    caps[eid] -= amount
                    answer[original_idx][eid] += amount

                new_remaining = remaining - amount
                if new_remaining == 0:
                    if stage + 1 == len(ordered):
                        return True
                    if search(stage + 1, ordered[stage + 1][2], None):
                        return True
                elif search(stage, new_remaining, path):
                    return True

                for eid in path:
                    caps[eid] += amount
                    answer[original_idx][eid] -= amount

        failed.add(state)
        return False

    possible = search(0, ordered[0][2], None)

    if not possible:
        sys.stdout.write("NO")
        return

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
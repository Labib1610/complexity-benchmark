import sys
import time
import random
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

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
out_edges = [[] for _ in range(n)]
for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v, c))
    out_edges[u].append(eid)


class Dinic:
    __slots__ = ("n", "g", "level", "pos")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n
        self.pos = [0] * n

    def add_edge(self, u, v, cap):
        a = [v, cap, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)
        return a

    def max_flow(self, s, t, limit):
        if s == t:
            return limit

        flow = 0
        g = self.g
        n = self.n

        while flow < limit:
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
            self.pos = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while self.pos[u] < len(g[u]):
                    e = g[u][self.pos[u]]
                    if e[1] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[1]))
                        if got:
                            e[1] -= got
                            e[2][1] += got
                            return got
                    self.pos[u] += 1
                return 0

            while flow < limit:
                got = dfs(s, limit - flow)
                if not got:
                    break
                flow += got

        return flow


def find_flow(residual, cid, route_order=None, need_override=None):
    s, t, demand = commodities[cid]
    need = demand if need_override is None else need_override
    if need == 0 or s == t:
        return [0] * m

    din = Dinic(n)
    refs = [None] * m
    order = range(m) if route_order is None else route_order
    for eid in order:
        if residual[eid] > 0:
            u, v, _ = edges[eid]
            refs[eid] = din.add_edge(u, v, residual[eid])

    got = din.max_flow(s, t, need)
    if got < need:
        return None

    result = [0] * m
    for eid, ref in enumerate(refs):
        if ref is not None:
            result[eid] = residual[eid] - ref[1]
    return result


def flow_value(residual, cid, limit):
    s, t, d = commodities[cid]
    if limit <= 0 or s == t:
        return limit

    din = Dinic(n)
    for eid, (u, v, _) in enumerate(edges):
        if residual[eid] > 0:
            din.add_edge(u, v, residual[eid])
    return din.max_flow(s, t, limit)


def try_sequential(order, randomized_routes=False):
    residual = [c for _, _, c in edges]
    answer = [[0] * m for _ in range(k)]

    for cid in order:
        if commodities[cid][2] == 0 or commodities[cid][0] == commodities[cid][1]:
            continue

        route_order = None
        if randomized_routes:
            route_order = list(range(m))
            random.shuffle(route_order)

        f = find_flow(residual, cid, route_order)
        if f is None:
            return None

        answer[cid] = f
        for eid, x in enumerate(f):
            residual[eid] -= x

    return answer


active = [i for i, (s, t, d) in enumerate(commodities) if d > 0 and s != t]

initial_residual = [c for _, _, c in edges]
initial_slacks = {}
globally_impossible = False
for cid in active:
    d = commodities[cid][2]
    val = flow_value(initial_residual, cid, d)
    if val < d:
        globally_impossible = True
        break
    initial_slacks[cid] = val - d

if globally_impossible:
    print("NO")
    sys.exit()

orders = []
orders.append(active[:])
orders.append(list(reversed(active)))
orders.append(sorted(active, key=lambda x: commodities[x][2], reverse=True))
orders.append(sorted(active, key=lambda x: (initial_slacks.get(x, 0), -commodities[x][2])))

seen_orders = set()
start_time = time.monotonic()

for order in orders:
    key = tuple(order)
    if key in seen_orders:
        continue
    seen_orders.add(key)
    ans = try_sequential(order)
    if ans is not None:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in ans)
        sys.stdout.write("\n".join(out))
        sys.exit()

random.seed(712367821)
attempts = min(32, max(4, 4 * len(active)))
for _ in range(attempts):
    if time.monotonic() - start_time > 1.2:
        break
    order = active[:]
    random.shuffle(order)
    key = tuple(order)
    if key in seen_orders:
        continue
    seen_orders.add(key)
    ans = try_sequential(order, randomized_routes=True)
    if ans is not None:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in ans)
        sys.stdout.write("\n".join(out))
        sys.exit()

deadline = start_time + 4.75
residual = [c for _, _, c in edges]
answer = [[0] * m for _ in range(k)]
failed_states = set()
timed_out = False


def expired():
    global timed_out
    if time.monotonic() >= deadline:
        timed_out = True
        return True
    return False


def solve_remaining(remaining):
    if expired():
        return False
    if not remaining:
        return True

    state = (remaining, tuple(residual))
    if state in failed_states:
        return False

    best_cid = -1
    best_key = None
    best_flow = None

    for cid in remaining:
        d = commodities[cid][2]
        f = find_flow(residual, cid)
        if f is None:
            if not timed_out:
                failed_states.add(state)
            return False

        used_edges = sum(1 for x in f if x)
        bottleneck_score = sum(
            1 for eid, x in enumerate(f)
            if x and x == residual[eid]
        )
        key = (bottleneck_score, used_edges, -d)
        if best_key is None or key > best_key:
            best_key = key
            best_cid = cid
            best_flow = f

    next_remaining = tuple(x for x in remaining if x != best_cid)

    for eid, x in enumerate(best_flow):
        if x:
            residual[eid] -= x
            answer[best_cid][eid] += x

    if solve_remaining(next_remaining):
        return True

    for eid, x in enumerate(best_flow):
        if x:
            residual[eid] += x
            answer[best_cid][eid] -= x

    s, t, demand = commodities[best_cid]
    visited = [False] * n
    visited[s] = True
    path = []

    def allocate_paths(rem, lower):
        if expired():
            return False
        if rem == 0:
            return solve_remaining(next_remaining)

        if flow_value(residual, best_cid, rem) < rem:
            return False

        found_any = False

        def dfs_paths(u):
            nonlocal found_any
            if expired():
                return False

            if u == t:
                ptuple = tuple(path)
                if lower is not None and ptuple <= lower:
                    return False

                found_any = True
                maxq = rem
                for eid in path:
                    if residual[eid] < maxq:
                        maxq = residual[eid]

                for q in range(maxq, 0, -1):
                    for eid in path:
                        residual[eid] -= q
                        answer[best_cid][eid] += q

                    ok = allocate_paths(rem - q, ptuple)
                    if ok:
                        return True

                    for eid in path:
                        residual[eid] += q
                        answer[best_cid][eid] -= q

                    if expired():
                        return False
                return False

            for eid in out_edges[u]:
                if residual[eid] <= 0:
                    continue
                v = edges[eid][1]
                if visited[v]:
                    continue
                visited[v] = True
                path.append(eid)
                if dfs_paths(v):
                    return True
                path.pop()
                visited[v] = False
                if expired():
                    return False
            return False

        if dfs_paths(s):
            return True
        return False

    if allocate_paths(demand, None):
        return True

    if not timed_out:
        failed_states.add(state)
    return False


remaining = tuple(active)
if solve_remaining(remaining):
    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))
else:
    print("NO")
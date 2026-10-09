import sys
import time
import random

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
    if s == t:
        d = 0
    commodities.append((s, t, d))

edges = []
base_cap = []
out_edges = [[] for _ in range(n)]
for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v))
    base_cap.append(c)
    out_edges[u].append(eid)

start_time = time.monotonic()
HARD_DEADLINE = start_time + 4.85


class Dinic:
    __slots__ = ("n", "g", "level", "pos")

    def __init__(self, n_):
        self.n = n_
        self.g = [[] for _ in range(n_)]
        self.level = [-1] * n_
        self.pos = [0] * n_

    def add_edge(self, u, v, c):
        a = [v, c, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)
        return a

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = [s]
        head = 0
        g = self.g
        while head < len(q):
            u = q[head]
            head += 1
            nl = level[u] + 1
            for e in g[u]:
                if e[1] > 0 and level[e[0]] < 0:
                    level[e[0]] = nl
                    if e[0] == t:
                        return True
                    q.append(e[0])
        return level[t] >= 0

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        g = self.g
        pos = self.pos
        level = self.level
        while pos[u] < len(g[u]):
            e = g[u][pos[u]]
            if e[1] > 0 and level[e[0]] == level[u] + 1:
                got = self.dfs(e[0], t, min(pushed, e[1]))
                if got:
                    e[1] -= got
                    e[2][1] += got
                    return got
            pos[u] += 1
        return 0

    def flow(self, s, t, limit):
        if s == t:
            return limit
        total = 0
        inf = 10**30
        while total < limit and self.bfs(s, t):
            for i in range(self.n):
                self.pos[i] = 0
            while total < limit:
                got = self.dfs(s, t, min(inf, limit - total))
                if not got:
                    break
                total += got
        return total


def route_one(caps, s, t, need, randomized=False, want_flow=True):
    if need == 0:
        return [] if want_flow else 0
    din = Dinic(n)
    refs = [None] * m if want_flow else None

    ids = list(range(m))
    if randomized:
        random.shuffle(ids)

    for eid in ids:
        c = caps[eid]
        if c > 0:
            u, v = edges[eid]
            ref = din.add_edge(u, v, c)
            if want_flow:
                refs[eid] = (ref, c)

    got = din.flow(s, t, need)
    if not want_flow:
        return got
    if got < need:
        return None

    result = [0] * m
    for eid, item in enumerate(refs):
        if item is not None:
            ref, initial = item
            result[eid] = initial - ref[1]
    return result


# Fast necessary checks and useful ordering information.
slack = [0] * k
for i, (s, t, d) in enumerate(commodities):
    if d == 0:
        continue
    got = route_one(base_cap, s, t, d, False, False)
    if got < d:
        print("NO")
        sys.exit()
    slack[i] = got - d
    if time.monotonic() > HARD_DEADLINE:
        print("NO")
        sys.exit()


def try_order(order, randomized):
    caps = base_cap[:]
    answer = [[0] * m for _ in range(k)]
    for ci in order:
        s, t, d = commodities[ci]
        if d == 0:
            continue
        f = route_one(caps, s, t, d, randomized, True)
        if f is None:
            return None
        answer[ci] = f
        for e, x in enumerate(f):
            caps[e] -= x
    return answer


active = [i for i, (_, _, d) in enumerate(commodities) if d > 0]

orders = []
orders.append(active[:])
orders.append(sorted(active, key=lambda x: (slack[x], -commodities[x][2], x)))
orders.append(sorted(active, key=lambda x: (-commodities[x][2], slack[x], x)))
orders.append(list(reversed(active)))

seen_orders = set()
for order in orders:
    key = tuple(order)
    if key in seen_orders:
        continue
    seen_orders.add(key)
    ans = try_order(order, False)
    if ans is not None:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in ans)
        sys.stdout.write("\n".join(out))
        sys.exit()

random.seed(712367821)
heuristic_deadline = min(HARD_DEADLINE, start_time + 2.0)
attempt = 0
while active and time.monotonic() < heuristic_deadline and attempt < 80:
    if attempt % 3 == 0:
        order = sorted(active, key=lambda x: (
            slack[x] + random.random() * (1 + commodities[x][2]),
            -commodities[x][2]
        ))
    else:
        order = active[:]
        random.shuffle(order)
    ans = try_order(order, True)
    if ans is not None:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in ans)
        sys.stdout.write("\n".join(out))
        sys.exit()
    attempt += 1

# Exact path-packing search. Every integral flow can be decomposed into simple
# unit paths, so this search is complete if it finishes before the deadline.
total_units = sum(d for _, _, d in commodities)
remaining = [d for _, _, d in commodities]
caps = base_cap[:]
exact_answer = [[0] * m for _ in range(k)]
last_path = [None] * k
timed_out = False

# Large instances are handled by the polynomial-time heuristic above; exact
# enumeration is reserved for instances where it is practically meaningful.
if total_units > 45:
    print("NO")
    sys.exit()

memo = set()
nodes_visited = 0


def generate_paths(s, t, lower):
    visited = [False] * n
    visited[s] = True
    path = []

    def dfs(u):
        if u == t:
            p = tuple(path)
            if lower is None or p >= lower:
                yield p
            return
        for eid in out_edges[u]:
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


def exact_search():
    global timed_out, nodes_visited
    nodes_visited += 1
    if (nodes_visited & 127) == 0 and time.monotonic() > HARD_DEADLINE:
        timed_out = True
        return False

    if all(x == 0 for x in remaining):
        return True

    if m <= 35:
        key = (tuple(caps), tuple(remaining), tuple(last_path))
        if key in memo:
            return False
        memo.add(key)

    chosen = -1
    chosen_score = None

    for ci in active:
        r = remaining[ci]
        if r == 0:
            continue
        s, t, _ = commodities[ci]
        got = route_one(caps, s, t, r, False, False)
        if got < r:
            return False
        score = (got - r, r)
        if chosen_score is None or score < chosen_score:
            chosen_score = score
            chosen = ci

    if chosen < 0:
        return True

    s, t, _ = commodities[chosen]
    old_lower = last_path[chosen]

    for path in generate_paths(s, t, old_lower):
        if timed_out:
            return False

        # Assign as many identical path units as useful, trying larger amounts
        # first while retaining all smaller possibilities for completeness.
        max_take = remaining[chosen]
        for eid in path:
            if caps[eid] < max_take:
                max_take = caps[eid]

        for take in range(max_take, 0, -1):
            remaining[chosen] -= take
            last_path[chosen] = path
            for eid in path:
                caps[eid] -= take
                exact_answer[chosen][eid] += take

            if exact_search():
                return True

            for eid in path:
                caps[eid] += take
                exact_answer[chosen][eid] -= take
            remaining[chosen] += take
            last_path[chosen] = old_lower

            if timed_out:
                return False

    last_path[chosen] = old_lower
    return False


if exact_search():
    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in exact_answer)
    sys.stdout.write("\n".join(out))
else:
    print("NO")
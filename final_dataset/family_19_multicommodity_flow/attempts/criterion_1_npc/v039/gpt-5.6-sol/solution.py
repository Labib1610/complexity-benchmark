import sys
import random
import itertools
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)
k = next(it)

tasks = []
for _ in range(k):
    s = next(it) - 1
    t = next(it) - 1
    d = next(it)
    tasks.append((s, t, d))

edges = []
out_edges = [[] for _ in range(n)]
for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v, c))
    if u != v and c > 0:
        out_edges[u].append(eid)

for adj in out_edges:
    adj.sort()


class Dinic:
    __slots__ = ("n", "g", "level", "ptr")

    def __init__(self, size):
        self.n = size
        self.g = [[] for _ in range(size)]
        self.level = [-1] * size
        self.ptr = [0] * size

    def add_edge(self, u, v, cap):
        a = [v, cap, None]
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
        q = deque([s])
        while q:
            u = q.popleft()
            nl = level[u] + 1
            for e in self.g[u]:
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
        ptr = self.ptr
        while ptr[u] < len(g[u]):
            e = g[u][ptr[u]]
            if e[1] > 0 and self.level[e[0]] == self.level[u] + 1:
                got = self.dfs(e[0], t, min(pushed, e[1]))
                if got:
                    e[1] -= got
                    e[2][1] += got
                    return got
            ptr[u] += 1
        return 0

    def maxflow(self, s, t, limit):
        if s == t:
            return limit
        flow = 0
        inf = 10**30
        while flow < limit and self.bfs(s, t):
            for i in range(self.n):
                self.ptr[i] = 0
            while flow < limit:
                pushed = self.dfs(s, t, min(inf, limit - flow))
                if not pushed:
                    break
                flow += pushed
        return flow


def compute_flow(capacities, s, t, need, randomized=False, want_usage=False):
    if need == 0 or s == t:
        return need, ([0] * m if want_usage else None)

    din = Dinic(n)
    refs = [None] * m

    if randomized:
        ids = [i for i, c in enumerate(capacities)
               if c > 0 and edges[i][0] != edges[i][1]]
        random.shuffle(ids)
    else:
        ids = range(m)

    for eid in ids:
        c = capacities[eid]
        if c <= 0:
            continue
        u, v, _ = edges[eid]
        if u == v:
            continue
        refs[eid] = (din.add_edge(u, v, c), c)

    got = din.maxflow(s, t, need)
    if not want_usage:
        return got, None

    usage = [0] * m
    for eid, ref in enumerate(refs):
        if ref is not None:
            arc, initial = ref
            usage[eid] = initial - arc[1]
    return got, usage


base_caps = [c for _, _, c in edges]

individual_max = [0] * k
for i, (s, t, d) in enumerate(tasks):
    if d == 0 or s == t:
        individual_max[i] = d
        continue
    got, _ = compute_flow(base_caps, s, t, d, False, False)
    if got < d:
        print("NO")
        sys.exit()
    individual_max[i] = got


def try_order(order, randomized=False):
    residual = base_caps[:]
    answer = [[0] * m for _ in range(k)]

    for idx in order:
        s, t, d = tasks[idx]
        if d == 0 or s == t:
            continue
        got, usage = compute_flow(residual, s, t, d, randomized, True)
        if got < d:
            return None
        answer[idx] = usage
        for eid, x in enumerate(usage):
            residual[eid] -= x
    return answer


active = [i for i, (_, _, d) in enumerate(tasks) if d > 0]
orders = []
seen_orders = set()


def add_order(order):
    key = tuple(order)
    if key not in seen_orders:
        seen_orders.add(key)
        orders.append(list(order))


add_order(active)
add_order(reversed(active))
add_order(sorted(active, key=lambda i: (-tasks[i][2], i)))
add_order(sorted(active, key=lambda i: (tasks[i][2], i)))

# Tasks with fewer usable outgoing/incoming links and larger demands first.
indeg = [0] * n
outdeg = [0] * n
for u, v, c in edges:
    if c > 0 and u != v:
        outdeg[u] += 1
        indeg[v] += 1

add_order(sorted(
    active,
    key=lambda i: (
        outdeg[tasks[i][0]] + indeg[tasks[i][1]],
        -tasks[i][2],
        i
    )
))

if len(active) <= 7:
    for p in itertools.permutations(active):
        add_order(p)
        if len(orders) >= 1000:
            break
else:
    rng = random.Random(712367821)
    for _ in range(120):
        p = active[:]
        rng.shuffle(p)
        add_order(p)

for trial, order in enumerate(orders):
    ans = try_order(order, randomized=(trial >= 5))
    if ans is not None:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in ans)
        sys.stdout.write("\n".join(out))
        sys.exit()


# Complete backtracking over simple path decompositions.
order = sorted(
    active,
    key=lambda i: (
        outdeg[tasks[i][0]] + indeg[tasks[i][1]],
        -tasks[i][2],
        i
    )
)

residual = base_caps[:]
answer = [[0] * m for _ in range(k)]
visited = [False] * n
current_path = []


def path_generator(s, t, lower_key):
    visited[s] = True
    current_path.clear()

    def walk(u):
        if u == t:
            key = tuple(current_path)
            if lower_key is None or key > lower_key:
                yield key
            return

        for eid in out_edges[u]:
            if residual[eid] <= 0:
                continue
            v = edges[eid][1]
            if visited[v]:
                continue
            visited[v] = True
            current_path.append(eid)
            yield from walk(v)
            current_path.pop()
            visited[v] = False

    yield from walk(s)
    visited[s] = False


def future_feasible(pos):
    for q in range(pos, len(order)):
        idx = order[q]
        s, t, d = tasks[idx]
        if d == 0 or s == t:
            continue
        got, _ = compute_flow(residual, s, t, d, False, False)
        if got < d:
            return False
    return True


def solve_commodity(pos, remaining, last_key):
    if pos == len(order):
        return True

    idx = order[pos]
    s, t, demand = tasks[idx]

    if remaining == 0:
        if not future_feasible(pos + 1):
            return False
        if pos + 1 == len(order):
            return True
        nxt = order[pos + 1]
        return solve_commodity(pos + 1, tasks[nxt][2], None)

    got, _ = compute_flow(residual, s, t, remaining, False, False)
    if got < remaining:
        return False

    for path in path_generator(s, t, last_key):
        bottleneck = remaining
        for eid in path:
            if residual[eid] < bottleneck:
                bottleneck = residual[eid]

        # Larger multiplicities are usually much more effective.
        for amount in range(bottleneck, 0, -1):
            for eid in path:
                residual[eid] -= amount
                answer[idx][eid] += amount

            if solve_commodity(pos, remaining - amount, path):
                return True

            for eid in path:
                residual[eid] += amount
                answer[idx][eid] -= amount

    return False


if not order:
    result = True
else:
    result = solve_commodity(0, tasks[order[0]][2], None)

if result:
    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))
else:
    print("NO")
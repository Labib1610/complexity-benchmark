import sys
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
for i in range(k):
    s = next(it) - 1
    t = next(it) - 1
    d = next(it)
    commodities.append((s, t, d))

edges = []
adj_edges = [[] for _ in range(n)]
initial_caps = [0] * m

for e in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v))
    initial_caps[e] = c
    if u != v and c > 0:
        adj_edges[u].append(e)

for a in adj_edges:
    a.sort()


class Dinic:
    __slots__ = ("n", "g", "level", "pos")

    def __init__(self, size):
        self.n = size
        self.g = [[] for _ in range(size)]
        self.level = [-1] * size
        self.pos = [0] * size

    def add_edge(self, u, v, cap):
        fi = len(self.g[u])
        ri = len(self.g[v])
        self.g[u].append([v, cap, ri])
        self.g[v].append([u, 0, fi])
        return fi

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            nl = level[u] + 1
            for v, cap, _ in self.g[u]:
                if cap > 0 and level[v] < 0:
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
        while self.pos[u] < len(g[u]):
            i = self.pos[u]
            v, cap, rev = g[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                got = self.dfs(v, t, min(pushed, cap))
                if got:
                    g[u][i][1] -= got
                    g[v][rev][1] += got
                    return got
            self.pos[u] += 1
        return 0

    def flow(self, s, t, limit):
        result = 0
        while result < limit and self.bfs(s, t):
            for i in range(self.n):
                self.pos[i] = 0
            while result < limit:
                pushed = self.dfs(s, t, limit - result)
                if not pushed:
                    break
                result += pushed
        return result


def get_flow(capacities, s, t, need, with_usage=False):
    if need <= 0 or s == t:
        return need, ([0] * m if with_usage else None)

    dinic = Dinic(n)
    refs = [None] * m

    for eid, ((u, v), cap) in enumerate(zip(edges, capacities)):
        if cap > 0 and u != v:
            idx = dinic.add_edge(u, v, cap)
            refs[eid] = (u, idx, cap)

    value = dinic.flow(s, t, need)

    if not with_usage:
        return value, None

    usage = [0] * m
    for eid, ref in enumerate(refs):
        if ref is not None:
            u, idx, original = ref
            usage[eid] = original - dinic.g[u][idx][1]
    return value, usage


def print_answer(answer):
    out = ["YES"]
    for row in answer:
        out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out))


positive = [i for i, (s, t, d) in enumerate(commodities) if d > 0 and s != t]

slack_info = {}
for ci in positive:
    s, t, d = commodities[ci]
    possible, _ = get_flow(initial_caps, s, t, d, False)
    if possible < d:
        print("NO")
        sys.exit()
    total_possible, _ = get_flow(initial_caps, s, t, sum(initial_caps), False)
    slack_info[ci] = total_possible - d


def try_order(order):
    caps = initial_caps[:]
    answer = [[0] * m for _ in range(k)]

    for ci in order:
        s, t, d = commodities[ci]
        value, usage = get_flow(caps, s, t, d, True)
        if value < d:
            return None
        answer[ci] = usage
        for eid, x in enumerate(usage):
            caps[eid] -= x
    return answer


orders = []
base_orders = [
    positive[:],
    list(reversed(positive)),
    sorted(positive, key=lambda x: (slack_info[x], -commodities[x][2], x)),
    sorted(positive, key=lambda x: (-commodities[x][2], slack_info[x], x)),
    sorted(positive, key=lambda x: (commodities[x][2], slack_info[x], x)),
]

seen_orders = set()
for order in base_orders:
    key = tuple(order)
    if key not in seen_orders:
        seen_orders.add(key)
        orders.append(order)

if len(positive) <= 9:
    rng = random.Random(712367)
    for _ in range(40):
        order = positive[:]
        rng.shuffle(order)
        key = tuple(order)
        if key not in seen_orders:
            seen_orders.add(key)
            orders.append(order)

for order in orders:
    answer = try_order(order)
    if answer is not None:
        print_answer(answer)
        sys.exit()

order = sorted(
    positive,
    key=lambda x: (slack_info[x], -commodities[x][2], x)
)

caps = initial_caps[:]
answer = [[0] * m for _ in range(k)]


def generate_paths(s, t, last_path):
    visited = [False] * n
    visited[s] = True
    path = []

    def dfs(u):
        if u == t:
            p = tuple(path)
            if last_path is None or p > last_path:
                yield p
            return

        for eid in adj_edges[u]:
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


def solve_commodity(pos):
    if pos == len(order):
        return True

    ci = order[pos]
    s, t, demand = commodities[ci]

    possible, direct_usage = get_flow(caps, s, t, demand, True)
    if possible < demand:
        return False

    for eid, x in enumerate(direct_usage):
        if x:
            caps[eid] -= x
            answer[ci][eid] += x

    if solve_commodity(pos + 1):
        return True

    for eid, x in enumerate(direct_usage):
        if x:
            caps[eid] += x
            answer[ci][eid] -= x

    def assign_paths(remaining, last_path):
        if remaining == 0:
            return solve_commodity(pos + 1)

        possible_now, _ = get_flow(caps, s, t, remaining, False)
        if possible_now < remaining:
            return False

        for path in generate_paths(s, t, last_path):
            bottleneck = remaining
            for eid in path:
                if caps[eid] < bottleneck:
                    bottleneck = caps[eid]

            for amount in range(bottleneck, 0, -1):
                for eid in path:
                    caps[eid] -= amount
                    answer[ci][eid] += amount

                if assign_paths(remaining - amount, path):
                    return True

                for eid in path:
                    caps[eid] += amount
                    answer[ci][eid] -= amount

        return False

    return assign_paths(demand, None)


if solve_commodity(0):
    print_answer(answer)
else:
    print("NO")
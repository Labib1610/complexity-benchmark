import sys
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
invalid = False
for _ in range(k):
    s = next(it) - 1
    t = next(it) - 1
    d = next(it)
    if s == t and d > 0:
        invalid = True
    commodities.append((s, t, d))

edges = []
out_edges = [[] for _ in range(n)]
rev_edges = [[] for _ in range(n)]

for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v, c))
    if u != v and c > 0:
        out_edges[u].append(eid)
        rev_edges[v].append(eid)

if invalid:
    print("NO")
    sys.exit()


class Dinic:
    __slots__ = ("n", "g", "level", "work")

    def __init__(self, size):
        self.n = size
        self.g = [[] for _ in range(size)]
        self.level = [-1] * size
        self.work = [0] * size

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
        work = self.work
        while work[u] < len(g[u]):
            idx = work[u]
            v, cap, rev = g[u][idx]
            if cap > 0 and level[v] == level[u] + 1:
                got = self.dfs(v, t, min(pushed, cap))
                if got:
                    g[u][idx][1] -= got
                    g[v][rev][1] += got
                    return got
            work[u] += 1
        return 0

    def maxflow(self, s, t, limit):
        if s == t:
            return limit
        total = 0
        while total < limit and self.bfs(s, t):
            for i in range(self.n):
                self.work[i] = 0
            while total < limit:
                pushed = self.dfs(s, t, limit - total)
                if not pushed:
                    break
                total += pushed
        return total


def get_flow(s, t, demand, residual, need_assignment=True):
    if demand == 0:
        return 0, [0] * m if need_assignment else None
    if s == t:
        return demand, [0] * m if need_assignment else None

    dinic = Dinic(n)
    refs = [None] * m if need_assignment else None

    for eid, (u, v, _) in enumerate(edges):
        cap = residual[eid]
        if cap > 0 and u != v:
            idx = dinic.add_edge(u, v, cap)
            if need_assignment:
                refs[eid] = (u, idx, cap)

    value = dinic.maxflow(s, t, demand)

    if not need_assignment:
        return value, None

    assignment = [0] * m
    if value == demand:
        for eid, ref in enumerate(refs):
            if ref is not None:
                u, idx, original_cap = ref
                assignment[eid] = original_cap - dinic.g[u][idx][1]
    return value, assignment


residual = [c for _, _, c in edges]
answer = [[0] * m for _ in range(k)]
unassigned_initial = tuple(i for i, (_, _, d) in enumerate(commodities) if d > 0)


def enumerate_paths(s, t):
    reachable = [False] * n
    q = deque([t])
    reachable[t] = True

    while q:
        v = q.popleft()
        for eid in rev_edges[v]:
            if residual[eid] <= 0:
                continue
            u = edges[eid][0]
            if not reachable[u]:
                reachable[u] = True
                q.append(u)

    if not reachable[s]:
        return []

    paths = []
    visited = [False] * n
    visited[s] = True
    path = []

    def dfs(u):
        if u == t:
            paths.append(tuple(path))
            return
        for eid in out_edges[u]:
            if residual[eid] <= 0:
                continue
            v = edges[eid][1]
            if reachable[v] and not visited[v]:
                visited[v] = True
                path.append(eid)
                dfs(v)
                path.pop()
                visited[v] = False

    dfs(s)
    paths.sort(key=len)
    return paths


def solve(remaining):
    if not remaining:
        return True

    chosen = -1
    chosen_flow = None
    chosen_key = None

    for ci in remaining:
        s, t, d = commodities[ci]
        value, flow = get_flow(s, t, d, residual, True)
        if value < d:
            return False

        used_edges = sum(1 for x in flow if x)
        key = (-d, used_edges)
        if chosen == -1 or key < chosen_key:
            chosen = ci
            chosen_flow = flow
            chosen_key = key

    next_remaining = tuple(x for x in remaining if x != chosen)
    s, t, demand = commodities[chosen]

    # First try a direct maximum-flow assignment.
    for eid, x in enumerate(chosen_flow):
        residual[eid] -= x
    answer[chosen] = chosen_flow

    if solve(next_remaining):
        return True

    for eid, x in enumerate(chosen_flow):
        residual[eid] += x
    answer[chosen] = [0] * m

    # Exhaustively enumerate path-flow decompositions for completeness.
    paths = enumerate_paths(s, t)
    if not paths:
        return False

    current = [0] * m
    plen = len(paths)

    def enumerate_allocations(pos, rem, recheck):
        if rem == 0:
            answer[chosen] = current[:]
            if solve(next_remaining):
                return True
            answer[chosen] = [0] * m
            return False

        if pos == plen:
            return False

        if recheck:
            possible, _ = get_flow(s, t, rem, residual, False)
            if possible < rem:
                return False

        path = paths[pos]
        max_amount = rem
        for eid in path:
            if residual[eid] < max_amount:
                max_amount = residual[eid]

        for amount in range(max_amount, -1, -1):
            if amount:
                for eid in path:
                    residual[eid] -= amount
                    current[eid] += amount

            if enumerate_allocations(pos + 1, rem - amount, amount > 0):
                return True

            if amount:
                for eid in path:
                    residual[eid] += amount
                    current[eid] -= amount

        return False

    return enumerate_allocations(0, demand, False)


if solve(unassigned_initial):
    print("YES")
    out = []
    for row in answer:
        out.append(" ".join(map(str, row)))
    print("\n".join(out))
else:
    print("NO")
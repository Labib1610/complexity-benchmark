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
for idx in range(k):
    s = next(it) - 1
    t = next(it) - 1
    d = next(it)
    commodities.append((s, t, d, idx))

edges = []
out_edges = [[] for _ in range(n)]
capacities = [0] * m

for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    c = next(it)
    edges.append((u, v))
    capacities[eid] = c
    if u != v:
        out_edges[u].append(eid)

for lst in out_edges:
    lst.sort()

for s, t, d, _ in commodities:
    if d < 0 or (d > 0 and s == t):
        print("NO")
        sys.exit()


def maxflow_with_usage(source, sink, limit, caps):
    if limit <= 0:
        return 0, [0] * m

    graph = [[] for _ in range(n)]
    refs = [None] * m

    def add_edge(u, v, c, eid):
        fwd = [v, len(graph[v]), c]
        rev = [u, len(graph[u]), 0]
        graph[u].append(fwd)
        graph[v].append(rev)
        refs[eid] = (fwd, c)

    for eid, (u, v) in enumerate(edges):
        c = caps[eid]
        if c > 0 and u != v:
            add_edge(u, v, c, eid)

    flow = 0
    level = [-1] * n

    while flow < limit:
        level[:] = [-1] * n
        level[source] = 0
        q = deque([source])

        while q:
            u = q.popleft()
            for e in graph[u]:
                if e[2] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])

        if level[sink] < 0:
            break

        ptr = [0] * n

        def send(u, pushed):
            if u == sink:
                return pushed
            while ptr[u] < len(graph[u]):
                e = graph[u][ptr[u]]
                v = e[0]
                if e[2] > 0 and level[v] == level[u] + 1:
                    got = send(v, min(pushed, e[2]))
                    if got:
                        e[2] -= got
                        graph[v][e[1]][2] += got
                        return got
                ptr[u] += 1
            return 0

        while flow < limit:
            pushed = send(source, limit - flow)
            if not pushed:
                break
            flow += pushed

    usage = [0] * m
    if flow:
        for eid, ref in enumerate(refs):
            if ref is not None:
                fwd, original = ref
                usage[eid] = original - fwd[2]

    return flow, usage


# Check individual feasibility and order the most constrained commodities first.
ordered = []
for commodity in commodities:
    s, t, d, original_index = commodity
    if d == 0:
        slack_ratio = float("inf")
    else:
        possible, _ = maxflow_with_usage(s, t, d, capacities)
        if possible < d:
            print("NO")
            sys.exit()
        slack_ratio = possible / d
    ordered.append((slack_ratio, -d, commodity))

ordered.sort(key=lambda x: (x[0], x[1]))
ordered = [x[2] for x in ordered]

answer = [[0] * m for _ in range(k)]
residual = capacities[:]
failed = set()
MEMO_LIMIT = 30000


def path_generator(source, sink, last_path):
    visited = [False] * n
    visited[source] = True
    path = []

    def generate(u, cmp_state):
        if u == sink:
            if last_path is None or cmp_state > 0:
                yield tuple(path)
            return

        depth = len(path)
        for eid in out_edges[u]:
            if residual[eid] <= 0:
                continue
            v = edges[eid][1]
            if visited[v]:
                continue

            new_cmp = cmp_state
            if last_path is not None and cmp_state == 0:
                if depth >= len(last_path):
                    new_cmp = 1
                elif eid < last_path[depth]:
                    continue
                elif eid > last_path[depth]:
                    new_cmp = 1

            visited[v] = True
            path.append(eid)
            yield from generate(v, new_cmp)
            path.pop()
            visited[v] = False

    initial_cmp = 1 if last_path is None else 0
    yield from generate(source, initial_cmp)


def solve(ci, remaining, last_path):
    if ci == k:
        return True

    s, t, demand, original_index = ordered[ci]

    if demand == 0:
        return solve(ci + 1, ordered[ci + 1][2] if ci + 1 < k else 0, None)

    if remaining == 0:
        return solve(ci + 1, ordered[ci + 1][2] if ci + 1 < k else 0, None)

    key = (ci, remaining, last_path, tuple(residual))
    if key in failed:
        return False

    # Every still-unfinished commodity must independently fit in the
    # currently residual network.
    current_flow, completion_usage = maxflow_with_usage(s, t, remaining, residual)
    if current_flow < remaining:
        if len(failed) >= MEMO_LIMIT:
            failed.clear()
        failed.add(key)
        return False

    for j in range(ci + 1, k):
        fs, ft, fd, _ = ordered[j]
        if fd == 0:
            continue
        possible, _ = maxflow_with_usage(fs, ft, fd, residual)
        if possible < fd:
            if len(failed) >= MEMO_LIMIT:
                failed.clear()
            failed.add(key)
            return False

    # First try a complete max-flow routing for this commodity.
    changed = []
    valid_completion = True
    for eid, value in enumerate(completion_usage):
        if value:
            if value > residual[eid]:
                valid_completion = False
                break
            residual[eid] -= value
            answer[original_index][eid] += value
            changed.append((eid, value))

    if valid_completion:
        next_remaining = ordered[ci + 1][2] if ci + 1 < k else 0
        if solve(ci + 1, next_remaining, None):
            return True

    for eid, value in changed:
        residual[eid] += value
        answer[original_index][eid] -= value

    # Exhaustively branch over a canonical, lexicographically ordered
    # decomposition into simple paths.
    for path in path_generator(s, t, last_path):
        bottleneck = remaining
        for eid in path:
            if residual[eid] < bottleneck:
                bottleneck = residual[eid]

        for amount in range(bottleneck, 0, -1):
            for eid in path:
                residual[eid] -= amount
                answer[original_index][eid] += amount

            if solve(ci, remaining - amount, path):
                return True

            for eid in path:
                residual[eid] += amount
                answer[original_index][eid] -= amount

    if len(failed) >= MEMO_LIMIT:
        failed.clear()
    failed.add(key)
    return False


initial_remaining = ordered[0][2] if k > 0 else 0

if solve(0, initial_remaining, None):
    output = ["YES"]
    for row in answer:
        output.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(output))
else:
    print("NO")
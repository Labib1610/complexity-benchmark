import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n_left = next(it)
n_right = next(it)
m = next(it)

U = [0] * m
V = [0] * m
deg_left_initial = [0] * n_left
deg_right_initial = [0] * n_right

for i in range(m):
    u = next(it) - 1
    v = next(it) - 1
    U[i] = u
    V[i] = v
    deg_left_initial[u] += 1
    deg_right_initial[v] += 1

delta = 0
if n_left:
    delta = max(delta, max(deg_left_initial))
if n_right:
    delta = max(delta, max(deg_right_initial))

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

answer = [0] * m

adj_left = [None] * n_left
adj_right = [None] * n_right
mate_left = [-1] * n_left
mate_right = [-1] * n_right
dist_left = [-1] * n_left
dist_right = [-1] * n_right
ptr_left = [0] * n_left
ptr_right = [0] * n_right

pending_left = [-1] * n_left
pending_right = [-1] * n_right
pair_left = [-1] * m
pair_right = [-1] * m
side = bytearray([2]) * m
selected = bytearray(m)


def matching_covering_max_degree(edges, degree_bound):
    touched_left = []
    touched_right = []

    for e in edges:
        u = U[e]
        v = V[e]

        if adj_left[u] is None:
            adj_left[u] = []
            touched_left.append(u)
        adj_left[u].append(e)

        if adj_right[v] is None:
            adj_right[v] = []
            touched_right.append(v)
        adj_right[v].append(e)

    required_left = [u for u in touched_left if len(adj_left[u]) == degree_bound]
    required_right = [v for v in touched_right if len(adj_right[v]) == degree_bound]

    def dfs_left(u):
        adjacency = adj_left[u]
        i = ptr_left[u]
        while i < len(adjacency):
            e = adjacency[i]
            ptr_left[u] = i + 1
            v = V[e]
            old = mate_right[v]

            if old == -1:
                mate_left[u] = e
                mate_right[v] = e
                return True

            u2 = U[old]
            if dist_left[u2] == dist_left[u] + 1 and dfs_left(u2):
                mate_left[u] = e
                mate_right[v] = e
                return True

            i = ptr_left[u]

        dist_left[u] = -1
        return False

    while True:
        q = deque()
        for u in touched_left:
            dist_left[u] = -1
            ptr_left[u] = 0

        missing = 0
        for u in required_left:
            if mate_left[u] == -1:
                dist_left[u] = 0
                q.append(u)
                missing += 1

        if missing == 0:
            break

        while q:
            u = q.popleft()
            for e in adj_left[u]:
                v = V[e]
                old = mate_right[v]
                if old != -1:
                    u2 = U[old]
                    if dist_left[u2] == -1:
                        dist_left[u2] = dist_left[u] + 1
                        q.append(u2)

        augmented = 0
        for u in required_left:
            if mate_left[u] == -1 and dfs_left(u):
                augmented += 1

        if augmented == 0:
            break

    def dfs_right(v):
        adjacency = adj_right[v]
        i = ptr_right[v]
        while i < len(adjacency):
            e = adjacency[i]
            ptr_right[v] = i + 1
            u = U[e]
            old = mate_left[u]

            if old == -1:
                mate_right[v] = e
                mate_left[u] = e
                return True

            v2 = V[old]
            if dist_right[v2] == dist_right[v] + 1 and dfs_right(v2):
                mate_right[v] = e
                mate_left[u] = e
                return True

            i = ptr_right[v]

        dist_right[v] = -1
        return False

    while True:
        q = deque()
        for v in touched_right:
            dist_right[v] = -1
            ptr_right[v] = 0

        missing = 0
        for v in required_right:
            if mate_right[v] == -1:
                dist_right[v] = 0
                q.append(v)
                missing += 1

        if missing == 0:
            break

        while q:
            v = q.popleft()
            for e in adj_right[v]:
                u = U[e]
                old = mate_left[u]
                if old != -1:
                    v2 = V[old]
                    if dist_right[v2] == -1:
                        dist_right[v2] = dist_right[v] + 1
                        q.append(v2)

        augmented = 0
        for v in required_right:
            if mate_right[v] == -1 and dfs_right(v):
                augmented += 1

        if augmented == 0:
            break

    matching = []
    for u in touched_left:
        e = mate_left[u]
        if e != -1:
            matching.append(e)
            selected[e] = 1

    for u in touched_left:
        adj_left[u] = None
        mate_left[u] = -1
    for v in touched_right:
        adj_right[v] = None
        mate_right[v] = -1

    return matching


def balanced_split(edges):
    touched_left = []
    touched_right = []

    for e in edges:
        pair_left[e] = -1
        pair_right[e] = -1
        side[e] = 2

        u = U[e]
        old = pending_left[u]
        if old == -1:
            pending_left[u] = e
            touched_left.append(u)
        else:
            pair_left[e] = old
            pair_left[old] = e
            pending_left[u] = -1

        v = V[e]
        old = pending_right[v]
        if old == -1:
            pending_right[v] = e
            touched_right.append(v)
        else:
            pair_right[e] = old
            pair_right[old] = e
            pending_right[v] = -1

    for u in touched_left:
        pending_left[u] = -1
    for v in touched_right:
        pending_right[v] = -1

    first = []
    second = []
    stack = []

    for start in edges:
        if side[start] != 2:
            continue

        side[start] = 0
        stack.append(start)

        while stack:
            e = stack.pop()
            c = side[e]

            x = pair_left[e]
            if x != -1 and side[x] == 2:
                side[x] = c ^ 1
                stack.append(x)

            x = pair_right[e]
            if x != -1 and side[x] == 2:
                side[x] = c ^ 1
                stack.append(x)

    for e in edges:
        if side[e] == 0:
            first.append(e)
        else:
            second.append(e)

    return first, second


tasks = [(list(range(m)), delta, 1)]

while tasks:
    edges, d, base = tasks.pop()

    if not edges:
        continue

    if d == 1:
        for e in edges:
            answer[e] = base
        continue

    if d & 1:
        matching = matching_covering_max_degree(edges, d)
        matching_color = base + d - 1

        for e in matching:
            answer[e] = matching_color

        remaining = []
        for e in edges:
            if selected[e]:
                selected[e] = 0
            else:
                remaining.append(e)

        if remaining:
            tasks.append((remaining, d - 1, base))
    else:
        first, second = balanced_split(edges)
        half = d // 2

        if second:
            tasks.append((second, half, base + half))
        if first:
            tasks.append((first, half, base))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
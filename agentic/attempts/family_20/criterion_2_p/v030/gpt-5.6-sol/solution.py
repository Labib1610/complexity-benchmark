import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    raise SystemExit

n1, n2, m = data[0], data[1], data[2]
U = [0] * m
V = [0] * m
deg_u = [0] * n1
deg_v = [0] * n2

p = 3
for i in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[i] = u
    V[i] = v
    deg_u[u] += 1
    deg_v[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

delta = max(max(deg_u), max(deg_v))
answer = [0] * m


def balanced_split(edges):
    adjacency = {}
    degree = {}

    for eid in edges:
        a = U[eid]
        b = n1 + V[eid]
        adjacency.setdefault(a, []).append(eid)
        adjacency.setdefault(b, []).append(eid)
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0) + 1

    odd = [x for x, d in degree.items() if d & 1]
    original_count = len(edges)
    extra_u = []
    extra_v = []

    for i in range(0, len(odd), 2):
        a = odd[i]
        b = odd[i + 1]
        eid = original_count + len(extra_u)
        extra_u.append(a)
        extra_v.append(b)
        adjacency[a].append(eid)
        adjacency[b].append(eid)

    total_edges = original_count + len(extra_u)
    used = bytearray(total_edges)
    ptr = {x: len(lst) - 1 for x, lst in adjacency.items()}
    edge_by_local = edges

    first = []
    second = []

    def endpoints(eid):
        if eid < original_count:
            real = edge_by_local[eid]
            return U[real], n1 + V[real]
        j = eid - original_count
        return extra_u[j], extra_v[j]

    for start in list(adjacency.keys()):
        lst = adjacency[start]
        pos = ptr[start]
        while pos >= 0 and used[lst[pos]]:
            pos -= 1
        ptr[start] = pos
        if pos < 0:
            continue

        vertex_stack = [start]
        edge_stack = []
        tour = []

        while vertex_stack:
            x = vertex_stack[-1]
            pos = ptr[x]
            ax = adjacency[x]
            while pos >= 0 and used[ax[pos]]:
                pos -= 1
            ptr[x] = pos

            if pos < 0:
                vertex_stack.pop()
                if edge_stack:
                    tour.append(edge_stack.pop())
                continue

            eid = ax[pos]
            ptr[x] = pos - 1
            if used[eid]:
                continue
            used[eid] = 1

            a, b = endpoints(eid)
            y = b if x == a else a
            vertex_stack.append(y)
            edge_stack.append(eid)

        tour.reverse()

        cut = -1
        for i, eid in enumerate(tour):
            if eid >= original_count:
                cut = i
                break
        if cut != -1:
            tour = tour[cut + 1:] + tour[:cut + 1]

        parity = 0
        for eid in tour:
            if eid >= original_count:
                parity = 0
            else:
                real = edge_by_local[eid]
                if parity == 0:
                    first.append(real)
                else:
                    second.append(real)
                parity ^= 1

    return first, second


def covering_matching(edges, k):
    adj_l = {}
    adj_r = {}
    dl = {}
    dr = {}

    for eid in edges:
        u = U[eid]
        v = V[eid]
        adj_l.setdefault(u, []).append(eid)
        adj_r.setdefault(v, []).append(eid)
        dl[u] = dl.get(u, 0) + 1
        dr[v] = dr.get(v, 0) + 1

    if not any(d == k for d in dl.values()) and not any(d == k for d in dr.values()):
        return []

    pair_l = {}
    pair_r = {}

    # Hopcroft-Karp maximum matching.
    while True:
        dist = {}
        q = deque()

        for u in adj_l:
            if u not in pair_l:
                dist[u] = 0
                q.append(u)

        found = False
        while q:
            u = q.popleft()
            nd = dist[u] + 1
            for eid in adj_l[u]:
                v = V[eid]
                me = pair_r.get(v)
                if me is None:
                    found = True
                else:
                    u2 = U[me]
                    if u2 not in dist:
                        dist[u2] = nd
                        q.append(u2)

        if not found:
            break

        it = {}

        def dfs(u):
            arr = adj_l[u]
            i = it.get(u, 0)
            while i < len(arr):
                eid = arr[i]
                i += 1
                it[u] = i
                v = V[eid]
                me = pair_r.get(v)
                if me is None:
                    pair_l[u] = eid
                    pair_r[v] = eid
                    return True
                u2 = U[me]
                if dist.get(u2) == dist[u] + 1 and dfs(u2):
                    pair_l[u] = eid
                    pair_r[v] = eid
                    return True
            dist[u] = -1
            return False

        augmented = 0
        for u in adj_l:
            if u not in pair_l and dfs(u):
                augmented += 1
        if augmented == 0:
            break

    def flip_path(path):
        for eid in path:
            u = U[eid]
            v = V[eid]
            if pair_l.get(u) == eid:
                del pair_l[u]
            if pair_r.get(v) == eid:
                del pair_r[v]

        for i in range(0, len(path), 2):
            eid = path[i]
            pair_l[U[eid]] = eid
            pair_r[V[eid]] = eid

    def repair_left():
        required = [u for u, d in dl.items() if d == k and u not in pair_l]

        for source in required:
            if source in pair_l:
                continue

            parent = {source: None}
            q = deque([source])
            target_same = None
            target_opposite = None
            target_edge = None
            target_from = None

            while q and target_same is None and target_opposite is None:
                u = q.popleft()
                matched_u = pair_l.get(u)

                for eid in adj_l[u]:
                    if eid == matched_u:
                        continue
                    v = V[eid]
                    me = pair_r.get(v)

                    if me is None:
                        target_opposite = v
                        target_edge = eid
                        target_from = u
                        break

                    u2 = U[me]
                    if u2 in parent:
                        continue
                    parent[u2] = (u, eid, me)

                    if dl.get(u2, 0) < k:
                        target_same = u2
                        break
                    q.append(u2)

            if target_same is not None:
                pieces = []
                cur = target_same
                while cur != source:
                    prev, e1, e2 = parent[cur]
                    pieces.append((e1, e2))
                    cur = prev
                path = []
                for e1, e2 in reversed(pieces):
                    path.append(e1)
                    path.append(e2)
                flip_path(path)
            elif target_opposite is not None:
                pieces = []
                cur = target_from
                while cur != source:
                    prev, e1, e2 = parent[cur]
                    pieces.append((e1, e2))
                    cur = prev
                path = []
                for e1, e2 in reversed(pieces):
                    path.append(e1)
                    path.append(e2)
                path.append(target_edge)
                flip_path(path)

    def repair_right():
        required = [v for v, d in dr.items() if d == k and v not in pair_r]

        for source in required:
            if source in pair_r:
                continue

            parent = {source: None}
            q = deque([source])
            target_same = None
            target_opposite = None
            target_edge = None
            target_from = None

            while q and target_same is None and target_opposite is None:
                v = q.popleft()
                matched_v = pair_r.get(v)

                for eid in adj_r[v]:
                    if eid == matched_v:
                        continue
                    u = U[eid]
                    me = pair_l.get(u)

                    if me is None:
                        target_opposite = u
                        target_edge = eid
                        target_from = v
                        break

                    v2 = V[me]
                    if v2 in parent:
                        continue
                    parent[v2] = (v, eid, me)

                    if dr.get(v2, 0) < k:
                        target_same = v2
                        break
                    q.append(v2)

            if target_same is not None:
                pieces = []
                cur = target_same
                while cur != source:
                    prev, e1, e2 = parent[cur]
                    pieces.append((e1, e2))
                    cur = prev
                path = []
                for e1, e2 in reversed(pieces):
                    path.append(e1)
                    path.append(e2)
                flip_path(path)
            elif target_opposite is not None:
                pieces = []
                cur = target_from
                while cur != source:
                    prev, e1, e2 = parent[cur]
                    pieces.append((e1, e2))
                    cur = prev
                path = []
                for e1, e2 in reversed(pieces):
                    path.append(e1)
                    path.append(e2)
                path.append(target_edge)
                flip_path(path)

    repair_left()
    repair_right()

    return list(pair_l.values())


stack = [(list(range(m)), delta, 1)]

while stack:
    edges, k, first_color = stack.pop()
    if not edges:
        continue

    if k == 1:
        for eid in edges:
            answer[eid] = first_color
        continue

    if k & 1:
        matching = covering_matching(edges, k)
        in_matching = set(matching)

        for eid in matching:
            answer[eid] = first_color

        remaining = [eid for eid in edges if eid not in in_matching]
        stack.append((remaining, k - 1, first_color + 1))
    else:
        a, b = balanced_split(edges)
        half = k // 2
        stack.append((b, half, first_color + half))
        stack.append((a, half, first_color))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)) + "\n")
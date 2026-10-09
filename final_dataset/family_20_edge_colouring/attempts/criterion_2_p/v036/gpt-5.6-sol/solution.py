import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = sys.stdin.buffer
nL, nR, m = map(int, data.readline().split())

X = [0] * m
Y = [0] * m
degL = [0] * nL
degR = [0] * nR

for i in range(m):
    u, v = map(int, data.readline().split())
    u -= 1
    v -= 1
    X[i] = u
    Y[i] = v
    degL[u] += 1
    degR[v] += 1

D = max(max(degL, default=0), max(degR, default=0))

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

answer = [0] * m
mark = [0] * m
mark_token = 0


def balanced_split(edges):
    global mark_token
    mark_token += 1
    token = mark_token

    adj = {}
    offset = nL

    for e in edges:
        a = X[e]
        b = offset + Y[e]
        adj.setdefault(a, []).append(e)
        adj.setdefault(b, []).append(e)

    first = []
    second = []

    def walk(start):
        cur = start
        parity = 0
        while True:
            lst = adj[cur]
            while lst and mark[lst[-1]] == token:
                lst.pop()
            if not lst:
                break

            e = lst.pop()
            if mark[e] == token:
                continue
            mark[e] = token

            if parity == 0:
                first.append(e)
            else:
                second.append(e)
            parity ^= 1

            a = X[e]
            b = offset + Y[e]
            cur = b if cur == a else a

    odd_vertices = [v for v, lst in adj.items() if len(lst) & 1]
    for v in odd_vertices:
        walk(v)

    for v in adj:
        walk(v)

    return first, second


def extract_matching(edges, delta):
    adj_l = {}
    adj_r = {}

    for e in edges:
        u = X[e]
        v = Y[e]
        adj_l.setdefault(u, []).append(e)
        adj_r.setdefault(v, []).append(e)

    required_l = [u for u, lst in adj_l.items() if len(lst) == delta]
    required_r = {v for v, lst in adj_r.items() if len(lst) == delta}

    match_l = {}
    match_r = {}

    # First saturate all required left vertices with Hopcroft-Karp.
    while True:
        dist = {}
        q = deque()
        for u in required_l:
            if u not in match_l:
                dist[u] = 0
                q.append(u)

        if not q:
            break

        best = None
        while q:
            u = q.popleft()
            d = dist[u]
            if best is not None and d >= best:
                continue

            for e in adj_l[u]:
                v = Y[e]
                old = match_r.get(v)
                if old is None:
                    best = d + 1
                else:
                    u2 = X[old]
                    if u2 not in dist:
                        dist[u2] = d + 1
                        q.append(u2)

        if best is None:
            break

        ptr = {}

        def dfs_left(u):
            i = ptr.get(u, 0)
            lst = adj_l[u]
            while i < len(lst):
                e = lst[i]
                i += 1
                ptr[u] = i
                v = Y[e]
                old = match_r.get(v)

                if old is None:
                    if dist[u] + 1 != best:
                        continue
                    match_l[u] = e
                    match_r[v] = e
                    return True

                u2 = X[old]
                if dist.get(u2) == dist[u] + 1 and dfs_left(u2):
                    match_l[u] = e
                    match_r[v] = e
                    return True

            dist[u] = -1
            return False

        changed = False
        for u in required_l:
            if u not in match_l and dist.get(u, -1) >= 0:
                if dfs_left(u):
                    changed = True
        if not changed:
            break

    # Then saturate required right vertices without uncovering required left
    # vertices or already covered required right vertices.
    while True:
        sources = [v for v in required_r if v not in match_r]
        if not sources:
            break

        dist = {}
        q = deque()
        for v in sources:
            dist[v] = 0
            q.append(v)

        best = None
        while q:
            v = q.popleft()
            d = dist[v]
            if best is not None and d >= best:
                continue

            matched_edge = match_r.get(v)
            for e in adj_r[v]:
                if e == matched_edge:
                    continue

                u = X[e]
                old = match_l.get(u)
                if old is None:
                    best = d + 1
                    continue

                v2 = Y[old]
                if v2 not in required_r:
                    best = d + 1
                elif v2 not in dist:
                    dist[v2] = d + 1
                    q.append(v2)

        if best is None:
            break

        ptr = {}

        def dfs_right(v):
            i = ptr.get(v, 0)
            lst = adj_r[v]
            current = match_r.get(v)

            while i < len(lst):
                e = lst[i]
                i += 1
                ptr[v] = i

                if e == current:
                    continue

                u = X[e]
                old = match_l.get(u)

                if old is None:
                    if dist[v] + 1 != best:
                        continue
                    match_l[u] = e
                    match_r[v] = e
                    return True

                v2 = Y[old]
                if v2 not in required_r:
                    if dist[v] + 1 != best:
                        continue
                    match_r.pop(v2, None)
                    match_l[u] = e
                    match_r[v] = e
                    return True

                if dist.get(v2) == dist[v] + 1 and dfs_right(v2):
                    match_l[u] = e
                    match_r[v] = e
                    return True

            dist[v] = -1
            return False

        changed = False
        for v in sources:
            if v not in match_r and dist.get(v, -1) >= 0:
                if dfs_right(v):
                    changed = True
        if not changed:
            break

    return set(match_l.values())


def solve(edges, delta, base_color):
    if not edges:
        return

    if delta == 1:
        for e in edges:
            answer[e] = base_color
        return

    if delta & 1:
        matching = extract_matching(edges, delta)
        remaining = []
        for e in edges:
            if e in matching:
                answer[e] = base_color
            else:
                remaining.append(e)
        solve(remaining, delta - 1, base_color + 1)
    else:
        left_edges, right_edges = balanced_split(edges)
        half = delta // 2
        solve(left_edges, half, base_color)
        solve(right_edges, half, base_color + half)


solve(list(range(m)), D, 1)

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
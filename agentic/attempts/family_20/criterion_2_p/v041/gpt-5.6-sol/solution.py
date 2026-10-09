import sys
from collections import deque
from array import array

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

nA, nB, m = data[0], data[1], data[2]
U = [0] * m
V = [0] * m
degA = [0] * nA
degB = [0] * nB

p = 3
for i in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[i] = u
    V[i] = v
    degA[u] += 1
    degB[v] += 1

K = max(max(degA, default=0), max(degB, default=0))
answer = [0] * m


def balanced_split(edges):
    q = len(edges)
    if q == 0:
        return [], []

    degree = {}
    odd_left = []
    odd_right = []

    for e in edges:
        u = U[e]
        v = nA + V[e]
        degree[u] = degree.get(u, 0) + 1
        degree[v] = degree.get(v, 0) + 1

    for x, d in degree.items():
        if d & 1:
            if x < nA:
                odd_left.append(x)
            else:
                odd_right.append(x)

    eu = array('i')
    ev = array('i')
    for e in edges:
        eu.append(U[e])
        ev.append(nA + V[e])

    next_vertex = nA + nB

    if len(odd_left) & 1:
        eu.append(odd_left.pop())
        ev.append(odd_right.pop())

    while odd_left:
        a = odd_left.pop()
        b = odd_left.pop()
        dummy = next_vertex
        next_vertex += 1
        eu.append(a)
        ev.append(dummy)
        eu.append(dummy)
        ev.append(b)

    while odd_right:
        a = odd_right.pop()
        b = odd_right.pop()
        dummy = next_vertex
        next_vertex += 1
        eu.append(a)
        ev.append(dummy)
        eu.append(dummy)
        ev.append(b)

    total = len(eu)
    head = array('i', [-1]) * next_vertex
    nxt = array('i', [0]) * (2 * total)
    edge_id = array('i', [0]) * (2 * total)

    pos = 0
    for i in range(total):
        a = eu[i]
        b = ev[i]

        edge_id[pos] = i
        nxt[pos] = head[a]
        head[a] = pos
        pos += 1

        edge_id[pos] = i
        nxt[pos] = head[b]
        head[b] = pos
        pos += 1

    cursor = array('i', head)
    used = bytearray(total)
    side = bytearray(q)

    for start in degree:
        h = cursor[start]
        while h != -1 and used[edge_id[h]]:
            h = nxt[h]
        cursor[start] = h
        if h == -1:
            continue

        stack_v = [start]
        stack_e = [-1]
        parity = 0

        while stack_v:
            x = stack_v[-1]
            h = cursor[x]
            while h != -1 and used[edge_id[h]]:
                h = nxt[h]
            cursor[x] = h

            if h == -1:
                stack_v.pop()
                e_local = stack_e.pop()
                if e_local != -1:
                    if e_local < q:
                        side[e_local] = parity
                    parity ^= 1
                continue

            e_local = edge_id[h]
            used[e_local] = 1
            cursor[x] = nxt[h]
            y = ev[e_local] if eu[e_local] == x else eu[e_local]
            stack_v.append(y)
            stack_e.append(e_local)

    first = []
    second = []
    for i, e in enumerate(edges):
        if side[i]:
            second.append(e)
        else:
            first.append(e)
    return first, second


def extract_matching(edges, D):
    adjL = {}
    adjR = {}

    for e in edges:
        u = U[e]
        r = V[e]
        adjL.setdefault(u, []).append(e)
        adjR.setdefault(r, []).append(e)

    requiredL = [u for u, es in adjL.items() if len(es) == D]
    requiredR = [r for r, es in adjR.items() if len(es) == D]
    requiredR_set = set(requiredR)

    matchL = {}
    matchR = {}
    matchEdgeL = {}

    dist = {}

    def bfs():
        queue = deque()
        found = False
        for u in requiredL:
            if u not in matchL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1

        while queue:
            u = queue.popleft()
            nd = dist[u] + 1
            for e in adjL[u]:
                r = V[e]
                u2 = matchR.get(r)
                if u2 is None:
                    found = True
                elif dist.get(u2, -1) == -1:
                    dist[u2] = nd
                    queue.append(u2)
        return found

    def dfs_hk(u):
        for e in adjL[u]:
            r = V[e]
            u2 = matchR.get(r)
            if u2 is None or (
                dist.get(u2, -1) == dist[u] + 1 and dfs_hk(u2)
            ):
                matchL[u] = r
                matchR[r] = u
                matchEdgeL[u] = e
                return True
        dist[u] = -1
        return False

    while bfs():
        for u in requiredL:
            if u not in matchL:
                dfs_hk(u)

    seen = set()

    def rematch_required_r(r):
        if r in seen:
            return False
        seen.add(r)

        for e in adjR[r]:
            u = U[e]
            old_r = matchL.get(u)

            if old_r is None or old_r not in requiredR_set or rematch_required_r(old_r):
                if old_r is not None:
                    matchR.pop(old_r, None)
                matchL[u] = r
                matchR[r] = u
                matchEdgeL[u] = e
                return True
        return False

    for r in requiredR:
        if r not in matchR:
            seen.clear()
            rematch_required_r(r)

    return set(matchEdgeL.values())


def color_graph(edges, D, offset):
    if not edges:
        return
    if D == 1:
        for e in edges:
            answer[e] = offset
        return

    if D & 1:
        matching = extract_matching(edges, D)
        remaining = []
        for e in edges:
            if e in matching:
                answer[e] = offset
            else:
                remaining.append(e)
        color_graph(remaining, D - 1, offset + 1)
    else:
        first, second = balanced_split(edges)
        half = D // 2
        color_graph(first, half, offset)
        color_graph(second, half, offset + half)


if m:
    color_graph(list(range(m)), K, 1)

out = ["YES", " ".join(map(str, answer))]
sys.stdout.write("\n".join(out))
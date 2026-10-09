import sys
from array import array
from collections import deque

sys.setrecursionlimit(1_000_000)

data = sys.stdin.buffer.read()
p = 0
ln = len(data)

def next_int():
    global p
    while p < ln and data[p] <= 32:
        p += 1
    x = 0
    while p < ln and data[p] > 32:
        x = x * 10 + data[p] - 48
        p += 1
    return x

nL = next_int()
nR = next_int()
m = next_int()

U = array('i')
V = array('i')
degL0 = array('i', [0]) * nL
degR0 = array('i', [0]) * nR

for _ in range(m):
    u = next_int() - 1
    v = next_int() - 1
    U.append(u)
    V.append(v)
    degL0[u] += 1
    degR0[v] += 1

delta = 0
if nL:
    delta = max(delta, max(degL0))
if nR:
    delta = max(delta, max(degR0))

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

colors = array('i', [0]) * m
selected_mark = bytearray(m)

def split_even(edges, bound):
    total_vertices = nL + nR
    dummy = total_vertices

    head = array('i', [-1]) * (total_vertices + 1)
    degree = array('i', [0]) * total_vertices
    nxt = array('i')
    touched = []

    for token, eid in enumerate(edges):
        a = U[eid]
        b = nL + V[eid]

        if degree[a] == 0:
            touched.append(a)
        if degree[b] == 0:
            touched.append(b)
        degree[a] += 1
        degree[b] += 1

        nxt.append(head[a])
        head[a] = token << 1
        nxt.append(head[b])
        head[b] = (token << 1) | 1

    odd = []
    for x in touched:
        if degree[x] & 1:
            odd.append(x)

    real_count = len(edges)
    for j, x in enumerate(odd):
        token = real_count + j
        nxt.append(head[x])
        head[x] = token << 1
        nxt.append(head[dummy])
        head[dummy] = (token << 1) | 1

    token_count = real_count + len(odd)
    used = bytearray(token_count)
    left = []
    right = []

    def other_vertex(token, cur):
        if token < real_count:
            eid = edges[token]
            a = U[eid]
            b = nL + V[eid]
            return b if cur == a else a
        x = odd[token - real_count]
        return dummy if cur == x else x

    def consume(start):
        vertex_stack = [start]
        edge_stack = []
        tour = []

        while vertex_stack:
            x = vertex_stack[-1]
            inc = head[x]
            while inc != -1 and used[inc >> 1]:
                inc = nxt[inc]
            head[x] = inc

            if inc == -1:
                vertex_stack.pop()
                if edge_stack:
                    tour.append(edge_stack.pop())
                continue

            head[x] = nxt[inc]
            token = inc >> 1
            if used[token]:
                continue
            used[token] = 1
            y = other_vertex(token, x)
            vertex_stack.append(y)
            edge_stack.append(token)

        for i, token in enumerate(tour):
            if token < real_count:
                if i & 1:
                    right.append(edges[token])
                else:
                    left.append(edges[token])

    if odd and head[dummy] != -1:
        consume(dummy)

    for x in touched:
        if head[x] != -1:
            consume(x)

    return left, right

def find_covering_matching(edges, bound):
    adjL = {}
    adjR = {}
    degL = {}
    degR = {}

    for eid in edges:
        u = U[eid]
        v = V[eid]
        if u in adjL:
            adjL[u].append(eid)
            degL[u] += 1
        else:
            adjL[u] = [eid]
            degL[u] = 1
        if v in adjR:
            adjR[v].append(eid)
            degR[v] += 1
        else:
            adjR[v] = [eid]
            degR[v] = 1

    required_left = [u for u, d in degL.items() if d == bound]
    required_right_set = {v for v, d in degR.items() if d == bound}

    matchL = {}
    matchR = {}
    dist = {}

    def bfs():
        q = deque()
        found = False
        for u in required_left:
            if u not in matchL:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1

        while q:
            u = q.popleft()
            nd = dist[u] + 1
            for eid in adjL[u]:
                v = V[eid]
                old = matchR.get(v)
                if old is None:
                    found = True
                else:
                    u2 = U[old]
                    if dist.get(u2, -1) == -1:
                        dist[u2] = nd
                        q.append(u2)
        return found

    def dfs_left(u):
        for eid in adjL[u]:
            v = V[eid]
            old = matchR.get(v)
            if old is None:
                matchL[u] = eid
                matchR[v] = eid
                return True
            u2 = U[old]
            if dist.get(u2, -1) == dist[u] + 1 and dfs_left(u2):
                matchL[u] = eid
                matchR[v] = eid
                return True
        dist[u] = -1
        return False

    while bfs():
        for u in required_left:
            if u not in matchL:
                dfs_left(u)

    # Saturate required right vertices by alternating swaps. These swaps never
    # make a matched left vertex unmatched.
    def repair_right(root):
        seen = set()

        def dfs_right(v):
            if v in seen:
                return False
            seen.add(v)

            for eid in adjR[v]:
                u = U[eid]
                old = matchL.get(u)

                if old is None:
                    matchL[u] = eid
                    matchR[v] = eid
                    return True

                old_v = V[old]
                if old_v == v:
                    return True

                if old_v not in required_right_set:
                    matchR.pop(old_v, None)
                    matchL[u] = eid
                    matchR[v] = eid
                    return True

                if dfs_right(old_v):
                    matchL[u] = eid
                    matchR[v] = eid
                    return True
            return False

        return dfs_right(root)

    for v in required_right_set:
        if v not in matchR:
            repair_right(v)

    return list(matchL.values())

stack = [(list(range(m)), delta)]
next_color = 1

while stack:
    edges, bound = stack.pop()
    if not edges:
        continue

    if bound == 1:
        c = next_color
        next_color += 1
        for eid in edges:
            colors[eid] = c
        continue

    if bound & 1:
        matching = find_covering_matching(edges, bound)
        c = next_color
        next_color += 1

        for eid in matching:
            colors[eid] = c
            selected_mark[eid] = 1

        remainder = []
        for eid in edges:
            if not selected_mark[eid]:
                remainder.append(eid)

        for eid in matching:
            selected_mark[eid] = 0

        if remainder:
            stack.append((remainder, bound - 1))
    else:
        a, b = split_even(edges, bound)
        half = bound >> 1
        if b:
            stack.append((b, half))
        if a:
            stack.append((a, half))

out = ["YES\n", " ".join(map(str, colors)), "\n"]
sys.stdout.write("".join(out))
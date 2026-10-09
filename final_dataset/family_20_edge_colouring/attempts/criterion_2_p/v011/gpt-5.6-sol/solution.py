import sys
from array import array
from collections import deque

sys.setrecursionlimit(1_000_000)

data = sys.stdin.buffer.read()
pos = 0
length = len(data)

def read_int():
    global pos
    while pos < length and data[pos] <= 32:
        pos += 1
    value = 0
    while pos < length and data[pos] > 32:
        value = value * 10 + data[pos] - 48
        pos += 1
    return value

nL = read_int()
nR = read_int()
m = read_int()

U = array('i')
V = array('i')
for _ in range(m):
    U.append(read_int() - 1)
    V.append(read_int() - 1)

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

headL = array('i', [-1]) * nL
headR = array('i', [-1]) * nR
degL = array('i', [0]) * nL
degR = array('i', [0]) * nR

nextL = array('i', [-1]) * m
nextR = array('i', [-1]) * m

matchL = array('i', [-1]) * nL
matchR = array('i', [-1]) * nR
dist = array('i', [-1]) * nL
ptr = array('i', [-1]) * nL
seenR = array('i', [0]) * nR

pairL = array('i', [-1]) * m
pairR = array('i', [-1]) * m
split_color = bytearray(m)
chosen = bytearray(m)
answer = array('i', [0]) * m

stamp = 0

def build_adjacency(edges):
    touchedL = []
    touchedR = []

    for e in edges:
        u = U[e]
        v = V[e]

        if headL[u] == -1:
            touchedL.append(u)
        nextL[e] = headL[u]
        headL[u] = e
        degL[u] += 1

        if headR[v] == -1:
            touchedR.append(v)
        nextR[e] = headR[v]
        headR[v] = e
        degR[v] += 1

    return touchedL, touchedR

def clear_adjacency(touchedL, touchedR):
    for u in touchedL:
        headL[u] = -1
        degL[u] = 0
        matchL[u] = -1
        dist[u] = -1
        ptr[u] = -1

    for v in touchedR:
        headR[v] = -1
        degR[v] = 0
        matchR[v] = -1

def critical_matching(edges, D):
    global stamp

    touchedL, touchedR = build_adjacency(edges)
    criticalL = [u for u in touchedL if degL[u] == D]
    criticalR = [v for v in touchedR if degR[v] == D]

    def bfs():
        q = deque()
        found = False

        for u in criticalL:
            if matchL[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
            ptr[u] = headL[u]

        while q:
            u = q.popleft()
            nd = dist[u] + 1
            e = headL[u]
            while e != -1:
                v = V[e]
                me = matchR[v]
                if me == -1:
                    found = True
                else:
                    u2 = U[me]
                    if dist[u2] == -1:
                        dist[u2] = nd
                        q.append(u2)
                e = nextL[e]

        return found

    def dfs_left(u):
        e = ptr[u]
        while e != -1:
            ptr[u] = nextL[e]
            v = V[e]
            me = matchR[v]

            if me == -1:
                matchL[u] = e
                matchR[v] = e
                return True

            u2 = U[me]
            if dist[u2] == dist[u] + 1 and dfs_left(u2):
                matchL[u] = e
                matchR[v] = e
                return True

            e = ptr[u]

        dist[u] = -1
        return False

    while bfs():
        for u in criticalL:
            if matchL[u] == -1:
                dfs_left(u)

    def reroute_right(r, current_stamp):
        seenR[r] = current_stamp
        e = headR[r]

        while e != -1:
            l = U[e]
            old = matchL[l]

            if old != e:
                if old == -1:
                    matchL[l] = e
                    matchR[r] = e
                    return True

                old_r = V[old]
                if degR[old_r] != D:
                    matchR[old_r] = -1
                    matchL[l] = e
                    matchR[r] = e
                    return True

                if seenR[old_r] != current_stamp and reroute_right(old_r, current_stamp):
                    matchL[l] = e
                    matchR[r] = e
                    return True

            e = nextR[e]

        return False

    for r in criticalR:
        if matchR[r] == -1:
            stamp += 1
            reroute_right(r, stamp)

    matching = []
    for u in touchedL:
        e = matchL[u]
        if e != -1:
            matching.append(e)

    clear_adjacency(touchedL, touchedR)
    return matching

def balanced_split(edges):
    touchedL, touchedR = build_adjacency(edges)

    for e in edges:
        pairL[e] = -1
        pairR[e] = -1
        split_color[e] = 2

    for u in touchedL:
        e = headL[u]
        while e != -1:
            f = nextL[e]
            if f == -1:
                break
            pairL[e] = f
            pairL[f] = e
            e = nextL[f]

    for v in touchedR:
        e = headR[v]
        while e != -1:
            f = nextR[e]
            if f == -1:
                break
            pairR[e] = f
            pairR[f] = e
            e = nextR[f]

    left_edges = []
    right_edges = []
    stack = []

    for start in edges:
        if split_color[start] != 2:
            continue

        split_color[start] = 0
        stack.append(start)

        while stack:
            e = stack.pop()
            c = split_color[e]

            f = pairL[e]
            if f != -1 and split_color[f] == 2:
                split_color[f] = c ^ 1
                stack.append(f)

            f = pairR[e]
            if f != -1 and split_color[f] == 2:
                split_color[f] = c ^ 1
                stack.append(f)

    for e in edges:
        if split_color[e] == 0:
            left_edges.append(e)
        else:
            right_edges.append(e)

    clear_adjacency(touchedL, touchedR)
    return left_edges, right_edges

def solve(edges, D, first_color):
    if not edges:
        return

    if D == 1:
        for e in edges:
            answer[e] = first_color
        return

    if D & 1:
        matching = critical_matching(edges, D)

        for e in matching:
            chosen[e] = 1
            answer[e] = first_color + D - 1

        remaining = []
        for e in edges:
            if chosen[e]:
                chosen[e] = 0
            else:
                remaining.append(e)

        solve(remaining, D - 1, first_color)
    else:
        a, b = balanced_split(edges)
        half = D // 2
        solve(a, half, first_color)
        solve(b, half, first_color + half)

initial_edges = list(range(m))

for e in initial_edges:
    degL[U[e]] += 1
    degR[V[e]] += 1

Delta = 0
for d in degL:
    if d > Delta:
        Delta = d
for d in degR:
    if d > Delta:
        Delta = d

for i in range(nL):
    degL[i] = 0
for i in range(nR):
    degR[i] = 0

solve(initial_edges, Delta, 1)

out = ["YES\n", " ".join(map(str, answer)), "\n"]
sys.stdout.write("".join(out))
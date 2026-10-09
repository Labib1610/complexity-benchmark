import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
nL = next(it)
nR = next(it)
m = next(it)

U = [0] * m
V = [0] * m
degL0 = [0] * nL
degR0 = [0] * nR

for i in range(m):
    u = next(it) - 1
    v = next(it) - 1
    U[i] = u
    V[i] = v
    degL0[u] += 1
    degR0[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

Delta = max(max(degL0), max(degR0))

N = nL + nR
DUMMY = N
adj = [[] for _ in range(N + 1)]

degL = [0] * nL
degR = [0] * nR
pairL = [-1] * nL
pairR = [-1] * nR
pairEdgeL = [-1] * nL
reqL = bytearray(nL)
reqR = bytearray(nR)
dist = [-1] * nL

used_edge = bytearray(m)
chosen = bytearray(m)
answer = [0] * m


def extract_covering_matching(edges, d):
    touchedL = []
    touchedR = []

    for e in edges:
        l = U[e]
        r = V[e]
        if degL[l] == 0:
            touchedL.append(l)
        if degR[r] == 0:
            touchedR.append(r)
        degL[l] += 1
        degR[r] += 1
        adj[l].append(e)
        adj[nL + r].append(e)

    left_required = []
    right_required = []

    for l in touchedL:
        if degL[l] == d:
            reqL[l] = 1
            left_required.append(l)

    for r in touchedR:
        if degR[r] == d:
            reqR[r] = 1
            right_required.append(r)

    def bfs():
        q = deque()
        found = False
        for l in left_required:
            if pairL[l] == -1:
                dist[l] = 0
                q.append(l)
            else:
                dist[l] = -1

        while q:
            l = q.popleft()
            nd = dist[l] + 1
            for e in adj[l]:
                r = V[e]
                l2 = pairR[r]
                if l2 == -1:
                    found = True
                elif dist[l2] == -1:
                    dist[l2] = nd
                    q.append(l2)
        return found

    def dfs_left(l):
        for e in adj[l]:
            r = V[e]
            l2 = pairR[r]
            if l2 == -1 or (dist[l2] == dist[l] + 1 and dfs_left(l2)):
                pairL[l] = r
                pairR[r] = l
                pairEdgeL[l] = e
                return True
        dist[l] = -1
        return False

    while bfs():
        for l in left_required:
            if pairL[l] == -1:
                dfs_left(l)

    seenR = [0] * nR
    stamp = 0

    def reroute_right(r):
        seenR[r] = stamp
        for e in adj[nL + r]:
            l = U[e]
            old = pairL[l]
            if old == r:
                continue

            if old == -1:
                pairL[l] = r
                pairR[r] = l
                pairEdgeL[l] = e
                return True

            if not reqR[old]:
                pairR[old] = -1
                pairL[l] = r
                pairR[r] = l
                pairEdgeL[l] = e
                return True

            if seenR[old] != stamp and reroute_right(old):
                pairL[l] = r
                pairR[r] = l
                pairEdgeL[l] = e
                return True
        return False

    for r in right_required:
        if pairR[r] == -1:
            stamp += 1
            if not reroute_right(r):
                raise RuntimeError("Matching construction failed")

    matching = []
    for l in touchedL:
        if pairL[l] != -1:
            e = pairEdgeL[l]
            chosen[e] = 1
            matching.append(e)

    remaining = []
    for e in edges:
        if not chosen[e]:
            remaining.append(e)

    for e in matching:
        chosen[e] = 0

    for l in touchedL:
        adj[l].clear()
        degL[l] = 0
        reqL[l] = 0
        pairL[l] = -1
        pairEdgeL[l] = -1
        dist[l] = -1

    for r in touchedR:
        adj[nL + r].clear()
        degR[r] = 0
        reqR[r] = 0
        pairR[r] = -1

    return matching, remaining


def split_even(edges):
    touched = []
    touched_flag = set()

    for e in edges:
        l = U[e]
        rnode = nL + V[e]
        if l not in touched_flag:
            touched_flag.add(l)
            touched.append(l)
        if rnode not in touched_flag:
            touched_flag.add(rnode)
            touched.append(rnode)
        adj[l].append(e)
        adj[rnode].append(e)

    odd_vertices = [x for x in touched if len(adj[x]) & 1]
    virtual_vertex = odd_vertices
    virtual_count = len(virtual_vertex)
    virtual_used = bytearray(virtual_count)

    for i, x in enumerate(virtual_vertex):
        code = m + i
        adj[x].append(code)
        adj[DUMMY].append(code)

    first = []
    second = []

    def other_endpoint(code, x):
        if code < m:
            a = U[code]
            b = nL + V[code]
            return b if x == a else a
        y = virtual_vertex[code - m]
        return y if x == DUMMY else DUMMY

    def is_used(code):
        if code < m:
            return used_edge[code]
        return virtual_used[code - m]

    def mark_used(code):
        if code < m:
            used_edge[code] = 1
        else:
            virtual_used[code - m] = 1

    def process_tour(start):
        stack_nodes = [start]
        stack_edges = [-1]
        reversed_order = []

        while stack_nodes:
            x = stack_nodes[-1]
            ax = adj[x]
            while ax and is_used(ax[-1]):
                ax.pop()

            if ax:
                code = ax.pop()
                if is_used(code):
                    continue
                mark_used(code)
                y = other_endpoint(code, x)
                stack_nodes.append(y)
                stack_edges.append(code)
            else:
                stack_nodes.pop()
                code = stack_edges.pop()
                if code != -1:
                    reversed_order.append(code)

        reversed_order.reverse()
        side = 0
        for code in reversed_order:
            if code >= m:
                side = 0
            else:
                if side == 0:
                    first.append(code)
                else:
                    second.append(code)
                side ^= 1

    if odd_vertices:
        process_tour(DUMMY)

    for x in touched:
        while adj[x]:
            if is_used(adj[x][-1]):
                adj[x].pop()
            else:
                process_tour(x)

    adj[DUMMY].clear()
    for e in edges:
        used_edge[e] = 0

    return first, second


stack = [(list(range(m)), Delta, 1)]

while stack:
    edges, d, base = stack.pop()
    if not edges:
        continue

    if d == 1:
        for e in edges:
            answer[e] = base
        continue

    if d & 1:
        matching, rest = extract_covering_matching(edges, d)
        for e in matching:
            answer[e] = base

        k = (d - 1) // 2
        if rest:
            a, b = split_even(rest)
            stack.append((b, k, base + 1 + k))
            stack.append((a, k, base + 1))
    else:
        k = d // 2
        a, b = split_even(edges)
        stack.append((b, k, base + k))
        stack.append((a, k, base))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
nL, nR, m = data[0], data[1], data[2]

U = [0] * m
V = [0] * m
degL = [0] * nL
degR = [0] * nR

pos = 3
for i in range(m):
    u = data[pos] - 1
    v = data[pos + 1] - 1
    pos += 2
    U[i] = u
    V[i] = v
    degL[u] += 1
    degR[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

Delta = max(max(degL), max(degR))
answer = [0] * m

matchL = [-1] * nL
matchR = [-1] * nR
distL = [0] * nL
distR = [0] * nR
seenL = [0] * nL
seenR = [0] * nR
ptrL = [0] * nL
ptrR = [0] * nR
phase_token = 0

pair1 = [-1] * m
pair2 = [-1] * m
visited = [0] * m
visit_token = 0


def build_adjacency(edges):
    adj_l = {}
    adj_r = {}
    for e in edges:
        u = U[e]
        v = V[e]
        if u in adj_l:
            adj_l[u].append(e)
        else:
            adj_l[u] = [e]
        if v in adj_r:
            adj_r[v].append(e)
        else:
            adj_r[v] = [e]
    return adj_l, adj_r


def saturate_left(required, adj_l):
    global phase_token

    while True:
        phase_token += 1
        token = phase_token
        q = deque()

        for u in required:
            if matchL[u] == -1:
                seenL[u] = token
                distL[u] = 0
                ptrL[u] = 0
                q.append(u)

        if not q:
            return

        terminal_found = False

        while q:
            u = q.popleft()
            nd = distL[u] + 1
            for e in adj_l[u]:
                v = V[e]
                old = matchR[v]
                if old == -1:
                    terminal_found = True
                else:
                    u2 = U[old]
                    if seenL[u2] != token:
                        seenL[u2] = token
                        distL[u2] = nd
                        ptrL[u2] = 0
                        q.append(u2)

        if not terminal_found:
            return

        def dfs(u):
            edges_u = adj_l[u]
            i = ptrL[u]
            while i < len(edges_u):
                e = edges_u[i]
                i += 1
                ptrL[u] = i
                v = V[e]
                old = matchR[v]

                if old == -1:
                    matchL[u] = e
                    matchR[v] = e
                    return True

                u2 = U[old]
                if (
                    seenL[u2] == token
                    and distL[u2] == distL[u] + 1
                    and dfs(u2)
                ):
                    matchL[u] = e
                    matchR[v] = e
                    return True

            return False

        progress = False
        for u in required:
            if matchL[u] == -1 and seenL[u] == token and dfs(u):
                progress = True

        if not progress:
            return


def saturate_right(required, required_set, adj_r):
    global phase_token

    while True:
        phase_token += 1
        token = phase_token
        q = deque()

        for v in required:
            if matchR[v] == -1:
                seenR[v] = token
                distR[v] = 0
                ptrR[v] = 0
                q.append(v)

        if not q:
            return

        terminal_found = False

        while q:
            v = q.popleft()
            nd = distR[v] + 1
            for e in adj_r[v]:
                u = U[e]
                old = matchL[u]
                if old == -1:
                    terminal_found = True
                else:
                    v2 = V[old]
                    if v2 not in required_set:
                        terminal_found = True
                    elif seenR[v2] != token:
                        seenR[v2] = token
                        distR[v2] = nd
                        ptrR[v2] = 0
                        q.append(v2)

        if not terminal_found:
            return

        def dfs(v):
            edges_v = adj_r[v]
            i = ptrR[v]
            while i < len(edges_v):
                e = edges_v[i]
                i += 1
                ptrR[v] = i
                u = U[e]
                old = matchL[u]

                if old == -1:
                    matchL[u] = e
                    matchR[v] = e
                    return True

                v2 = V[old]
                if v2 not in required_set:
                    matchR[v2] = -1
                    matchL[u] = e
                    matchR[v] = e
                    return True

                if (
                    seenR[v2] == token
                    and distR[v2] == distR[v] + 1
                    and dfs(v2)
                ):
                    matchL[u] = e
                    matchR[v] = e
                    return True

            return False

        progress = False
        for v in required:
            if matchR[v] == -1 and seenR[v] == token and dfs(v):
                progress = True

        if not progress:
            return


def extract_covering_matching(edges, D):
    adj_l, adj_r = build_adjacency(edges)

    for u in adj_l:
        matchL[u] = -1
    for v in adj_r:
        matchR[v] = -1

    required_l = [u for u, es in adj_l.items() if len(es) == D]
    required_r = [v for v, es in adj_r.items() if len(es) == D]

    if required_l:
        saturate_left(required_l, adj_l)

    if required_r:
        required_r_set = set(required_r)
        saturate_right(required_r, required_r_set, adj_r)

    selected = set()
    for u in adj_l:
        e = matchL[u]
        if e != -1:
            selected.add(e)

    return selected


def split_balanced(edges):
    global visit_token

    adj_l, adj_r = build_adjacency(edges)

    for e in edges:
        pair1[e] = -1
        pair2[e] = -1

    def connect(a, b):
        if pair1[a] == -1:
            pair1[a] = b
        else:
            pair2[a] = b

        if pair1[b] == -1:
            pair1[b] = a
        else:
            pair2[b] = a

    for es in adj_l.values():
        limit = len(es) - 1
        for i in range(0, limit, 2):
            connect(es[i], es[i + 1])

    for es in adj_r.values():
        limit = len(es) - 1
        for i in range(0, limit, 2):
            connect(es[i], es[i + 1])

    visit_token += 1
    token = visit_token
    first = []
    second = []

    def traverse(start):
        prev = -1
        cur = start
        parity = 0

        while cur != -1 and visited[cur] != token:
            visited[cur] = token
            if parity == 0:
                first.append(cur)
            else:
                second.append(cur)
            parity ^= 1

            a = pair1[cur]
            b = pair2[cur]
            if a != -1 and a != prev:
                nxt = a
            elif b != -1 and b != prev:
                nxt = b
            else:
                nxt = -1

            prev, cur = cur, nxt

    for e in edges:
        degree = (1 if pair1[e] != -1 else 0) + (1 if pair2[e] != -1 else 0)
        if degree < 2 and visited[e] != token:
            traverse(e)

    for e in edges:
        if visited[e] != token:
            traverse(e)

    return first, second


def color_graph(edges, D, base):
    if not edges:
        return

    if D == 1:
        for e in edges:
            answer[e] = base
        return

    if D & 1:
        selected = extract_covering_matching(edges, D)

        remaining = []
        for e in edges:
            if e in selected:
                answer[e] = base
            else:
                remaining.append(e)

        half = (D - 1) // 2
        left_edges, right_edges = split_balanced(remaining)
        color_graph(left_edges, half, base + 1)
        color_graph(right_edges, half, base + 1 + half)
    else:
        half = D // 2
        left_edges, right_edges = split_balanced(edges)
        color_graph(left_edges, half, base)
        color_graph(right_edges, half, base + half)


color_graph(list(range(m)), Delta, 1)

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
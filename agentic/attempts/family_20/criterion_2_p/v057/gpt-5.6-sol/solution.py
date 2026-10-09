import sys
from collections import deque
from array import array

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

nA, nB, m = data[0], data[1], data[2]

U = array('i')
V = array('i')
deg_a = [0] * nA
deg_b = [0] * nB

p = 3
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U.append(u)
    V.append(v)
    deg_a[u] += 1
    deg_b[v] += 1

D = max(max(deg_a, default=0), max(deg_b, default=0))

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

answer = [0] * m


def required_matching(edges, bound):
    adj_l = [None] * nA
    adj_r = [None] * nB
    touched_l = []
    touched_r = []

    for eid in edges:
        u = U[eid]
        v = V[eid]
        if adj_l[u] is None:
            adj_l[u] = []
            touched_l.append(u)
        if adj_r[v] is None:
            adj_r[v] = []
            touched_r.append(v)
        adj_l[u].append(eid)
        adj_r[v].append(eid)

    req_l = [u for u in touched_l if len(adj_l[u]) == bound]
    req_r = [v for v in touched_r if len(adj_r[v]) == bound]

    if not req_l and not req_r:
        return set()

    match_l = [-1] * nA
    match_r = [-1] * nB
    match_e = [-1] * nA
    dist_l = [-1] * nA

    # First cover all required left-side vertices.
    while True:
        q = deque()
        for u in req_l:
            if match_l[u] == -1:
                dist_l[u] = 0
                q.append(u)
            else:
                dist_l[u] = -1

        found = False
        while q:
            u = q.popleft()
            nd = dist_l[u] + 1
            for eid in adj_l[u]:
                v = V[eid]
                u2 = match_r[v]
                if u2 == -1:
                    found = True
                elif dist_l[u2] == -1:
                    dist_l[u2] = nd
                    q.append(u2)

        if not found:
            break

        def dfs_left(u):
            for eid in adj_l[u]:
                v = V[eid]
                u2 = match_r[v]
                if u2 == -1 or (
                    dist_l[u2] == dist_l[u] + 1 and dfs_left(u2)
                ):
                    old_v = match_l[u]
                    if old_v != -1 and match_r[old_v] == u:
                        match_r[old_v] = -1
                    match_l[u] = v
                    match_r[v] = u
                    match_e[u] = eid
                    return True
            dist_l[u] = -1
            return False

        changed = False
        for u in req_l:
            if match_l[u] == -1 and dfs_left(u):
                changed = True
        if not changed:
            break

    req_r_flag = bytearray(nB)
    for v in req_r:
        req_r_flag[v] = 1

    # Then cover required right-side vertices without uncovering required left ones.
    dist_r = [-1] * nB

    while True:
        sources = []
        q = deque()
        for v in req_r:
            if match_r[v] == -1:
                dist_r[v] = 0
                q.append(v)
                sources.append(v)
            else:
                dist_r[v] = -1

        if not sources:
            break

        best = -1
        while q:
            v = q.popleft()
            dv = dist_r[v]
            if best != -1 and dv >= best:
                continue

            for eid in adj_r[v]:
                u = U[eid]
                if match_l[u] == v:
                    continue

                old_v = match_l[u]
                if old_v == -1 or not req_r_flag[old_v]:
                    best = dv
                elif dist_r[old_v] == -1:
                    dist_r[old_v] = dv + 1
                    q.append(old_v)

        if best == -1:
            break

        def dfs_right(v):
            dv = dist_r[v]
            for eid in adj_r[v]:
                u = U[eid]
                if match_l[u] == v:
                    continue

                old_v = match_l[u]
                if old_v == -1 or not req_r_flag[old_v]:
                    if dv != best:
                        continue
                    if old_v != -1 and match_r[old_v] == u:
                        match_r[old_v] = -1
                    match_l[u] = v
                    match_r[v] = u
                    match_e[u] = eid
                    return True

                if (
                    dv < best
                    and dist_r[old_v] == dv + 1
                    and dfs_right(old_v)
                ):
                    match_l[u] = v
                    match_r[v] = u
                    match_e[u] = eid
                    return True

            dist_r[v] = -1
            return False

        changed = False
        for v in sources:
            if match_r[v] == -1 and dfs_right(v):
                changed = True

        if not changed:
            break

    return {match_e[u] for u in touched_l if match_e[u] != -1}


def balanced_split(edges):
    total_vertices = nA + nB
    super_vertex = total_vertices
    adj = [None] * (total_vertices + 1)
    touched = []

    eu = array('i')
    ev = array('i')
    original = array('i')

    def add_edge(a, b, eid):
        idx = len(eu)
        eu.append(a)
        ev.append(b)
        original.append(eid)

        if adj[a] is None:
            adj[a] = []
            touched.append(a)
        if adj[b] is None:
            adj[b] = []
            touched.append(b)
        adj[a].append(idx)
        adj[b].append(idx)

    for eid in edges:
        add_edge(U[eid], nA + V[eid], eid)

    odd_vertices = []
    for x in touched:
        if len(adj[x]) & 1:
            odd_vertices.append(x)

    if odd_vertices:
        for x in odd_vertices:
            add_edge(x, super_vertex, -1)

    used = bytearray(len(eu))
    left_part = []
    right_part = []

    def process_component(start):
        stack_v = [start]
        stack_e = [-1]
        tour = []

        while stack_v:
            x = stack_v[-1]
            lst = adj[x]
            while lst and used[lst[-1]]:
                lst.pop()

            if lst:
                le = lst.pop()
                if used[le]:
                    continue
                used[le] = 1
                y = ev[le] if eu[le] == x else eu[le]
                stack_v.append(y)
                stack_e.append(le)
            else:
                stack_v.pop()
                incoming = stack_e.pop()
                if incoming != -1:
                    tour.append(incoming)

        for i, le in enumerate(tour):
            eid = original[le]
            if eid != -1:
                if i & 1:
                    right_part.append(eid)
                else:
                    left_part.append(eid)

    if odd_vertices:
        process_component(super_vertex)

    for x in touched:
        lst = adj[x]
        while lst and used[lst[-1]]:
            lst.pop()
        if lst:
            process_component(x)

    return left_part, right_part


stack = [(list(range(m)), D, 1)]

while stack:
    edges, bound, first_color = stack.pop()

    if not edges:
        continue

    if bound == 1:
        for eid in edges:
            answer[eid] = first_color
        continue

    if bound & 1:
        chosen = required_matching(edges, bound)
        if chosen:
            for eid in chosen:
                answer[eid] = first_color
            remaining = [eid for eid in edges if eid not in chosen]
        else:
            remaining = edges

        half = (bound - 1) // 2
        if half:
            part1, part2 = balanced_split(remaining)
            stack.append((part2, half, first_color + 1 + half))
            stack.append((part1, half, first_color + 1))
    else:
        half = bound // 2
        part1, part2 = balanced_split(edges)
        stack.append((part2, half, first_color + half))
        stack.append((part1, half, first_color))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
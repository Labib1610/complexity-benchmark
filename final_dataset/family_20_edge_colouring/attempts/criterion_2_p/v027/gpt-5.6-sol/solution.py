import sys
from collections import deque
from array import array

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
nL = next(it)
nR = next(it)
m = next(it)

U = array('i', [0]) * m
V = array('i', [0]) * m
for i in range(m):
    U[i] = next(it) - 1
    V[i] = next(it) - 1

answer = array('i', [0]) * m
seen_edge = array('i', [0]) * m
split_token = 0


def maximum_matching(edges, adj_l):
    match_l = {}
    match_r = {}

    while True:
        dist = {}
        q = deque()

        for u in adj_l:
            if u not in match_l:
                dist[u] = 0
                q.append(u)

        found = False
        while q:
            u = q.popleft()
            nd = dist[u] + 1
            for v, _ in adj_l[u]:
                mr = match_r.get(v)
                if mr is None:
                    found = True
                else:
                    u2 = mr[0]
                    if u2 not in dist:
                        dist[u2] = nd
                        q.append(u2)

        if not found:
            break

        ptr = {}

        def dfs(u):
            lst = adj_l[u]
            i = ptr.get(u, 0)
            while i < len(lst):
                v, eid = lst[i]
                ptr[u] = i + 1
                mr = match_r.get(v)
                if mr is None:
                    match_l[u] = (v, eid)
                    match_r[v] = (u, eid)
                    return True
                u2 = mr[0]
                if dist.get(u2) == dist[u] + 1 and dfs(u2):
                    match_l[u] = (v, eid)
                    match_r[v] = (u, eid)
                    return True
                i += 1
            dist[u] = -1
            return False

        augmented = False
        for u in adj_l:
            if u not in match_l and dfs(u):
                augmented = True
        if not augmented:
            break

    return match_l, match_r


def cover_critical_left(critical, degree, max_degree, adj_l, match_l, match_r):
    for root in critical:
        if root in match_l:
            continue

        parent = {}
        visited = {root}
        stack = [root]
        final = None
        displaced = None

        while stack and final is None:
            u = stack.pop()
            for v, eid in adj_l[u]:
                mr = match_r.get(v)
                if mr is None:
                    final = (u, v, eid)
                    displaced = None
                    break

                u2 = mr[0]
                if degree[u2] < max_degree:
                    final = (u, v, eid)
                    displaced = u2
                    break

                if u2 not in visited:
                    visited.add(u2)
                    parent[u2] = (u, v, eid)
                    stack.append(u2)

        if final is None:
            continue

        transitions = [final]
        cur = final[0]
        while cur != root:
            p, v, eid = parent[cur]
            transitions.append((p, v, eid))
            cur = p
        transitions.reverse()

        if displaced is not None:
            match_l.pop(displaced, None)

        for u, v, eid in transitions:
            match_l[u] = (v, eid)
            match_r[v] = (u, eid)


def cover_critical_right(critical, degree, max_degree, adj_r, match_l, match_r):
    for root in critical:
        if root in match_r:
            continue

        parent = {}
        visited = {root}
        stack = [root]
        final = None
        displaced = None

        while stack and final is None:
            v = stack.pop()
            for u, eid in adj_r[v]:
                ml = match_l.get(u)
                if ml is None:
                    final = (v, u, eid)
                    displaced = None
                    break

                v2 = ml[0]
                if degree[v2] < max_degree:
                    final = (v, u, eid)
                    displaced = v2
                    break

                if v2 not in visited:
                    visited.add(v2)
                    parent[v2] = (v, u, eid)
                    stack.append(v2)

        if final is None:
            continue

        transitions = [final]
        cur = final[0]
        while cur != root:
            p, u, eid = parent[cur]
            transitions.append((p, u, eid))
            cur = p
        transitions.reverse()

        if displaced is not None:
            match_r.pop(displaced, None)

        for v, u, eid in transitions:
            match_r[v] = (u, eid)
            match_l[u] = (v, eid)


def extract_matching(edges, deg_l, deg_r, d):
    adj_l = {}
    adj_r = {}

    for eid in edges:
        u = U[eid]
        v = V[eid]
        adj_l.setdefault(u, []).append((v, eid))
        adj_r.setdefault(v, []).append((u, eid))

    match_l, match_r = maximum_matching(edges, adj_l)

    critical_l = [u for u, x in deg_l.items() if x == d]
    critical_r = [v for v, x in deg_r.items() if x == d]

    cover_critical_left(
        critical_l, deg_l, d, adj_l, match_l, match_r
    )
    cover_critical_right(
        critical_r, deg_r, d, adj_r, match_l, match_r
    )

    return {eid for _, eid in match_l.values()}


def balanced_split(edges, deg_l, deg_r):
    global split_token
    split_token += 1
    token = split_token

    dl = nL + nR
    dr = dl + 1

    adjacency = {}
    dummy_u = []
    dummy_v = []

    for eid in edges:
        a = U[eid]
        b = nL + V[eid]
        adjacency.setdefault(a, []).append(eid)
        adjacency.setdefault(b, []).append(eid)

    def add_dummy(a, b):
        idx = len(dummy_u)
        ref = -idx - 1
        dummy_u.append(a)
        dummy_v.append(b)
        adjacency.setdefault(a, []).append(ref)
        adjacency.setdefault(b, []).append(ref)

    odd_l = [u for u, x in deg_l.items() if x & 1]
    odd_r = [v for v, x in deg_r.items() if x & 1]

    for u in odd_l:
        add_dummy(u, dr)
    for v in odd_r:
        add_dummy(dl, nL + v)
    if len(odd_l) & 1:
        add_dummy(dl, dr)

    dummy_used = bytearray(len(dummy_u))
    first = []
    second = []

    def is_used(ref):
        if ref >= 0:
            return seen_edge[ref] == token
        return dummy_used[-ref - 1] != 0

    def mark_used(ref):
        if ref >= 0:
            seen_edge[ref] = token
        else:
            dummy_used[-ref - 1] = 1

    def other(ref, node):
        if ref >= 0:
            a = U[ref]
            b = nL + V[ref]
        else:
            idx = -ref - 1
            a = dummy_u[idx]
            b = dummy_v[idx]
        return b if node == a else a

    for start in list(adjacency.keys()):
        stack_nodes = [start]
        stack_edges = []
        circuit = []

        while stack_nodes:
            node = stack_nodes[-1]
            lst = adjacency[node]
            while lst and is_used(lst[-1]):
                lst.pop()

            if lst:
                ref = lst.pop()
                if is_used(ref):
                    continue
                mark_used(ref)
                nxt = other(ref, node)
                stack_nodes.append(nxt)
                stack_edges.append(ref)
            else:
                stack_nodes.pop()
                if stack_edges:
                    circuit.append(stack_edges.pop())

        for i, ref in enumerate(circuit):
            if ref >= 0:
                if i & 1:
                    second.append(ref)
                else:
                    first.append(ref)

    return first, second


def color_edges(edges, start_color):
    if not edges:
        return

    deg_l = {}
    deg_r = {}
    d = 0

    for eid in edges:
        u = U[eid]
        v = V[eid]

        x = deg_l.get(u, 0) + 1
        deg_l[u] = x
        if x > d:
            d = x

        x = deg_r.get(v, 0) + 1
        deg_r[v] = x
        if x > d:
            d = x

    if d == 1:
        for eid in edges:
            answer[eid] = start_color
        return

    if d & 1:
        matching = extract_matching(edges, deg_l, deg_r, d)
        remaining = []
        matching_color = start_color + d - 1

        for eid in edges:
            if eid in matching:
                answer[eid] = matching_color
            else:
                remaining.append(eid)

        color_edges(remaining, start_color)
    else:
        first, second = balanced_split(edges, deg_l, deg_r)
        half = d // 2
        color_edges(first, start_color)
        color_edges(second, start_color + half)


if m:
    color_edges(list(range(m)), 1)

out = ["YES"]
out.append(" ".join(map(str, answer)))
sys.stdout.write("\n".join(out))
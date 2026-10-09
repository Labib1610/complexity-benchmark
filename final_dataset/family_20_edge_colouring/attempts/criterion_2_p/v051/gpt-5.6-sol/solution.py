import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
NS, NG, M = data[0], data[1], data[2]

U = [0] * M
V = [0] * M
deg_u = [0] * NS
deg_v = [0] * NG

p = 3
for i in range(M):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[i] = u
    V[i] = v
    deg_u[u] += 1
    deg_v[v] += 1

if M == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

D = max(max(deg_u), max(deg_v))
answer = [0] * M

match_l = [-1] * NS
match_r = [-1] * NG
match_edge = [-1] * NS
seen_l = [0] * NS
seen_r = [0] * NG
seen_token = 0

used_mark = [0] * M
mark_token = 0


def covering_matching(edges, bound):
    global seen_token

    adj_l = {}
    adj_r = {}

    for e in edges:
        l = U[e]
        r = V[e]
        if l in adj_l:
            adj_l[l].append(e)
        else:
            adj_l[l] = [e]
        if r in adj_r:
            adj_r[r].append(e)
        else:
            adj_r[r] = [e]

    left_vertices = list(adj_l.keys())
    right_vertices = list(adj_r.keys())

    for l in left_vertices:
        match_l[l] = -1
        match_edge[l] = -1
    for r in right_vertices:
        match_r[r] = -1

    required_l = [l for l in left_vertices if len(adj_l[l]) == bound]
    required_r = [r for r in right_vertices if len(adj_r[r]) == bound]
    required_r_set = set(required_r)

    dist = {}
    ptr = {}

    def bfs():
        q = deque()
        found = False
        dist.clear()

        for l in required_l:
            if match_l[l] == -1:
                dist[l] = 0
                q.append(l)

        while q:
            l = q.popleft()
            nd = dist[l] + 1
            for e in adj_l[l]:
                r = V[e]
                l2 = match_r[r]
                if l2 == -1:
                    found = True
                elif l2 not in dist:
                    dist[l2] = nd
                    q.append(l2)
        return found

    def dfs_hk(l):
        edges_l = adj_l[l]
        i = ptr.get(l, 0)

        while i < len(edges_l):
            e = edges_l[i]
            i += 1
            ptr[l] = i
            r = V[e]
            l2 = match_r[r]

            if l2 == -1 or (
                dist.get(l2, -1) == dist[l] + 1 and dfs_hk(l2)
            ):
                match_l[l] = r
                match_r[r] = l
                match_edge[l] = e
                return True

        dist[l] = -1
        return False

    while bfs():
        ptr.clear()
        for l in required_l:
            if match_l[l] == -1:
                dfs_hk(l)

    def relocate_right(r, token):
        seen_r[r] = token

        for e in adj_r[r]:
            l = U[e]
            if seen_l[l] == token:
                continue
            seen_l[l] = token

            old_r = match_l[l]
            if old_r == -1:
                match_l[l] = r
                match_r[r] = l
                match_edge[l] = e
                return True

            if old_r not in required_r_set:
                match_r[old_r] = -1
                match_l[l] = r
                match_r[r] = l
                match_edge[l] = e
                return True

            if seen_r[old_r] != token and relocate_right(old_r, token):
                match_l[l] = r
                match_r[r] = l
                match_edge[l] = e
                return True

        return False

    for r in required_r:
        if match_r[r] == -1:
            seen_token += 1
            relocate_right(r, seen_token)

    return [match_edge[l] for l in left_vertices if match_l[l] != -1]


def balanced_split(edges, excluded=None):
    global mark_token

    mark_token += 1
    token = mark_token

    if excluded:
        for e in excluded:
            used_mark[e] = token

    adjacency = {}

    for e in edges:
        if used_mark[e] == token:
            continue
        a = U[e]
        b = NS + V[e]

        if a in adjacency:
            adjacency[a].append(e)
        else:
            adjacency[a] = [e]

        if b in adjacency:
            adjacency[b].append(e)
        else:
            adjacency[b] = [e]

    if not adjacency:
        return [], []

    position = {x: len(lst) - 1 for x, lst in adjacency.items()}
    first = []
    second = []

    def traverse(start):
        stack_v = [start]
        stack_e = []
        trail = []

        while stack_v:
            x = stack_v[-1]
            lst = adjacency[x]
            i = position[x]

            while i >= 0 and used_mark[lst[i]] == token:
                i -= 1
            position[x] = i

            if i < 0:
                stack_v.pop()
                if stack_e:
                    trail.append(stack_e.pop())
                continue

            e = lst[i]
            position[x] = i - 1
            if used_mark[e] == token:
                continue

            used_mark[e] = token
            y = NS + V[e] if x < NS else U[e]
            stack_v.append(y)
            stack_e.append(e)

        for i, e in enumerate(trail):
            if i & 1:
                second.append(e)
            else:
                first.append(e)

    for x, lst in adjacency.items():
        if len(lst) & 1:
            i = position[x]
            while i >= 0 and used_mark[lst[i]] == token:
                i -= 1
            position[x] = i
            if i >= 0:
                traverse(x)

    for x, lst in adjacency.items():
        i = position[x]
        while i >= 0 and used_mark[lst[i]] == token:
            i -= 1
        position[x] = i
        if i >= 0:
            traverse(x)

    return first, second


tasks = [(list(range(M)), D, 1)]

while tasks:
    edges, bound, offset = tasks.pop()

    if not edges:
        continue

    if bound == 1:
        for e in edges:
            answer[e] = offset
        continue

    if bound & 1:
        matching = covering_matching(edges, bound)
        for e in matching:
            answer[e] = offset

        half = bound // 2
        a, b = balanced_split(edges, matching)

        if b:
            tasks.append((b, half, offset + 1 + half))
        if a:
            tasks.append((a, half, offset + 1))
    else:
        half = bound // 2
        a, b = balanced_split(edges)

        if b:
            tasks.append((b, half, offset + half))
        if a:
            tasks.append((a, half, offset))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")
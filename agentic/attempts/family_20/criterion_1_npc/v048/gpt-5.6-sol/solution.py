import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    raise SystemExit

n, m = data[0], data[1]
U = [0] * m
V = [0] * m
adj = [[] for _ in range(n)]

p = 2
for e in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[e] = u
    V[e] = v
    adj[u].append(e)
    adj[v].append(e)

active_v = [True] * n
active_e = [True] * m
reductions = []


def other(e, x):
    return V[e] if U[e] == x else U[e]


def edges_between(a, b):
    result = []
    for e in adj[a]:
        if active_e[e] and other(e, a) == b:
            result.append(e)
    return result


def find_triangle():
    for a in range(len(adj)):
        if not active_v[a]:
            continue
        neighbors = []
        seen = set()
        for e in adj[a]:
            if not active_e[e]:
                continue
            b = other(e, a)
            if active_v[b] and b not in seen:
                seen.add(b)
                neighbors.append(b)

        ln = len(neighbors)
        for i in range(ln):
            b = neighbors[i]
            for j in range(i + 1, ln):
                c = neighbors[j]
                ab = edges_between(a, b)
                ac = edges_between(a, c)
                bc = edges_between(b, c)
                if len(ab) != 1 or len(ac) != 1 or len(bc) != 1:
                    continue

                internal = {ab[0], ac[0], bc[0]}
                ext_a = [e for e in adj[a] if active_e[e] and e not in internal]
                ext_b = [e for e in adj[b] if active_e[e] and e not in internal]
                ext_c = [e for e in adj[c] if active_e[e] and e not in internal]
                if len(ext_a) == len(ext_b) == len(ext_c) == 1:
                    return a, b, c, ab[0], bc[0], ac[0], ext_a[0], ext_b[0], ext_c[0]
    return None


while True:
    tri = find_triangle()
    if tri is None:
        break

    a, b, c, eab, ebc, eac, ea, eb, ec = tri
    w = len(adj)
    adj.append([ea, eb, ec])
    active_v.append(True)

    for old, e in ((a, ea), (b, eb), (c, ec)):
        if U[e] == old:
            U[e] = w
        else:
            V[e] = w

    active_v[a] = active_v[b] = active_v[c] = False
    active_e[eab] = active_e[ebc] = active_e[eac] = False
    reductions.append((eab, ebc, eac, ea, eb, ec))

total_vertices = len(adj)
visited = [False] * total_vertices
components = []

for s in range(total_vertices):
    if not active_v[s] or visited[s]:
        continue
    q = [s]
    visited[s] = True
    verts = []
    edge_set = set()
    while q:
        x = q.pop()
        verts.append(x)
        for e in adj[x]:
            if not active_e[e]:
                continue
            edge_set.add(e)
            y = other(e, x)
            if not visited[y]:
                visited[y] = True
                q.append(y)
    components.append((verts, list(edge_set)))

answer = [0] * m


def bipartition(verts):
    side = {}
    for start in verts:
        if start in side:
            continue
        side[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            sx = side[x]
            for e in adj[x]:
                if not active_e[e]:
                    continue
                y = other(e, x)
                if y not in side:
                    side[y] = sx ^ 1
                    q.append(y)
                elif side[y] == sx:
                    return None
    return side


def color_bipartite(verts, edges, side):
    left = [x for x in verts if side[x] == 0]
    match_r = {}
    match_l = {}
    seen = {}
    token = 0

    def augment(x):
        nonlocal token
        for e in adj[x]:
            if not active_e[e]:
                continue
            y = other(e, x)
            if seen.get(y, 0) == token:
                continue
            seen[y] = token
            old = match_r.get(y)
            if old is None:
                match_r[y] = e
                match_l[x] = e
                return True
            old_left = other(old, y)
            if augment(old_left):
                match_r[y] = e
                match_l[x] = e
                return True
        return False

    for x in left:
        token += 1
        if not augment(x):
            return False

    matching = set(match_l.values())
    for e in matching:
        answer[e] = 1

    for start_e in edges:
        if start_e in matching or answer[start_e] != 0:
            continue
        start_vertex = U[start_e]
        cur_vertex = start_vertex
        cur_edge = start_e
        color = 2

        while answer[cur_edge] == 0:
            answer[cur_edge] = color
            nxt_vertex = other(cur_edge, cur_vertex)
            nxt_edge = None
            for e in adj[nxt_vertex]:
                if active_e[e] and e not in matching and e != cur_edge:
                    nxt_edge = e
                    break
            if nxt_edge is None:
                return False
            cur_vertex = nxt_vertex
            cur_edge = nxt_edge
            color = 5 - color

    return True


PERMS = tuple(permutations((1, 2, 4)))
domains = [7] * m


def solve_component_csp(verts, edges):
    trail = []

    def rollback(mark):
        while len(trail) > mark:
            e, old = trail.pop()
            domains[e] = old

    def restrict(e, mask, queue):
        new_mask = domains[e] & mask
        if new_mask == 0:
            return False
        if new_mask != domains[e]:
            trail.append((e, domains[e]))
            domains[e] = new_mask
            queue.append(U[e])
            queue.append(V[e])
        return True

    def feasible_options(x):
        es = adj[x]
        d0, d1, d2 = domains[es[0]], domains[es[1]], domains[es[2]]
        return [p for p in PERMS
                if (d0 & p[0]) and (d1 & p[1]) and (d2 & p[2])]

    def propagate(initial):
        queue = deque(initial)
        while queue:
            x = queue.popleft()
            if not active_v[x]:
                continue
            es = adj[x]
            opts = feasible_options(x)
            if not opts:
                return False

            supports = [0, 0, 0]
            for op in opts:
                supports[0] |= op[0]
                supports[1] |= op[1]
                supports[2] |= op[2]

            for i in range(3):
                if not restrict(es[i], supports[i], queue):
                    return False
        return True

    root = verts[0]
    root_edges = adj[root]
    for i, e in enumerate(root_edges):
        domains[e] = 1 << i

    if not propagate(verts):
        return False

    def dfs():
        chosen = None
        chosen_opts = None
        best_count = 7
        best_score = -1

        for x in verts:
            opts = feasible_options(x)
            cnt = len(opts)
            if cnt <= 1:
                continue

            score = 0
            for e in adj[x]:
                y = other(e, x)
                for f in adj[y]:
                    score += 3 - domains[f].bit_count()

            if cnt < best_count or (cnt == best_count and score > best_score):
                best_count = cnt
                best_score = score
                chosen = x
                chosen_opts = opts

        if chosen is None:
            return True

        es = adj[chosen]
        for op in chosen_opts:
            mark = len(trail)
            queue = deque()
            ok = True
            for i in range(3):
                if not restrict(es[i], op[i], queue):
                    ok = False
                    break
            if ok and propagate(queue) and dfs():
                return True
            rollback(mark)
        return False

    if not dfs():
        return False

    for e in edges:
        d = domains[e]
        if d == 1:
            answer[e] = 1
        elif d == 2:
            answer[e] = 2
        elif d == 4:
            answer[e] = 3
        else:
            return False
    return True


for verts, edges in components:
    side = bipartition(verts)
    if side is not None:
        if not color_bipartite(verts, edges, side):
            print("NO")
            raise SystemExit
    else:
        if not solve_component_csp(verts, edges):
            print("NO")
            raise SystemExit

for eab, ebc, eac, ea, eb, ec in reversed(reductions):
    answer[eab] = answer[ec]
    answer[ebc] = answer[ea]
    answer[eac] = answer[eb]

for x in answer:
    if x not in (1, 2, 3):
        print("NO")
        raise SystemExit

out = ["YES", " ".join(map(str, answer))]
sys.stdout.write("\n".join(out))
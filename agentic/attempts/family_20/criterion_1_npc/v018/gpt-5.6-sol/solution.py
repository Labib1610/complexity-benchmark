import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)

data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit()

n, m = data[0], data[1]
edges = []
adj = [[] for _ in range(n)]
idx = 2

valid = (m * 2 == 3 * n and len(data) == 2 + 2 * m)

for eid in range(m):
    u = data[idx] - 1
    v = data[idx + 1] - 1
    idx += 2
    if not (0 <= u < n and 0 <= v < n and u != v):
        valid = False
    edges.append((u, v))
    if 0 <= u < n and 0 <= v < n:
        adj[u].append(eid)
        adj[v].append(eid)

if not valid or any(len(adj[v]) != 3 for v in range(n)):
    print("NO")
    sys.exit()

def other(eid, v):
    a, b = edges[eid]
    return b if a == v else a

# A cubic graph with a bridge cannot have a 3-edge-coloring.
tin = [-1] * n
low = [0] * n
timer = 0
has_bridge = False

def bridge_dfs(v, parent_edge):
    global timer, has_bridge
    tin[v] = low[v] = timer
    timer += 1
    for eid in adj[v]:
        if eid == parent_edge:
            continue
        to = other(eid, v)
        if tin[to] == -1:
            bridge_dfs(to, eid)
            low[v] = min(low[v], low[to])
            if low[to] > tin[v]:
                has_bridge = True
        else:
            low[v] = min(low[v], tin[to])

for s in range(n):
    if tin[s] == -1:
        bridge_dfs(s, -1)

if has_bridge:
    print("NO")
    sys.exit()

# Find connected components and bipartitions.
side = [-1] * n
comp = [-1] * n
components = []
component_bip = []

for start in range(n):
    if comp[start] != -1:
        continue
    cid = len(components)
    vertices = []
    bip = True
    q = deque([start])
    comp[start] = cid
    side[start] = 0

    while q:
        v = q.popleft()
        vertices.append(v)
        for eid in adj[v]:
            to = other(eid, v)
            if comp[to] == -1:
                comp[to] = cid
                side[to] = side[v] ^ 1
                q.append(to)
            elif side[to] == side[v]:
                bip = False

    components.append(vertices)
    component_bip.append(bip)

answer = [-1] * m

# Color every bipartite component using one perfect matching and alternating cycles.
left_vertices = [
    v for v in range(n)
    if component_bip[comp[v]] and side[v] == 0
]

pair_right = [-1] * n
match_edge_left = [-1] * n

def augment(v, seen):
    for eid in adj[v]:
        to = other(eid, v)
        if seen[to]:
            continue
        seen[to] = True
        old_left = pair_right[to]
        if old_left == -1 or augment(old_left, seen):
            pair_right[to] = v
            match_edge_left[v] = eid
            return True
    return False

for v in left_vertices:
    seen = [False] * n
    if not augment(v, seen):
        print("NO")
        sys.exit()

for v in left_vertices:
    answer[match_edge_left[v]] = 0

residual = [[] for _ in range(n)]
for eid, (u, v) in enumerate(edges):
    if component_bip[comp[u]] and answer[eid] == -1:
        residual[u].append(eid)
        residual[v].append(eid)

for eid, (u, v) in enumerate(edges):
    if not component_bip[comp[u]] or answer[eid] != -1:
        continue

    answer[eid] = 1
    q = deque([eid])
    ok = True

    while q and ok:
        cur = q.popleft()
        a, b = edges[cur]
        wanted = 3 - answer[cur]

        for vertex in (a, b):
            for nxt in residual[vertex]:
                if nxt == cur:
                    continue
                if answer[nxt] == -1:
                    answer[nxt] = wanted
                    q.append(nxt)
                elif answer[nxt] != wanted:
                    ok = False
                    break
            if not ok:
                break

    if not ok:
        print("NO")
        sys.exit()

# General exact CSP solver for non-bipartite components.
perms = list(permutations(range(3)))
state_mask = [[[0] * 3 for _ in range(3)]][0]
state_mask = [[0] * 3 for _ in range(3)]

for state, p in enumerate(perms):
    for pos in range(3):
        state_mask[pos][p[pos]] |= 1 << state

edge_pos_u = [0] * m
edge_pos_v = [0] * m

for v in range(n):
    for pos, eid in enumerate(adj[v]):
        u, w = edges[eid]
        if u == v:
            edge_pos_u[eid] = pos
        else:
            edge_pos_v[eid] = pos

domains = [0b111111] * n

# Constrain already colored bipartite components.
for eid, color in enumerate(answer):
    if color == -1:
        continue
    u, v = edges[eid]
    domains[u] &= state_mask[edge_pos_u[eid]][color]
    domains[v] &= state_mask[edge_pos_v[eid]][color]

# Remove global color symmetry independently in each unresolved component.
identity_state = perms.index((0, 1, 2))
for cid, vertices in enumerate(components):
    if not component_bip[cid]:
        domains[vertices[0]] = 1 << identity_state

trail = []

def propagate(initial_edges):
    q = deque(initial_edges)

    while q:
        eid = q.popleft()
        u, v = edges[eid]
        du = domains[u]
        dv = domains[v]
        pu = edge_pos_u[eid]
        pv = edge_pos_v[eid]

        allowed = 0
        for c in range(3):
            if (du & state_mask[pu][c]) and (dv & state_mask[pv][c]):
                allowed |= 1 << c

        if allowed == 0:
            return False

        support_u = 0
        support_v = 0
        for c in range(3):
            if allowed & (1 << c):
                support_u |= state_mask[pu][c]
                support_v |= state_mask[pv][c]

        ndu = du & support_u
        ndv = dv & support_v

        if ndu == 0 or ndv == 0:
            return False

        if ndu != du:
            trail.append((u, du))
            domains[u] = ndu
            q.extend(adj[u])

        if ndv != dv:
            trail.append((v, dv))
            domains[v] = ndv
            q.extend(adj[v])

    return True

if not propagate(range(m)):
    print("NO")
    sys.exit()

def edge_allowed_colors(eid):
    u, v = edges[eid]
    du = domains[u]
    dv = domains[v]
    pu = edge_pos_u[eid]
    pv = edge_pos_v[eid]
    result = 0
    for c in range(3):
        if (du & state_mask[pu][c]) and (dv & state_mask[pv][c]):
            result |= 1 << c
    return result

def solve():
    chosen_edge = -1
    chosen_colors = 0
    best_count = 4
    best_worst = 10**9

    for eid in range(m):
        if answer[eid] != -1:
            continue

        colors = edge_allowed_colors(eid)
        count = colors.bit_count()

        if count == 0:
            return False
        if count == 1:
            continue

        u, v = edges[eid]
        pu = edge_pos_u[eid]
        pv = edge_pos_v[eid]
        worst = 0

        for c in range(3):
            if colors & (1 << c):
                su = (domains[u] & state_mask[pu][c]).bit_count()
                sv = (domains[v] & state_mask[pv][c]).bit_count()
                worst = max(worst, su * sv)

        if count < best_count or (count == best_count and worst < best_worst):
            best_count = count
            best_worst = worst
            chosen_edge = eid
            chosen_colors = colors

    if chosen_edge == -1:
        return True

    u, v = edges[chosen_edge]
    pu = edge_pos_u[chosen_edge]
    pv = edge_pos_v[chosen_edge]

    options = []
    for c in range(3):
        if chosen_colors & (1 << c):
            score = (
                (domains[u] & state_mask[pu][c]).bit_count()
                * (domains[v] & state_mask[pv][c]).bit_count()
            )
            options.append((score, c))
    options.sort()

    for _, color in options:
        mark = len(trail)

        ndu = domains[u] & state_mask[pu][color]
        ndv = domains[v] & state_mask[pv][color]

        if ndu and ndv:
            if ndu != domains[u]:
                trail.append((u, domains[u]))
                domains[u] = ndu
            if ndv != domains[v]:
                trail.append((v, domains[v]))
                domains[v] = ndv

            if propagate(adj[u] + adj[v]) and solve():
                return True

        while len(trail) > mark:
            vertex, old_domain = trail.pop()
            domains[vertex] = old_domain

    return False

if not solve():
    print("NO")
    sys.exit()

for eid in range(m):
    if answer[eid] != -1:
        continue
    colors = edge_allowed_colors(eid)
    if colors == 0 or colors & (colors - 1):
        print("NO")
        sys.exit()
    answer[eid] = colors.bit_length() - 1

print("YES")
print(*[c + 1 for c in answer])
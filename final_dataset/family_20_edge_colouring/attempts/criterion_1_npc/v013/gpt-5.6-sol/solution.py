import sys
from collections import deque

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)

U = [0] * m
V = [0] * m
inc = [[] for _ in range(n)]

for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    U[eid] = u
    V[eid] = v
    inc[u].append(eid)
    inc[v].append(eid)

# A bridge in a cubic graph makes a 3-edge-coloring impossible.
tin = [-1] * n
low = [0] * n
timer = 0
has_bridge = False

def bridge_dfs(x, parent_edge):
    global timer, has_bridge
    tin[x] = low[x] = timer
    timer += 1

    for eid in inc[x]:
        if eid == parent_edge:
            continue
        y = V[eid] if U[eid] == x else U[eid]
        if tin[y] == -1:
            bridge_dfs(y, eid)
            low[x] = min(low[x], low[y])
            if low[y] > tin[x]:
                has_bridge = True
        else:
            low[x] = min(low[x], tin[y])

for s in range(n):
    if tin[s] == -1:
        bridge_dfs(s, -1)

if has_bridge:
    print("NO")
    sys.exit()

# Test bipartiteness and record connected-component roots.
side = [-1] * n
component_roots = []
is_bipartite = True

for s in range(n):
    if side[s] != -1:
        continue
    component_roots.append(s)
    side[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for eid in inc[x]:
            y = V[eid] if U[eid] == x else U[eid]
            if side[y] == -1:
                side[y] = side[x] ^ 1
                q.append(y)
            elif side[y] == side[x]:
                is_bipartite = False

# Cubic bipartite graphs can be colored directly:
# find one perfect matching, then alternate on the remaining cycles.
if is_bipartite:
    left = [x for x in range(n) if side[x] == 0]
    pair_u = [-1] * n
    pair_v = [-1] * n
    pair_edge = [-1] * n
    dist = [-1] * n

    def hk_bfs():
        q = deque()
        found = False
        for x in left:
            if pair_u[x] == -1:
                dist[x] = 0
                q.append(x)
            else:
                dist[x] = -1

        while q:
            x = q.popleft()
            for eid in inc[x]:
                y = V[eid] if U[eid] == x else U[eid]
                px = pair_v[y]
                if px == -1:
                    found = True
                elif dist[px] == -1:
                    dist[px] = dist[x] + 1
                    q.append(px)
        return found

    def hk_dfs(x):
        for eid in inc[x]:
            y = V[eid] if U[eid] == x else U[eid]
            px = pair_v[y]
            if px == -1 or (dist[px] == dist[x] + 1 and hk_dfs(px)):
                pair_u[x] = y
                pair_v[y] = x
                pair_edge[x] = eid
                return True
        dist[x] = -1
        return False

    matched = 0
    while hk_bfs():
        for x in left:
            if pair_u[x] == -1 and hk_dfs(x):
                matched += 1

    if matched != len(left):
        print("NO")
        sys.exit()

    color = [-1] * m
    for x in left:
        color[pair_edge[x]] = 0

    ok = True
    for start in range(m):
        if color[start] != -1:
            continue

        color[start] = 1
        q = deque([U[start], V[start]])

        while q and ok:
            x = q.popleft()
            cycle_edges = [eid for eid in inc[x] if color[eid] != 0]

            if len(cycle_edges) != 2:
                ok = False
                break

            a, b = cycle_edges
            ca, cb = color[a], color[b]

            if ca != -1 and cb != -1:
                if ca == cb:
                    ok = False
            elif ca != -1:
                color[b] = 3 - ca
                q.append(V[b] if U[b] == x else U[b])
            elif cb != -1:
                color[a] = 3 - cb
                q.append(V[a] if U[a] == x else U[a])

    if ok:
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")
    sys.exit()

# General cubic graph: constraint propagation with exact backtracking.
FULL = 0b111
color = [-1] * m
used = [0] * n
remaining = [3] * n
trail = []

def rollback(mark):
    while len(trail) > mark:
        eid = trail.pop()
        c = color[eid]
        bit = 1 << c
        color[eid] = -1
        used[U[eid]] ^= bit
        used[V[eid]] ^= bit
        remaining[U[eid]] += 1
        remaining[V[eid]] += 1

def propagate(first_edge, first_color):
    queue = deque([(first_edge, first_color)])

    while queue:
        eid, c = queue.popleft()

        if color[eid] != -1:
            if color[eid] != c:
                return False
            continue

        u = U[eid]
        v = V[eid]
        bit = 1 << c

        if (used[u] & bit) or (used[v] & bit):
            return False

        color[eid] = c
        trail.append(eid)
        used[u] |= bit
        used[v] |= bit
        remaining[u] -= 1
        remaining[v] -= 1

        for x in (u, v):
            for ne in inc[x]:
                if color[ne] != -1:
                    continue
                a = U[ne]
                b = V[ne]
                domain = FULL & ~used[a] & ~used[b]
                if domain == 0:
                    return False
                if domain & (domain - 1) == 0:
                    queue.append((ne, domain.bit_length() - 1))

    return True

# Break color-permutation symmetry independently in each component.
initial_ok = True
for root in component_roots:
    root_edges = inc[root]
    for c, eid in enumerate(root_edges):
        if not propagate(eid, c):
            initial_ok = False
            break
    if not initial_ok:
        break

if not initial_ok:
    print("NO")
    sys.exit()

def solve():
    best_edge = -1
    best_domain = 0
    best_size = 4
    best_score = -1

    for eid in range(m):
        if color[eid] != -1:
            continue

        u = U[eid]
        v = V[eid]
        domain = FULL & ~used[u] & ~used[v]
        size = domain.bit_count()

        if size == 0:
            return False

        score = used[u].bit_count() + used[v].bit_count()
        if size < best_size or (size == best_size and score > best_score):
            best_size = size
            best_score = score
            best_edge = eid
            best_domain = domain
            if size == 1:
                break

    if best_edge == -1:
        return True

    domain = best_domain
    while domain:
        bit = domain & -domain
        domain -= bit
        c = bit.bit_length() - 1
        mark = len(trail)

        if propagate(best_edge, c) and solve():
            return True

        rollback(mark)

    return False

if solve():
    print("YES")
    print(" ".join(str(c + 1) for c in color))
else:
    print("NO")
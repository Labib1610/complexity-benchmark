import sys
from collections import deque

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit()

n, m = data[0], data[1]
edges = []
adj = [[] for _ in range(n)]

p = 2
valid = (m * 2 == 3 * n and len(data) == 2 + 2 * m)
for eid in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if not (0 <= u < v < n):
        valid = False
    edges.append((u, v))
    if 0 <= u < n and 0 <= v < n:
        adj[u].append(eid)
        adj[v].append(eid)

if not valid or any(len(adj[v]) != 3 for v in range(n)):
    print("NO")
    sys.exit()

# A cubic graph containing a bridge cannot have a proper 3-edge-coloring.
tin = [-1] * n
low = [0] * n
timer = 0
has_bridge = False

def bridge_dfs(u, parent_eid):
    global timer, has_bridge
    tin[u] = low[u] = timer
    timer += 1

    for eid in adj[u]:
        if eid == parent_eid:
            continue
        a, b = edges[eid]
        v = b if a == u else a
        if tin[v] == -1:
            bridge_dfs(v, eid)
            low[u] = min(low[u], low[v])
            if low[v] > tin[u]:
                has_bridge = True
        else:
            low[u] = min(low[u], tin[v])

for start in range(n):
    if tin[start] == -1:
        bridge_dfs(start, -1)

if has_bridge:
    print("NO")
    sys.exit()

# Find connected components and their bipartitions.
side = [-1] * n
components = []

for start in range(n):
    if side[start] != -1:
        continue
    q = deque([start])
    side[start] = 0
    vertices = []
    component_edges = []
    is_bipartite = True

    while q:
        u = q.popleft()
        vertices.append(u)
        for eid in adj[u]:
            a, b = edges[eid]
            v = b if a == u else a
            if u < v:
                component_edges.append(eid)
            if side[v] == -1:
                side[v] = side[u] ^ 1
                q.append(v)
            elif side[v] == side[u]:
                is_bipartite = False

    components.append((vertices, component_edges, is_bipartite))

color = [0] * m
used = [0] * n
FULL = (1 << 1) | (1 << 2) | (1 << 3)


def color_bipartite_component(vertices, component_edges):
    left = [u for u in vertices if side[u] == 0]
    mate_u = [-1] * n       # Matching edge incident to a left vertex
    mate_v = [-1] * n       # Matched left vertex for a right vertex
    dist = [-1] * n

    def bfs():
        q = deque()
        found = False
        for u in left:
            if mate_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1

        while q:
            u = q.popleft()
            for eid in adj[u]:
                a, b = edges[eid]
                v = b if a == u else a
                pu = mate_v[v]
                if pu == -1:
                    found = True
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return found

    def dfs(u):
        for eid in adj[u]:
            a, b = edges[eid]
            v = b if a == u else a
            pu = mate_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                mate_u[u] = eid
                mate_v[v] = u
                return True
        dist[u] = -1
        return False

    matched = 0
    while bfs():
        for u in left:
            if mate_u[u] == -1 and dfs(u):
                matched += 1

    if matched != len(left):
        return False

    for u in left:
        eid = mate_u[u]
        color[eid] = 1
        a, b = edges[eid]
        used[a] |= 1 << 1
        used[b] |= 1 << 1

    # The remaining edges form disjoint even cycles.
    for start_eid in component_edges:
        if color[start_eid] != 0:
            continue

        start_vertex = edges[start_eid][0]
        current_vertex = start_vertex
        current_eid = start_eid
        cycle = []

        while True:
            cycle.append(current_eid)
            a, b = edges[current_eid]
            next_vertex = b if a == current_vertex else a

            if next_vertex == start_vertex:
                break

            next_eid = -1
            for eid in adj[next_vertex]:
                if eid != current_eid and color[eid] == 0:
                    next_eid = eid
                    break

            if next_eid == -1:
                return False

            current_vertex = next_vertex
            current_eid = next_eid

            if len(cycle) > len(component_edges):
                return False

        if len(cycle) & 1:
            return False

        for i, eid in enumerate(cycle):
            c = 2 + (i & 1)
            color[eid] = c
            a, b = edges[eid]
            used[a] |= 1 << c
            used[b] |= 1 << c

    return True


def color_general_component(vertices, component_edges):
    trail = []

    def rollback(mark):
        while len(trail) > mark:
            eid = trail.pop()
            c = color[eid]
            bit = 1 << c
            a, b = edges[eid]
            used[a] ^= bit
            used[b] ^= bit
            color[eid] = 0

    def propagate(initial):
        stack = list(initial)

        while stack:
            eid, c = stack.pop()
            if color[eid] != 0:
                if color[eid] != c:
                    return False
                continue

            a, b = edges[eid]
            bit = 1 << c
            if (used[a] | used[b]) & bit:
                return False

            color[eid] = c
            used[a] |= bit
            used[b] |= bit
            trail.append(eid)

            for x in (a, b):
                for fid in adj[x]:
                    if color[fid] != 0:
                        continue
                    y, z = edges[fid]
                    available = FULL & ~(used[y] | used[z])
                    if available == 0:
                        return False
                    if available & (available - 1) == 0:
                        forced_color = available.bit_length() - 1
                        stack.append((fid, forced_color))

        return True

    def search():
        best_eid = -1
        best_available = 0
        best_count = 4
        best_score = -1

        for eid in component_edges:
            if color[eid] != 0:
                continue
            a, b = edges[eid]
            available = FULL & ~(used[a] | used[b])
            cnt = available.bit_count()

            if cnt == 0:
                return False

            score = used[a].bit_count() + used[b].bit_count()
            if cnt < best_count or (cnt == best_count and score > best_score):
                best_count = cnt
                best_score = score
                best_eid = eid
                best_available = available

        if best_eid == -1:
            return True

        candidate_colors = []
        mask = best_available
        while mask:
            bit = mask & -mask
            c = bit.bit_length() - 1
            mask -= bit

            # Prefer choices that immediately force more neighboring edges.
            force_score = 0
            a, b = edges[best_eid]
            for x in (a, b):
                new_used_x = used[x] | bit
                for fid in adj[x]:
                    if fid == best_eid or color[fid] != 0:
                        continue
                    y, z = edges[fid]
                    uy = new_used_x if y == x else used[y]
                    uz = new_used_x if z == x else used[z]
                    av = FULL & ~(uy | uz)
                    if av != 0 and av & (av - 1) == 0:
                        force_score += 1
            candidate_colors.append((-force_score, c))

        candidate_colors.sort()

        for _, c in candidate_colors:
            mark = len(trail)
            if propagate([(best_eid, c)]) and search():
                return True
            rollback(mark)

        return False

    # Fix the global color permutation at one vertex.
    root = vertices[0]
    root_edges = adj[root]
    initial_mark = len(trail)

    if not propagate([
        (root_edges[0], 1),
        (root_edges[1], 2),
        (root_edges[2], 3),
    ]):
        rollback(initial_mark)
        return False

    if search():
        return True

    rollback(initial_mark)
    return False


possible = True
for vertices, component_edges, is_bipartite in components:
    if is_bipartite:
        if not color_bipartite_component(vertices, component_edges):
            possible = False
            break
    else:
        if not color_general_component(vertices, component_edges):
            possible = False
            break

if not possible:
    print("NO")
else:
    print("YES")
    print(*color)
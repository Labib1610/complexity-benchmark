import sys
from collections import deque

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)

edges = []
adj = [[] for _ in range(n)]

for eid in range(m):
    u = next(it) - 1
    v = next(it) - 1
    edges.append((u, v))
    adj[u].append(eid)
    adj[v].append(eid)

if any(len(adj[v]) != 3 for v in range(n)):
    print("NO")
    sys.exit()

# A cubic graph with a bridge cannot be 3-edge-colored.
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
        a, b = edges[eid]
        to = b if a == v else a
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

# Find connected components and test bipartiteness.
side = [-1] * n
components = []

for start in range(n):
    if side[start] != -1:
        continue

    q = deque([start])
    side[start] = 0
    vertices = []
    bipartite = True

    while q:
        v = q.popleft()
        vertices.append(v)
        for eid in adj[v]:
            a, b = edges[eid]
            to = b if a == v else a
            if side[to] == -1:
                side[to] = side[v] ^ 1
                q.append(to)
            elif side[to] == side[v]:
                bipartite = False

    components.append((vertices, bipartite))

answer = [0] * m

def color_bipartite_component(vertices):
    left = [v for v in vertices if side[v] == 0]
    pair_u = [-1] * n
    pair_v = [-1] * n
    pair_edge_u = [-1] * n
    dist = [-1] * n

    def bfs():
        q = deque()
        reachable_free = False
        for u in left:
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1

        while q:
            u = q.popleft()
            for eid in adj[u]:
                a, b = edges[eid]
                v = b if a == u else a
                pu = pair_v[v]
                if pu == -1:
                    reachable_free = True
                elif dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return reachable_free

    def dfs(u):
        for eid in adj[u]:
            a, b = edges[eid]
            v = b if a == u else a
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                pair_edge_u[u] = eid
                return True
        dist[u] = -1
        return False

    matched = 0
    while bfs():
        for u in left:
            if pair_u[u] == -1 and dfs(u):
                matched += 1

    if matched != len(left):
        return False

    matching = set()
    for u in left:
        eid = pair_edge_u[u]
        if eid < 0:
            return False
        matching.add(eid)
        answer[eid] = 1

    # The complement of a perfect matching in a cubic bipartite graph
    # consists of even cycles.
    for v in vertices:
        for start_eid in adj[v]:
            if start_eid in matching or answer[start_eid] != 0:
                continue

            answer[start_eid] = 2
            q = deque([start_eid])

            while q:
                eid = q.popleft()
                next_color = 5 - answer[eid]  # 2 <-> 3
                a, b = edges[eid]

                for x in (a, b):
                    for other in adj[x]:
                        if other == eid or other in matching:
                            continue
                        if answer[other] == 0:
                            answer[other] = next_color
                            q.append(other)
                        elif answer[other] != next_color:
                            return False

    return True

non_bip_components = []

for vertices, bipartite in components:
    if bipartite:
        if not color_bipartite_component(vertices):
            print("NO")
            sys.exit()
    else:
        non_bip_components.append(vertices)

# Domains use bits 1, 2, 4 for the three colors.
domains = [7] * m
permutations = (
    (1, 2, 4), (1, 4, 2),
    (2, 1, 4), (2, 4, 1),
    (4, 1, 2), (4, 2, 1)
)
trail = []

def reduce_domain(eid, new_domain, queue):
    old = domains[eid]
    new_domain &= old
    if new_domain == old:
        return True
    if new_domain == 0:
        return False

    trail.append((eid, old))
    domains[eid] = new_domain
    u, v = edges[eid]
    queue.append(u)
    queue.append(v)
    return True

def propagate(queue):
    while queue:
        v = queue.popleft()
        e0, e1, e2 = adj[v]
        d0, d1, d2 = domains[e0], domains[e1], domains[e2]

        allow0 = allow1 = allow2 = 0
        found = False

        for p0, p1, p2 in permutations:
            if (d0 & p0) and (d1 & p1) and (d2 & p2):
                found = True
                allow0 |= p0
                allow1 |= p1
                allow2 |= p2

        if not found:
            return False

        if not reduce_domain(e0, allow0, queue):
            return False
        if not reduce_domain(e1, allow1, queue):
            return False
        if not reduce_domain(e2, allow2, queue):
            return False

    return True

def rollback(mark):
    while len(trail) > mark:
        eid, old = trail.pop()
        domains[eid] = old

def valid_permutations(v):
    e0, e1, e2 = adj[v]
    d0, d1, d2 = domains[e0], domains[e1], domains[e2]
    result = []
    for p in permutations:
        if (d0 & p[0]) and (d1 & p[1]) and (d2 & p[2]):
            result.append(p)
    return result

def solve_component(vertices):
    root = vertices[0]
    initial_mark = len(trail)
    q = deque()

    for eid, color in zip(adj[root], (1, 2, 4)):
        if not reduce_domain(eid, color, q):
            rollback(initial_mark)
            return False

    if not propagate(q):
        rollback(initial_mark)
        return False

    def search():
        best_v = -1
        best_options = None
        best_count = 7

        for v in vertices:
            opts = valid_permutations(v)
            count = len(opts)
            if count == 0:
                return False
            if 1 < count < best_count:
                best_count = count
                best_v = v
                best_options = opts
                if count == 2:
                    break

        if best_v == -1:
            return True

        incident = adj[best_v]

        for p in best_options:
            mark = len(trail)
            q = deque()
            ok = True

            for eid, color in zip(incident, p):
                if not reduce_domain(eid, color, q):
                    ok = False
                    break

            if ok and propagate(q) and search():
                return True

            rollback(mark)

        return False

    if search():
        return True

    rollback(initial_mark)
    return False

for vertices in non_bip_components:
    if not solve_component(vertices):
        print("NO")
        sys.exit()

for vertices in non_bip_components:
    for v in vertices:
        for eid in adj[v]:
            d = domains[eid]
            if d == 1:
                answer[eid] = 1
            elif d == 2:
                answer[eid] = 2
            elif d == 4:
                answer[eid] = 3
            else:
                print("NO")
                sys.exit()

# Final verification.
for v in range(n):
    colors = [answer[eid] for eid in adj[v]]
    if sorted(colors) != [1, 2, 3]:
        print("NO")
        sys.exit()

print("YES")
print(*answer)
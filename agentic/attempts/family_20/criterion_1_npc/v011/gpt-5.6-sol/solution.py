import sys
from collections import deque

sys.setrecursionlimit(10000)

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

# A bridge cannot occur in a 3-edge-colorable cubic graph.
timer = 0
tin = [-1] * n
low = [0] * n
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

for start in range(n):
    if tin[start] == -1:
        bridge_dfs(start, -1)

if has_bridge:
    print("NO")
    sys.exit()

# Find connected components and test bipartiteness.
side = [-1] * n
components = []
all_bipartite = True

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
    if not bipartite:
        all_bipartite = False

answer = [-1] * m

def color_bipartite_component(vertices):
    left = [v for v in vertices if side[v] == 0]

    for color in range(2):
        pair_u = [-1] * n
        pair_v = [-1] * n
        dist = [-1] * n

        def bfs():
            q = deque()
            found = False
            for u in left:
                if pair_u[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1

            while q:
                u = q.popleft()
                for eid in adj[u]:
                    if answer[eid] != -1:
                        continue
                    a, b = edges[eid]
                    v = b if a == u else a
                    pe = pair_v[v]
                    if pe == -1:
                        found = True
                    else:
                        x, y = edges[pe]
                        u2 = x if side[x] == 0 else y
                        if dist[u2] == -1:
                            dist[u2] = dist[u] + 1
                            q.append(u2)
            return found

        def dfs(u):
            for eid in adj[u]:
                if answer[eid] != -1:
                    continue
                a, b = edges[eid]
                v = b if a == u else a
                pe = pair_v[v]
                if pe == -1:
                    pair_u[u] = eid
                    pair_v[v] = eid
                    return True
                x, y = edges[pe]
                u2 = x if side[x] == 0 else y
                if dist[u2] == dist[u] + 1 and dfs(u2):
                    pair_u[u] = eid
                    pair_v[v] = eid
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

        for u in left:
            answer[pair_u[u]] = color

    for v in vertices:
        for eid in adj[v]:
            if answer[eid] == -1:
                answer[eid] = 2

    return True

if all_bipartite:
    for vertices, _ in components:
        if not color_bipartite_component(vertices):
            print("NO")
            sys.exit()
    print("YES")
    print(*[c + 1 for c in answer])
    sys.exit()

# Color bipartite components directly; the remaining components are solved by DLX.
for vertices, bipartite in components:
    if bipartite:
        if not color_bipartite_component(vertices):
            print("NO")
            sys.exit()

# Exact-cover formulation:
# - one column for each edge (choose exactly one color),
# - one column for each (vertex, color) pair.
column_count = m + 3 * n
root = 0

L = list(range(column_count + 1))
R = list(range(column_count + 1))
U = list(range(column_count + 1))
D = list(range(column_count + 1))
C = list(range(column_count + 1))
S = [0] * (column_count + 1)
ROW = [-1] * (column_count + 1)

for c in range(column_count + 1):
    L[c] = c - 1
    R[c] = c + 1
L[0] = column_count
R[column_count] = 0

row_first = [-1] * (3 * m)

def add_row(row_id, columns):
    first = -1
    previous = -1

    for col0 in columns:
        col = col0 + 1
        idx = len(L)

        L.append(idx)
        R.append(idx)
        U.append(U[col])
        D.append(col)
        C.append(col)
        S.append(0)
        ROW.append(row_id)

        D[U[col]] = idx
        U[col] = idx
        S[col] += 1

        if first == -1:
            first = idx
        else:
            L[idx] = previous
            R[previous] = idx
        previous = idx

    L[first] = previous
    R[previous] = first
    row_first[row_id] = first

for eid, (u, v) in enumerate(edges):
    for color in range(3):
        row_id = 3 * eid + color
        add_row(
            row_id,
            (
                eid,
                m + 3 * u + color,
                m + 3 * v + color
            )
        )

def cover(col):
    R[L[col]] = R[col]
    L[R[col]] = L[col]
    i = D[col]
    while i != col:
        j = R[i]
        while j != i:
            D[U[j]] = D[j]
            U[D[j]] = U[j]
            S[C[j]] -= 1
            j = R[j]
        i = D[i]

def uncover(col):
    i = U[col]
    while i != col:
        j = L[i]
        while j != i:
            S[C[j]] += 1
            D[U[j]] = j
            U[D[j]] = j
            j = L[j]
        i = U[i]
    R[L[col]] = col
    L[R[col]] = col

solution_rows = []

def select_fixed_row(row_id):
    node = row_first[row_id]
    solution_rows.append(row_id)
    j = node
    while True:
        cover(C[j])
        j = R[j]
        if j == node:
            break

# Fix already colored bipartite components.
for eid in range(m):
    if answer[eid] != -1:
        select_fixed_row(3 * eid + answer[eid])

# Break color symmetry independently in every non-bipartite component.
for vertices, bipartite in components:
    if bipartite:
        continue
    v = vertices[0]
    incident = adj[v]
    for color, eid in enumerate(incident):
        select_fixed_row(3 * eid + color)

def search():
    if R[root] == root:
        return True

    col = R[root]
    best = col
    best_size = S[col]
    col = R[col]

    while col != root:
        if S[col] < best_size:
            best = col
            best_size = S[col]
            if best_size <= 1:
                break
        col = R[col]

    if best_size == 0:
        return False

    cover(best)
    row_node = D[best]

    while row_node != best:
        solution_rows.append(ROW[row_node])

        j = R[row_node]
        while j != row_node:
            cover(C[j])
            j = R[j]

        if search():
            return True

        j = L[row_node]
        while j != row_node:
            uncover(C[j])
            j = L[j]

        solution_rows.pop()
        row_node = D[row_node]

    uncover(best)
    return False

if not search():
    print("NO")
    sys.exit()

for row_id in solution_rows:
    eid, color = divmod(row_id, 3)
    answer[eid] = color

if any(c == -1 for c in answer):
    print("NO")
else:
    print("YES")
    print(*[c + 1 for c in answer])
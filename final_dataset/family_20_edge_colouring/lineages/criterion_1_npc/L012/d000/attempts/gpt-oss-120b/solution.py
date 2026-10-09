import sys
sys.setrecursionlimit(10000)

# ------------------------------------------------------------
# 1. read input
data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
it = iter(data)
n = int(next(it))
m = int(next(it))
edges = []
adj = [[] for _ in range(n)]
for idx in range(m):
    u = int(next(it)) - 1
    v = int(next(it)) - 1
    edges.append((u, v))
    adj[u].append((v, idx))
    adj[v].append((u, idx))

# ------------------------------------------------------------
# 2. bridge detection
tin = [-1] * n
low = [0] * n
timer = 0
has_bridge = False

def dfs(v, p):
    global timer, has_bridge
    tin[v] = low[v] = timer
    timer += 1
    for to, _ in adj[v]:
        if to == p:
            continue
        if tin[to] != -1:
            low[v] = min(low[v], tin[to])
        else:
            dfs(to, v)
            low[v] = min(low[v], low[to])
            if low[to] > tin[v]:
                has_bridge = True

dfs(0, -1)
if has_bridge:
    print("NO")
    sys.exit()

# ------------------------------------------------------------
# 3. Edmonds' blossom algorithm (maximum matching)
from collections import deque

def blossom_maximum_matching(n, g):
    # g: adjacency list of vertices (list of lists)
    INF = n + 5
    match = [-1] * n
    base = list(range(n))
    p = [-1] * n
    q = deque()
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used_path = [False] * n
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal used, p, base, q, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cur = lca(v, to)
                    blossom[:] = [False] * n
                    mark_path(v, cur, to)
                    mark_path(to, cur, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = cur
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting
                        v = to
                        while v != -1:
                            pv = p[v]
                            nv = match[pv] if pv != -1 else -1
                            match[v] = pv
                            match[pv] = v
                            v = nv
                        return True
                    else:
                        used[match[to]] = True
                        q.append(match[to])
        return False

    for v in range(n):
        if match[v] == -1:
            find_path(v)
    return match

# build simple adjacency list for blossom (no edge indices needed)
g = [[] for _ in range(n)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

mate = blossom_maximum_matching(n, g)

if any(x == -1 for x in mate):
    print("NO")
    sys.exit()

# ------------------------------------------------------------
# 4. colour edges
color = [0] * m
# colour 1 for matching edges
for idx, (u, v) in enumerate(edges):
    if mate[u] == v:
        color[idx] = 1

# build adjacency of remaining edges (those not coloured yet)
rem_adj = [[] for _ in range(n)]
for idx, (u, v) in enumerate(edges):
    if color[idx] == 0:
        rem_adj[u].append((v, idx))
        rem_adj[v].append((u, idx))

visited_edge = [False] * m

for start in range(n):
    for to, eid in rem_adj[start]:
        if visited_edge[eid]:
            continue
        # walk the whole cycle
        cycle = []
        cur = start
        prev = -1
        while True:
            # find the unused edge from cur that is not the edge we came from
            for nxt, neid in rem_adj[cur]:
                if visited_edge[neid]:
                    continue
                if nxt == prev:
                    continue
                # this is the next edge
                visited_edge[neid] = True
                cycle.append(neid)
                prev, cur = cur, nxt
                break
            else:
                # should not happen
                break
            if cur == start:
                break
        # colour alternately 2,3
        for i, eid in enumerate(cycle):
            color[eid] = 2 if i % 2 == 0 else 3

print("YES")
print(' '.join(str(c) for c in color))
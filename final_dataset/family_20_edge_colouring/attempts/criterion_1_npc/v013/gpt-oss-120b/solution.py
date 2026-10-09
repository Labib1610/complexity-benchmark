import sys
sys.setrecursionlimit(10000)

# ---------- 1. read ----------
def read():
    data = sys.stdin.read().strip().split()
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
    return n, m, edges, adj

# ---------- 2. bridge detection ----------
def has_bridge(n, adj):
    timer = 0
    tin = [-1] * n
    low = [0] * n
    visited = [False] * n
    bridge = False

    def dfs(v, p):
        nonlocal timer, bridge
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, _ in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridge = True

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridge

# ---------- 3. Blossom (Edmonds) ----------
# implementation from CP‑Algorithms, adapted for 0‑based vertices
from collections import deque

def blossom_maximum_matching(n, g):
    # g: adjacency list of sets
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
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
                    curbase = lca(v, to)
                    blossom = [False] * n
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting path found
                        return to
                    to_match = match[to]
                    used[to_match] = True
                    q.append(to_match)
        return -1

    for v in range(n):
        if match[v] == -1:
            to = find_path(v)
            if to == -1:
                continue
            # augment
            cur = to
            while cur != -1:
                prev = p[cur]
                nxt = match[prev] if prev != -1 else -1
                match[cur] = prev
                match[prev] = cur
                cur = nxt
    return match

# ---------- 4. main ----------
def solve():
    n, m, edges, adj = read()
    if has_bridge(n, adj):
        print("NO")
        return

    # build adjacency set for blossom
    g = [set() for _ in range(n)]
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    mate = blossom_maximum_matching(n, g)
    # verify perfect matching
    if any(x == -1 for x in mate):
        print("NO")
        return

    # colour array
    colour = [0] * m
    # map edge (u,v) to its id (multiple edges not present)
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = idx
        edge_id[(v, u)] = idx

    # 1. colour matching edges with 1 and build remaining adjacency
    rem_adj = [[] for _ in range(n)]
    for v in range(n):
        u = mate[v]
        if v < u:  # each edge once
            idx = edge_id[(v, u)]
            colour[idx] = 1
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    # 2. colour cycles alternating 2,3
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev = -1
        cur_colour = 2
        while True:
            visited[cur] = True
            # find the next edge not coming from prev
            for to, idx in rem_adj[cur]:
                if to == prev:
                    continue
                # this is the edge to traverse
                colour[idx] = cur_colour
                # move forward
                prev, cur = cur, to
                cur_colour = 5 - cur_colour   # switch 2<->3
                break
            else:
                break
            if visited[cur]:
                # cycle closed
                break

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()
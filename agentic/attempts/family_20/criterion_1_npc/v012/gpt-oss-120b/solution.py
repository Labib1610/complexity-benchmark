import sys
sys.setrecursionlimit(10000)

# ---------- 1. read input ----------
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
    tin = [-1]*n
    low = [0]*n
    visited = [False]*n
    bridge_found = False

    def dfs(v, p):
        nonlocal timer, bridge_found
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
                    bridge_found = True

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridge_found

# ---------- 3. Blossom algorithm (Edmonds) ----------
from collections import deque

def blossom_maximum_matching(n, graph):
    # graph: adjacency list of sets (undirected)
    INF = n + 5
    match = [-1]*n
    base = list(range(n))
    p = [-1]*n
    q = deque()
    used = [False]*n
    blossom = [False]*n

    def lca(a, b):
        used_path = [False]*n
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
        nonlocal p, base, used, blossom, q
        used = [False]*n
        p = [-1]*n
        for i in range(n):
            base[i] = i
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for to in graph[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False]*n
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
                        # augmenting
                        cur = to
                        while cur != -1:
                            prev = p[cur]
                            nxt = match[prev] if prev != -1 else -1
                            match[cur] = prev
                            match[prev] = cur
                            cur = nxt
                        return True
                    else:
                        used[match[to]] = True
                        q.append(match[to])
        return False

    for v in range(n):
        if match[v] == -1:
            find_path(v)
    return match

# ---------- 4. main ----------
def solve():
    n, m, edges, adj = read()
    if has_bridge(n, adj):
        print("NO")
        return

    # build adjacency list for blossom (as list of neighbours)
    g = [set() for _ in range(n)]
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    match = blossom_maximum_matching(n, g)
    if any(x == -1 for x in match):
        print("NO")
        return

    # map matched edge to its index
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = idx
        edge_id[(v, u)] = idx

    colour = [0]*m
    matched_edge = [False]*m
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            idx = edge_id[(v, u)]
            colour[idx] = 1
            matched_edge[idx] = True

    # build adjacency of remaining edges (non‑matching)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not matched_edge[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False]*m
    for start in range(n):
        for to, idx in rem_adj[start]:
            if visited_edge[idx]:
                continue
            # traverse one cycle
            cur = start
            cur_col = 2
            while True:
                # find the unused edge from cur
                for nxt, eidx in rem_adj[cur]:
                    if not visited_edge[eidx]:
                        break
                visited_edge[eidx] = True
                colour[eidx] = cur_col
                cur_col = 5 - cur_col          # switch between 2 and 3
                cur = nxt
                if cur == start:
                    break

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()
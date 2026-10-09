import sys
sys.setrecursionlimit(10000)

# ---------- 1. bridge detection ----------
def has_bridge(n, adj):
    tin = [0] * n
    low = [0] * n
    timer = 1
    visited = [False] * n
    def dfs(v, p):
        nonlocal timer
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
                    raise StopIteration  # bridge found
    try:
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
        return False
    except StopIteration:
        return True

# ---------- 2. Edmonds blossom (general matching) ----------
# implementation adapted from https://github.com/jaehyunp/stanfordacm
def blossom(adj, n):
    INF = n + 5
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = []
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used2 = [False] * n
        while True:
            a = base[a]
            used2[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used2[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal q, used, p, base, blossom
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]
            q_head += 1
            for to in adj[v]:
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
            if to != -1:
                # augment
                cur = to
                while cur != -1:
                    prev = p[cur]
                    nxt = match[prev] if prev != -1 else -1
                    match[cur] = prev
                    match[prev] = cur
                    cur = nxt
    return match

# ---------- 3. main ----------
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
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

    # bridge test
    if has_bridge(n, adj):
        print("NO")
        return

    # build simple adjacency list for blossom (only neighbours)
    simple_adj = [[] for _ in range(n)]
    for u, v in edges:
        simple_adj[u].append(v)
        simple_adj[v].append(u)

    match = blossom(simple_adj, n)
    if any(x == -1 for x in match):
        print("NO")
        return

    # colour array
    colour = [0] * m
    # colour matched edges with 1
    matched_edge = {}
    for v in range(n):
        u = match[v]
        if v < u:
            # find edge index
            for to, idx in adj[v]:
                if to == u:
                    colour[idx] = 1
                    matched_edge[(v, u)] = idx
                    matched_edge[(u, v)] = idx
                    break

    # remaining edges form cycles, colour alternately 2/3
    visited_edge = [False] * m
    for idx, c in enumerate(colour):
        if c == 1:
            visited_edge[idx] = True

    for start in range(n):
        # each vertex has exactly two unvisited incident edges now
        for to, idx in adj[start]:
            if visited_edge[idx]:
                continue
            # start a new cycle from this edge
            cur = start
            prev = -1
            cur_colour = 2
            while True:
                # find the unvisited edge from cur that is not the one we came from
                for nxt, eidx in adj[cur]:
                    if visited_edge[eidx]:
                        continue
                    if nxt == prev:
                        continue
                    # this is the next edge in the cycle
                    colour[eidx] = cur_colour
                    visited_edge[eidx] = True
                    # move forward
                    prev, cur = cur, nxt
                    cur_colour = 5 - cur_colour   # switch between 2 and 3
                    break
                else:
                    break
                # if we returned to start and the edge back to start is already visited, cycle finished
                if cur == start and prev != -1:
                    # check if there is still an unvisited edge from start (the other side of the cycle)
                    # it will be handled when we iterate other vertices
                    pass

    print("YES")
    print(' '.join(str(colour[i]) for i in range(m)))

if __name__ == "__main__":
    solve()
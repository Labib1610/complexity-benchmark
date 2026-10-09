import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom algorithm (max matching) ----------
def max_matching(n, adj):
    """return list match where match[v] = partner or -1"""
    INF = n + 5
    match = [-1] * n
    p = [-1] * n          # parent in the forest
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
        q = [root]
        used[root] = True
        head = 0
        while head < len(q):
            v = q[head]
            head += 1
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

# ------------------- main solving part -------------------------

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
        adj[u].append(v)
        adj[v].append(u)

    match = max_matching(n, adj)
    if any(x == -1 for x in match):
        print("NO")
        return

    # colour 1 for matching edges
    colour = [0] * m
    for i, (u, v) in enumerate(edges):
        if match[u] == v:
            colour[i] = 1

    # build graph of remaining edges (those with colour 0)
    rem_adj = [[] for _ in range(n)]
    edge_id = {}
    for i, (u, v) in enumerate(edges):
        if colour[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))
            edge_id[(u, v)] = edge_id[(v, u)] = i

    visited_edge = [False] * m
    visited_vert = [False] * n

    for start in range(n):
        if visited_vert[start]:
            continue
        # start DFS only if there is a remaining edge incident
        if not any(colour[eid] == 0 for _, eid in rem_adj[start]):
            visited_vert[start] = True
            continue
        stack = [(start, -1, 0)]  # vertex, incoming edge id, colour to use for next edge
        while stack:
            v, inc_eid, col_next = stack.pop()
            visited_vert[v] = True
            cur = col_next
            for to, eid in rem_adj[v]:
                if colour[eid] != 0:
                    continue
                if visited_edge[eid]:
                    continue
                # assign colour 2 or 3 alternately
                colour[eid] = 2 if cur == 0 else 3
                visited_edge[eid] = True
                # next vertex will use opposite colour for its other edge
                stack.append((to, eid, 1 - cur))
                cur = 1 - cur  # alternate along the cycle

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    solve()
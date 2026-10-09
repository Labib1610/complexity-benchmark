import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom (CP‑algorithm version) ----------
def blossom_maximum_matching(n, g):
    """n vertices 0..n-1, g adjacency list (list of lists of neighbours)"""
    INF = n + 5
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = []
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

# ---------- main ----------
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

    # find maximum matching
    match = blossom_maximum_matching(n, adj)
    matched_cnt = sum(1 for x in match if x != -1) // 2
    if matched_cnt * 2 != n:
        print("NO")
        return

    # colour array
    col = [0] * m
    # DSU for contraction
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a = find(a); b = find(b)
        if a != b:
            parent[b] = a

    # mark matched edges, colour 1, union their ends
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            col[idx] = 1
            union(u, v)

    # build adjacency of contracted graph (only unmatched edges)
    comp_adj = dict()          # comp -> list of (neighbor comp, edge idx)
    for idx, (u, v) in enumerate(edges):
        if col[idx] != 0:
            continue
        cu = find(u)
        cv = find(v)
        if cu == cv:
            # should not happen in a proper cubic graph with perfect matching
            print("NO")
            return
        comp_adj.setdefault(cu, []).append((cv, idx))
        comp_adj.setdefault(cv, []).append((cu, idx))

    # each component must have degree 2
    for lst in comp_adj.values():
        if len(lst) != 2:
            print("NO")
            return

    used_edge = [False] * m
    for start in list(comp_adj.keys()):
        # walk all cycles starting from this component
        while comp_adj[start]:
            cur = start
            cur_color = 2
            while True:
                # take an unused incident edge
                while comp_adj[cur] and used_edge[comp_adj[cur][-1][1]]:
                    comp_adj[cur].pop()
                if not comp_adj[cur]:
                    break
                nxt, eidx = comp_adj[cur].pop()
                if used_edge[eidx]:
                    continue
                used_edge[eidx] = True
                col[eidx] = cur_color
                # remove the opposite direction entry
                lst = comp_adj[nxt]
                for i in range(len(lst)):
                    if lst[i][0] == cur and lst[i][1] == eidx:
                        lst.pop(i)
                        break
                cur = nxt
                cur_color = 5 - cur_color   # toggle between 2 and 3
            # after finishing one cycle, break to outer while to check remaining edges

    print("YES")
    print(' '.join(str(c) for c in col))

if __name__ == "__main__":
    solve()
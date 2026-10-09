import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom algorithm (max matching) ----------
# implementation adapted from https://github.com/jaehyunp/stanfordacm
def max_matching(n, adj):
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

# -------------------- main solving part --------------------
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

    match = max_matching(n, adj)          # vertex -> its partner or -1
    # build set of matching edges
    in_match = set()
    for v in range(n):
        if match[v] != -1 and v < match[v]:
            in_match.add((v, match[v]))

    colour = [0] * m
    # colour matching edges with 3
    for idx, (u, v) in enumerate(edges):
        if (u, v) in in_match or (v, u) in in_match:
            colour[idx] = 3

    # build adjacency of non‑matching edges for cycle traversal
    non_adj = [[] for _ in range(n)]
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            non_adj[u].append((v, idx))
            non_adj[v].append((u, idx))
            edge_id[(u, v)] = edge_id[(v, u)] = idx

    visited_edge = [False] * m
    for start in range(n):
        for (to, eid) in non_adj[start]:
            if visited_edge[eid]:
                continue
            # start a new cycle
            cur = start
            cur_colour = 1
            while True:
                # find the unused edge from cur
                for (nxt, neid) in non_adj[cur]:
                    if not visited_edge[neid]:
                        break
                visited_edge[neid] = True
                colour[neid] = cur_colour
                cur_colour = 2 if cur_colour == 1 else 1
                cur = nxt
                if cur == start:
                    break

    # output
    out = ['YES', ' '.join(map(str, colour))]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
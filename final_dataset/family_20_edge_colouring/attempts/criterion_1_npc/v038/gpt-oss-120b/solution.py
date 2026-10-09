import sys
sys.setrecursionlimit(10000)

# ---------- Blossom (Edmonds) implementation ----------
# based on CP‑Algorithms: https://cp-algorithms.com/graph/edmonds_karp.html
class Blossom:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, idx):
        self.g[u].append((v, idx))
        self.g[v].append((u, idx))

    def max_matching(self):
        n = self.n
        g = self.g
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
                for to, _ in g[v]:
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

# ---------- Main solution ----------
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    deg = [0]*n
    edge_id = {}
    for idx in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
        deg[u] += 1
        deg[v] += 1
        edge_id[(u, v)] = edge_id[(v, u)] = idx

    if any(d != 3 for d in deg):
        print("NO")
        return

    # bridge detection
    sys.setrecursionlimit(10000)
    tin = [-1]*n
    low = [0]*n
    timer = 0
    has_bridge = False
    def dfs(v, p):
        nonlocal timer, has_bridge
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
        return

    # blossom matching
    bl = Blossom(n)
    for idx, (u, v) in enumerate(edges):
        bl.add_edge(u, v, idx)
    match = bl.max_matching()
    if any(x == -1 for x in match):
        print("NO")
        return
    # build matching set
    matched = [False]*m
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            idx = edge_id[(v, u)]
            matched[idx] = True

    colour = [0]*m
    # colour 1 for matching edges, and build reduced adjacency
    red_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if matched[idx]:
            colour[idx] = 1
        else:
            red_adj[u].append((v, idx))
            red_adj[v].append((u, idx))

    visited = [False]*n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        cur = start
        prev = -1
        curcol = 2
        while True:
            visited[cur] = True
            # two neighbours, pick the one not equal to prev
            nxt, eid = red_adj[cur][0] if red_adj[cur][0][0] != prev else red_adj[cur][1]
            colour[eid] = curcol
            curcol = 5 - curcol          # toggle 2<->3
            prev, cur = cur, nxt
            if cur == start:
                break

    print("YES")
    print(' '.join(str(colour[i]) for i in range(m)))

if __name__ == "__main__":
    solve()
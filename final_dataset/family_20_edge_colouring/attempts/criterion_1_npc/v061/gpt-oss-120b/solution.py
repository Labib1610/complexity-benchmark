import sys
sys.setrecursionlimit(10000)

# ------------------------------------------------------------
# 1. bridge detection (Tarjan)
def find_bridges(n, adj):
    timer = 0
    tin = [0] * n
    low = [0] * n
    visited = [False] * n
    has_bridge = False

    def dfs(v, p):
        nonlocal timer, has_bridge
        visited[v] = True
        timer += 1
        tin[v] = low[v] = timer
        for to, _ in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return has_bridge

# ------------------------------------------------------------
# 2. Edmonds' blossom (implementation from emaxx)
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
            for i in range(n):
                base[i] = i
            q = []
            q_head = 0
            q.append(root)
            used[root] = True
            while q_head < len(q):
                v = q[q_head]
                q_head += 1
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

# ------------------------------------------------------------
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

    # 1) bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # 2) perfect matching
    bl = Blossom(n)
    for idx, (u, v) in enumerate(edges):
        bl.add_edge(u, v, idx)
    match = bl.max_matching()
    matched_edges = set()
    for v in range(n):
        if match[v] != -1 and v < match[v]:
            # find edge index between v and match[v]
            for to, idx in adj[v]:
                if to == match[v]:
                    matched_edges.add(idx)
                    break

    if len(matched_edges) != n // 2:
        print("NO")
        return

    # 3) colour assignment
    colour = [0] * m
    for idx in matched_edges:
        colour[idx] = 1

    # build remaining adjacency (each vertex degree 2)
    rem = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem[u].append((v, idx))
            rem[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle
        v = start
        prev_edge = -1
        cur_colour = 2
        while True:
            visited[v] = True
            # pick the edge not equal to prev_edge
            for to, idx in rem[v]:
                if idx != prev_edge:
                    nxt = to
                    eidx = idx
                    break
            colour[eidx] = cur_colour
            cur_colour = 5 - cur_colour          # toggle 2<->3
            prev_edge = eidx
            v = nxt
            if visited[v]:
                break

    print("YES")
    print(' '.join(str(colour[i]) for i in range(m)))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(10000)

# ------------------------------------------------------------
# 1. bridge detection
def find_bridges(n, adj):
    tin = [0] * n
    low = [0] * n
    timer = 1
    bridges = []

    def dfs(v, p):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if to == p:
                continue
            if tin[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append(eid)
    for i in range(n):
        if not tin[i]:
            dfs(i, -1)
    return bridges

# ------------------------------------------------------------
# 2. Edmonds' blossom algorithm (maximum matching in general graph)
# implementation adapted from https://github.com/jaehyunp/stanfordacm
class Blossom:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def max_matching(self):
        n = self.n
        match = [-1] * n
        base = list(range(n))
        p = [-1] * n
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

        def mark_path(v, b, x):
            while base[v] != b:
                blossom[base[v]] = blossom[base[match[v]]] = True
                p[v] = x
                x = match[v]
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
                for to in self.adj[v]:
                    if base[v] == base[to] or match[v] == to:
                        continue
                    if to == root or (match[to] != -1 and p[match[to]] != -1):
                        cur = lca(v, to)
                        blossom = [False] * n
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
                            # augmenting path found
                            return to
                        to_match = match[to]
                        used[to_match] = True
                        q.append(to_match)
            return -1

        def augment_path(finish):
            v = finish
            while v != -1:
                pv = p[v]
                nv = match[pv] if pv != -1 else -1
                match[v] = pv
                match[pv] = v
                v = nv

        for v in range(n):
            if match[v] == -1:
                finish = find_path(v)
                if finish != -1:
                    augment_path(finish)
        return match

# ------------------------------------------------------------
def main():
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

    # 1. bridge test
    if find_bridges(n, adj):
        print("NO")
        return

    # 2. perfect matching
    blossom = Blossom(n)
    for u, v in edges:
        blossom.add_edge(u, v)
    match = blossom.max_matching()
    # verify perfect
    if any(x == -1 for x in match):
        print("NO")
        return

    # 3. colour edges
    colour = [0] * m
    # colour matching edges with 1
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            colour[idx] = 1

    # build graph of remaining edges (degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for to, eid in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # traverse the cycle
            cycle = []
            cur = start
            prev = -1
            while True:
                # find next edge not visited
                for nxt, neid in rem_adj[cur]:
                    if neid == prev:
                        continue
                    if visited_edge[neid]:
                        continue
                    cycle.append((cur, nxt, neid))
                    visited_edge[neid] = True
                    prev = neid
                    cur = nxt
                    break
                else:
                    break
                if cur == start:
                    break
            # colour alternately 2,3
            col = 2
            for _, _, eid in cycle:
                colour[eid] = col
                col = 5 - col   # switch between 2 and 3

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    main()
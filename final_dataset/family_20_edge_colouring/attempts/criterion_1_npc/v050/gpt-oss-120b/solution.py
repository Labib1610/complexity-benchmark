import sys
sys.setrecursionlimit(10000)

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

    # ---------- Edmonds' blossom (max matching) ----------
    from collections import deque

    INF = n + 5

    def blossom_maximum_matching():
        # implementation for general graph, returns match list and size
        N = n
        g = [[] for _ in range(N)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        match = [-1] * N
        p = [-1] * N
        base = list(range(N))
        q = deque()
        used = [False] * N
        blossom = [False] * N

        def lca(a, b):
            used2 = [False] * N
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
            nonlocal used, p, base, q, blossom
            used = [False] * N
            p = [-1] * N
            for i in range(N):
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
                        blossom = [False] * N
                        mark_path(v, curbase, to)
                        mark_path(to, curbase, v)
                        for i in range(N):
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

        def augment_path(finish):
            v = finish
            while v != -1:
                pv = p[v]
                ppv = match[pv] if pv != -1 else -1
                match[v] = pv
                match[pv] = v
                v = ppv

        for v in range(N):
            if match[v] == -1:
                finish = find_path(v)
                if finish != -1:
                    augment_path(finish)

        size = sum(1 for x in match if x != -1) // 2
        return match, size

    match, size = blossom_maximum_matching()
    if size * 2 != n:
        print("NO")
        return

    # ---------- build colouring ----------
    colour = [0] * m
    # colour matched edges with 1
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            # find edge index
            for to, idx in adj[v]:
                if to == u:
                    colour[idx] = 1
                    break

    # remaining edges: each vertex degree 2 now
    visited_edge = [False] * m
    for idx, c in enumerate(colour):
        if c == 1:
            visited_edge[idx] = True

    # adjacency of remaining edges (edge index stored)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not visited_edge[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    for start in range(n):
        # find an uncoloured incident edge
        for to, idx in rem_adj[start]:
            if colour[idx] == 0:
                # walk the whole cycle
                cur = start
                cur_colour = 2
                while True:
                    # take the edge from cur that is still uncoloured
                    for nxt, eidx in rem_adj[cur]:
                        if colour[eidx] == 0:
                            colour[eidx] = cur_colour
                            cur = nxt
                            cur_colour = 5 - cur_colour   # switch 2<->3
                            break
                    else:
                        break
                break

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()
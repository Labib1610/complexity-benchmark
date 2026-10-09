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

    # ---------- Edmonds' blossom algorithm (max matching) ----------
    # implementation based on emaxx.ru
    N = n
    g = [[] for _ in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = [-1] * N
    p = [-1] * N
    base = list(range(N))
    q = []
    used = [False] * N
    blossom = [False] * N

    def lca(a, b):
        used_path = [False] * N
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
        used = [False] * N
        p = [-1] * N
        base = list(range(N))
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

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    # ---------------------------------------------------------------

    if any(mch == -1 for mch in match):
        print("NO")
        return

    # Build color assignment
    color = [0] * m
    in_match = [False] * m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1
            in_match[idx] = True

    # remaining edges adjacency
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not in_match[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    # verify degree 2 for all vertices in remaining graph
    for v in range(n):
        if len(rem_adj[v]) != 2:
            print("NO")
            return

    visited_edge = [False] * m
    for start in range(n):
        for (nbr, eidx) in rem_adj[start]:
            if visited_edge[eidx]:
                continue
            # traverse cycle
            cur = start
            cur_color = 2
            while True:
                # find edge from cur that is not visited
                for (to, ei) in rem_adj[cur]:
                    if not visited_edge[ei]:
                        break
                else:
                    break
                visited_edge[ei] = True
                color[ei] = cur_color
                cur_color = 5 - cur_color  # toggle between 2 and 3
                cur = to
                # continue until we return to start
                if cur == start:
                    # mark the last edge that closes the cycle
                    # find the remaining unvisited edge at start
                    for (to2, ei2) in rem_adj[cur]:
                        if not visited_edge[ei2]:
                            visited_edge[ei2] = True
                            color[ei2] = cur_color
                    break

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
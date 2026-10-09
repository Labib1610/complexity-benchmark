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
    g = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        g[u].append((v, idx))
        g[v].append((u, idx))

    # Edmonds' blossom algorithm for maximum matching
    N = n
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

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
            for to in adj[v]:
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

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    if any(mch == -1 for mch in match):
        print("NO")
        return

    # Build color assignment
    color = [0] * m
    # color 1 for matching edges
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1

    # Build adjacency of remaining edges (those not colored)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse each cycle
        v = start
        while not visited[v]:
            visited[v] = True
            for to, idx in rem_adj[v]:
                if color[idx] == 0:
                    # assign alternating colors 2 and3
                    # determine color based on parity of step
                    # we can do DFS
                    stack = [(v, None, 2)]
                    while stack:
                        cur, parent_edge, curcol = stack.pop()
                        for nxt, eidx in rem_adj[cur]:
                            if eidx == parent_edge:
                                continue
                            if color[eidx] != 0:
                                continue
                            color[eidx] = curcol
                            stack.append((nxt, eidx, 5 - curcol))  # toggle 2<->3
                    break
            # move to next vertex in component
            # find any unvisited neighbor via uncolored edge
            nxt = None
            for to, idx in rem_adj[v]:
                if not visited[to]:
                    nxt = to
                    break
            if nxt is None:
                break
            v = nxt

    print("YES")
    print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    solve()
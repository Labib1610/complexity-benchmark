import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # Blossom algorithm for maximum matching
    from collections import deque

    N = n
    g = [[] for _ in range(N)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = [-1]*N
    p = [-1]*N
    base = list(range(N))
    q = deque()
    used = [False]*N
    blossom = [False]*N

    def lca(a, b):
        used_path = [False]*N
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

    def mark_path(v, b, child):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = child
            child = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal used, p, base, q, blossom
        used = [False]*N
        p = [-1]*N
        base = list(range(N))
        q.clear()
        q.append(root)
        used[root] = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cur = lca(v, to)
                    blossom = [False]*N
                    mark_path(v, cur, to)
                    mark_path(to, cur, v)
                    for i in range(N):
                        if blossom[base[i]]:
                            base[i] = cur
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

    for v in range(N):
        if match[v] == -1:
            find_path(v)

    if any(mch == -1 for mch in match):
        print("NO")
        return

    # Build color assignment
    color = [0]*m
    # color 1 for matching edges
    for v in range(N):
        u = match[v]
        if v < u:
            # find edge index
            for to, idx in adj[v]:
                if to == u:
                    color[idx] = 1
                    break

    # remaining edges form cycles, color alternately 2 and 3
    visited_edge = [False]*m
    for idx, c in enumerate(color):
        if c == 1:
            visited_edge[idx] = True

    for start in range(N):
        # traverse each cycle starting from unmatched edge
        for to, idx in adj[start]:
            if visited_edge[idx]:
                continue
            # start new cycle
            cur = start
            col = 2
            while True:
                # find edge from cur not visited
                for nxt, eidx in adj[cur]:
                    if visited_edge[eidx]:
                        continue
                    visited_edge[eidx] = True
                    color[eidx] = col
                    # move to next vertex
                    cur = nxt
                    col = 5 - col  # toggle between 2 and 3
                    break
                else:
                    break
                # continue until back to start
                if cur == start:
                    break

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
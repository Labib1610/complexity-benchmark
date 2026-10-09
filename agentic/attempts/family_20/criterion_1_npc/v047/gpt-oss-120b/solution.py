import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    g = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        edges.append((u, v))
        g[u].append((v, idx))
        g[v].append((u, idx))

    # Edmonds' blossom algorithm for maximum matching
    N = n
    match = [-1]*N
    p = [-1]*N
    base = list(range(N))
    q = []
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

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal q, used, p, base, blossom
        used = [False]*N
        p = [-1]*N
        base = list(range(N))
        q = []
        q_head = 0
        q.append(root)
        used[root] = True
        while q_head < len(q):
            v = q[q_head]; q_head += 1
            for to, _ in g[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False]*N
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
                            if prev != -1:
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

    if sum(1 for x in match if x != -1)//2 != n//2:
        print("NO")
        return

    # assign colors
    color = [0]*m
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1

    # build graph of remaining edges (color 0)
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx]==0:
            adj[u].append((v, idx))
            adj[v].append((u, idx))

    visited_edge = [False]*m
    for start in range(n):
        for to, idx in adj[start]:
            if visited_edge[idx]:
                continue
            # traverse cycle
            cycle = []
            cur = start
            prev = -1
            while True:
                # find next edge not visited
                for nxt, eidx in adj[cur]:
                    if eidx==prev: continue
                    if not visited_edge[eidx]:
                        cycle.append(eidx)
                        visited_edge[eidx]=True
                        prev = eidx
                        cur = nxt
                        break
                else:
                    break
                if cur==start:
                    break
            # assign alternating 2,3
            for i, eidx in enumerate(cycle):
                color[eidx] = 2 if i%2==0 else 3

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
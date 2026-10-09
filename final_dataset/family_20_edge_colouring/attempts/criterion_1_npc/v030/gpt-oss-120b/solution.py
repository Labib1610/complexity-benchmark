import sys
sys.setrecursionlimit(10000)

def blossom_maximum_matching(n, edges):
    # implementation of Edmonds' blossom algorithm (Gabow)
    g = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        g[u].append((v, i))
        g[v].append((u, i))

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
        qi = 0
        while qi < len(q):
            v = q[qi]
            qi += 1
            for to, eid in g[v]:
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
                        return to
                    to_match = match[to]
                    if not used[to_match]:
                        used[to_match] = True
                        q.append(to_match)
        return -1

    for v in range(n):
        if match[v] == -1:
            to = find_path(v)
            if to != -1:
                # augment
                cur = to
                while cur != -1:
                    prev = p[cur]
                    nxt = match[prev] if prev != -1 else -1
                    match[cur] = prev
                    match[prev] = cur
                    cur = nxt
    return match

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        edges.append((u, v))
    # find perfect matching
    match = blossom_maximum_matching(n, edges)
    # check perfect
    if any(x == -1 for x in match):
        print("NO")
        return
    # assign colors
    color = [0]*m
    # map edge to index
    edge_id = {}
    for idx, (u,v) in enumerate(edges):
        edge_id[(u,v)] = idx
        edge_id[(v,u)] = idx
    # color 1 for matching edges
    for v in range(n):
        u = match[v]
        if v < u:
            idx = edge_id[(v,u)]
            color[idx] = 1
    # build remaining graph (degree 2)
    adj = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        if color[idx]==0:
            adj[u].append((v,idx))
            adj[v].append((u,idx))
    visited = [False]*n
    for start in range(n):
        if visited[start]:
            continue
        # traverse cycle
        cur = start
        prev = -1
        cyc = []
        while True:
            visited[cur]=True
            for to, eid in adj[cur]:
                if to!=prev:
                    cyc.append(eid)
                    prev, cur = cur, to
                    break
            else:
                break
            if cur==start:
                break
        # assign alternating colors 2 and3
        for i, eid in enumerate(cyc):
            color[eid] = 2 if i%2==0 else 3
    if any(c==0 for c in color):
        print("NO")
        return
    print("YES")
    print(' '.join(map(str,color)))

if __name__ == "__main__":
    main()
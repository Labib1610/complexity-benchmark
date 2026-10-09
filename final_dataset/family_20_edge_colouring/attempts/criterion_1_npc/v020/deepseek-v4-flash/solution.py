def lca(a, b, match, base, p, n):
    used = [False]*n
    while True:
        a = base[a]
        used[a] = True
        if match[a] == -1:
            break
        a = p[match[a]]
    while True:
        b = base[b]
        if used[b]:
            return b
        b = p[match[b]]

def mark_path(v, b, children, base, p, n):
    while base[v] != b:
        children[base[v]] = True
        v = p[match[v]]
        children[base[v]] = True

def find_path(root, n, adj, match, p, base, used, blossom):
    used = [False]*n
    p = [-1]*n
    base = list(range(n))
    q = [root]
    used[root] = True
    for v in q:
        for u in adj[v]:
            if base[v] == base[u] or match[v] == u:
                continue
            if u == root or (match[u] != -1 and p[match[u]] != -1):
                curbase = lca(v, u, match, base, p, n)
                blossom = [False]*n
                mark_path(v, curbase, blossom, base, p, n)
                mark_path(u, curbase, blossom, base, p, n)
                for i in range(n):
                    if blossom[base[i]]:
                        base[i] = curbase
                        if not used[i]:
                            used[i] = True
                            q.append(i)
            elif p[u] == -1:
                p[u] = v
                if match[u] == -1:
                    return u, p
                u = match[u]
                used[u] = True
                q.append(u)
    return -1, p

def max_matching(n, adj):
    match = [-1]*n
    p = [-1]*n
    base = list(range(n))
    used = [False]*n
    blossom = [False]*n
    for i in range(n):
        if match[i] == -1:
            v, p = find_path(i, n, adj, match, p, base, used, blossom)
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv
    return match
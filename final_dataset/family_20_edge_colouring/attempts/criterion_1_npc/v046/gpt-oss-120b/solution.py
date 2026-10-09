import sys
sys.setrecursionlimit(10000)

def blossom_max_matching(n, edges):
    # implementation based on emaxx.ru
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))

    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = []
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used_path = [False] * n
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
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
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
            ppv = match[pv] if pv != -1 else -1
            match[v] = pv
            match[pv] = v
            v = ppv

    for v in range(n):
        if match[v] == -1:
            finish = find_path(v)
            if finish != -1:
                augment_path(finish)

    return match

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    match = blossom_max_matching(n, edges)
    # check perfect matching
    if any(x == -1 for x in match):
        print("NO")
        return

    # build set of matched edge indices
    matched_idx = set()
    for i, j in enumerate(match):
        if i < j:
            # find edge index
            for idx, (u, v) in enumerate(edges):
                if (u == i and v == j) or (u == j and v == i):
                    matched_idx.add(idx)
                    break

    # color array
    color = [0] * m
    for idx in matched_idx:
        color[idx] = 1

    # remaining graph is 2-regular, build adjacency of remaining edges
    adj = [[] for _ in range(n)]
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        if idx in matched_idx:
            continue
        adj[u].append((v, idx))
        adj[v].append((u, idx))
        edge_id[(u, v)] = edge_id[(v, u)] = idx

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # traverse cycle
        cur = start
        prev = -1
        cyc_edges = []
        while True:
            visited[cur] = True
            # pick next edge not coming from prev
            nxt = None
            nxt_idx = None
            for to, idx in adj[cur]:
                if to != prev:
                    nxt = to
                    nxt_idx = idx
                    break
            if nxt is None:
                break
            cyc_edges.append(nxt_idx)
            prev, cur = cur, nxt
            if cur == start:
                break
        # color alternating 2,3
        for i, idx in enumerate(cyc_edges):
            color[idx] = 2 if i % 2 == 0 else 3

    print("YES")
    print(' '.join(str(c) for c in color))

if __name__ == "__main__":
    main()
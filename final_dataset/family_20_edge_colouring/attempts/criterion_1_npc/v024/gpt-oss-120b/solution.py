import sys
sys.setrecursionlimit(10000)

def blossom_maximum_matching(n, adj):
    """Edmonds' blossom algorithm, returns match list of size n (0‑based)."""
    INF = n + 5
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
        q = [root]
        used[root] = True
        head = 0
        while head < len(q):
            v = q[head]
            head += 1
            for to in adj[v]:
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
                        # augmenting path found
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

    for v in range(n):
        if match[v] == -1:
            find_path(v)
    return match

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
        adj[u].append(v)
        adj[v].append(u)

    match = blossom_maximum_matching(n, adj)
    if any(x == -1 for x in match):
        print("NO")
        return

    # build set of matched edges
    matched_edge = set()
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            matched_edge.add((v, u))

    colour = [0] * m
    # colour 1 for matching edges
    for idx, (u, v) in enumerate(edges):
        if (u, v) in matched_edge or (v, u) in matched_edge:
            colour[idx] = 1

    # build adjacency of remaining edges with edge ids
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if colour[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_edge = [False] * m
    for start in range(n):
        for (to, eid) in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the cycle
            cycle = []
            cur_v = start
            cur_e = eid
            while True:
                visited_edge[cur_e] = True
                cycle.append(cur_e)
                # move to the other vertex
                u, v = edges[cur_e]
                nxt_v = v if cur_v == u else u
                # find next edge (the other incident edge not used yet)
                nxt = None
                for (nbr, ne) in rem_adj[nxt_v]:
                    if not visited_edge[ne] and ne != cur_e:
                        nxt = (nbr, ne)
                        break
                if nxt is None:
                    break
                cur_v, cur_e = nxt_v, nxt[1]
                if cur_v == start:
                    break
            # colour alternately 2,3
            for i, e_id in enumerate(cycle):
                colour[e_id] = 2 if i % 2 == 0 else 3

    print("YES")
    print(' '.join(map(str, colour)))

if __name__ == "__main__":
    main()
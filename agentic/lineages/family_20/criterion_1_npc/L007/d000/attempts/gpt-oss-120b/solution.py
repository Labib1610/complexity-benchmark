import sys
sys.setrecursionlimit(10000)

def blossom_maximum_matching(n, adj):
    """Edmonds' blossom algorithm, returns list match where match[v] = partner or -1"""
    INF = n + 5
    match = [-1] * n
    p = [-1] * n          # parent in the forest
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
        nonlocal q, p, base, used, blossom
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

    # map each matched pair to its edge id
    edge_id = {}
    for i, (u, v) in enumerate(edges):
        edge_id[(u, v)] = i
        edge_id[(v, u)] = i

    colour = [0] * m
    in_match = [False] * m
    for v in range(n):
        u = match[v]
        if u > v:  # handle each pair once
            eid = edge_id[(v, u)]
            colour[eid] = 1
            in_match[eid] = True

    # build remaining adjacency with edge ids
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if not in_match[i]:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))

    visited_edge = [False] * m
    for start in range(n):
        # each vertex has exactly 2 remaining incident edges
        for (to, eid) in rem_adj[start]:
            if visited_edge[eid]:
                continue
            # walk the cycle
            cur = start
            cur_eid = eid
            cur_col = 2
            while True:
                visited_edge[cur_eid] = True
                colour[cur_eid] = cur_col
                # move to the other vertex of the edge
                nxt = edges[cur_eid][0] ^ edges[cur_eid][1] ^ cur
                # find the next edge (the one not equal to cur_eid)
                for (nbr, ne) in rem_adj[nxt]:
                    if not visited_edge[ne]:
                        cur = nxt
                        cur_eid = ne
                        cur_col = 5 - cur_col   # toggle between 2 and 3
                        break
                else:
                    break  # cycle finished
    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    main()
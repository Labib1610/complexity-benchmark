import sys
sys.setrecursionlimit(10000)

def blossom_maximum_matching(n, adj):
    # implementation of Edmonds' blossom algorithm (O(n^3))
    INF = n + 5
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
        adj[u].append(v)
        adj[v].append(u)

    match = blossom_maximum_matching(n, adj)
    if any(x == -1 for x in match):
        print("NO")
        return

    # colour array
    col = [0] * m
    # mark matching edges colour 1
    in_match = set()
    for v in range(n):
        u = match[v]
        if u != -1 and v < u:
            in_match.add((v, u))
    for i, (u, v) in enumerate(edges):
        if (u, v) in in_match or (v, u) in in_match:
            col[i] = 1

    # build graph of remaining edges (2-regular)
    rem_adj = [[] for _ in range(n)]
    edge_id = {}
    for i, (u, v) in enumerate(edges):
        if col[i] == 0:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))
            edge_id[(u, v)] = i
            edge_id[(v, u)] = i

    visited_edge = [False] * m
    for i in range(m):
        if col[i] != 0 or visited_edge[i]:
            continue
        # walk the cycle
        u, v = edges[i]
        cur = u
        prev = -1
        cur_edge = i
        cur_color = 2
        while True:
            visited_edge[cur_edge] = True
            col[cur_edge] = cur_color
            # move to the other vertex of the edge
            nxt = edges[cur_edge][0] ^ edges[cur_edge][1] ^ cur
            # find next edge in the cycle (the one not equal to cur_edge)
            for nb, eid in rem_adj[nxt]:
                if eid != cur_edge:
                    next_edge = eid
                    break
            cur = nxt
            cur_edge = next_edge
            cur_color = 5 - cur_color  # toggle between 2 and 3
            if visited_edge[cur_edge]:
                # close the cycle
                visited_edge[cur_edge] = True
                col[cur_edge] = cur_color
                break

    print("YES")
    print(' '.join(str(c) for c in col))

if __name__ == "__main__":
    solve()
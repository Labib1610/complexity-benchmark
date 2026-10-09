import sys
sys.setrecursionlimit(10000)

# ---------- Edmonds' blossom algorithm (CP‑Algorithms) ----------
def max_matching(n, adj):
    """return list match where match[v] = partner or -1"""
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

# -----------------------------------------------------------------

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

    match = max_matching(n, adj)
    if any(x == -1 for x in match):
        print("NO")
        return

    # build edge -> is in matching
    in_match = [False] * m
    # map unordered pair to edge index (there is at most one edge per pair)
    pair_to_idx = {}
    for i, (u, v) in enumerate(edges):
        pair_to_idx[(u, v)] = i
        pair_to_idx[(v, u)] = i

    for v in range(n):
        u = match[v]
        if u > v:  # handle each edge once
            idx = pair_to_idx[(v, u)]
            in_match[idx] = True

    colour = [0] * m
    for i, flag in enumerate(in_match):
        if flag:
            colour[i] = 1

    # build adjacency of non‑matching edges with edge indices
    non_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if not in_match[i]:
            non_adj[u].append((v, i))
            non_adj[v].append((u, i))

    visited_edge = [False] * m
    for start in range(n):
        # walk each cycle
        for (nbr, eid) in non_adj[start]:
            if visited_edge[eid]:
                continue
            # start new cycle
            cycle_edges = []
            cur = start
            prev = -1
            while True:
                # find the unused edge from cur not leading back to prev
                for (to, eidx) in non_adj[cur]:
                    if visited_edge[eidx]:
                        continue
                    if to == prev:
                        continue
                    # this is the next edge
                    cycle_edges.append(eidx)
                    visited_edge[eidx] = True
                    prev, cur = cur, to
                    break
                else:
                    break  # should not happen
                if cur == start:
                    break
            # colour alternately 2,3
            col = 2
            for eidx in cycle_edges:
                colour[eidx] = col
                col = 5 - col  # switch between 2 and 3

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    solve()
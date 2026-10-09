import sys
sys.setrecursionlimit(10000)

def blossom_maximum_matching(n, adj):
    """Edmonds' blossom algorithm, returns list match[v] = partner or -1."""
    INF = n + 5
    match = [-1] * n
    p = [-1] * n          # parent in the forest
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

    def mark_path(v, b, child):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = child
            child = match[v]
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
    edge_id = {}
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_id[(u, v)] = idx
        edge_id[(v, u)] = idx

    match = blossom_maximum_matching(n, adj)
    # build matching edge list
    matched_edges = []
    used = [False] * n
    for v in range(n):
        if match[v] != -1 and not used[v]:
            u = match[v]
            matched_edges.append((v, u))
            used[v] = used[u] = True

    if len(matched_edges) != n // 2:
        print("NO")
        return

    colour = [0] * m
    # colour matching edges with 1
    for u, v in matched_edges:
        eid = edge_id[(u, v)]
        colour[eid] = 1

    # process remaining edges (they form cycles)
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # walk the cycle starting from start using non‑matched edges
        cur = start
        prev = -1
        cycle_edges = []
        while True:
            visited[cur] = True
            # find the two incident non‑matched edges
            nxt = None
            for to in adj[cur]:
                if (cur, to) in edge_id:
                    eid = edge_id[(cur, to)]
                    if colour[eid] == 0:  # not in matching
                        if to != prev:
                            nxt = to
                            cycle_edges.append(eid)
                            break
            if nxt is None:
                break
            prev, cur = cur, nxt
            if cur == start:
                break

        # colour the collected cycle alternating 2,3
        col = 2
        for eid in cycle_edges:
            colour[eid] = col
            col = 5 - col   # switch between 2 and 3

    print("YES")
    print(' '.join(str(c) for c in colour))

if __name__ == "__main__":
    main()
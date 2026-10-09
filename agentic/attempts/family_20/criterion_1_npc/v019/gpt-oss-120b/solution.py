import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    adj = [[] for _ in range(n+1)]
    for idx in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # ---------- Edmonds' blossom algorithm ----------
    from collections import deque

    N = n
    g = [[] for _ in range(N+1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    match = [0]*(N+1)
    p = [0]*(N+1)
    base = list(range(N+1))
    q = deque()
    used = [False]*(N+1)
    blossom = [False]*(N+1)

    def lca(a, b):
        used_path = [False]*(N+1)
        while True:
            a = base[a]
            used_path[a] = True
            if match[a]==0: break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, children):
        while base[v]!=b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal used, p, base, q, blossom
        used = [False]*(N+1)
        p = [0]*(N+1)
        for i in range(N+1):
            base[i]=i
        q.clear()
        q.append(root)
        used[root]=True
        while q:
            v = q.popleft()
            for to in g[v]:
                if base[v]==base[to] or match[v]==to:
                    continue
                if to==root or (match[to]!=0 and p[match[to]]!=0):
                    cur = lca(v, to)
                    blossom = [False]*(N+1)
                    mark_path(v, cur, to)
                    mark_path(to, cur, v)
                    for i in range(1,N+1):
                        if blossom[base[i]]:
                            base[i]=cur
                            if not used[i]:
                                used[i]=True
                                q.append(i)
                elif p[to]==0:
                    p[to]=v
                    if match[to]==0:
                        # augmenting
                        v=to
                        while v!=0:
                            pv = p[v]
                            ppv = match[pv]
                            match[v]=pv
                            match[pv]=v
                            v=ppv
                        return True
                    else:
                        used[match[to]]=True
                        q.append(match[to])
        return False

    for v in range(1,N+1):
        if match[v]==0:
            find_path(v)

    # --------------------------------------------------

    if any(match[i]==0 for i in range(1, n+1)):
        print("NO")
        return

    color = [0]*m
    # assign color 1 to matching edges
    edge_id_map = {}
    for idx, (u, v) in enumerate(edges):
        edge_id_map[(u, v)] = edge_id_map[(v, u)] = idx

    for v in range(1, n+1):
        u = match[v]
        if v < u:
            idx = edge_id_map[(v, u)]
            color[idx] = 1

    # remaining edges form degree-2 graph
    visited_edge = [False]*m
    for idx, c in enumerate(color):
        if c==1:
            visited_edge[idx]=True

    for start in range(m):
        if visited_edge[start]:
            continue
        # start a cycle
        u, v = edges[start]
        cur = start
        cur_u = u
        cur_v = v
        seq = []
        while True:
            visited_edge[cur]=True
            seq.append((cur, cur_u, cur_v))
            # move to next edge from cur_v not visited
            nxt = None
            for nb, eid in adj[cur_v]:
                if not visited_edge[eid]:
                    nxt = (nb, eid)
                    break
            if nxt is None:
                break
            nxt_v, nxt_eid = nxt
            # next edge goes from cur_v to nxt_v
            cur_u, cur_v = cur_v, nxt_v
            cur = nxt_eid
        # assign alternating colors 2,3
        col = 2
        for eid, _, _ in seq:
            color[eid]=col
            col = 5 - col  # toggle between 2 and 3

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
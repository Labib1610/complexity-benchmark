import sys
import random
sys.setrecursionlimit(10000)

def blossom_max_matching(n, adj):
    # Edmonds' blossom algorithm for maximum matching in general graph
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

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # Build adjacency list for blossom (undirected)
    blossom_adj = adj

    # Try multiple random permutations to find suitable perfect matching
    for _ in range(30):
        order = list(range(n))
        random.shuffle(order)
        # relabel vertices according to order to possibly affect matching
        inv = [0]*n
        for i, v in enumerate(order):
            inv[v]=i
        rel_adj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                rel_adj[inv[u]].append(inv[v])
        match = blossom_max_matching(n, rel_adj)
        # translate back
        match_orig = [-1]*n
        for i in range(n):
            if match[i]!=-1:
                match_orig[order[i]] = order[match[i]]
        # check perfect
        if any(x==-1 for x in match_orig):
            continue
        # edges in matching
        in_match = set()
        for u in range(n):
            v = match_orig[u]
            if u < v:
                in_match.add((u,v))
        # build 2-factor of remaining edges
        used = [False]*m
        color = [0]*m
        # assign color 1 to matching edges
        for idx,(u,v) in enumerate(edges):
            if (u,v) in in_match or (v,u) in in_match:
                color[idx]=1
                used[idx]=True
        # build adjacency of remaining graph
        rem_adj = [[] for _ in range(n)]
        edge_id = {}
        for idx,(u,v) in enumerate(edges):
            if not used[idx]:
                rem_adj[u].append((v,idx))
                rem_adj[v].append((u,idx))
                edge_id[(u,v)] = idx
                edge_id[(v,u)] = idx
        ok = True
        # each component is a cycle
        for start in range(n):
            for (nbr, eid) in rem_adj[start]:
                if color[eid]==0:
                    # traverse cycle
                    cur = start
                    prev = -1
                    cur_color = 2
                    while True:
                        # find edge not used yet from cur
                        for (to, eid2) in rem_adj[cur]:
                            if color[eid2]==0:
                                # take this edge
                                color[eid2]=cur_color
                                cur_color = 5 - cur_color  # toggle between 2 and3
                                prev = cur
                                cur = to
                                break
                        else:
                            ok=False
                            break
                        if cur==start:
                            break
                    if not ok:
                        break
            if not ok:
                break
        if ok and all(c!=0 for c in color):
            print("YES")
            print(' '.join(map(str,color)))
            return
    print("NO")

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(1000000)

def find_perfect_matching(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Blossom algorithm for maximum matching
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    q = []
    used = [False] * n
    blossom = [False] * n
    
    def lca(a, b):
        used_lca = [False] * n
        while True:
            a = base[a]
            used_lca[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_lca[b]:
                return b
            b = p[match[b]]
    
    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]
    
    def find_path(root):
        nonlocal p, base, used, q, blossom
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
        q = [root]
        used[root] = True
        for qi in range(len(q)):
            v = q[qi]
            for to, _ in adj[v]:
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
                    to = match[to]
                    used[to] = True
                    q.append(to)
        return -1
    
    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv
    
    # Check perfect
    if all(m != -1 for m in match):
        matching_edges = []
        for u in range(n):
            if u < match[u]:
                # find edge index
                for to, idx in adj[u]:
                    if to == match[u]:
                        matching_edges.append(idx)
                        break
        return matching_edges
    else:
        return None

def solve():
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
    
    # Check if graph is cubic
    deg = [0]*n
    for u,v in edges:
        deg[u]+=1
        deg[v]+=1
    if any(d != 3 for d in deg):
        print("NO")
        return
    
    # Find perfect matching for color 1
    match_edges = find_perfect_matching(n, edges)
    if match_edges is None:
        print("NO")
        return
    
    color = [0]*m
    for idx in match_edges:
        color[idx] = 1
    
    # Remaining edges form cycles
    # Build adjacency for remaining edges
    adj_rem = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        if color[idx] == 0:
            adj_rem[u].append((v, idx))
            adj_rem[v].append((u, idx))
    
    visited = [False]*n
    for i in range(n):
        if not visited[i] and adj_rem[i]:
            # traverse cycle
            cycle_edges = []
            start = i
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                # pick next
                nxt = None
                nxt_idx = None
                for to, idx in adj_rem[cur]:
                    if to != prev:
                        nxt = to
                        nxt_idx = idx
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt_idx)
                prev, cur = cur, nxt
                if cur == start:
                    break
            # color cycle alternately 2,3
            for k, idx in enumerate(cycle_edges):
                color[idx] = 2 if k % 2 == 0 else 3
    
    # Check all colored
    if any(c == 0 for c in color):
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(1000000)

def find_perfect_matching(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Blossom algorithm for maximum matching
    # Standard implementation
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
        nonlocal p, base, used, blossom, q
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = [root]
        used[root] = True
        for v in q:
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
    
    # Check if perfect
    if all(m != -1 for m in match):
        matching_edges = []
        for u in range(n):
            if u < match[u]:
                matching_edges.append((u, match[u]))
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
    
    # Check degree
    deg = [0]*n
    for u,v in edges:
        deg[u] += 1
        deg[v] += 1
    if any(d != 3 for d in deg):
        print("NO")
        return
    
    # Find perfect matching
    matching = find_perfect_matching(n, edges)
    if matching is None:
        print("NO")
        return
    
    # Build edge index map
    edge_idx = {}
    for idx, (u,v) in enumerate(edges):
        edge_idx[(u,v)] = idx
        edge_idx[(v,u)] = idx
    
    # Color assignment
    color = [0]*m
    # Mark matching edges with color 3
    match_set = set()
    for u,v in matching:
        match_set.add((u,v))
        match_set.add((v,u))
        color[edge_idx[(u,v)]] = 3
    
    # Build remaining graph (degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        if (u,v) not in match_set:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))
    
    # Color cycles with 1 and 2
    visited = [False]*n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cur = start
            prev = -1
            while True:
                visited[cur] = True
                # find next
                nxt = -1
                nxt_idx = -1
                for to, idx in rem_adj[cur]:
                    if to != prev:
                        nxt = to
                        nxt_idx = idx
                        break
                if nxt == -1:
                    break
                # color edge
                # Determine color: alternate
                # We'll color based on parity of step
                # We'll do BFS/DFS with alternating
                # Simpler: traverse and assign alternating
                # We'll do a simple loop
                # Actually we need to assign colors along cycle
                # We'll do a DFS
                pass
    
    # Better: traverse each cycle and color alternately
    visited = [False]*n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # find cycle
            cycle_edges = []
            cur = start
            prev = -1
            while True:
                visited[cur] = True
                # find next unvisited or back to start
                nxt = -1
                nxt_idx = -1
                for to, idx in rem_adj[cur]:
                    if to != prev:
                        nxt = to
                        nxt_idx = idx
                        break
                if nxt == -1:
                    break
                cycle_edges.append(nxt_idx)
                prev, cur = cur, nxt
                if cur == start:
                    break
            # color alternately
            for i, idx in enumerate(cycle_edges):
                color[idx] = 1 if i % 2 == 0 else 2
    
    # Check if all colored
    if any(c == 0 for c in color):
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()
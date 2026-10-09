import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj):
    # Tarjan's algorithm
    visited = [False]*n
    tin = [-1]*n
    low = [-1]*n
    timer = 0
    bridges = set()
    def dfs(v, p):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

# Edmonds' Blossom algorithm for maximum matching
def max_matching(n, adj):
    # adj: list of lists of neighbors
    match = [-1]*n
    p = [-1]*n
    base = [-1]*n
    used = [False]*n
    blossom = [False]*n
    from collections import deque

    def lca(a, b):
        used_lca = [False]*n
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
        nonlocal p, base, used, blossom
        used = [False]*n
        p = [-1]*n
        for i in range(n):
            base[i] = i
        q = deque([root])
        used[root] = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False]*n
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
    return match

def solve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for eid in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append((v, eid))
        adj[v].append((u, eid))
        edges.append((u, v))
    
    # Check bridges
    bridges = find_bridges(n, adj)
    if bridges:
        print("NO")
        return
    
    # Build adjacency list for matching (just neighbors)
    adj_match = [[] for _ in range(n)]
    for u, v in edges:
        adj_match[u].append(v)
        adj_match[v].append(u)
    
    match = max_matching(n, adj_match)
    
    # Check perfect matching
    if any(match[i] == -1 for i in range(n)):
        print("NO")
        return
    
    # Color edges
    color = [0]*m
    # Matching edges get color 3
    for eid, (u, v) in enumerate(edges):
        if match[u] == v:
            color[eid] = 3
    
    # Build graph of non-matching edges
    adj_rem = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == 0:
            adj_rem[u].append((v, eid))
            adj_rem[v].append((u, eid))
    
    # Color cycles with 1 and 2
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            # find cycle
            stack = [(i, -1, -1)]  # node, parent, parent_edge
            cycle_edges = []
            nodes = []
            while stack:
                v, p, pe = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                nodes.append(v)
                if pe != -1:
                    cycle_edges.append(pe)
                for to, eid in adj_rem[v]:
                    if to == p:
                        continue
                    stack.append((to, v, eid))
            # Now color cycle edges alternately
            # We need to traverse the cycle properly
            # Since it's 2-regular, each node has degree 2 in adj_rem
            # Find start
            start = nodes[0]
            # Walk
            prev = -1
            cur = start
            first_edge = -1
            edge_list = []
            while True:
                # find next neighbor not prev
                nxt = -1
                ne = -1
                for to, eid in adj_rem[cur]:
                    if to != prev:
                        nxt = to
                        ne = eid
                        break
                if nxt == -1:
                    break
                edge_list.append(ne)
                if first_edge == -1:
                    first_edge = ne
                prev, cur = cur, nxt
                if cur == start:
                    break
            # Now color alternately
            c = 1
            for eid in edge_list:
                color[eid] = c
                c = 3 - c  # toggle 1<->2
    # Output
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
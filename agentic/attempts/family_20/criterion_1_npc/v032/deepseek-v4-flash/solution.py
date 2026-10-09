import sys
sys.setrecursionlimit(10000)

def find_3_edge_coloring(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Check degree
    for i in range(n):
        if len(adj[i]) != 3:
            return None
    
    # Blossom algorithm for maximum matching
    # We'll implement Edmonds' Blossom algorithm
    # Returns a list of matched edges (u,v) or None if no perfect matching
    
    # Implementation of Blossom for general graph
    # Based on standard O(n^3) implementation
    
    n_vertices = n
    # We'll store graph as adjacency list of vertices
    graph = [[] for _ in range(n_vertices)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Blossom algorithm
    match = [-1] * n_vertices
    p = [-1] * n_vertices
    base = list(range(n_vertices))
    q = []
    used = [False] * n_vertices
    blossom = [False] * n_vertices
    
    def lca(a, b):
        used_lca = [False] * n_vertices
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
        nonlocal used, p, base, q, blossom
        used = [False] * n_vertices
        p = [-1] * n_vertices
        base = list(range(n_vertices))
        q = [root]
        used[root] = True
        for qi in range(len(q)):
            v = q[qi]
            for u in graph[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != -1 and p[match[u]] != -1):
                    curbase = lca(v, u)
                    blossom = [False] * n_vertices
                    mark_path(v, curbase, u)
                    mark_path(u, curbase, v)
                    for i in range(n_vertices):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[u] == -1:
                    p[u] = v
                    if match[u] == -1:
                        return u
                    u = match[u]
                    used[u] = True
                    q.append(u)
        return -1
    
    def augment(v):
        while v != -1:
            pv = p[v]
            nv = match[pv]
            match[v] = pv
            match[pv] = v
            v = nv
    
    for i in range(n_vertices):
        if match[i] == -1:
            v = find_path(i)
            if v != -1:
                augment(v)
    
    # Check perfect matching
    for i in range(n_vertices):
        if match[i] == -1:
            return None
    
    # Build matching edge list
    matching_edges = []
    for u in range(n_vertices):
        v = match[u]
        if u < v:
            matching_edges.append((u, v))
    
    # Remove matching edges, remaining graph is 2-regular (cycles)
    # Build adjacency for remaining graph
    rem_adj = [[] for _ in range(n_vertices)]
    for u, v in edges:
        if match[u] != v:  # not a matching edge
            rem_adj[u].append(v)
            rem_adj[v].append(u)
    
    # Color the cycles with 1 and 2
    color = [-1] * len(edges)
    # Map edge index to color
    edge_index = {}
    for idx, (u, v) in enumerate(edges):
        edge_index[(u, v)] = idx
        edge_index[(v, u)] = idx
    
    # Color matching edges with 3
    for u, v in matching_edges:
        color[edge_index[(u, v)]] = 3
    
    # Color cycles
    visited = [False] * n_vertices
    for i in range(n_vertices):
        if not visited[i] and len(rem_adj[i]) > 0:
            # traverse cycle
            cycle_vertices = []
            cur = i
            prev = -1
            while True:
                visited[cur] = True
                cycle_vertices.append(cur)
                # find next
                nxt = -1
                for nb in rem_adj[cur]:
                    if nb != prev:
                        nxt = nb
                        break
                if nxt == -1:
                    break
                prev, cur = cur, nxt
                if cur == i:
                    break
            # color edges alternately
            for j in range(len(cycle_vertices)):
                u = cycle_vertices[j]
                v = cycle_vertices[(j+1) % len(cycle_vertices)]
                if (u, v) in edge_index:
                    color[edge_index[(u, v)]] = 1 if j % 2 == 0 else 2
                else:
                    color[edge_index[(v, u)]] = 1 if j % 2 == 0 else 2
    
    return color

def main():
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
    
    color = find_3_edge_coloring(n, edges)
    if color is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    main()
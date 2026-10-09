import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check degree 3
    for v in range(1, n + 1):
        if len(adj[v]) != 3:
            print("NO")
            return
    
    # Build adjacency with edge indices
    adj_set = [set() for _ in range(n + 1)]
    for v in range(1, n + 1):
        for u, e in adj[v]:
            adj_set[v].add(u)
    
    # Find triangles
    triangles = []
    in_triangle = [False] * (n + 1)
    edge_in_triangle = [False] * m
    
    for i in range(m):
        u, v = edges[i]
        common = adj_set[u] & adj_set[v]
        for w in common:
            if w > v:
                # Triangle u-v-w
                triangles.append((u, v, w))
                in_triangle[u] = True
                in_triangle[v] = True
                in_triangle[w] = True
                edge_in_triangle[i] = True
                # Find edges v-w and u-w
                for u2, e2 in adj[v]:
                    if u2 == w:
                        edge_in_triangle[e2] = True
                        break
                for u2, e2 in adj[u]:
                    if u2 == w:
                        edge_in_triangle[e2] = True
                        break
    
    # Build contracted graph
    # Nodes: original vertices not in triangle + triangle supernodes
    # Map triangle to supernode id
    tri_to_node = {}
    node_list = []
    for v in range(1, n + 1):
        if not in_triangle[v]:
            node_list.append(v)
    
    for idx, (a, b, c) in enumerate(triangles):
        sid = n + 1 + idx
        tri_to_node[(a, b, c)] = sid
        node_list.append(sid)
    
    # Build adjacency for contracted graph
    contracted_adj = [[] for _ in range(n + 1 + len(triangles))]
    contracted_edges = []  # (u, v, original_edge_idx)
    
    for i in range(m):
        if edge_in_triangle[i]:
            continue
        u, v = edges[i]
        # Find which supernode u and v belong to
        su = u
        sv = v
        for idx, (a, b, c) in enumerate(triangles):
            sid = n + 1 + idx
            if u == a or u == b or u == c:
                su = sid
            if v == a or v == b or v == c:
                sv = sid
        if su != sv:
            contracted_adj[su].append((sv, i))
            contracted_adj[sv].append((su, i))
            contracted_edges.append((su, sv, i))
    
    # Check if contracted graph is bipartite
    color = [0] * (n + 1 + len(triangles))
    visited = [False] * (n + 1 + len(triangles))
    
    for start in node_list:
        if not visited[start]:
            stack = [start]
            visited[start] = True
            color[start] = 1
            while stack:
                u = stack.pop()
                for v, e in contracted_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Assign colors
    ans = [0] * m
    
    # Triangle edges: assign 1, 2, 3
    for idx, (a, b, c) in enumerate(triangles):
        # Find the three edges
        e_ab = e_bc = e_ca = -1
        for u, e in adj[a]:
            if u == b:
                e_ab = e
            elif u == c:
                e_ca = e
        for u, e in adj[b]:
            if u == c:
                e_bc = e
        ans[e_ab] = 1
        ans[e_bc] = 2
        ans[e_ca] = 3
    
    # Non-triangle edges: assign based on color
    for i in range(m):
        if not edge_in_triangle[i]:
            u, v = edges[i]
            su = u
            sv = v
            for idx, (a, b, c) in enumerate(triangles):
                sid = n + 1 + idx
                if u == a or u == b or u == c:
                    su = sid
                if v == a or v == b or v == c:
                    sv = sid
            # Color is 1 or 2, assign that
            ans[i] = color[su]
    
    print("YES")
    print(' '.join(map(str, ans)))

solve()
import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
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
    
    # Check if 3-regular
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Find cycles
    cycle_edges = set()
    visited = [False] * (n + 1)
    parent = [(-1, -1)] * (n + 1)  # (parent_node, edge_index)
    
    stack = [(1, -1, -1)]  # (node, parent_node, edge_index)
    found_cycle = False
    
    while stack and not found_cycle:
        u, p, ei = stack.pop()
        if visited[u]:
            # Found cycle
            # Backtrack from u and p to find cycle
            path_u = []
            path_p = []
            node = u
            while node != -1:
                path_u.append(node)
                node = parent[node][0]
            node = p
            while node != -1:
                path_p.append(node)
                node = parent[node][0]
            # Find LCA
            path_u.reverse()
            path_p.reverse()
            i = 0
            while i < len(path_u) and i < len(path_p) and path_u[i] == path_p[i]:
                i += 1
            lca = path_u[i-1]
            # Collect cycle edges
            node = u
            while node != lca:
                cycle_edges.add(parent[node][1])
                node = parent[node][0]
            node = p
            while node != lca:
                cycle_edges.add(parent[node][1])
                node = parent[node][0]
            cycle_edges.add(ei)
            found_cycle = True
            break
        visited[u] = True
        parent[u] = (p, ei)
        for v, idx in adj[u]:
            if idx == ei:
                continue
            if not visited[v]:
                stack.append((v, u, idx))
            elif v != p:
                # Found cycle
                path_u = []
                path_p = []
                node = u
                while node != -1:
                    path_u.append(node)
                    node = parent[node][0]
                node = v
                while node != -1:
                    path_p.append(node)
                    node = parent[node][0]
                path_u.reverse()
                path_p.reverse()
                i = 0
                while i < len(path_u) and i < len(path_p) and path_u[i] == path_p[i]:
                    i += 1
                lca = path_u[i-1]
                node = u
                while node != lca:
                    cycle_edges.add(parent[node][1])
                    node = parent[node][0]
                node = v
                while node != lca:
                    cycle_edges.add(parent[node][1])
                    node = parent[node][0]
                cycle_edges.add(idx)
                found_cycle = True
                break
        if found_cycle:
            break
    
    # Build tree edges
    tree_edges = set(range(m)) - cycle_edges
    
    # Assign colors to tree edges (bipartite)
    color = [0] * m
    visited = [False] * (n + 1)
    
    # BFS from node 1
    queue = [1]
    visited[1] = True
    while queue:
        u = queue.pop(0)
        for v, idx in adj[u]:
            if idx in tree_edges and not visited[v]:
                visited[v] = True
                color[idx] = color[idx] if color[idx] != 0 else 1
                # Determine color based on parity
                # Actually we need to track depth
                pass
    
    # Better approach: track depth
    depth = [-1] * (n + 1)
    depth[1] = 0
    queue = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    while queue:
        u = queue.pop(0)
        for v, idx in adj[u]:
            if idx in tree_edges:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    queue.append(v)
    
    for idx in tree_edges:
        u, v = edges[idx]
        if depth[u] > depth[v]:
            u, v = v, u
        # u is parent of v
        color[idx] = 1 if depth[v] % 2 == 1 else 2
    
    # Assign colors to cycle edges
    # Build cycle as list of edges
    cycle_list = list(cycle_edges)
    
    # Build adjacency within cycle
    cycle_adj = [[] for _ in range(n + 1)]
    for idx in cycle_list:
        u, v = edges[idx]
        cycle_adj[u].append((v, idx))
        cycle_adj[v].append((u, idx))
    
    # Find cycle path
    start = -1
    for idx in cycle_list:
        u, v = edges[idx]
        if len(cycle_adj[u]) == 2:
            start = u
            break
        if len(cycle_adj[v]) == 2:
            start = v
            break
    
    # Traverse cycle
    cycle_path = []
    visited_edge = set()
    curr = start
    prev = -1
    while len(visited_edge) < len(cycle_list):
        for nxt, idx in cycle_adj[curr]:
            if idx not in visited_edge and nxt != prev:
                cycle_path.append(idx)
                visited_edge.add(idx)
                prev = curr
                curr = nxt
                break
    
    # Assign colors to cycle
    L = len(cycle_path)
    for i, idx in enumerate(cycle_path):
        color[idx] = 1 if i % 2 == 0 else 2
    
    # Check if cycle length is odd
    if L % 2 == 1:
        # Need to use color 3
        # Find an edge in cycle that can be changed to 3
        # Check constraints at its endpoints
        for i, idx in enumerate(cycle_path):
            u, v = edges[idx]
            # Check if we can change this edge to 3
            # Get colors of other edges at u and v
            colors_u = set()
            colors_v = set()
            for w, j in adj[u]:
                if j != idx:
                    colors_u.add(color[j])
            for w, j in adj[v]:
                if j != idx:
                    colors_v.add(color[j])
            if 3 not in colors_u and 3 not in colors_v:
                color[idx] = 3
                break
        else:
            # Try changing a tree edge to 3
            for idx in tree_edges:
                u, v = edges[idx]
                colors_u = set()
                colors_v = set()
                for w, j in adj[u]:
                    if j != idx:
                        colors_u.add(color[j])
                for w, j in adj[v]:
                    if j != idx:
                        colors_v.add(color[j])
                if 3 not in colors_u and 3 not in colors_v:
                    color[idx] = 3
                    break
            else:
                print("NO")
                return
    
    # Verify solution
    for u in range(1, n + 1):
        colors = set()
        for v, idx in adj[u]:
            colors.add(color[idx])
        if len(colors) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()
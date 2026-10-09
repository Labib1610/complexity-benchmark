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
    
    # Check degree
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    # Check bipartite
    color = [0] * (n + 1)
    is_bipartite = True
    stack = []
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack.append(start)
            while stack:
                u = stack.pop()
                for v, _ in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if is_bipartite:
        print("NO")
        return
    
    # Find odd cycle
    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    visited = [False] * (n + 1)
    cycle_nodes = []
    cycle_edges = []
    
    stack = [(1, 0, -1, -1)]
    found = False
    
    while stack and not found:
        u, state, p, pe = stack.pop()
        if state == 0:
            if visited[u]:
                continue
            visited[u] = True
            parent[u] = p
            parent_edge[u] = pe
            stack.append((u, 1, p, pe))
            for v, eid in adj[u]:
                if not found:
                    if not visited[v]:
                        stack.append((v, 0, u, eid))
                    elif v != p:
                        # Found cycle
                        cycle_nodes.append(u)
                        cycle_edges.append(eid)
                        curr = u
                        while curr != v:
                            cycle_nodes.append(parent[curr])
                            cycle_edges.append(parent_edge[curr])
                            curr = parent[curr]
                        found = True
        else:
            pass
    
    L = len(cycle_nodes)
    
    # Assign phases to cycle edges
    edge_phase = [0] * m
    for i in range(L):
        edge_phase[cycle_edges[i]] = (i % 3) + 1
    
    # Process remaining edges
    processed = [False] * (n + 1)
    for node in cycle_nodes:
        processed[node] = True
    
    queue = list(cycle_nodes)
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        used = set()
        for v, eid in adj[u]:
            if edge_phase[eid] != 0:
                used.add(edge_phase[eid])
        for v, eid in adj[u]:
            if edge_phase[eid] == 0:
                for ph in range(1, 4):
                    if ph not in used:
                        edge_phase[eid] = ph
                        used.add(ph)
                        if not processed[v]:
                            processed[v] = True
                            queue.append(v)
                        break
    
    print("YES")
    print(' '.join(map(str, edge_phase)))

solve()
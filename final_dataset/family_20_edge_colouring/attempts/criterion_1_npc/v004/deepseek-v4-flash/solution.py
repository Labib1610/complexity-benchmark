import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj, edges):
    # Tarjan's algorithm for bridges
    visited = [False] * (n+1)
    tin = [-1] * (n+1)
    low = [-1] * (n+1)
    timer = 0
    bridges = set()

    def dfs(v, p_edge):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def find_perfect_matching(n, adj, edges):
    # For cubic graph, we can find a perfect matching via simple augmenting path
    # We'll use a simple greedy + augmenting path (Kuhn's algorithm style)
    match_to = [0] * (n+1)  # matched vertex for each vertex
    adj_list = [[] for _ in range(n+1)]
    for idx, (u, v) in enumerate(edges):
        adj_list[u].append(v)
        adj_list[v].append(u)

    def try_kuhn(v, visited):
        for to in adj_list[v]:
            if visited[to]:
                continue
            visited[to] = True
            if match_to[to] == 0 or try_kuhn(match_to[to], visited):
                match_to[to] = v
                match_to[v] = to
                return True
        return False

    for v in range(1, n+1):
        if match_to[v] == 0:
            visited = [False] * (n+1)
            try_kuhn(v, visited)

    # Build matching edge ids
    matching_edges = []
    used = [False] * (n+1)
    for u, v in edges:
        if match_to[u] == v and not used[u] and not used[v]:
            matching_edges.append((u, v))
            used[u] = used[v] = True
    return matching_edges

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n+1)]
    for eid in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check bridges
    bridges = find_bridges(n, adj, edges)
    if bridges:
        print("NO")
        return

    # Find perfect matching
    matching_edges = find_perfect_matching(n, adj, edges)
    if len(matching_edges) != n // 2:
        print("NO")
        return

    # Color matching edges with 3
    color = [0] * m
    match_edge_ids = set()
    for u, v in matching_edges:
        # find edge id
        for eid, (a, b) in enumerate(edges):
            if (a == u and b == v) or (a == v and b == u):
                color[eid] = 3
                match_edge_ids.add(eid)
                break

    # Build graph without matching edges
    adj2 = [[] for _ in range(n+1)]
    for eid, (u, v) in enumerate(edges):
        if eid in match_edge_ids:
            continue
        adj2[u].append((v, eid))
        adj2[v].append((u, eid))

    # Color remaining cycles with 1 and 2
    visited = [False] * (n+1)
    for start in range(1, n+1):
        if not visited[start]:
            # find cycle
            cycle_edges = []
            stack = [(start, -1)]
            parent = {start: -1}
            while stack:
                v, pe = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                for to, eid in adj2[v]:
                    if eid == pe:
                        continue
                    if not visited[to]:
                        parent[to] = (v, eid)
                        stack.append((to, eid))
                    else:
                        # found cycle
                        # reconstruct
                        cycle_edges = []
                        cur = v
                        while cur != to:
                            pv, pe = parent[cur]
                            cycle_edges.append(pe)
                            cur = pv
                        cycle_edges.append(eid)
                        break
                if cycle_edges:
                    break
            if not cycle_edges:
                continue
            # color cycle alternately 1,2
            for i, eid in enumerate(cycle_edges):
                color[eid] = 1 if i % 2 == 0 else 2

    # Check if all colored
    if any(c == 0 for c in color):
        print("NO")
        return

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()
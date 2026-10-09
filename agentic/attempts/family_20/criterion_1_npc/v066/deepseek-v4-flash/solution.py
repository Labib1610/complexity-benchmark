import sys
sys.setrecursionlimit(1000000)

def find_perfect_matching(n, adj, edge_id):
    # Simple DFS-based matching for cubic bridgeless graph
    match_to = [-1] * n
    used = [False] * n

    def dfs(u):
        for v, eid in adj[u]:
            if used[v]:
                continue
            used[v] = True
            if match_to[v] == -1 or dfs(match_to[v]):
                match_to[v] = u
                match_to[u] = v
                return True
        return False

    for u in range(n):
        used = [False] * n
        dfs(u)

    # Build matching edge list
    matching_edges = []
    seen = [False] * n
    for u in range(n):
        if not seen[u] and match_to[u] != -1:
            v = match_to[u]
            seen[u] = seen[v] = True
            # find edge id
            for w, eid in adj[u]:
                if w == v:
                    matching_edges.append(eid)
                    break
    return matching_edges

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    edges = []
    for eid in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check if graph is connected
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        u = stack.pop()
        for v, _ in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    if not all(visited):
        print("NO")
        return

    # Check for bridges using Tarjan
    tin = [-1] * n
    low = [-1] * n
    timer = [0]
    has_bridge = [False]

    def dfs_bridge(u, p_edge):
        tin[u] = low[u] = timer[0]
        timer[0] += 1
        for v, eid in adj[u]:
            if eid == p_edge:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs_bridge(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    has_bridge[0] = True

    dfs_bridge(0, -1)
    if has_bridge[0]:
        print("NO")
        return

    # Find perfect matching
    matching_edges = find_perfect_matching(n, adj, None)
    if len(matching_edges) != n // 2:
        print("NO")
        return

    color = [0] * m
    for eid in matching_edges:
        color[eid] = 1

    # Remaining graph: cycles, color alternately 2 and 3
    remaining_adj = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == 0:
            remaining_adj[u].append((v, eid))
            remaining_adj[v].append((u, eid))

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # find cycle
        cycle_edges = []
        # walk
        u = start
        prev = -1
        while True:
            visited[u] = True
            # pick next unvisited neighbor
            nxt = None
            for v, eid in remaining_adj[u]:
                if eid != prev:
                    nxt = (v, eid)
                    break
            if nxt is None:
                break
            v, eid = nxt
            cycle_edges.append(eid)
            prev = eid
            u = v
            if u == start:
                break
        # color alternately
        for i, eid in enumerate(cycle_edges):
            color[eid] = 2 if i % 2 == 0 else 3

    # Verify
    for u in range(n):
        cols = set()
        for v, eid in adj[u]:
            cols.add(color[eid])
        if len(cols) != 3:
            print("NO")
            return

    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()
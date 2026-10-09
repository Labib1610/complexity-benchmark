import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, edges, adj):
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
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
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def edge_color_cubic(n, edges, adj):
    # We'll use a constructive method: find a perfect matching, remove it,
    # the remaining graph is 2-regular (disjoint cycles), color those with 2 colors.
    # Repeat for 3 colors.
    color = [0] * len(edges)
    remaining_edges = list(range(len(edges)))
    adj_rem = [list(adj[i]) for i in range(n + 1)]

    for col in (1, 2, 3):
        # Find a perfect matching in the remaining graph
        match = [-1] * (n + 1)
        # Simple greedy matching (works for bridgeless cubic graphs if we use proper algorithm,
        # but here we can use a known fact: every bridgeless cubic graph has a perfect matching.
        # We'll use a simple DFS-based augmenting path to find perfect matching.
        def try_kuhn(v, visited):
            for to, eid in adj_rem[v]:
                if eid not in remaining_set:
                    continue
                if visited[to]:
                    continue
                visited[to] = True
                if match[to] == -1 or try_kuhn(match[to], visited):
                    match[to] = v
                    return True
            return False

        remaining_set = set(remaining_edges)
        for v in range(1, n + 1):
            visited = [False] * (n + 1)
            try_kuhn(v, visited)

        # Now match contains pairs; assign color
        used_edges = set()
        for v in range(1, n + 1):
            if match[v] != -1 and v < match[v]:
                # find edge id between v and match[v]
                for to, eid in adj[v]:
                    if to == match[v]:
                        color[eid] = col
                        used_edges.add(eid)
                        break
        # Remove matched edges from remaining
        remaining_edges = [e for e in remaining_edges if e not in used_edges]
        # Rebuild adj_rem without used edges
        adj_rem = [[] for _ in range(n + 1)]
        for eid in remaining_edges:
            u, v = edges[eid]
            adj_rem[u].append((v, eid))
            adj_rem[v].append((u, eid))

    return color

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for eid in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))
        deg[u] += 1
        deg[v] += 1

    # Check cubic
    if any(d != 3 for d in deg[1:]):
        print("NO")
        return

    # Check bridges
    bridges = find_bridges(n, edges, adj)
    if bridges:
        print("NO")
        return

    # Color edges
    color = edge_color_cubic(n, edges, adj)
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    main()
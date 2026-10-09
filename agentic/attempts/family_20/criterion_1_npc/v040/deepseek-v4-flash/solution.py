import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj):
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0
    bridges = []

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
                    bridges.append(eid)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def edge_color_cubic(n, edges, adj):
    # We'll use a known constructive method:
    # 1. Find a perfect matching, remove it, color it with color 1.
    # 2. Remaining graph is 2-regular (cycles), color alternately with 2 and 3.
    color = [0] * len(edges)
    adj_edges = [[] for _ in range(n + 1)]
    for idx, (u, v) in enumerate(edges):
        adj_edges[u].append((v, idx))
        adj_edges[v].append((u, idx))

    # Find perfect matching using simple DFS-based approach for cubic graph
    matched = [False] * (n + 1)
    match_edge = [-1] * (n + 1)
    used = [False] * len(edges)

    def augment(u):
        for v, eid in adj_edges[u]:
            if used[eid]:
                continue
            if matched[v]:
                continue
            matched[u] = matched[v] = True
            match_edge[u] = match_edge[v] = eid
            used[eid] = True
            return True
        return False

    for u in range(1, n + 1):
        if not matched[u]:
            augment(u)

    # If not all matched, fallback: use simple greedy
    if not all(matched[1:]):
        matched = [False] * (n + 1)
        match_edge = [-1] * (n + 1)
        used = [False] * len(edges)
        for u in range(1, n + 1):
            if not matched[u]:
                for v, eid in adj_edges[u]:
                    if not used[eid] and not matched[v]:
                        matched[u] = matched[v] = True
                        match_edge[u] = match_edge[v] = eid
                        used[eid] = True
                        break

    for i in range(1, n + 1):
        if match_edge[i] != -1:
            color[match_edge[i]] = 1

    # Remaining edges form cycles
    remaining_edges = [i for i in range(len(edges)) if color[i] == 0]
    # Build graph of remaining edges
    rem_adj = [[] for _ in range(n + 1)]
    for eid in remaining_edges:
        u, v = edges[eid]
        rem_adj[u].append((v, eid))
        rem_adj[v].append((u, eid))

    visited = [False] * (n + 1)
    for start in range(1, n + 1):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                nxt = None
                for to, eid in rem_adj[cur]:
                    if to != prev:
                        nxt = (to, eid)
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt[1])
                prev, cur = cur, nxt[0]
                if cur == start:
                    break
            # color alternately 2,3
            for k, eid in enumerate(cycle_edges):
                color[eid] = 2 if k % 2 == 0 else 3
    return color

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    for eid in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    bridges = find_bridges(n, adj)
    if bridges:
        print("NO")
        return

    color = edge_color_cubic(n, edges, adj)
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    main()
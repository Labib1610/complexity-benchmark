import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, edges, adj):
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = [0]
    bridges = set()

    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
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
    dfs(1, -1)
    return bridges

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
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

    # Check for bridges
    bridges = find_bridges(n, edges, adj)
    if bridges:
        print("NO")
        return

    # 3-edge-coloring for bridgeless cubic graph
    color = [-1] * m

    # Use a simple backtracking with degree constraints
    # Since graph is cubic and bridgeless, a solution exists.
    # We'll use a greedy + backtracking approach.

    # Build adjacency with edge ids
    edge_adj = [[] for _ in range(n + 1)]
    for eid, (u, v) in enumerate(edges):
        edge_adj[u].append(eid)
        edge_adj[v].append(eid)

    # Try to color edges one by one
    # We'll use a recursive backtracking with forward checking
    # But for n=2000, we need something efficient.
    # Use a known algorithm: find a perfect matching, remove it, color it color 1,
    # then the remaining graph is 2-regular (cycles), color alternately 2 and 3.

    # Step 1: Find a perfect matching in the cubic graph.
    # Use simple greedy matching (since graph is cubic and bridgeless, perfect matching exists)
    matched = [False] * (n + 1)
    matching_edges = []
    for eid, (u, v) in enumerate(edges):
        if not matched[u] and not matched[v]:
            matched[u] = True
            matched[v] = True
            matching_edges.append(eid)
            color[eid] = 1

    # Step 2: The remaining edges form disjoint cycles.
    # Color them alternately 2 and 3.
    remaining_adj = [[] for _ in range(n + 1)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == -1:
            remaining_adj[u].append((v, eid))
            remaining_adj[v].append((u, eid))

    visited_vertex = [False] * (n + 1)
    for start in range(1, n + 1):
        if not visited_vertex[start] and remaining_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited_vertex[cur] = True
                # pick next unvisited edge
                nxt = None
                for to, eid in remaining_adj[cur]:
                    if eid != prev:
                        nxt = (to, eid)
                        break
                if nxt is None:
                    break
                to, eid = nxt
                cycle_edges.append(eid)
                prev = eid
                cur = to
                if cur == start:
                    break
            # color alternately
            for i, eid in enumerate(cycle_edges):
                color[eid] = 2 if i % 2 == 0 else 3

    # Output
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N1 = int(input_data[0])
    N2 = int(input_data[1])
    M = int(input_data[2])

    if M == 0:
        sys.stdout.write("YES\n\n")
        return

    # Read edges
    # Primary processors: 1..N1
    # Secondary processors: 1..N2 (we can offset by N1)
    u_arr = [0] * M
    v_arr = [0] * M
    deg1 = [0] * (N1 + 1)
    deg2 = [0] * (N2 + 1)

    idx = 3
    for i in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        u_arr[i] = u
        v_arr[i] = v
        deg1[u] += 1
        deg2[v] += 1

    K = max(max(deg1), max(deg2))
    if K == 0:
        sys.stdout.write("YES\n\n")
        return

    ans = [0] * M

    # Recursive function to color a subset of edges
    # edge_indices: list of original edge indices
    def divide_and_conquer(edge_indices, color_start, num_colors):
        if not edge_indices:
            return
        if num_colors == 1:
            for e in edge_indices:
                ans[e] = color_start
            return

        # Find active vertices and their degrees in the current subgraph
        # We'll use local arrays or dicts
        # Map active vertices to 0..V-1
        # Primary: 1..N1, Secondary: N1+1..N1+N2
        active_u = set()
        active_v = set()
        for e in edge_indices:
            active_u.add(u_arr[e])
            active_v.add(v_arr[e])

        # We can build adjacency list
        # Identify odd degree vertices
        deg_u = {}
        deg_v = {}
        for u in active_u:
            deg_u[u] = 0
        for v in active_v:
            deg_v[v] = 0

        for e in edge_indices:
            deg_u[u_arr[e]] += 1
            deg_v[v_arr[e]] += 1

        odd_u = [u for u in active_u if deg_u[u] % 2 != 0]
        odd_v = [v for v in active_v if deg_v[v] % 2 != 0]

        # Pair odd vertices
        dummy_edges = []
        min_len = min(len(odd_u), len(odd_v))
        for i in range(min_len):
            dummy_edges.append((odd_u[i], odd_v[i]))

        if len(odd_u) > min_len:
            dummy_v = -1
            for i in range(min_len, len(odd_u)):
                dummy_edges.append((odd_u[i], dummy_v))
        elif len(odd_v) > min_len:
            dummy_u = -1
            for i in range(min_len, len(odd_v)):
                dummy_edges.append((dummy_u, odd_v[i]))

        # Build graph for Euler tour
        # Nodes: u in active_u (int), v in active_v (can use negative or shifted)
        # To avoid collisions:
        # primary: u
        # secondary: -v (since v >= 1)
        # dummy primary: -N2 - 1
        # dummy secondary: -1 (already covered if secondary is -v)
        # Let's map all vertices to 0..total_nodes-1
        node_map = {}

        def get_id(x, is_sec):
            key = (x, is_sec)
            if key not in node_map:
                node_map[key] = len(node_map)
            return node_map[key]

        adj = []

        def add_edge(u_id, v_id, eid):
            while len(adj) <= max(u_id, v_id):
                adj.append([])
            adj[u_id].append((v_id, eid))
            adj[v_id].append((u_id, eid))

        for e in edge_indices:
            u_id = get_id(u_arr[e], False)
            v_id = get_id(v_arr[e], True)
            add_edge(u_id, v_id, e)

        dummy_start_eid = M + 100
        for i, (du, dv) in enumerate(dummy_edges):
            u_id = get_id(du, False)
            v_id = get_id(dv, True)
            add_edge(u_id, v_id, dummy_start_eid + i)

        num_nodes = len(node_map)
        while len(adj) < num_nodes:
            adj.append([])

        # Euler tour on all components
        visited_edges = set()
        edge_side = {}
        ptr = [0] * num_nodes

        for i in range(num_nodes):
            if ptr[i] < len(adj[i]):
                # Hierholzer's algorithm
                stack = [i]
                tour = []
                while stack:
                    curr = stack[-1]
                    while ptr[curr] < len(adj[curr]) and adj[curr][ptr[curr]][
                        1
                    ] in visited_edges:
                        ptr[curr] += 1
                    if ptr[curr] < len(adj[curr]):
                        nxt, eid = adj[curr][ptr[curr]]
                        ptr[curr] += 1
                        visited_edges.add(eid)
                        stack.append(nxt)
                    else:
                        tour.append(stack.pop())

                # tour is a cycle of vertices: v0, v1, ..., vn where v0 == vn
                for j in range(len(tour) - 1):
                    # Edge between tour[j] and tour[j+1]
                    pass
                # Alternate edges in the tour
                # To assign cleanly, we can do it during DFS / tour construction
                # But even simpler:

        # Alternative clean Hierholzer:
        visited_edges = [False] * (M + len(dummy_edges) + 200)
        group0 = []
        group1 = []

        ptr = [0] * num_nodes
        for i in range(num_nodes):
            if ptr[i] < len(adj[i]):
                stack = [(i, -1)]
                trail = []
                while stack:
                    curr, in_edge = stack[-1]
                    while (
                        ptr[curr] < len(adj[curr])
                        and visited_edges[adj[curr][ptr[curr]][1] % len(visited_edges)]
                    ):
                        ptr[curr] += 1
                    if ptr[curr] < len(adj[curr]):
                        nxt, eid = adj[curr][ptr[curr]]
                        ptr[curr] += 1
                        visited_edges[eid % len(visited_edges)] = True
                        stack.append((nxt, eid))
                    else:
                        node, eid = stack.pop()
                        if eid != -1:
                            trail.append(eid)

                for k, eid in enumerate(trail):
                    if eid < M:
                        if k % 2 == 0:
                            group0.append(eid)
                        else:
                            group1.append(eid)

        c0 = num_colors // 2
        c1 = num_colors - c0
        divide_and_conquer(group0, color_start, c0)
        divide_and_conquer(group1, color_start + c0, c1)

    all_edges = list(range(M))
    divide_and_conquer(all_edges, 1, K)

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
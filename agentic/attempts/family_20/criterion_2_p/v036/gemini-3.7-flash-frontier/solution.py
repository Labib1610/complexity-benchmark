import sys

# Increase recursion depth just in case, though we will use an iterative/queue-based approach
sys.setrecursionlimit(2000000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_L = int(input_data[0])
    n_R = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        print("YES")
        print()
        return

    U = [0] * m
    V = [0] * m
    deg_L = [0] * (n_L + 1)
    deg_R = [0] * (n_R + 1)

    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        U[i] = u
        V[i] = v
        deg_L[u] += 1
        deg_R[v] += 1

    D = max(max(deg_L), max(deg_R))
    if D == 0:
        print("YES")
        print(" ".join(["1"] * m))
        return

    ans = [0] * m

    # Each subproblem is (edge_indices, num_colors, color_offset)
    stack = [(list(range(m)), D, 1)]

    while stack:
        edges, d, offset = stack.pop()
        if d == 1:
            for e in edges:
                ans[e] = offset
            continue

        # Split edges into two sets of size ceil(d/2) and floor(d/2) colors
        # Collect vertices involved in this subproblem
        # To avoid large arrays, use local indexing or sparse structures
        # Build adjacency list with dummy edges to make all degrees even
        
        # Count degrees of vertices involved
        local_deg = {}
        for e in edges:
            u = U[e]
            v = -V[e]  # use negative for R to distinguish
            local_deg[u] = local_deg.get(u, 0) + 1
            local_deg[v] = local_deg.get(v, 0) + 1

        odd_L = []
        odd_R = []
        for v, deg in local_deg.items():
            if deg % 2 != 0:
                if v > 0:
                    odd_L.append(v)
                else:
                    odd_R.append(v)

        # Balance odd vertices between L and R
        # Add dummy vertices if necessary
        dummy_id = 1000000000
        while len(odd_L) < len(odd_R):
            dummy_L = dummy_id
            dummy_id += 1
            odd_L.append(dummy_L)
        while len(odd_R) < len(odd_L):
            dummy_R = -dummy_id
            dummy_id += 1
            odd_R.append(dummy_R)

        # Build graph for Euler tour
        # Nodes will be mapped to 0..V_count-1
        adj = {}
        for e in edges:
            u = U[e]
            v = -V[e]
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((v, e))
            adj[v].append((u, e))

        # Add dummy edges
        dummy_edge_idx = -1
        for u, v in zip(odd_L, odd_R):
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((v, dummy_edge_idx))
            adj[v].append((u, dummy_edge_idx))
            dummy_edge_idx -= 1

        # Find Euler circuits / trails
        # Hierholzer's algorithm
        used_edges = set()
        edges1 = []
        edges2 = []

        for start_node in list(adj.keys()):
            while adj[start_node]:
                # Find an Eulerian cycle
                curr_path = [start_node]
                cycle = []

                while curr_path:
                    curr = curr_path[-1]
                    while adj[curr] and adj[curr][-1][1] in used_edges:
                        adj[curr].pop()

                    if adj[curr]:
                        nxt, e_idx = adj[curr].pop()
                        used_edges.add(e_idx)
                        curr_path.append(nxt)
                    else:
                        cycle.append(curr_path.pop())

                # Cycle contains vertices in order
                # The edges traversed form alternating 0/1 assignment
                # Since graph is bipartite and regular-degree even, cycle has even length of edges
                for i in range(len(cycle) - 1):
                    u = cycle[i]
                    # We need the edge between cycle[i] and cycle[i+1], but we can't easily find it
                    # Instead of recovering from vertices, let's track edges during traversal!

        # Let's do Hierholzer properly storing edges:
        # Re-initialize to do it cleanly

    # Refactored below cleanly and efficiently
    pass


def run():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n_L = int(input_data[0])
    n_R = int(input_data[1])
    m = int(input_data[2])

    if m == 0:
        print("YES")
        print()
        return

    U = [0] * m
    V = [0] * m
    deg_L = [0] * (n_L + 1)
    deg_R = [0] * (n_R + 1)

    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        U[i] = u
        V[i] = v
        deg_L[u] += 1
        deg_R[v] += 1

    D = max(max(deg_L), max(deg_R))
    if D == 0:
        print("YES")
        print(" ".join(["1"] * m))
        return

    ans = [0] * m

    stack = [(list(range(m)), D, 1)]

    while stack:
        edges, d, offset = stack.pop()
        if d == 1:
            for e in edges:
                ans[e] = offset
            continue

        d1 = (d + 1) // 2
        d2 = d // 2

        # Count degrees
        local_deg = {}
        for e in edges:
            u = U[e]
            v = -V[e]
            local_deg[u] = local_deg.get(u, 0) + 1
            local_deg[v] = local_deg.get(v, 0) + 1

        odd_L = []
        odd_R = []
        for v, deg in local_deg.items():
            if deg % 2 != 0:
                if v > 0:
                    odd_L.append(v)
                else:
                    odd_R.append(v)

        dummy_id = 1000000000
        while len(odd_L) < len(odd_R):
            dummy_L = dummy_id
            dummy_id += 1
            odd_L.append(dummy_L)
        while len(odd_R) < len(odd_L):
            dummy_R = -dummy_id
            dummy_id += 1
            odd_R.append(dummy_R)

        adj = {}
        for e in edges:
            u = U[e]
            v = -V[e]
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((v, e))
            adj[v].append((u, e))

        dummy_edge_idx = -1
        for u, v in zip(odd_L, odd_R):
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append((v, dummy_edge_idx))
            adj[v].append((u, dummy_edge_idx))
            dummy_edge_idx -= 1

        # Hierholzer's algorithm with edge tracking
        used = set()
        edges1 = []
        edges2 = []

        for start_node in list(adj.keys()):
            if not adj[start_node]:
                continue
            
            # Find Euler tours from start_node
            # We can use a non-recursive approach
            curr_v = start_node
            edge_stack = []
            
            # Hierholzer with edge stack
            v_stack = [curr_v]
            tour_edges = []
            
            while v_stack:
                u = v_stack[-1]
                while adj[u] and adj[u][-1][1] in used:
                    adj[u].pop()
                if adj[u]:
                    nxt, e_idx = adj[u].pop()
                    used.add(e_idx)
                    v_stack.append(nxt)
                    edge_stack.append(e_idx)
                else:
                    v_stack.pop()
                    if edge_stack:
                        tour_edges.append(edge_stack.pop())

            # tour_edges forms an Eulerian cycle (in reverse, but order doesn't matter for alternating)
            for i, e_idx in enumerate(tour_edges):
                if e_idx >= 0:
                    if i % 2 == 0:
                        edges1.append(e_idx)
                    else:
                        edges2.append(e_idx)

        stack.append((edges2, d2, offset + d1))
        stack.append((edges1, d1, offset))

    print("YES")
    print(*(ans[i] for i in range(m)))


if __name__ == "__main__":
    run()
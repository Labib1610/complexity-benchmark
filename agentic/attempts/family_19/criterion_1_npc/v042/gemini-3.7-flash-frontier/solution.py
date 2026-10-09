import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    swarms = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        swarms.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Try using scipy.optimize.milp
    try:
        import numpy as np
        from scipy.optimize import LinearConstraint, milp

        num_vars = k * m
        c = np.ones(num_vars)  # Minimize total flow to find shortest paths

        # Constraints
        # 1. Capacity constraints: for each edge j, sum_i x_{i, j} <= cap_j
        # 2. Flow conservation: for each commodity i, vertex v, sum out - sum in = b_{i, v}

        row_list = []
        lhs_list = []
        rhs_list = []

        # Capacity constraints
        for j in range(m):
            row = np.zeros(num_vars)
            for i in range(k):
                row[i * m + j] = 1.0
            row_list.append(row)
            lhs_list.append(0.0)
            rhs_list.append(float(edges[j][2]))

        # Flow conservation
        for i in range(k):
            s, t, d = swarms[i]
            for v in range(n):
                row = np.zeros(num_vars)
                # out-edges from v
                for j in range(m):
                    if edges[j][0] == v:
                        row[i * m + j] += 1.0
                    if edges[j][1] == v:
                        row[i * m + j] -= 1.0

                req = 0.0
                if s == t:
                    req = 0.0
                elif v == s:
                    req = float(d)
                elif v == t:
                    req = -float(d)
                else:
                    req = 0.0

                row_list.append(row)
                lhs_list.append(req)
                rhs_list.append(req)

        A = np.array(row_list)
        constraints = LinearConstraint(A, lhs_list, rhs_list)
        integrality = np.ones(num_vars)
        bounds_ub = np.zeros(num_vars)
        for i in range(k):
            for j in range(m):
                bounds_ub[i * m + j] = min(swarms[i][2], edges[j][2])

        from scipy.optimize import Bounds

        bounds = Bounds(lb=np.zeros(num_vars), ub=bounds_ub)

        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

        if res.success:
            print("YES")
            x = np.round(res.x).astype(int)
            for i in range(k):
                row = [str(x[i * m + j]) for j in range(m)]
                print(*(row))
            return
        else:
            print("NO")
            return

    except Exception:
        pass

    # Pure Python DFS Backtracking fallback for small instances
    # Decompose into unit paths or swarm paths
    # Flatten demands into individual units
    units = []
    for i in range(k):
        s, t, d = swarms[i]
        for _ in range(d):
            units.append((i, s, t))

    rem_cap = [edges[j][2] for j in range(m)]
    flow = [[0] * m for _ in range(k)]

    # Adjacency list: u -> list of (v, edge_index)
    adj = [[] for _ in range(n)]
    for j, (u, v, cap) in enumerate(edges):
        adj[u].append((v, j))

    def dfs(unit_idx):
        if unit_idx == len(units):
            return True

        comm_id, start_node, target_node = units[unit_idx]

        # Find a path from start_node to target_node
        visited = [False] * n
        path_edges = []

        def find_path(curr):
            if curr == target_node:
                return True
            visited[curr] = True
            for nxt, edge_idx in adj[curr]:
                if not visited[nxt] and rem_cap[edge_idx] > 0:
                    rem_cap[edge_idx] -= 1
                    flow[comm_id][edge_idx] += 1
                    path_edges.append(edge_idx)

                    if find_path(nxt):
                        return True

                    path_edges.pop()
                    flow[comm_id][edge_idx] -= 1
                    rem_cap[edge_idx] += 1
            return False

        # Try all simple paths
        def search_paths(curr):
            if curr == target_node:
                if dfs(unit_idx + 1):
                    return True
                return False

            visited[curr] = True
            for nxt, edge_idx in adj[curr]:
                if not visited[nxt] and rem_cap[edge_idx] > 0:
                    rem_cap[edge_idx] -= 1
                    flow[comm_id][edge_idx] += 1
                    if search_paths(nxt):
                        return True
                    flow[comm_id][edge_idx] -= 1
                    rem_cap[edge_idx] += 1
            visited[curr] = False
            return False

        return search_paths(start_node)

    if dfs(0):
        print("YES")
        for i in range(k):
            print(*(flow[i]))
    else:
        print("NO")


if __name__ == "__main__":
    solve()
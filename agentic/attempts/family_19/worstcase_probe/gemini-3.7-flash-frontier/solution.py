import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    commodities = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        commodities.append((s, t, d))
        
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))

    # Try using scipy if available
    try:
        from scipy.optimize import milp, LinearConstraint, Bounds
        import numpy as np

        num_vars = k * m
        # Bounds: 0 <= x_{c, e} <= cap_e
        lb = np.zeros(num_vars)
        ub = np.zeros(num_vars)
        for c in range(k):
            for e in range(m):
                ub[c * m + e] = edges[e][2]

        # Constraints
        # 1. Capacity constraints: sum_c x_{c, e} <= cap_e for each e
        row_list = []
        rhs_lb = []
        rhs_ub = []

        for e in range(m):
            row = np.zeros(num_vars)
            for c in range(k):
                row[c * m + e] = 1.0
            row_list.append(row)
            rhs_lb.append(0.0)
            rhs_ub.append(float(edges[e][2]))

        # 2. Conservation constraints: for each commodity c and each node u
        # Unique nodes
        all_nodes = set()
        for u, v, _ in edges:
            all_nodes.add(u)
            all_nodes.add(v)
        for s, t, _ in commodities:
            all_nodes.add(s)
            all_nodes.add(t)

        for c in range(k):
            s, t, d = commodities[c]
            for node in all_nodes:
                row = np.zeros(num_vars)
                has_edge = False
                for e, (u, v, _) in enumerate(edges):
                    if u == node:
                        row[c * m + e] += 1.0
                        has_edge = True
                    if v == node:
                        row[c * m + e] -= 1.0
                        has_edge = True
                
                target = 0.0
                if node == s:
                    target += d
                if node == t:
                    target -= d
                
                if has_edge or target != 0.0:
                    row_list.append(row)
                    rhs_lb.append(target)
                    rhs_ub.append(target)

        A = np.array(row_list)
        constraints = LinearConstraint(A, rhs_lb, rhs_ub)
        integrality = np.ones(num_vars)
        c_obj = np.zeros(num_vars)
        bounds = Bounds(lb, ub)

        res = milp(c=c_obj, integrality=integrality, constraints=constraints, bounds=bounds)

        if res.success:
            print("YES")
            sol = np.round(res.x).astype(int)
            for c in range(k):
                row_flows = [str(sol[c * m + e]) for e in range(m)]
                print(*(row_flows))
        else:
            print("NO")
        return

    except ImportError:
        pass

    # Fallback: Backtracking / DFS solver for small instances or pure integer search
    # Map edges
    # Variables: flow[c][e]
    flow = [[0] * m for _ in range(k)]
    edge_rem = [edges[e][2] for e in range(m)]
    
    # Simple path-based decomposition search
    def find_dispatch(c_idx):
        if c_idx == k:
            return True
        s, t, d = commodities[c_idx]
        if d == 0:
            return find_dispatch(c_idx + 1)
        
        # Backtracking paths for commodity c_idx
        # Generate possible unit or multi-unit paths
        def route(node, cur_d, path_edges):
            if cur_d == 0:
                return find_dispatch(c_idx + 1)
            if node == t:
                return route(s, cur_d, [])
            
            for e, (u, v, cap) in enumerate(edges):
                if u == node and edge_rem[e] > 0:
                    amt = min(cur_d, edge_rem[e])
                    for send in range(amt, 0, -1):
                        edge_rem[e] -= send
                        flow[c_idx][e] += send
                        if route(v, cur_d - send if v == t else cur_d, path_edges + [e]):
                            return True
                        edge_rem[e] += send
                        flow[c_idx][e] -= send
            return False

        return route(s, d, [])

    if find_dispatch(0):
        print("YES")
        for c in range(k):
            print(*(flow[c]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
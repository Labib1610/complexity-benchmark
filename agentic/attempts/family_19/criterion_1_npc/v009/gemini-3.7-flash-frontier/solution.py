import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    
    products = []
    for _ in range(k):
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
        products.append((s, t, d))
        
    lanes = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        lanes.append((u, v, cap))

    # Try solving with scipy.optimize.milp if available
    try:
        import numpy as np
        from scipy.optimize import milp, LinearConstraint, Bounds
        
        num_vars = k * m
        # Capacity constraints: m constraints
        # Conservation constraints: k * n constraints
        num_constraints = m + k * n
        
        A_rows = []
        b_l = []
        b_u = []
        
        # 1. Capacity constraints
        for j in range(m):
            row = np.zeros(num_vars)
            for i in range(k):
                row[i * m + j] = 1.0
            A_rows.append(row)
            b_l.append(0.0)
            b_u.append(float(lanes[j][2]))
            
        # 2. Flow conservation constraints
        for i in range(k):
            s_i, t_i, d_i = products[i]
            for u in range(1, n + 1):
                row = np.zeros(num_vars)
                for j in range(m):
                    u_j, v_j, _ = lanes[j]
                    if u_j == u:
                        row[i * m + j] += 1.0
                    if v_j == u:
                        row[i * m + j] -= 1.0
                
                target = 0.0
                if s_i == t_i:
                    target = 0.0
                elif u == s_i:
                    target = float(d_i)
                elif u == t_i:
                    target = float(-d_i)
                
                A_rows.append(row)
                b_l.append(target)
                b_u.append(target)
                
        A = np.array(A_rows)
        constraints = LinearConstraint(A, b_l, b_u)
        integrality = np.ones(num_vars)
        c = np.zeros(num_vars)
        bounds = Bounds(lb=0.0, ub=np.inf)
        
        res = milp(c=c, integrality=integrality, constraints=constraints, bounds=bounds)
        
        if res.success:
            print("YES")
            x = np.round(res.x).astype(int)
            for i in range(k):
                row = x[i * m : (i + 1) * m]
                print(*(row.tolist()))
            return
        else:
            print("NO")
            return
    except ImportError:
        pass

    # Fallback: Path-based local search / Multiplicative Weights Update Algorithm
    import heapq
    import random
    import math

    # Check trivial infeasibilities
    adj = [[] for _ in range(n + 1)]
    for j, (u, v, cap) in enumerate(lanes):
        adj[u].append((v, cap, j))

    # Break demands into unit flows
    units = []
    for i, (s, t, d) in enumerate(products):
        for _ in range(d):
            units.append(i)

    num_units = len(units)
    if num_units == 0:
        print("YES")
        for _ in range(k):
            print(*(0 for _ in range(m)))
        return

    unit_paths = [[] for _ in range(num_units)]
    edge_usage = [0] * m

    def dijkstra(s, t, weights):
        dist = {s: 0.0}
        parent = {}
        pq = [(0.0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float('inf')):
                continue
            if u == t:
                break
            for v, cap, j in adj[u]:
                if cap <= 0:
                    continue
                w = weights[j]
                if d + w < dist.get(v, float('inf')):
                    dist[v] = d + w
                    parent[v] = (u, j)
        if t not in parent and s != t:
            return None
        path = []
        curr = t
        while curr != s:
            p, j = parent[curr]
            path.append(j)
            curr = p
        path.reverse()
        return path

    # Initialize paths with MWUA
    for u_idx, p_idx in enumerate(units):
        s, t, _ = products[p_idx]
        weights = [1.0 + (edge_usage[j] / max(1, lanes[j][2])) ** 2 for j in range(m)]
        path = dijkstra(s, t, weights)
        if path is None:
            print("NO")
            return
        unit_paths[u_idx] = path
        for j in path:
            edge_usage[j] += 1

    # Local search to resolve capacity violations
    max_steps = 20000
    for step in range(max_steps):
        overloaded = [j for j in range(m) if edge_usage[j] > lanes[j][2]]
        if not overloaded:
            # Valid solution found!
            print("YES")
            flow = [[0] * m for _ in range(k)]
            for u_idx, path in enumerate(unit_paths):
                p_idx = units[u_idx]
                for j in path:
                    flow[p_idx][j] += 1
            for row in flow:
                print(*(row))
            return

        # Pick a random overloaded edge
        e = random.choice(overloaded)
        # Find units traversing this edge
        candidates = [u_idx for u_idx, path in enumerate(unit_paths) if e in path]
        if not candidates:
            continue
        u_idx = random.choice(candidates)
        p_idx = units[u_idx]
        s, t, _ = products[p_idx]

        # Remove old path
        for j in unit_paths[u_idx]:
            edge_usage[j] -= 1

        # Reroute with penalized weights
        weights = []
        for j in range(m):
            cap = lanes[j][2]
            usage = edge_usage[j]
            ratio = (usage + 1) / max(1, cap)
            weights.append(math.exp(min(20.0, 3.0 * ratio)) + random.uniform(0, 0.01))

        new_path = dijkstra(s, t, weights)
        if new_path is None:
            new_path = unit_paths[u_idx]

        unit_paths[u_idx] = new_path
        for j in new_path:
            edge_usage[j] += 1

    print("NO")

if __name__ == '__main__':
    solve()
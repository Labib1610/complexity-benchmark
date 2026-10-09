import sys
import itertools

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Try using scipy milp if available
    try:
        import scipy.optimize as opt
        from scipy.sparse import lil_matrix
        import numpy as np
    except ImportError:
        print("NO")
        return
    
    # Variables: x[i][j] = flow of commodity i on edge j
    num_vars = k * m
    c = np.zeros(num_vars)  # objective: any feasible solution
    
    # Constraints:
    # 1. Capacity: sum_i x[i][j] <= cap_j
    # 2. Flow conservation for each commodity at each node (except source/sink)
    # 3. Source outflow - inflow = d_i
    # 4. Sink inflow - outflow = d_i
    # 5. x >= 0 and integer
    
    A_rows = []
    b_lo = []
    b_hi = []
    
    # Capacity constraints
    for j, (u, v, cap) in enumerate(edges):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + j] = 1
        A_rows.append(row)
        b_lo.append(0)
        b_hi.append(cap)
    
    # Flow conservation for each commodity at each node
    for i, (s, t, d) in enumerate(commodities):
        for node in range(n):
            if node == s or node == t:
                continue
            row = np.zeros(num_vars)
            for j, (u, v, cap) in enumerate(edges):
                if u == node:
                    row[i*m + j] += 1  # outflow
                if v == node:
                    row[i*m + j] -= 1  # inflow
            A_rows.append(row)
            b_lo.append(0)
            b_hi.append(0)
    
    # Source constraint: outflow - inflow = d
    for i, (s, t, d) in enumerate(commodities):
        row = np.zeros(num_vars)
        for j, (u, v, cap) in enumerate(edges):
            if u == s:
                row[i*m + j] += 1
            if v == s:
                row[i*m + j] -= 1
        A_rows.append(row)
        b_lo.append(d)
        b_hi.append(d)
    
    # Sink constraint: inflow - outflow = d
    for i, (s, t, d) in enumerate(commodities):
        row = np.zeros(num_vars)
        for j, (u, v, cap) in enumerate(edges):
            if v == t:
                row[i*m + j] += 1
            if u == t:
                row[i*m + j] -= 1
        A_rows.append(row)
        b_lo.append(d)
        b_hi.append(d)
    
    A = np.array(A_rows)
    lb = np.array(b_lo)
    ub = np.array(b_hi)
    
    # Variable bounds
    var_lb = np.zeros(num_vars)
    var_ub = np.full(num_vars, np.inf)
    
    integrality = np.ones(num_vars)  # all integer
    
    # Solve MILP
    res = opt.milp(c, integrality=integrality, bounds=opt.Bounds(var_lb, var_ub),
                   constraints=opt.LinearConstraint(A, lb, ub))
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    print("YES")
    for i in range(k):
        flows = [int(round(x[i*m + j])) for j in range(m)]
        print(' '.join(map(str, flows)))

if __name__ == "__main__":
    solve()
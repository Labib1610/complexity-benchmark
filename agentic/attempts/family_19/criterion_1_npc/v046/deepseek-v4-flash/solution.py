import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
    
    # Variables: x[i][j] for order i, edge j
    num_vars = k * m
    
    # Objective: all zeros (feasibility only)
    c_obj = np.zeros(num_vars)
    
    # Constraints:
    # 1. Flow conservation for each order and each node
    # 2. Capacity constraints for each edge
    
    constraints = []
    lower_bounds = []
    upper_bounds = []
    
    # Node conservation constraints
    for i in range(k):
        s_i, t_i, d_i = orders[i]
        for v in range(n):
            row = np.zeros(num_vars)
            # outgoing edges from v
            for j, (u, vv, _) in enumerate(edges):
                if u == v:
                    row[i * m + j] += 1
                if vv == v:
                    row[i * m + j] -= 1
            # RHS depends on node type
            if v == s_i:
                rhs = d_i
            elif v == t_i:
                rhs = -d_i
            else:
                rhs = 0
            constraints.append(row)
            lower_bounds.append(rhs)
            upper_bounds.append(rhs)
    
    # Capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        constraints.append(row)
        lower_bounds.append(-np.inf)
        upper_bounds.append(edges[j][2])
    
    A = np.array(constraints)
    lb = np.array(lower_bounds)
    ub = np.array(upper_bounds)
    
    lc = LinearConstraint(A, lb, ub)
    
    # Integrality: all variables integer
    integrality = np.ones(num_vars)
    
    # Bounds: x >= 0
    bounds = Bounds(np.zeros(num_vars), np.full(num_vars, np.inf))
    
    res = milp(c=c_obj, constraints=lc, integrality=integrality, bounds=bounds)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    # Output
    print("YES")
    for i in range(k):
        row = []
        for j in range(m):
            row.append(str(int(round(x[i * m + j]))))
        print(" ".join(row))

if __name__ == "__main__":
    solve()
import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    items = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        items.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        lim = int(next(it))
        edges.append((u, v, lim))
    
    # Build incidence matrix for each item type
    # Variables: x[i][j] for i in 0..k-1, j in 0..m-1
    # Total variables = k*m
    num_vars = k * m
    
    # Constraints:
    # 1) Link capacity: for each link j, sum_i x[i][j] <= limit[j]
    # 2) Flow conservation for each item type and each node
    
    constraints = []
    lb = []
    ub = []
    
    # Link capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + j] = 1
        constraints.append(row)
        lb.append(-np.inf)
        ub.append(edges[j][2])
    
    # Flow conservation constraints
    for i in range(k):
        s, t, d = items[i]
        # For each node v
        for v in range(n):
            row = np.zeros(num_vars)
            # inflow - outflow
            for j, (u, w, _) in enumerate(edges):
                if w == v:
                    row[i*m + j] += 1  # inflow
                if u == v:
                    row[i*m + j] -= 1  # outflow
            if v == s:
                # outflow - inflow = d  => inflow - outflow = -d
                lb.append(-d)
                ub.append(-d)
            elif v == t:
                # inflow - outflow = d
                lb.append(d)
                ub.append(d)
            else:
                lb.append(0)
                ub.append(0)
            constraints.append(row)
    
    A = np.array(constraints)
    lc = LinearConstraint(A, np.array(lb), np.array(ub))
    
    # Objective: all zeros (feasibility only)
    c = np.zeros(num_vars)
    
    # Bounds: all variables >= 0, integer
    bounds = Bounds(np.zeros(num_vars), np.full(num_vars, np.inf))
    
    integrality = np.ones(num_vars)  # all integer
    
    res = milp(c=c, constraints=lc, bounds=bounds, integrality=integrality)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    # Output
    print("YES")
    for i in range(k):
        row = []
        for j in range(m):
            row.append(str(int(round(x[i*m + j]))))
        print(" ".join(row))

if __name__ == "__main__":
    main()
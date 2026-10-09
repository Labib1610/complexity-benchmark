import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds, integrality

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    freqs = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        freqs.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
    
    # Variables: x[i][j] for frequency i, edge j
    # Total variables = k * m
    num_vars = k * m
    
    # Objective: all zeros (feasibility)
    c_obj = np.zeros(num_vars)
    
    # Bounds: all variables >= 0
    lb = np.zeros(num_vars)
    ub = np.full(num_vars, np.inf)
    bounds = Bounds(lb, ub)
    
    # Integrality: all integer
    intg = np.ones(num_vars)
    
    constraints = []
    lower_bounds = []
    upper_bounds = []
    
    # Edge capacity constraints: sum_i x[i][j] <= cap_j
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        constraints.append(row)
        lower_bounds.append(-np.inf)
        upper_bounds.append(edges[j][2])
    
    # Flow conservation constraints for each frequency and each node
    for i in range(k):
        s, t, d = freqs[i]
        for v in range(n):
            row = np.zeros(num_vars)
            # incoming edges
            for j, (u, w, _) in enumerate(edges):
                if w == v:
                    row[i * m + j] += 1
                if u == v:
                    row[i * m + j] -= 1
            # For source: out - in = d
            if v == s:
                lower_bounds.append(d)
                upper_bounds.append(d)
            elif v == t:
                lower_bounds.append(-d)
                upper_bounds.append(-d)
            else:
                lower_bounds.append(0)
                upper_bounds.append(0)
            constraints.append(row)
    
    A = np.array(constraints)
    lc = LinearConstraint(A, np.array(lower_bounds), np.array(upper_bounds))
    
    res = milp(c=c_obj, constraints=[lc], integrality=intg, bounds=bounds, options={"time_limit": 4.5})
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    # Output
    print("YES")
    for i in range(k):
        vals = [str(int(round(x[i * m + j]))) for j in range(m)]
        print(" ".join(vals))

if __name__ == "__main__":
    solve()
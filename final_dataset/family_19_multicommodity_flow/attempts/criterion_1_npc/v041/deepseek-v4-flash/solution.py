import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    sources = []
    targets = []
    demands = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        sources.append(s)
        targets.append(t)
        demands.append(d)
    
    edges_u = []
    edges_v = []
    caps = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges_u.append(u)
        edges_v.append(v)
        caps.append(c)
    
    # Variables: x[i][j] for aid i, edge j
    num_vars = k * m
    # We'll flatten row-major: x[i*m + j]
    
    # Equality constraints: flow conservation
    A_eq = []
    b_eq = []
    
    # For each aid type i and each node v:
    # outflow - inflow = demand at source, -demand at sink, 0 otherwise
    for i in range(k):
        for v in range(n):
            row = [0.0] * num_vars
            # outflow: edges from v
            for j in range(m):
                if edges_u[j] == v:
                    row[i*m + j] += 1.0
                if edges_v[j] == v:
                    row[i*m + j] -= 1.0
            # RHS
            if v == sources[i]:
                rhs = demands[i]
            elif v == targets[i]:
                rhs = -demands[i]
            else:
                rhs = 0
            A_eq.append(row)
            b_eq.append(rhs)
    
    # Inequality constraints: sum_i x[i][j] <= cap[j]
    A_ub = []
    b_ub = []
    for j in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i*m + j] = 1.0
        A_ub.append(row)
        b_ub.append(caps[j])
    
    # Bounds: x >= 0
    bounds = [(0, None)] * num_vars
    
    # Objective: zero vector
    c = [0.0] * num_vars
    
    # Solve
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs', integrality=np.ones(num_vars))
    
    if res.status != 0:
        print("NO")
        return
    
    x = res.x
    # Round to nearest integer (should already be integer)
    x = np.rint(x).astype(int)
    
    print("YES")
    for i in range(k):
        row = [str(x[i*m + j]) for j in range(m)]
        print(" ".join(row))

if __name__ == "__main__":
    solve()
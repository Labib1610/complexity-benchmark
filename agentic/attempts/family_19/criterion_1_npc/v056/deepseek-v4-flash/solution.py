import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    contracts = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        contracts.append((s, t, d))
    
    routes = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        routes.append((u, v, c))
    
    # Variables: x[i][j] = flow of contract i on route j
    # Total variables = k * m
    num_vars = k * m
    
    # Objective: minimize 0 (feasibility only)
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. Route capacity: sum_i x[i][j] <= c_j for each route j
    # 2. Flow conservation at intermediate nodes for each contract
    # 3. Source/destination balance for each contract
    
    constraints = []
    lower_bounds = []
    upper_bounds = []
    
    # Route capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        constraints.append(row)
        lower_bounds.append(0)
        upper_bounds.append(routes[j][2])
    
    # Flow conservation for each contract and each node
    for i in range(k):
        s, t, d = contracts[i]
        for node in range(n):
            row = np.zeros(num_vars)
            # outgoing - incoming = 0 for intermediate, = d at source, = -d at destination
            for j, (u, v, c) in enumerate(routes):
                if u == node:
                    row[i * m + j] += 1
                if v == node:
                    row[i * m + j] -= 1
            constraints.append(row)
            if node == s:
                lower_bounds.append(d)
                upper_bounds.append(d)
            elif node == t:
                lower_bounds.append(-d)
                upper_bounds.append(-d)
            else:
                lower_bounds.append(0)
                upper_bounds.append(0)
    
    A = np.array(constraints)
    lc = LinearConstraint(A, lower_bounds, upper_bounds)
    
    # Variables are non-negative integers
    bounds = Bounds(np.zeros(num_vars), np.full(num_vars, np.inf))
    
    integrality = np.ones(num_vars)  # all integer
    
    res = milp(c=c, constraints=lc, bounds=bounds, integrality=integrality)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    print("YES")
    for i in range(k):
        line = []
        for j in range(m):
            line.append(str(int(round(x[i * m + j]))))
        print(" ".join(line))

if __name__ == "__main__":
    solve()
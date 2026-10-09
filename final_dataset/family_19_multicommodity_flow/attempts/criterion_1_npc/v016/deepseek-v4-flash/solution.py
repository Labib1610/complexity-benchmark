import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

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
    
    edges = []
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Variables: x[i][j] for i in range(k), j in range(m)
    num_vars = k * m
    
    # Build constraint matrix
    # Constraints:
    # 1) For each corridor j: sum_i x[i][j] <= cap[j]  (m constraints)
    # 2) For each contract i and each node v:
    #    inflow - outflow = 0 for intermediate nodes
    #    outflow - inflow = d_i at origin
    #    inflow - outflow = d_i at destination
    #    (n * k constraints)
    
    # We'll build as sparse matrix
    A = lil_matrix((m + n * k, num_vars), dtype=float)
    lb = np.zeros(m + n * k)
    ub = np.full(m + n * k, np.inf)
    
    row = 0
    # Corridor capacity constraints
    for j in range(m):
        for i in range(k):
            A[row, i * m + j] = 1
        ub[row] = edges[j][2]
        row += 1
    
    # Flow conservation constraints
    for i in range(k):
        s, t, d = contracts[i]
        for v in range(n):
            # For each node v, sum of incoming - sum of outgoing = b
            # b = d at origin, -d at destination, 0 otherwise
            b = 0
            if v == s:
                b = d
            elif v == t:
                b = -d
            # For each edge
            for j, (u, w, cap) in enumerate(edges):
                if u == v:
                    # outgoing: subtract
                    A[row, i * m + j] = -1
                if w == v:
                    # incoming: add
                    A[row, i * m + j] = 1
            lb[row] = b
            ub[row] = b
            row += 1
    
    A = A.tocsr()
    
    # Objective: minimize 0 (feasibility only)
    c = np.zeros(num_vars)
    
    # Bounds: all variables >= 0, integer
    bounds = Bounds(lb=np.zeros(num_vars), ub=np.full(num_vars, np.inf))
    
    integrality = np.ones(num_vars)  # all integer
    
    constraints = LinearConstraint(A, lb, ub)
    
    res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    
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
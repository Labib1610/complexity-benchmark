import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
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
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Variables: x_{i,j} = flow of order i on edge j
    # Total variables = k * m
    num_vars = k * m
    
    # Objective: none (feasibility only), so zero coefficients
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. For each edge j, sum_i x_{i,j} <= cap_j
    # 2. For each order i and each node v (not source/sink), flow conservation
    # 3. For each order i, at source: outflow - inflow = d_i
    # 4. For each order i, at sink: inflow - outflow = d_i
    
    A_ub = []
    b_ub = []
    
    # Edge capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])
    
    # Flow conservation constraints (equality)
    A_eq = []
    b_eq = []
    
    # For each order i and each node v
    for i in range(k):
        s, t, d = orders[i]
        for v in range(n):
            row = np.zeros(num_vars)
            # Outflow from v for order i
            for j, (u, w, cap) in enumerate(edges):
                if u == v:
                    row[i*m + j] += 1
                if w == v:
                    row[i*m + j] -= 1
            # For source: outflow - inflow = d
            # For sink: inflow - outflow = d  => outflow - inflow = -d
            if v == s:
                A_eq.append(row)
                b_eq.append(d)
            elif v == t:
                A_eq.append(row)
                b_eq.append(-d)
            else:
                A_eq.append(row)
                b_eq.append(0)
    
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    
    # Bounds: x >= 0
    bounds = [(0, None)] * num_vars
    
    # Solve LP (relaxed, but we need integer)
    # Use integer programming via linprog with integrality
    integrality = np.ones(num_vars)  # all integer
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs', integrality=integrality)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x.astype(int)
    
    print("YES")
    for i in range(k):
        row = [str(x[i*m + j]) for j in range(m)]
        print(" ".join(row))

if __name__ == "__main__":
    solve()
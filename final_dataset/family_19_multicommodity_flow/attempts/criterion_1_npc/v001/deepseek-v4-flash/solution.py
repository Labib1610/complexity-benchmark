import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    products = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))
    
    routes = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        routes.append((u, v, cap))
    
    # Variables: x_{i,j} for product i on route j
    # Total variables = k * m
    num_vars = k * m
    
    # Objective: minimize 0 (feasibility)
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. Route capacity: sum_i x_{i,j} <= cap_j for each route j
    # 2. Flow conservation at intermediate nodes for each product
    # 3. Source/sink balance for each product
    
    A_ub = []
    b_ub = []
    
    # Route capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + j] = 1
        A_ub.append(row)
        b_ub.append(routes[j][2])
    
    # Flow conservation constraints
    # For each product i and each hub h that is not source or sink of product i:
    # sum_{routes leaving h} x_{i,route} - sum_{routes entering h} x_{i,route} = 0
    # For source: sum_{leaving} - sum_{entering} = d_i
    # For sink: sum_{entering} - sum_{leaving} = d_i
    
    A_eq = []
    b_eq = []
    
    for i in range(k):
        s, t, d = products[i]
        for h in range(n):
            if h == s:
                # source: outflow - inflow = d
                row = np.zeros(num_vars)
                for j, (u, v, cap) in enumerate(routes):
                    if u == h:
                        row[i*m + j] += 1
                    if v == h:
                        row[i*m + j] -= 1
                A_eq.append(row)
                b_eq.append(d)
            elif h == t:
                # sink: inflow - outflow = d
                row = np.zeros(num_vars)
                for j, (u, v, cap) in enumerate(routes):
                    if v == h:
                        row[i*m + j] += 1
                    if u == h:
                        row[i*m + j] -= 1
                A_eq.append(row)
                b_eq.append(d)
            else:
                # intermediate: inflow - outflow = 0
                row = np.zeros(num_vars)
                for j, (u, v, cap) in enumerate(routes):
                    if v == h:
                        row[i*m + j] += 1
                    if u == h:
                        row[i*m + j] -= 1
                A_eq.append(row)
                b_eq.append(0)
    
    # Bounds: x >= 0
    bounds = [(0, None)] * num_vars
    
    # Solve LP
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')
    
    if not res.success:
        print("NO")
        return
    
    # Check integrality (since capacities and demands are integers, LP solution should be integral if feasible)
    x = res.x
    # Round to nearest integer (should be close)
    x_int = np.round(x).astype(int)
    
    # Verify feasibility with integer solution
    # Check capacities
    for j in range(m):
        total = sum(x_int[i*m + j] for i in range(k))
        if total > routes[j][2]:
            print("NO")
            return
    
    # Check product balances
    for i in range(k):
        s, t, d = products[i]
        outflow = sum(x_int[i*m + j] for j, (u, v, cap) in enumerate(routes) if u == s)
        inflow = sum(x_int[i*m + j] for j, (u, v, cap) in enumerate(routes) if v == s)
        if outflow - inflow != d:
            print("NO")
            return
        outflow_t = sum(x_int[i*m + j] for j, (u, v, cap) in enumerate(routes) if u == t)
        inflow_t = sum(x_int[i*m + j] for j, (u, v, cap) in enumerate(routes) if v == t)
        if inflow_t - outflow_t != d:
            print("NO")
            return
    
    # Output
    print("YES")
    for i in range(k):
        line = []
        for j in range(m):
            line.append(str(x_int[i*m + j]))
        print(" ".join(line))

if __name__ == "__main__":
    solve()
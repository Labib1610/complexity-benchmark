import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    groups = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        groups.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Variables: for each commodity i and edge j: x[i][j]
    # Total variables = k*m
    num_vars = k * m
    
    # Constraints:
    # 1. For each edge j: sum_i x[i][j] <= cap_j
    # 2. Flow conservation at each node for each commodity
    # 3. Source/sink demands
    
    A_ub = []
    b_ub = []
    
    # Edge capacity constraints
    for j in range(m):
        row = [0]*num_vars
        for i in range(k):
            row[i*m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])
    
    # Flow conservation: for each commodity i and each node v:
    # Incoming - outgoing = 0 (except source/sink)
    # For source: outgoing - incoming = d_i
    # For sink: incoming - outgoing = d_i
    
    A_eq = []
    b_eq = []
    
    for i in range(k):
        s, t, d = groups[i]
        for v in range(n):
            row = [0]*num_vars
            # outgoing from v
            for j,(u,to,cap) in enumerate(edges):
                if u == v:
                    row[i*m + j] = 1
                if to == v:
                    row[i*m + j] = -1
            if v == s:
                # out - in = d
                b_eq.append(d)
                A_eq.append(row)
            elif v == t:
                # in - out = d => -(out - in) = d => out - in = -d
                b_eq.append(-d)
                A_eq.append(row)
            else:
                b_eq.append(0)
                A_eq.append(row)
    
    # variable bounds: all >= 0
    bounds = [(0, None)] * num_vars
    
    # Solve LP: minimize 0 (feasibility)
    res = linprog(c=[0]*num_vars, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    # Check integrality (should be integral due to total unimodularity)
    for val in x:
        if abs(val - round(val)) > 1e-6:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        row = []
        for j in range(m):
            val = round(x[i*m + j])
            row.append(str(val))
        print(" ".join(row))

if __name__ == "__main__":
    solve()
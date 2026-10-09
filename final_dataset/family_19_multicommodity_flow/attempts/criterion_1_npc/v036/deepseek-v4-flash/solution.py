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
    
    # Objective: minimize 0 (feasibility)
    c = np.zeros(num_vars)
    
    A_ub = []
    b_ub = []
    
    # Capacity constraints: sum_i x_{i,j} <= cap_j
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])
    
    # Flow conservation constraints for each order and each node (except source/sink)
    # For each order i, for each node v not source/sink: inflow = outflow
    # inflow: sum over edges (u,v) of x_{i,edge}
    # outflow: sum over edges (v,w) of x_{i,edge}
    # So: sum_{edges into v} x_i - sum_{edges out of v} x_i = 0
    
    A_eq = []
    b_eq = []
    
    for i in range(k):
        s, t, d = orders[i]
        for v in range(n):
            if v == s or v == t:
                continue
            row = np.zeros(num_vars)
            for j, (u, w, cap) in enumerate(edges):
                if w == v:
                    row[i*m + j] += 1
                if u == v:
                    row[i*m + j] -= 1
            A_eq.append(row)
            b_eq.append(0)
    
    # Source: outflow - inflow = d
    for i in range(k):
        s, t, d = orders[i]
        row = np.zeros(num_vars)
        for j, (u, w, cap) in enumerate(edges):
            if u == s:
                row[i*m + j] += 1
            if w == s:
                row[i*m + j] -= 1
        A_eq.append(row)
        b_eq.append(d)
    
    # Sink: inflow - outflow = d
    for i in range(k):
        s, t, d = orders[i]
        row = np.zeros(num_vars)
        for j, (u, w, cap) in enumerate(edges):
            if w == t:
                row[i*m + j] += 1
            if u == t:
                row[i*m + j] -= 1
        A_eq.append(row)
        b_eq.append(d)
    
    # Bounds: x >= 0
    bounds = [(0, None)] * num_vars
    
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')
    
    if res.success:
        print("YES")
        x = res.x
        for i in range(k):
            line = []
            for j in range(m):
                line.append(str(int(round(x[i*m + j]))))
            print(" ".join(line))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
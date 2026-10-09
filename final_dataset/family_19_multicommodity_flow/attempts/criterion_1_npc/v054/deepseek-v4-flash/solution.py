import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    streams = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        streams.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Variables: x_{i,j} for stream i on edge j
    num_vars = k * m
    
    # Objective: minimize 0 (just feasibility)
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. Capacity constraints: sum_i x_{i,j} <= cap_j
    A_ub = []
    b_ub = []
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])
    
    # 2. Flow conservation for each stream at each node
    A_eq = []
    b_eq = []
    for i in range(k):
        s, t, d = streams[i]
        for node in range(n):
            row = np.zeros(num_vars)
            # outgoing edges
            for j, (u, v, cap) in enumerate(edges):
                if u == node:
                    row[i * m + j] += 1
                if v == node:
                    row[i * m + j] -= 1
            A_eq.append(row)
            if node == s:
                b_eq.append(d)
            elif node == t:
                b_eq.append(-d)
            else:
                b_eq.append(0)
    
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    
    bounds = [(0, None)] * num_vars
    
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if res.success:
        print("YES")
        x = res.x
        for i in range(k):
            line = []
            for j in range(m):
                line.append(int(round(x[i * m + j])))
            print(" ".join(map(str, line)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
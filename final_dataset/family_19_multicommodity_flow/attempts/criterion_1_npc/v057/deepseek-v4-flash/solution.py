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
    
    batches = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        batches.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Number of variables: k * m
    num_vars = k * m
    
    # We'll build A_ub and b_ub for capacity constraints
    A_ub = []
    b_ub = []
    
    # Capacity constraints: for each edge e, sum_i x[i][e] <= cap_e
    for e in range(m):
        row = [0] * num_vars
        for i in range(k):
            row[i * m + e] = 1
        A_ub.append(row)
        b_ub.append(edges[e][2])
    
    # Equality constraints: flow conservation + source/sink
    A_eq = []
    b_eq = []
    
    for i in range(k):
        s, t, d = batches[i]
        for node in range(n):
            row = [0] * num_vars
            # outgoing edges
            for e, (u, v, cap) in enumerate(edges):
                if u == node:
                    row[i * m + e] += 1
                if v == node:
                    row[i * m + e] -= 1
            # source: out - in = d
            # sink: in - out = d => out - in = -d
            if node == s:
                b_eq.append(d)
            elif node == t:
                b_eq.append(-d)
            else:
                b_eq.append(0)
            A_eq.append(row)
    
    # Bounds: all variables >= 0
    bounds = [(0, None)] * num_vars
    
    # Objective: zero vector (feasibility only)
    c = [0] * num_vars
    
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')
    
    if res.status != 0:
        print("NO")
        return
    
    x = res.x
    print("YES")
    for i in range(k):
        line = []
        for e in range(m):
            val = x[i * m + e]
            # Round to nearest integer (should be integer due to integrality of LP if capacities are integers)
            line.append(str(int(round(val))))
        print(" ".join(line))

if __name__ == "__main__":
    solve()
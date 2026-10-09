import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

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
    
    # Variables: x[i][e] = flow of stream i on edge e
    # Total variables = k * m
    num_vars = k * m
    
    # Objective: minimize 0 (just feasibility)
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. Capacity constraints: sum_i x[i][e] <= cap[e] for each edge e
    # 2. Flow conservation for each stream at each node (except source/sink)
    # 3. Demand at source and sink
    
    constraints = []
    lower_bounds = []
    upper_bounds = []
    
    # Capacity constraints
    for e in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + e] = 1
        constraints.append(LinearConstraint(row, -np.inf, edges[e][2]))
    
    # Flow conservation for each stream at each node
    for i in range(k):
        s, t, d = streams[i]
        for node in range(n):
            if node == s or node == t:
                continue
            row = np.zeros(num_vars)
            # outgoing edges
            for e, (u, v, cap) in enumerate(edges):
                if u == node:
                    row[i * m + e] += 1
                if v == node:
                    row[i * m + e] -= 1
            constraints.append(LinearConstraint(row, 0, 0))
    
    # Source constraint: net outflow = d
    for i in range(k):
        s, t, d = streams[i]
        row = np.zeros(num_vars)
        for e, (u, v, cap) in enumerate(edges):
            if u == s:
                row[i * m + e] += 1
            if v == s:
                row[i * m + e] -= 1
        constraints.append(LinearConstraint(row, d, d))
    
    # Sink constraint: net inflow = d
    for i in range(k):
        s, t, d = streams[i]
        row = np.zeros(num_vars)
        for e, (u, v, cap) in enumerate(edges):
            if v == t:
                row[i * m + e] += 1
            if u == t:
                row[i * m + e] -= 1
        constraints.append(LinearConstraint(row, d, d))
    
    # Bounds: all variables >= 0 and integer
    bounds = Bounds(np.zeros(num_vars), np.full(num_vars, np.inf))
    
    integrality = np.ones(num_vars)  # all integer
    
    res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    print("YES")
    for i in range(k):
        row_vals = [int(round(x[i * m + e])) for e in range(m)]
        print(" ".join(map(str, row_vals)))

if __name__ == "__main__":
    solve()
import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    swarms = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        swarms.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Variables: x[i][j] for swarm i, edge j
    num_vars = k * m
    
    # Objective: minimize 0 (feasibility)
    c = np.zeros(num_vars)
    
    # Constraints:
    # 1. Flow conservation for each swarm at each node (except source/sink)
    # 2. Edge capacity: sum_i x[i][j] <= cap_j
    # 3. Source/sink net flow constraints
    
    A_ub = []
    b_ub = []
    A_eq = []
    b_eq = []
    
    # Edge capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])
    
    # Flow conservation for each swarm at each node
    for i in range(k):
        s, t, d = swarms[i]
        for v in range(n):
            if v == s or v == t:
                continue
            row = np.zeros(num_vars)
            # outgoing edges from v
            for j, (u, w, cap) in enumerate(edges):
                if u == v:
                    row[i * m + j] += 1
                if w == v:
                    row[i * m + j] -= 1
            A_eq.append(row)
            b_eq.append(0)
    
    # Source/sink net flow constraints
    for i in range(k):
        s, t, d = swarms[i]
        # source: outflow - inflow = d
        row = np.zeros(num_vars)
        for j, (u, v, cap) in enumerate(edges):
            if u == s:
                row[i * m + j] += 1
            if v == s:
                row[i * m + j] -= 1
        A_eq.append(row)
        b_eq.append(d)
        
        # sink: inflow - outflow = d
        row = np.zeros(num_vars)
        for j, (u, v, cap) in enumerate(edges):
            if v == t:
                row[i * m + j] += 1
            if u == t:
                row[i * m + j] -= 1
        A_eq.append(row)
        b_eq.append(d)
    
    # Bounds: x >= 0
    bounds = [(0, None)] * num_vars
    
    # Solve LP (integrality not needed due to total unimodularity)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')
    
    if res.status != 0:
        print("NO")
        return
    
    x = res.x
    # Round to nearest integer (should be already integral)
    x = np.round(x).astype(int)
    
    # Verify feasibility
    # Check capacities
    for j in range(m):
        total = sum(x[i * m + j] for i in range(k))
        if total > edges[j][2]:
            print("NO")
            return
    
    # Check flow conservation
    for i in range(k):
        s, t, d = swarms[i]
        inflow = [0]*n
        outflow = [0]*n
        for j, (u, v, cap) in enumerate(edges):
            outflow[u] += x[i*m+j]
            inflow[v] += x[i*m+j]
        for v in range(n):
            if v == s:
                if outflow[v] - inflow[v] != d:
                    print("NO")
                    return
            elif v == t:
                if inflow[v] - outflow[v] != d:
                    print("NO")
                    return
            else:
                if inflow[v] != outflow[v]:
                    print("NO")
                    return
    
    print("YES")
    for i in range(k):
        print(' '.join(str(x[i*m+j]) for j in range(m)))

if __name__ == "__main__":
    solve()
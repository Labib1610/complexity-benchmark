import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    consignments = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        consignments.append((s-1, t-1, d))
    corridors = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        corridors.append((u-1, v-1, c))
    
    # Variables: x[i][e] for i in range(k), e in range(m)
    num_vars = k * m
    c_vec = np.zeros(num_vars)  # objective: any feasible
    
    # Constraints:
    # 1. Capacity per corridor: sum_i x[i][e] <= c_e
    # 2. Flow conservation for each consignment at each node (except s,t)
    # 3. Supply/demand at s and t
    
    A = []
    b_low = []
    b_up = []
    
    # Capacity constraints
    for e in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i*m + e] = 1
        A.append(row)
        b_low.append(-np.inf)
        b_up.append(corridors[e][2])
    
    # Flow conservation
    for i in range(k):
        s_i, t_i, d_i = consignments[i]
        for v in range(n):
            if v == s_i or v == t_i:
                continue
            row = np.zeros(num_vars)
            # incoming
            for e, (u, vv, c) in enumerate(corridors):
                if vv == v:
                    row[i*m + e] += 1
                if u == v:
                    row[i*m + e] -= 1
            A.append(row)
            b_low.append(0)
            b_up.append(0)
    
    # Supply at s_i: out - in = d_i
    for i in range(k):
        s_i, t_i, d_i = consignments[i]
        row = np.zeros(num_vars)
        for e, (u, vv, c) in enumerate(corridors):
            if u == s_i:
                row[i*m + e] += 1
            if vv == s_i:
                row[i*m + e] -= 1
        A.append(row)
        b_low.append(d_i)
        b_up.append(d_i)
    
    # Demand at t_i: in - out = d_i
    for i in range(k):
        s_i, t_i, d_i = consignments[i]
        row = np.zeros(num_vars)
        for e, (u, vv, c) in enumerate(corridors):
            if vv == t_i:
                row[i*m + e] += 1
            if u == t_i:
                row[i*m + e] -= 1
        A.append(row)
        b_low.append(d_i)
        b_up.append(d_i)
    
    A = np.array(A)
    constraints = LinearConstraint(A, b_low, b_up)
    bounds = Bounds(0, np.inf)
    
    res = milp(c=c_vec, constraints=constraints, integrality=np.ones(num_vars), bounds=bounds)
    
    if res.success:
        print("YES")
        x = res.x
        for i in range(k):
            line = []
            for e in range(m):
                line.append(int(round(x[i*m + e])))
            print(' '.join(map(str, line)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
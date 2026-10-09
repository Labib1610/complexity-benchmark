import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    tasks = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        tasks.append((s, t, d))
    
    links = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        links.append((u, v, cap))
    
    # Variables: x[i][j] for task i, link j
    num_vars = k * m
    c = np.zeros(num_vars)  # objective: any feasible solution
    
    # Constraints:
    # 1. Link capacity: sum_i x[i][j] <= cap[j]
    # 2. Flow conservation at intermediate nodes for each task
    # 3. Source/destination net flow
    
    constraints = []
    lb = []
    ub = []
    
    # Link capacity constraints
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        constraints.append(row)
        lb.append(-np.inf)
        ub.append(links[j][2])
    
    # Flow conservation for each task and each node
    for i in range(k):
        s, t, d = tasks[i]
        for v in range(n):
            row = np.zeros(num_vars)
            # outgoing links from v
            for j, (u, w, cap) in enumerate(links):
                if u == v:
                    row[i * m + j] += 1
                if w == v:
                    row[i * m + j] -= 1
            # For source: outflow - inflow = d
            # For dest: inflow - outflow = d => outflow - inflow = -d
            if v == s:
                constraints.append(row)
                lb.append(d)
                ub.append(d)
            elif v == t:
                constraints.append(row)
                lb.append(-d)
                ub.append(-d)
            else:
                constraints.append(row)
                lb.append(0)
                ub.append(0)
    
    A = np.array(constraints)
    lc = LinearConstraint(A, lb, ub)
    bounds = Bounds(0, np.inf)
    
    integrality = np.ones(num_vars)  # all integer
    
    res = milp(c=c, constraints=lc, integrality=integrality, bounds=bounds)
    
    if not res.success:
        print("NO")
        return
    
    x = res.x
    print("YES")
    for i in range(k):
        row = [int(round(x[i * m + j])) for j in range(m)]
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    solve()
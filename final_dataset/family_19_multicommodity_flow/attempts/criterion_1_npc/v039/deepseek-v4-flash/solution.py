import sys
import numpy as np
from scipy.optimize import linprog

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    tasks = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        tasks.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Variables: for each task i and edge j, x[i][j]
    num_vars = k * m

    # Objective: none (just feasibility), so zero coefficients
    c = np.zeros(num_vars)

    A_ub = []
    b_ub = []

    # Capacity constraints: sum over tasks for each edge <= cap
    for j in range(m):
        row = np.zeros(num_vars)
        for i in range(k):
            row[i * m + j] = 1
        A_ub.append(row)
        b_ub.append(edges[j][2])

    # Conservation constraints for each task and each node (except source/dest)
    # outflow - inflow = 0 for intermediate nodes; = d for source; = -d for dest
    for i in range(k):
        s, t, d = tasks[i]
        for v in range(n):
            row = np.zeros(num_vars)
            for j, (u, w, _) in enumerate(edges):
                if u == v:
                    row[i * m + j] += 1
                if w == v:
                    row[i * m + j] -= 1
            if v == s:
                A_ub.append(row)
                b_ub.append(d)  # exactly d net outflow — but as inequality?
                # Actually it's equality, so use A_eq
            elif v == t:
                # net inflow = d => outflow - inflow = -d
                pass
            else:
                A_ub.append(row)
                b_ub.append(0)  # net 0

    # We need equalities for source/dest balances
    A_eq = []
    b_eq = []
    for i in range(k):
        s, t, d = tasks[i]
        row_s = np.zeros(num_vars)
        row_t = np.zeros(num_vars)
        for j, (u, w, _) in enumerate(edges):
            if u == s:
                row_s[i * m + j] += 1
            if w == s:
                row_s[i * m + j] -= 1
            if u == t:
                row_t[i * m + j] += 1
            if w == t:
                row_t[i * m + j] -= 1
        A_eq.append(row_s)
        b_eq.append(d)
        A_eq.append(row_t)
        b_eq.append(-d)

    bounds = [(0, None)] * num_vars

    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method='highs')

    if res.success:
        x = res.x
        # Round to nearest integers (should be nearly integer)
        flow = np.rint(x).astype(int)
        # Verify constraints
        # capacities
        for j in range(m):
            total = sum(flow[i * m + j] for i in range(k))
            if total > edges[j][2]:
                print("NO")
                return
        # conservation
        for i in range(k):
            s, t, d = tasks[i]
            net = [0]*n
            for j,(u,w,_) in enumerate(edges):
                net[u] += flow[i*m+j]
                net[w] -= flow[i*m+j]
            if net[s] != d or net[t] != -d:
                print("NO")
                return
            for v in range(n):
                if v != s and v != t and net[v] != 0:
                    print("NO")
                    return
        print("YES")
        for i in range(k):
            print(" ".join(str(flow[i*m+j]) for j in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
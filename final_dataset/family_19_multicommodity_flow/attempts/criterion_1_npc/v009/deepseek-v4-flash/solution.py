import sys
import pulp

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
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
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    prob = pulp.LpProblem("Dispatch", pulp.LpMinimize)
    
    # Variables: x[i][j] = flow of product i on edge j
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer') for j in range(m)] for i in range(k)]
    
    # Objective: dummy (feasibility only)
    prob += 0
    
    # Capacity constraints
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= edges[j][2], f"cap_{j}"
    
    # Flow conservation for each product
    for i in range(k):
        s, t, d = products[i]
        for v in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][1] == v)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][0] == v)
            if v == s:
                prob += outflow - inflow == d, f"prod_{i}_src_{v}"
            elif v == t:
                prob += inflow - outflow == d, f"prod_{i}_dst_{v}"
            else:
                prob += inflow - outflow == 0, f"prod_{i}_mid_{v}"
    
    # Solve
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[status] != 'Optimal':
        print("NO")
        return
    
    print("YES")
    for i in range(k):
        row = []
        for j in range(m):
            row.append(str(int(x[i][j].value())))
        print(" ".join(row))

if __name__ == "__main__":
    solve()
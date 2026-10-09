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
    
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
    
    tubes = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        tubes.append((u, v, cap))
    
    prob = pulp.LpProblem("PneumaticRouting", pulp.LpMinimize)
    
    # Variables: x[i][j] = flow of order i on tube j
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer') for j in range(m)] for i in range(k)]
    
    # Objective: dummy (feasibility only)
    prob += 0
    
    # Flow conservation for each order
    for i, (s, t, d) in enumerate(orders):
        # For each vat, compute net flow
        for v in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if tubes[j][1] == v)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if tubes[j][0] == v)
            if v == s:
                prob += (outflow - inflow == d)
            elif v == t:
                prob += (inflow - outflow == d)
            else:
                prob += (inflow - outflow == 0)
    
    # Capacity constraints on each tube
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= tubes[j][2]
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[prob.status] == 'Optimal':
        print("YES")
        for i in range(k):
            print(' '.join(str(int(pulp.value(x[i][j]))) for j in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
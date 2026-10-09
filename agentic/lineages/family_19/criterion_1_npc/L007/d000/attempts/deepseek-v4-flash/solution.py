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
    
    belts = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        belts.append((u, v, cap))
    
    # Create LP problem
    prob = pulp.LpProblem("ParcelDistribution", pulp.LpMinimize)
    
    # Variables: x[i][j] = flow of order i on belt j
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer') for j in range(m)] for i in range(k)]
    
    # Objective: dummy (feasibility)
    prob += 0
    
    # Constraints: flow conservation for each order
    for i, (s, t, d) in enumerate(orders):
        # For each desk, net flow = 0 except start (+d) and end (-d)
        for desk in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if belts[j][1] == desk)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if belts[j][0] == desk)
            if desk == s:
                prob += (outflow - inflow == d)
            elif desk == t:
                prob += (inflow - outflow == d)
            else:
                prob += (inflow - outflow == 0)
    
    # Capacity constraints on belts
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= belts[j][2]
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[prob.status] == 'Optimal':
        print("YES")
        for i in range(k):
            row = [str(int(x[i][j].value())) for j in range(m)]
            print(" ".join(row))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
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
    
    # Variables: x[i][j]
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer') for j in range(m)] for i in range(k)]
    
    # Objective: dummy (0)
    prob += 0
    
    # Flow conservation constraints
    for i, (s, t, d) in enumerate(orders):
        # For each node
        for node in range(n):
            inflow = pulp.lpSum(x[i][j] for j, (u, v, cap) in enumerate(tubes) if v == node)
            outflow = pulp.lpSum(x[i][j] for j, (u, v, cap) in enumerate(tubes) if u == node)
            if node == s:
                prob += (outflow - inflow == d), f"origin_{i}_{node}"
            elif node == t:
                prob += (inflow - outflow == d), f"dest_{i}_{node}"
            else:
                prob += (inflow - outflow == 0), f"mid_{i}_{node}"
    
    # Capacity constraints
    for j, (u, v, cap) in enumerate(tubes):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= cap, f"cap_{j}"
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[prob.status] == 'Optimal':
        print("YES")
        for i in range(k):
            print(" ".join(str(int(x[i][j].value())) for j in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
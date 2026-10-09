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
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Create LP problem
    prob = pulp.LpProblem("FreightDispatch", pulp.LpMinimize)
    
    # Variables: x[i][j] = flow of order i on edge j
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer') for j in range(m)] for i in range(k)]
    
    # Objective: dummy (feasibility only)
    prob += 0
    
    # Capacity constraints
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= edges[j][2], f"cap_{j}"
    
    # Flow conservation for each order
    for i, (s, t, d) in enumerate(orders):
        # For each node, inflow - outflow = 0 except at source and sink
        for node in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][1] == node)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][0] == node)
            if node == s:
                prob += outflow - inflow == d, f"src_{i}_{node}"
            elif node == t:
                prob += inflow - outflow == d, f"dst_{i}_{node}"
            else:
                prob += inflow - outflow == 0, f"mid_{i}_{node}"
    
    # Solve
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[status] != 'Optimal':
        print("NO")
        return
    
    print("YES")
    for i in range(k):
        row = [str(int(x[i][j].value())) for j in range(m)]
        print(" ".join(row))

if __name__ == "__main__":
    solve()
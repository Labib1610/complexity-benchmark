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
    
    contracts = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        contracts.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
    
    # Create LP problem
    prob = pulp.LpProblem("Dispatch", pulp.LpMaximize)
    
    # Variables: x[i][j] = flow of contract i on edge j
    x = []
    for i in range(k):
        row = []
        for j in range(m):
            var = pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer')
            row.append(var)
        x.append(row)
    
    # Objective: dummy (feasibility)
    prob += 0
    
    # Edge capacity constraints
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= edges[j][2], f"cap_{j}"
    
    # Flow conservation for each contract
    for i, (s, t, d) in enumerate(contracts):
        # For each node, net flow = 0 except source and sink
        for node in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][1] == node)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][0] == node)
            if node == s:
                prob += outflow - inflow == d, f"src_{i}_{node}"
            elif node == t:
                prob += inflow - outflow == d, f"sink_{i}_{node}"
            else:
                prob += inflow - outflow == 0, f"mid_{i}_{node}"
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[prob.status] != 'Optimal':
        print("NO")
        return
    
    print("YES")
    for i in range(k):
        line = []
        for j in range(m):
            line.append(str(int(x[i][j].value())))
        print(" ".join(line))

if __name__ == "__main__":
    solve()
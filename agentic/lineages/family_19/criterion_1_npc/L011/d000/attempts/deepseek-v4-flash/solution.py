import sys
import pulp

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
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
    
    prob = pulp.LpProblem("Routing", pulp.LpMinimize)
    
    # Variables: x[i][j]
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat=pulp.LpInteger) for j in range(m)] for i in range(k)]
    
    # Objective: dummy (feasibility)
    prob += 0
    
    # Edge capacity constraints
    for j in range(m):
        prob += pulp.lpSum(x[i][j] for i in range(k)) <= edges[j][2]
    
    # Flow conservation for each contract
    for i in range(k):
        s, t, d = contracts[i]
        # For each node v
        for v in range(n):
            inflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][1] == v)
            outflow = pulp.lpSum(x[i][j] for j in range(m) if edges[j][0] == v)
            if v == s:
                prob += outflow - inflow == d
            elif v == t:
                prob += inflow - outflow == d
            else:
                prob += inflow - outflow == 0
    
    # Solve
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    if pulp.LpStatus[status] != "Optimal":
        print("NO")
    else:
        print("YES")
        for i in range(k):
            row = [str(int(x[i][j].value())) for j in range(m)]
            print(" ".join(row))

if __name__ == "__main__":
    main()
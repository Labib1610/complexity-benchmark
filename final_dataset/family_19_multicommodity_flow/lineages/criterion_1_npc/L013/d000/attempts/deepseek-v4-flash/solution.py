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

    compounds = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        compounds.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    prob = pulp.LpProblem("ManifoldRouting", pulp.LpMinimize)

    # Variables: x[i][e] for compound i, edge e
    x = [[pulp.LpVariable(f"x_{i}_{e}", lowBound=0, cat='Integer') for e in range(m)] for i in range(k)]

    # Edge capacity constraints
    for e in range(m):
        prob += pulp.lpSum(x[i][e] for i in range(k)) <= edges[e][2], f"cap_{e}"

    # Flow conservation for each compound and node
    for i, (s, t, d) in enumerate(compounds):
        for v in range(n):
            inflow = pulp.lpSum(x[i][e] for e in range(m) if edges[e][1] == v)
            outflow = pulp.lpSum(x[i][e] for e in range(m) if edges[e][0] == v)
            if v == s:
                prob += outflow - inflow == d, f"source_{i}_{v}"
            elif v == t:
                prob += inflow - outflow == d, f"sink_{i}_{v}"
            else:
                prob += inflow - outflow == 0, f"balance_{i}_{v}"

    # Solve
    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[status] != 'Optimal':
        print("NO")
        return

    print("YES")
    for i in range(k):
        line = []
        for e in range(m):
            val = int(pulp.value(x[i][e]))
            line.append(str(val))
        print(" ".join(line))

if __name__ == "__main__":
    solve()